#!/usr/bin/env python3
"""
Gera o PDF do roteiro preliminar do episodio sobre o Acordo Mercosul-Uniao Europeia.
Disciplina CX904 - Podcast CERI | Instituto de Economia - Unicamp

Uso:  python3 gerar_roteiro_pdf.py
Saida: roteiro-preliminar-mercosul-ue.pdf
"""
import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, HRFlowable, Image, KeepTogether, PageTemplate,
    Paragraph, Spacer, Table, TableStyle,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
LOGOS = os.path.join(ROOT, 'logos')
OUT = os.path.join(ROOT, 'roteiro-preliminar-mercosul-ue.pdf')

# ---------------------------------------------------------------- identificacao
ALUNOS = [
    ('Alan Araújo Lima', '243684'),
    ('Nathan', '[a confirmar]'),
]
DISCIPLINA = 'CX904 - Podcast CERI'
ENTREGA = 'Roteiro preliminar - 9 de outubro de 2026'

# ---------------------------------------------------------------------- fontes
FDIR = '/usr/share/fonts/google-noto'
BASE = 'Noto'
pdfmetrics.registerFont(TTFont(BASE, f'{FDIR}/NotoSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont(BASE + '-Bold', f'{FDIR}/NotoSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont(BASE + '-Italic', f'{FDIR}/NotoSans-Italic.ttf'))
pdfmetrics.registerFont(TTFont(BASE + '-BoldItalic', f'{FDIR}/NotoSans-BoldItalic.ttf'))
pdfmetrics.registerFontFamily(BASE, normal=BASE, bold=BASE + '-Bold',
                              italic=BASE + '-Italic', boldItalic=BASE + '-BoldItalic')

# -------------------------------------------------------------------- geometria
PAGE_W, PAGE_H = A4
LEFT = RIGHT = 2.5 * cm
TOP = 2.0 * cm
BOTTOM = 2.0 * cm
CONTENT_W = PAGE_W - LEFT - RIGHT

# ------------------------------------------------------------------------ cores
INK = colors.HexColor('#1A1A1A')
NAVY = colors.HexColor('#1F3864')
IEBLUE = colors.HexColor('#44697D')
GRAY = colors.HexColor('#5A5A5A')
RULE = colors.HexColor('#C9D2DA')
BOXBG = colors.HexColor('#F4F6F8')
TABHEAD = colors.HexColor('#1F3864')
TABALT = colors.HexColor('#F2F5F8')

styles = getSampleStyleSheet()


def _add(name, **kw):
    styles.add(ParagraphStyle(name=name, **kw))


# cabecalho de identificacao
_add('IdCenter', parent=styles['Normal'], fontName=BASE + '-Bold', fontSize=11,
     leading=15, alignment=TA_CENTER, textColor=INK, spaceAfter=0)
_add('IdLeft', parent=styles['Normal'], fontName=BASE, fontSize=10.5,
     leading=16, textColor=INK, spaceAfter=0)
_add('DocTitle', parent=styles['Normal'], fontName=BASE + '-Bold', fontSize=13,
     leading=18, alignment=TA_CENTER, textColor=NAVY, spaceBefore=4, spaceAfter=2)
# corpo
_add('H1x', parent=styles['Heading1'], fontName=BASE + '-Bold', fontSize=12.5,
     leading=16, textColor=NAVY, spaceBefore=14, spaceAfter=7, keepWithNext=True)
# variante sem keepWithNext: para secoes que abrem com tabela longa, deixando-a
# fluir e quebrar entre paginas em vez de empurrar tudo e abrir claro em branco
_add('H1free', parent=styles['H1x'], keepWithNext=False)
_add('H2x', parent=styles['Heading2'], fontName=BASE + '-Bold', fontSize=10.8,
     leading=14, textColor=IEBLUE, spaceBefore=10, spaceAfter=5, keepWithNext=True)
_add('Bodyx', parent=styles['BodyText'], fontName=BASE, fontSize=10,
     leading=15.2, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=7,
     firstLineIndent=0)
_add('Bulletx', parent=styles['BodyText'], fontName=BASE, fontSize=9.4,
     leading=13.6, textColor=INK, alignment=TA_JUSTIFY, leftIndent=12,
     bulletIndent=2, spaceAfter=4)
_add('QBody', parent=styles['BodyText'], fontName=BASE + '-Bold', fontSize=10,
     leading=14.6, textColor=INK, alignment=TA_JUSTIFY, spaceBefore=6, spaceAfter=3)
_add('QMeta', parent=styles['BodyText'], fontName=BASE, fontSize=9.2,
     leading=13.2, textColor=GRAY, alignment=TA_JUSTIFY, leftIndent=12,
     spaceAfter=2)
_add('Refx', parent=styles['BodyText'], fontName=BASE, fontSize=9.4,
     leading=13.4, textColor=INK, spaceAfter=7)
_add('Cellx', parent=styles['BodyText'], fontName=BASE, fontSize=8.6,
     leading=11.8, textColor=INK, spaceAfter=0)
_add('CellHead', parent=styles['BodyText'], fontName=BASE + '-Bold', fontSize=8.6,
     leading=11.8, textColor=colors.white, spaceAfter=0)
_add('Mailx', parent=styles['BodyText'], fontName=BASE, fontSize=9.4,
     leading=14, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6)


def P(t, s='Bodyx'):
    return Paragraph(t, styles[s])


def B(t):
    return Paragraph(t, styles['Bulletx'], bulletText='\u2022')


def H1(t):
    return P(t, 'H1x')


def H2(t):
    return P(t, 'H2x')


# ------------------------------------------------------------------- cabecalho
def logo_row():
    """Logos oficiais: Unicamp a esquerda, Instituto de Economia a direita."""
    uni = os.path.join(LOGOS, 'unicamp-logo.png')
    ie = os.path.join(LOGOS, 'ie-logotipo-color.png')
    cells = []

    if os.path.exists(uni):
        iw, ih = ImageReader(uni).getSize()
        h = 1.75 * cm
        cells.append(Image(uni, width=h * iw / ih, height=h))
    else:
        cells.append(P('', 'Cellx'))

    if os.path.exists(ie):
        iw, ih = ImageReader(ie).getSize()
        w = 5.0 * cm
        cells.append(Image(ie, width=w, height=w * ih / iw))
    else:
        cells.append(P('', 'Cellx'))

    t = Table([cells], colWidths=[CONTENT_W * 0.35, CONTENT_W * 0.65])
    t.setStyle(TableStyle([
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    return t


def cabecalho():
    s = [logo_row(), Spacer(1, 0.55 * cm),
         P('UNIVERSIDADE ESTADUAL DE CAMPINAS', 'IdCenter'),
         P('INSTITUTO DE ECONOMIA', 'IdCenter'),
         Spacer(1, 0.75 * cm),
         P(f'<b>Disciplina:</b> {DISCIPLINA}', 'IdLeft')]
    rotulo = 'Alunos:' if len(ALUNOS) > 1 else 'Aluno:'
    nomes = '; '.join(f'{n} &nbsp;&nbsp;<b>RA:</b> {ra}' for n, ra in ALUNOS)
    s.append(P(f'<b>{rotulo}</b> {nomes}', 'IdLeft'))
    s += [Spacer(1, 0.75 * cm),
          HRFlowable(width='100%', thickness=0.9, color=RULE),
          Spacer(1, 0.35 * cm),
          P(ENTREGA, 'DocTitle'),
          P('Mercosul-UE em aplicação provisória: que inserção externa '
            'o acordo consolida?', 'DocTitle'),
          Spacer(1, 0.2 * cm),
          HRFlowable(width='100%', thickness=0.9, color=RULE),
          Spacer(1, 0.3 * cm)]
    return s


# --------------------------------------------------------------------- tabelas
def tabela(linhas, larguras):
    data = [[P(c, 'CellHead') for c in linhas[0]]]
    data += [[P(c, 'Cellx') for c in row] for row in linhas[1:]]
    t = Table(data, colWidths=larguras, repeatRows=1, hAlign='LEFT')
    cmds = [
        ('GRID', (0, 0), (-1, -1), 0.4, RULE),
        ('BACKGROUND', (0, 0), (-1, 0), TABHEAD),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]
    for i in range(1, len(data)):
        if i % 2 == 0:
            cmds.append(('BACKGROUND', (0, i), (-1, i), TABALT))
    t.setStyle(TableStyle(cmds))
    return t


def caixa(paras, largura=None):
    t = Table([[p] for p in paras], colWidths=[largura or CONTENT_W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BOXBG),
        ('LINEBEFORE', (0, 0), (0, -1), 2.2, IEBLUE),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -2), 1),
    ]))
    return t


def pergunta(num, texto, porque, follow):
    return KeepTogether([
        P(f'<b>{num}.</b> {texto}', 'QBody'),
        P(f'<i>Por que ela está aqui:</i> {porque}', 'QMeta'),
        P(f'<i>Follow-up:</i> {follow}', 'QMeta'),
        Spacer(1, 5),
    ])


# ---------------------------------------------------------------------- rodape
def header_footer(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.5)
        canvas.line(LEFT, PAGE_H - 1.25 * cm, PAGE_W - RIGHT, PAGE_H - 1.25 * cm)
        canvas.setFont(BASE, 7.8)
        canvas.setFillColor(GRAY)
        canvas.drawString(LEFT, PAGE_H - 1.0 * cm,
                          'CX904 - Podcast CERI | Roteiro preliminar')
        canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - 1.0 * cm,
                               'Acordo Mercosul-União Europeia')
    canvas.setFont(BASE, 8.2)
    canvas.setFillColor(GRAY)
    canvas.drawCentredString(PAGE_W / 2, 1.15 * cm, str(doc.page))
    canvas.restoreState()


# ================================================================== CONTEUDO
S = []
S += cabecalho()

# --- 1. Tema e titulo
S.append(H1('Tema e título do episódio'))
S.append(caixa([
    P('<b>Título:</b> Mercosul-UE em aplicação provisória: que inserção externa '
      'o acordo consolida?', 'Cellx'),
    Spacer(1, 4),
    P('<b>Alternativos:</b> (i) Quarenta e quatro por cento: o acordo Mercosul-UE '
      'e a pauta que o Brasil leva à Europa; (ii) Em vigor e sob litígio: o acordo '
      'Mercosul-UE entre a desgravação tarifária e o Tribunal de Justiça.', 'Cellx'),
]))
S.append(Spacer(1, 8))
S.append(P(
    'O episódio examina que padrão de especialização produtiva o Acordo '
    'Mercosul-União Europeia tende a consolidar, agora que deixou de ser promessa '
    'diplomática recorrente e passou a produzir efeitos jurídicos concretos. A '
    'discussão se organiza em dois eixos, ambos verificáveis em documentos: de um '
    'lado, a composição da pauta comercial entre os blocos, que permite situar o '
    'acordo no debate sobre reprimarização e especialização regressiva na divisão '
    'internacional do trabalho; de outro, as margens de política industrial que o '
    'texto efetivamente preserva ou suprime, examinadas a partir dos capítulos de '
    'compras governamentais, propriedade intelectual, barreiras técnicas e do '
    'mecanismo de salvaguardas bilaterais.'))
S.append(P(
    'O episódio não discute, deliberadamente, duas questões adjacentes. A primeira '
    'é o mérito ambiental do acordo, tema que exigiria tratamento próprio e que '
    'deslocaria o eixo da economia industrial para a regulação ambiental comparada. '
    'A segunda é o diagnóstico geral sobre o neoliberalismo e sua eventual '
    'superação, recorte que cabe ao episódio do G4 ("O capitalismo acabou?") e cuja '
    'incorporação aqui produziria sobreposição sem ganho analítico. O interesse '
    'deste episódio é mais restrito e, por isso, respondível em trinta minutos: um '
    'acordo comercial específico, já em vigor, e o padrão de inserção externa que '
    'ele institucionaliza.'))

# --- 2. Pergunta-guia
S.append(H1('Pergunta-guia'))
S.append(caixa([
    P('<b>Que padrão de inserção externa o Acordo Mercosul-União Europeia '
      'consolida?</b>', 'Cellx'),
]))
S.append(Spacer(1, 8))
S.append(P(
    'A pergunta é respondível no formato porque não exige projeção macroeconômica '
    'nem arbitragem entre modelos de equilíbrio geral, e sim a leitura conjunta de '
    'dois conjuntos de evidências disponíveis: a composição setorial do comércio '
    'bilateral e o conteúdo normativo do texto acordado. Ela se desdobra, portanto, '
    'em dois eixos. O primeiro é o eixo do padrão de especialização: dada a '
    'assimetria observada da pauta, a desgravação tarifária tende a aprofundá-la ou '
    'a abrir espaço para sua diversificação? O segundo é o eixo das margens de '
    'política industrial: supondo que a diversificação seja desejável, o acordo '
    'preserva ou suprime os instrumentos de que o Estado brasileiro precisaria para '
    'promovê-la? Trata-se de uma pergunta aberta, e não de uma conclusão a ser '
    'confirmada pelo entrevistado — há interpretações divergentes e documentadas '
    'sobre ambos os eixos, e o episódio ganha ao expô-las.'))

# --- 3. Justificativa
S.append(H1('Justificativa e relevância'))
for par in [
    'A relevância do tema decorre de um marco recente e ainda pouco discutido em '
    'profundidade. Depois de vinte e seis anos de negociação, o Acordo de Parceria '
    'Estratégica Mercosul-União Europeia foi assinado em Assunção, no Paraguai, em '
    '17 de janeiro de 2026 (MAPA, 2026), e sua vertente comercial entrou em '
    'aplicação provisória em 1º de maio de 2026, após a promulgação pelo Decreto '
    'nº 12.953, de 28 de abril de 2026, que internalizou o Acordo Provisório de '
    'Comércio no ordenamento jurídico brasileiro (Notícia Siscomex Importação '
    'nº 51, de 27 mai. 2026).',

    'O arranjo jurídico, contudo, é menos estável do que a expressão "entrada em '
    'vigor" sugere, e a razão disso é a própria arquitetura do acordo. Foram '
    'assinados dois instrumentos distintos: o Acordo Provisório de Comércio, que '
    'cobre apenas o pilar comercial e que, por tratar de matéria de competência '
    'exclusiva da União Europeia, dispensa a ratificação individual pelos '
    'Estados-membros; e o Acordo de Parceria, que agrega os pilares político e de '
    'cooperação e que, por ser acordo misto, depende da ratificação pelos vinte e '
    'sete (Conjur, 29 abr. 2026; MAPA, 2026). O que está efetivamente em vigor, '
    'portanto, é o primeiro instrumento, e não o conjunto. Acrescente-se um detalhe '
    'de pouca circulação e consequência relevante: o Acordo de Parceria admite '
    'vigência bilateral, de modo que a conclusão da ratificação pela União Europeia '
    'e pelo Brasil bastaria para que ele produzisse efeitos entre essas partes, sem '
    'aguardar os vinte e sete (MAPA, 2026).',

    'Esse fatiamento é precisamente o que foi judicializado, e é o que torna o '
    'intervalo entre aplicação provisória e vigência plena economicamente '
    'relevante. Em 21 de janeiro de 2026, quatro dias após a assinatura, o '
    'Parlamento Europeu aprovou, por 334 votos a 324, resolução que solicita '
    'parecer do Tribunal de Justiça da União Europeia sobre a base jurídica de '
    'ambos os instrumentos, suspendendo o processo de consentimento por prazo que '
    'pode alcançar dois anos (Conjur, 29 abr. 2026). Em 29 de setembro de 2026, o '
    'mesmo Tribunal indeferiu o pedido da Polônia de suspensão liminar da aplicação '
    'provisória, mas manteve em análise a ação principal, que pede a anulação da '
    'Decisão (UE) 2026/183 do Conselho sob o argumento de que a Comissão Europeia '
    'fracionou artificialmente o acordo de associação para evitar a exigência de '
    'unanimidade no Conselho, em violação ao artigo 218 do Tratado sobre o '
    'Funcionamento da União Europeia (Canal Rural/Estadão Conteúdo, 29 set. 2026). '
    'Preferências tarifárias já operam, portanto, sob uma decisão do Conselho cuja '
    'validade está sob exame judicial — situação que interessa ao episódio não como '
    'curiosidade processual, mas porque define o horizonte de cálculo de quem '
    'decide investir com base nessas preferências.',

    'O ponto analítico central, contudo, é a assimetria da pauta comercial. Em '
    '2025, os produtos agrícolas responderam por US$ 21,8 bilhões das exportações '
    'brasileiras à União Europeia, o equivalente a 44% da pauta destinada ao bloco; '
    'considerado o agronegócio como um todo, com a inclusão de celulose, couros '
    'processados e madeira, o valor alcança US$ 25,2 bilhões, ou aproximadamente '
    '51% (MAPA, 2026). Um recorte metodologicamente distinto converge para a mesma '
    'ordem de grandeza: em 2025, 52% das exportações brasileiras ao bloco foram '
    'realizadas pelos setores agropecuário e extrativista (Conjur, 29 abr. 2026). A '
    'convergência entre agregações diferentes reforça a leitura de que a posição '
    'brasileira na relação bilateral é a de fornecedor de matérias-primas e de bens '
    'de baixo processamento, o que remete o acordo ao problema clássico da '
    'deterioração dos termos de intercâmbio e da especialização periférica '
    '(PREBISCH, 1949; FURTADO, 1959) e à discussão sobre a supressão dos '
    'instrumentos de promoção industrial que os próprios países centrais utilizaram '
    'em sua industrialização (CHANG, 2002).',

    'Há, no entanto, evidência que tensiona essa leitura e que o episódio precisa '
    'apresentar. A desgravação europeia não se concentra em bens primários: a '
    'partir de 1º de maio de 2026, a União Europeia zerou o imposto de importação '
    'de 2.932 produtos, dos quais 21,8% são máquinas e equipamentos, 12,5% '
    'alimentos, 9,1% produtos siderúrgicos, 8,9% máquinas, aparelhos e materiais '
    'elétricos e 8,1% químicos (Conjur, 29 abr. 2026). A abertura, portanto, é '
    'majoritariamente de alto valor agregado, e a Confederação Nacional da '
    'Indústria estima que mais de cinco mil produtos passem a ter tarifa zero, o '
    'equivalente a mais de 80% das importações europeias de bens brasileiros em '
    '2025 (CNI, 2026). O problema analítico que daí resulta é mais interessante do '
    'que a denúncia da assimetria: a oportunidade existe no papel, mas seu '
    'aproveitamento exigiria que a pauta exportadora nacional mudasse, e os '
    'produtos agroindustriais considerados sensíveis — carne bovina, frango, arroz, '
    'mel, açúcar e etanol — permanecem sob cotas tarifárias, com acesso limitado e '
    'controlado (Conjur, 29 abr. 2026). É essa distância entre abertura formal e '
    'capacidade produtiva de ocupá-la que a entrevista deve investigar.',

    'O tema dialoga diretamente com a agenda do CERI sobre inserção externa '
    'brasileira, comércio internacional e política industrial, e os convidados '
    'indicados pertencem ao Núcleo de Economia Industrial e da Tecnologia do '
    'próprio Instituto, o que torna a entrevista factível no prazo da disciplina.',
]:
    S.append(P(par))

# --- 4. Estrutura dos 30 minutos
S.append(P('Estrutura dos 30 minutos', 'H1free'))
S.append(tabela([
    ['Bloco', 'Min.', 'Conteúdo', 'Função narrativa'],
    ['Abertura e gancho', '0\u20112',
     'A decisão do TJUE de 29 de setembro de 2026 sobre o pedido polonês: o acordo '
     'está em vigor e, simultaneamente, sob litígio quanto à validade da decisão '
     'que autorizou sua aplicação provisória',
     'Estabelecer que o tema é atual e que o "acordo em vigor" é um objeto jurídico '
     'instável'],
    ['Contextualização 1 — o que, exatamente, entrou em vigor', '2‑8',
     'A distinção entre os dois instrumentos e o estado de cada um',
     'Desfazer a confusão corrente entre acordo comercial e acordo de parceria, e '
     'mostrar por que isso importa'],
    ['Contextualização 2 — a assimetria da pauta', '8‑13',
     'Composição das exportações brasileiras ao bloco e perfil da desgravação '
     'concedida pela União Europeia',
     'Apresentar os dois conjuntos de dados que sustentam, e tensionam, a hipótese '
     'do episódio'],
    ['Entrevista', '13‑27',
     'Seis perguntas, em progressão do diagnóstico ao contrafactual',
     'Submeter a hipótese a quem pesquisa o tema'],
    ['Fechamento', '27‑30',
     'Síntese da resposta à pergunta-guia e delimitação do que permanece em aberto',
     'Encerrar sem fabricar conclusão'],
], [3.1 * cm, 1.5 * cm, 5.5 * cm, 5.9 * cm]))

S.append(H2('Contextualização 1 — dados e documentos a citar (2-8 min)'))
for b in [
    'Assinatura em Assunção, Paraguai, em 17 de janeiro de 2026, após vinte e seis '
    'anos de negociação (MAPA, 2026).',
    'Aprovação, pelo Conselho da União Europeia, em 9 de janeiro de 2026, das duas '
    'decisões que autorizam a assinatura dos dois instrumentos (Conselho da UE, '
    '2026). <font color="#A61C00">[VERIFICAR: número e data da decisão relativa ao '
    'Acordo Provisório no Jornal Oficial da UE]</font>',
    'A distinção entre o Acordo Provisório de Comércio, de competência exclusiva da '
    'União Europeia, e o Acordo de Parceria, acordo misto sujeito à ratificação '
    'pelos vinte e sete (Conjur, 29 abr. 2026; MAPA, 2026).',
    'A previsão de vigência bilateral do Acordo de Parceria (MAPA, 2026).',
    'Resolução do Parlamento Europeu de 21 de janeiro de 2026, aprovada por 334 a '
    '324, solicitando parecer ao TJUE; suspensão do consentimento por prazo que '
    'pode chegar a dois anos (Conjur, 29 abr. 2026).',
    'Aprovação do texto pelo Congresso Nacional por meio do PDL nº 41/2026 e '
    'promulgação pelo Decreto nº 12.953, de 28 de abril de 2026; início da '
    'aplicação provisória em 1º de maio de 2026.',
    'Decreto nº 12.866, de 4 de março de 2026, que regulamenta a investigação e a '
    'aplicação de salvaguardas bilaterais em acordos de livre comércio, incluído o '
    'Mercosul-União Europeia.',
    'Ação da Polônia contra o Conselho da União Europeia pedindo a anulação da '
    'Decisão (UE) 2026/183; indeferimento do pedido de suspensão liminar em 29 de '
    'setembro de 2026 e manutenção da ação principal em análise; fundamentos '
    'invocados: fracionamento artificial do acordo para evitar a unanimidade no '
    'Conselho, em violação ao artigo 218 do TFUE, avanço da aplicação provisória '
    'sem consentimento definitivo do Parlamento Europeu e ausência de '
    'cláusulas-espelho de simetria sanitária e ambiental (Canal Rural/Estadão '
    'Conteúdo, 29 set. 2026).',
]:
    S.append(B(b))

S.append(H2('Contextualização 2 — dados e documentos a citar (8-13 min)'))
for b in [
    'Exportações brasileiras de produtos agrícolas à União Europeia em 2025: '
    'US$ 21,8 bilhões, equivalentes a 44% da pauta destinada ao bloco; '
    'US$ 25,2 bilhões, ou cerca de 51%, considerado o agronegócio como um todo, com '
    'celulose, couros processados e madeira (MAPA, 2026).',
    'Recorte alternativo, com agregação distinta: 52% das exportações brasileiras '
    'ao bloco em 2025 provenientes dos setores agropecuário e extrativista (Conjur, '
    '29 abr. 2026).',
    'Perfil da desgravação concedida pela União Europeia a partir de 1º de maio de '
    '2026: 2.932 produtos com tarifa zerada, dos quais 21,8% máquinas e '
    'equipamentos, 12,5% alimentos, 9,1% siderúrgicos, 8,9% máquinas, aparelhos e '
    'materiais elétricos e 8,1% químicos (Conjur, 29 abr. 2026).',
    'Estimativa da CNI: mais de cinco mil produtos com tarifa zero, equivalentes a '
    'mais de 80% das importações europeias de bens brasileiros em 2025 (CNI, 2026).',
    'Manutenção de cotas tarifárias para produtos agroindustriais sensíveis: carne '
    'bovina, frango, arroz, mel, açúcar e etanol (Conjur, 29 abr. 2026).',
    'Cronograma de desgravação oferecido pela União Europeia, constante do Apêndice '
    '2-A-1 do Acordo (Siscomex).',
    'Estimativas divergentes de impacto agregado: governo brasileiro, acréscimo de '
    '0,34% do PIB, ou R$ 37 bilhões; Ipea, 0,46% do PIB, ou US$ 9,3 bilhões, até '
    '2040. A divergência será apresentada como divergência, sem escolha entre as '
    'duas.',
    'Dimensão do mercado resultante: cerca de 720 milhões de habitantes e PIB '
    'combinado superior a US$ 22 trilhões (Siscomex, 2026).',
]:
    S.append(B(b))

# --- 5. Roteiro de entrevista
S.append(H1('Roteiro de entrevista'))
S.append(pergunta(
    1,
    'O senhor diria que o padrão de comércio que o acordo encontra — com cerca de '
    'metade da pauta brasileira ao bloco concentrada em produtos agrícolas e '
    'extrativos — é um ponto de partida que a desgravação tende a aprofundar, ou um '
    'ponto de partida que ela permite modificar?',
    'é a tradução direta da pergunta-guia e estabelece o diagnóstico sobre o qual '
    'todas as demais se apoiam.',
    'se a resposta for que depende de fatores internos, quais fatores, e em que '
    'prazo eles operariam diante de um cronograma de desgravação que se estende por '
    'até quinze anos?'))
S.append(pergunta(
    2,
    'A abertura europeia não é concentrada em bens primários: dos 2.932 produtos '
    'que tiveram tarifa zerada em maio, 21,8% são máquinas e equipamentos e 9,1% '
    'são siderúrgicos. Por que uma concessão desse perfil não se converte, '
    'automaticamente, em diversificação da pauta brasileira?',
    'submete a hipótese do episódio ao contra-dado mais forte disponível e impede '
    'que a contextualização pareça selecionar evidências.',
    'existe precedente, em acordos anteriores do Mercosul ou de outros países '
    'latino-americanos, em que uma concessão tarifária de alto valor agregado tenha '
    'efetivamente alterado a composição das exportações?'))
S.append(pergunta(
    3,
    'No trabalho que o senhor apresentou com Marta Castilho sobre os impactos do '
    'acordo na indústria brasileira, há avaliação sobre os instrumentos de política '
    'industrial. Quais margens o texto preserva e quais ele suprime, considerando '
    'especificamente compras governamentais, propriedade intelectual, barreiras '
    'técnicas e exigências de conteúdo local?',
    'é o segundo eixo da pergunta-guia, e dirige-se ao ponto em que o entrevistado '
    'tem contribuição própria e publicada.',
    'o mecanismo de salvaguardas bilaterais regulamentado pelo Decreto '
    'nº 12.866/2026 compensa, em alguma medida, as margens suprimidas, ou opera em '
    'registro distinto?'))
S.append(pergunta(
    4,
    'Quais setores da indústria de transformação brasileira ganham e quais perdem '
    'com o acordo? Interessa que o senhor os nomeie, inclusive aqueles cujo '
    'resultado é ambíguo.',
    'exigência explícita do recorte combinado com os professores e o ponto em que o '
    'episódio deixa de ser abstrato para o ouvinte.',
    'entre os setores que perdem, há algum em que a perda decorra menos da tarifa e '
    'mais das regras não tarifárias do acordo?'))
S.append(pergunta(
    5,
    'O acordo comercial está em aplicação provisória desde maio, mas a decisão do '
    'Conselho que autorizou essa aplicação é objeto de ação de anulação ainda em '
    'curso no TJUE, e o consentimento do Parlamento Europeu permanece suspenso. Que '
    'efeito econômico tem operar sob preferências tarifárias com esse grau de '
    'incerteza jurídica?',
    'converte o intervalo entre aplicação provisória e vigência plena, que é o '
    'segundo item da contextualização, em pergunta sobre decisão de investimento.',
    'essa incerteza afeta de modo desigual quem exporta commodities e quem '
    'precisaria investir em capacidade produtiva nova para aproveitar as '
    'preferências?'))
S.append(pergunta(
    6,
    'Supondo que o diagnóstico de especialização regressiva esteja correto, o que '
    'precisaria ser feito internamente, e em que prazo, para que o acordo não '
    'consolidasse esse padrão? Há algum caso em que as margens preservadas pelo '
    'texto seriam suficientes para isso?',
    'fecha o episódio em registro de política econômica, e não de denúncia, '
    'permitindo que o entrevistado qualifique ou rejeite a hipótese.',
    'o caso dos minerais críticos, em que o Brasil detém o segundo maior depósito '
    'natural do mundo e não dispõe de política nacional específica de gestão '
    'estratégica, é um exemplo dessa margem não aproveitada ou um problema de outra '
    'natureza?'))

# --- 6. Entrevistado
S.append(H1('Entrevistado'))
S.append(P(
    '<b>Principal: Fernando Sarti (Instituto de Economia, Unicamp).</b> Professor '
    'do Instituto desde julho de 2002 e livre-docente desde 2019, é pesquisador do '
    'Núcleo de Economia Industrial e da Tecnologia desde 1988, do qual foi '
    'coordenador entre 2005 e 2007. A escolha se justifica por ele ser coautor, com '
    'Marta Castilho, do trabalho "Impactos do Acordo Mercosul e União Europeia '
    'sobre a Indústria Brasileira", apresentado no V Encontro Nacional de Economia '
    'Industrial e Inovação — isto é, por ter examinado exatamente o objeto da '
    'pergunta-guia, e pelo ângulo da indústria de transformação, que é o eixo do '
    'episódio. As perguntas 3, 4 e 6 dirigem-se particularmente a ele.'))
S.append(P(
    '<b>Reserva: Célio Hiratuka (Instituto de Economia, Unicamp).</b> Professor '
    'associado, pesquisador do mesmo Núcleo de Economia Industrial e da Tecnologia, '
    'coordenador do Grupo de Estudos Brasil-China e Diretor Associado do Instituto '
    'entre outubro de 2019 e outubro de 2023. Sua trajetória em comércio '
    'internacional e política industrial cobre o mesmo eixo, e a coordenação do '
    'Grupo de Estudos Brasil-China acrescenta a possibilidade de situar o acordo na '
    'comparação com o padrão de comércio Brasil-China. As perguntas 1, 2 e 4 '
    'dirigem-se particularmente a ele.'))
S.append(P(
    '<b>Alternativa externa:</b> Marta Castilho (UFRJ), coautora do estudo citado e '
    'organizadora de "Impactos do acordo Mercosul-União Europeia sobre as mulheres" '
    '(2023). Fica como terceira opção apenas por não pertencer ao Instituto, o que '
    'torna o agendamento menos previsível no prazo da disciplina.'))

S.append(H2('Minuta de e-mail de convite'))
S.append(caixa([
    P('<b>Assunto:</b> Convite para entrevista — Podcast CERI (CX904), episódio '
      'sobre o Acordo Mercosul-União Europeia', 'Mailx'),
    Spacer(1, 5),
    P('Prezado Professor Fernando Sarti,', 'Mailx'),
    P('Somos alunos de graduação do Instituto de Economia e cursamos a disciplina '
      'CX904 — Podcast CERI, cujo produto final é um episódio de aproximadamente '
      'trinta minutos.', 'Mailx'),
    P('Nosso episódio examina que padrão de inserção externa o Acordo '
      'Mercosul-União Europeia consolida, agora que o Acordo Provisório de Comércio '
      'está em aplicação provisória desde 1º de maio. Tomamos como referência '
      'central o trabalho que o senhor apresentou com Marta Castilho, no V ENEI, '
      'sobre os impactos do acordo na indústria brasileira.', 'Mailx'),
    P('Gostaríamos de convidá-lo para a entrevista, com duração aproximada de '
      'trinta minutos, em data de sua conveniência, no Instituto ou de forma '
      'remota. Enviaríamos as perguntas com antecedência.', 'Mailx'),
    P('Agradecemos a atenção.', 'Mailx'),
    P('Alan Araújo Lima — RA 243684<br/>Nathan — RA [a confirmar]', 'Mailx'),
]))

# --- 7. Referencias
S.append(H1('Referências preliminares'))
S.append(H2('Apresentadas na primeira entrega'))
for r in [
    'BRASIL. Decreto nº 12.953, de 28 de abril de 2026. Promulga o Acordo '
    'Provisório de Comércio entre o Mercosul e a União Europeia. <i>Diário Oficial '
    'da União</i>: seção 1, edição extra, Brasília, DF, 28 abr. 2026.',
    'CASTILHO, Marta et al. (org.). <i>Impactos do acordo Mercosul-União Europeia '
    'sobre as mulheres</i>: precarização, perda de emprego e pobreza. Rio de '
    'Janeiro: Instituto Equit, 2023.',
    'CHANG, Ha-Joon. <i>Kicking away the ladder</i>: development strategy in '
    'historical perspective. London: Anthem Press, 2002.',
    'FURTADO, Celso. <i>Formação econômica do Brasil</i>. Rio de Janeiro: Fundo de '
    'Cultura, 1959.',
    'PREBISCH, Raúl. <i>El desarrollo económico de la América Latina y algunos de '
    'sus principales problemas</i>. Santiago: Cepal, 1949.',
    'SARTI, Fernando; CASTILHO, Marta. Impactos do acordo Mercosul e União Europeia '
    'sobre a indústria brasileira. In: ENCONTRO NACIONAL DE ECONOMIA INDUSTRIAL E '
    'INOVAÇÃO, 5., 2021, Belo Horizonte. <i>Anais</i>. São Paulo: Blucher '
    'Proceedings, 2021. <font color="#A61C00">[VERIFICAR: autoria, paginação e '
    'imprint — a primeira entrega registrou "Belo Horizonte: Face/UFMG"; a lista de '
    'artigos do V ENEI está em Blucher Proceedings]</font>',
]:
    S.append(P(r, 'Refx'))

S.append(H2('Acréscimos desta entrega'))
for r in [
    'BRASIL. Congresso Nacional. <i>Projeto de Decreto Legislativo nº 41, de '
    '2026</i>. Aprova o texto do Acordo Provisório de Comércio entre o Mercado '
    'Comum do Sul (Mercosul) e seus Estados-Partes, de um lado, e a União Europeia, '
    'de outro, assinado em Assunção, Paraguai, em 17 de janeiro de 2026. Brasília, '
    'DF, 2026.',
    'BRASIL. Decreto nº 12.866, de 4 de março de 2026. Regulamenta o procedimento '
    'para investigação e aplicação de medidas de salvaguardas bilaterais em acordos '
    'comerciais firmados pelo Brasil. <i>Diário Oficial da União</i>: edição extra, '
    'Brasília, DF, 4 mar. 2026.',
    'BRASIL. Ministério da Agricultura e Pecuária. <i>Acordo de Parceria '
    'Estratégica Mercosul-União Europeia</i>. Brasília, DF, 2026.',
    'BRASIL. Ministério do Desenvolvimento, Indústria, Comércio e Serviços. '
    '<i>Comex Stat</i>: exportações e importações por país e por setor. Brasília, '
    'DF, 2026.',
    'BRASIL. Secretaria Especial da Receita Federal. <i>Notícia Siscomex Importação '
    'nº 51, de 27 de maio de 2026</i>. Retificação dos anexos relativos à '
    'implementação do Acordo Provisório de Comércio entre o Mercosul e a União '
    'Europeia. Brasília, DF, 2026.',
    'CONFEDERAÇÃO NACIONAL DA INDÚSTRIA. <i>Manual do Acordo Mercosul-União '
    'Europeia</i>. Brasília, DF: CNI, 2026.',
    'CONSELHO DA UNIÃO EUROPEIA. <i>Decisão (UE) 2026/183</i>, relativa à '
    'assinatura e à aplicação provisória do Acordo Provisório de Comércio entre a '
    'União Europeia e o Mercosul. <i>Jornal Oficial da União Europeia</i>, 2026. '
    '<font color="#A61C00">[VERIFICAR: data, ementa exata e número do Jornal '
    'Oficial]</font>',
    'MERCOSUL; UNIÃO EUROPEIA. <i>Acordo Provisório de Comércio</i>. Apêndice '
    '2-A-1: cronograma de desgravação tarifária da União Europeia. Assunção, '
    '17 jan. 2026.',
    'Acordo Mercosul-UE entra em vigor no dia 1º: lições e apontamentos. '
    '<i>Consultor Jurídico</i>, São Paulo, 29 abr. 2026. '
    '<font color="#A61C00">[VERIFICAR: autoria da coluna]</font>',
    'TJUE rejeita pedido da Polônia contra aplicação provisória do acordo '
    'Mercosul-UE. <i>Canal Rural</i>, 29 set. 2026. Fonte: Estadão Conteúdo.',
]:
    S.append(P(r, 'Refx'))

# --- 8. Nota de correcoes
S.append(H1('Nota sobre correções à primeira entrega'))
S.append(P(
    'Dois pontos da primeira entrega foram corrigidos após consulta às fontes '
    'primárias, e registramos a correção para que não pareça ajuste silencioso.'))
S.append(P(
    '<b>Primeiro.</b> A primeira entrega afirmava que a vigência definitiva '
    '"depende da ratificação pelos 27 Estados-membros e do parecer do Tribunal de '
    'Justiça da União Europeia". A formulação confundia os dois instrumentos: a '
    'ratificação pelos vinte e sete condiciona o Acordo de Parceria, e não o Acordo '
    'Provisório de Comércio, que é o que está em aplicação provisória e que '
    'dispensa esse trâmite por tratar de matéria de competência exclusiva da União '
    'Europeia. A distinção passou a ocupar o primeiro bloco de contextualização, '
    'por ser condição para entender o que está em jogo no litígio em curso.'))
S.append(P(
    '<b>Segundo.</b> O dado de US$ 21,8 bilhões e 44% da pauta está correto, mas '
    'sua atribuição ao Comex Stat é imprecisa. A formulação consta da página '
    'oficial do Ministério da Agricultura e Pecuária sobre o acordo, e o agregado '
    '"produtos agrícolas" corresponde à classificação do Ministério, não a uma '
    'categoria nativa do Comex Stat, cujos dados de base alimentam o cálculo. A '
    'referência passou a ser o MAPA, e a mesma fonte permitiu acrescentar o valor '
    'de US$ 25,2 bilhões para o agronegócio em sentido amplo, equivalente a cerca '
    'de 51% da pauta.'))

# --- 9. Pendencias
S.append(H1('Pendências e próximos passos'))
for i, b in enumerate([
    '<b>Registro acadêmico.</b> Confirmar o RA do Nathan para a versão final da '
    'entrega.',
    '<b>Contato com o entrevistado.</b> Enviar o convite ao Professor Fernando '
    'Sarti na semana de 13 de outubro, com as perguntas em anexo; acionar o '
    'Professor Célio Hiratuka caso não haja resposta em uma semana.',
    '<b>Dados a confirmar.</b> Autoria, paginação e imprint do trabalho de Sarti e '
    'Castilho no V ENEI; número, data e ementa exata da Decisão (UE) 2026/183 no '
    'Jornal Oficial da União Europeia; número e data da decisão do Conselho de 9 de '
    'janeiro de 2026 relativa ao Acordo Provisório; autoria da coluna da Consultor '
    'Jurídico de 29 de abril de 2026.',
    '<b>Replicação no Comex Stat.</b> Reproduzir a composição da pauta exportadora '
    'à União Europeia em 2025 diretamente no Comex Stat, declarando a agregação '
    'utilizada, para dispor de um cálculo próprio além do agregado do MAPA.',
    '<b>Acompanhamento processual.</b> Verificar, até a gravação, se houve '
    'movimentação na ação principal da Polônia no TJUE ou no pedido de parecer '
    'formulado pelo Parlamento Europeu, dado que ambos podem alterar o bloco de '
    'abertura.',
    '<b>Divisão de tarefas.</b> Definir entre os dois a responsabilidade pela '
    'contextualização, pela condução da entrevista e pela edição.',
    '<b>Gravação.</b> Data provável na segunda metade de novembro, condicionada à '
    'agenda do entrevistado.',
], start=1):
    S.append(Paragraph(b, styles['Bulletx'], bulletText=f'{i}.'))


# ===================================================================== BUILD
def build():
    autores = ' e '.join(n for n, _ in ALUNOS)
    doc = BaseDocTemplate(
        OUT, pagesize=A4, leftMargin=LEFT, rightMargin=RIGHT,
        topMargin=TOP, bottomMargin=BOTTOM,
        title='Roteiro preliminar - Acordo Mercosul-Uniao Europeia (CX904)',
        author=autores,
        subject='CX904 - Podcast CERI | Instituto de Economia - Unicamp',
        creator=autores)
    frame = Frame(LEFT, BOTTOM, CONTENT_W, PAGE_H - TOP - BOTTOM, id='normal')
    doc.addPageTemplates([PageTemplate(id='main', frames=[frame],
                                       onPage=header_footer)])
    doc.build(S)
    print(f'PDF gerado: {OUT}')


if __name__ == '__main__':
    build()
