"""
Gera 'lista1-resolvida-e-exercicios-extra.pdf':
  Parte I   - Lista 1 da disciplina resolvida por completo (Q1 a Q6, todos os itens)
  Parte II  - Banco de 23 exercicios NOVOS, apenas enunciados
  Parte III - Gabaritos comentados do banco novo

Todos os resultados numericos sao conferidos por verificar_contas.py (114 checagens).
Uso: python3 gerar_lista1_resolvida_pdf.py
"""
import os

from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Spacer

from estilo_pdf import (
    BORDER, GOLD, GRAY, GREEN, LIGHT_BLUE, LIGHT_GREEN, LIGHT_PURPLE, LIGHT_RED,
    PURPLE, RED, F, P, bullets, build_pdf, caption, cover, img, note, table,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.join(ROOT, 'graficos')
OUT = os.path.join(ROOT, 'lista1-resolvida-e-exercicios-extra.pdf')

W1, W2 = 3.1 * cm, 13.6 * cm


def figure(name, text, width=16.6 * cm):
    return [img(GRAPH, name, width), caption(text)]


def resposta(text):
    return note('Resposta', text, LIGHT_GREEN, GREEN)


def enunciado(titulo, texto):
    return [P(titulo, 'H2x'), note('Enunciado', texto, colors.white, BORDER), Spacer(1, .1 * cm)]


# ===========================================================================
# PARTE I — LISTA 1 RESOLVIDA
# ===========================================================================
def parte1():
    S = [P('Parte I — Lista 1 da disciplina, resolvida por completo', 'H1x')]
    S += [P('Os enunciados abaixo são os da <b>Lista 1</b> (CE-362, 2º semestre de 2026). '
            'As equações de custo da Questão 5 estavam em imagem dentro do PDF original e foram '
            'recuperadas: são C₁(Q₁) = 10Q₁² e C₂(Q₂) = 20Q₂².', 'Bodyx')]

    # ---------------------------------------------------------------- Q1
    S += [P('Questão 1 — equilíbrio geral com Cobb–Douglas', 'H1x')]
    S += [note('Enunciado',
               'Dois agentes (A; B) e dois bens (x₁; x₂). Cada agente tem Uᵢ(x₁,x₂) = x₁·x₂. '
               'O agente A possui 4 unidades de x₁ e 2 de x₂; o agente B possui 1 de x₁ e 3 de x₂. '
               'A dotação total de cada bem é 5 unidades. Determine: (a) se haverá trocas e por quê; '
               '(b) as funções de demanda; (c) os preços relativos de equilíbrio; (d) as quantidades '
               'de equilíbrio; (e) a representação gráfica; (f) a interpretação em termos de ótimo de Pareto.',
               colors.white, BORDER)]

    S += [P('(a) Haverá trocas?', 'H2x')]
    S += [P('O critério é comparar as Taxas Marginais de Substituição <b>na dotação inicial</b>. '
            'Para U = x₁x₂, temos UMg₁ = x₂ e UMg₂ = x₁, logo TMS = x₂/x₁.', 'Bodyx')]
    S += [F('TMS_A(4,2) = 2/4 = 0,5        TMS_B(1,3) = 3/1 = 3')]
    S += [P('As TMS são <b>diferentes</b>, então existe espaço para troca mutuamente benéfica. '
            'A leitura econômica: A abre mão de apenas 0,5 unidade do bem 2 para ganhar 1 unidade do bem 1, '
            'enquanto B aceita entregar até 3. Como B valoriza o bem 1 muito mais que A, <b>A vende bem 1 '
            'e compra bem 2</b>, e B faz o oposto.', 'Bodyx')]
    S += [resposta('<b>Sim, haverá trocas</b>, porque TMS_A = 0,5 ≠ 3 = TMS_B na dotação inicial. '
                   'A alocação inicial não é Pareto-eficiente.')]

    S += [P('(b) Funções de demanda', 'H2x')]
    S += [P('Passo 1 — a renda é o valor da dotação aos preços vigentes:', 'Bodyx')]
    S += [F('m_A = 4p₁ + 2p₂          m_B = 1p₁ + 3p₂')]
    S += [P('Passo 2 — condição de ótimo TMS = p₁/p₂ combinada com a restrição orçamentária. '
            'Para Cobb–Douglas com expoentes iguais, cada agente gasta <b>metade</b> da renda em cada bem:', 'Bodyx')]
    S += [F('x₁ᵢ*(p,mᵢ) = mᵢ / (2p₁)          x₂ᵢ*(p,mᵢ) = mᵢ / (2p₂)')]
    S += [P('Escrevendo explicitamente em função dos preços:', 'Bodyx')]
    S += [F('x₁ᴬ = (4p₁+2p₂)/(2p₁)      x₂ᴬ = (4p₁+2p₂)/(2p₂)\n'
            'x₁ᴮ = (p₁+3p₂)/(2p₁)        x₂ᴮ = (p₁+3p₂)/(2p₂)')]

    S += [P('(c) Preços relativos de equilíbrio', 'H2x')]
    S += [P('Basta limpar <b>um</b> mercado (Lei de Walras cuida do outro). No mercado do bem 1:', 'Bodyx')]
    S += [F('x₁ᴬ + x₁ᴮ = 5\n'
            '(4p₁+2p₂)/(2p₁) + (p₁+3p₂)/(2p₁) = 5\n'
            '(5p₁ + 5p₂) / (2p₁) = 5\n'
            '5p₁ + 5p₂ = 10p₁   ⇒   5p₂ = 5p₁')]
    S += [resposta('<b>p₁/p₂ = 1</b> — os dois bens têm o mesmo preço em equilíbrio. '
                   'Lembre que apenas o preço relativo é determinado; podemos normalizar p₁ = p₂ = 1.')]

    S += [P('(d) Quantidades de equilíbrio', 'H2x')]
    S += [F('Com p₁ = p₂ = 1:   m_A = 4+2 = 6        m_B = 1+3 = 4')]
    S += [F('x₁ᴬ = 6/2 = 3      x₂ᴬ = 6/2 = 3\n'
            'x₁ᴮ = 4/2 = 2      x₂ᴮ = 4/2 = 2')]
    S += [P('Verificação de factibilidade: 3 + 2 = 5 ✔ para o bem 1 e 3 + 2 = 5 ✔ para o bem 2. '
            'Os dois mercados fecham, como a Lei de Walras prevê.', 'Bodyx')]
    S.append(table([
        [P('Agente', 'Smallx'), P('Dotação', 'Smallx'), P('Cesta final', 'Smallx'),
         P('Demanda líquida', 'Smallx'), P('Utilidade antes → depois', 'Smallx')],
        [P('A', 'Smallx'), P('(4, 2)', 'Smallx'), P('<b>(3, 3)</b>', 'Smallx'),
         P('(−1, +1) — vende bem 1', 'Smallx'), P('8 → <b>9</b> (melhora)', 'Smallx')],
        [P('B', 'Smallx'), P('(1, 3)', 'Smallx'), P('<b>(2, 2)</b>', 'Smallx'),
         P('(+1, −1) — compra bem 1', 'Smallx'), P('3 → <b>4</b> (melhora)', 'Smallx')],
    ], [1.8 * cm, 2.4 * cm, 2.6 * cm, 5.2 * cm, 4.7 * cm]))
    S += [resposta('<b>A = (3, 3) e B = (2, 2).</b> A troca exatamente 1 unidade do bem 1 por '
                   '1 unidade do bem 2 com B. Ambos melhoram: confirma o ganho mútuo previsto em (a).')]

    S += [P('(e) Representação gráfica', 'H2x')]
    S += figure('01-caixa-edgeworth.png',
                'Caixa de Edgeworth 5 × 5. W é a dotação (4,2) para A; E é o equilíbrio (3,3). '
                'A reta orçamentária tem inclinação −1 porque p₁/p₂ = 1. A lente amarela reúne as '
                'trocas que melhoram os dois; o núcleo é o trecho da curva de contrato dentro da lente.')
    S += [P('Como desenhar na prova, em quatro passos: (1) caixa com base 5 e altura 5, origem de A '
            'embaixo à esquerda e origem de B no canto oposto; (2) marque W = (4,2); (3) desenhe a diagonal '
            'x₂ᴬ = x₁ᴬ, que é a curva de contrato; (4) trace a reta de inclinação −1 por W e marque E = (3,3), '
            'onde a reta cruza a diagonal — nesse ponto as curvas de indiferença se tangenciam.', 'Bodyx')]

    S += [P('(f) Interpretação em termos de ótimo de Pareto', 'H2x')]
    S += [P('A curva de contrato sai da condição de eficiência TMS_A = TMS_B:', 'Bodyx')]
    S += [F('x₂ᴬ/x₁ᴬ = x₂ᴮ/x₁ᴮ = (5−x₂ᴬ)/(5−x₁ᴬ)\n'
            'x₂ᴬ(5−x₁ᴬ) = x₁ᴬ(5−x₂ᴬ)\n'
            '5x₂ᴬ − x₁ᴬx₂ᴬ = 5x₁ᴬ − x₁ᴬx₂ᴬ   ⇒   x₂ᴬ = x₁ᴬ')]
    S += [P('A curva de contrato é a <b>diagonal</b> da caixa. O equilíbrio (3,3) satisfaz x₂ᴬ = x₁ᴬ, '
            'portanto está sobre ela. No ponto E: TMS_A = 3/3 = 1, TMS_B = 2/2 = 1 e p₁/p₂ = 1, isto é, as duas '
            'taxas subjetivas se igualam à taxa objetiva de mercado.', 'Bodyx')]
    S += [note('O que isso ilustra (Primeiro Teorema do Bem-Estar)',
               'O equilíbrio competitivo alcançado pela troca voluntária é Pareto-eficiente: não há mais '
               'realocação capaz de melhorar um agente sem piorar o outro. Cuidado com a pegadinha: '
               'eficiência <b>não</b> significa justiça. Se a dotação inicial fosse muito desigual, o equilíbrio '
               'continuaria eficiente e continuaria desigual.', LIGHT_BLUE, colors.HexColor('#1F4E79'))]

    # ---------------------------------------------------------------- Q2
    S += [PageBreak(), P('Questão 2 — julgar afirmativas com Cobb–Douglas assimétrica', 'H1x')]
    S += [note('Enunciado',
               'Dois indivíduos com U(x,y) = x⁴y⁶ e V(x,y) = x⁶y⁴. Dotações iniciais (4,2) e (2,4), '
               'respectivamente. Em equilíbrio, julgue: (a) o primeiro indivíduo gastará 40% do valor de sua '
               'dotação com o bem x; (b) o preço de equilíbrio de x relativo a y é 2; (c) o primeiro indivíduo '
               'consumirá 2,4 unidades de x; (d) o módulo da TMS entre x e y para o primeiro indivíduo no '
               'equilíbrio é 1.', colors.white, BORDER)]
    S += [P('Montagem', 'H2x')]
    S += [P('Para U = xᵅyᵝ, a fração da renda gasta em x é α/(α+β). Aqui:', 'Bodyx')]
    S += [F('Indivíduo 1 (x⁴y⁶):  α/(α+β) = 4/10 = 40% em x,  60% em y\n'
            'Indivíduo 2 (x⁶y⁴):  α/(α+β) = 6/10 = 60% em x,  40% em y')]
    S += [P('Normalizando p_y = 1 e chamando r = p_x/p_y, as rendas são o valor das dotações:', 'Bodyx')]
    S += [F('m₁ = 4r + 2          m₂ = 2r + 4')]
    S += [P('Limpando o mercado do bem x (dotação total 4 + 2 = 6):', 'Bodyx')]
    S += [F('0,4(4r+2)/r + 0,6(2r+4)/r = 6\n'
            '(1,6 + 0,8/r) + (1,2 + 2,4/r) = 6\n'
            '2,8 + 3,2/r = 6   ⇒   3,2/r = 3,2   ⇒   r = 1')]
    S += [P('Com r = 1: m₁ = 6 e m₂ = 6. As cestas são:', 'Bodyx')]
    S += [F('Indivíduo 1: x₁ = 0,4·6/1 = 2,4      y₁ = 0,6·6/1 = 3,6\n'
            'Indivíduo 2: x₂ = 0,6·6/1 = 3,6      y₂ = 0,4·6/1 = 2,4')]
    S += [P('Factibilidade: 2,4 + 3,6 = 6 ✔ nos dois bens.', 'Bodyx')]
    S += [P('Julgamento item por item', 'H2x')]
    S.append(table([
        [P('Item', 'Smallx'), P('Afirmação', 'Smallx'), P('Veredito', 'Smallx'), P('Justificativa', 'Smallx')],
        [P('(a)', 'Smallx'), P('Gasta 40% da dotação em x', 'Smallx'), P('<b>VERDADEIRA</b>', 'Smallx'),
         P('Para x⁴y⁶ a fração é 4/(4+6) = 0,4, propriedade direta da Cobb–Douglas.', 'Smallx')],
        [P('(b)', 'Smallx'), P('p_x/p_y = 2', 'Smallx'), P('<b>FALSA</b>', 'Smallx'),
         P('O market clearing dá r = 1, não 2. As preferências são espelhadas e as dotações também, '
           'então o preço relativo é unitário por simetria.', 'Smallx')],
        [P('(c)', 'Smallx'), P('Consome 2,4 de x', 'Smallx'), P('<b>VERDADEIRA</b>', 'Smallx'),
         P('x₁ = 0,4 · m₁/p_x = 0,4 · 6/1 = 2,4.', 'Smallx')],
        [P('(d)', 'Smallx'), P('|TMS| = 1 no equilíbrio', 'Smallx'), P('<b>VERDADEIRA</b>', 'Smallx'),
         P('TMS = UMg_x/UMg_y = 4y/(6x) = 2(3,6)/(3·2,4) = 1, que iguala p_x/p_y = 1 — '
           'a condição de ótimo interior.', 'Smallx')],
    ], [1.3 * cm, 3.9 * cm, 2.5 * cm, 9.0 * cm]))
    S += [resposta('<b>Verdadeiras: (a), (c) e (d). Falsa: (b).</b> O preço relativo correto é p_x/p_y = 1.')]
    S += [note('Atalho de prova', 'Quando as preferências e as dotações são <b>espelhadas</b> '
               '(x⁴y⁶ com (4,2) contra x⁶y⁴ com (2,4)), o preço relativo de equilíbrio é 1 por simetria. '
               'Dá para responder (b) em segundos e conferir a álgebra depois.', GOLD)]

    # ---------------------------------------------------------------- Q3
    S += [PageBreak(), P('Questão 3 — curva de contrato com um agente Leontief', 'H1x')]
    S += [note('Enunciado',
               'Economia de troca pura com dois bens e dois indivíduos. UA(x₁,x₂) = x₁^(1/3)x₂^(2/3), '
               'UB(x₁,x₂) = min{x₁,x₂}, dotações wA = (10,20) e wB = (20,5). Avalie: '
               '(a) xA = (10,5), xB = (20,20) está na curva de contrato; (b) no equilíbrio walrasiano os preços '
               'dos dois bens são determinados e únicos; (c) o conjunto das alocações eficientes satisfaz '
               'x₂ᴬ = x₁ᴬ − 5; (d) se p₁ = 1 e p₂ = 1, o excesso de demanda será (−7,5; 7,5).',
               colors.white, BORDER)]
    S += [P('Dotações totais e o formato da caixa', 'H2x')]
    S += [F('Bem 1: 10 + 20 = 30          Bem 2: 20 + 5 = 25\n'
            'A caixa de Edgeworth tem base 30 e altura 25.')]
    S += [P('(c) primeiro, porque as outras dependem dela — a curva de contrato', 'H2x')]
    S += [P('B tem preferências Leontief (complementares perfeitos). Suas cestas ótimas ficam sempre no '
            '<b>vértice</b> da curva de indiferença, onde x₁ᴮ = x₂ᴮ; consumir mais de um bem sem o outro não '
            'aumenta o mínimo e é desperdício. Combinando com a factibilidade:', 'Bodyx')]
    S += [F('(1) x₁ᴬ + x₁ᴮ = 30\n'
            '(2) x₂ᴬ + x₂ᴮ = 25\n'
            '(3) x₁ᴮ = x₂ᴮ      (ótimo de B)')]
    S += [F('De (3) e (2):  x₂ᴬ = 25 − x₂ᴮ = 25 − x₁ᴮ\n'
            'De (1):        x₁ᴮ = 30 − x₁ᴬ\n'
            'Substituindo:  x₂ᴬ = 25 − (30 − x₁ᴬ)   ⇒   x₂ᴬ = x₁ᴬ − 5')]
    S += [resposta('<b>(c) VERDADEIRA.</b> A curva de contrato é a reta x₂ᴬ = x₁ᴬ − 5, válida no trecho '
                   'em que a alocação cabe na caixa (x₁ᴬ de 5 a 30).')]
    S += [P('(a) A alocação dada é eficiente?', 'H2x')]
    S += [P('Teste de factibilidade: 10 + 20 = 30 ✔ e 5 + 20 = 25 ✔. Teste da condição de B: '
            'x₁ᴮ = x₂ᴮ = 20 ✔, está no vértice. Teste da curva de contrato: x₂ᴬ = 5 e x₁ᴬ − 5 = 10 − 5 = 5 ✔.', 'Bodyx')]
    S += [P('Por que isso basta: no vértice de uma Leontief a curva de indiferença tem um bico, e o '
            '"conjunto de TMS" admissíveis ali é um intervalo inteiro, não um número único. Assim, qualquer '
            'TMS de A pode ser acomodada, e a eficiência não exige a igualdade usual TMS_A = TMS_B.', 'Bodyx')]
    S += [resposta('<b>(a) VERDADEIRA.</b> A alocação é factível, respeita x₁ᴮ = x₂ᴮ e satisfaz '
                   'x₂ᴬ = x₁ᴬ − 5: está na curva de contrato.')]
    S += [P('(b) Os preços são determinados e únicos?', 'H2x')]
    S += [P('Em equilíbrio geral, somente os <b>preços relativos</b> são determinados. Multiplicar todos os '
            'preços pela mesma constante positiva não altera as restrições orçamentárias nem as escolhas — '
            'é por isso que se normaliza um preço (numerário). Logo não existe um par (p₁, p₂) absoluto único.', 'Bodyx')]
    S += [resposta('<b>(b) FALSA.</b> O equilíbrio walrasiano determina apenas p₁/p₂, não os níveis absolutos.')]
    S += [P('(d) Excesso de demanda com p₁ = p₂ = 1', 'H2x')]
    S += [F('Agente A (Cobb–Douglas, frações 1/3 e 2/3):\n'
            'm_A = 10(1) + 20(1) = 30\n'
            'x₁ᴬ = (1/3)(30)/1 = 10        x₂ᴬ = (2/3)(30)/1 = 20')]
    S += [P('Note um detalhe elegante: <b>A demanda exatamente a sua própria dotação</b> (10,20). '
            'A esses preços, A não quer negociar — sua demanda líquida é (0,0).', 'Bodyx')]
    S += [F('Agente B (Leontief, x₁ = x₂ = m/(p₁+p₂)):\n'
            'm_B = 20(1) + 5(1) = 25\n'
            'x₁ᴮ = x₂ᴮ = 25/(1+1) = 12,5')]
    S += [F('Demanda líquida de B:  (12,5 − 20 ; 12,5 − 5) = (−7,5 ; +7,5)')]
    S += [F('Excesso agregado:  z₁ = (10 + 12,5) − 30 = −7,5\n'
            '                   z₂ = (20 + 12,5) − 25 = +7,5')]
    S += [resposta('<b>(d) VERDADEIRA.</b> z = (−7,5; +7,5): excesso de <b>oferta</b> do bem 1 e excesso de '
                   '<b>demanda</b> do bem 2. O leiloeiro reduziria p₁ e/ou aumentaria p₂. Confira a Lei de Walras: '
                   'p₁z₁ + p₂z₂ = 1(−7,5) + 1(+7,5) = 0 ✔')]
    S += figure('09-q3-edgeworth-leontief.png',
                'Caixa 30 × 25. A curva de contrato é a reta x₂ᴬ = x₁ᴬ − 5. A curva de indiferença de B é o '
                '"L" com vértice sobre essa reta. Em (10,5) a alocação do item (a) é eficiente; com p = (1,1) '
                'as demandas são incompatíveis e geram z = (−7,5; +7,5).')
    S += [resposta('<b>Resumo da Questão 3 — (a) V, (b) F, (c) V, (d) V.</b>')]

    # ---------------------------------------------------------------- Q4
    S += [PageBreak(), P('Questão 4 — monopolista com custo quadrático', 'H1x')]
    S += [note('Enunciado', 'A demanda de mercado é P = 18 − Q e a firma monopolista tem custo total '
               'CT(Q) = 27 + 2Q². Qual o preço fixado pelo monopolista? Qual a quantidade produzida?',
               colors.white, BORDER)]
    S += [F('Receita total:      RT = P·Q = (18 − Q)Q = 18Q − Q²\n'
            'Receita marginal:   RMg = dRT/dQ = 18 − 2Q\n'
            'Custo marginal:     CMg = dCT/dQ = 4Q')]
    S += [F('Condição de ótimo RMg = CMg:\n'
            '18 − 2Q = 4Q   ⇒   18 = 6Q   ⇒   Q_m = 3')]
    S += [F('Preço lido na DEMANDA (nunca na RMg):\n'
            'P_m = 18 − 3 = 15')]
    S += [P('Vale calcular o lucro, porque o resultado é instrutivo:', 'Bodyx')]
    S += [F('Lucro = RT − CT = 15(3) − [27 + 2(3²)] = 45 − (27 + 18) = 45 − 45 = 0')]
    S += [F('Conferindo pelo custo médio:  CMe(3) = 27/3 + 2(3) = 9 + 6 = 15 = P_m')]
    S += [resposta('<b>Q_m = 3 e P_m = 15</b>, com <b>lucro exatamente zero</b>. '
                   'Ser monopolista não garante lucro positivo: o poder de mercado permite cobrar acima do '
                   'custo marginal (15 &gt; 12), mas aqui o custo fixo de 27 consome toda a margem. '
                   'Ainda assim, produzir 3 é melhor que fechar, o que daria prejuízo de 27.')]
    S += figure('10-q4-lucro-zero.png',
                'O ótimo está onde RMg cruza CMg (Q = 3). O preço é lido na demanda (15). Como CMe(3) = 15 '
                'coincide com o preço, o retângulo de lucro tem altura zero.', 15.4 * cm)
    S += [note('Pegadinha clássica',
               'Muita gente lê o preço na curva de RMg e responde 12. O procedimento correto é: encontre Q '
               'igualando RMg = CMg e <b>suba verticalmente até a curva de demanda</b> para ler o preço.',
               LIGHT_RED, RED)]

    # ---------------------------------------------------------------- Q5
    S += [PageBreak(), P('Questão 5 — monopolista com duas fábricas', 'H1x')]
    S += [note('Enunciado',
               'Uma empresa tem duas fábricas, com C₁(Q₁) = 10Q₁² e C₂(Q₂) = 20Q₂². A demanda é P = 700 − 5Q, '
               'com Q = Q₁ + Q₂. (a) Faça um diagrama com os custos marginais das duas fábricas, as curvas de '
               'receita média e marginal e o custo marginal total; indique a produção de cada fábrica, a produção '
               'total e o preço. (b) Se o custo da mão de obra aumentar apenas na Fábrica 1, como ajustar Q₁, Q₂, '
               'a produção total e o preço?', colors.white, BORDER)]
    S += [P('(a) Alocação da produção entre as fábricas', 'H2x')]
    S += [P('O princípio é duplo. Primeiro, a firma alocaria mal a produção se uma fábrica tivesse custo '
            'marginal maior que a outra — ela transferiria unidades para a fábrica barata. Logo, no ótimo:', 'Bodyx')]
    S += [F('CMg₁ = CMg₂        (alocação eficiente entre plantas)')]
    S += [P('Segundo, o nível total segue a regra usual do monopólio. Juntando:', 'Bodyx')]
    S += [F('CMg₁ = CMg₂ = RMg')]
    S += [F('CMg₁ = dC₁/dQ₁ = 20Q₁        CMg₂ = dC₂/dQ₂ = 40Q₂\n'
            'RT = (700 − 5Q)Q   ⇒   RMg = 700 − 10Q,  com Q = Q₁ + Q₂')]
    S += [P('Passo 1 — igualar os custos marginais entre as fábricas:', 'Bodyx')]
    S += [F('20Q₁ = 40Q₂   ⇒   Q₁ = 2Q₂   ⇒   Q = Q₁ + Q₂ = 3Q₂')]
    S += [P('A Fábrica 1 é a mais eficiente na margem, por isso produz o dobro. Passo 2 — igualar à RMg:', 'Bodyx')]
    S += [F('700 − 10(3Q₂) = 40Q₂\n'
            '700 − 30Q₂ = 40Q₂   ⇒   700 = 70Q₂   ⇒   Q₂ = 10')]
    S += [F('Q₁ = 2(10) = 20        Q = 30        P = 700 − 5(30) = 550')]
    S += [P('Conferência (sempre faça): CMg₁ = 20(20) = 400; CMg₂ = 40(10) = 400; '
            'RMg = 700 − 10(30) = 400. As três coincidem ✔', 'Bodyx')]
    S += [F('Lucro = 550(30) − 10(20)² − 20(10)²\n'
            '      = 16 500 − 4 000 − 2 000 = 10 500')]
    S += [P('Sobre a curva de custo marginal <b>total</b> pedida no enunciado: ela é a soma '
            '<b>horizontal</b> das duas, isto é, para cada nível de custo marginal somam-se as quantidades:', 'Bodyx')]
    S += [F('Q = CMg/20 + CMg/40 = 3·CMg/40   ⇒   CMg_total(Q) = (40/3)Q')]
    S += [F('Checagem: (40/3)(30) = 400 ✔ — cruza a RMg exatamente em Q = 30.')]
    S += [resposta('<b>Q₁ = 20, Q₂ = 10, Q = 30, P = 550</b> e lucro de <b>10 500</b>. '
                   'A Fábrica 1 produz o dobro da 2 porque seu custo marginal cresce na metade da velocidade.')]
    S += figure('07-q5-duas-fabricas.png',
                'O diagrama pedido no item (a). A demanda é também a curva de receita média. A linha '
                'horizontal em 400 mostra a igualdade CMg₁ = CMg₂ = RMg, de onde se leem Q₁ = 20, Q₂ = 10 e '
                'Q = 30; o preço 550 é lido na demanda.')

    S += [P('(b) Alta do custo de mão de obra apenas na Fábrica 1', 'H2x')]
    S += [P('Raciocine em duas etapas. Etapa 1: CMg₁ sobe, então a curva de custo marginal total se desloca '
            'para cima/esquerda. Cruzando com a RMg (que é decrescente), a produção total <b>cai</b> e, pela '
            'demanda, o preço <b>sobe</b>.', 'Bodyx')]
    S += [P('Etapa 2, e aqui está a sutileza: com Q total menor, a receita marginal <b>sobe</b> '
            '(RMg = 700 − 10Q é decrescente em Q). Como a Fábrica 2 continua obedecendo CMg₂ = RMg, ou seja '
            '40Q₂ = RMg, um RMg maior exige <b>Q₂ maior</b>. A Fábrica 2 compensa parcialmente a retração da 1.', 'Bodyx')]
    S += [P('Ilustração numérica com um choque que eleva o CMg₁ em 100 unidades (CMg₁ = 20Q₁ + 100):', 'Bodyx')]
    S.append(table([
        [P('Variável', 'Smallx'), P('Antes', 'Smallx'), P('Depois', 'Smallx'), P('Direção', 'Smallx')],
        [P('Q₁ (Fábrica 1)', 'Smallx'), P('20', 'Smallx'), P('≈ 16,43', 'Smallx'), P('<b>REDUZIR</b>', 'Smallx')],
        [P('Q₂ (Fábrica 2)', 'Smallx'), P('10', 'Smallx'), P('≈ 10,71', 'Smallx'), P('<b>AUMENTAR</b>', 'Smallx')],
        [P('Q total', 'Smallx'), P('30', 'Smallx'), P('≈ 27,14', 'Smallx'), P('<b>REDUZIR</b>', 'Smallx')],
        [P('Preço', 'Smallx'), P('550', 'Smallx'), P('≈ 564,29', 'Smallx'), P('<b>AUMENTAR</b>', 'Smallx')],
    ], [4.2 * cm, 3.3 * cm, 3.3 * cm, 5.9 * cm]))
    S += [resposta('<b>Q₁ reduz, Q₂ aumenta, produção total reduz e preço aumenta.</b> '
                   'O erro comum é dizer que Q₂ fica inalterado: ele muda porque a receita marginal de '
                   'equilíbrio se desloca.')]
    S += figure('08-q5b-choque-custo.png',
                'O deslocamento do custo marginal total para cima reduz Q e eleva P. Como RMg é decrescente, '
                'o novo RMg de equilíbrio é mais alto, e a Fábrica 2 responde produzindo mais.', 15.4 * cm)

    # ---------------------------------------------------------------- Q6
    S += [PageBreak(), P('Questão 6 — discriminação com elasticidades diferentes', 'H1x')]
    S += [note('Enunciado', 'Um monopolista vende em dois mercados, 1 e 2, com elasticidades ε₁ = −2 e '
               'ε₂ = −4. Suponha a possibilidade de discriminação. O monopolista cobra p₁ = 2,5p₂. '
               'Ele está maximizando? Mostre.', colors.white, BORDER)]
    S += [P('Nota sobre o enunciado: por trabalhar com dois grupos de consumidores e elasticidades '
            'distintas, o caso é de discriminação de <b>terceiro grau</b>, e é assim que os slides tratam '
            'este mesmo exemplo.', 'Smallx')]
    S += [P('A condição de maximização', 'H2x')]
    S += [P('Vender uma unidade a mais em qualquer mercado custa o mesmo CMg. Então, no ótimo, a receita '
            'marginal tem de ser igual nos dois mercados — caso contrário valeria a pena remanejar vendas:', 'Bodyx')]
    S += [F('RMg₁ = RMg₂ = CMg,  com  RMg = P(1 − 1/|ε|)')]
    S += [F('RMg₁ = p₁(1 − 1/2)  = 0,50 p₁\n'
            'RMg₂ = p₂(1 − 1/4)  = 0,75 p₂')]
    S += [F('Igualando:  0,50 p₁ = 0,75 p₂   ⇒   p₁/p₂ = 0,75/0,50 = 1,5')]
    S += [P('Testando a política da firma', 'H2x')]
    S += [F('Se p₁ = 2,5 p₂:\n'
            'RMg₁ = 0,50(2,5 p₂) = 1,25 p₂\n'
            'RMg₂ = 0,75 p₂\n'
            '1,25 p₂ > 0,75 p₂   ⇒   RMg₁ > RMg₂')]
    S += [P('Como a receita marginal no mercado 1 é maior que no mercado 2, deslocar vendas para o mercado 1 '
            'aumenta a receita total sem alterar o custo total. Portanto a política atual não é ótima.', 'Bodyx')]
    S += [resposta('<b>Não, ele não está maximizando.</b> A relação ótima é <b>p₁/p₂ = 1,5</b>, e ele pratica 2,5. '
                   'O preço no mercado 1 está alto demais e no mercado 2 baixo demais. O ajuste correto é '
                   '<b>reduzir p₁</b> (vender mais no mercado 1) e/ou <b>aumentar p₂</b>, até igualar as receitas '
                   'marginais.')]
    S += [note('A regra intuitiva, e o sinal de que você entendeu',
               'O preço maior vai para o mercado <b>menos</b> elástico — aqui o mercado 1, com |ε₁| = 2. '
               'Isso está certo na direção: p₁ > p₂. O erro da firma é de <b>magnitude</b>: a diferença deveria '
               'ser de 50%, não de 150%.', GOLD)]
    S += figure('05-discriminacao-precos.png',
                'Painel da direita: demandas calibradas para |ε₁| = 2 e |ε₂| = 4 no ótimo, com CMg = 20. '
                'Os preços ótimos são 40 e 80/3 ≈ 26,7, cuja razão é exatamente 1,5.', 16.8 * cm)

    S += [note('Gabarito-resumo da Lista 1',
               '<b>Q1:</b> haverá troca; p₁/p₂ = 1; A = (3,3); B = (2,2); equilíbrio na curva de contrato '
               'x₂ᴬ = x₁ᴬ.   <b>Q2:</b> V, F, V, V (p_x/p_y = 1).   <b>Q3:</b> V, F, V, V (curva de contrato '
               'x₂ᴬ = x₁ᴬ − 5; z = (−7,5; +7,5)).   <b>Q4:</b> Q = 3, P = 15, lucro zero.   '
               '<b>Q5:</b> Q₁ = 20, Q₂ = 10, Q = 30, P = 550, lucro 10 500; com choque na Fábrica 1: '
               'Q₁ cai, Q₂ sobe, Q cai, P sobe.   <b>Q6:</b> não maximiza; p₁/p₂ deveria ser 1,5.',
               LIGHT_GREEN, GREEN)]
    return S


# ===========================================================================
# PARTE II — BANCO DE EXERCÍCIOS NOVOS (enunciados)
# ===========================================================================
EX_A = [
    ('A1', 'Troca pura simétrica',
     'Dois agentes com Uᵢ = x₁x₂. Dotações w_A = (6,2) e w_B = (2,6). '
     '(a) Calcule as TMS na dotação e diga se haverá troca. (b) Encontre p₁/p₂. '
     '(c) Encontre as cestas de equilíbrio e as demandas líquidas. (d) Escreva a curva de contrato.'),
    ('A2', 'Dotações em cantos opostos',
     'U_A = x₁^(1/2)x₂^(1/2) com w_A = (10,0); U_B = x₁^(1/4)x₂^(3/4) com w_B = (0,10). '
     '(a) Escreva a renda de cada agente. (b) Normalize p₁ = 1 e encontre p₂. '
     '(c) Encontre as cestas de equilíbrio e verifique a factibilidade. '
     '(d) Explique economicamente por que p₂ > p₁ neste caso.'),
    ('A3', 'Preferências quase-lineares',
     'Os dois agentes têm U = ln(x₁) + x₂. Dotações w_A = (2,1) e w_B = (3,4). '
     '(a) Derive a demanda por x₁ e mostre que ela não depende da renda. '
     '(b) Normalize p₂ = 1 e encontre p₁. (c) Encontre as cestas de equilíbrio. '
     '(d) Qual é o formato da curva de contrato na caixa de Edgeworth? Por quê?'),
    ('A4', 'Substitutos perfeitos contra complementares perfeitos',
     'O Consumidor I tem u(x,y) = x + 2y e dotação (0,12). O Consumidor II tem u(x,y) = min{x, 2y} '
     'e dotação (12,0). (a) Por que o preço relativo de equilíbrio é determinado pelas preferências do '
     'Consumidor I? (b) Encontre p_y/p_x. (c) Encontre as duas cestas de equilíbrio.'),
    ('A5', 'A dotação já é eficiente?',
     'U_A = x₁^(2/3)x₂^(1/3) com w_A = (6,3); U_B = x₁^(1/3)x₂^(2/3) com w_B = (3,6). '
     '(a) Calcule as TMS na dotação inicial. (b) Encontre p₁/p₂ e as cestas de equilíbrio. '
     '(c) Calcule as demandas líquidas e interprete o resultado.'),
]

EX_B = [
    ('B1', 'Monopólio com custo marginal constante e bem-estar completo',
     'Demanda P = 120 − 2Q e custo total CT = 20Q + 100. (a) Encontre Q_m, P_m e o lucro. '
     '(b) Encontre a quantidade e o preço competitivos. (c) Calcule EC, EP e ET no monopólio e na '
     'concorrência. (d) Calcule a perda de peso morto. (e) Calcule a elasticidade no ótimo e verifique '
     'a fórmula do markup P/CMg = 1/(1 − 1/|ε|).'),
    ('B2', 'Demanda na forma direta',
     'A demanda é dada por Q = 100 − 2P e o custo total é CT = 5Q. '
     '(a) Obtenha a demanda inversa. (b) Encontre Q_m, P_m e o lucro. '
     '(c) Calcule a elasticidade no ótimo e o markup.'),
    ('B3', 'Duas fábricas (variação da Q5 da lista)',
     'C₁ = 5Q₁², C₂ = 10Q₂² e demanda P = 400 − 2Q. (a) Encontre Q₁, Q₂, Q e P. '
     '(b) Calcule o lucro. (c) Escreva a curva de custo marginal total e verifique que ela cruza a RMg '
     'na quantidade encontrada.'),
    ('B4', 'Terceiro grau contra preço único',
     'Um monopolista com CMg constante = 20 atende dois mercados separáveis: Q₁ = 100 − P₁ e '
     'Q₂ = 120 − 2P₂. (a) Encontre os preços e quantidades discriminando. (b) Calcule as elasticidades '
     'no ótimo e confirme a regra "preço maior no mercado menos elástico". (c) Calcule o lucro '
     'discriminando. (d) Calcule o lucro cobrando preço único e compare.'),
    ('B5', 'Primeiro grau, monopólio uniforme e PPM',
     'Demanda P = 80 − Q e CMg = 2Q. (a) Encontre a quantidade eficiente e o excedente total sob '
     'discriminação perfeita. (b) Encontre Q_m e P_m no monopólio com preço único. '
     '(c) Calcule EC, EP e a perda de peso morto. (d) Compare o excedente total dos dois regimes e '
     'comente a diferença distributiva.'),
    ('B6', 'Markup direto pela elasticidade',
     'Um monopolista tem CMg constante igual a 30. (a) Se a elasticidade-preço da demanda no ponto '
     'ótimo é −3, qual o preço e o markup? (b) E se a elasticidade fosse −1,5? '
     '(c) O que aconteceria se a elasticidade no ponto considerado fosse −0,8?'),
]

EX_C = [
    ('C1', 'Pela Lei de Walras, se n − 1 mercados estão em equilíbrio, é possível que no n-ésimo haja '
     'excesso de demanda.'),
    ('C2', 'O Primeiro Teorema do Bem-Estar garante que o equilíbrio competitivo é equitativo.'),
    ('C3', 'Se a dotação inicial já está sobre a curva de contrato, as possibilidades de troca estão '
     'exauridas.'),
    ('C4', 'Em uma caixa de Edgeworth é impossível que uma alocação eficiente atribua consumo nulo dos '
     'dois bens a um dos consumidores.'),
    ('C5', 'No equilíbrio walrasiano de uma economia de trocas, os preços absolutos dos bens são '
     'determinados de forma única.'),
    ('C6', 'Se os dois agentes têm U = ln(x₁) + x₂, o conjunto das alocações Pareto-eficientes é uma reta '
     'vertical na caixa de Edgeworth.'),
    ('C7', 'O monopolista maximiza lucro no ponto em que P = CMg.'),
    ('C8', 'Um monopolista pode escolher um ponto na região inelástica da demanda se o seu custo marginal '
     'for suficientemente baixo.'),
    ('C9', 'Na discriminação de preços de primeiro grau não há perda de peso morto.'),
    ('C10', 'Na discriminação de terceiro grau, o preço deve ser maior no mercado com demanda mais '
     'elástica.'),
    ('C11', 'Toda a redução do excedente do consumidor provocada pelo monopólio é perda de peso morto.'),
    ('C12', 'Se as TMS de dois consumidores são diferentes, existe espaço para troca mutuamente benéfica.'),
]


def parte2():
    S = [PageBreak(), P('Parte II — Banco de 23 exercícios novos', 'H1x')]
    S += [P('Estes exercícios <b>não</b> estão na Lista 1: foram construídos no mesmo estilo e com a mesma '
            'notação, para treinar depois de dominar a lista. Resolva sem olhar a Parte III. '
            'Os blocos A e B são numéricos; o bloco C é de julgamento de afirmativas, no formato usado '
            'em provas e na ANPEC.', 'Bodyx')]
    S += [note('Como usar', '<b>Bloco A</b> (5 exercícios) — equilíbrio geral e caixa de Edgeworth. '
               '<b>Bloco B</b> (6 exercícios) — monopólio, bem-estar e discriminação. '
               '<b>Bloco C</b> (12 afirmativas) — conceitos. Tempo sugerido: 15 minutos por exercício '
               'numérico e 1 minuto por afirmativa.', LIGHT_BLUE, colors.HexColor('#1F4E79'))]

    S += [P('Bloco A — Equilíbrio geral', 'H1x')]
    for code, title, text in EX_A:
        S += enunciado(f'{code} — {title}', text)

    S += [P('Bloco B — Monopólio, bem-estar e discriminação', 'H1x')]
    for code, title, text in EX_B:
        S += enunciado(f'{code} — {title}', text)

    S += [P('Bloco C — Verdadeiro ou falso (justifique)', 'H1x')]
    rows = [[P('Nº', 'Smallx'), P('Afirmativa', 'Smallx'), P('V ou F', 'Smallx')]]
    for code, text in EX_C:
        rows.append([P(f'<b>{code}</b>', 'Smallx'), P(text, 'Smallx'), P('________', 'Smallx')])
    S.append(table(rows, [1.2 * cm, 13.3 * cm, 2.2 * cm]))
    return S


# ===========================================================================
# PARTE III — GABARITOS DO BANCO NOVO
# ===========================================================================
def parte3():
    S = [PageBreak(), P('Parte III — Gabaritos comentados do banco novo', 'H1x')]

    # ----- A1
    S += [P('A1 — Troca pura simétrica', 'H2x')]
    S += [F('TMS = x₂/x₁\n'
            'TMS_A(6,2) = 2/6 = 1/3        TMS_B(2,6) = 6/2 = 3')]
    S += [P('(a) Diferentes, então há troca: A valoriza relativamente o bem 2 e B o bem 1.', 'Answer')]
    S += [F('m_A = 6p₁ + 2p₂      m_B = 2p₁ + 6p₂\n'
            'Mercado 1:  (6p₁+2p₂)/(2p₁) + (2p₁+6p₂)/(2p₁) = 8\n'
            '(8p₁ + 8p₂)/(2p₁) = 8   ⇒   8p₁ + 8p₂ = 16p₁   ⇒   p₁ = p₂')]
    S += [F('Com p₁ = p₂ = 1:  m_A = 8, m_B = 8\n'
            'A = (4, 4)        B = (4, 4)')]
    S += [P('(c) Demandas líquidas: A = (−2, +2) e B = (+2, −2). '
            '(d) Curva de contrato: TMS_A = TMS_B dá x₂ᴬ = x₁ᴬ, a diagonal da caixa 8 × 8.', 'Answer')]
    S += [resposta('<b>p₁/p₂ = 1; A = (4,4); B = (4,4).</b> Simetria perfeita: cada um troca 2 unidades. '
                   'Utilidade de A vai de 12 para 16 e de B também de 12 para 16.')]

    # ----- A2
    S += [P('A2 — Dotações em cantos opostos', 'H2x')]
    S += [F('(a) m_A = 10p₁ + 0p₂ = 10p₁\n'
            '    m_B = 0p₁ + 10p₂ = 10p₂')]
    S += [P('As frações de gasto são: A metade em cada bem; B um quarto no bem 1 e três quartos no bem 2.', 'Answer')]
    S += [F('x₁ᴬ = (1/2)(10p₁)/p₁ = 5\n'
            'x₁ᴮ = (1/4)(10p₂)/p₁ = 2,5 p₂/p₁')]
    S += [F('Mercado 1:  5 + 2,5 p₂/p₁ = 10   ⇒   p₂/p₁ = 2')]
    S += [F('(b) Com p₁ = 1 ⇒ p₂ = 2.  m_A = 10, m_B = 20')]
    S += [F('(c) x₁ᴬ = 0,5(10)/1 = 5        x₂ᴬ = 0,5(10)/2 = 2,5\n'
            '    x₁ᴮ = 0,25(20)/1 = 5       x₂ᴮ = 0,75(20)/2 = 7,5\n'
            'Factibilidade: 5 + 5 = 10 ✔   e   2,5 + 7,5 = 10 ✔')]
    S += [P('(d) O bem 2 é mais caro porque a demanda relativa por ele é maior: B, que detém todo o estoque '
            'do bem 2, gasta 75% da renda nele, enquanto A gasta apenas 50%. Com procura relativa maior, o '
            'preço relativo de equilíbrio do bem 2 sobe.', 'Answer')]
    S += [resposta('<b>p₁/p₂ = 1/2 (ou p₂/p₁ = 2); A = (5; 2,5); B = (5; 7,5).</b>')]

    # ----- A3
    S += [P('A3 — Preferências quase-lineares', 'H2x')]
    S += [F('(a) U = ln x₁ + x₂  ⇒  UMg₁ = 1/x₁ e UMg₂ = 1\n'
            'TMS = (1/x₁)/1 = p₁/p₂   ⇒   x₁* = p₂/p₁')]
    S += [P('A demanda pelo bem 1 depende <b>apenas dos preços</b>; toda variação de renda vai para o bem 2. '
            'Essa é a marca da quase-linearidade — e a razão de a curva de contrato ser vertical.', 'Answer')]
    S += [F('x₂* = (m − p₁x₁*)/p₂ = m/p₂ − 1')]
    S += [F('(b) Os dois agentes demandam o mesmo x₁ = p₂/p₁. Dotação total do bem 1 = 2 + 3 = 5:\n'
            '2(p₂/p₁) = 5   ⇒   p₂/p₁ = 2,5   ⇒   p₁/p₂ = 2/5')]
    S += [F('(c) Com p₂ = 1 e p₁ = 0,4:\n'
            'x₁ᴬ = x₁ᴮ = 2,5\n'
            'm_A = 0,4(2) + 1(1) = 1,8   ⇒   x₂ᴬ = 1,8 − 1 = 0,8\n'
            'm_B = 0,4(3) + 1(4) = 5,2   ⇒   x₂ᴮ = 5,2 − 1 = 4,2\n'
            'Factibilidade bem 2: 0,8 + 4,2 = 5 ✔')]
    S += [P('(d) A eficiência exige TMS_A = TMS_B, ou seja 1/x₁ᴬ = 1/x₁ᴮ, logo x₁ᴬ = x₁ᴮ = 2,5. '
            'A quantidade do bem 1 de cada agente é fixa nas alocações eficientes, e o bem 2 pode ser dividido '
            'de qualquer forma: a curva de contrato é uma <b>reta vertical</b>.', 'Answer')]
    S += [resposta('<b>p₁/p₂ = 2/5; A = (2,5; 0,8); B = (2,5; 4,2).</b> Curva de contrato: reta vertical '
                   'em x₁ᴬ = 2,5.')]
    S += figure('11-a3-quaselinear.png',
                'Com utilidade quase-linear, a curva de contrato é vertical: a divisão eficiente do bem 1 é '
                'única, e só a partilha do bem 2 varia ao longo da curva.', 14.6 * cm)

    # ----- A4
    S += [P('A4 — Substitutos perfeitos contra complementares perfeitos', 'H2x')]
    S += [P('(a) O Consumidor I tem curvas de indiferença <b>retas</b>, com TMS constante igual a 1/2. '
            'Se o preço relativo diferisse de 1/2, ele iria para um canto e o mercado não fecharia. '
            'O Consumidor II tem preferências de proporção fixa: sua escolha relativa é a mesma para qualquer '
            'preço, então não ancora o preço. Logo o preço relativo é ditado pela TMS de I.', 'Answer')]
    S += [F('(b) u = x + 2y ⇒ UMg_x = 1, UMg_y = 2 ⇒ TMS = 1/2\n'
            'p_x/p_y = 1/2   ⇒   p_y/p_x = 2')]
    S += [F('(c) Consumidor II: ótimo em x = 2y; renda m_II = 12p_x. Com p_x = 1, p_y = 2:\n'
            '1(2y) + 2(y) = 12   ⇒   4y = 12   ⇒   y = 3,  x = 6')]
    S += [F('Consumidor I fica com o restante:\n'
            'x_I = 12 − 6 = 6        y_I = 12 − 3 = 9')]
    S += [P('Confira que I respeita seu orçamento: m_I = 2(12) = 24 e o gasto é 1(6) + 2(9) = 24 ✔', 'Answer')]
    S += [resposta('<b>p_y/p_x = 2; Consumidor I = (6, 9); Consumidor II = (6, 3).</b>')]

    # ----- A5
    S += [P('A5 — A dotação já é eficiente?', 'H2x')]
    S += [F('U_A = x₁^(2/3)x₂^(1/3) ⇒ TMS_A = (2/3)x₂/[(1/3)x₁] = 2x₂/x₁\n'
            'U_B = x₁^(1/3)x₂^(2/3) ⇒ TMS_B = (1/3)x₂/[(2/3)x₁] = x₂/(2x₁)')]
    S += [F('(a) Na dotação:  TMS_A(6,3) = 2(3)/6 = 1        TMS_B(3,6) = 6/(2·3) = 1')]
    S += [P('As TMS <b>já são iguais</b> na dotação inicial. Isso indica que a alocação de partida está sobre '
            'a curva de contrato e que não haverá troca.', 'Answer')]
    S += [F('(b) m_A = 6p₁ + 3p₂,  m_B = 3p₁ + 6p₂. Mercado 1 (total 9):\n'
            '(2/3)(6p₁+3p₂)/p₁ + (1/3)(3p₁+6p₂)/p₁ = 9\n'
            '(4p₁ + 2p₂) + (p₁ + 2p₂) = 9p₁\n'
            '5p₁ + 4p₂ = 9p₁   ⇒   p₁ = p₂')]
    S += [F('Com p₁ = p₂ = 1:  m_A = 9, m_B = 9\n'
            'A = (6, 3)        B = (3, 6)')]
    S += [P('(c) As demandas líquidas são (0,0) para os dois agentes. Cada um demanda exatamente a sua '
            'dotação. A economia já estava em equilíbrio: os preços apenas <b>validam</b> a alocação inicial, '
            'sem provocar nenhuma transação.', 'Answer')]
    S += [resposta('<b>Não há troca: p₁/p₂ = 1 e cada agente permanece com a própria dotação.</b> '
                   'Lição: uma dotação inicial pode já ser Pareto-eficiente, e nesse caso o equilíbrio '
                   'walrasiano coincide com ela.')]

    # ----- B1
    S += [PageBreak(), P('B1 — Monopólio com custo marginal constante e bem-estar', 'H2x')]
    S += [F('RT = (120 − 2Q)Q   ⇒   RMg = 120 − 4Q\n'
            'CT = 20Q + 100     ⇒   CMg = 20')]
    S += [F('(a) 120 − 4Q = 20   ⇒   Q_m = 25       P_m = 120 − 2(25) = 70\n'
            'Lucro = 70(25) − [20(25) + 100] = 1 750 − 600 = 1 150')]
    S += [F('(b) Competitivo (P = CMg): 120 − 2Q = 20   ⇒   Q_c = 50,  P_c = 20')]
    S += [F('(c) Monopólio:   EC = ½(25)(120 − 70) = 625\n'
            '                 EP = (70 − 20)(25) = 1 250      [retângulo, pois CMg é constante]\n'
            '                 ET = 1 875\n'
            '    Concorrência: EC = ½(50)(120 − 20) = 2 500     EP = 0     ET = 2 500')]
    S += [F('(d) PPM = 2 500 − 1 875 = 625\n'
            'Conferindo pelo triângulo: ½(50 − 25)(70 − 20) = ½(25)(50) = 625 ✔')]
    S += [F('(e) ε = (dQ/dP)(P/Q) = (−1/2)(70/25) = −1,4\n'
            'Markup: P/CMg = 70/20 = 3,5\n'
            'Fórmula: 1/(1 − 1/1,4) = 1/(1 − 0,7143) = 1/0,2857 = 3,5 ✔')]
    S += [resposta('<b>Q_m = 25, P_m = 70, lucro 1 150; Q_c = 50, P_c = 20; PPM = 625; |ε| = 1,4; '
                   'markup 3,5.</b> Note que com CMg constante o EP competitivo é zero e todo o excedente '
                   'é do consumidor.')]
    S += figure('12-b1-bem-estar.png',
                'Com custo marginal constante, o excedente do produtor no monopólio é um retângulo simples e '
                'a perda de peso morto é o triângulo entre Q_m e Q_c.', 15.4 * cm)

    # ----- B2
    S += [P('B2 — Demanda na forma direta', 'H2x')]
    S += [F('(a) Q = 100 − 2P   ⇒   2P = 100 − Q   ⇒   P = 50 − Q/2')]
    S += [P('Este é o passo que mais gera erro: é preciso <b>inverter</b> a demanda antes de derivar a '
            'receita marginal.', 'Answer')]
    S += [F('(b) RT = (50 − Q/2)Q = 50Q − Q²/2   ⇒   RMg = 50 − Q\n'
            'CMg = 5\n'
            '50 − Q = 5   ⇒   Q_m = 45        P_m = 50 − 22,5 = 27,5\n'
            'Lucro = 27,5(45) − 5(45) = 1 237,5 − 225 = 1 012,5')]
    S += [F('(c) ε = (dQ/dP)(P/Q) = (−2)(27,5/45) ≈ −1,222\n'
            'Markup = 27,5/5 = 5,5      e      1/(1 − 1/1,222) = 5,5 ✔')]
    S += [resposta('<b>Q_m = 45, P_m = 27,5, lucro 1 012,5, |ε| ≈ 1,22, markup 5,5.</b> '
                   'Demanda pouco elástica no ótimo produz markup alto.')]

    # ----- B3
    S += [P('B3 — Duas fábricas', 'H2x')]
    S += [F('CMg₁ = 10Q₁        CMg₂ = 20Q₂        RMg = 400 − 4Q')]
    S += [F('(a) Igualando as fábricas: 10Q₁ = 20Q₂   ⇒   Q₁ = 2Q₂   ⇒   Q = 3Q₂\n'
            '400 − 4(3Q₂) = 20Q₂   ⇒   400 − 12Q₂ = 20Q₂   ⇒   Q₂ = 12,5\n'
            'Q₁ = 25        Q = 37,5        P = 400 − 2(37,5) = 325')]
    S += [F('Conferência: CMg₁ = 10(25) = 250; CMg₂ = 20(12,5) = 250; RMg = 400 − 150 = 250 ✔')]
    S += [F('(b) Lucro = 325(37,5) − 5(25)² − 10(12,5)²\n'
            '         = 12 187,5 − 3 125 − 1 562,5 = 7 500')]
    S += [F('(c) Soma horizontal:  Q = CMg/10 + CMg/20 = 3CMg/20   ⇒   CMg_total = (20/3)Q\n'
            'Em Q = 37,5:  (20/3)(37,5) = 250 ✔  — cruza a RMg no ponto correto.')]
    S += [resposta('<b>Q₁ = 25, Q₂ = 12,5, Q = 37,5, P = 325, lucro 7 500.</b>')]

    # ----- B4
    S += [P('B4 — Terceiro grau contra preço único', 'H2x')]
    S += [F('(a) Mercado 1: P₁ = 100 − Q₁ ⇒ RMg₁ = 100 − 2Q₁ = 20 ⇒ Q₁ = 40, P₁ = 60\n'
            '    Mercado 2: P₂ = 60 − Q₂/2 ⇒ RMg₂ = 60 − Q₂ = 20 ⇒ Q₂ = 40, P₂ = 40')]
    S += [F('(b) ε₁ = (−1)(60/40) = −1,5        ε₂ = (−2)(40/40) = −2\n'
            'Verificação: P₁(1 − 1/1,5) = 60(1/3) = 20 = CMg ✔\n'
            '             P₂(1 − 1/2)   = 40(1/2) = 20 = CMg ✔')]
    S += [P('O mercado 1 é o menos elástico (|ε₁| = 1,5 &lt; 2) e recebe o preço mais alto (60 &gt; 40), '
            'exatamente como a regra prevê.', 'Answer')]
    S += [F('(c) Lucro discriminando = (60 − 20)(40) + (40 − 20)(40) = 1 600 + 800 = 2 400')]
    S += [F('(d) Preço único: demanda agregada Q = (100 − P) + (120 − 2P) = 220 − 3P\n'
            'P = (220 − Q)/3   ⇒   RMg = (220 − 2Q)/3 = 20   ⇒   Q = 80\n'
            'P = (220 − 80)/3 = 140/3 ≈ 46,67\n'
            'Lucro = (46,67 − 20)(80) = 6 400/3 ≈ 2 133,33')]
    S += [resposta('<b>Discriminando: P₁ = 60, P₂ = 40, lucro 2 400. Com preço único: P ≈ 46,67, '
                   'lucro ≈ 2 133,33.</b> Discriminar rende cerca de 12,5% mais lucro — é isso que explica '
                   'a prática, quando a revenda pode ser bloqueada.')]

    # ----- B5
    S += [P('B5 — Primeiro grau, monopólio uniforme e PPM', 'H2x')]
    S += [F('(a) Quantidade eficiente: P = CMg ⇒ 80 − Q = 2Q ⇒ Q = 80/3 ≈ 26,67\n'
            'Excedente total = ∫₀^(80/3) [(80 − Q) − 2Q] dQ = ∫₀^(80/3) (80 − 3Q) dQ\n'
            '                = 80Q − 1,5Q²  em  80/3  =  3 200/3 ≈ 1 066,67')]
    S += [P('Sob discriminação perfeita, esse valor inteiro vira excedente do produtor e o EC é zero.', 'Answer')]
    S += [F('(b) RMg = 80 − 2Q = 2Q   ⇒   Q_m = 20        P_m = 80 − 20 = 60')]
    S += [F('(c) EC = ½(20)(80 − 60) = 200\n'
            'EP = ∫₀²⁰ (60 − 2Q) dQ = 60(20) − 20² = 1 200 − 400 = 800\n'
            'ET = 1 000\n'
            'PPM = 3 200/3 − 1 000 = 200/3 ≈ 66,67')]
    S += [F('Conferindo a PPM pela área: ∫₂₀^(80/3) [(80 − Q) − 2Q] dQ = 200/3 ✔')]
    S += [P('(d) O excedente total é maior sob discriminação perfeita (1 066,67 contra 1 000), porque a '
            'quantidade é a eficiente. Mas a distribuição é radicalmente diferente: no primeiro grau o '
            'consumidor fica com zero, enquanto no preço único ele retém 200. Eficiência e distribuição são '
            'dimensões distintas.', 'Answer')]
    S += [resposta('<b>1º grau: Q = 80/3, ET = 3 200/3 ≈ 1 066,67 todo para a firma. '
                   'Preço único: Q = 20, P = 60, EC = 200, EP = 800, PPM = 200/3 ≈ 66,67.</b>')]

    # ----- B6
    S += [P('B6 — Markup direto pela elasticidade', 'H2x')]
    S += [F('Regra:  P(1 − 1/|ε|) = CMg      ⇒      P = CMg / (1 − 1/|ε|)')]
    S += [F('(a) |ε| = 3:   P(1 − 1/3) = 30   ⇒   P(2/3) = 30   ⇒   P = 45\n'
            '    Markup = 45/30 = 1,5')]
    S += [F('(b) |ε| = 1,5: P(1 − 1/1,5) = 30   ⇒   P(1/3) = 30   ⇒   P = 90\n'
            '    Markup = 90/30 = 3')]
    S += [P('(c) Com |ε| = 0,8 &lt; 1, teríamos 1 − 1/0,8 = −0,25, e o preço resultaria negativo — um '
            'absurdo. O que isso revela é que <b>o ponto não pode ser um ótimo</b>: na região inelástica '
            'RMg &lt; 0, então reduzir a quantidade aumentaria a receita e diminuiria o custo ao mesmo tempo. '
            'Um monopolista nunca opera ali.', 'Answer')]
    S += [resposta('<b>(a) P = 45, markup 1,5. (b) P = 90, markup 3. (c) Impossível: |ε| &lt; 1 não pode '
                   'ocorrer no ótimo.</b> Quanto menos elástica a demanda, maior o markup.')]

    # ----- C
    S += [PageBreak(), P('Bloco C — Gabarito das afirmativas', 'H1x')]
    gab = [
        ('C1', 'FALSA', 'A Lei de Walras garante o contrário: se n − 1 mercados estão em equilíbrio, o '
                        'n-ésimo também estará. O valor do excesso de demanda agregado é zero para qualquer '
                        'vetor de preços.'),
        ('C2', 'FALSA', 'O teorema garante <b>eficiência de Pareto</b>, e nada diz sobre distribuição. Uma '
                        'alocação em que um agente tem tudo pode ser eficiente.'),
        ('C3', 'VERDADEIRA', 'Estar na curva de contrato significa que não existe realocação capaz de '
                             'melhorar um sem piorar o outro; logo não há troca voluntária a fazer.'),
        ('C4', 'FALSA', 'Os cantos da caixa são eficientes. Se um agente tem tudo, melhorar o outro exige '
                        'necessariamente piorar o primeiro.'),
        ('C5', 'FALSA', 'Apenas os preços relativos são determinados; escalar todos os preços não muda nada. '
                        'Por isso normalizamos um preço como numerário.'),
        ('C6', 'VERDADEIRA', 'Com U = ln x₁ + x₂, a eficiência exige 1/x₁ᴬ = 1/x₁ᴮ, ou seja x₁ᴬ fixo. '
                             'A curva de contrato é vertical (ver exercício A3).'),
        ('C7', 'FALSA', 'P = CMg é a condição da concorrência perfeita. O monopolista usa RMg = CMg e depois '
                        'lê o preço na curva de demanda, o que em geral resulta em P &gt; CMg.'),
        ('C8', 'FALSA', 'Na região inelástica RMg &lt; 0. Reduzir a quantidade aumentaria a receita e '
                        'reduziria o custo simultaneamente, então nenhum ponto ali pode ser ótimo, '
                        'independentemente do nível do CMg.'),
        ('C9', 'VERDADEIRA', 'A firma expande a produção enquanto a disposição a pagar exceder o CMg, '
                             'atingindo a quantidade eficiente. Todo o excedente, porém, é capturado por ela.'),
        ('C10', 'FALSA', 'É o inverso: preço mais alto no mercado <b>menos</b> elástico. A condição '
                         'RMg₁ = RMg₂ = CMg implica que quem tem demanda mais rígida paga mais.'),
        ('C11', 'FALSA', 'Parte da queda do EC é <b>transferência</b> para o produtor (o retângulo de '
                         'margem). A perda de peso morto é apenas a parcela que não vira excedente de ninguém.'),
        ('C12', 'VERDADEIRA', 'TMS diferentes significam avaliações relativas diferentes, o que abre espaço '
                              'para uma troca que melhore ambos. A troca cessa quando as TMS se igualam ou '
                              'em soluções de canto/vértice.'),
    ]
    rows = [[P('Nº', 'Smallx'), P('Resposta', 'Smallx'), P('Por quê', 'Smallx')]]
    for code, verdict, why in gab:
        rows.append([P(f'<b>{code}</b>', 'Smallx'), P(f'<b>{verdict}</b>', 'Smallx'), P(why, 'Smallx')])
    S.append(table(rows, [1.2 * cm, 2.5 * cm, 13.0 * cm]))

    S += [Spacer(1, .3 * cm)]
    S += [note('Placar de referência',
               'Bloco C: 8 ou mais acertos indicam boa base conceitual. Os erros mais frequentes são em '
               '<b>C8</b> (região inelástica), <b>C10</b> (direção da regra de elasticidade) e <b>C11</b> '
               '(transferência versus peso morto) — releia essas três justificativas com atenção.', GOLD)]
    S += [Spacer(1, .3 * cm)]
    S += [P('<b>Nota de conferência:</b> todos os valores numéricos deste PDF — as seis questões da Lista 1 e '
            'os onze exercícios numéricos do banco novo — são recalculados automaticamente pelo script '
            'verificar_contas.py, com 114 checagens simbólicas em SymPy. Se algum número fosse alterado por '
            'engano, o script falharia.', 'Smallx')]
    return S


if __name__ == '__main__':
    badge = note('O que há neste arquivo',
                 'Parte I — as seis questões da Lista 1 resolvidas passo a passo, com todos os itens. '
                 'Parte II — 23 exercícios novos (11 numéricos e 12 afirmativas), apenas com enunciados. '
                 'Parte III — gabaritos comentados dos exercícios novos.',
                 LIGHT_PURPLE, PURPLE)
    story = cover('LISTA 1 RESOLVIDA', 'e banco de exercícios novos para treinar',
                  ['<b>Disciplina:</b> CE-362 / CE-362D — Microeconomia II',
                   '<b>Universidade:</b> Instituto de Economia — Unicamp',
                   '<b>Tópicos:</b> equilíbrio geral, caixa de Edgeworth, monopólio,',
                   'bem-estar e discriminação de preços'],
                  badge)
    story += parte1() + parte2() + parte3()
    path = build_pdf(OUT, story,
                     title='Lista 1 resolvida e exercícios extra — Microeconomia II',
                     left_title='LISTA 1 RESOLVIDA + EXERCÍCIOS NOVOS',
                     right_title='Microeconomia II | Unicamp',
                     footer_note='Confira sempre a notação usada em aula')
    print(path)
    print(os.path.getsize(path), 'bytes')
