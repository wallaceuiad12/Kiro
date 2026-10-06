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
    ('Alan Araújo Lima', '238212'),
    ('Nathan Pereira', '243684'),
    ('Matteo Lucato', '246226'),
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
# Documento monocromatico: tudo preto sobre branco, sem preenchimentos.
INK = colors.black
NAVY = colors.black
IEBLUE = colors.black
GRAY = colors.black
RULE = colors.black

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
     leading=11.8, textColor=INK, spaceAfter=0)
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
    uni = os.path.join(LOGOS, 'unicamp-logo-preto.png')
    ie = os.path.join(LOGOS, 'ie-logotipo-preto.png')
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
    if len(ALUNOS) <= 2:
        nomes = '; '.join(f'{n} &nbsp;&nbsp;<b>RA:</b> {ra}' for n, ra in ALUNOS)
        s.append(P(f'<b>{rotulo}</b> {nomes}', 'IdLeft'))
    else:
        # com tres integrantes a linha unica estoura a largura: um por linha,
        # com o rotulo apenas na primeira
        s.append(P(f'<b>{rotulo}</b>', 'IdLeft'))
        for n, ra in ALUNOS:
            s.append(P(f'&nbsp;&nbsp;&nbsp;&nbsp;{n} &nbsp;&nbsp;<b>RA:</b> {ra}',
                       'IdLeft'))
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
    # sem preenchimento: grade fina preta e cabecalho apenas em negrito,
    # separado do corpo por um fio mais grosso
    t.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.4, RULE),
        ('LINEBELOW', (0, 0), (-1, 0), 1.0, RULE),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]))
    return t


def caixa(paras, largura=None):
    t = Table([[p] for p in paras], colWidths=[largura or CONTENT_W])
    # caixa sem fundo: so um contorno fino preto
    t.setStyle(TableStyle([
        ('BOX', (0, 0), (-1, -1), 0.5, RULE),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
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
S.append(P('<b>Título:</b> Mercosul-UE em aplicação provisória: que inserção '
           'externa o acordo consolida?'))
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
    'confirmada pelo entrevistado, já que há interpretações divergentes e '
    'documentadas '
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
    'validade está sob exame judicial, situação que interessa ao episódio não como '
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
    'produtos agroindustriais considerados sensíveis (carne bovina, frango, arroz, '
    'mel, açúcar e etanol) permanecem sob cotas tarifárias, com acesso limitado e '
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
    ['Contextualização 1: o que, exatamente, entrou em vigor', '2‑8',
     'A distinção entre os dois instrumentos e o estado de cada um',
     'Desfazer a confusão corrente entre acordo comercial e acordo de parceria, e '
     'mostrar por que isso importa'],
    ['Contextualização 2: a assimetria da pauta', '8‑13',
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

S.append(H2('Contextualização 1: dados e documentos a citar (2 a 8 min)'))
for b in [
    'Assinatura em Assunção, Paraguai, em 17 de janeiro de 2026, após vinte e seis '
    'anos de negociação (MAPA, 2026).',
    'Aprovação, pelo Conselho da União Europeia, em 9 de janeiro de 2026, das duas '
    'decisões que autorizam a assinatura dos instrumentos: a Decisão (UE) 2026/183, '
    'relativa à assinatura e à aplicação provisória do Acordo Provisório sobre '
    'Comércio, e a Decisão (UE) 2026/185, relativa ao Acordo de Parceria. Ambas '
    'foram publicadas no Jornal Oficial da União Europeia de 27 de fevereiro de '
    '2026 (JO L, 2026/183 e JO L, 2026/185).',
    'O texto do próprio Acordo Provisório sobre Comércio foi publicado no mesmo '
    'Jornal Oficial, em JO L, 2026/184, de 27 de fevereiro de 2026, o que permite '
    'citar os capítulos diretamente da fonte oficial.',
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
    'Ação da Polônia contra o Conselho da União Europeia, autuada como Processo '
    'C-460/26, pedindo a anulação da Decisão (UE) 2026/183. O pedido de suspensão '
    'liminar foi indeferido por despacho do vice-presidente do Tribunal de Justiça '
    'em 29 de setembro de 2026, no Processo C-460/26 R, e a ação principal segue em '
    'análise; fundamentos '
    'invocados: fracionamento artificial do acordo para evitar a unanimidade no '
    'Conselho, em violação ao artigo 218 do TFUE, avanço da aplicação provisória '
    'sem consentimento definitivo do Parlamento Europeu e ausência de '
    'cláusulas-espelho de simetria sanitária e ambiental (Canal Rural/Estadão '
    'Conteúdo, 29 set. 2026).',
]:
    S.append(B(b))

S.append(H2('Contextualização 2: dados e documentos a citar (8 a 13 min)'))
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
    'O senhor diria que o padrão de comércio que o acordo encontra, com cerca de '
    'metade da pauta brasileira ao bloco concentrada em produtos agrícolas e '
    'extrativos, é um ponto de partida que a desgravação tende a aprofundar, ou um '
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
    '<b>Primeira opção: Fernando Sarti.</b> O professor Sarti é do NEIT, o núcleo '
    'de economia industrial do Instituto, e foi ele quem escreveu, com Marta '
    'Castilho, o trabalho sobre os impactos do acordo na indústria brasileira que '
    'está nas nossas referências. É a escolha mais direta que temos: ele já olhou '
    'para esse problema pelo ângulo que nos interessa, o da indústria de '
    'transformação, e não pelo do agronegócio, que é o recorte que domina o debate '
    'público sobre o acordo. As perguntas 3, 4 e 6 são especialmente para ele, e a '
    '3 parte do que ele próprio argumenta no texto.'))
S.append(P(
    '<b>Segunda opção: Célio Hiratuka.</b> Também é do NEIT e trabalha com comércio '
    'internacional e política industrial, então cobre o mesmo terreno. Tem uma '
    'vantagem própria: como coordena o Grupo de Estudos Brasil-China, pode comparar '
    'o padrão que o acordo com a União Europeia tende a consolidar com o que o '
    'comércio com a China já consolidou, contraponto que o episódio não teria de '
    'outra forma. Nesse caso, as perguntas 1, 2 e 4 ganhariam peso.'))
S.append(P(
    '<b>Se nenhum dos dois puder: Marta Castilho (UFRJ).</b> É a coautora do estudo '
    'e organizou o livro sobre os impactos do acordo sobre as mulheres. Ficou em '
    'terceiro só porque não é do Instituto, e combinar agenda com alguém de fora, '
    'no prazo que temos, é mais arriscado.'))

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
    'INOVAÇÃO, 5., 2021, Belo Horizonte. <i>Anais</i>. São Paulo: Blucher, 2021. '
    'p. 1647-1659. (Blucher Engineering Proceedings). '
    'DOI: 10.5151/v-enei-731.',
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
    'UNIÃO EUROPEIA. Conselho da União Europeia. Decisão (UE) 2026/183 do Conselho, '
    'de 9 de janeiro de 2026, relativa à assinatura e à aplicação provisória do '
    'Acordo Provisório sobre Comércio entre a União Europeia, por um lado, e o '
    'Mercado Comum do Sul, a República Argentina, a República Federativa do Brasil, '
    'a República do Paraguai e a República Oriental do Uruguai, por outro. '
    '<i>Jornal Oficial da União Europeia</i>, L, 2026/183, 27 fev. 2026.',
    'UNIÃO EUROPEIA. Conselho da União Europeia. Decisão (UE) 2026/185 do Conselho, '
    'de 9 de janeiro de 2026, relativa à assinatura, em nome da União, e à '
    'aplicação provisória do Acordo de Parceria entre a União Europeia e os seus '
    'Estados-Membros, por um lado, e o Mercado Comum do Sul e seus Estados-Partes, '
    'por outro. <i>Jornal Oficial da União Europeia</i>, L, 2026/185, '
    '27 fev. 2026.',
    'TRIBUNAL DE JUSTIÇA DA UNIÃO EUROPEIA. <i>Processo C-460/26</i>: República da '
    'Polónia contra Conselho da União Europeia. Comunicação de ação. <i>Jornal '
    'Oficial da União Europeia</i>, C, 2026/3166, 2026. Despacho de medidas '
    'provisórias no Processo C-460/26 R, de 29 de setembro de 2026.',
    'UNIÃO EUROPEIA; MERCOSUL. <i>Acordo Provisório sobre Comércio entre a União '
    'Europeia, por um lado, e o Mercado Comum do Sul, a República Argentina, a '
    'República Federativa do Brasil, a República do Paraguai e a República Oriental '
    'do Uruguai, por outro</i>. Assinado em Assunção, 17 de janeiro de 2026. '
    '<i>Jornal Oficial da União Europeia</i>, L, 2026/184, 27 fev. 2026. Apêndice '
    '2-A-1: cronograma de desgravação tarifária da União Europeia.',
    'ACORDO Mercosul-UE entra em vigor no dia 1º: lições e apontamentos. '
    '<i>Consultor Jurídico</i>, São Paulo, 29 abr. 2026. Coluna Território '
    'Aduaneiro. Entrada pelo título: a página não identifica a autoria da coluna.',
    'TJUE rejeita pedido da Polônia contra aplicação provisória do acordo '
    'Mercosul-UE. <i>Canal Rural</i>, 29 set. 2026. Fonte: Estadão Conteúdo.',
]:
    S.append(P(r, 'Refx'))

# ===================================================================== BUILD
def build():
    nomes = [n for n, _ in ALUNOS]
    autores = nomes[0] if len(nomes) == 1 else \
        ', '.join(nomes[:-1]) + ' e ' + nomes[-1]
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
