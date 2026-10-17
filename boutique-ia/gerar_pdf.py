#!/usr/bin/env python3
"""
Agrega o material da boutique de IA em um único PDF.

Entrada
  guia-boutique-ia-cold-chain.md   corpo principal, doze partes
  prompt-guia-boutique-ia.md       anexo A
  README.md                        anexo B

Saída
  guia-boutique-ia-cold-chain.pdf  com capa, sumário paginado, cabeçalho e rodapé

Uso
  python3 gerar_pdf.py

Dependências
  reportlab e fonttools. No sandbox foi usado um venv em /projects/sandbox/.venv-pdf
  porque o site-packages do sistema é somente leitura.

As fontes variáveis Noto Sans e JetBrains Mono são instanciadas em pesos estáticos
dentro de .fonts/ no momento do build, porque o reportlab não lê eixo variável.
"""
import os
import re
import sys

from fontTools.ttLib import TTFont as FTFont
from fontTools.varLib.instancer import instantiateVariableFont

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, CondPageBreak, Frame, HRFlowable, ListFlowable, ListItem,
    NextPageTemplate, PageBreak, PageTemplate, Paragraph, Spacer, Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = os.path.dirname(os.path.abspath(__file__))
FONT_CACHE = os.path.join(ROOT, '.fonts')
os.makedirs(FONT_CACHE, exist_ok=True)

TITULO = 'Boutique de IA · Projeto Cold Chain'
SUBTITULO = ('Escopo do projeto, fundamentos de cadeia do frio, desenho do '
             'playbook da área e plano de implementação conjunta')
AUTOR = 'Matteo Lucato'
DATA = 'Outubro de 2026'
SAIDA = os.path.join(ROOT, 'guia-boutique-ia-cold-chain.pdf')


# ---------------------------------------------------------------- fontes ----
VAR_SANS = '/usr/share/fonts/google-noto-vf/NotoSans[wght].ttf'
VAR_SANS_IT = '/usr/share/fonts/google-noto-vf/NotoSans-Italic[wght].ttf'
VAR_MONO = os.path.join(ROOT, os.pardir, 'decade-stories', 'fonts',
                        'JetBrainsMono[wght].ttf')


def _instanciar(origem, peso, destino):
    """Congela uma fonte variável em um peso fixo e devolve o caminho."""
    alvo = os.path.join(FONT_CACHE, destino)
    if os.path.exists(alvo):
        return alvo
    fonte = FTFont(origem)
    instantiateVariableFont(fonte, {'wght': peso}, inplace=True,
                            updateFontNames=False)
    fonte.save(alvo)
    return alvo


def registrar_fontes():
    base, mono = 'Noto', 'Mono'
    pdfmetrics.registerFont(TTFont(base, _instanciar(VAR_SANS, 400, 'noto-400.ttf')))
    pdfmetrics.registerFont(TTFont(base + '-Bold', _instanciar(VAR_SANS, 700, 'noto-700.ttf')))
    pdfmetrics.registerFont(TTFont(base + '-Italic', _instanciar(VAR_SANS_IT, 400, 'noto-it-400.ttf')))
    pdfmetrics.registerFont(TTFont(base + '-BoldItalic', _instanciar(VAR_SANS_IT, 700, 'noto-it-700.ttf')))
    pdfmetrics.registerFontFamily(base, normal=base, bold=base + '-Bold',
                                  italic=base + '-Italic',
                                  boldItalic=base + '-BoldItalic')
    if os.path.exists(VAR_MONO):
        pdfmetrics.registerFont(TTFont(mono, _instanciar(VAR_MONO, 400, 'mono-400.ttf')))
    else:
        mono = base
    return base, mono


BASE, MONO = registrar_fontes()

# --------------------------------------------------------------- estilos ----
PAGE_W, PAGE_H = A4
LEFT = RIGHT = 2.1 * cm
TOP = 2.0 * cm
BOTTOM = 1.9 * cm
CONTENT_W = PAGE_W - LEFT - RIGHT

NAVY = colors.HexColor('#15314B')
AZUL = colors.HexColor('#1F6FB2')
GELO = colors.HexColor('#EEF4F9')
CINZA = colors.HexColor('#5A6672')
LINHA = colors.HexColor('#C8D6E2')
TEXTO = colors.HexColor('#1B1F23')

E = {}
E['corpo'] = ParagraphStyle('corpo', fontName=BASE, fontSize=9.4, leading=14.4,
                            textColor=TEXTO, alignment=TA_JUSTIFY,
                            spaceAfter=6.5)
E['h1'] = ParagraphStyle('h1', fontName=BASE + '-Bold', fontSize=19, leading=23,
                         textColor=NAVY, spaceBefore=0, spaceAfter=3)
E['h2'] = ParagraphStyle('h2', fontName=BASE + '-Bold', fontSize=13.2,
                         leading=17, textColor=NAVY, spaceBefore=13,
                         spaceAfter=5)
E['h3'] = ParagraphStyle('h3', fontName=BASE + '-Bold', fontSize=10.4,
                         leading=14, textColor=AZUL, spaceBefore=10,
                         spaceAfter=3.5)
E['sub'] = ParagraphStyle('sub', parent=E['corpo'], fontName=BASE + '-Bold',
                          textColor=NAVY, alignment=TA_LEFT, spaceBefore=7,
                          spaceAfter=3)
E['item'] = ParagraphStyle('item', parent=E['corpo'], spaceAfter=3.2,
                           alignment=TA_LEFT)
E['quote'] = ParagraphStyle('quote', parent=E['corpo'], fontName=BASE + '-Italic',
                            leftIndent=0.7 * cm, rightIndent=0.4 * cm,
                            textColor=NAVY, alignment=TA_LEFT,
                            spaceBefore=4, spaceAfter=8)
E['celula'] = ParagraphStyle('celula', fontName=BASE, fontSize=8.1, leading=11,
                             textColor=TEXTO, alignment=TA_LEFT)
E['celula_h'] = ParagraphStyle('celula_h', parent=E['celula'],
                               fontName=BASE + '-Bold', textColor=colors.white)
E['capa_rotulo'] = ParagraphStyle('capa_rotulo', fontName=BASE + '-Bold',
                                  fontSize=9, leading=12, textColor=AZUL)
E['capa_titulo'] = ParagraphStyle('capa_titulo', fontName=BASE + '-Bold',
                                  fontSize=30, leading=35, textColor=NAVY)
E['capa_sub'] = ParagraphStyle('capa_sub', fontName=BASE, fontSize=12.5,
                               leading=18, textColor=CINZA)
E['capa_meta'] = ParagraphStyle('capa_meta', fontName=BASE + '-Bold',
                                fontSize=10, leading=14, textColor=NAVY)
E['nota'] = ParagraphStyle('nota', fontName=BASE, fontSize=8.3, leading=12,
                           textColor=CINZA, alignment=TA_LEFT)
E['codigo'] = ParagraphStyle('codigo', fontName=MONO, fontSize=8.3, leading=12.5,
                             textColor=NAVY, alignment=TA_LEFT)
E['toc1'] = ParagraphStyle('toc1', fontName=BASE + '-Bold', fontSize=9.8,
                           leading=15, textColor=NAVY, spaceBefore=6)
E['toc2'] = ParagraphStyle('toc2', fontName=BASE, fontSize=9.2, leading=14,
                           textColor=TEXTO, leftIndent=0.5 * cm)
E['toc3'] = ParagraphStyle('toc3', fontName=BASE, fontSize=8.4, leading=12.5,
                           textColor=CINZA, leftIndent=1.1 * cm)


# ------------------------------------------------------- markdown inline ----
TOKEN = re.compile(
    r'(\[[^\]]+\]\([^)]+\)'      # link
    r'|`[^`]+`'                   # código
    r'|\*\*[^*]+\*\*'             # negrito
    r')'
)


def _esc(txt):
    return (txt.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def inline(txt):
    """Converte markdown inline em marcação do reportlab."""
    saida = []
    for parte in TOKEN.split(txt):
        if not parte:
            continue
        if parte.startswith('[') and '](' in parte:
            rotulo, url = parte[1:].split('](', 1)
            url = url.rstrip(')')
            saida.append(
                f'<link href="{_esc(url)}" color="#1F6FB2">{_esc(rotulo)}</link>')
        elif parte.startswith('`') and parte.endswith('`'):
            saida.append(f'<font face="{MONO}" size="8.6" color="#15314B">'
                         f'{_esc(parte[1:-1])}</font>')
        elif parte.startswith('**') and parte.endswith('**'):
            saida.append(f'<b>{_esc(parte[2:-2])}</b>')
        else:
            saida.append(_esc(parte))
    return ''.join(saida)


# -------------------------------------------------------- markdown bloco ----
def _limpar(txt):
    txt = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', txt)
    return re.sub(r'[`*]', '', txt)


def _larguras(linhas, tam=8.1, pad=11.0):
    """
    Distribui a largura das colunas garantindo que nenhuma palavra seja quebrada.

    Primeiro reserva, para cada coluna, a largura da maior palavra que ela contém.
    O espaço restante é repartido na proporção do volume de texto de cada coluna,
    que é o que evita coluna de prosa comprimida ao lado de coluna de uma letra.
    """
    n = len(linhas[0])
    minimos, folga = [], []
    for i in range(n):
        # Célula com trecho em código é medida na fonte mono, que é mais larga.
        medidas = [(_limpar(l[i]),
                    (MONO, 8.6) if '`' in l[i] else (BASE + '-Bold', tam))
                   for l in linhas]
        palavra = max(
            [pdfmetrics.stringWidth(p, f, s)
             for t, (f, s) in medidas for p in t.split()] or [0])
        inteiro = max(pdfmetrics.stringWidth(t, f, s) for t, (f, s) in medidas)
        textos = [t for t, _ in medidas]
        minimos.append(min(palavra + pad, CONTENT_W * 0.42))
        folga.append(max(inteiro - palavra, 1.0))

    soma = sum(minimos)
    if soma >= CONTENT_W:
        return [CONTENT_W * m / soma for m in minimos]
    sobra = CONTENT_W - soma
    peso_total = sum(f ** 0.8 for f in folga)
    return [m + sobra * (f ** 0.8) / peso_total
            for m, f in zip(minimos, folga)]


def tabela(linhas):
    dados = [[Paragraph(inline(c), E['celula_h'] if i == 0 else E['celula'])
              for c in linha] for i, linha in enumerate(linhas)]
    t = Table(dados, colWidths=_larguras(linhas), repeatRows=1, hAlign='LEFT')
    estilo = [
        ('BACKGROUND', (0, 0), (-1, 0), NAVY),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('LINEBELOW', (0, 0), (-1, -2), 0.4, LINHA),
        ('BOX', (0, 0), (-1, -1), 0.5, LINHA),
    ]
    for r in range(2, len(dados), 2):
        estilo.append(('BACKGROUND', (0, r), (-1, r), GELO))
    t.setStyle(TableStyle(estilo))
    return t


def lista(itens, ordenada):
    # itens chega como [(numero_original, texto)]. O número do markdown é
    # preservado para que listas longas continuem a contagem entre subtítulos.
    objs = []
    for numero, t in itens:
        extra = {'value': numero} if ordenada else {}
        objs.append(ListItem(Paragraph(inline(t), E['item']),
                             leftIndent=0.62 * cm, **extra))
    return ListFlowable(
        objs, bulletType='1' if ordenada else 'bullet',
        bulletFontName=BASE + '-Bold',
        bulletFontSize=9 if ordenada else 8.6,
        bulletColor=AZUL, bulletDedent=0.62 * cm,
        leftIndent=0.62 * cm, bulletFormat='%s.' if ordenada else None,
        spaceBefore=2, spaceAfter=6,
    )


RE_H = re.compile(r'^(#{1,4})\s+(.*)$')
RE_LI = re.compile(r'^[-*]\s+(.*)$')
RE_OL = re.compile(r'^(\d+)\.\s+(.*)$')
RE_TR = re.compile(r'^\|(.+)\|\s*$')
RE_SEP = re.compile(r'^\|[\s:|-]+\|\s*$')


def converter(md, rotulo_h1=None):
    """Transforma markdown em uma lista de flowables."""
    fl = []
    linhas = md.split('\n')
    i = 0
    buffer_par = []
    buffer_li, ordenada = [], False

    def fechar_par():
        if buffer_par:
            txt = ' '.join(buffer_par).strip()
            buffer_par.clear()
            if txt.startswith('**') and txt.endswith('**') and txt.count('**') == 2:
                fl.append(Paragraph(inline(txt), E['sub']))
            else:
                fl.append(Paragraph(inline(txt), E['corpo']))

    def fechar_li():
        if buffer_li:
            fl.append(lista(list(buffer_li), ordenada))
            buffer_li.clear()

    while i < len(linhas):
        linha = linhas[i].rstrip()
        nu = linha.strip()

        if not nu:
            fechar_par()
            fechar_li()
            i += 1
            continue

        if nu in ('---', '***', '___'):
            fechar_par()
            fechar_li()
            fl.append(Spacer(1, 4))
            i += 1
            continue

        if nu.startswith('```'):
            fechar_par()
            fechar_li()
            i += 1
            bloco = []
            while i < len(linhas) and not linhas[i].strip().startswith('```'):
                bloco.append(linhas[i].rstrip())
                i += 1
            i += 1
            if bloco:
                texto = '<br/>'.join(_esc(l) for l in bloco)
                fl.append(Table(
                    [[Paragraph(texto, E['codigo'])]], colWidths=[CONTENT_W],
                    hAlign='LEFT',
                    style=TableStyle([
                        ('BACKGROUND', (0, 0), (-1, -1), GELO),
                        ('BOX', (0, 0), (-1, -1), 0.5, LINHA),
                        ('TOPPADDING', (0, 0), (-1, -1), 6),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
                        ('LEFTPADDING', (0, 0), (-1, -1), 8),
                    ])))
                fl.append(Spacer(1, 7))
            continue

        m = RE_H.match(nu)
        if m:
            fechar_par()
            fechar_li()
            nivel, texto = len(m.group(1)), m.group(2)
            if nivel == 1:
                fl.append(Paragraph(inline(rotulo_h1 or texto), E['h1']))
                fl.append(HRFlowable(width='100%', thickness=1.4, color=AZUL,
                                     spaceBefore=4, spaceAfter=11))
            elif nivel == 2:
                fl.append(CondPageBreak(4.6 * cm))
                fl.append(Paragraph(inline(texto), E['h2']))
                fl.append(HRFlowable(width='100%', thickness=0.6, color=LINHA,
                                     spaceBefore=1, spaceAfter=7))
            else:
                fl.append(CondPageBreak(2.8 * cm))
                fl.append(Paragraph(inline(texto), E['h3']))
            i += 1
            continue

        if nu.startswith('> '):
            fechar_par()
            fechar_li()
            bloco = []
            while i < len(linhas) and linhas[i].strip().startswith('>'):
                bloco.append(linhas[i].strip().lstrip('>').strip())
                i += 1
            fl.append(Table(
                [[Paragraph(inline(' '.join(bloco)), E['quote'])]],
                colWidths=[CONTENT_W], hAlign='LEFT',
                style=TableStyle([
                    ('LINEBEFORE', (0, 0), (0, -1), 2.2, AZUL),
                    ('BACKGROUND', (0, 0), (-1, -1), GELO),
                    ('TOPPADDING', (0, 0), (-1, -1), 6),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                    ('LEFTPADDING', (0, 0), (-1, -1), 4),
                ])))
            fl.append(Spacer(1, 5))
            continue

        if RE_TR.match(nu):
            fechar_par()
            fechar_li()
            bruto = []
            while i < len(linhas) and RE_TR.match(linhas[i].strip()):
                if not RE_SEP.match(linhas[i].strip()):
                    bruto.append([c.strip() for c in
                                  linhas[i].strip().strip('|').split('|')])
                i += 1
            if bruto:
                n = max(len(r) for r in bruto)
                bruto = [r + [''] * (n - len(r)) for r in bruto]
                fl.append(CondPageBreak(3.4 * cm))
                fl.append(tabela(bruto))
                fl.append(Spacer(1, 9))
            continue

        m = RE_OL.match(nu)
        if m:
            fechar_par()
            if buffer_li and not ordenada:
                fechar_li()
            ordenada = True
            buffer_li.append((int(m.group(1)), m.group(2)))
            i += 1
            continue

        m = RE_LI.match(nu)
        if m:
            fechar_par()
            if buffer_li and ordenada:
                fechar_li()
            ordenada = False
            buffer_li.append((None, m.group(1)))
            i += 1
            continue

        fechar_li()
        buffer_par.append(nu)
        i += 1

    fechar_par()
    fechar_li()
    return fl


# ------------------------------------------------------------- documento ----
class Documento(BaseDocTemplate):
    """Registra as entradas do sumário em duas passadas de build."""

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        nome = flowable.style.name
        nivel = {'h1': 0, 'h2': 1, 'h3': 2}.get(nome)
        if nivel is None:
            return
        texto = re.sub(r'<[^>]+>', '', flowable.getPlainText()).strip()
        self.notify('TOCEntry', (nivel, texto, self.page))


def moldura(canvas, doc):
    canvas.saveState()
    canvas.setFont(BASE, 7.4)
    canvas.setFillColor(CINZA)
    canvas.drawString(LEFT, PAGE_H - TOP + 0.52 * cm,
                      'Guia de preparação · Boutique de IA · Cold Chain')
    canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - TOP + 0.52 * cm, AUTOR)
    canvas.setStrokeColor(LINHA)
    canvas.setLineWidth(0.5)
    canvas.line(LEFT, PAGE_H - TOP + 0.3 * cm, PAGE_W - RIGHT,
                PAGE_H - TOP + 0.3 * cm)
    canvas.line(LEFT, BOTTOM - 0.45 * cm, PAGE_W - RIGHT, BOTTOM - 0.45 * cm)
    canvas.setFillColor(NAVY)
    canvas.setFont(BASE + '-Bold', 7.8)
    canvas.drawRightString(PAGE_W - RIGHT, BOTTOM - 0.95 * cm, str(doc.page))
    canvas.setFont(BASE, 7.4)
    canvas.setFillColor(CINZA)
    canvas.drawString(LEFT, BOTTOM - 0.95 * cm, DATA)
    canvas.restoreState()


def capa_fundo(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(NAVY)
    canvas.rect(0, PAGE_H - 1.0 * cm, PAGE_W, 1.0 * cm, stroke=0, fill=1)
    canvas.setFillColor(AZUL)
    canvas.rect(0, PAGE_H - 1.0 * cm, PAGE_W * 0.42, 1.0 * cm, stroke=0, fill=1)
    canvas.setFillColor(GELO)
    canvas.rect(0, 0, PAGE_W, 0.55 * cm, stroke=0, fill=1)
    canvas.restoreState()


def capa():
    sumario_do_conteudo = [
        'Decodificação da fala do interlocutor, com leitura de fase, escopo e modelo de engajamento',
        'One pager de escopo em quatro fases, com entregáveis, critérios de aceite, papéis e riscos',
        'Fundamentos técnicos de cadeia do frio e a regulação brasileira aplicável',
        'Casos de uso de IA em cinco camadas de maturidade, com pré requisito de dado de cada uma',
        'Anatomia do playbook da área em doze blocos, com RACI e governança de autonomia',
        'Árvore de indicadores, business case com aritmética explícita e plano de 30, 60 e 90 dias',
        'Dezesseis perguntas para fazer e respostas âncora para as perguntas prováveis',
    ]
    fl = [
        Spacer(1, 2.6 * cm),
        Paragraph('PREPARAÇÃO PARA CONVERSA DE PROJETO', E['capa_rotulo']),
        Spacer(1, 0.45 * cm),
        Paragraph(TITULO, E['capa_titulo']),
        Spacer(1, 0.5 * cm),
        HRFlowable(width='38%', thickness=2.4, color=AZUL, hAlign='LEFT',
                   spaceAfter=0.55 * cm),
        Paragraph(SUBTITULO, E['capa_sub']),
        Spacer(1, 1.5 * cm),
        Table([[Paragraph(
            '<b><font color="#FFFFFF">O que está neste documento</font></b>',
            ParagraphStyle('faixa', parent=E['nota'], fontSize=9, leading=13))]],
              colWidths=[CONTENT_W], hAlign='LEFT',
              style=TableStyle([
                  ('BACKGROUND', (0, 0), (-1, -1), NAVY),
                  ('TOPPADDING', (0, 0), (-1, -1), 6),
                  ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                  ('LEFTPADDING', (0, 0), (-1, -1), 9),
              ])),
        Table([[lista([(None, t) for t in sumario_do_conteudo], False)]],
              colWidths=[CONTENT_W],
              hAlign='LEFT',
              style=TableStyle([
                  ('BACKGROUND', (0, 0), (-1, -1), GELO),
                  ('TOPPADDING', (0, 0), (-1, -1), 7),
                  ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                  ('LEFTPADDING', (0, 0), (-1, -1), 8),
                  ('RIGHTPADDING', (0, 0), (-1, -1), 8),
              ])),
        Spacer(1, 1.3 * cm),
        Paragraph(f'{AUTOR}<br/>{DATA}', E['capa_meta']),
        Spacer(1, 0.7 * cm),
        Paragraph('Nenhum número deste documento é dado do cliente. Benchmarks de '
                  'mercado estão referenciados na seção de fontes e os valores de '
                  'exemplo estão rotulados como ilustrativos.', E['nota']),
        PageBreak(),
    ]
    return fl


def pagina_sumario():
    toc = TableOfContents()
    toc.levelStyles = [E['toc1'], E['toc2'], E['toc3']]
    toc.dotsMinLevel = 0
    # Estilo clonado com outro nome para que o próprio título não entre no sumário.
    titulo = ParagraphStyle('titulo_sumario', parent=E['h1'])
    return [
        Paragraph('Sumário', titulo),
        HRFlowable(width='100%', thickness=1.4, color=AZUL, spaceBefore=4,
                   spaceAfter=11),
        toc,
        PageBreak(),
    ]


def ler(nome):
    with open(os.path.join(ROOT, nome), encoding='utf-8') as f:
        return f.read()


def main():
    doc = Documento(SAIDA, pagesize=A4, leftMargin=LEFT, rightMargin=RIGHT,
                    topMargin=TOP, bottomMargin=BOTTOM, title=TITULO,
                    author=AUTOR,
                    subject='Preparação para projeto de Cold Chain em boutique de IA')
    quadro = Frame(LEFT, BOTTOM, CONTENT_W, PAGE_H - TOP - BOTTOM, id='corpo')
    doc.addPageTemplates([
        PageTemplate(id='capa', frames=[quadro], onPage=capa_fundo),
        PageTemplate(id='corpo', frames=[quadro], onPage=moldura),
    ])

    historia = capa()
    historia.insert(len(historia) - 1, NextPageTemplate('corpo'))
    historia += pagina_sumario()
    historia += converter(ler('guia-boutique-ia-cold-chain.md'))
    historia.append(PageBreak())
    historia += converter(ler('prompt-guia-boutique-ia.md'),
                          rotulo_h1='Anexo A · Prompt gerador do guia')
    historia.append(PageBreak())
    historia += converter(ler('README.md'),
                          rotulo_h1='Anexo B · Índice do material e como regerar')

    doc.multiBuild(historia)
    tam = os.path.getsize(SAIDA) / 1024
    print(f'PDF gerado em {SAIDA} com {doc.page} páginas e {tam:.0f} KB')


if __name__ == '__main__':
    sys.exit(main())
