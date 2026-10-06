"""
Gera o PDF e o Markdown das três provas dissertativas com gabarito COMPLETO.

Esta é a edição completa de `provas-dissertativas-com-gabarito.pdf`: reproduz as
três provas e todos os gabaritos da primeira versão e acrescenta os blocos que
faltavam. Todo bloco novo vem marcado com "[acrescentado]" no título.

O conteúdo fica na lista DOC, em blocos ('tipo', dados). Dois renderizadores
consomem a mesma lista — um gera o PDF (ReportLab, estilo_pdf.py), o outro gera
o Markdown —, de modo que o texto é escrito uma única vez.

Uso: python3 gerar_provas_pdf.py
Saída: provas-dissertativas-gabarito-completo.pdf
       provas-dissertativas-gabarito-completo.md
"""
import os
import re

from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import KeepTogether, PageBreak, Spacer

from estilo_pdf import (
    BLUE, CONTENT_W, GOLD, GREEN, LIGHT_BLUE, LIGHT_GREEN, LIGHT_PURPLE,
    LIGHT_RED, NAVY, PURPLE, RED, P, build_pdf, bullets, cover, note, rule,
    table,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(ROOT, 'provas-dissertativas-gabarito-completo.pdf')
MD = os.path.join(ROOT, 'provas-dissertativas-gabarito-completo.md')

TITULO = 'Três provas dissertativas — gabarito completo'

PALETAS = {
    'azul': (LIGHT_BLUE, BLUE),
    'verde': (LIGHT_GREEN, GREEN),
    'vermelho': (LIGHT_RED, RED),
    'roxo': (LIGHT_PURPLE, PURPLE),
    'ouro': (GOLD, colors.HexColor('#D6B656')),
}

# Larguras de coluna reaproveitadas
W_PONTOS = [CONTENT_W - 2.0 * cm, 2.0 * cm]
W_TRES = [CONTENT_W * .40, CONTENT_W * .40, CONTENT_W * .20]

NOVO = '  <font color="#A61C00">[acrescentado]</font>'


# ===========================================================================
# RENDERIZADORES
# ===========================================================================
def _md_inline(t):
    t = t.replace('<br/>', '  \n').replace('<br />', '  \n')
    t = re.sub(r'</?b>', '**', t)
    t = re.sub(r'</?i>', '*', t)
    t = re.sub(r'<font[^>]*>', '', t)
    t = t.replace('</font>', '')
    t = t.replace('&amp;', '&')
    return t.strip()


def render_pdf(doc):
    S = []
    for bloco in doc:
        tipo, dados = bloco[0], bloco[1:]
        if tipo == 'capa':
            titulo, sub, linhas, caixa = dados[0]
            badge = None
            if caixa:
                bg, bd = PALETAS[caixa[2]]
                badge = note(caixa[0], caixa[1], bg, bd, width=CONTENT_W * .88)
            S += cover(titulo, sub, linhas, badge=badge)
        elif tipo in ('h1', 'h2', 'h3'):
            estilo = {'h1': 'H1x', 'h2': 'H2x', 'h3': 'H3x'}[tipo]
            S += [P(dados[0], estilo)]
        elif tipo == 'p':
            S += [P(dados[0], 'Bodyx')]
        elif tipo == 'small':
            S += [P(dados[0], 'Smallx')]
        elif tipo == 'toc':
            S += [P(linha, 'TOC') for linha in dados[0]]
        elif tipo == 'bullets':
            S += bullets(dados[0])
        elif tipo == 'note':
            titulo, linhas, paleta = dados[0]
            bg, bd = PALETAS[paleta]
            # KeepTogether impede que o título da caixa fique órfão numa página
            # e o corpo escorregue para a seguinte.
            S += [KeepTogether(note(titulo, linhas, bg, bd))]
        elif tipo == 'table':
            linhas, widths = dados[0]
            S += table(linhas, widths)
        elif tipo == 'rule':
            S += rule()
        elif tipo == 'pagebreak':
            S += [PageBreak()]
        elif tipo == 'space':
            S += [Spacer(1, dados[0] * cm)]
    return S


def _md_quote(titulo, linhas):
    """Citação em bloco: título em negrito e corpo, sem linhas vazias internas."""
    partes = ['> **' + _md_inline(titulo) + '**']
    for linha in linhas:
        partes.append('>')
        partes.append('> ' + _md_inline(linha).replace('\n', '\n> '))
    return '\n'.join(partes)


def render_md(doc):
    out = []
    for bloco in doc:
        tipo, dados = bloco[0], bloco[1:]
        if tipo == 'capa':
            titulo, sub, linhas, caixa = dados[0]
            out.append('# ' + _md_inline(titulo))
            out.append('**' + _md_inline(sub) + '**')
            out.append('  \n'.join(_md_inline(l) for l in linhas))
            if caixa:
                out.append(_md_quote(caixa[0], caixa[1]))
        elif tipo == 'h1':
            out.append('\n## ' + _md_inline(dados[0]))
        elif tipo == 'h2':
            out.append('\n### ' + _md_inline(dados[0]))
        elif tipo == 'h3':
            out.append('\n#### ' + _md_inline(dados[0]))
        elif tipo in ('p', 'small'):
            out.append(_md_inline(dados[0]))
        elif tipo == 'toc':
            out.append('\n'.join('- ' + _md_inline(l) for l in dados[0]))
        elif tipo == 'bullets':
            itens = []
            for item in dados[0]:
                if item.startswith('>'):
                    itens.append('    - ' + _md_inline(item[1:]))
                else:
                    itens.append('- ' + _md_inline(item))
            out.append('\n'.join(itens))
        elif tipo == 'note':
            titulo, linhas, _ = dados[0]
            out.append(_md_quote(titulo, linhas))
        elif tipo == 'table':
            linhas = dados[0][0]
            cab = ['**' + _md_inline(str(c)) + '**' for c in linhas[0]]
            out.append('| ' + ' | '.join(cab) + ' |')
            out.append('|' + '---|' * len(cab))
            for linha in linhas[1:]:
                celulas = [_md_inline(str(c)).replace('\n', '<br>') for c in linha]
                out.append('| ' + ' | '.join(celulas) + ' |')
        elif tipo == 'rule':
            out.append('\n---')
    return '\n\n'.join(out) + '\n'


DOC = []


def H1(t):
    DOC.append(('h1', t))


def H2(t):
    DOC.append(('h2', t))


def H3(t):
    DOC.append(('h3', t))


def TXT(t):
    DOC.append(('p', t))


def LST(items):
    DOC.append(('bullets', items))


def BOX(titulo, linhas, paleta='ouro'):
    DOC.append(('note', (titulo, linhas if isinstance(linhas, list) else [linhas], paleta)))


def TAB(linhas, widths=None):
    DOC.append(('table', (linhas, widths or W_PONTOS)))


def RULE():
    DOC.append(('rule',))


def BREAK():
    DOC.append(('pagebreak',))


def PONTOS(itens):
    """Tabela Item | Pontos a partir de pares (texto, pontos)."""
    TAB([['Item', 'Pontos']] + [[t, str(p)] for t, p in itens])


# ===========================================================================
# CAPA E SUMÁRIO
# ===========================================================================
DOC.append(('capa', (
    'Três provas dissertativas',
    'Gabarito completo — todos os itens',
    [
        'Pontos 1 e 2 do programa · <b>Seis autores, uma linha</b>',
        '100 pontos e 2 horas por prova',
    ],
    ('Como usar', [
        'A <b>Parte I</b> traz as três provas; a <b>Parte II</b>, os gabaritos. Resolva primeiro, '
        'por escrito e no tempo, <b>sem olhar a Parte II</b> — gabarito lido antes de tentar não '
        'treina nada.',
        'Cada gabarito tem cinco blocos: <b>o que a questão pede</b>, a <b>distribuição de pontos</b> '
        'item por item, uma <b>resposta-modelo</b>, os <b>erros que mais custam nota</b> e os '
        '<b>pontos de diferenciação</b>.',
        'Esta edição <b>completa a versão anterior</b>: os blocos que faltavam foram escritos e vêm '
        'marcados com <b>[acrescentado]</b>. Agora as nove questões têm os cinco blocos — e a '
        '<b>resposta-modelo é individual para cada alínea</b>, sem sínteses que juntem itens.',
    ], 'azul'),
)))

DOC.append(('space', 0.8))
H2('Sumário')
DOC.append(('toc', [
    '<b>Parte I</b> — As provas',
    '<b>Prova 1</b> — O sentido da colonização e o Antigo Sistema Colonial',
    '<b>Prova 2</b> — O Estado português: patrimonialismo, fisco e expansão',
    '<b>Prova 3</b> — Escala, Estado e o que havia antes',
    '<b>Parte II</b> — Gabaritos (com o mapa de cobertura)',
    '<b>Apêndice A</b> — Os dez erros clássicos',
    '<b>Apêndice B</b> — Quadro de autoavaliação',
]))
BREAK()

# ===========================================================================
# PARTE I — AS PROVAS
# ===========================================================================
H1('Parte I — As provas')
TXT(
    'Simulados sobre os pontos 1 e 2 do programa, no formato dissertativo. Cada prova tem três '
    'questões, 100 pontos e duração sugerida de 2 horas. Os excertos de fontes vêm sintetizados, '
    'como é de regra em prova — na resposta, trate-os como o documento integral.')

# --- PROVA 1 ---------------------------------------------------------------
H2('Prova 1 — O sentido da colonização e o Antigo Sistema Colonial')
DOC.append(('small', 'Pontos 1.1, 1.2 e 1.3 do programa · 100 pontos · 2 horas'))

H3('Questão 1 (40 pontos)')
BOX('Caio Prado Jr., <i>Formação do Brasil Contemporâneo</i> (1942), cap. “O sentido da colonização”',
    '“Se vamos à essência da nossa formação, veremos que na realidade nos constituímos para fornecer '
    'açúcar, tabaco, alguns outros gêneros; [...] para o comércio europeu. <b>Nada mais que isto.</b>”',
    'azul')
LST([
    '<b>a)</b> Explique o que Caio Prado entende por “sentido da colonização”, deixando claro por que '
    'essa categoria não se confunde com a <b>intenção</b> dos colonizadores. <b>(12 pontos)</b>',
    '<b>b)</b> Demonstre por que a formulação de Caio Prado é incompatível com a tese de um Brasil '
    'colonial <b>feudal</b>, e indique a consequência dessa incompatibilidade para o debate '
    'historiográfico e político de sua época. <b>(12 pontos)</b>',
    '<b>c)</b> Fernando Novais reformula o “sentido” como “sistema”. Identifique o <b>mecanismo '
    'específico</b> que ele acrescenta e a <b>contradição interna</b> que, segundo ele, conduz esse '
    'sistema à crise. <b>(16 pontos)</b>',
])

H3('Questão 2 (35 pontos)')
TXT(
    'Fragoso, Bicalho e Gouvêa propõem ler o Brasil colonial a partir das <b>bases da materialidade '
    'e da governabilidade</b> no império.')
LST([
    '<b>a)</b> Explique cada uma das duas bases, indicando o tipo de <b>evidência empírica</b> que as '
    'sustenta. <b>(15 pontos)</b>',
    '<b>b)</b> Explicite o <b>deslocamento de unidade de análise</b> que essa leitura implica em '
    'relação a Caio Prado e Novais. <b>(8 pontos)</b>',
    '<b>c)</b> Posicione-se de forma justificada: essa leitura <b>refuta</b> ou <b>redimensiona</b> a '
    'interpretação clássica? Em sua resposta, distinga os <b>níveis</b> em que a crítica opera '
    '(empírico, metodológico, teórico). <b>(12 pontos)</b>',
])

H3('Questão 3 (25 pontos)')
BOX('Frei Vicente do Salvador, <i>História do Brasil</i> (1627) — excerto sintetizado',
    'O frade censura os moradores da colônia por usarem a terra não como <b>senhores</b>, mas como '
    '<b>usufrutuários</b>: vivem voltados para o litoral e para o reino, como se estivessem de '
    'passagem, contentando-se de “andar arranhando a terra como caranguejos”, sem penetrar o interior '
    'nem edificar nada duradouro.',
    'azul')
LST([
    '<b>a)</b> Comente a fonte à luz da tese do “sentido da colonização”. <b>(13 pontos)</b>',
    '<b>b)</b> Aponte um <b>limite</b> do uso desse documento como prova do argumento de Caio Prado, '
    'levando em conta a natureza do texto e de quem o escreve. <b>(12 pontos)</b>',
])
BREAK()

# --- PROVA 2 ---------------------------------------------------------------
H2('Prova 2 — O Estado português: patrimonialismo, fisco e expansão')
DOC.append(('small', 'Pontos 2.1 e 2.2 do programa · 100 pontos · 2 horas'))

H3('Questão 1 (40 pontos)')
TXT('“<b>Patrimonialismo ou feudalismo?</b>” Responda a essa questão a partir de Raimundo Faoro.')
LST([
    '<b>a)</b> Defina com precisão os três conceitos weberianos que ele mobiliza: '
    '<b>patrimonialismo</b>, <b>estamento</b> e <b>capitalismo politicamente orientado</b>. '
    '<b>(15 pontos)</b>',
    '<b>b)</b> Reconstitua a <b>evidência histórica</b> que Faoro usa para sustentar que Portugal não '
    'conheceu o feudalismo pleno, mencionando ao menos <b>três elementos concretos</b>. '
    '<b>(15 pontos)</b>',
    '<b>c)</b> Explique por que, para Faoro, a <b>Revolução de Avis</b> (1383-85) não produziu uma '
    'burguesia autônoma, mas um Estado que absorveu o comércio. <b>(10 pontos)</b>',
])

H3('Questão 2 (35 pontos)')
TXT(
    'Vitorino Magalhães Godinho propõe compreender a formação do Estado português por suas '
    '<b>finanças públicas</b>.')
LST([
    '<b>a)</b> Reconstitua o argumento: qual era a <b>base de receita</b> da Coroa, que <b>pressões</b> '
    'a tornavam insuficiente e como o <b>ultramar</b> alterou essa estrutura? <b>(15 pontos)</b>',
    '<b>b)</b> Explique de que maneira essa abordagem <b>sustenta</b> a tese de Faoro. '
    '<b>(10 pontos)</b>',
    '<b>c)</b> Explique de que maneira ela <b>qualifica ou limita</b> a mesma tese. <b>(10 pontos)</b>',
])

H3('Questão 3 (25 pontos)')
BOX('Zurara, <i>Crónica do descobrimento e conquista de Guiné</i> (1453), cap. VII — síntese do conteúdo',
    'O cronista enumera as razões pelas quais o Infante D. Henrique mandou buscar as terras da Guiné: '
    'conhecer as terras situadas além do Cabo; estabelecer comércio com eventuais cristãos ali '
    'existentes; avaliar a extensão real do poder dos “infiéis”; encontrar algum príncipe cristão que '
    'o auxiliasse contra eles; e difundir a fé, salvando almas. A tudo isso o cronista acrescenta a '
    'inclinação pessoal do Infante, atribuída à sua constituição e à influência dos astros.',
    'azul')
LST([
    '<b>a)</b> A fonte <b>confirma</b> ou <b>contraria</b> as explicações econômicas da expansão '
    'marítima? Justifique. <b>(13 pontos)</b>',
    '<b>b)</b> Discuta a relação entre as <b>razões declaradas</b> numa fonte e as <b>determinações '
    'estruturais</b> identificadas pelo historiador, mobilizando Godinho e/ou Boxer. '
    '<b>(12 pontos)</b>',
])
BREAK()

# --- PROVA 3 ---------------------------------------------------------------
H2('Prova 3 — Escala, Estado e o que havia antes')
DOC.append(('small', 'Pontos 1.3, 2.2 e 2.3 do programa · prova integradora · 100 pontos · 2 horas'))

H3('Questão 1 (35 pontos)')
LST([
    '<b>a)</b> Explique a crítica de Eduardo Góes Neves ao <b>determinismo ambiental</b> na arqueologia '
    'amazônica, apresentando ao menos <b>três tipos de evidência</b> e indicando, para cada um, '
    '<b>o que ele refuta</b>. <b>(18 pontos)</b>',
    '<b>b)</b> Explique a tese da <b>floresta como produto histórico</b> e sua consequência para a '
    '<b>periodização</b> da história do Brasil. <b>(9 pontos)</b>',
    '<b>c)</b> Segundo a <b>teoria da circunscrição</b> de Carneiro (1970), por que a ausência de '
    '“cerco” na Amazônia é relevante para compará-la à formação do Estado português? '
    '<b>(8 pontos)</b>',
])

H3('Questão 2 (40 pontos)')
TXT(
    'O quadro “Seis autores, uma linha” organiza os autores do programa por <b>unidade de análise</b>: '
    'a colônia (Caio Prado), o Antigo Sistema Colonial (Novais), o império como um todo (Fragoso '
    '<i>et al.</i>), o Estado português (Faoro), as finanças públicas (Godinho) e a floresta (Neves).')
TXT('Escolha <b>três</b> desses autores e, para cada um, demonstre:')
LST([
    'qual <b>pergunta</b> a unidade de análise escolhida permite responder;',
    'como essa escolha <b>determina a tese</b> sustentada;',
    'o que a escolha <b>torna invisível</b>.',
])
TXT(
    'Conclua avaliando se as divergências entre os três autores escolhidos são '
    '<b>incompatibilidades reais</b> ou <b>efeitos de escala</b>.')

H3('Questão 3 (25 pontos)')
BOX('Afirmação para análise',
    '“A colônia existia para o mercado europeu.”', 'vermelho')
TXT(
    'A afirmação é <b>verdadeira</b>, <b>falsa</b> ou <b>insuficiente</b>? Defenda uma posição, '
    'mobilizando pelo menos <b>três autores</b> do programa e justificando a escolha do qualificativo.')
BREAK()

# ===========================================================================
# PARTE II — GABARITOS
# ===========================================================================
H1('Parte II — Gabaritos')
TXT(
    'Cada questão tem cinco blocos. <b>O que a questão pede</b> explicita a operação intelectual '
    'cobrada. A <b>distribuição dos pontos</b> lista os itens que o corretor procura, com o valor de '
    'cada um — use-a como <i>checklist</i> ao se corrigir. A <b>resposta-modelo</b> mostra o texto '
    'redigido, não apenas o tópico. Os <b>erros que mais custam nota</b> e os <b>pontos de '
    'diferenciação</b> indicam, respectivamente, onde se perde e onde se ganha a nota alta.')

H2('Mapa de cobertura desta edição')
TXT(
    'A primeira versão trazia a distribuição de pontos de todas as questões, mas só parte dos outros '
    'blocos. A tabela mostra o que já existia (<b>✓</b>) e o que foi escrito agora (<b>+</b>).')
TAB([
    ['Questão', 'O que pede', 'Pontos', 'Resposta-modelo (por item)', 'Erros', 'Diferenciação'],
    ['<b>Prova 1 · Q1</b>', '✓', '✓', 'a <b>+</b> · b <b>+</b> · c ✓', '✓', '✓'],
    ['<b>Prova 1 · Q2</b>', '<b>+</b>', '✓', 'a <b>+</b> · b <b>+</b> · c ✓', '✓', '<b>+</b>'],
    ['<b>Prova 1 · Q3</b>', '<b>+</b>', '✓', 'a <b>+</b> · b <b>+</b>', '<b>+</b>', '✓'],
    ['<b>Prova 2 · Q1</b>', '✓', '✓',
     'a <b>+</b> · b <b>+</b> · c <b>+</b><br/><i>antes: síntese única das três</i>', '✓', '✓'],
    ['<b>Prova 2 · Q2</b>', '<b>+</b>', '✓',
     'a <b>+</b> · b ✓ · c <b>+</b><br/><i>antes: b e c num bloco só</i>', '✓', '<b>+</b>'],
    ['<b>Prova 2 · Q3</b>', '<b>+</b>', '✓', 'a <b>+</b> · b <b>+</b>', '<b>+</b>', '✓'],
    ['<b>Prova 3 · Q1</b>', '<b>+</b>', '✓', 'a <b>+</b> · b <b>+</b> · c <b>+</b>', '<b>+</b>', '✓'],
    ['<b>Prova 3 · Q2</b>', '✓', '✓',
     'corpo <b>+</b> · conclusão ✓<br/><i>+ repertório dos seis autores</i>', '✓', '<b>+</b>'],
    ['<b>Prova 3 · Q3</b>', '✓', '✓', 'questão sem alíneas ✓', '<b>+</b>', '✓'],
], [CONTENT_W * .15, CONTENT_W * .12, CONTENT_W * .09, CONTENT_W * .34,
    CONTENT_W * .10, CONTENT_W * .20])
BOX('Resposta-modelo de todos os itens',
    'Na primeira versão, três questões tinham resposta-modelo <b>agrupada</b>: a Prova 2 · Q1 trazia '
    'uma síntese única das alíneas a, b e c; a Prova 2 · Q2 juntava b e c num só bloco; e a Prova 3 · '
    'Q2 só desenvolvia a conclusão, deixando o corpo da resposta — os três autores — por escrever. '
    'Agora <b>cada alínea tem a sua própria resposta-modelo</b>, redigida para cobrir exatamente os '
    'itens pontuados daquela alínea. São <b>22 respostas-modelo</b> no total.', 'ouro')
TXT(
    'Acrescentou-se também o <b>Apêndice A</b>, com a lista dos dez erros clássicos — que o quadro de '
    'autoavaliação da primeira versão citava sem apresentar.')
RULE()

# ===========================================================================
# GABARITO — PROVA 1
# ===========================================================================
H1('Gabarito — Prova 1')

# --- Q1 --------------------------------------------------------------------
H2('Questão 1 (40 pontos)')
BOX('O que a questão pede',
    'Um percurso em três etapas: <b>definir</b> o conceito com precisão (a), entender sua <b>função '
    'polêmica</b> (b) e mostrar a <b>reformulação</b> de Novais (c). A questão testa se você sabe que '
    '“sentido” é categoria <b>estrutural</b> e que Novais acrescenta <b>mecanismo</b> e '
    '<b>dinâmica</b>.', 'verde')

H3('a) Distribuição dos pontos (12)')
PONTOS([
    ('Definir “sentido” como <b>linha dominante e objetiva</b> de evolução, apreensível quando se '
     'olha o processo “a distância”', 4),
    ('Afirmar que a colonização é capítulo da expansão <b>comercial</b> europeia — empresa, não '
     'povoamento', 3),
    ('Distinguir <b>sentido ≠ intenção</b>: é a lógica objetiva do conjunto, independente da vontade '
     'dos agentes', 3),
    ('Indicar a <b>função metodológica</b>: o sentido organiza a explicação do povoamento, da vida '
     'material e da vida social', 2),
])

H3('b) Distribuição dos pontos (12)')
PONTOS([
    ('Feudalismo supõe economia de base senhorial, voltada ao consumo interno e à renda da terra; a '
     'colônia nasce <b>voltada ao mercado</b> e produzindo mercadoria', 4),
    ('A colônia é, desde a origem, engrenagem de um circuito <b>mercantil</b> — portanto não há etapa '
     'feudal a ser superada', 3),
    ('Consequência historiográfica: ruptura com a leitura institucional-narrativa e com a culturalista '
     '(Freyre, Sérgio Buarque), deslocando a explicação para a economia', 2),
    ('Consequência política: invalida o diagnóstico de uma revolução “anti-feudal” necessária — tese '
     'que Caio Prado desenvolverá em <i>A Revolução Brasileira</i> (1966)', 3),
])

H3('c) Distribuição dos pontos (16)')
PONTOS([
    ('Nomear o mecanismo: o <b>exclusivo metropolitano</b>', 3),
    ('Explicar sua mecânica: monopólio da intermediação que fixa preço <b>nas duas pontas</b> (vende '
     'insumos e escravos caro, compra a produção barato) → <b>troca desigual</b> e transferência de '
     'excedente', 5),
    ('Situar a função no sistema: <b>acumulação primitiva</b> em escala europeia, beneficiando o '
     'capital mercantil metropolitano e, via fisco, o Estado absolutista', 3),
    ('Enunciar a contradição: a acumulação gera o capital industrial, que exige mercados abertos e '
     'trabalho livre — e para o qual o exclusivo se torna <b>obstáculo</b>', 4),
    ('Concluir que a crise é <b>estrutural</b>, não conjuntural: “o sistema engendra a sua própria '
     'negação”', 1),
])

H3('Resposta-modelo condensada (item a)' + NOVO)
TXT(
    'Caio Prado não pergunta o que os colonizadores <i>quiseram</i> fazer, e sim o que, no conjunto, '
    'eles <i>acabaram</i> fazendo. “Sentido” designa a linha dominante e objetiva de evolução de um '
    'povo, apreensível apenas quando se observa o processo “a distância” — isto é, quando se abandona '
    'o detalhe cronológico e se procura a regularidade que ordena três séculos. No caso brasileiro, '
    'essa linha é uma só: a colonização dos trópicos é capítulo da <b>expansão comercial</b> europeia, '
    'e a colônia se constitui como <b>empresa</b> destinada a fornecer gêneros de alto valor ao '
    'mercado europeu — não como projeto de povoamento nem como transplante da sociedade metropolitana.')
TXT(
    'Daí a distinção decisiva entre <b>sentido</b> e <b>intenção</b>. O sentido não está na cabeça de '
    'nenhum agente: nem o donatário, nem o senhor de engenho, nem o rei precisam tê-lo formulado, e '
    'cada um pode ter perseguido fins próprios e até divergentes. Trata-se da lógica objetiva do '
    'conjunto, que se impõe aos participantes independentemente do que eles creiam estar fazendo, e '
    'que se revela ao historiador retrospectivamente. É por isso que a categoria resiste à objeção de '
    'que havia colonos querendo ficar: o sentido é um resultado estrutural, não uma soma de desejos.')
TXT(
    'A função da categoria é <b>metodológica</b>. O sentido é o princípio ordenador a partir do qual '
    'Prado deduz e organiza os três grandes blocos do livro — o povoamento, a vida material e a vida '
    'social. Tudo o que vem depois é derivação: grande lavoura, latifúndio, escravidão, instabilidade '
    'social. O conceito não é, portanto, uma tese entre outras; é a chave que torna o livro um sistema '
    'explicativo em vez de uma narrativa.')

H3('Resposta-modelo condensada (item b)' + NOVO)
TXT(
    'Feudalismo designa uma economia de base senhorial: produção voltada primariamente ao consumo do '
    'próprio domínio, excedente apropriado como <b>renda da terra</b>, trabalhador servil adscrito ao '
    'solo e <b>soberania fragmentada</b> entre senhores com jurisdição própria. A colônia brasileira '
    'não corresponde a nenhum desses elementos no que eles têm de essencial. Ela nasce produzindo '
    '<b>mercadoria</b> para um mercado distante; o seu produto é açúcar destinado a Lisboa e a '
    'Antuérpia, não grão para o celeiro senhorial; o seu trabalhador é escravo <b>comprado</b> — ele '
    'mesmo mercadoria importada —, e não servo preso à gleba; e a terra vale pelo que exporta.')
TXT(
    'A incompatibilidade, portanto, não é de grau nem de cronologia: a colônia é, desde a origem, '
    'engrenagem de um circuito mercantil. Não existe no Brasil uma “etapa feudal” a ser superada, '
    'porque nunca houve transição a completar.')
TXT(
    'A consequência <b>historiográfica</b> é o deslocamento do eixo da explicação. Prado rompe '
    'simultaneamente com a história institucional-narrativa, que explicava o Brasil por leis, '
    'capitanias e governadores, e com a leitura culturalista de Gilberto Freyre e Sérgio Buarque de '
    'Holanda, que o explicava por herança ibérica, caráter e relações domésticas. A explicação passa à '
    'economia e à posição do país na divisão internacional do trabalho.')
TXT(
    'A consequência <b>política</b> é igualmente direta, e explica a temperatura do debate entre os '
    'anos 1940 e 1960. Se não há feudalismo, não há latifúndio pré-capitalista a ser destruído por uma '
    'revolução democrático-burguesa em aliança com a burguesia nacional — que era o programa então '
    'sustentado pelo PCB. O atraso brasileiro deixa de ser resíduo feudal e passa a ser produto do '
    'próprio capitalismo, o que muda o inimigo e o sujeito da transformação. Prado extrairá a '
    'conclusão de forma explícita em <i>A Revolução Brasileira</i> (1966).')

H3('Resposta-modelo condensada (item c)')
TXT(
    'Novais converte o “sentido” em <b>sistema</b>, dotado de estrutura e dinâmica. A estrutura tem '
    'por nervo o <b>exclusivo metropolitano</b>: o monopólio da intermediação comercial da colônia, '
    'que permite ao comerciante metropolitano fixar simultaneamente o preço de venda dos insumos — '
    'manufaturas, sal, ferramentas e, decisivamente, escravos — e o preço de compra da produção '
    'colonial. Daí resulta <b>troca desigual</b> e transferência contínua de excedente, sem '
    'necessidade de confisco: a drenagem é efeito da própria estrutura de mercado. Esse excedente '
    'alimenta a <b>acumulação primitiva</b> europeia, apropriado pelo capital mercantil e, pela '
    'tributação, pelo Estado absolutista.')
TXT(
    'A escravidão é peça necessária, e por duas razões: o trabalho livre exigiria salário e consumo, '
    'isto é, um mercado interno colonial incompatível com o exclusivo; e o cativo é ele mesmo '
    'mercadoria importada, fazendo do tráfico um dos ramos mais lucrativos do conjunto — a dupla '
    'articulação entre <i>plantation</i> e tráfico no tripé metrópole–colônia–África.')
TXT(
    'A contradição é <b>interna</b>: ao produzir a acumulação que viabiliza o capitalismo industrial, '
    'o sistema cria o agente que exige o seu oposto — mercados amplos e abertos, insumos baratos, '
    'trabalho livre. As instituições que geraram a acumulação tornam-se obstáculo à sua continuidade. '
    'A crise de 1776-1808 é, por isso, estrutural: a Revolução Francesa, o Haiti e as independências '
    'são a sua <b>forma</b>, não a sua <b>causa</b>.')

BOX('Erros que mais custam nota',
    'Tratar o exclusivo como imposto ou como exclusividade de rotas (perde-se o essencial: o poder de '
    'fixar preços nas duas pontas). Apresentar a escravidão como atraso ou resíduo pré-capitalista — '
    'Novais afirma o contrário. Explicar a crise apenas por eventos externos. Dizer que Novais apenas '
    'repete Caio Prado. Em (a), confundir sentido com intenção, que é exatamente o que a questão pede '
    'para distinguir.', 'vermelho')
BOX('Pontos de diferenciação',
    'Observar que “<b>nada mais que isto</b>”, no excerto, é uma afirmação de <b>suficiência '
    'explicativa</b> — e que é precisamente essa suficiência, não a existência da exportação, que '
    'será contestada depois. Notar também que Prado e Novais respondem a perguntas distintas: Prado '
    'parte da colônia para explicar o <b>Brasil</b>; Novais parte do sistema para explicar a '
    '<b>transição europeia</b>.', 'azul')
BREAK()

# --- Q2 --------------------------------------------------------------------
H2('Questão 2 (35 pontos)')
BOX('O que a questão pede' + NOVO,
    'Domínio do artigo em dois planos: o <b>conteúdo</b> (as duas bases e a evidência que as sustenta) '
    'e a <b>operação metodológica</b> (a mudança de unidade de análise). O item (c) é o que separa as '
    'respostas: não pede opinião, e sim que você <b>hierarquize os níveis</b> em que uma crítica '
    'historiográfica pode operar. Responder “refuta” ou “redimensiona” sem essa distinção custa a '
    'maior parte dos pontos do item.', 'verde')

H3('a) Distribuição dos pontos (15)')
PONTOS([
    ('<b>Materialidade</b>: setor de abastecimento de grande porte; circuitos intra e intercoloniais '
     '(Rio–Angola, Rio–Prata, Rio–Minas, Bahia–Costa da Mina); acumulação endógena; centralidade do '
     '<b>crédito</b> colonial', 6),
    ('<b>Governabilidade</b>: economia da mercê (serviço → recompensa → poder local); corpos '
     'intermediários (câmaras, Misericórdias, irmandades, ordens militares); negociação entre Coroa e '
     'elites locais', 6),
    ('<b>Evidência empírica</b>: inventários <i>post-mortem</i>, registros notariais e de crédito, '
     'documentação camerária e paroquial', 3),
])

H3('b) Distribuição dos pontos (8)')
PONTOS([
    ('Identificar o deslocamento: da <b>colônia</b> como função / do <b>sistema</b> para o '
     '<b>império como um todo</b>, rede policêntrica', 4),
    ('Explicar a inversão do olhar: de <b>fora para dentro</b> passa a <b>dentro para fora</b>; a '
     'colônia ganha lógica própria de reprodução', 2),
    ('Mencionar a formulação da <b>monarquia pluricontinental</b> e o modelo '
     '<b>corporativo-jurisdicional</b> do Antigo Regime (Hespanha) como fundamento', 2),
])

H3('c) Distribuição dos pontos (12)')
PONTOS([
    ('Sustentar posição clara e argumentada (qualquer das duas é aceitável se bem defendida)', 3),
    ('Distinguir os níveis da crítica: <b>empírico</b> (dimensão do mercado interno e da acumulação '
     'local), <b>metodológico</b> (o “sentido” torna a sociedade ininteligível como sociedade), '
     '<b>teórico</b> (substituir a chave da acumulação primitiva pela do Antigo Regime corporativo)', 6),
    ('Reconhecer que eles não negam o exclusivo nem a <i>plantation</i>, mas o <b>monopólio '
     'explicativo</b>', 3),
])

H3('Resposta-modelo condensada (item a)' + NOVO)
TXT(
    '<b>Materialidade</b> é a base econômica da reprodução da sociedade colonial, e a tese é que ela é '
    'muito maior e muito mais interna do que a historiografia clássica supõe. Há um setor de '
    '<b>abastecimento</b> de grande porte — alimentos, animais de carga, transporte, construção, '
    'serviços urbanos — voltado ao mercado interno. Há circuitos mercantis que <b>não passam por '
    'Lisboa</b>: Rio–Angola, Rio–Prata, Rio–Minas, Bahia–Costa da Mina. Há acumulação <b>endógena</b>, '
    'com fortunas constituídas e reproduzidas na própria colônia. E há, no centro do arranjo, o '
    '<b>crédito colonial</b>, controlado por comerciantes locais que financiam a produção, o '
    'abastecimento e o próprio tráfico. Quem controla o crédito controla a economia: é esse o passo '
    'que converte o suposto “apêndice” em centro de decisão.')
TXT(
    '<b>Governabilidade</b> é a base política: como se governa um império dessa extensão sem '
    'burocracia moderna nem monopólio estatal da coerção. A resposta é a <b>economia da mercê</b> — a '
    'lógica serviço → recompensa → poder local, pela qual a Coroa remunera serviços com ofícios, '
    'tenças, hábitos das ordens e privilégios, produzindo elites que devem ao rei a sua posição e, '
    'simultaneamente, consolidam autonomia local. Entre a Coroa e os súditos operam <b>corpos '
    'intermediários</b> dotados de jurisdição própria: câmaras municipais, Misericórdias, irmandades, '
    'ordens militares. Governar, nesse arranjo, é <b>negociar</b> com eles — e a negociação inclui o '
    'conflito, inclusive armado.')
TXT(
    'A <b>evidência</b> é serial e local, e é isso que dá força ao argumento: inventários '
    '<i>post-mortem</i>, que revelam a composição das fortunas e o peso das dívidas ativas; registros '
    'notariais e de crédito; documentação camerária e paroquial. Não são fontes da administração '
    'central — e é precisamente por isso que mostram o que a documentação metropolitana não podia '
    'mostrar.')

H3('Resposta-modelo condensada (item b)' + NOVO)
TXT(
    'O deslocamento é de <b>unidade de análise</b>. Em Caio Prado, a unidade é a colônia lida no quadro '
    'da expansão europeia; em Novais, o <b>sistema</b>, do qual a colônia é peça funcional. Em ambos o '
    'eixo é bipolar — metrópole e colônia — e a direção do olhar vai de fora para dentro. Fragoso, '
    'Bicalho e Gouvêa adotam como unidade o <b>império como um todo</b>: uma rede <b>policêntrica</b> '
    'e pluricontinental, com vários núcleos de acumulação e de poder, em que o Rio de Janeiro se liga a '
    'Angola, ao Prata e a Minas sem precisar da mediação de Lisboa.')
TXT(
    'A consequência é a <b>inversão do olhar</b>: passa-se a observar de dentro para fora, e a colônia '
    'deixa de ser <i>função</i> para se tornar <i>sociedade</i> com lógica própria de reprodução. O '
    'fundamento é duplo: a formulação da <b>monarquia pluricontinental</b> e o modelo '
    '<b>corporativo-jurisdicional</b> do Antigo Regime (Hespanha), segundo o qual o poder régio não é '
    'proprietário da máquina administrativa, mas árbitro entre corpos com jurisdição própria. Daí o '
    'título-programa: um <i>Antigo Regime nos trópicos</i>.')

H3('Resposta-modelo condensada (item c)')
TXT(
    '<b>Redimensiona</b> mais do que refuta — e é preciso separar os níveis. No plano <b>empírico</b>, '
    'a crítica é devastadora: o volume do abastecimento, dos circuitos intracoloniais e das fortunas '
    'constituídas localmente é grande demais para caber na categoria de “apêndice”. No plano '
    '<b>metodológico</b>, a objeção é ainda mais forte e independe da quantificação: tomado como '
    'explicação suficiente, o “sentido” torna a sociedade colonial ininteligível <i>como sociedade</i>, '
    'pois ela passa a não ter lógica própria, apenas uma função — e uma sociedade que só tem função '
    'não tem história interna.')
TXT(
    'No plano <b>teórico</b>, porém, não há refutação, e sim troca de problema. Caio Prado e Novais '
    'explicam a <b>inserção</b> da colônia num circuito de acumulação; Fragoso, Bicalho e Gouvêa '
    'explicam a sua <b>reprodução interna</b>. São perguntas distintas, e a resposta de uma não '
    'invalida a da outra. Convém notar que os autores não negam o exclusivo nem a <i>plantation</i>: '
    'negam que expliquem tudo. A leitura que converte o artigo em “o Brasil não foi explorado” é '
    'caricatura.')
TXT(
    'Cabe, por fim, registrar o limite da própria revisão: boa parte da evidência provém da elite do '
    'Rio de Janeiro setecentista, e sua generalização para o conjunto da América portuguesa é um '
    'problema de escala não resolvido.')

BOX('Erros que mais custam nota',
    'Ler os autores como negadores da exploração colonial. Tomar “negociação” por harmonia — '
    'negociação é a <b>forma do conflito</b> e inclui a revolta armada (Vila Rica, 1720, é negociação '
    'rompida). Responder “refuta” ou “redimensiona” sem distinguir os níveis da crítica: é aí que se '
    'concentram os pontos.', 'vermelho')
BOX('Pontos de diferenciação' + NOVO,
    'Nomear o <b>crédito</b> como o centro do argumento, em vez de apenas listar “mercado interno”: é '
    'o controle do crédito por comerciantes coloniais que sustenta a tese da acumulação endógena. '
    'Explicitar a natureza <b>serial e local</b> das fontes e observar que o resultado depende do tipo '
    'de documento consultado — mudar a fonte muda a colônia que se vê. E aplicar aos revisionistas o '
    'mesmo rigor que eles aplicam aos clássicos, registrando que a base empírica é sobretudo a elite '
    'carioca setecentista: é o movimento que demonstra maturidade historiográfica.', 'azul')
BREAK()

# --- Q3 --------------------------------------------------------------------
H2('Questão 3 (25 pontos)')
BOX('O que a questão pede' + NOVO,
    'Uma questão de <b>método</b>, não de conteúdo. O item (a) pede que você use a fonte como '
    'evidência da tese; o item (b), que mostre por que ela <b>não a prova</b>. Os pontos se concentram '
    'em tratar o documento <i>como documento</i> — gênero, autor, intenção, limites — em vez de '
    'parafraseá-lo.', 'verde')

H3('a) Distribuição dos pontos (13)')
PONTOS([
    ('Ler a fonte como <b>testemunho contemporâneo</b> da economia extrovertida: orientação para o '
     'litoral e para o reino, ausência de projeto de povoamento', 5),
    ('Articular com a categoria de Caio Prado: a colônia como <b>empresa</b> e não como projeto de '
     'sociedade; o colono age como quem está de passagem', 4),
    ('Explorar a oposição <b>senhor × usufrutuário</b> como formulação, por um contemporâneo, daquilo '
     'que Caio Prado chamará de <b>ausência de nexo</b> e de caráter improvisado', 4),
])

H3('b) Distribuição dos pontos (12)')
PONTOS([
    ('Identificar a natureza do texto: é <b>normativo e moralizante</b>, não análise econômica — um '
     'frade franciscano censurando a falta de zelo e de virtude dos colonos', 5),
    ('Reconhecer que o documento tem <b>agenda própria</b>: a crítica supõe um dever de povoar e '
     'edificar, e serve a um projeto missionário e civilizador', 3),
    ('Apontar o risco de <b>circularidade</b>: usar como prova da tese um texto que já é, ele mesmo, '
     'juízo de valor sobre o fenômeno', 2),
    ('Observar que a própria existência da crítica demonstra que <b>havia quem pensasse</b> em '
     'povoamento e permanência — e que Fragoso <i>et al.</i> leriam o mesmo texto como evidência de '
     '<b>disputa de projetos</b>', 2),
])

H3('Resposta-modelo condensada (item a)' + NOVO)
TXT(
    'O excerto é um testemunho contemporâneo — e involuntário — daquilo que Caio Prado chamará, três '
    'séculos depois, de <b>sentido da colonização</b>. O frade descreve uma sociedade voltada para o '
    'litoral e para o reino, cujos membros se comportam como quem está de passagem: não penetram o '
    'interior, não edificam o que permaneça, contentam-se de “arranhar a terra como caranguejos”. A '
    'imagem registra, no plano da <b>conduta</b>, a estrutura que Prado descreverá no plano da '
    '<b>economia</b> — uma colônia organizada como empresa, e não como projeto de sociedade.')
TXT(
    'A oposição entre <b>senhor</b> e <b>usufrutuário</b> é especialmente eloquente: é a formulação '
    'seiscentista do que Prado chamará de ausência de nexo e de caráter improvisado da vida colonial. '
    'Quem usufrui não constrói instituições, porque não pretende ficar; e uma sociedade que não '
    'pretende ficar não desenvolve mercado interno, vida urbana nem coesão. O documento mostra, '
    'portanto, que a extroversão da colônia era perceptível aos contemporâneos como <b>comportamento</b> '
    'antes de ser teorizada como <b>estrutura</b>.')

H3('Resposta-modelo condensada (item b)' + NOVO)
TXT(
    'O limite está na natureza do texto e em quem o escreve. Não se trata de análise econômica, mas de '
    '<b>censura moral</b>: Frei Vicente é um religioso que repreende a falta de zelo, de virtude e de '
    'permanência dos colonos. A sua crítica pressupõe um <b>dever</b> — povoar, edificar, cristianizar '
    '— e serve a um projeto missionário e civilizador. O que para Prado é diagnóstico estrutural é, na '
    'fonte, acusação; e as duas coisas não se provam do mesmo modo.')
TXT(
    'Há, por isso, risco de <b>circularidade</b>: toma-se como evidência de um fenômeno um texto que '
    'já é, ele mesmo, juízo de valor sobre esse fenômeno. A fonte confirma a tese porque ambas partem '
    'da mesma premissa — que a colônia deveria ter sido outra coisa.')
TXT(
    'E há um efeito inverso, mais interessante: a própria existência da repreensão demonstra que '
    'havia, no século XVII, <b>quem pensasse</b> em povoamento e permanência. Isto é, o “sentido” não '
    'era unânime nem incontestado, e a colônia abrigava <b>projetos em disputa</b>. Fragoso, Bicalho e '
    'Gouvêa leriam o mesmo excerto exatamente assim. O documento prova que a extroversão era percebida '
    'e criticada; não prova que fosse a totalidade da vida colonial.')

BOX('Erros que mais custam nota' + NOVO,
    'Parafrasear o excerto em vez de interrogá-lo — é o erro central da questão. Tratar a fonte como '
    'prova suficiente da tese, sem perceber a circularidade. Em (b), apontar como limite apenas que o '
    'texto é “antigo”, “religioso” ou “subjetivo”: a crítica precisa ser específica quanto a gênero, '
    'autor e agenda. E esquecer que o mesmo documento sustenta a leitura oposta.', 'vermelho')
BOX('Pontos de diferenciação',
    'O movimento mais valorizado é <b>interrogar a fonte</b> em vez de parafraseá-la: quem escreve, '
    'para quem, com que interesse, e o que o documento <b>não pode</b> provar. Mostrar que o mesmo '
    'excerto sustenta duas leituras opostas — prova do “sentido” para Caio Prado, indício de projetos '
    'em disputa para os revisionistas — demonstra domínio do <b>debate</b>, e não apenas da fonte.',
    'azul')
BREAK()

# ===========================================================================
# GABARITO — PROVA 2
# ===========================================================================
H1('Gabarito — Prova 2')

# --- Q1 --------------------------------------------------------------------
H2('Questão 1 (40 pontos)')
BOX('O que a questão pede',
    'Rigor conceitual weberiano (a), ancoragem empírica (b) e compreensão do passo decisivo do '
    'argumento (c). É a questão em que a imprecisão no uso de “patrimonialismo” custa mais caro.',
    'verde')

H3('a) Distribuição dos pontos (15)')
PONTOS([
    ('<b>Patrimonialismo</b>: forma de dominação <b>tradicional</b> em que a administração é extensão '
     'da <b>casa do soberano</b> — quadros como dependentes pessoais, cargo como <b>prebenda</b>, '
     'ausência de separação entre patrimônio público e privado, de regra impessoal e de carreira por '
     'competência', 6),
    ('<b>Estamento</b>: estrato definido por <b>honra, estilo de vida e privilégio juridicamente '
     'garantido</b>, em contraste com <b>classe</b>, definida pela posição no mercado', 5),
    ('<b>Capitalismo politicamente orientado</b>: lucro obtido por oportunidades <b>garantidas '
     'politicamente</b> (monopólios, concessões, arrematação de tributos, fornecimento ao Estado), e '
     'não pela concorrência', 4),
])

H3('b) Distribuição dos pontos (15)')
PONTOS([
    ('<b>Reconquista</b>: território conquistado pela Coroa e distribuído <b>a partir dela</b>; o rei é '
     'a origem dos títulos e da jurisdição', 4),
    ('<b>Não fragmentação da soberania</b>: existem senhorios e doações, mas a jurisdição última '
     'permanece régia', 4),
    ('<b>Lei Mental (1434)</b>: as doações régias revertem à Coroa na falta de herdeiro varão direto — '
     'se a terra retorna sempre ao rei, não há senhorio autônomo', 4),
    ('<b>Monopólios régios</b> e expansão como <b>empresa da Coroa</b>: Casa da Guiné e Mina, Casa da '
     'Índia, estancos', 3),
])

H3('c) Distribuição dos pontos (10)')
PONTOS([
    ('Reconstituir 1383-85: crise dinástica, Avis ascendendo com apoio <b>urbano e mercantil</b> contra '
     'a alta nobreza castelhanizada', 3),
    ('Identificar o resultado: Estado <b>centralizado precocemente</b>, antes das demais monarquias '
     'nacionais', 2),
    ('Explicar o passo decisivo: quem comanda é a <b>Coroa</b>, não os mercadores — o apoio mercantil '
     'não gera burguesia autônoma, mas um Estado que <b>absorve</b> o comércio', 4),
    ('Concluir: sem burguesia autônoma, a riqueza passa pelo Estado e consolida-se o <b>estamento '
     'burocrático</b>, origem do patronato político brasileiro', 1),
])

H3('Resposta-modelo condensada (item a)' + NOVO)
TXT(
    'Faoro responde <b>patrimonialismo</b>, e a resposta é weberiana no sentido estrito. Os três '
    'conceitos precisam ser definidos com rigor, porque é da precisão deles que depende o resto do '
    'argumento.')
TXT(
    '<b>Patrimonialismo</b> é uma forma de <b>dominação tradicional</b> em que a administração é '
    'extensão da <b>casa do soberano</b>. Os quadros não são funcionários no sentido moderno, mas '
    'dependentes pessoais do senhor, recrutados por lealdade e confiança; o cargo é <b>prebenda</b> — '
    'fonte de renda apropriada por quem o ocupa —, e não função delimitada por competência. Faltam, '
    'por definição, a separação entre o patrimônio do rei e o do reino, a regra impessoal e a carreira '
    'por mérito. Importa dizer o que o conceito <b>não</b> é: não se trata de desvio moral nem de '
    'corrupção, mas de um <b>tipo de dominação legítima</b> — a acusação de corrupção pressuporia a '
    'norma impessoal que aqui simplesmente não existe.')
TXT(
    '<b>Estamento</b> designa um estrato social definido por <b>honra, estilo de vida e privilégio '
    'juridicamente garantido</b>: pertence-se a ele por qualidade reconhecida e protegida em direito, '
    'com acesso reservado a cargos, foros e distinções. O contraste é com <b>classe</b>, definida pela '
    'posição no <b>mercado</b> — pela propriedade e pela chance de obter renda. A distinção é decisiva '
    'para Faoro: um estamento se fecha e se reproduz pelo controle de posições no <b>Estado</b>, e não '
    'pela concorrência econômica.')
TXT(
    '<b>Capitalismo politicamente orientado</b> nomeia a obtenção de lucro por meio de oportunidades '
    '<b>garantidas politicamente</b>: monopólios e estancos, concessões, arrematação de tributos, '
    'contratos de fornecimento ao Estado, privilégios de rota. O ganho decorre da proximidade ao poder '
    'que distribui a oportunidade, não da eficiência na concorrência. É o tipo de capitalismo '
    'compatível com — e produzido por — a dominação patrimonial.')

H3('Resposta-modelo condensada (item b)' + NOVO)
TXT(
    'A evidência é <b>institucional</b>, e não cultural: Faoro não argumenta por temperamento ibérico, '
    'mas por estrutura jurídica de propriedade e de jurisdição.')
TXT(
    'A <b>Reconquista</b> é o ponto de partida. O território é conquistado sob comando régio e '
    '<b>distribuído a partir da Coroa</b>: o rei é a fonte dos títulos de propriedade e da jurisdição, '
    'e não o vértice de uma pirâmide de pactos entre pares. A terra chega ao senhor pela mão do '
    'monarca — não o monarca ao poder pela soma dos senhores.')
TXT(
    'Daí a <b>não fragmentação da soberania</b>. As formas senhoriais existem — doações, honras, '
    'coutos —, e Faoro não as nega; mas a jurisdição última permanece <b>régia</b>, e é isso que '
    'separa o caso português do feudalismo pleno. O senhor exerce poderes delegados e revogáveis, não '
    'soberania própria.')
TXT(
    'A <b>Lei Mental de 1434</b> é a prova mais forte e a menos lembrada: determina que as doações '
    'régias <b>revertam à Coroa</b> na falta de herdeiro varão direto. Onde a terra retorna sempre ao '
    'rei, nenhum senhorio se torna autônomo e a propriedade senhorial é estruturalmente precária. Não '
    'há vassalagem feudal no sentido pleno: o monarca nunca se converte em <i>primus inter pares</i>.')
TXT(
    'Por fim, os <b>monopólios régios</b> e a organização da expansão como <b>empresa da Coroa</b> — '
    'Casa da Guiné e Mina, Casa da Índia, estancos — mostram que o padrão se estende da terra ao '
    'comércio: o que seria a esfera da iniciativa mercantil nasce, em Portugal, dentro do aparelho do '
    'rei.')

H3('Resposta-modelo condensada (item c)' + NOVO)
TXT(
    'A <b>Revolução de Avis</b> completa o quadro. Em 1383-85 Portugal vive uma <b>crise dinástica</b>: '
    'morto D. Fernando sem sucessor masculino, a alta nobreza, ligada por casamento e interesse a '
    'Castela, inclina-se pela solução castelhana; contra ela, a Casa de Avis ascende com apoio dos '
    'setores <b>urbanos e mercantis</b> de Lisboa e do Porto e da pequena nobreza. O resultado imediato '
    'é um Estado <b>centralizado precocemente</b>, antes das demais monarquias nacionais, com uma '
    'nobreza nova criada pelo próprio rei e dependente dele.')
TXT(
    'O passo decisivo do argumento está em identificar <b>quem comanda</b> o arranjo que se segue. A '
    'monarquia vence com apoio urbano e mercantil, mas o beneficiário é a <b>Coroa</b>, não os '
    'mercadores: a expansão marítima se organiza como <b>empresa régia</b>, com monopólios e estancos, '
    'e o comerciante entra nela como <b>concessionário</b> — não como sujeito autônomo de acumulação. '
    'Em lugar de uma burguesia que conquista o Estado, tem-se um <b>Estado que absorve o comércio</b>.')
TXT(
    'A consequência fecha a tese. Sem burguesia autônoma, a riqueza passa necessariamente pelo Estado '
    '— é o <b>capitalismo politicamente orientado</b> —, e os quadros que operam esse aparelho '
    'cristalizam-se num <b>estamento burocrático</b> que se apropria do Estado e vive dele. '
    'Transplantada para a América, a lógica produz o patronato político brasileiro.')

BOX('Erros que mais custam nota',
    'Usar patrimonialismo como sinônimo de <b>corrupção</b>: é o erro mais comum e o mais penalizado. '
    'Confundir <b>estamento</b> com <b>classe</b>. Atribuir a Faoro a tese de que Portugal era feudal '
    '— ele sustenta exatamente o contrário. Responder (c) dizendo que Avis instaurou o poder da '
    'burguesia: o ponto de Faoro é precisamente o oposto.', 'vermelho')
BOX('Pontos de diferenciação',
    'Citar a <b>Lei Mental</b> como evidência: é o dado institucional mais forte e quase ninguém se '
    'lembra dele. Observar a tensão conceitual de “<b>estamento burocrático</b>”, que combina um termo '
    'da dominação tradicional com outro da racional-legal — defensável pela noção weberiana de '
    '<b>burocracia patrimonial</b>, mas tensa. E marcar a distância entre o conceito weberiano e o '
    'clichê do debate público brasileiro.', 'azul')
BREAK()

# --- Q2 --------------------------------------------------------------------
H2('Questão 2 (35 pontos)')
BOX('O que a questão pede' + NOVO,
    'Reconstituir um argumento de <b>história financeira</b> (a) e, em seguida, usá-lo em <b>duas '
    'direções opostas</b> sobre a mesma tese (b e c). A questão avalia se você consegue sustentar e '
    'qualificar o mesmo autor sem se contradizer — o exercício de <b>convergência e limite</b> que a '
    'prova cobra. Quem escreve a mesma coisa em (b) e em (c) perde metade dos pontos.', 'verde')

H3('a) Distribuição dos pontos (15)')
PONTOS([
    ('<b>Base de receita medieval</b>: rendas da terra, sisas, portagens, direitos, monopólios régios, '
     'rendas das ordens militares', 4),
    ('<b>Pressões</b>: custo da guerra e da expansão — armadas, fortalezas, guarnições — e da corte, '
     'gerando <b>déficit crônico</b>', 4),
    ('<b>Expedientes</b>: quebra da moeda, empréstimos, antecipação e alienação de receitas, venda de '
     'ofícios', 3),
    ('<b>Deslocamento</b>: da renda fundiária para a renda do <b>comércio e das alfândegas</b>; ouro '
     'da Guiné e depois a especiaria tornam-se espinha dorsal da receita', 4),
])

H3('b) Distribuição dos pontos (10)')
PONTOS([
    ('Mostrar que a economia <b>passa de fato pelo Estado</b>: o “capitalismo politicamente orientado” '
     'ganha comprovação contábil', 5),
    ('Reforçar a tese do <b>Estado empresário</b>: monopólios e alfândegas como receita central, não '
     'acessória', 3),
    ('Fundamentar a <b>precocidade da centralização</b> por uma via material, e não apenas tipológica', 2),
])

H3('c) Distribuição dos pontos (10)')
PONTOS([
    ('O Estado não é onipotente, e sim <b>fiscalmente acossado</b>: receitas empenhadas de antemão, '
     'déficit estrutural', 4),
    ('Dependência de <b>credores estrangeiros</b> (genoveses, florentinos, flamengos, alemães) e '
     'distribuição europeia feita em <b>Antuérpia</b>: o monopólio é em parte <b>nominal</b>', 4),
    ('A expansão aparece como <b>necessidade fiscal</b> — “fuga para frente” — e não como projeto '
     'soberano de um estamento todo-poderoso; Godinho recusa, além disso, a <b>causa única</b>', 2),
])

H3('Resposta-modelo condensada (item a)' + NOVO)
TXT(
    'A receita da Coroa portuguesa medieval é de base <b>fundiária e jurisdicional</b>: rendas das '
    'terras régias, sisas, portagens e direitos de passagem, monopólios ou estancos, e as rendas das '
    '<b>ordens militares</b>, cuja administração a Coroa vai progressivamente concentrando. É uma '
    'receita rígida e pouco elástica, atada à produção agrária e ao consumo interno — cresce devagar e '
    'depende da colheita.')
TXT(
    'As pressões que a tornam insuficiente são de dois tipos, e ambas crescem. A <b>guerra e a '
    'expansão</b> são caríssimas: armadas, fortalezas, guarnições, resgate de cativos, manutenção das '
    'praças no Norte da África. E a <b>corte</b>, ao se ampliar e ao remunerar a nobreza com tenças e '
    'mercês, converte-se ela mesma em despesa estrutural. O resultado é <b>déficit crônico</b>, '
    'enfrentado por expedientes que denunciam a precariedade: quebra da moeda, empréstimos, antecipação '
    'e alienação de receitas futuras, venda de ofícios.')
TXT(
    'O ultramar altera a <b>estrutura</b> da receita, e não apenas o seu volume — e é esse o ponto do '
    'argumento. A espinha dorsal se desloca da renda da terra para a renda do <b>comércio e das '
    'alfândegas</b>: primeiro o ouro da Guiné, depois, decisivamente, a especiaria. A Coroa passa a '
    'viver do que <b>circula</b>, não do que se colhe. É essa inversão que faz do Estado português um '
    '<b>Estado-empresário</b>, cuja saúde financeira depende do giro mercantil que ele próprio '
    'monopoliza — e que, por isso mesmo, precisa manter o giro a qualquer custo.')

H3('Resposta-modelo condensada (item b)')
TXT(
    'Godinho <b>sustenta</b> Faoro ao dar lastro material àquilo que em <i>Os Donos do Poder</i> é '
    'tipologia: se a espinha dorsal da receita régia se desloca da renda da terra para as alfândegas e '
    'os monopólios de comércio, então a economia efetivamente <b>passa pelo Estado</b>, e o '
    '“capitalismo politicamente orientado” deixa de ser conceito e ganha contabilidade. O '
    'Estado-empresário de Faoro aparece nas contas.')
TXT(
    'O reforço é duplo. Primeiro, monopólios e alfândegas aparecem como receita <b>central</b>, e não '
    'acessória: não são privilégios pitorescos à margem de uma economia privada — são o que mantém a '
    'Coroa de pé. Segundo, a <b>precocidade da centralização</b> ganha explicação material, e não '
    'apenas tipológica: Portugal se centraliza cedo porque a sua máquina fiscal depende de um comércio '
    'que só o Estado pode armar, monopolizar e proteger militarmente.')
TXT(
    'O ganho argumentativo, para quem defende Faoro, é escapar da acusação de essencialismo: a tese '
    'deixa de repousar sobre um tipo weberiano e passa a apoiar-se em série orçamentária.')

H3('Resposta-modelo condensada (item c)' + NOVO)
TXT(
    'Mas Godinho <b>qualifica</b> a tese no ponto mais sensível. O Estado que emerge do orçamento não é '
    'proprietário onipotente: é estrutural e cronicamente <b>endividado</b>, com receitas empenhadas '
    'antes de arrecadadas e expedientes permanentes de antecipação e alienação.')
TXT(
    'Mais: depende do capital <b>genovês, florentino, flamengo e alemão</b> para armar as frotas, e é '
    'incapaz de controlar a distribuição europeia da especiaria, feita em <b>Antuérpia</b>. O monopólio '
    'régio é, em medida importante, <b>nominal</b> — a Coroa monopoliza a compra na origem, não o '
    'mercado que fixa o preço final.')
TXT(
    'Daí a inflexão sobre a própria expansão: ela aparece menos como projeto soberano de um estamento '
    'que domina a sociedade do que como <b>fuga para frente</b> de uma Coroa acossada pelo próprio '
    'caixa. E Godinho recusa, além disso, a <b>causa única</b>: a expansão é complexo de fatores '
    'convergentes, não execução de uma vontade.')
TXT(
    'A conclusão é que os dois se completam <b>invertendo a direção da causalidade</b>: para Faoro, o '
    'Estado organiza a economia; para Godinho, a <b>restrição orçamentária organiza o Estado</b>. '
    'Vistos juntos, o patrimonialismo deixa de ser poder absoluto e passa a ser aperto permanente.')

BOX('Erro que mais custa nota',
    '<b>Inventar percentuais de receita.</b> Godinho trabalha com séries cujos critérios e '
    'periodizações variam entre os quadros; afirmar “X% da receita vinha do ultramar” sem o quadro em '
    'mãos é mais arriscado do que descrever com segurança a <b>direção</b> do deslocamento. Numa prova, '
    'a formulação qualitativa precisa vale mais que um número errado. Vale somar: escrever em (c) o '
    'mesmo que em (b), por não perceber que a questão pede as duas direções.', 'vermelho')
BOX('Pontos de diferenciação' + NOVO,
    'Formular a <b>inversão de causalidade</b> com nitidez: em Faoro o Estado organiza a economia; em '
    'Godinho a restrição orçamentária organiza o Estado. Observar que a dependência do capital genovês, '
    'florentino e flamengo e a distribuição da especiaria em Antuérpia tornam o monopólio régio em '
    'parte <b>nominal</b> — ponto que desmonta a imagem do Estado onipotente <i>sem</i> negar o '
    'patrimonialismo. E notar que o argumento muda o <b>tipo de prova</b> admitida no debate: de '
    'tipologia weberiana para série orçamentária, o que é, em si, uma tomada de posição metodológica.',
    'azul')
BREAK()

# --- Q3 --------------------------------------------------------------------
H2('Questão 3 (25 pontos)')
BOX('O que a questão pede' + NOVO,
    'Uma <b>armadilha deliberada</b>: a pergunta oferece dois polos — “confirma” ou “contraria” — e '
    'premia quem recusa ambos. O que se avalia é a compreensão da diferença entre as <b>razões '
    'declaradas</b> por um contemporâneo e as <b>determinações estruturais</b> reconstituídas pelo '
    'historiador.', 'verde')

H3('a) Distribuição dos pontos (13)')
PONTOS([
    ('Recusar a dicotomia: a fonte nem confirma nem contraria diretamente, porque opera em <b>outro '
     'registro</b> — o das razões declaradas e legitimadas', 5),
    ('Notar que as razões de Zurara são <b>mistas</b>, e que algumas já são econômicas (comerciar, '
     'conhecer terras, avaliar o poder do adversário), ao lado das religiosas e cavaleirescas', 4),
    ('Identificar o <b>gênero e a função</b>: crônica encomiástica, escrita para exaltar o Infante e '
     'legitimar a empresa — a linguagem da cruzada é a forma <b>legítima</b> de enunciar o '
     'empreendimento', 4),
])

H3('b) Distribuição dos pontos (12)')
PONTOS([
    ('Formular a distinção: <b>razões declaradas</b> (autorrepresentação, legitimação) não coincidem '
     'com <b>determinações estruturais</b> (fisco, mercado, demografia), e uma não desmente a outra', 4),
    ('Mobilizar <b>Godinho</b>: a expansão como <b>complexo de fatores convergentes</b>, com a '
     'necessidade fiscal entre eles; recusa da causa única — o que acomoda a pluralidade de razões da '
     'fonte', 4),
    ('Mobilizar <b>Boxer</b>: móveis plurais — ouro da Guiné, cruzada, busca do Preste João, '
     'especiaria, honra cavaleiresca; expansão como “<b>cruzada que dá lucro</b>”', 3),
    ('Concluir metodologicamente: a fonte é evidência privilegiada de <b>mentalidade e legitimação</b>, '
     'e não prova nem refuta a determinação econômica', 1),
])

H3('Resposta-modelo condensada (item a)' + NOVO)
TXT(
    'A fonte não confirma nem contraria as explicações econômicas, porque opera em outro registro: o '
    'das <b>razões declaradas</b> e socialmente legitimadas. Zurara não está explicando a expansão; '
    'está <b>justificando-a</b> e exaltando o Infante. Exigir dela uma resposta sobre causalidade '
    'estrutural é pedir o que o documento não se propõe a fazer.')
TXT(
    'E, mesmo nesse registro, a lista é <b>mista</b>: conhecer as terras além do Cabo, estabelecer '
    'comércio, avaliar a extensão real do poder dos adversários são razões que já contêm conteúdo '
    'econômico, geográfico e estratégico, ao lado das religiosas e cavaleirescas. A própria fonte, '
    'portanto, desmente a oposição que a pergunta sugere.')
TXT(
    'Decisivo é o <b>gênero</b>: crônica encomiástica, escrita por um cronista régio para honrar o '
    'patrono e a empresa. A linguagem da cruzada e da salvação de almas é a forma <b>legítima</b> de '
    'enunciar o empreendimento num texto desse tipo — não a prova de que o móvel fosse exclusivamente '
    'espiritual, nem uma fachada cínica sobre interesses confessados em segredo. É o vocabulário '
    'disponível para dizer publicamente o que se fazia.')

H3('Resposta-modelo condensada (item b)' + NOVO)
TXT(
    'A distinção metodológica é a seguinte: o que os agentes <b>dizem</b> sobre os seus motivos '
    'pertence à história das representações e da legitimação; o que os <b>constrange</b> — fisco, '
    'mercado, demografia, técnica — pertence à análise estrutural. Uma não desmente a outra, e '
    'confundir os planos produz dois erros simétricos: tomar a crônica por explicação causal, ou '
    'descartá-la como mera ideologia.')
TXT(
    '<b>Godinho</b> acomoda a fonte sem concessões, porque recusa explicitamente a <b>causa única</b> e '
    'descreve a expansão como complexo de fatores convergentes: a pressão fiscal da Coroa, a busca de '
    'metal amoedável, a insuficiência cerealífera, os interesses de uma nobreza sem guerra e de um '
    'capital mercantil em busca de aplicação, e o horizonte mental da cruzada. Nesse quadro, a '
    'pluralidade de razões de Zurara não é ruído a ser filtrado: é o que se deve esperar de uma '
    'empresa sobredeterminada.')
TXT(
    '<b>Boxer</b> vai na mesma direção com a sua fórmula: móveis plurais — ouro da Guiné, cruzada, '
    'busca do Preste João, especiaria, honra cavaleiresca — numa empresa que se descreve bem como '
    '<b>cruzada que dá lucro</b>. Para os contemporâneos, fé, honra e proveito não eram alternativas '
    'excludentes, e exigir que escolhessem entre elas é anacronismo.')
TXT(
    'A conclusão é metodológica: a crónica é evidência <b>privilegiada</b> de mentalidade e de '
    'legitimação, e documento <b>inadequado</b> para provar ou refutar a determinação econômica. '
    'Sabê-lo é a resposta que a questão procura.')

BOX('Erros que mais custam nota' + NOVO,
    'Escolher um dos polos da dicotomia — é o que a questão testa. Tratar as razões religiosas como '
    'fachada cínica: anacronismo que projeta nos contemporâneos a nossa separação entre fé e proveito. '
    'Usar a fonte como prova da tese econômica só porque menciona comércio, sem considerar o gênero do '
    'texto. E citar Godinho ou Boxer como autoridade, sem reconstituir o argumento da <b>causalidade '
    'plural</b> que os torna pertinentes aqui.', 'vermelho')
BOX('Pontos de diferenciação',
    'O erro de armadilha da questão é escolher um dos dois polos. A resposta forte <b>recusa a '
    'dicotomia</b> e explica por quê: fé, honra e lucro não eram alternativas excludentes para os '
    'contemporâneos, e a linguagem religiosa-cavaleiresca era a forma legítima de enunciar uma empresa '
    'que também era mercantil. Quem observa que a <b>própria fonte já inclui razões econômicas</b> ao '
    'lado das religiosas desmonta a oposição com a própria evidência. Mencionar a atribuição '
    '<b>astrológica</b> da inclinação do Infante como índice do horizonte mental do século XV é um '
    'ganho adicional.', 'azul')
BREAK()

# ===========================================================================
# GABARITO — PROVA 3
# ===========================================================================
H1('Gabarito — Prova 3')

# --- Q1 --------------------------------------------------------------------
H2('Questão 1 (35 pontos)')
BOX('O que a questão pede' + NOVO,
    'Três operações distintas: <b>articular evidência ao que ela refuta</b> (a), extrair a consequência '
    '<b>teórica e cronológica</b> da tese (b) e aplicar corretamente um conceito <b>que não é de '
    'Neves</b> (c). A pontuação de (a) é por <b>par</b> evidência–refutação: listar achados sem dizer o '
    'que cada um derruba vale metade.', 'verde')

H3('a) Distribuição dos pontos (18) — 6 pontos por evidência bem articulada ao que ela refuta')
TAB([
    ['Evidência', 'O que refuta', 'Pontos'],
    ['<b>Terras pretas de índio</b> (antrossolos férteis produzidos por ocupação prolongada)',
     'O <b>solo como limite dado</b>: a fertilidade é efeito do assentamento, não sua restrição', '6'],
    ['<b>Sítios extensos, profundos, de ocupação contínua</b>; montículos, estruturas de terra, valas',
     'A tese dos <b>grupos pequenos, móveis e igualitários</b>; indicam sedentarismo, densidade e '
     'trabalho coletivo coordenado', '6'],
    ['<b>Tradições cerâmicas elaboradas e duradouras</b>; domesticação de plantas',
     'O caráter supostamente <b>intrusivo</b> da complexidade (importada dos Andes) e a ideia de '
     '<b>natureza intocada</b>', '6'],
], W_TRES)
TXT(
    'Mencionar nominalmente o modelo de <b>Betty Meggers</b> (solos pobres → baixa capacidade de '
    'suporte → sociedades simples) e a imagem do “<b>paraíso falso</b>” acrescenta precisão à resposta.')

H3('b) Distribuição dos pontos (9)')
PONTOS([
    ('A composição da floresta atual carrega a <b>assinatura de manejo humano milenar</b> (mandioca, '
     'pupunha, cacau, castanha, açaí; concentrações de espécies úteis)', 3),
    ('Consequência teórica: <b>natureza e história</b> deixam de ser domínios separados — o ambiente é '
     'produto histórico', 3),
    ('Consequência para a periodização: a história do Brasil <b>não começa em 1500</b>; os oito mil '
     'anos anteriores são história, não pré-história, e a “floresta vazia” é artefato do <b>colapso '
     'demográfico</b> pós-1492, não estado original', 3),
])

H3('c) Distribuição dos pontos (8)')
PONTOS([
    ('Enunciar a teoria: <b>pressão demográfica + circunscrição ambiental + guerra</b> → os derrotados '
     'não podem fugir e são incorporados como subordinados tributários → <b>Estado coercitivo</b>', 3),
    ('Aplicar à Amazônia: <b>sem cerco</b>, a terra é aberta, a fissão e a fuga são sempre possíveis, a '
     'vitória militar não se converte em sujeição permanente → <b>complexidade sem Estado '
     'coercitivo</b>', 3),
    ('Fechar o contraste: Portugal é o caso oposto — território circunscrito, guerra permanente de '
     'Reconquista e fisco acossado produzem Estado centralizado e coercitivo (Faoro e Godinho)', 2),
])

H3('Resposta-modelo condensada (item a)' + NOVO)
TXT(
    'O alvo é o <b>determinismo ambiental</b> que, na formulação de Betty Meggers, deduzia a '
    'organização social da qualidade do solo: solos tropicais pobres → baixa capacidade de suporte → '
    'populações necessariamente pequenas, móveis e igualitárias; a Amazônia como “<b>paraíso falso</b>”, '
    'exuberante na aparência e limitada na realidade. Neves responde com evidência, e cada tipo refuta '
    'uma peça distinta do modelo.')
TXT(
    'As <b>terras pretas de índio</b> — antrossolos profundos e férteis, carregados de carvão, '
    'fragmentos cerâmicos e matéria orgânica — refutam a <b>premissa</b>: ali a fertilidade é '
    '<i>efeito</i> do assentamento prolongado, não a sua restrição prévia. O solo é produto do trabalho '
    'humano, e a seta causal do modelo se inverte.')
TXT(
    'Os <b>sítios extensos, profundos e de ocupação contínua</b>, com montículos, estruturas de terra e '
    'valas, refutam a <b>conclusão</b> sobre a forma social: indicam sedentarismo, densidade '
    'demográfica e trabalho coletivo coordenado — isto é, exatamente as sociedades que o modelo '
    'declarava impossíveis naquele ambiente.')
TXT(
    'As <b>tradições cerâmicas elaboradas e duradouras</b> e a <b>domesticação de plantas</b> refutam a '
    'tese do caráter <b>intrusivo</b> da complexidade — a ideia de que o que houvesse de sofisticado '
    'teria vindo dos Andes — e, com ela, a imagem de uma natureza intocada. Há desenvolvimento local, '
    'longo e cumulativo, com cronologia própria.')

H3('Resposta-modelo condensada (item b)' + NOVO)
TXT(
    'Daí a tese da <b>floresta como produto histórico</b>. A composição da floresta atual carrega a '
    'assinatura de milênios de manejo: mandioca, pupunha, cacau, castanha, açaí; concentrações de '
    'espécies úteis em torno de sítios antigos. A floresta que o europeu encontrou e descreveu como '
    'virgem já era, em medida significativa, <b>resultado de trabalho indígena</b>.')
TXT(
    'As consequências são duas. A <b>teórica</b>: natureza e história deixam de ser domínios separados, '
    'e o ambiente passa a ser <i>objeto</i> da história, não o seu cenário — o que retira da '
    'explicação o recurso ao meio como dado fixo. A de <b>periodização</b>: a história do Brasil não '
    'começa em 1500. Os oito mil anos anteriores são história, e não “pré-história”, e a floresta vazia '
    'que a tradição tomou por estado original é <b>artefato do colapso demográfico</b> posterior a '
    '1492. O que se descreveu como natureza primitiva é, em parte, a cicatriz de uma catástrofe '
    'populacional.')

H3('Resposta-modelo condensada (item c)' + NOVO)
TXT(
    'A <b>teoria da circunscrição</b> de Carneiro explica a origem do Estado pela conjunção de três '
    'fatores: pressão demográfica, circunscrição ambiental e guerra. Onde a terra agricultável é '
    '<b>cercada</b> por áreas improdutivas — mar, deserto, montanha —, o derrotado não tem para onde '
    'fugir, e a vitória militar se converte em sujeição permanente e tributo. É assim que nasce o '
    'Estado coercitivo.')
TXT(
    'Na Amazônia <b>não há cerco</b>. A terra é aberta, a fissão do grupo e a migração são sempre '
    'possíveis, e por isso a vitória militar não se converte em sujeição duradoura: observa-se '
    'adensamento populacional, obras de terra e complexidade social <b>sem</b> Estado coercitivo. A '
    'ausência de Estado não indica, portanto, atraso — indica outra equação entre geografia, '
    'população e poder.')
TXT(
    'O contraste com Portugal é o que amarra a comparação do curso. Território delimitado, guerra '
    'permanente de Reconquista, população circunscrita e fisco acossado produzem exatamente o oposto: '
    'centralização precoce e coerção concentrada — o Estado que <b>Faoro</b> descreve como tipo de '
    'dominação e <b>Godinho</b> pelas contas. Mesma pergunta — como se organizam poder e produção —, '
    'respostas opostas, porque a geografia da circunscrição difere.')

BOX('Erros que mais custam nota' + NOVO,
    'Listar evidências sem dizer <b>o que cada uma refuta</b>: metade dos pontos de (a) está no '
    'pareamento. Atribuir a teoria da circunscrição a <b>Neves</b> — é de <b>Carneiro</b>, mobilizada '
    'no curso como moldura comparativa. Inverter a tese de (c) e concluir que a Amazônia foi '
    '“urbanizada” ou “estatal” como os Andes: o argumento é complexidade <i>sem</i> Estado coercitivo. '
    'Tratar as terras pretas como solo naturalmente fértil, quando o ponto é que foram '
    '<b>produzidas</b>. E dizer que Neves “prova que havia civilização na Amazônia”, formulação que '
    'reintroduz a régua andina que ele recusa.', 'vermelho')
BOX('Pontos de diferenciação',
    'Notar que Carneiro construiu a teoria <b>comparando justamente os vales costeiros do Peru com a '
    'bacia amazônica</b> — a Amazônia é o <b>caso negativo original</b> da teoria, não uma aplicação '
    'posterior. E manter a atribuição correta: a circunscrição é de Carneiro; a ênfase própria de Neves '
    'está em refutar o determinismo ambiental e documentar a <b>domesticação da paisagem</b>. Atribuir '
    'a circunscrição a Neves é erro de atribuição.', 'azul')
BREAK()

# --- Q2 --------------------------------------------------------------------
H2('Questão 2 (40 pontos)')
BOX('O que a questão pede',
    'É a questão mais aberta e a que mais distingue candidatos. Ela <b>não pede resumos</b>: pede que '
    'você trate a <b>unidade de análise como variável explicativa</b>. A estrutura de pontuação premia '
    'a terceira coluna — <b>o que a escala torna invisível</b> —, porque é aí que se demonstra análise '
    'em vez de memorização.', 'verde')

H3('Distribuição dos pontos (40)')
PONTOS([
    ('Para <b>cada</b> autor escolhido (3 × 10 = 30): pergunta que a escala permite responder (3); como '
     'a escala <b>determina a tese</b> (4); o que ela <b>torna invisível</b> (3)', 30),
    ('<b>Conclusão</b>: avaliar se as divergências são incompatibilidades reais ou efeitos de escala', 10),
])

H3('Repertório por autor (o candidato escolhe três)')
TAB([
    ['Autor', 'Pergunta que a escala responde', 'Como a escala determina a tese',
     'O que torna invisível'],
    ['<b>Caio Prado</b>', 'Por que o Brasil é desigual e extrovertido?',
     'Recortando a <b>colônia</b> dentro da expansão comercial europeia, a economia aparece '
     'necessariamente como <b>função externa</b>',
     'A vida social interna com lógica própria; o peso do abastecimento'],
    ['<b>Novais</b>', 'Por que a Europa industrializou e por que o sistema entrou em crise?',
     'Tomando o <b>sistema</b> como unidade, a colônia só pode aparecer como peça funcional; e um '
     'sistema pode ter <b>contradição interna</b>, o que permite deduzir a crise',
     'A variação regional e a agência dos sujeitos coloniais'],
    ['<b>Fragoso <i>et al.</i></b>', 'Como a sociedade colonial se reproduzia e se governava?',
     'Recortando o <b>império como rede</b>, aparecem circuitos, crédito e hierarquias que o eixo '
     'metrópole-colônia não capta',
     'A drenagem de excedente e a violência estrutural da escravidão'],
    ['<b>Faoro</b>', 'Por que o Estado brasileiro antecede e domina a sociedade?',
     'Tomando o <b>Estado</b> como sujeito de longa duração, a <b>continuidade</b> se impõe sobre a '
     'ruptura',
     'As descontinuidades históricas e os limites reais do poder régio'],
    ['<b>Godinho</b>', 'O que a Coroa podia de fato fazer?',
     'Lendo o Estado pelo <b>orçamento</b>, ele aparece como objeto de <b>restrição</b>, não como '
     'vontade soberana',
     'A colônia como sujeito; a sociedade'],
    ['<b>Neves</b>', 'O que havia antes, e por que a floresta é como é?',
     'Adotando a <b>longa duração</b> e o ambiente como unidade, a história se estende por milênios e o '
     'meio se torna produto',
     'A economia colonial propriamente dita'],
], [CONTENT_W * .13, CONTENT_W * .22, CONTENT_W * .40, CONTENT_W * .25])

H3('Resposta-modelo condensada (corpo da resposta — os três autores)' + NOVO)
TXT(
    'A escolha abaixo é deliberada: Caio Prado, Fragoso <i>et al.</i> e Faoro recortam três escalas '
    'muito distintas — a colônia, a rede imperial e o Estado —, e por isso o exercício de comparação '
    'rende mais. Qualquer trio serve, desde que as <b>três colunas</b> sejam preenchidas para cada '
    'autor.')
TXT(
    '<b>Caio Prado Jr. — a colônia no quadro da expansão comercial europeia.</b> A pergunta que a '
    'escala permite responder é: <i>por que o Brasil é desigual e extrovertido?</i> Ao recortar a '
    'colônia <b>dentro</b> da expansão comercial europeia, a economia só pode aparecer como função '
    'externa — se a unidade de análise é a colônia definida pela sua inserção, então o que a explica '
    'está fora dela, e a tese do “sentido” segue <b>necessariamente</b> do recorte. É a escala que '
    'produz a conclusão, não o contrário. O que ela torna invisível é a vida social interna dotada de '
    'lógica própria: o abastecimento, o mercado interno, a formação de fortunas locais — que o recorte '
    'converte em detalhe subsidiário <b>antes</b> de examiná-los.')
TXT(
    '<b>Fragoso, Bicalho e Gouvêa — o império como rede pluricontinental.</b> A pergunta é outra: '
    '<i>como a sociedade colonial se reproduzia e se governava?</i> Tomando como unidade o império '
    'policêntrico, tornam-se visíveis os circuitos que não passam por Lisboa, o crédito controlado por '
    'comerciantes coloniais e as hierarquias construídas pela economia da mercê — precisamente o que o '
    'eixo bipolar metrópole-colônia não capta. A tese do “Antigo Regime nos trópicos” é consequência '
    'direta dessa ampliação de escala. O que ela torna invisível é a drenagem de excedente e a '
    'violência estrutural da escravidão: ao iluminar a agência das elites coloniais, a rede deixa na '
    'sombra a coerção que sustentava a produção.')
TXT(
    '<b>Faoro — o Estado português como sujeito de longa duração.</b> A pergunta é: <i>por que o Estado '
    'brasileiro antecede e domina a sociedade?</i> Tomando o Estado como unidade e percorrendo-o da '
    'Reconquista à República, a <b>continuidade</b> se impõe sobre a ruptura — uma série de seis '
    'séculos privilegia, por construção, o que permanece, e é essa escala temporal que produz a tese '
    'do patrimonialismo persistente. O que ela torna invisível são as descontinuidades históricas e os '
    '<b>limites reais</b> do poder régio: o Estado aparece como vontade, e não como objeto de '
    'restrição — exatamente o que Godinho mostrará ao ler a mesma Coroa pelo orçamento.')

H3('Resposta-modelo da conclusão')
TXT(
    'As divergências são, em boa parte, <b>efeitos de escala</b> — mas não integralmente, e a distinção '
    'importa. São efeito de escala as oposições entre Caio Prado e Fragoso <i>et al.</i> quanto ao peso '
    'do mercado interno, ou entre Faoro e Godinho quanto à força do Estado. Em ambos os casos, os '
    'autores respondem a <b>perguntas diferentes</b>: um explica a inserção da colônia num circuito de '
    'acumulação, o outro a sua reprodução interna; um descreve o tipo de dominação, o outro a restrição '
    'orçamentária. Nesses casos a síntese é possível e desejável, e consiste em atribuir cada tese ao '
    'problema que ela resolve.')
TXT(
    'Há, porém, <b>incompatibilidade real</b> quando as teses disputam o <b>mesmo objeto na mesma '
    'escala</b>. É o caso da crítica de <b>Gorender</b> a Caio Prado e Novais: afirmar que a colônia '
    'tem um <b>modo de produção</b> com leis de movimento próprias é incompatível com explicá-la pela '
    '<b>circulação</b> mercantil, e não há conciliação por repartição de escalas. É também o caso da '
    'divergência entre Faoro e a historiografia de <b>Hespanha</b> sobre o grau de centralização do '
    'Estado do Antigo Regime: ou o rei era proprietário da máquina, ou era árbitro entre corpos com '
    'jurisdição própria.')
TXT(
    'O critério, portanto, é este: <b>divergências sobre o mesmo objeto na mesma escala são '
    'incompatibilidades; divergências entre escalas distintas são divisões de trabalho.</b> Reconhecer '
    'a diferença evita tanto o ecletismo que soma tudo quanto o sectarismo que escolhe um autor e '
    'descarta os demais.')

BOX('Erros que mais custam nota',
    'Escrever <b>três resumos</b> em vez de analisar a escala — é o erro que mais derruba a nota nesta '
    'questão. Omitir a terceira coluna (o que fica invisível), que concentra 9 dos 30 pontos. Concluir '
    'apenas que “todos têm razão a seu modo”: a conclusão precisa de <b>critério</b>, e o critério é a '
    'distinção entre divergência de escala e divergência de objeto.', 'vermelho')
BOX('Pontos de diferenciação' + NOVO,
    'Tratar a unidade de análise como <b>variável</b>, e não como rótulo: demonstrar que a tese é '
    '<i>consequência</i> da escala, de modo que mudar o recorte mudaria a conclusão do próprio autor. '
    'Enunciar o <b>critério da conclusão antes de aplicá-lo</b>, em vez de deixá-lo implícito. Usar um '
    'caso de incompatibilidade real — Gorender contra Prado e Novais, Hespanha contra Faoro — para '
    'provar que o critério <b>discrimina</b>, e não apenas reconcilia. E observar que a escolha da '
    'unidade de análise é ela mesma uma decisão teórica, e não um recorte neutro: é o que transforma a '
    'resposta em argumento próprio.', 'azul')
BREAK()

# --- Q3 --------------------------------------------------------------------
H2('Questão 3 (25 pontos)')
BOX('O que a questão pede',
    'O qualificativo “<b>insuficiente</b>” é a resposta mais defensável, e a questão foi construída '
    'para premiá-lo. Mas “verdadeira” e “falsa” podem render pontuação integral se o candidato '
    'justificar com rigor — o que se avalia é a <b>qualidade da argumentação</b>, não a escolha.',
    'verde')

H3('Distribuição dos pontos (25)')
PONTOS([
    ('Escolha <b>explícita</b> do qualificativo, com justificação do porquê daquele termo <b>e não dos '
     'outros</b>', 4),
    ('Reconhecer o que a afirmação <b>acerta</b>: há de fato exclusivo, <i>plantation</i>, monocultura e '
     'drenagem de excedente (Caio Prado, Novais)', 6),
    ('Mostrar o que ela <b>omite</b>: mercado interno, circuitos intracoloniais, acumulação endógena, '
     'hierarquias e governo locais (Fragoso <i>et al.</i>)', 6),
    ('Mobilizar ao menos <b>três autores</b> de forma efetivamente articulada, e não apenas citada', 5),
    ('Fechar com <b>posição metodológica</b> sobre escala e suficiência explicativa', 4),
])

H3('Resposta-modelo condensada')
TXT(
    '<b>Insuficiente</b> — e o termo é escolhido deliberadamente contra os outros dois. “Falsa” seria '
    'indefensável, porque o exclusivo metropolitano, a <i>plantation</i> e a drenagem de excedente são '
    'fatos estabelecidos; “verdadeira” seria excessiva, porque a afirmação pretende <b>suficiência '
    'explicativa</b>, e é a suficiência que não se sustenta.')
TXT(
    'O que a afirmação <b>acerta</b> está bem demonstrado por Caio Prado e Novais. Há um sentido '
    'dominante que organiza a produção colonial em torno da exportação, e há um dispositivo concreto '
    'que opera a transferência de valor: o exclusivo, que permite ao comerciante metropolitano fixar os '
    'preços nas duas pontas da troca. Nesse nível, a proposição é verdadeira.')
TXT(
    'O que ela <b>omite</b> é a existência de uma <b>sociedade</b>. Fragoso, Bicalho e Gouvêa mostram um '
    'setor de abastecimento de grande porte, circuitos que não passam por Lisboa — Rio–Angola, '
    'Rio–Prata, Rio–Minas —, crédito controlado por comerciantes coloniais e fortunas constituídas e '
    'reproduzidas localmente. Mostram também que o império se governava por negociação, mercê e corpos '
    'intermediários, e que havia uma nobreza da terra com projeto próprio. Nada disso é dedutível da '
    'fórmula inicial. E <b>Neves</b> acrescenta um limite anterior: o território não era um palco '
    'vazio, e a materialidade da empresa colonial incluía plantas domesticadas, solos construídos, '
    'caminhos e trabalho indígenas.')
TXT(
    'A conclusão é metodológica. A afirmação descreve corretamente a <b>inserção</b> da colônia num '
    'circuito de acumulação europeu, mas é oferecida como explicação da <b>totalidade</b> da vida '
    'colonial — e é nessa passagem da parte ao todo que falha. Vale aqui a advertência que '
    '<b>Gorender</b> dirigiu a Prado e Novais: explicar uma formação social pela circulação, e não '
    'pelas relações de produção, é tomar o <b>modo de inserção</b> pelo <b>modo de existir</b>. A '
    'proposição não é falsa; é uma escala tomada pelo todo.')

BOX('Erros que mais custam nota' + NOVO,
    'Responder “falsa” por entender que a afirmação <i>nega</i> o mercado interno: ela não nega nada, '
    'apenas afirma pouco demais — e a diferença entre erro e insuficiência é o eixo da questão. '
    'Escolher o qualificativo e não justificar a escolha <b>contra os outros dois</b>: são 4 pontos '
    'perdidos na primeira linha. Enfileirar paráfrases de três autores sem articulá-los num argumento, '
    'o que satisfaz a letra do enunciado e não os 5 pontos de articulação. E transformar a resposta em '
    '“depende”, sem tomar posição.', 'vermelho')
BOX('Pontos de diferenciação',
    'Justificar <b>explicitamente</b> por que “insuficiente” e não “falsa” — isto é, mostrar '
    'consciência de que a questão é sobre <b>suficiência explicativa</b>, não sobre veracidade '
    'factual. Articular os autores num argumento próprio, em vez de enfileirar paráfrases. E usar a '
    'crítica de <b>Gorender</b>, que opera num nível distinto da crítica revisionista: não discute a '
    'dimensão do mercado interno, mas a <b>legitimidade</b> de explicar uma formação social pela '
    'circulação.', 'azul')
BREAK()

# ===========================================================================
# APÊNDICE A — OS DEZ ERROS CLÁSSICOS
# ===========================================================================
H1('Apêndice A — Os dez erros clássicos' + NOVO)
TXT(
    'O quadro de autoavaliação da primeira versão remetia a uma “lista dos dez erros clássicos” que não '
    'constava do material. Ei-la, consolidada a partir dos blocos de <b>erros que mais custam nota</b> '
    'das nove questões. Use-a como última revisão antes da prova.')
TAB([
    ['#', 'Erro', 'Formulação correta'],
    ['1', 'Usar <b>patrimonialismo</b> como sinônimo de corrupção ou de desvio moral',
     'É um <b>tipo de dominação legítima</b>: administração como extensão da casa do soberano, cargo '
     'como prebenda, sem separação entre público e privado'],
    ['2', 'Confundir <b>estamento</b> com <b>classe</b>',
     'Estamento define-se por honra, estilo de vida e privilégio jurídico; classe, pela posição no '
     'mercado'],
    ['3', 'Tratar o <b>exclusivo metropolitano</b> como imposto ou exclusividade de rotas',
     'É o monopólio da intermediação que fixa preços <b>nas duas pontas</b> — e por isso transfere '
     'excedente sem confisco'],
    ['4', 'Apresentar a <b>escravidão</b> como atraso ou resíduo pré-capitalista',
     'Em Novais é peça necessária do sistema: impede o mercado interno e faz do cativo mercadoria '
     'importada'],
    ['5', 'Explicar a <b>crise do sistema</b> por eventos externos',
     'A contradição é interna; 1789, o Haiti e as independências são a <b>forma</b> da crise, não a sua '
     'causa'],
    ['6', 'Dizer que <b>Novais repete Caio Prado</b>',
     'Novais converte o sentido em sistema, acrescenta o <b>mecanismo</b> (exclusivo) e a '
     '<b>dinâmica</b> (crise deduzida da estrutura)'],
    ['7', 'Ler os <b>revisionistas</b> como negadores da exploração colonial, e “negociação” como '
     'harmonia',
     'Eles negam o <b>monopólio explicativo</b>, não o exclusivo; negociação é a forma do conflito e '
     'inclui a revolta armada'],
    ['8', 'Atribuir a <b>circunscrição</b> a Neves, ou concluir que a Amazônia teve Estado',
     'A teoria é de <b>Carneiro</b> (1970); a tese é <b>complexidade sem Estado coercitivo</b>, e as '
     'terras pretas são <b>produzidas</b>, não dadas'],
    ['9', 'Parafrasear fontes em vez de interrogá-las; escolher um polo nas questões de documento',
     'Pergunte sempre: quem escreve, para quem, com que interesse, e o que o documento <b>não pode</b> '
     'provar'],
    ['10', 'Resumir autores em vez de analisar a <b>escala</b>; concluir que “todos têm razão”',
     'Mesmo objeto e mesma escala → incompatibilidade; escalas distintas → divisão de trabalho. A '
     'conclusão exige <b>critério</b>'],
], [0.8 * cm, CONTENT_W * .42 - 0.4 * cm, CONTENT_W * .58 - 0.4 * cm])
BOX('Bônus: o erro que não entra na lista porque é de outra natureza',
    '<b>Inventar números.</b> Percentuais de receita em Godinho, volume do tráfico, população colonial '
    '— as séries variam de critério e de periodização entre os quadros. Descrever com segurança a '
    '<b>direção</b> de um movimento vale mais que arriscar um valor errado, e o corretor percebe a '
    'diferença imediatamente.', 'ouro')
RULE()

# ===========================================================================
# APÊNDICE B — QUADRO DE AUTOAVALIAÇÃO
# ===========================================================================
H1('Apêndice B — Quadro de autoavaliação')
TXT('Depois de corrigir cada prova, verifique:')
TAB([
    ['Critério', 'Peso real na nota'],
    ['Defini os <b>conceitos</b> com precisão, em vez de usá-los como rótulos?', 'Alto'],
    ['Nomeei o <b>mecanismo</b> (sentido, exclusivo, mercê, Lei Mental, circunscrição), e não apenas a '
     'conclusão?', 'Alto'],
    ['Distingui os <b>níveis</b> da crítica — empírico, metodológico, teórico?', 'Alto'],
    ['<b>Interroguei</b> as fontes em vez de parafraseá-las?', 'Médio'],
    ['Tomei <b>posição com critério explícito</b>, em vez de concluir que “todos têm razão”?', 'Médio'],
    ['Evitei os <b>dez erros clássicos</b> do Apêndice A?', 'Alto'],
    ['Articulei os autores num <b>argumento próprio</b>, em vez de enfileirar paráfrases?', 'Médio'],
    ['Respeitei a <b>distribuição de pontos</b>, dando mais espaço ao item que vale mais?', 'Médio'],
], [CONTENT_W - 3.4 * cm, 3.4 * cm])
BOX('Como usar a pontuação a seu favor',
    'A distribuição de pontos de cada item é, na prática, um <b>roteiro de redação</b>. Um item de 6 '
    'pontos pede desenvolvimento; um de 2 pontos pede uma frase. Escrever três parágrafos sobre o que '
    'vale 2 e uma linha sobre o que vale 6 é a forma mais comum de perder nota <b>sabendo a matéria</b>.',
    'ouro')


# ===========================================================================
# GERAÇÃO
# ===========================================================================
if __name__ == '__main__':
    build_pdf(PDF, render_pdf(DOC), TITULO,
              'PROVAS DISSERTATIVAS — GABARITO COMPLETO', 'Seis autores, uma linha',
              'Material de estudo — Prova 1')
    with open(MD, 'w', encoding='utf-8') as f:
        f.write(render_md(DOC))
    print('PDF:', PDF)
    print('MD: ', MD)
