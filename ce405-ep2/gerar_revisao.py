# -*- coding: utf-8 -*-
"""
Gera o sumário de revisão da lista de Economia Política II em Markdown e PDF.

Uso:
    pip install reportlab
    python3 ce405-ep2/gerar_revisao.py

Saídas:
    ce405-ep2/REVISAO.md            leitura no GitHub e no celular
    ce405-ep2/revisao-ce405.pdf     versão para imprimir e revisar antes da prova

Para cada questão o sumário traz o esqueleto da resposta em tópicos, a lista do
que precisa aparecer na folha para garantir nota máxima, e os erros frequentes
que derrubam a nota.
"""
import glob
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, HRFlowable, KeepTogether, PageBreak, PageTemplate,
    Paragraph, Spacer, Table, TableStyle,
)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from revisao import (  # noqa: E402
    ERROS_TRANSVERSAIS, ESTRATEGIA, FORMULAS, MAPA, NUMEROS_Q6, REVISAO,
)

AQUI = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(AQUI, 'REVISAO.md')
PDF = os.path.join(AQUI, 'revisao-ce405.pdf')


# ------------------------------------------------------------------- tipografia
def _fonte(*nomes):
    """Devolve o caminho do primeiro arquivo de fonte encontrado."""
    for nome in nomes:
        for padrao in ('/usr/share/fonts/**/%s' % nome,
                       '/usr/local/share/fonts/**/%s' % nome,
                       os.path.expanduser('~/.fonts/**/%s' % nome)):
            achados = glob.glob(padrao, recursive=True)
            if achados:
                return achados[0]
    return None


BASE = 'Helvetica'
_mapa_fontes = [('NotoSans-Regular.ttf', ''), ('NotoSans-Bold.ttf', '-Bold'),
                ('NotoSans-Italic.ttf', '-Italic'),
                ('NotoSans-BoldItalic.ttf', '-BoldItalic')]
_caminhos = [(suf, _fonte(arq)) for arq, suf in _mapa_fontes]
if all(c for _, c in _caminhos):
    BASE = 'Noto'
    for suf, caminho in _caminhos:
        pdfmetrics.registerFont(TTFont(BASE + suf, caminho))
    pdfmetrics.registerFontFamily(BASE, normal=BASE, bold=BASE + '-Bold',
                                  italic=BASE + '-Italic',
                                  boldItalic=BASE + '-BoldItalic')

# Noto Sans não cobre alguns símbolos (≈, ✓, ✗, →). Troca pelos disponíveis.
SUBSTITUICOES = {'≈': '~'}

# Marcadores escolhidos entre os glifos que a fonte tem. O '[ ]' do checklist
# serve também para o aluno ir marcando à caneta durante a revisão.
MARCA_TOPICO = '\u2022'   # bullet
MARCA_CHECK = '[  ]'      # checklist de nota máxima
MARCA_ERRO = '\u00d7'     # sinal de multiplicação, lido como cruz

NAVY = colors.HexColor('#17365D')
BLUE = colors.HexColor('#1F4E79')
GREEN = colors.HexColor('#2E7D32')
RED = colors.HexColor('#A61C00')
GRAY = colors.HexColor('#555555')
DARK = colors.HexColor('#202124')
BG_NOTA = colors.HexColor('#EAF4EA')
BR_NOTA = colors.HexColor('#9CC69C')
BG_ERRO = colors.HexColor('#FCE8E2')
BR_ERRO = colors.HexColor('#E0A99A')
BG_CAB = colors.HexColor('#EAF2F8')
BORDER = colors.HexColor('#AAB7C4')

PAGE_W, PAGE_H = A4
LEFT = RIGHT = 1.5 * cm
TOP = 1.5 * cm
BOTTOM = 1.4 * cm
CONTENT_W = PAGE_W - LEFT - RIGHT

estilos = getSampleStyleSheet()


def _add(nome, **kw):
    estilos.add(ParagraphStyle(name=nome, **kw))


_add('Capa', parent=estilos['Title'], fontName=BASE + '-Bold', fontSize=22, leading=27,
     alignment=TA_CENTER, textColor=NAVY, spaceAfter=12)
_add('CapaSub', parent=estilos['Normal'], fontName=BASE, fontSize=11.5, leading=17,
     alignment=TA_CENTER, textColor=GRAY, spaceAfter=6)
_add('H1', parent=estilos['Heading1'], fontName=BASE + '-Bold', fontSize=14, leading=18,
     textColor=NAVY, spaceBefore=10, spaceAfter=6, keepWithNext=True)
_add('QTit', parent=estilos['Heading2'], fontName=BASE + '-Bold', fontSize=11.5, leading=15,
     textColor=colors.white, spaceBefore=0, spaceAfter=0)
_add('Grupo', parent=estilos['Heading3'], fontName=BASE + '-Bold', fontSize=9.6, leading=12.5,
     textColor=BLUE, spaceBefore=5, spaceAfter=2, keepWithNext=True)
_add('Corpo', parent=estilos['BodyText'], fontName=BASE, fontSize=8.8, leading=12.2,
     textColor=DARK, alignment=TA_JUSTIFY, spaceAfter=2)
_add('Item', parent=estilos['BodyText'], fontName=BASE, fontSize=8.8, leading=12.2,
     textColor=DARK, alignment=TA_JUSTIFY, leftIndent=11, firstLineIndent=-7, spaceAfter=2.5)
_add('Pede', parent=estilos['BodyText'], fontName=BASE + '-Italic', fontSize=8.8,
     leading=12, textColor=GRAY, spaceAfter=3)
_add('BoxTitNota', parent=estilos['BodyText'], fontName=BASE + '-Bold', fontSize=9.2,
     leading=12, textColor=GREEN, spaceAfter=3)
_add('BoxTitErro', parent=estilos['BodyText'], fontName=BASE + '-Bold', fontSize=9.2,
     leading=12, textColor=RED, spaceAfter=3)
_add('Peq', parent=estilos['BodyText'], fontName=BASE, fontSize=7.6, leading=10.4,
     textColor=GRAY, spaceAfter=2)


def esc(texto):
    """Escapa XML e converte **negrito** e *itálico* nas tags do ReportLab."""
    for de, para in SUBSTITUICOES.items():
        texto = texto.replace(de, para)
    texto = (texto.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
    texto = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', texto)
    texto = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', texto)
    return texto


def P(texto, estilo='Corpo'):
    return Paragraph(esc(texto), estilos[estilo])


def item(texto, marca=MARCA_TOPICO, estilo='Item'):
    return Paragraph(marca + '  ' + esc(texto), estilos[estilo])


def caixa(titulo, linhas, bg, borda, estilo_titulo, marca=MARCA_TOPICO):
    """
    Caixa colorida com título e itens.

    Usa uma linha de tabela por item, e não uma célula única com a lista dentro.
    Célula única não quebra entre páginas, e quando a caixa não cabia no resto da
    folha ela pulava inteira para a página seguinte, deixando um vazio enorme.
    Com uma linha por item a caixa divide e o texto flui.
    """
    dados = [[P(titulo, estilo_titulo)]] + [[item(l, marca)] for l in linhas]
    t = Table(dados, colWidths=[CONTENT_W], splitByRow=1, hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('BOX', (0, 0), (-1, -1), .7, borda),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 6),
    ]))
    return t


def faixa_questao(entrada):
    texto = 'Q%d  (cap. %s)   %s' % (entrada['q'], entrada['cap'], entrada['titulo'])
    t = Table([[Paragraph(esc(texto), estilos['QTit'])]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), NAVY),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    return t


def tabela(dados, larguras):
    t = Table(dados, colWidths=larguras, repeatRows=1, hAlign='LEFT')
    cmds = [
        ('GRID', (0, 0), (-1, -1), .35, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('BACKGROUND', (0, 0), (-1, 0), BG_CAB),
    ]
    t.setStyle(TableStyle(cmds))
    return t


def cabecalho_rodape(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(colors.HexColor('#D2D9DF'))
        canvas.setLineWidth(.5)
        canvas.line(LEFT, PAGE_H - 1.0 * cm, PAGE_W - RIGHT, PAGE_H - 1.0 * cm)
        canvas.setFont(BASE + '-Bold', 7.4)
        canvas.setFillColor(NAVY)
        canvas.drawString(LEFT, PAGE_H - .75 * cm, 'Economia Política II  |  Revisão da Lista I')
        canvas.setFont(BASE, 7.4)
        canvas.setFillColor(GRAY)
        canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - .75 * cm,
                               'O Capital, Livro I (Boitempo)')
    canvas.setStrokeColor(colors.HexColor('#D2D9DF'))
    canvas.setLineWidth(.5)
    canvas.line(LEFT, .9 * cm, PAGE_W - RIGHT, .9 * cm)
    canvas.setFont(BASE, 7.4)
    canvas.setFillColor(GRAY)
    canvas.drawString(LEFT, .6 * cm, 'CE405, turma C')
    canvas.drawRightString(PAGE_W - RIGHT, .6 * cm, str(doc.page))
    canvas.restoreState()


# ---------------------------------------------------------------------- PDF
def escrever_pdf():
    S = []

    S += [Spacer(1, 1.6 * cm),
          P('Sumário de revisão', 'Capa'),
          P('Lista de Questões I de Economia Política II', 'CapaSub'),
          P('CE405, turma C, 2025', 'CapaSub'),
          Spacer(1, .5 * cm),
          HRFlowable(width='70%', thickness=1.5, color=BLUE, hAlign='CENTER'),
          Spacer(1, .5 * cm),
          P('Marx, O Capital, Livro I, edição Boitempo', 'CapaSub'),
          P('20 questões, com esqueleto da resposta em tópicos, critérios para nota '
            'máxima e erros que derrubam a nota', 'CapaSub'),
          Spacer(1, .8 * cm)]

    S += [P('Mapa dos capítulos', 'H1')]
    dados = [['Cap.', 'Título', 'Questões']]
    dados += [[P(c, 'Corpo'), P(t, 'Corpo'), P(q, 'Corpo')] for c, t, q in MAPA]
    S += [tabela(dados, [1.3 * cm, CONTENT_W - 5.4 * cm, 4.1 * cm])]

    S += [P('Fórmulas que não podem falhar', 'H1')]
    dados = [['Grandeza', 'Fórmula', 'Observação']]
    dados += [[P(g, 'Corpo'), P('**%s**' % f, 'Corpo'), P(o, 'Corpo')]
              for g, f, o in FORMULAS]
    S += [tabela(dados, [3.9 * cm, 6.2 * cm, CONTENT_W - 10.1 * cm])]

    S += [P('Números da questão 6, para conferir de cabeça', 'H1')]
    pares = [[P('**%s**' % g, 'Corpo'), P(v, 'Corpo')] for g, v in NUMEROS_Q6]
    meio = (len(pares) + 1) // 2
    esq, dir_ = pares[:meio], pares[meio:]
    while len(dir_) < len(esq):
        dir_.append([P('', 'Corpo'), P('', 'Corpo')])
    dados = [['Grandeza', 'Valor', 'Grandeza', 'Valor']]
    dados += [esq[i] + dir_[i] for i in range(len(esq))]
    col = (CONTENT_W - 2 * 2.2 * cm) / 2
    S += [tabela(dados, [col, 2.2 * cm, col, 2.2 * cm])]

    S += [PageBreak()]

    for entrada in REVISAO:
        bloco = [faixa_questao(entrada), Spacer(1, 3),
                 P('**O que pede.** ' + entrada['pede'], 'Pede')]
        for titulo_grupo, itens in entrada['topicos']:
            bloco.append(P(titulo_grupo, 'Grupo'))
            bloco += [item(i) for i in itens]
        S += [KeepTogether(bloco[:4])] + bloco[4:]
        S += [Spacer(1, 5),
              caixa('Para nota máxima', entrada['nota_maxima'],
                    BG_NOTA, BR_NOTA, 'BoxTitNota', marca=MARCA_CHECK),
              Spacer(1, 4),
              caixa('Erros que derrubam a nota', entrada['erros'],
                    BG_ERRO, BR_ERRO, 'BoxTitErro', marca=MARCA_ERRO),
              Spacer(1, 10)]

    S += [PageBreak(),
          P('Erros transversais, valem para toda a prova', 'H1')]
    S += [item(e) for e in ERROS_TRANSVERSAIS]
    S += [Spacer(1, 8), P('Estratégia para as 2 horas', 'H1')]
    S += [item(e) for e in ESTRATEGIA]

    doc = BaseDocTemplate(PDF, pagesize=A4, leftMargin=LEFT, rightMargin=RIGHT,
                          topMargin=TOP, bottomMargin=BOTTOM,
                          title='Revisão da Lista I de Economia Política II',
                          author='Kiro')
    frame = Frame(LEFT, BOTTOM, CONTENT_W, PAGE_H - TOP - BOTTOM, id='n')
    doc.addPageTemplates([PageTemplate(id='main', frames=[frame],
                                       onPage=cabecalho_rodape)])
    doc.build(S)
    return PDF


# ----------------------------------------------------------------- Markdown
def escrever_markdown():
    L = ['# Sumário de revisão, Lista de Questões I de Economia Política II',
         '',
         'CE405, turma C, 2025. Referência: MARX, Karl. *O Capital*, Livro I '
         '(ed. Boitempo).',
         '',
         'Para cada questão: esqueleto da resposta em tópicos, o que precisa aparecer na '
         'folha para garantir nota máxima, e os erros que derrubam a nota.',
         '']

    L += ['## Mapa dos capítulos', '', '| Cap. | Título | Questões |', '|---|---|---|']
    L += ['| %s | %s | %s |' % (c, t, q) for c, t, q in MAPA]

    L += ['', '## Fórmulas que não podem falhar', '',
          '| Grandeza | Fórmula | Observação |', '|---|---|---|']
    L += ['| %s | `%s` | %s |' % (g, f, o) for g, f, o in FORMULAS]

    L += ['', '## Números da questão 6', '', '| Grandeza | Valor |', '|---|---|']
    L += ['| %s | %s |' % (g, v) for g, v in NUMEROS_Q6]

    L += ['', '---', '']
    for e in REVISAO:
        L += ['## Q%d (cap. %s) %s' % (e['q'], e['cap'], e['titulo']), '',
              '**O que pede.** %s' % e['pede'], '']
        for titulo_grupo, itens in e['topicos']:
            L += ['### ' + titulo_grupo, '']
            L += ['- ' + i for i in itens]
            L.append('')
        L += ['**Para nota máxima**', '']
        L += ['- [ ] ' + c for c in e['nota_maxima']]
        L += ['', '**Erros que derrubam a nota**', '']
        L += ['- ' + c for c in e['erros']]
        L += ['', '---', '']

    L += ['## Erros transversais, valem para toda a prova', '']
    L += ['- ' + e for e in ERROS_TRANSVERSAIS]
    L += ['', '## Estratégia para as 2 horas', '']
    L += ['%d. %s' % (i + 1, e) for i, e in enumerate(ESTRATEGIA)]
    L.append('')

    with open(MD, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(L))
    return MD


if __name__ == '__main__':
    print('fonte do PDF:', BASE)
    print('questões:', len(REVISAO))
    print('markdown ->', escrever_markdown())
    print('pdf      ->', escrever_pdf())
    topicos = sum(len(i) for e in REVISAO for _, i in e['topicos'])
    print()
    print('tópicos: %d | critérios de nota máxima: %d | erros mapeados: %d'
          % (topicos,
             sum(len(e['nota_maxima']) for e in REVISAO),
             sum(len(e['erros']) for e in REVISAO) + len(ERROS_TRANSVERSAIS)))
