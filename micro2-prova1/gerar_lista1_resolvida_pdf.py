"""
Gera 'lista1-resolvida-e-exercicios-extra.pdf':
  Parte I   - Lista 1 da disciplina resolvida por completo (Q1 a Q6, todos os itens)
  Parte II  - Banco de 23 exercicios NOVOS, apenas enunciados
  Parte III - Gabaritos comentados do banco novo

Toda a matematica de exibicao e LaTeX renderizado (ver estilo_pdf.formula).
Os resultados numericos sao conferidos por verificar_contas.py (114 checagens).
Uso: python3 gerar_lista1_resolvida_pdf.py
"""
import os

from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Spacer

from estilo_pdf import (
    BLUE, BORDER, GOLD, GREEN, LIGHT_BLUE, LIGHT_GREEN, LIGHT_PURPLE, LIGHT_RED,
    PURPLE, RED, P, build_pdf, caption, cover, formula, img, note, table,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.join(ROOT, 'graficos')
OUT = os.path.join(ROOT, 'lista1-resolvida-e-exercicios-extra.pdf')


def figure(name, text, width=16.6 * cm):
    return [img(GRAPH, name, width), caption(text)]


def resposta(text):
    return note('Resposta', text, LIGHT_GREEN, GREEN)


def enunciado(titulo, texto):
    return [P(titulo, 'H2x'), note('Enunciado', texto, colors.white, BORDER),
            Spacer(1, .1 * cm)]


# ===========================================================================
# PARTE I — LISTA 1 RESOLVIDA
# ===========================================================================
def q1():
    S = [P('Questão 1 — equilíbrio geral com Cobb–Douglas', 'H1x')]
    S += [note('Enunciado',
               'Dois agentes (A; B) e dois bens (x₁; x₂). Cada agente tem '
               'U<sub>i</sub>(x₁,x₂) = x₁·x₂. O agente A possui 4 unidades de x₁ e 2 de x₂; o agente B '
               'possui 1 de x₁ e 3 de x₂. A dotação total de cada bem é 5 unidades. Determine: '
               '(a) se haverá trocas e por quê; (b) as funções de demanda; (c) os preços relativos de '
               'equilíbrio; (d) as quantidades de equilíbrio; (e) a representação gráfica; '
               '(f) a interpretação em termos de ótimo de Pareto.', colors.white, BORDER)]

    S += [P('(a) Haverá trocas?', 'H2x')]
    S += [P('O critério é comparar as Taxas Marginais de Substituição <b>na dotação inicial</b>. '
            'Para U = x₁x₂ temos UMg₁ = x₂ e UMg₂ = x₁, logo a TMS é a razão x₂/x₁.')]
    S += formula([
        r'TMS_i = \frac{UMg_1^i}{UMg_2^i} = \frac{x_2^i}{x_1^i}',
        r'TMS_A(4,2) = \frac{2}{4} = 0{,}5 \qquad TMS_B(1,3) = \frac{3}{1} = 3',
    ])
    S += [P('As TMS são <b>diferentes</b>, então existe espaço para troca mutuamente benéfica. '
            'A leitura econômica: A abre mão de apenas 0,5 unidade do bem 2 para ganhar 1 unidade do '
            'bem 1, enquanto B aceitaria entregar até 3. Como B valoriza relativamente mais o bem 1, '
            '<b>A vende bem 1 e compra bem 2</b>, e B faz o oposto.')]
    S += [resposta('<b>Sim, haverá trocas</b>, porque TMS<sub>A</sub> = 0,5 ≠ 3 = TMS<sub>B</sub> na '
                   'dotação inicial. A alocação inicial não é Pareto-eficiente.')]

    S += [P('(b) Funções de demanda', 'H2x')]
    S += [P('Passo 1 — a renda é o valor da dotação aos preços vigentes:')]
    S += formula([r'm_A = 4p_1 + 2p_2 \qquad m_B = 1p_1 + 3p_2'])
    S += [P('Passo 2 — a condição de ótimo TMS = p₁/p₂ junto com a restrição orçamentária. Para '
            'Cobb–Douglas com expoentes iguais, cada agente gasta <b>metade</b> da renda em cada bem:')]
    S += formula([
        r'x_1^{i\,*}(p, m_i) = \frac{m_i}{2p_1} \qquad x_2^{i\,*}(p, m_i) = \frac{m_i}{2p_2}',
    ])
    S += [P('Escrevendo explicitamente em função dos preços:')]
    S += formula([
        r'x_1^A = \frac{4p_1 + 2p_2}{2p_1} \qquad x_2^A = \frac{4p_1 + 2p_2}{2p_2}',
        r'x_1^B = \frac{p_1 + 3p_2}{2p_1} \qquad x_2^B = \frac{p_1 + 3p_2}{2p_2}',
    ])

    S += [P('(c) Preços relativos de equilíbrio', 'H2x')]
    S += [P('Basta equilibrar <b>um</b> mercado, porque a Lei de Walras garante o outro. '
            'No mercado do bem 1:')]
    S += formula([
        r'x_1^A + x_1^B = 5',
        r'\frac{4p_1 + 2p_2}{2p_1} + \frac{p_1 + 3p_2}{2p_1} = 5',
        r'\frac{5p_1 + 5p_2}{2p_1} = 5 \;\Longrightarrow\; 5p_1 + 5p_2 = 10p_1 '
        r'\;\Longrightarrow\; p_1 = p_2',
    ])
    S += [resposta('<b>p₁/p₂ = 1</b> — os dois bens têm o mesmo preço em equilíbrio. Lembre que apenas o '
                   'preço relativo é determinado, então podemos normalizar p₁ = p₂ = 1.')]

    S += [P('(d) Quantidades de equilíbrio', 'H2x')]
    S += formula([
        r'p_1 = p_2 = 1 \;\Longrightarrow\; m_A = 4 + 2 = 6 \qquad m_B = 1 + 3 = 4',
        r'x_1^A = \frac{6}{2} = 3 \qquad x_2^A = \frac{6}{2} = 3',
        r'x_1^B = \frac{4}{2} = 2 \qquad x_2^B = \frac{4}{2} = 2',
        r'\text{factibilidade: } 3 + 2 = 5 \;\checkmark \quad\text{(nos dois bens)}',
    ])
    S.append(table([
        [P('Agente', 'Smallx'), P('Dotação', 'Smallx'), P('Cesta final', 'Smallx'),
         P('Demanda líquida', 'Smallx'), P('Utilidade', 'Smallx')],
        [P('A', 'Smallx'), P('(4, 2)', 'Smallx'), P('<b>(3, 3)</b>', 'Smallx'),
         P('(−1, +1) — vende bem 1', 'Smallx'), P('8 → <b>9</b>', 'Smallx')],
        [P('B', 'Smallx'), P('(1, 3)', 'Smallx'), P('<b>(2, 2)</b>', 'Smallx'),
         P('(+1, −1) — compra bem 1', 'Smallx'), P('3 → <b>4</b>', 'Smallx')],
    ], [1.8 * cm, 2.4 * cm, 2.6 * cm, 5.5 * cm, 3.4 * cm]))
    S += [resposta('<b>A = (3, 3) e B = (2, 2).</b> A troca exatamente 1 unidade do bem 1 por 1 unidade '
                   'do bem 2 com B. Ambos melhoram, o que confirma o ganho mútuo previsto no item (a).')]

    S += [P('(e) Representação gráfica', 'H2x')]
    S += figure('01-caixa-edgeworth.png',
                'Caixa de Edgeworth 5 × 5. W é a dotação (4,2) para A; E é o equilíbrio (3,3). A reta '
                'orçamentária tem inclinação −1 porque p₁/p₂ = 1. A lente amarela reúne as trocas que '
                'melhoram os dois, e o núcleo é o trecho da curva de contrato dentro dela.')
    S += [P('Como desenhar na prova, em quatro passos: (1) caixa de base 5 e altura 5, com a origem de A '
            'embaixo à esquerda e a de B no canto oposto; (2) marque W = (4,2); (3) desenhe a diagonal, '
            'que é a curva de contrato; (4) trace a reta de inclinação −1 por W e marque E = (3,3), onde '
            'ela cruza a diagonal — ali as curvas de indiferença se tangenciam.')]

    S += [P('(f) Interpretação em termos de ótimo de Pareto', 'H2x')]
    S += [P('A curva de contrato vem da condição de eficiência TMS<sub>A</sub> = TMS<sub>B</sub>:')]
    S += formula([
        r'\frac{x_2^A}{x_1^A} = \frac{x_2^B}{x_1^B} = \frac{5 - x_2^A}{5 - x_1^A}',
        r'x_2^A\left(5 - x_1^A\right) = x_1^A\left(5 - x_2^A\right)',
        r'5x_2^A - x_1^A x_2^A = 5x_1^A - x_1^A x_2^A \;\Longrightarrow\; x_2^A = x_1^A',
    ])
    S += [P('A curva de contrato é a <b>diagonal</b> da caixa. O equilíbrio (3,3) a satisfaz, então está '
            'sobre ela. No ponto E todas as taxas coincidem:')]
    S += formula([r'TMS_A = \frac{3}{3} = 1 \qquad TMS_B = \frac{2}{2} = 1 \qquad \frac{p_1}{p_2} = 1'])
    S += [note('O que isso ilustra (Primeiro Teorema do Bem-Estar)',
               'O equilíbrio competitivo alcançado pela troca voluntária é Pareto-eficiente: não há mais '
               'realocação capaz de melhorar um agente sem piorar o outro. Cuidado com a pegadinha: '
               'eficiência <b>não</b> significa justiça. Se a dotação inicial fosse muito desigual, o '
               'equilíbrio continuaria eficiente e continuaria desigual.', LIGHT_BLUE, BLUE)]
    return S


def q2():
    S = [PageBreak(), P('Questão 2 — julgar afirmativas com Cobb–Douglas assimétrica', 'H1x')]
    S += [note('Enunciado',
               'Dois indivíduos com U(x,y) = x⁴y⁶ e V(x,y) = x⁶y⁴. Dotações iniciais (4,2) e (2,4), '
               'respectivamente. Em equilíbrio, julgue: (a) o primeiro indivíduo gastará 40% do valor de '
               'sua dotação com o bem x; (b) o preço de equilíbrio de x relativo a y é 2; (c) o primeiro '
               'indivíduo consumirá 2,4 unidades de x; (d) o módulo da TMS entre x e y para o primeiro '
               'indivíduo no equilíbrio é 1.', colors.white, BORDER)]

    S += [P('Montagem', 'H2x')]
    S += [P('Para U = xᵅyᵝ, a fração da renda gasta em x é α/(α+β):')]
    S += formula([
        r'\text{indivíduo 1 } (x^4y^6): \quad \frac{4}{10} = 40\% \text{ em } x, \;\; 60\% \text{ em } y',
        r'\text{indivíduo 2 } (x^6y^4): \quad \frac{6}{10} = 60\% \text{ em } x, \;\; 40\% \text{ em } y',
    ])
    S += [P('Normalizando p<sub>y</sub> = 1 e chamando r = p<sub>x</sub>/p<sub>y</sub>, as rendas são o '
            'valor das dotações:')]
    S += formula([
        r'm_1 = 4r + 2 \qquad m_2 = 2r + 4',
        r'\frac{0{,}4(4r+2)}{r} + \frac{0{,}6(2r+4)}{r} = 6',
        r'\left(1{,}6 + \frac{0{,}8}{r}\right) + \left(1{,}2 + \frac{2{,}4}{r}\right) = 6',
        r'2{,}8 + \frac{3{,}2}{r} = 6 \;\Longrightarrow\; \frac{3{,}2}{r} = 3{,}2 '
        r'\;\Longrightarrow\; r = 1',
    ])
    S += [P('Com r = 1 temos m₁ = 6 e m₂ = 6, e as cestas ficam:')]
    S += formula([
        r'\text{indivíduo 1:}\quad x_1 = 0{,}4\cdot\frac{6}{1} = 2{,}4 \qquad y_1 = 0{,}6\cdot 6 = 3{,}6',
        r'\text{indivíduo 2:}\quad x_2 = 0{,}6\cdot\frac{6}{1} = 3{,}6 \qquad y_2 = 0{,}4\cdot 6 = 2{,}4',
        r'\text{factibilidade: } 2{,}4 + 3{,}6 = 6 \;\checkmark \quad\text{(nos dois bens)}',
    ])
    S += [P('E a TMS do indivíduo 1 no equilíbrio:')]
    S += formula([
        r'TMS_1 = \frac{UMg_x}{UMg_y} = \frac{4x^3y^6}{6x^4y^5} = \frac{4y}{6x} '
        r'= \frac{2(3{,}6)}{3(2{,}4)} = 1 = \frac{p_x}{p_y}',
    ])

    S += [P('Julgamento item por item', 'H2x')]
    S.append(table([
        [P('Item', 'Smallx'), P('Afirmação', 'Smallx'), P('Veredito', 'Smallx'),
         P('Justificativa', 'Smallx')],
        [P('(a)', 'Smallx'), P('Gasta 40% da dotação em x', 'Smallx'), P('<b>VERDADEIRA</b>', 'Smallx'),
         P('Para x⁴y⁶ a fração é 4/(4+6) = 0,4, propriedade direta da Cobb–Douglas.', 'Smallx')],
        [P('(b)', 'Smallx'), P('p<sub>x</sub>/p<sub>y</sub> = 2', 'Smallx'), P('<b>FALSA</b>', 'Smallx'),
         P('O equilíbrio de mercado dá r = 1, não 2. Preferências e dotações são espelhadas, então o '
           'preço relativo é unitário por simetria.', 'Smallx')],
        [P('(c)', 'Smallx'), P('Consome 2,4 de x', 'Smallx'), P('<b>VERDADEIRA</b>', 'Smallx'),
         P('x₁ = 0,4 · m₁/p<sub>x</sub> = 0,4 · 6/1 = 2,4.', 'Smallx')],
        [P('(d)', 'Smallx'), P('|TMS| = 1 no equilíbrio', 'Smallx'), P('<b>VERDADEIRA</b>', 'Smallx'),
         P('A TMS é 4y/(6x) = 1, que iguala p<sub>x</sub>/p<sub>y</sub> = 1 — a condição de ótimo '
           'interior.', 'Smallx')],
    ], [1.3 * cm, 4.0 * cm, 2.6 * cm, 8.8 * cm]))
    S += [resposta('<b>Verdadeiras: (a), (c) e (d). Falsa: (b).</b> O preço relativo correto é '
                   'p<sub>x</sub>/p<sub>y</sub> = 1.')]
    S += [note('Atalho de prova',
               'Quando as preferências e as dotações são <b>espelhadas</b> (x⁴y⁶ com (4,2) contra x⁶y⁴ '
               'com (2,4)), o preço relativo de equilíbrio é 1 por simetria. Dá para responder (b) em '
               'segundos e conferir a álgebra depois.', GOLD)]
    return S


def q3():
    S = [PageBreak(), P('Questão 3 — curva de contrato com um agente Leontief', 'H1x')]
    S += [note('Enunciado',
               'Economia de troca pura com dois bens e dois indivíduos. '
               'U<sub>A</sub>(x₁,x₂) = x₁<super>1/3</super>x₂<super>2/3</super>, '
               'U<sub>B</sub>(x₁,x₂) = min{x₁,x₂}, dotações w<sub>A</sub> = (10,20) e '
               'w<sub>B</sub> = (20,5). Avalie: (a) x<sub>A</sub> = (10,5), x<sub>B</sub> = (20,20) está '
               'na curva de contrato; (b) no equilíbrio walrasiano os preços dos dois bens são '
               'determinados e únicos; (c) o conjunto das alocações eficientes satisfaz '
               'x₂<super>A</super> = x₁<super>A</super> − 5; (d) se p₁ = 1 e p₂ = 1, o excesso de demanda '
               'será (−7,5; 7,5).', colors.white, BORDER)]

    S += [P('Dotações totais e o formato da caixa', 'H2x')]
    S += formula([
        r'\text{bem 1: } 10 + 20 = 30 \qquad \text{bem 2: } 20 + 5 = 25',
        r'\text{a caixa de Edgeworth tem base } 30 \text{ e altura } 25',
    ])

    S += [P('(c) primeiro, porque os outros itens dependem dele', 'H2x')]
    S += [P('B tem preferências Leontief (complementares perfeitos). Suas cestas ótimas ficam sempre no '
            '<b>vértice</b> da curva de indiferença, onde as quantidades se igualam: consumir mais de um '
            'bem sem o outro não aumenta o mínimo e é desperdício. Combinando com a factibilidade:')]
    S += formula([
        r'(1)\;\; x_1^A + x_1^B = 30 \qquad (2)\;\; x_2^A + x_2^B = 25 '
        r'\qquad (3)\;\; x_1^B = x_2^B',
        r'\text{de (3) e (2): } x_2^A = 25 - x_2^B = 25 - x_1^B',
        r'\text{de (1): } x_1^B = 30 - x_1^A',
        r'x_2^A = 25 - \left(30 - x_1^A\right) \;\Longrightarrow\; x_2^A = x_1^A - 5',
    ])
    S += [resposta('<b>(c) VERDADEIRA.</b> A curva de contrato é a reta x₂<super>A</super> = '
                   'x₁<super>A</super> − 5, no trecho em que a alocação cabe na caixa '
                   '(x₁<super>A</super> de 5 a 30).')]

    S += [P('(a) A alocação dada é eficiente?', 'H2x')]
    S += formula([
        r'\text{factibilidade: } 10 + 20 = 30 \;\checkmark \qquad 5 + 20 = 25 \;\checkmark',
        r'\text{vértice de B: } x_1^B = x_2^B = 20 \;\checkmark',
        r'\text{curva de contrato: } x_2^A = 5 \;\text{ e }\; x_1^A - 5 = 10 - 5 = 5 \;\checkmark',
    ])
    S += [P('Por que esses três testes bastam: no vértice de uma Leontief a curva de indiferença tem um '
            'bico, e o conjunto de TMS admissíveis ali é um intervalo inteiro em vez de um número único. '
            'Assim qualquer TMS de A pode ser acomodada, e a eficiência não exige a igualdade usual '
            'TMS<sub>A</sub> = TMS<sub>B</sub>.')]
    S += [resposta('<b>(a) VERDADEIRA.</b> A alocação é factível, respeita o vértice de B e satisfaz a '
                   'curva de contrato.')]

    S += [P('(b) Os preços são determinados e únicos?', 'H2x')]
    S += [P('Em equilíbrio geral, somente os <b>preços relativos</b> são determinados. Multiplicar todos '
            'os preços pela mesma constante positiva não altera as restrições orçamentárias nem as '
            'escolhas — é justamente por isso que se normaliza um preço como numerário. Logo não existe '
            'um par absoluto único.')]
    S += [resposta('<b>(b) FALSA.</b> O equilíbrio walrasiano determina apenas p₁/p₂, não os níveis '
                   'absolutos.')]

    S += [P('(d) Excesso de demanda com p₁ = p₂ = 1', 'H2x')]
    S += formula([
        r'\text{agente A (Cobb--Douglas, frações } 1/3 \text{ e } 2/3):',
        r'm_A = 10(1) + 20(1) = 30',
        r'x_1^A = \frac{1}{3}\cdot\frac{30}{1} = 10 \qquad x_2^A = \frac{2}{3}\cdot\frac{30}{1} = 20',
    ])
    S += [P('Note um detalhe elegante: <b>A demanda exatamente a sua própria dotação</b> (10,20). '
            'A esses preços A não quer negociar, e sua demanda líquida é nula.')]
    S += formula([
        r'\text{agente B (Leontief): } x_1 = x_2 = \frac{m}{p_1 + p_2}',
        r'm_B = 20(1) + 5(1) = 25 \;\Longrightarrow\; x_1^B = x_2^B = \frac{25}{2} = 12{,}5',
        r'e^A = (0,\; 0) \qquad e^B = (12{,}5 - 20,\;\; 12{,}5 - 5) = (-7{,}5;\; +7{,}5)',
        r'z_1 = (10 + 12{,}5) - 30 = -7{,}5 \qquad z_2 = (20 + 12{,}5) - 25 = +7{,}5',
        r'\text{Lei de Walras: } p_1 z_1 + p_2 z_2 = 1(-7{,}5) + 1(+7{,}5) = 0 \;\checkmark',
    ])
    S += [resposta('<b>(d) VERDADEIRA.</b> z = (−7,5; +7,5): excesso de <b>oferta</b> do bem 1 e excesso '
                   'de <b>demanda</b> do bem 2. O leiloeiro reduziria p₁ e/ou aumentaria p₂.')]
    S += figure('09-q3-edgeworth-leontief.png',
                'Caixa 30 × 25. A curva de contrato é a reta x₂ᴬ = x₁ᴬ − 5 e a curva de indiferença de B '
                'é o "L" com vértice sobre ela. Em (10,5) a alocação do item (a) é eficiente; com '
                'p = (1,1) as demandas são incompatíveis e geram z = (−7,5; +7,5).')
    S += [resposta('<b>Resumo da Questão 3 — (a) V, (b) F, (c) V, (d) V.</b>')]
    return S


def q4():
    S = [PageBreak(), P('Questão 4 — monopolista com custo quadrático', 'H1x')]
    S += [note('Enunciado', 'A demanda de mercado é P = 18 − Q e a firma monopolista tem custo total '
               'CT(Q) = 27 + 2Q². Qual o preço fixado pelo monopolista? Qual a quantidade produzida?',
               colors.white, BORDER)]
    S += formula([
        r'R(Q) = P\cdot Q = (18 - Q)Q = 18Q - Q^2',
        r'RMg = \frac{dR}{dQ} = 18 - 2Q \qquad CMg = \frac{dCT}{dQ} = 4Q',
        r'RMg = CMg: \quad 18 - 2Q = 4Q \;\Longrightarrow\; 18 = 6Q \;\Longrightarrow\; Q_m = 3',
        r'P_m = 18 - 3 = 15 \quad \text{(lido na DEMANDA, nunca na } RMg)',
    ])
    S += [P('Vale calcular o lucro, porque o resultado é instrutivo:')]
    S += formula([
        r'\pi = R - CT = 15(3) - \left[27 + 2(3^2)\right] = 45 - (27 + 18) = 45 - 45 = 0',
        r'\text{conferindo pelo custo médio: } CMe(3) = \frac{27}{3} + 2(3) = 9 + 6 = 15 = P_m',
    ])
    S += [resposta('<b>Q<sub>m</sub> = 3 e P<sub>m</sub> = 15</b>, com <b>lucro exatamente zero</b>. '
                   'Ser monopolista não garante lucro positivo: o poder de mercado permite cobrar acima '
                   'do custo marginal (15 contra 12), mas aqui o custo fixo de 27 consome toda a margem. '
                   'Ainda assim produzir 3 é melhor que fechar, o que daria prejuízo de 27.')]
    S += figure('10-q4-lucro-zero.png',
                'O ótimo está onde RMg cruza CMg (Q = 3) e o preço é lido na demanda (15). Como CMe(3) '
                'coincide com o preço, o retângulo de lucro tem altura zero.', 15.4 * cm)
    S += [note('Pegadinha clássica',
               'Muita gente lê o preço na curva de receita marginal e responde 12. O procedimento '
               'correto é achar Q igualando RMg = CMg e <b>subir verticalmente até a curva de '
               'demanda</b> para ler o preço.', LIGHT_RED, RED)]
    return S


def q5():
    S = [PageBreak(), P('Questão 5 — monopolista com duas fábricas', 'H1x')]
    S += [note('Enunciado',
               'Uma empresa tem duas fábricas, com C₁(Q₁) = 10Q₁² e C₂(Q₂) = 20Q₂². A demanda é '
               'P = 700 − 5Q, com Q = Q₁ + Q₂. (a) Faça um diagrama com os custos marginais das duas '
               'fábricas, as curvas de receita média e marginal e o custo marginal total; indique a '
               'produção de cada fábrica, a produção total e o preço. (b) Se o custo da mão de obra '
               'aumentar apenas na Fábrica 1, como ajustar Q₁, Q₂, a produção total e o preço?',
               colors.white, BORDER)]
    S += [P('As equações de custo estavam embutidas como imagem no PDF original da lista e foram '
            'recuperadas por renderização.', 'Smallx')]

    S += [P('(a) Alocação da produção entre as fábricas', 'H2x')]
    S += [P('O princípio é duplo. Primeiro, a firma alocaria mal a produção se uma fábrica tivesse custo '
            'marginal maior que a outra: ela transferiria unidades para a fábrica mais barata na margem. '
            'Segundo, o nível total segue a regra usual do monopólio. Juntando as duas condições:')]
    S += formula([r'CMg_1 = CMg_2 = RMg'])
    S += formula([
        r'CMg_1 = \frac{dC_1}{dQ_1} = 20Q_1 \qquad CMg_2 = \frac{dC_2}{dQ_2} = 40Q_2',
        r'R = (700 - 5Q)Q \;\Longrightarrow\; RMg = 700 - 10Q, \quad Q = Q_1 + Q_2',
    ])
    S += [P('Passo 1 — igualar os custos marginais entre as fábricas:')]
    S += formula([
        r'20Q_1 = 40Q_2 \;\Longrightarrow\; Q_1 = 2Q_2 \;\Longrightarrow\; Q = Q_1 + Q_2 = 3Q_2',
    ])
    S += [P('A Fábrica 1 é a mais eficiente na margem, por isso produz o dobro. '
            'Passo 2 — igualar à receita marginal:')]
    S += formula([
        r'700 - 10(3Q_2) = 40Q_2 \;\Longrightarrow\; 700 - 30Q_2 = 40Q_2 '
        r'\;\Longrightarrow\; Q_2 = 10',
        r'Q_1 = 2(10) = 20 \qquad Q = 30 \qquad P = 700 - 5(30) = 550',
        r'\text{conferência: } CMg_1 = 20(20) = 400,\;\; CMg_2 = 40(10) = 400,\;\; '
        r'RMg = 700 - 300 = 400 \;\checkmark',
        r'\pi = 550(30) - 10(20)^2 - 20(10)^2 = 16\,500 - 4\,000 - 2\,000 = 10\,500',
    ])
    S += [P('Sobre a curva de custo marginal <b>total</b> pedida no enunciado: ela é a soma '
            '<b>horizontal</b> das duas, isto é, para cada nível de custo marginal somam-se as '
            'quantidades que cada fábrica produziria:')]
    S += formula([
        r'Q = \frac{CMg}{20} + \frac{CMg}{40} = \frac{3\,CMg}{40} '
        r'\;\Longrightarrow\; CMg_{total}(Q) = \frac{40}{3}Q',
        r'\text{checagem: } \frac{40}{3}(30) = 400 \;\checkmark \quad '
        r'\text{cruza a } RMg \text{ exatamente em } Q = 30',
    ])
    S += [resposta('<b>Q₁ = 20, Q₂ = 10, Q = 30, P = 550</b> e lucro de <b>10 500</b>. A Fábrica 1 '
                   'produz o dobro da 2 porque seu custo marginal cresce na metade da velocidade.')]
    S += figure('07-q5-duas-fabricas.png',
                'O diagrama pedido no item (a). A demanda é também a curva de receita média. A linha '
                'horizontal em 400 mostra a igualdade CMg₁ = CMg₂ = RMg, de onde se leem Q₁ = 20, '
                'Q₂ = 10 e Q = 30; o preço 550 é lido na demanda.')

    S += [P('(b) Alta do custo de mão de obra apenas na Fábrica 1', 'H2x')]
    S += [P('Etapa 1: CMg₁ sobe, então a curva de custo marginal total se desloca para cima e para a '
            'esquerda. Cruzando com a receita marginal, que é decrescente, a produção total <b>cai</b> '
            'e, pela demanda, o preço <b>sobe</b>.')]
    S += [P('Etapa 2, e aqui está a sutileza: com a produção total menor, a receita marginal de '
            'equilíbrio <b>sobe</b>. Como a Fábrica 2 continua obedecendo CMg₂ = RMg, uma receita '
            'marginal maior exige quantidade maior nela. A Fábrica 2 compensa parcialmente a retração '
            'da Fábrica 1.')]
    S += formula([
        r'RMg = 700 - 10Q \;\text{ é decrescente} \;\Longrightarrow\; '
        r'Q \downarrow \;\Rightarrow\; RMg \uparrow',
        r'40Q_2 = RMg \uparrow \;\Longrightarrow\; Q_2 \uparrow',
    ])
    S += [P('Ilustração numérica com um choque que eleva o custo marginal da Fábrica 1 em 100 unidades '
            '(CMg₁ = 20Q₁ + 100):')]
    S.append(table([
        [P('Variável', 'Smallx'), P('Antes', 'Smallx'), P('Depois', 'Smallx'), P('Direção', 'Smallx')],
        [P('Q₁ (Fábrica 1)', 'Smallx'), P('20', 'Smallx'), P('≈ 16,43', 'Smallx'),
         P('<b>REDUZIR</b>', 'Smallx')],
        [P('Q₂ (Fábrica 2)', 'Smallx'), P('10', 'Smallx'), P('≈ 10,71', 'Smallx'),
         P('<b>AUMENTAR</b>', 'Smallx')],
        [P('Q total', 'Smallx'), P('30', 'Smallx'), P('≈ 27,14', 'Smallx'),
         P('<b>REDUZIR</b>', 'Smallx')],
        [P('Preço', 'Smallx'), P('550', 'Smallx'), P('≈ 564,29', 'Smallx'),
         P('<b>AUMENTAR</b>', 'Smallx')],
    ], [4.2 * cm, 3.3 * cm, 3.3 * cm, 5.9 * cm]))
    S += [resposta('<b>Q₁ reduz, Q₂ aumenta, produção total reduz e preço aumenta.</b> O erro comum é '
                   'dizer que Q₂ fica inalterado: ele muda porque a receita marginal de equilíbrio se '
                   'desloca.')]
    S += figure('08-q5b-choque-custo.png',
                'O deslocamento do custo marginal total para cima reduz Q e eleva P. Como a receita '
                'marginal é decrescente, o novo RMg de equilíbrio é mais alto e a Fábrica 2 responde '
                'produzindo mais.', 15.4 * cm)
    return S


def q6():
    S = [PageBreak(), P('Questão 6 — discriminação com elasticidades diferentes', 'H1x')]
    S += [note('Enunciado', 'Um monopolista vende em dois mercados, 1 e 2, com elasticidades ε₁ = −2 e '
               'ε₂ = −4. Suponha a possibilidade de discriminação. O monopolista cobra p₁ = 2,5p₂. '
               'Ele está maximizando? Mostre.', colors.white, BORDER)]
    S += [P('Nota sobre o enunciado: por trabalhar com dois grupos de consumidores e elasticidades '
            'distintas, o caso é de discriminação de <b>terceiro grau</b>, e é assim que os slides '
            'tratam este mesmo exemplo.', 'Smallx')]

    S += [P('A condição de maximização', 'H2x')]
    S += [P('Vender uma unidade a mais em qualquer mercado custa o mesmo CMg. Então, no ótimo, a receita '
            'marginal tem de ser igual nos dois mercados — caso contrário valeria a pena remanejar '
            'vendas do mercado de receita marginal menor para o de receita marginal maior.')]
    S += formula([
        r'RMg_1 = RMg_2 = CMg, \qquad RMg = P\left(1 - \frac{1}{|\epsilon|}\right)',
        r'RMg_1 = p_1\left(1 - \frac{1}{2}\right) = 0{,}50\,p_1',
        r'RMg_2 = p_2\left(1 - \frac{1}{4}\right) = 0{,}75\,p_2',
        r'0{,}50\,p_1 = 0{,}75\,p_2 \;\Longrightarrow\; '
        r'\frac{p_1}{p_2} = \frac{0{,}75}{0{,}50} = 1{,}5',
    ])
    S += [P('Testando a política da firma', 'H2x')]
    S += formula([
        r'\text{se } p_1 = 2{,}5\,p_2: \quad RMg_1 = 0{,}50(2{,}5\,p_2) = 1{,}25\,p_2',
        r'RMg_2 = 0{,}75\,p_2',
        r'1{,}25\,p_2 \;>\; 0{,}75\,p_2 \;\Longrightarrow\; RMg_1 > RMg_2',
    ])
    S += [P('Como a receita marginal no mercado 1 é maior que no mercado 2, deslocar vendas para o '
            'mercado 1 aumenta a receita total sem alterar o custo total. Portanto a política atual não '
            'é ótima.')]
    S += [resposta('<b>Não, ele não está maximizando.</b> A relação ótima é <b>p₁/p₂ = 1,5</b> e ele '
                   'pratica 2,5. O preço no mercado 1 está alto demais e no mercado 2 baixo demais. '
                   'O ajuste correto é <b>reduzir p₁</b> (vender mais no mercado 1) e/ou '
                   '<b>aumentar p₂</b>, até igualar as receitas marginais.')]
    S += [note('A regra intuitiva, e o sinal de que você entendeu',
               'O preço maior vai para o mercado <b>menos</b> elástico — aqui o mercado 1, com '
               '|ε₁| = 2. A direção da política da firma está certa (p₁ &gt; p₂); o erro é de '
               '<b>magnitude</b>: a diferença deveria ser de 50%, não de 150%.', GOLD)]
    S += figure('05-discriminacao-precos.png',
                'Painel da direita: demandas calibradas para |ε₁| = 2 e |ε₂| = 4 no ótimo, com CMg = 20. '
                'Os preços ótimos são 40 e 80/3 ≈ 26,7, cuja razão é exatamente 1,5.', 16.8 * cm)
    S += [note('Gabarito-resumo da Lista 1',
               '<b>Q1:</b> haverá troca; p₁/p₂ = 1; A = (3,3); B = (2,2); curva de contrato '
               'x₂ᴬ = x₁ᴬ. <b>Q2:</b> V, F, V, V. <b>Q3:</b> V, F, V, V; curva de contrato '
               'x₂ᴬ = x₁ᴬ − 5 e z = (−7,5; +7,5). <b>Q4:</b> Q = 3, P = 15, lucro zero. '
               '<b>Q5:</b> Q₁ = 20, Q₂ = 10, Q = 30, P = 550, lucro 10 500; com choque na Fábrica 1, '
               'Q₁ cai, Q₂ sobe, Q cai e P sobe. <b>Q6:</b> não maximiza; p₁/p₂ deveria ser 1,5.',
               LIGHT_GREEN, GREEN)]
    return S


def parte1():
    S = [P('Parte I — Lista 1 da disciplina, resolvida por completo', 'H1x')]
    S += [P('Os enunciados abaixo são os da <b>Lista 1</b> (CE-362, 2º semestre de 2026), resolvidos '
            'item por item.')]
    return S + q1() + q2() + q3() + q4() + q5() + q6()


# ===========================================================================
# PARTE II — BANCO DE EXERCÍCIOS NOVOS
# ===========================================================================
EX_A = [
    ('A1', 'Troca pura simétrica',
     'Dois agentes com U<sub>i</sub> = x₁x₂. Dotações w<sub>A</sub> = (6,2) e w<sub>B</sub> = (2,6). '
     '(a) Calcule as TMS na dotação e diga se haverá troca. (b) Encontre p₁/p₂. (c) Encontre as cestas '
     'de equilíbrio e as demandas líquidas. (d) Escreva a curva de contrato.'),
    ('A2', 'Dotações em cantos opostos',
     'U<sub>A</sub> = x₁<super>1/2</super>x₂<super>1/2</super> com w<sub>A</sub> = (10,0); '
     'U<sub>B</sub> = x₁<super>1/4</super>x₂<super>3/4</super> com w<sub>B</sub> = (0,10). '
     '(a) Escreva a renda de cada agente. (b) Normalize p₁ = 1 e encontre p₂. (c) Encontre as cestas de '
     'equilíbrio e verifique a factibilidade. (d) Explique economicamente por que p₂ &gt; p₁.'),
    ('A3', 'Preferências quase-lineares',
     'Os dois agentes têm U = ln(x₁) + x₂. Dotações w<sub>A</sub> = (2,1) e w<sub>B</sub> = (3,4). '
     '(a) Derive a demanda por x₁ e mostre que não depende da renda. (b) Normalize p₂ = 1 e encontre p₁. '
     '(c) Encontre as cestas de equilíbrio. (d) Qual o formato da curva de contrato? Por quê?'),
    ('A4', 'Substitutos perfeitos contra complementares perfeitos',
     'O Consumidor I tem u(x,y) = x + 2y e dotação (0,12). O Consumidor II tem u(x,y) = min{x, 2y} e '
     'dotação (12,0). (a) Por que o preço relativo de equilíbrio é determinado pelas preferências do '
     'Consumidor I? (b) Encontre p<sub>y</sub>/p<sub>x</sub>. (c) Encontre as duas cestas de equilíbrio.'),
    ('A5', 'A dotação já é eficiente?',
     'U<sub>A</sub> = x₁<super>2/3</super>x₂<super>1/3</super> com w<sub>A</sub> = (6,3); '
     'U<sub>B</sub> = x₁<super>1/3</super>x₂<super>2/3</super> com w<sub>B</sub> = (3,6). '
     '(a) Calcule as TMS na dotação inicial. (b) Encontre p₁/p₂ e as cestas de equilíbrio. '
     '(c) Calcule as demandas líquidas e interprete.'),
]

EX_B = [
    ('B1', 'Monopólio com custo marginal constante e bem-estar completo',
     'Demanda P = 120 − 2Q e custo total CT = 20Q + 100. (a) Encontre Q<sub>m</sub>, P<sub>m</sub> e o '
     'lucro. (b) Encontre a quantidade e o preço competitivos. (c) Calcule EC, EP e ET no monopólio e na '
     'concorrência. (d) Calcule a perda de peso morto. (e) Calcule a elasticidade no ótimo e verifique a '
     'fórmula do markup.'),
    ('B2', 'Demanda na forma direta',
     'A demanda é Q = 100 − 2P e o custo total é CT = 5Q. (a) Obtenha a demanda inversa. '
     '(b) Encontre Q<sub>m</sub>, P<sub>m</sub> e o lucro. (c) Calcule a elasticidade no ótimo e o '
     'markup.'),
    ('B3', 'Duas fábricas (variação da Q5 da lista)',
     'C₁ = 5Q₁², C₂ = 10Q₂² e demanda P = 400 − 2Q. (a) Encontre Q₁, Q₂, Q e P. (b) Calcule o lucro. '
     '(c) Escreva a curva de custo marginal total e verifique que ela cruza a receita marginal na '
     'quantidade encontrada.'),
    ('B4', 'Terceiro grau contra preço único',
     'Um monopolista com CMg constante igual a 20 atende dois mercados separáveis: Q₁ = 100 − P₁ e '
     'Q₂ = 120 − 2P₂. (a) Encontre preços e quantidades discriminando. (b) Calcule as elasticidades no '
     'ótimo e confirme a regra do preço maior no mercado menos elástico. (c) Calcule o lucro '
     'discriminando. (d) Calcule o lucro com preço único e compare.'),
    ('B5', 'Primeiro grau, monopólio uniforme e perda de peso morto',
     'Demanda P = 80 − Q e CMg = 2Q. (a) Encontre a quantidade eficiente e o excedente total sob '
     'discriminação perfeita. (b) Encontre Q<sub>m</sub> e P<sub>m</sub> no monopólio com preço único. '
     '(c) Calcule EC, EP e a perda de peso morto. (d) Compare o excedente total dos dois regimes e '
     'comente a diferença distributiva.'),
    ('B6', 'Markup direto pela elasticidade',
     'Um monopolista tem CMg constante igual a 30. (a) Se a elasticidade-preço no ótimo é −3, qual o '
     'preço e o markup? (b) E se fosse −1,5? (c) O que aconteceria se a elasticidade no ponto '
     'considerado fosse −0,8?'),
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
    ('C6', 'Se os dois agentes têm U = ln(x₁) + x₂, o conjunto das alocações Pareto-eficientes é uma '
     'reta vertical na caixa de Edgeworth.'),
    ('C7', 'O monopolista maximiza lucro no ponto em que P = CMg.'),
    ('C8', 'Um monopolista pode escolher um ponto na região inelástica da demanda se o seu custo '
     'marginal for suficientemente baixo.'),
    ('C9', 'Na discriminação de preços de primeiro grau não há perda de peso morto.'),
    ('C10', 'Na discriminação de terceiro grau, o preço deve ser maior no mercado com demanda mais '
     'elástica.'),
    ('C11', 'Toda a redução do excedente do consumidor provocada pelo monopólio é perda de peso morto.'),
    ('C12', 'Se as TMS de dois consumidores são diferentes, existe espaço para troca mutuamente '
     'benéfica.'),
]


def parte2():
    S = [PageBreak(), P('Parte II — Banco de 23 exercícios novos', 'H1x')]
    S += [P('Estes exercícios <b>não</b> estão na Lista 1: foram construídos no mesmo estilo e com a '
            'mesma notação, para treinar depois de dominar a lista. Resolva sem olhar a Parte III.')]
    S += [note('Como usar',
               '<b>Bloco A</b> (5 exercícios) — equilíbrio geral e caixa de Edgeworth. '
               '<b>Bloco B</b> (6 exercícios) — monopólio, bem-estar e discriminação. '
               '<b>Bloco C</b> (12 afirmativas) — conceitos. Tempo sugerido: 15 minutos por exercício '
               'numérico e 1 minuto por afirmativa.', LIGHT_BLUE, BLUE)]

    S += [P('Bloco A — Equilíbrio geral', 'H1x')]
    for code, titulo, texto in EX_A:
        S += enunciado(f'{code} — {titulo}', texto)

    S += [P('Bloco B — Monopólio, bem-estar e discriminação', 'H1x')]
    for code, titulo, texto in EX_B:
        S += enunciado(f'{code} — {titulo}', texto)

    S += [P('Bloco C — Verdadeiro ou falso (justifique)', 'H1x')]
    rows = [[P('Nº', 'Smallx'), P('Afirmativa', 'Smallx'), P('V ou F', 'Smallx')]]
    for code, texto in EX_C:
        rows.append([P(f'<b>{code}</b>', 'Smallx'), P(texto, 'Smallx'), P('________', 'Smallx')])
    S.append(table(rows, [1.2 * cm, 13.3 * cm, 2.2 * cm]))
    return S


# ===========================================================================
# PARTE III — GABARITOS DO BANCO NOVO
# ===========================================================================
def gabaritos_a():
    S = [PageBreak(), P('Parte III — Gabaritos comentados do banco novo', 'H1x')]

    S += [P('A1 — Troca pura simétrica', 'H2x')]
    S += formula([
        r'TMS_A(6,2) = \frac{2}{6} = \frac{1}{3} \qquad TMS_B(2,6) = \frac{6}{2} = 3',
    ])
    S += [P('(a) As TMS são diferentes, então há troca: A valoriza relativamente o bem 2 e B o bem 1.',
            'Answer')]
    S += formula([
        r'm_A = 6p_1 + 2p_2 \qquad m_B = 2p_1 + 6p_2',
        r'\frac{6p_1+2p_2}{2p_1} + \frac{2p_1+6p_2}{2p_1} = 8 '
        r'\;\Longrightarrow\; \frac{8p_1 + 8p_2}{2p_1} = 8 \;\Longrightarrow\; p_1 = p_2',
        r'p_1 = p_2 = 1: \quad m_A = 8,\; m_B = 8 \;\Longrightarrow\; x^A = (4,4),\;\; x^B = (4,4)',
        r'e^A = (-2, +2) \qquad e^B = (+2, -2) \qquad \text{curva de contrato: } x_2^A = x_1^A',
    ])
    S += [note('Resposta', '<b>p₁/p₂ = 1; A = (4,4); B = (4,4).</b> Simetria perfeita: cada um troca '
               '2 unidades, e a utilidade de ambos sobe de 12 para 16.', LIGHT_GREEN, GREEN)]

    S += [P('A2 — Dotações em cantos opostos', 'H2x')]
    S += formula([
        r'm_A = 10p_1 + 0p_2 = 10p_1 \qquad m_B = 0p_1 + 10p_2 = 10p_2',
        r'x_1^A = \frac{1}{2}\cdot\frac{10p_1}{p_1} = 5 \qquad '
        r'x_1^B = \frac{1}{4}\cdot\frac{10p_2}{p_1} = \frac{2{,}5\,p_2}{p_1}',
        r'5 + \frac{2{,}5\,p_2}{p_1} = 10 \;\Longrightarrow\; \frac{p_2}{p_1} = 2',
        r'p_1 = 1,\; p_2 = 2: \quad m_A = 10,\; m_B = 20',
        r'x^A = (5;\; 2{,}5) \qquad x^B = (5;\; 7{,}5)',
        r'\text{factibilidade: } 5 + 5 = 10 \;\checkmark \qquad 2{,}5 + 7{,}5 = 10 \;\checkmark',
    ])
    S += [P('(d) O bem 2 é mais caro porque a demanda relativa por ele é maior: B, que detém todo o '
            'estoque do bem 2, gasta 75% da renda nele, enquanto A gasta apenas 50%. Procura relativa '
            'maior eleva o preço relativo de equilíbrio.', 'Answer')]
    S += [note('Resposta', '<b>p₁/p₂ = 1/2 (ou p₂/p₁ = 2); A = (5; 2,5); B = (5; 7,5).</b>',
               LIGHT_GREEN, GREEN)]

    S += [P('A3 — Preferências quase-lineares', 'H2x')]
    S += formula([
        r'U = \ln x_1 + x_2 \;\Longrightarrow\; UMg_1 = \frac{1}{x_1}, \quad UMg_2 = 1',
        r'TMS = \frac{1/x_1}{1} = \frac{p_1}{p_2} \;\Longrightarrow\; x_1^* = \frac{p_2}{p_1}',
        r'x_2^* = \frac{m - p_1 x_1^*}{p_2} = \frac{m}{p_2} - 1',
    ])
    S += [P('(a) A demanda pelo bem 1 depende <b>apenas dos preços</b>: toda variação de renda vai para '
            'o bem 2. Essa é a marca da quase-linearidade, e a razão de a curva de contrato ser '
            'vertical.', 'Answer')]
    S += formula([
        r'\text{os dois demandam o mesmo } x_1 = \frac{p_2}{p_1}, \;\; '
        r'\text{dotação total de } x_1 = 5',
        r'2\cdot\frac{p_2}{p_1} = 5 \;\Longrightarrow\; \frac{p_2}{p_1} = 2{,}5 '
        r'\;\Longrightarrow\; \frac{p_1}{p_2} = \frac{2}{5}',
        r'p_2 = 1,\; p_1 = 0{,}4: \quad x_1^A = x_1^B = 2{,}5',
        r'm_A = 0{,}4(2) + 1(1) = 1{,}8 \;\Longrightarrow\; x_2^A = 1{,}8 - 1 = 0{,}8',
        r'm_B = 0{,}4(3) + 1(4) = 5{,}2 \;\Longrightarrow\; x_2^B = 5{,}2 - 1 = 4{,}2',
        r'\text{factibilidade do bem 2: } 0{,}8 + 4{,}2 = 5 \;\checkmark',
    ])
    S += [P('(d) A eficiência exige TMS<sub>A</sub> = TMS<sub>B</sub>, ou seja 1/x₁<super>A</super> = '
            '1/x₁<super>B</super>, logo x₁<super>A</super> = x₁<super>B</super> = 2,5. A quantidade do '
            'bem 1 é fixa em todas as alocações eficientes e só a partilha do bem 2 varia: a curva de '
            'contrato é uma <b>reta vertical</b>.', 'Answer')]
    S += [note('Resposta', '<b>p₁/p₂ = 2/5; A = (2,5; 0,8); B = (2,5; 4,2).</b> Curva de contrato '
               'vertical em x₁<super>A</super> = 2,5.', LIGHT_GREEN, GREEN)]
    S += figure('11-a3-quaselinear.png',
                'Com utilidade quase-linear a curva de contrato é vertical: a divisão eficiente do bem 1 '
                'é única e só a partilha do bem 2 muda ao longo da curva.', 14.6 * cm)

    S += [P('A4 — Substitutos perfeitos contra complementares perfeitos', 'H2x')]
    S += [P('(a) O Consumidor I tem curvas de indiferença <b>retas</b>, com TMS constante igual a 1/2. '
            'Se o preço relativo diferisse de 1/2 ele iria para um canto e o mercado não fecharia. '
            'O Consumidor II tem proporção fixa: sua escolha relativa é a mesma para qualquer preço, '
            'então não ancora nada. Logo o preço relativo é ditado pela TMS de I.', 'Answer')]
    S += formula([
        r'u = x + 2y \;\Longrightarrow\; UMg_x = 1,\; UMg_y = 2 \;\Longrightarrow\; TMS = \frac{1}{2}',
        r'\frac{p_x}{p_y} = \frac{1}{2} \;\Longrightarrow\; \frac{p_y}{p_x} = 2',
        r'\text{Consumidor II: } x = 2y, \quad m_{II} = 12p_x, \quad p_x = 1,\; p_y = 2',
        r'1(2y) + 2(y) = 12 \;\Longrightarrow\; 4y = 12 \;\Longrightarrow\; y = 3,\;\; x = 6',
        r'\text{Consumidor I fica com o resto: } x_I = 12 - 6 = 6, \quad y_I = 12 - 3 = 9',
        r'\text{confere o orçamento de I: } m_I = 2(12) = 24 = 1(6) + 2(9) \;\checkmark',
    ])
    S += [note('Resposta', '<b>p<sub>y</sub>/p<sub>x</sub> = 2; Consumidor I = (6, 9); '
               'Consumidor II = (6, 3).</b>', LIGHT_GREEN, GREEN)]

    S += [P('A5 — A dotação já é eficiente?', 'H2x')]
    S += formula([
        r'TMS_A = \frac{(2/3)x_2}{(1/3)x_1} = \frac{2x_2}{x_1} \qquad '
        r'TMS_B = \frac{(1/3)x_2}{(2/3)x_1} = \frac{x_2}{2x_1}',
        r'TMS_A(6,3) = \frac{2(3)}{6} = 1 \qquad TMS_B(3,6) = \frac{6}{2(3)} = 1',
    ])
    S += [P('(a) As TMS <b>já são iguais</b> na dotação inicial, o que indica que a alocação de partida '
            'está sobre a curva de contrato.', 'Answer')]
    S += formula([
        r'\frac{(2/3)(6p_1+3p_2)}{p_1} + \frac{(1/3)(3p_1+6p_2)}{p_1} = 9',
        r'(4p_1 + 2p_2) + (p_1 + 2p_2) = 9p_1 \;\Longrightarrow\; 5p_1 + 4p_2 = 9p_1 '
        r'\;\Longrightarrow\; p_1 = p_2',
        r'p_1 = p_2 = 1: \quad x^A = (6,3) = w^A \qquad x^B = (3,6) = w^B',
        r'e^A = (0,0) \qquad e^B = (0,0)',
    ])
    S += [P('(c) Cada agente demanda exatamente a sua dotação. A economia já estava em equilíbrio: os '
            'preços apenas <b>validam</b> a alocação inicial, sem provocar transação alguma.', 'Answer')]
    S += [note('Resposta', '<b>Não há troca: p₁/p₂ = 1 e cada agente permanece com a própria dotação.</b> '
               'A lição é que uma dotação inicial pode já ser Pareto-eficiente, e nesse caso o '
               'equilíbrio walrasiano coincide com ela.', LIGHT_GREEN, GREEN)]
    return S


def gabaritos_b():
    S = [PageBreak(), P('B1 — Monopólio com custo marginal constante e bem-estar', 'H2x')]
    S += formula([
        r'R = (120 - 2Q)Q \;\Longrightarrow\; RMg = 120 - 4Q \qquad CMg = 20',
        r'120 - 4Q = 20 \;\Longrightarrow\; Q_m = 25 \qquad P_m = 120 - 2(25) = 70',
        r'\pi = 70(25) - \left[20(25) + 100\right] = 1\,750 - 600 = 1\,150',
        r'\text{competitivo: } 120 - 2Q = 20 \;\Longrightarrow\; Q_c = 50,\;\; P_c = 20',
    ])
    S += formula([
        r'EC_m = \frac{1}{2}(25)(120 - 70) = 625 \qquad EP_m = (70 - 20)(25) = 1\,250',
        r'EC_c = \frac{1}{2}(50)(120 - 20) = 2\,500 \qquad EP_c = 0',
        r'PPM = 2\,500 - (625 + 1\,250) = 625',
        r'\text{conferindo: } \frac{1}{2}(50 - 25)(70 - 20) = 625 \;\checkmark',
    ])
    S += [P('Com custo marginal constante o excedente do produtor é um retângulo simples, e na '
            'concorrência ele é zero: todo o excedente fica com o consumidor.', 'Answer')]
    S += formula([
        r'\epsilon = \frac{dQ}{dP}\cdot\frac{P}{Q} = \left(-\frac{1}{2}\right)\frac{70}{25} = -1{,}4',
        r'\frac{P}{CMg} = \frac{70}{20} = 3{,}5 \qquad '
        r'\frac{1}{1 - 1/1{,}4} = \frac{1}{0{,}2857} = 3{,}5 \;\checkmark',
    ])
    S += [note('Resposta', '<b>Q<sub>m</sub> = 25, P<sub>m</sub> = 70, lucro 1 150; Q<sub>c</sub> = 50, '
               'P<sub>c</sub> = 20; PPM = 625; |ε| = 1,4; markup 3,5.</b>', LIGHT_GREEN, GREEN)]
    S += figure('12-b1-bem-estar.png',
                'Com custo marginal constante, o excedente do produtor no monopólio é um retângulo e a '
                'perda de peso morto é o triângulo entre Q<sub>m</sub> e Q<sub>c</sub>.', 15.4 * cm)

    S += [P('B2 — Demanda na forma direta', 'H2x')]
    S += formula([
        r'Q = 100 - 2P \;\Longrightarrow\; 2P = 100 - Q \;\Longrightarrow\; P = 50 - \frac{Q}{2}',
    ])
    S += [P('Este é o passo que mais gera erro: é preciso <b>inverter</b> a demanda antes de derivar a '
            'receita marginal.', 'Answer')]
    S += formula([
        r'R = \left(50 - \frac{Q}{2}\right)Q = 50Q - \frac{Q^2}{2} '
        r'\;\Longrightarrow\; RMg = 50 - Q',
        r'50 - Q = 5 \;\Longrightarrow\; Q_m = 45 \qquad P_m = 50 - 22{,}5 = 27{,}5',
        r'\pi = 27{,}5(45) - 5(45) = 1\,237{,}5 - 225 = 1\,012{,}5',
        r'\epsilon = (-2)\frac{27{,}5}{45} \approx -1{,}22 \qquad '
        r'\frac{P}{CMg} = \frac{27{,}5}{5} = 5{,}5',
    ])
    S += [note('Resposta', '<b>Q<sub>m</sub> = 45, P<sub>m</sub> = 27,5, lucro 1 012,5, |ε| ≈ 1,22, '
               'markup 5,5.</b> Demanda pouco elástica no ótimo produz markup alto.', LIGHT_GREEN, GREEN)]

    S += [P('B3 — Duas fábricas', 'H2x')]
    S += formula([
        r'CMg_1 = 10Q_1 \qquad CMg_2 = 20Q_2 \qquad RMg = 400 - 4Q',
        r'10Q_1 = 20Q_2 \;\Longrightarrow\; Q_1 = 2Q_2 \;\Longrightarrow\; Q = 3Q_2',
        r'400 - 12Q_2 = 20Q_2 \;\Longrightarrow\; Q_2 = 12{,}5 \qquad Q_1 = 25 '
        r'\qquad Q = 37{,}5',
        r'P = 400 - 2(37{,}5) = 325',
        r'\text{conferência: } CMg_1 = 250,\;\; CMg_2 = 250,\;\; RMg = 400 - 150 = 250 \;\checkmark',
        r'\pi = 325(37{,}5) - 5(25)^2 - 10(12{,}5)^2 = 12\,187{,}5 - 3\,125 - 1\,562{,}5 = 7\,500',
    ])
    S += formula([
        r'Q = \frac{CMg}{10} + \frac{CMg}{20} = \frac{3\,CMg}{20} '
        r'\;\Longrightarrow\; CMg_{total} = \frac{20}{3}Q',
        r'\frac{20}{3}(37{,}5) = 250 \;\checkmark',
    ])
    S += [note('Resposta', '<b>Q₁ = 25, Q₂ = 12,5, Q = 37,5, P = 325, lucro 7 500.</b>',
               LIGHT_GREEN, GREEN)]

    S += [P('B4 — Terceiro grau contra preço único', 'H2x')]
    S += formula([
        r'\text{mercado 1: } P_1 = 100 - Q_1 \;\Longrightarrow\; RMg_1 = 100 - 2Q_1 = 20 '
        r'\;\Longrightarrow\; Q_1 = 40,\; P_1 = 60',
        r'\text{mercado 2: } P_2 = 60 - \frac{Q_2}{2} \;\Longrightarrow\; RMg_2 = 60 - Q_2 = 20 '
        r'\;\Longrightarrow\; Q_2 = 40,\; P_2 = 40',
        r'\epsilon_1 = (-1)\frac{60}{40} = -1{,}5 \qquad \epsilon_2 = (-2)\frac{40}{40} = -2',
        r'P_1\left(1 - \frac{1}{1{,}5}\right) = 60\cdot\frac{1}{3} = 20 = CMg \;\checkmark',
        r'P_2\left(1 - \frac{1}{2}\right) = 40\cdot\frac{1}{2} = 20 = CMg \;\checkmark',
    ])
    S += [P('O mercado 1 é o menos elástico e recebe o preço mais alto (60 contra 40), exatamente como '
            'a regra prevê.', 'Answer')]
    S += formula([
        r'\pi_{disc} = (60-20)(40) + (40-20)(40) = 1\,600 + 800 = 2\,400',
        r'\text{preço único: } Q = (100 - P) + (120 - 2P) = 220 - 3P '
        r'\;\Longrightarrow\; P = \frac{220 - Q}{3}',
        r'RMg = \frac{220 - 2Q}{3} = 20 \;\Longrightarrow\; Q = 80, \quad '
        r'P = \frac{140}{3} \approx 46{,}67',
        r'\pi_{único} = \left(\frac{140}{3} - 20\right)(80) = \frac{6\,400}{3} \approx 2\,133{,}33',
    ])
    S += [note('Resposta', '<b>Discriminando: P₁ = 60, P₂ = 40, lucro 2 400. Com preço único: '
               'P ≈ 46,67, lucro ≈ 2 133,33.</b> Discriminar rende cerca de 12,5% mais lucro — é isso '
               'que explica a prática, quando a revenda pode ser bloqueada.', LIGHT_GREEN, GREEN)]

    S += [P('B5 — Primeiro grau, monopólio uniforme e perda de peso morto', 'H2x')]
    S += formula([
        r'\text{quantidade eficiente: } 80 - Q = 2Q \;\Longrightarrow\; Q = \frac{80}{3} '
        r'\approx 26{,}67',
        r'ET_{1º grau} = \int_0^{80/3}\left[(80 - Q) - 2Q\right]dQ = \int_0^{80/3}(80 - 3Q)\,dQ',
        r'= \left[80Q - \frac{3Q^2}{2}\right]_0^{80/3} = \frac{3\,200}{3} \approx 1\,066{,}67',
    ])
    S += [P('Sob discriminação perfeita esse valor inteiro vira excedente do produtor, e o excedente do '
            'consumidor é zero.', 'Answer')]
    S += formula([
        r'RMg = 80 - 2Q = 2Q \;\Longrightarrow\; Q_m = 20 \qquad P_m = 80 - 20 = 60',
        r'EC = \frac{1}{2}(20)(80 - 60) = 200',
        r'EP = \int_0^{20}(60 - 2Q)\,dQ = 60(20) - 20^2 = 800',
        r'ET_m = 1\,000 \qquad PPM = \frac{3\,200}{3} - 1\,000 = \frac{200}{3} \approx 66{,}67',
        r'\text{conferindo: } \int_{20}^{80/3}\left[(80 - Q) - 2Q\right]dQ = \frac{200}{3} \;\checkmark',
    ])
    S += [P('(d) O excedente total é maior sob discriminação perfeita (1 066,67 contra 1 000), porque a '
            'quantidade é a eficiente. Mas a distribuição é radicalmente diferente: no primeiro grau o '
            'consumidor fica com zero, enquanto no preço único ele retém 200. Eficiência e distribuição '
            'são dimensões distintas.', 'Answer')]
    S += [note('Resposta', '<b>1º grau: Q = 80/3, ET ≈ 1 066,67 todo para a firma. Preço único: Q = 20, '
               'P = 60, EC = 200, EP = 800, PPM ≈ 66,67.</b>', LIGHT_GREEN, GREEN)]

    S += [P('B6 — Markup direto pela elasticidade', 'H2x')]
    S += formula([
        r'P\left(1 - \frac{1}{|\epsilon|}\right) = CMg \;\Longrightarrow\; '
        r'P = \frac{CMg}{1 - 1/|\epsilon|}',
        r'|\epsilon| = 3: \quad P\left(1 - \frac{1}{3}\right) = 30 \;\Longrightarrow\; '
        r'P = 45, \quad \text{markup} = 1{,}5',
        r'|\epsilon| = 1{,}5: \quad P\left(1 - \frac{1}{1{,}5}\right) = 30 \;\Longrightarrow\; '
        r'P = 90, \quad \text{markup} = 3',
        r'|\epsilon| = 0{,}8: \quad 1 - \frac{1}{0{,}8} = -0{,}25 \;\Longrightarrow\; P < 0 \;(!)',
    ])
    S += [P('(c) O preço negativo é um absurdo, e o que isso revela é que <b>o ponto não pode ser um '
            'ótimo</b>: na região inelástica a receita marginal é negativa, então reduzir a quantidade '
            'aumentaria a receita e diminuiria o custo ao mesmo tempo. Um monopolista nunca opera ali.',
            'Answer')]
    S += [note('Resposta', '<b>(a) P = 45, markup 1,5. (b) P = 90, markup 3. (c) Impossível: |ε| &lt; 1 '
               'não pode ocorrer no ótimo.</b> Quanto menos elástica a demanda, maior o markup.',
               LIGHT_GREEN, GREEN)]
    return S


GABARITO_C = [
    ('C1', 'FALSA', 'A Lei de Walras garante o contrário: se n − 1 mercados estão em equilíbrio, o '
                    'n-ésimo também estará. O valor do excesso de demanda agregado é zero para qualquer '
                    'vetor de preços.'),
    ('C2', 'FALSA', 'O teorema garante <b>eficiência de Pareto</b> e nada diz sobre distribuição. '
                    'Uma alocação em que um agente tem tudo pode ser eficiente.'),
    ('C3', 'VERDADEIRA', 'Estar na curva de contrato significa que não existe realocação capaz de '
                         'melhorar um sem piorar o outro, logo não há troca voluntária a fazer.'),
    ('C4', 'FALSA', 'Os cantos da caixa são eficientes: se um agente tem tudo, melhorar o outro exige '
                    'necessariamente piorar o primeiro.'),
    ('C5', 'FALSA', 'Apenas os preços relativos são determinados, porque escalar todos os preços não '
                    'muda escolha alguma. É por isso que se normaliza um numerário.'),
    ('C6', 'VERDADEIRA', 'Com U = ln x₁ + x₂ a eficiência exige 1/x₁ᴬ = 1/x₁ᴮ, ou seja x₁ᴬ fixo. '
                         'A curva de contrato é vertical (ver exercício A3).'),
    ('C7', 'FALSA', 'P = CMg é a condição da concorrência perfeita. O monopolista usa RMg = CMg e depois '
                    'lê o preço na curva de demanda, o que em geral resulta em preço acima do custo '
                    'marginal.'),
    ('C8', 'FALSA', 'Na região inelástica a receita marginal é negativa. Reduzir a quantidade aumentaria '
                    'a receita e reduziria o custo ao mesmo tempo, então nenhum ponto ali pode ser '
                    'ótimo, qualquer que seja o custo marginal.'),
    ('C9', 'VERDADEIRA', 'A firma expande a produção enquanto a disposição a pagar exceder o custo '
                         'marginal, atingindo a quantidade eficiente. Todo o excedente, porém, é '
                         'capturado por ela.'),
    ('C10', 'FALSA', 'É o inverso: preço mais alto no mercado <b>menos</b> elástico. A condição '
                     'RMg₁ = RMg₂ = CMg implica que quem tem demanda mais rígida paga mais.'),
    ('C11', 'FALSA', 'Parte da queda do excedente do consumidor é <b>transferência</b> para o produtor. '
                     'A perda de peso morto é apenas a parcela que não vira excedente de ninguém.'),
    ('C12', 'VERDADEIRA', 'TMS diferentes significam avaliações relativas diferentes, o que abre espaço '
                          'para troca que melhore ambos. A troca cessa quando as TMS se igualam ou em '
                          'soluções de canto ou vértice.'),
]


def gabaritos_c():
    S = [PageBreak(), P('Bloco C — Gabarito das afirmativas', 'H1x')]
    rows = [[P('Nº', 'Smallx'), P('Resposta', 'Smallx'), P('Por quê', 'Smallx')]]
    for code, veredito, porque in GABARITO_C:
        rows.append([P(f'<b>{code}</b>', 'Smallx'), P(f'<b>{veredito}</b>', 'Smallx'),
                     P(porque, 'Smallx')])
    S.append(table(rows, [1.2 * cm, 2.6 * cm, 12.9 * cm]))
    S += [Spacer(1, .3 * cm),
          note('Placar de referência',
               'Oito ou mais acertos indicam boa base conceitual. Os erros mais frequentes são em '
               '<b>C8</b> (região inelástica), <b>C10</b> (direção da regra de elasticidade) e '
               '<b>C11</b> (transferência contra peso morto) — releia essas três justificativas com '
               'atenção.', GOLD)]
    S += [Spacer(1, .3 * cm),
          P('<b>Nota de conferência:</b> todos os valores numéricos deste PDF — as seis questões da '
            'Lista 1 e os onze exercícios numéricos do banco novo — são recalculados automaticamente '
            'por <i>verificar_contas.py</i>, com 114 checagens simbólicas em SymPy. Se algum número '
            'fosse alterado por engano, o script falharia.', 'Smallx')]
    return S


def main():
    badge = note('O que há neste arquivo',
                 'Parte I — as seis questões da Lista 1 resolvidas passo a passo, com todos os itens. '
                 'Parte II — 23 exercícios novos (11 numéricos e 12 afirmativas), apenas com '
                 'enunciados. Parte III — gabaritos comentados dos exercícios novos.',
                 LIGHT_PURPLE, PURPLE)
    story = cover('LISTA 1 RESOLVIDA', 'e banco de exercícios novos para treinar',
                  ['<b>Disciplina:</b> CE-362 / CE-362D — Microeconomia II',
                   '<b>Universidade:</b> Instituto de Economia — Unicamp',
                   '',
                   'Equilíbrio geral • Caixa de Edgeworth • Monopólio',
                   'Bem-estar • Discriminação de preços'],
                  badge)
    story += parte1() + parte2() + gabaritos_a() + gabaritos_b() + gabaritos_c()
    caminho = build_pdf(OUT, story,
                        title='Lista 1 resolvida e exercícios extra — Microeconomia II',
                        left_title='LISTA 1 RESOLVIDA + EXERCÍCIOS NOVOS',
                        right_title='Microeconomia II | Unicamp',
                        footer_note='Confira sempre a notação usada em aula')
    print(caminho)
    print(os.path.getsize(caminho), 'bytes')


if __name__ == '__main__':
    main()
