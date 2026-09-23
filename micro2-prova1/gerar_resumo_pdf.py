"""
Gera 'resumo-micro2-prova1.pdf' — resumo da Prova 1 de Microeconomia II (CE-362D / Unicamp).
Fontes: Revisao_EGeMONO.pdf, lista1.pdf, excedente.pdf e o programa da disciplina.
Toda a matemática de exibição é LaTeX renderizado (ver estilo_pdf.formula).
Uso: python3 gerar_resumo_pdf.py
"""
import os

from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Spacer

from estilo_pdf import (
    BLUE, BORDER, GOLD, GREEN, LIGHT_BLUE, LIGHT_GREEN, LIGHT_RED, RED,
    P, bullets, build_pdf, caption, cover, formula, img, note, table,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.join(ROOT, 'graficos')
OUT = os.path.join(ROOT, 'resumo-micro2-prova1.pdf')


def figure(name, text, width=16.6 * cm):
    return [img(GRAPH, name, width), caption(text)]


def secao_escopo():
    S = [P('1. Escopo provável da P1 e mapa do material', 'H1x')]
    S += [P('O programa de Microeconomia II enumera quatro blocos: Equilíbrio Geral; Estruturas de '
            'Mercado e Estratégia Competitiva; Teoria dos Jogos; e Incerteza. Entretanto, a aula de '
            'revisão fornecida é explicitamente “Equilíbrio Geral e Monopólio”, e a Lista 1 cobra '
            'equilíbrio geral, monopólio, custos multiplanta e discriminação de preços. Este resumo '
            'prioriza esse recorte, sem afirmar que os demais blocos estejam fora da disciplina inteira.')]
    S.append(table([
        [P('Fonte', 'Smallx'), P('Conteúdo identificado', 'Smallx'), P('Uso neste resumo', 'Smallx')],
        [P('<b>Revisao_EGeMONO.pdf</b>', 'Smallx'),
         P('Leiloeiro walrasiano; equilíbrio parcial e geral; Pareto; caixa de Edgeworth; álgebra do '
           'equilíbrio; Lei de Walras; monopólio; elasticidade; markup; bem-estar; discriminação de '
           '1º a 3º graus.', 'Smallx'),
         P('Fonte principal da teoria e dos exemplos numéricos.', 'Smallx')],
        [P('<b>lista1.pdf</b>', 'Smallx'),
         P('Troca pura, demandas Cobb–Douglas e Leontief, curva de contrato, monopólio, duas fábricas '
           'e discriminação de preços.', 'Smallx'),
         P('Modelo de exercícios e notação da prova.', 'Smallx')],
        [P('<b>excedente.pdf</b>', 'Smallx'),
         P('Comparação concorrência × monopólio com P = 100 − 2Q e CMg = 10 + 3Q; EC, EP, ET e PPM.', 'Smallx'),
         P('Cálculos de bem-estar e gráfico de áreas.', 'Smallx')],
        [P('<b>Programa da disciplina</b>', 'Smallx'),
         P('Objetivos, ementa, organização do conteúdo e datas das provas.', 'Smallx'),
         P('Contextualização; não especifica isoladamente o conteúdo da P1.', 'Smallx')],
    ], [3.2 * cm, 8.6 * cm, 4.9 * cm]))
    S += [Spacer(1, .25 * cm),
          note('Atenção sobre o recorte',
               'O programa geral menciona concorrência perfeita, concorrência monopolística, oligopólios '
               'e teoria dos jogos. Eles aparecem na ementa anual, mas não são desenvolvidos no material '
               'de revisão anexado, e por isso não são tratados aqui como conteúdo confirmado da P1.',
               LIGHT_BLUE, BLUE)]
    return S


def secao_equilibrio_geral():
    S = [PageBreak(), P('2. Equilíbrio geral em uma economia de trocas', 'H1x')]
    S += [P('Equilíbrio parcial estuda um mercado isoladamente, mantendo os demais constantes. '
            'Equilíbrio geral reconhece que preços e quantidades de todos os mercados são determinados '
            'simultaneamente: uma mudança em um mercado altera a renda, a demanda e os preços relativos '
            'nos outros.')]

    S += [P('2.1 Estrutura do modelo de trocas', 'H2x')]
    S += bullets([
        'Dois ou mais consumidores, dois ou mais bens e dotações iniciais.',
        'Cada consumidor escolhe a cesta que maximiza sua utilidade dentro da restrição orçamentária.',
        'A oferta total de cada bem é a soma das dotações iniciais: não há produção.',
        'Um equilíbrio walrasiano é um vetor de preços e uma alocação em que todos otimizam e todos os '
        'mercados se equilibram.',
    ])

    S += [P('2.2 O leiloeiro walrasiano e o tâtonnement', 'H2x')]
    S += [P('O leiloeiro anuncia um vetor de preços; os agentes informam demandas e ofertas; o leiloeiro '
            'calcula a demanda excedente agregada de cada bem e ajusta os preços. As transações só '
            'ocorrem no equilíbrio.')]
    S.extend(formula([
        r'z_i(p) \;=\; \sum \mathrm{Demanda}_i(p) \;-\; \sum \mathrm{Oferta}_i(p)',
        r'z_i(p) > 0 \;\text{(excesso de demanda)} \;\Longrightarrow\; \text{o leiloeiro aumenta } p_i',
        r'z_i(p) < 0 \;\text{(excesso de oferta)} \;\Longrightarrow\; \text{o leiloeiro reduz } p_i',
        r'\text{o processo para quando } z_i(p^*) = 0 \;\text{ para todo bem } i',
    ]))

    S += [P('2.3 Factibilidade, renda e demanda líquida', 'H2x')]
    S += [P('Este é o ponto que mais gera erro na prova: na economia de trocas a renda <b>não</b> é um '
            'número dado, e sim o valor da dotação aos preços vigentes.')]
    S.extend(formula([
        r'\text{Renda:}\quad m_i \;=\; p_1 w_i^1 + p_2 w_i^2',
        r'\text{Factibilidade:}\quad \sum_i x_i^1 = \sum_i w_i^1 '
        r'\quad\text{e}\quad \sum_i x_i^2 = \sum_i w_i^2',
        r'\text{Demanda líquida:}\quad e_i^k \;=\; x_i^k - w_i^k',
        r'\text{Demanda excedente agregada:}\quad z^k(p) \;=\; \sum_i e_i^k(p) '
        r'\;=\; \sum_i x_i^k(p) - \sum_i w_i^k',
    ]))
    S += [P('Interpretação dos sinais: se e<sub>i</sub><super>k</super> &gt; 0 o agente é demandante '
            'líquido do bem k; se for negativo, ele oferece parte da própria dotação. No equilíbrio, a '
            'soma das demandas líquidas é zero em cada mercado.')]
    S += figure('06-lei-de-walras.png',
                'Demanda excedente e ajuste de preços no exemplo numérico dos slides. O preço absoluto é '
                'normalizado; o que importa é o preço relativo.')
    return S


def secao_edgeworth():
    S = [PageBreak(), P('3. Caixa de Edgeworth, eficiência e curva de contrato', 'H1x')]
    S += [P('A caixa de Edgeworth representa todas as alocações factíveis entre dois agentes e dois bens. '
            'A origem do agente A fica no canto inferior esquerdo e a origem do agente B no canto superior '
            'direito. Um ponto dentro da caixa informa a cesta de A e, por complementaridade, a de B.')]

    S += [P('3.1 Trocas mutuamente benéficas', 'H2x')]
    S += [P('A Taxa Marginal de Substituição mede quanto de um bem o consumidor aceita abrir mão para '
            'obter uma unidade adicional do outro, mantendo a utilidade constante. Em solução interior:')]
    S.extend(formula([
        r'TMS_i \;=\; \frac{UMg_1^i}{UMg_2^i} \;=\; \frac{p_1}{p_2}',
    ]))
    S += bullets([
        'Se as TMS dos dois agentes são <b>diferentes</b>, existe troca que melhora ambos.',
        'A troca se esgota quando as TMS se igualam — ou em soluções de canto ou de vértice.',
        'A dotação inicial é apenas o ponto de partida e não precisa ser eficiente.',
    ])

    S += [P('3.2 Curva de contrato e eficiência de Pareto', 'H2x')]
    S += [P('A curva de contrato reúne as alocações Pareto-eficientes: aquelas em que não é possível '
            'melhorar um agente sem piorar o outro. Para soluções interiores:')]
    S.extend(formula([r'TMS_A \;=\; TMS_B']))
    S += [P('Em uma economia com produção, a eficiência também exige que as TMS dos consumidores se '
            'igualem à taxa marginal de transformação, e que as taxas marginais de substituição técnica '
            'coincidam entre firmas. Isso não é necessário nos exercícios de troca pura da Lista 1.')]

    S += [P('3.3 Exemplo completo com Cobb–Douglas', 'H2x')]
    S += [P('Dados da Questão 1 da Lista 1: U<sub>i</sub> = x<sub>1</sub>x<sub>2</sub> para os dois '
            'agentes, w<sub>A</sub> = (4, 2) e w<sub>B</sub> = (1, 3), com dotação total de 5 unidades de '
            'cada bem.')]
    S.extend(formula([
        r'TMS_A(4,2) = \frac{2}{4} = \frac{1}{2} \qquad TMS_B(1,3) = \frac{3}{1} = 3'
        r'\quad\Longrightarrow\quad \text{há ganhos de troca}',
        r'x_1^{i\,*} = \frac{m_i}{2p_1} \qquad x_2^{i\,*} = \frac{m_i}{2p_2}',
        r'\frac{4p_1 + 2p_2}{2p_1} + \frac{p_1 + 3p_2}{2p_1} = 5 '
        r'\;\Longrightarrow\; \frac{5p_1 + 5p_2}{2p_1} = 5 \;\Longrightarrow\; p_1 = p_2',
        r'\text{com } p_1 = p_2 = 1:\quad x^A = (3,3) \qquad x^B = (2,2)',
    ]))
    S += figure('01-caixa-edgeworth.png',
                'Caixa 5 × 5. W é a dotação de A; E é o equilíbrio. A reta orçamentária tem inclinação '
                '−1 porque os preços são iguais. A lente amarela reúne as trocas que melhoram os dois e o '
                'núcleo é o trecho da curva de contrato dentro dela.')
    S += [note('Leitura econômica do gráfico',
               'A dotação W está dentro da lente de ganhos mútuos, então ambos podem melhorar trocando. '
               'O ponto E está sobre a curva de contrato (a diagonal x<sub>2</sub><super>A</super> = '
               'x<sub>1</sub><super>A</super>) e também dentro do núcleo compatível com a dotação inicial. '
               'A reta orçamentária reúne as cestas de mesmo valor aos preços de equilíbrio.',
               LIGHT_GREEN, GREEN)]
    return S


def secao_algebra_walras():
    S = [PageBreak(), P('4. Álgebra do equilíbrio e Lei de Walras', 'H1x')]
    S += [P('O procedimento algébrico é quase sempre o mesmo. Vale decorar o roteiro e treinar até ficar '
            'mecânico, porque isso libera tempo na prova para a interpretação.')]

    S += [P('4.1 Roteiro em cinco passos', 'H2x')]
    S.append(table([
        [P('Passo', 'Smallx'), P('O que fazer', 'Smallx')],
        [P('1', 'Smallx'), P('Escrever a renda de cada agente como valor da dotação: '
                             'm<sub>i</sub> = p₁w<sub>i</sub><super>1</super> + '
                             'p₂w<sub>i</sub><super>2</super>.', 'Smallx')],
        [P('2', 'Smallx'), P('Resolver a escolha ótima com TMS<sub>i</sub> = p₁/p₂ e substituir na '
                             'restrição orçamentária.', 'Smallx')],
        [P('3', 'Smallx'), P('Obter as demandas marshallianas e somá-las entre os agentes.', 'Smallx')],
        [P('4', 'Smallx'), P('Normalizar um preço (numerário) e impor o equilíbrio em um mercado.', 'Smallx')],
        [P('5', 'Smallx'), P('Conferir o outro mercado pela factibilidade e pela Lei de Walras.', 'Smallx')],
    ], [1.4 * cm, 15.3 * cm]))

    S += [P('4.2 Regra de bolso para Cobb–Douglas', 'H2x')]
    S.extend(formula([
        r'U(x_1,x_2) = x_1^{\alpha}\, x_2^{\beta} \;\Longrightarrow\; '
        r'x_1^* = \frac{\alpha}{\alpha+\beta}\cdot\frac{m}{p_1}'
        r'\qquad x_2^* = \frac{\beta}{\alpha+\beta}\cdot\frac{m}{p_2}',
    ]))
    S += [P('Cada agente gasta a fração α/(α+β) da renda no bem 1 e o restante no bem 2, '
            'independentemente dos preços. Essa regra resolve a maior parte dos itens da Lista 1.')]

    S += [P('4.3 Exemplo numérico dos slides', 'H2x')]
    S += [P('Dados: U<sub>A</sub> = x₁<super>A</super>(x₂<super>A</super>)², '
            'w<sub>A</sub> = (10, 10); U<sub>B</sub> = (x₁<super>B</super>)²x₂<super>B</super>, '
            'w<sub>B</sub> = (20, 20). Normalize p₁ = 1 e encontre p₂.')]
    S.extend(formula([
        r'TMS_A = \frac{x_2^A}{2x_1^A} = \frac{p_1}{p_2} = \frac{1}{p_2}'
        r'\;\Longrightarrow\; x_2^A = \frac{2x_1^A}{p_2}',
        r'm_A = 10 + 10p_2 \;\Longrightarrow\; x_1^A = \frac{10(1+p_2)}{3}'
        r'\qquad x_2^A = \frac{20(1+p_2)}{3p_2}',
        r'x_1^B = \frac{40(1+p_2)}{3} \qquad x_2^B = \frac{20(1+p_2)}{3p_2}',
        r'\frac{10(1+p_2)}{3} + \frac{40(1+p_2)}{3} = 30 \;\Longrightarrow\; '
        r'50(1+p_2) = 90 \;\Longrightarrow\; p_2 = 0{,}8',
    ]))
    S += [P('Com p₂ = 0,8: A consome (6, 15) e B consome (24, 15). A é ofertante líquido do bem 1 e '
            'demandante líquido do bem 2; B faz o oposto. A soma das demandas é (30, 30), igual à soma '
            'das dotações.')]
    S.extend(formula([
        r'e^A = (6-10,\; 15-10) = (-4,\; +5) \qquad e^B = (24-20,\; 15-20) = (+4,\; -5)',
        r'1\cdot(-4) + 0{,}8\cdot(+5) + 1\cdot(+4) + 0{,}8\cdot(-5) = 0',
    ]))

    S += [P('4.4 Lei de Walras', 'H2x')]
    S.extend(formula([
        r'\sum_k p_k\, z_k(p) \;=\; 0 \qquad \forall\, p',
    ]))
    S += [P('O valor da demanda excedente agregada é zero para <b>qualquer</b> vetor de preços, não só no '
            'equilíbrio. A consequência prática: se n − 1 mercados estão equilibrados, o n-ésimo também '
            'está, então em dois bens basta equilibrar um mercado. Além disso, apenas preços relativos são '
            'determinados — multiplicar todos os preços pela mesma constante não muda nada, e é por isso '
            'que se escolhe um numerário.')]
    S += [note('Não confunda',
               'A Lei de Walras <b>não</b> diz que todo mercado está em equilíbrio a qualquer preço. '
               'Ela diz que o <i>valor</i> do excesso de demanda agregado é sempre zero. Fora do '
               'equilíbrio, um mercado com excesso de demanda é necessariamente compensado por outro com '
               'excesso de oferta.', LIGHT_RED, RED)]
    return S


def secao_monopolio():
    S = [PageBreak(), P('5. Monopólio: decisão, receita marginal e elasticidade', 'H1x')]
    S += [P('O monopolista é <i>price maker</i>: enfrenta a demanda de mercado e escolhe a quantidade que '
            'maximiza o lucro. Ele não escolhe preço e quantidade de forma independente, porque a demanda '
            'amarra os dois.')]
    S.extend(formula([r'\max_{Q}\;\; \pi(Q) \;=\; R(Q) - C(Q)']))

    S += [P('5.1 Receita marginal e o efeito-preço', 'H2x')]
    S += [P('Aumentar a quantidade tem dois efeitos: vende-se mais unidades, mas o preço cai para '
            '<b>todas</b> as unidades. O segundo efeito é o que separa o monopólio da concorrência.')]
    S.extend(formula([
        r'R(Q) = P(Q)\cdot Q',
        r"RMg(Q) = \frac{dR}{dQ} = P(Q) + P'(Q)\cdot Q",
        r"\text{efeito quantidade: } P(Q) > 0 \qquad \text{efeito preço: } P'(Q)\cdot Q < 0",
        r"\text{concorrência perfeita: } P'(Q) = 0 \;\Longrightarrow\; RMg = P",
    ]))
    S += [P('Para demanda linear, a receita marginal tem o mesmo intercepto vertical e o dobro da '
            'inclinação:')]
    S.extend(formula([
        r'P(y) = a - by \;\Longrightarrow\; R(y) = ay - by^2 \;\Longrightarrow\; RMg(y) = a - 2by',
        r'\text{intercepto horizontal: } \frac{a}{2b} \;\text{ contra }\; \frac{a}{b} \text{ da demanda}',
    ]))
    S += figure('02-demanda-rmg.png',
                'A receita marginal corta o eixo horizontal na metade do intercepto da demanda, exatamente '
                'onde a elasticidade tem módulo 1.')

    S += [P('5.2 Condição de ótimo', 'H2x')]
    S.extend(formula([
        r'RMg(Q_m) \;=\; CMg(Q_m)',
        r'P_m \;=\; P(Q_m) \quad \text{(lido na DEMANDA, nunca na } RMg)',
        r'\pi_m \;=\; \left[P_m - CMe(Q_m)\right]\cdot Q_m',
    ]))
    S += [P('A curva de oferta competitiva vem do custo marginal acima do mínimo do custo médio. '
            'O monopolista <b>não</b> tem curva de oferta independente: a quantidade ótima depende '
            'conjuntamente da demanda e do custo.')]
    S += figure('03-monopolio-equilibrio.png',
                'Exemplo dos slides com P = 100 − y e C(y) = y²/2 + 10. O monopólio produz y = 100/3 e '
                'cobra p = 200/3; a referência competitiva seria y = 50 e p = 50.')

    S += [P('5.3 Elasticidade, markup e poder de mercado', 'H2x')]
    S.extend(formula([
        r'RMg = p(y)\left(1 + \frac{1}{\epsilon(y)}\right) '
        r'= p(y)\left(1 - \frac{1}{|\epsilon(y)|}\right), \qquad \epsilon(y) < 0',
        r'p(y)\left(1 - \frac{1}{|\epsilon(y)|}\right) = CMg(y)',
        r'\frac{P}{CMg} \;=\; \frac{1}{1 - \dfrac{1}{|\epsilon|}} \;=\; M \;>\; 1',
    ]))
    S += bullets([
        'Quanto <b>menos</b> elástica a demanda, maior o markup.',
        'O poder de mercado é medido pelo inverso da elasticidade, 1/|ε|.',
        'Na concorrência perfeita |ε| tende ao infinito e o markup vai a 1, isto é, P = CMg.',
    ])
    S += [note('Por que o monopolista nunca opera na região inelástica',
               'Se |ε| &lt; 1, então 1 − 1/|ε| &lt; 0 e portanto RMg &lt; 0. Reduzir a quantidade '
               'aumentaria a receita total <b>e</b> reduziria o custo total ao mesmo tempo. Nenhum ponto '
               'nessa região pode ser ótimo, qualquer que seja o custo marginal.', GOLD)]
    S += [P('5.4 Exemplo numérico dos slides', 'H2x')]
    S.extend(formula([
        r'P(y) = 100 - y, \qquad C(y) = \frac{y^2}{2} + 10',
        r'RMg = 100 - 2y, \qquad CMg = y',
        r'100 - 2y = y \;\Longrightarrow\; y_m = \frac{100}{3} \approx 33{,}33 '
        r'\qquad p_m = \frac{200}{3} \approx 66{,}67',
        r'\text{concorrência: } P = CMg \;\Longrightarrow\; y_c = 50, \quad p_c = 50',
    ]))
    return S


def secao_bem_estar():
    S = [PageBreak(), P('6. Bem-estar: concorrência versus monopólio', 'H1x')]
    S += [P('O material de excedente usa P = 100 − 2Q e CMg = 10 + 3Q. Na concorrência, a disposição a '
            'pagar da última unidade se iguala ao custo marginal. No monopólio a firma restringe a '
            'quantidade, porque considera o efeito da queda de preço sobre todas as unidades.')]

    S += [P('6.1 Os dois equilíbrios', 'H2x')]
    S.extend(formula([
        r'\text{Concorrência:}\quad 100 - 2Q = 10 + 3Q \;\Longrightarrow\; Q_c = 18,\;\; P_c = 64',
        r'\text{Monopólio:}\quad RMg = 100 - 4Q',
        r'100 - 4Q = 10 + 3Q \;\Longrightarrow\; Q_m = \frac{90}{7} \approx 12{,}86 '
        r'\qquad P_m = \frac{520}{7} \approx 74{,}29',
    ]))

    S += [P('6.2 Excedentes', 'H2x')]
    S.extend(formula([
        r'EC = \frac{1}{2}\cdot Q\cdot\left(P_{max} - P\right)',
        r'EC_c = \frac{1}{2}(18)(100-64) = 324 \qquad EP_c = \frac{1}{2}(18)(64-10) = 486',
        r'CMg(Q_m) = 10 + 3\cdot\frac{90}{7} = \frac{340}{7} \approx 48{,}57',
        r'\text{retângulo: } Q_m\left(P_m - CMg(Q_m)\right) = \frac{90}{7}\cdot\frac{180}{7} '
        r'\approx 330{,}61',
        r'\text{triângulo: } \frac{1}{2}Q_m\left(CMg(Q_m) - CMg(0)\right) \approx 248{,}98',
        r'EP_m \approx 330{,}61 + 248{,}98 = 578{,}57',
    ]))
    S += [P('Atenção: com custo marginal <b>crescente</b>, o excedente do produtor no monopólio não é um '
            'triângulo simples. Ele é a área entre a linha de preço e a curva de custo marginal, o que dá '
            'um retângulo mais um triângulo.')]
    S.append(table([
        [P('Indicador', 'Smallx'), P('Concorrência', 'Smallx'), P('Monopólio', 'Smallx'),
         P('Efeito', 'Smallx')],
        [P('Quantidade', 'Smallx'), P('18', 'Smallx'), P('12,86', 'Smallx'), P('reduz', 'Smallx')],
        [P('Preço', 'Smallx'), P('64', 'Smallx'), P('74,29', 'Smallx'), P('aumenta', 'Smallx')],
        [P('Excedente do consumidor', 'Smallx'), P('324', 'Smallx'), P('165,31', 'Smallx'),
         P('cai 158,69', 'Smallx')],
        [P('Excedente do produtor', 'Smallx'), P('486', 'Smallx'), P('578,57', 'Smallx'),
         P('sobe 92,57', 'Smallx')],
        [P('Excedente total', 'Smallx'), P('810', 'Smallx'), P('743,88', 'Smallx'), P('cai', 'Smallx')],
        [P('Perda de peso morto', 'Smallx'), P('0', 'Smallx'), P('66,12', 'Smallx'),
         P('perda líquida', 'Smallx')],
    ], [5.2 * cm, 3.4 * cm, 3.4 * cm, 4.7 * cm]))

    S += [P('6.3 Transferência contra perda líquida', 'H2x')]
    S.extend(formula([
        r'\text{Transferência } EC \to EP = Q_m\left(P_m - P_c\right) '
        r'= \frac{90}{7}\left(\frac{520}{7} - 64\right) \approx 132{,}24',
        r'PPM = ET_c - ET_m = 810 - 743{,}88 = 66{,}12',
        r'\text{conferindo: } PPM = \frac{1}{2}\left(Q_c - Q_m\right)\left(P_m - CMg(Q_m)\right) '
        r'\approx \frac{1}{2}(5{,}14)(25{,}71) = 66{,}12',
    ]))
    S += [P('A queda de 158,69 no excedente do consumidor <b>não</b> é toda perda social: 132,24 é '
            'transferência para o produtor e apenas o restante compõe a perda líquida. A perda de peso '
            'morto corresponde às unidades entre Q<sub>m</sub> e Q<sub>c</sub> que deixaram de ser '
            'produzidas mesmo tendo benefício social acima do custo.')]
    S += figure('04-onus-monopolio.png',
                'Áreas de excedente do consumidor e do produtor, transferência e perda de peso morto no '
                'exemplo do material.')
    return S


def secao_discriminacao():
    S = [PageBreak(), P('7. Discriminação de preços', 'H1x')]
    S += [P('Discriminar é cobrar preços diferentes por unidades ou consumidores conforme a disposição a '
            'pagar. Exige poder de mercado, capacidade de distinguir ou induzir tipos e algum bloqueio à '
            'revenda entre consumidores.')]
    S.append(table([
        [P('Grau', 'Smallx'), P('Como funciona', 'Smallx'), P('Resultado típico', 'Smallx')],
        [P('1º', 'Smallx'), P('Preço personalizado, igual à disposição a pagar de cada consumidor.', 'Smallx'),
         P('Captura todo o excedente do consumidor; produz até P = CMg; sem perda de peso morto.', 'Smallx')],
        [P('2º', 'Smallx'), P('Menu de quantidades, pacotes ou versões; o consumidor se auto-seleciona.', 'Smallx'),
         P('Extrai excedente sem observar diretamente o tipo de cada consumidor.', 'Smallx')],
        [P('3º', 'Smallx'), P('Preços diferentes por grupos observáveis (estudante, idoso, região).', 'Smallx'),
         P('Preço mais alto no mercado menos elástico.', 'Smallx')],
    ], [1.5 * cm, 8.2 * cm, 7.0 * cm]))

    S += [P('7.1 Terceiro grau: a condição central', 'H2x')]
    S += [P('Uma unidade adicional custa o mesmo CMg em qualquer mercado. Logo, no ótimo, a receita '
            'marginal tem de ser igual nos dois — caso contrário compensaria remanejar vendas.')]
    S.extend(formula([
        r'RMg_1 \;=\; RMg_2 \;=\; CMg',
        r'p_1\left(1 - \frac{1}{|\epsilon_1|}\right) = p_2\left(1 - \frac{1}{|\epsilon_2|}\right) = CMg',
    ]))
    S += [P('Aplicando ao exemplo dos slides e da Lista 1, com ε₁ = −2 e ε₂ = −4:')]
    S.extend(formula([
        r'RMg_1 = p_1\left(1 - \frac{1}{2}\right) = 0{,}50\,p_1 \qquad '
        r'RMg_2 = p_2\left(1 - \frac{1}{4}\right) = 0{,}75\,p_2',
        r'0{,}50\,p_1 = 0{,}75\,p_2 \;\Longrightarrow\; \frac{p_1}{p_2} = 1{,}5',
    ]))
    S += [P('Se a firma cobrasse p₁ = 2,5p₂, teríamos RMg₁ = 1,25p₂ contra RMg₂ = 0,75p₂. Como a receita '
            'marginal no mercado 1 seria maior, valeria a pena vender mais nele: reduzir p₁ e/ou aumentar '
            'p₂ até igualar as receitas marginais.')]
    S += figure('05-discriminacao-precos.png',
                'Os três graus de discriminação. No painel da direita as demandas estão calibradas para '
                'módulos de elasticidade 2 e 4 no ótimo, com razão de preços exatamente 1,5.', 16.8 * cm)

    S += [P('7.2 Segundo grau: o exemplo dos slides', 'H2x')]
    S += [P('O Tipo A aceita pagar 30, 20 e 10 pelas três primeiras unidades; o Tipo B aceita 20 e 10 '
            'pelas duas primeiras. Um pacote de 2 unidades por R$ 30 captura o Tipo B (20 + 10) e um '
            'pacote de 3 unidades por R$ 60 captura o Tipo A (30 + 20 + 10). Os pacotes fazem os tipos se '
            'revelarem por conta própria.')]
    return S


def secao_metodo():
    S = [PageBreak(), P('8. Método de resolução e pegadinhas', 'H1x')]
    S += [P('8.1 Checklist de equilíbrio geral', 'H2x')]
    S += bullets([
        'Liste as dotações e some os totais de cada bem: é a base da caixa de Edgeworth.',
        'Calcule a renda como <b>valor</b> da dotação, nunca como quantidade.',
        'Derive a demanda individual antes de somar entre agentes.',
        'Normalize um preço e equilibre apenas um mercado.',
        'Confira o segundo mercado pela factibilidade e pela Lei de Walras.',
        'Verifique se as cestas finais somam exatamente as dotações totais.',
    ])
    S += [P('8.2 Checklist de monopólio', 'H2x')]
    S += bullets([
        'Se a demanda vier como Q(P), <b>inverta</b> para P(Q) antes de derivar.',
        'Calcule a receita total e depois a receita marginal.',
        'Iguale a receita marginal ao custo marginal para achar a quantidade.',
        'Volte à curva de demanda para ler o preço.',
        'Compare o preço com o custo médio para obter o lucro.',
        'Para bem-estar, calcule também o equilíbrio competitivo com P = CMg.',
    ])
    S += [P('8.3 Pegadinhas frequentes', 'H2x')]
    S.append(table([
        [P('Erro', 'Smallx'), P('Correção', 'Smallx')],
        [P('Usar P = CMg no monopólio.', 'Smallx'),
         P('P = CMg é a condição competitiva. No monopólio use RMg = CMg e leia o preço na demanda.', 'Smallx')],
        [P('Ler o preço na curva de receita marginal.', 'Smallx'),
         P('A RMg serve apenas para achar a quantidade. O preço sempre sai da demanda.', 'Smallx')],
        [P('Tratar Pareto-eficiente como justo.', 'Smallx'),
         P('Eficiência e equidade são critérios distintos. Os cantos da caixa são eficientes e '
           'extremamente desiguais.', 'Smallx')],
        [P('Buscar preços absolutos no equilíbrio geral.', 'Smallx'),
         P('Só o preço relativo é determinado. Fixe um numerário.', 'Smallx')],
        [P('Dizer que toda a perda do consumidor é peso morto.', 'Smallx'),
         P('Boa parte é transferência para o produtor. A PPM é apenas a perda líquida do excedente total.', 'Smallx')],
        [P('No 3º grau, cobrar mais onde a demanda é mais elástica.', 'Smallx'),
         P('É o inverso: preço mais alto no mercado <b>menos</b> elástico.', 'Smallx')],
        [P('Usar a fórmula triangular do EP com CMg crescente.', 'Smallx'),
         P('Com CMg crescente, o EP do monopólio é retângulo mais triângulo.', 'Smallx')],
    ], [5.6 * cm, 11.1 * cm]))
    return S


EXERCICIOS = [
    ('Exercício 1 — Lista 1, Q1 (troca pura)',
     'Dois agentes A e B têm U<sub>i</sub>(x₁,x₂) = x₁x₂, com dotações w<sub>A</sub> = (4,2) e '
     'w<sub>B</sub> = (1,3). (a) Verifique se há incentivo à troca na dotação inicial. '
     '(b) Encontre as demandas marshallianas. (c) Determine p₁/p₂ e as cestas de equilíbrio. '
     '(d) Calcule as demandas líquidas e interprete em termos de eficiência de Pareto.'),
    ('Exercício 2 — Lista 1, Q2 (Cobb–Douglas assimétrica)',
     'U = x⁴y⁶ para o agente 1 e V = x⁶y⁴ para o agente 2, com dotações (4,2) e (2,4). Julgue: '
     '(a) o agente 1 gasta 40% da renda em x; (b) p<sub>x</sub>/p<sub>y</sub> = 2; '
     '(c) o agente 1 consome 2,4 unidades de x; (d) a TMS do agente 1 no equilíbrio é 1.'),
    ('Exercício 3 — Lista 1, Q3 (curva de contrato com Leontief)',
     'U<sub>A</sub> = x₁<super>1/3</super>x₂<super>2/3</super>, '
     'U<sub>B</sub> = min{x₁, x₂}, w<sub>A</sub> = (10,20) e w<sub>B</sub> = (20,5). '
     '(a) Obtenha a curva de contrato. (b) Avalie se x<sub>A</sub> = (10,5) e x<sub>B</sub> = (20,20) é '
     'Pareto-eficiente. (c) Com p₁ = p₂ = 1, calcule o excesso de demanda agregado.'),
    ('Exercício 4 — Lista 1, Q4 (monopólio)',
     'A demanda é P = 18 − Q e o custo total é CT(Q) = 27 + 2Q². Encontre a receita marginal, o custo '
     'marginal, a quantidade e o preço de monopólio. Calcule o lucro e interprete.'),
    ('Exercício 5 — exemplo dos slides (equilíbrio geral)',
     'U<sub>A</sub> = x₁<super>A</super>(x₂<super>A</super>)², '
     'U<sub>B</sub> = (x₁<super>B</super>)²x₂<super>B</super>, w<sub>A</sub> = (10,10) e '
     'w<sub>B</sub> = (20,20). Normalize p₁ = 1, encontre p₂, as cestas de equilíbrio e as demandas '
     'líquidas. Verifique a Lei de Walras.'),
    ('Exercício 6 — Lista 1, Q6 (terceiro grau)',
     'Um monopolista vende em dois mercados com ε₁ = −2 e ε₂ = −4. Mostre se a política p₁ = 2,5p₂ '
     'maximiza o lucro e encontre a relação correta entre os preços.'),
    ('Exercício 7 — excedentes e perda de peso morto',
     'Com P = 100 − 2Q e CMg = 10 + 3Q, calcule os equilíbrios competitivo e monopolista, os excedentes '
     'do consumidor e do produtor nos dois casos, o excedente total e a perda de peso morto. Separe a '
     'parcela de transferência.'),
    ('Exercício 8 — questão conceitual',
     'Explique por que o monopolista nunca escolhe quantidade na região inelástica da demanda, e por que '
     'a discriminação de primeiro grau elimina a perda de peso morto embora seja distributivamente '
     'controversa.'),
]


def secao_exercicios():
    S = [PageBreak(), P('9. Exercícios para resolver', 'H1x')]
    S += [P('Resolva antes de abrir a seção 10. Os exercícios 1 a 4 e 6 são da Lista 1; os demais '
            'consolidam os exemplos dos slides e do material de excedente.')]
    S += [note('Onde encontrar mais',
               'A Lista 1 resolvida item por item, incluindo a Questão 5 das duas fábricas, e um banco de '
               '23 exercícios adicionais com gabarito estão no arquivo '
               '<b>lista1-resolvida-e-exercicios-extra.pdf</b>, na mesma pasta.', LIGHT_BLUE, BLUE)]
    for titulo, texto in EXERCICIOS:
        S += [P(titulo, 'H2x'), note('Para resolver', texto, colors.white, BORDER),
              Spacer(1, .08 * cm)]
    return S


def secao_gabaritos():
    S = [PageBreak(), P('10. Gabaritos comentados', 'H1x')]

    S += [P('Gabarito 1 — troca pura', 'H2x')]
    S.extend(formula([
        r'TMS_A(4,2) = \frac{2}{4} = 0{,}5 \qquad TMS_B(1,3) = \frac{3}{1} = 3 '
        r'\;\Longrightarrow\; \text{há troca}',
        r'x_1^{i\,*} = \frac{m_i}{2p_1} \qquad x_2^{i\,*} = \frac{m_i}{2p_2}',
        r'\frac{5p_1+5p_2}{2p_1} = 5 \;\Longrightarrow\; \frac{p_1}{p_2} = 1',
        r'm_A = 6,\; m_B = 4 \;\Longrightarrow\; x^A = (3,3),\quad x^B = (2,2)',
        r'e^A = (-1,+1) \qquad e^B = (+1,-1)',
    ]))
    S += [P('A curva de contrato é x₂<super>A</super> = x₁<super>A</super> e o ponto (3,3) está sobre ela, '
            'com TMS<sub>A</sub> = TMS<sub>B</sub> = 1 = p₁/p₂. A utilidade de A sai de 8 para 9 e a de B '
            'de 3 para 4.', 'Answer')]
    S += [note('Resposta', 'Há incentivo à troca; <b>p₁/p₂ = 1</b>; <b>A = (3,3)</b> e <b>B = (2,2)</b>. '
               'O equilíbrio é Pareto-eficiente.', LIGHT_GREEN, GREEN)]

    S += [P('Gabarito 2 — Cobb–Douglas assimétrica', 'H2x')]
    S.extend(formula([
        r'\text{frações de gasto em } x:\quad \frac{4}{10} = 40\% \;\text{(agente 1)},\qquad '
        r'\frac{6}{10} = 60\% \;\text{(agente 2)}',
        r'p_y = 1,\; r = p_x: \qquad m_1 = 4r+2, \qquad m_2 = 2r+4',
        r'\frac{0{,}4(4r+2)}{r} + \frac{0{,}6(2r+4)}{r} = 6 '
        r'\;\Longrightarrow\; 2{,}8 + \frac{3{,}2}{r} = 6 \;\Longrightarrow\; r = 1',
        r'x_1 = 0{,}4\cdot\frac{6}{1} = 2{,}4 \qquad y_1 = 0{,}6\cdot 6 = 3{,}6',
        r'TMS_1 = \frac{4y}{6x} = \frac{2(3{,}6)}{3(2{,}4)} = 1',
    ]))
    S += [note('Resposta', '<b>Verdadeiras: (a), (c) e (d). Falsa: (b)</b> — o preço relativo é 1, não 2. '
               'Atalho: preferências e dotações espelhadas implicam preço relativo unitário por simetria.',
               LIGHT_GREEN, GREEN)]

    S += [P('Gabarito 3 — curva de contrato com Leontief', 'H2x')]
    S.extend(formula([
        r'\text{totais: } 10+20 = 30 \;\text{(bem 1)}, \qquad 20+5 = 25 \;\text{(bem 2)}',
        r'\min\{x_1,x_2\} \;\Longrightarrow\; x_1^B = x_2^B \quad\text{(vértice)}',
        r'x_2^A = 25 - x_2^B = 25 - x_1^B = 25 - (30 - x_1^A) \;\Longrightarrow\; x_2^A = x_1^A - 5',
        r'p = (1,1):\quad m_A = 30 \;\Longrightarrow\; x^A = (10,20) = w^A '
        r'\;\Longrightarrow\; e^A = (0,0)',
        r'm_B = 25 \;\Longrightarrow\; x_1^B = x_2^B = \frac{25}{2} = 12{,}5 '
        r'\;\Longrightarrow\; e^B = (-7{,}5,\; +7{,}5)',
        r'z = (-7{,}5,\; +7{,}5) \qquad p_1 z_1 + p_2 z_2 = 0 \;\checkmark',
    ]))
    S += [P('Note que o agente A demanda exatamente sua própria dotação a esses preços, então todo o '
            'desequilíbrio vem de B. A alocação do item (a) é factível, respeita o vértice de B e satisfaz '
            'a curva de contrato, logo é eficiente.', 'Answer')]
    S += [note('Resposta', '<b>(a) V, (b) F, (c) V, (d) V.</b> Curva de contrato '
               'x₂<super>A</super> = x₁<super>A</super> − 5 e excesso de demanda (−7,5; +7,5).',
               LIGHT_GREEN, GREEN)]

    S += [P('Gabarito 4 — monopólio com custo quadrático', 'H2x')]
    S.extend(formula([
        r'R(Q) = (18-Q)Q \;\Longrightarrow\; RMg = 18 - 2Q, \qquad CMg = 4Q',
        r'18 - 2Q = 4Q \;\Longrightarrow\; Q_m = 3 \qquad P_m = 18 - 3 = 15',
        r'\pi = 15(3) - \left[27 + 2(3^2)\right] = 45 - 45 = 0',
        r'CMe(3) = \frac{27}{3} + 2(3) = 15 = P_m',
    ]))
    S += [note('Resposta', '<b>Q = 3, P = 15 e lucro exatamente zero.</b> Ser monopolista não garante lucro: '
               'o preço fica acima do custo marginal (15 contra 12), mas o custo fixo de 27 consome toda a '
               'margem. Ainda assim produzir 3 é melhor que fechar, o que daria prejuízo de 27.',
               LIGHT_GREEN, GREEN)]

    S += [P('Gabarito 5 — exemplo dos slides', 'H2x')]
    S.extend(formula([
        r'x_1^A = \frac{10(1+p_2)}{3}, \quad x_1^B = \frac{40(1+p_2)}{3}',
        r'\frac{50(1+p_2)}{3} = 30 \;\Longrightarrow\; p_2 = 0{,}8',
        r'x^A = (6,15) \qquad x^B = (24,15)',
        r'e^A = (-4,+5) \qquad e^B = (+4,-5)',
    ]))
    S += [P('As demandas somam (30, 30), exatamente as dotações totais, e a Lei de Walras confirma o '
            'segundo mercado sem precisar resolvê-lo.', 'Answer')]

    S += [P('Gabarito 6 — discriminação de terceiro grau', 'H2x')]
    S.extend(formula([
        r'RMg_1 = 0{,}50\,p_1 \qquad RMg_2 = 0{,}75\,p_2',
        r'0{,}50\,p_1 = 0{,}75\,p_2 \;\Longrightarrow\; \frac{p_1}{p_2} = 1{,}5',
        r'\text{se } p_1 = 2{,}5\,p_2: \quad RMg_1 = 1{,}25\,p_2 \;>\; RMg_2 = 0{,}75\,p_2',
    ]))
    S += [note('Resposta', '<b>Não está maximizando.</b> A razão correta é <b>p₁/p₂ = 1,5</b>. '
               'A direção está certa (preço maior no mercado menos elástico), mas a magnitude está errada: '
               'deveria ser 50% de diferença, não 150%. O ajuste é reduzir p₁ e/ou aumentar p₂.',
               LIGHT_GREEN, GREEN)]

    S += [P('Gabarito 7 — excedentes e perda de peso morto', 'H2x')]
    S.extend(formula([
        r'Q_c = 18,\; P_c = 64 \qquad Q_m = \frac{90}{7} \approx 12{,}86,\; '
        r'P_m = \frac{520}{7} \approx 74{,}29',
        r'EC_c = 324, \quad EP_c = 486, \quad ET_c = 810',
        r'EC_m \approx 165{,}31, \quad EP_m \approx 578{,}57, \quad ET_m \approx 743{,}88',
        r'\text{transferência} \approx 132{,}24 \qquad PPM = 810 - 743{,}88 = 66{,}12',
    ]))
    S += [P('O produtor ganha excedente, mas o ganho de 92,57 não compensa a perda de 158,69 do '
            'consumidor. A diferença é a perda líquida de bem-estar.', 'Answer')]

    S += [P('Gabarito 8 — questão conceitual', 'H2x')]
    S += [P('Na região inelástica |ε| &lt; 1, então RMg = P(1 − 1/|ε|) &lt; 0. Reduzir a quantidade '
            'aumentaria a receita e reduziria o custo simultaneamente, portanto nenhum ponto ali pode ser '
            'ótimo, independentemente do custo marginal.', 'Answer')]
    S += [P('Na discriminação de primeiro grau cada unidade é vendida ao preço máximo que aquele '
            'consumidor aceita pagar. A firma segue expandindo enquanto a disposição a pagar for pelo '
            'menos o custo marginal, então a quantidade coincide com a eficiente e a perda de peso morto '
            'desaparece. A ressalva é distributiva: o excedente do consumidor vai a zero, e toda a '
            'eficiência é apropriada pela firma.', 'Answer')]
    return S


CHECKLIST = [
    'Desenhar e interpretar uma caixa de Edgeworth, identificando as duas origens.',
    'Calcular a TMS e explicar por que TMS diferentes geram ganhos de troca.',
    'Derivar a curva de contrato com Cobb–Douglas e com Leontief.',
    'Escrever a renda de cada consumidor como valor da dotação.',
    'Obter demandas Cobb–Douglas pela regra de bolso e equilibrar um mercado.',
    'Enunciar a Lei de Walras e explicar preço relativo e numerário.',
    'Calcular receita total, receita marginal, quantidade, preço e lucro de monopólio.',
    'Explicar por que o monopolista opera só na região elástica.',
    'Calcular excedentes e perda de peso morto com curvas lineares.',
    'Distinguir transferência de excedente de perda de peso morto.',
    'Aplicar a igualdade de receitas marginais na discriminação de terceiro grau.',
    'Explicar os três graus de discriminação e as condições que os viabilizam.',
]


def secao_formulario():
    S = [PageBreak(), P('11. Formulário e checklist final', 'H1x')]
    S += [P('11.1 Formulário de uma página', 'H2x')]
    S.extend(formula([
        r'm_i = p_1 w_i^1 + p_2 w_i^2',
        r'TMS_i = \frac{UMg_1^i}{UMg_2^i} = \frac{p_1}{p_2}',
        r'U = x_1^{\alpha}x_2^{\beta} \;\Longrightarrow\; '
        r'x_1^* = \frac{\alpha}{\alpha+\beta}\frac{m}{p_1},\quad '
        r'x_2^* = \frac{\beta}{\alpha+\beta}\frac{m}{p_2}',
        r'\sum_i x_i^k = \sum_i w_i^k \qquad z^k = \sum_i x_i^k - \sum_i w_i^k',
    ], juntar=False))
    S.extend(formula([
        r'\text{Pareto interior: } TMS_A = TMS_B',
        r'\text{Lei de Walras: } \sum_k p_k z_k(p) = 0 \quad \forall\, p',
        r'\text{Leontief } \min\{x_1,x_2\}: \; x_1 = x_2 = \frac{m}{p_1+p_2}',
    ], juntar=False))
    S.extend(formula([
        r"R(Q) = P(Q)Q \qquad RMg = P + P'(Q)\,Q \qquad RMg = CMg "
        r"\;\Longrightarrow\; P_m = P(Q_m)",
        r'P(y) = a - by \;\Longrightarrow\; RMg = a - 2by',
        r'RMg = P\left(1 - \frac{1}{|\epsilon|}\right) \qquad '
        r'\frac{P}{CMg} = \frac{1}{1 - 1/|\epsilon|}',
        r'\pi = \left[P - CMe(Q)\right]Q \qquad \text{concorrência: } P = CMg',
    ], juntar=False))
    S.extend(formula([
        r'EC = \frac{1}{2}Q\left(P_{max} - P\right) \qquad PPM = ET_c - ET_m',
        r'\text{3º grau: } RMg_1 = RMg_2 = CMg \;\Longrightarrow\; '
        r'\text{maior preço onde } |\epsilon| \text{ é menor}',
    ], juntar=False))

    S += [P('11.2 Checklist “eu sei fazer?”', 'H2x')]
    S += [P('Marque cada item somente depois de resolvê-lo sem consultar o texto:')]
    S += [P('□ ' + item) for item in CHECKLIST]
    S += [Spacer(1, .25 * cm),
          note('Prioridade para a véspera',
               '<b>1.</b> Refaça os exercícios 1, 3, 4, 6 e 7. '
               '<b>2.</b> Memorize o roteiro RMg = CMg e a regra do terceiro grau. '
               '<b>3.</b> Desenhe de memória a caixa de Edgeworth e o gráfico de perda de peso morto. '
               '<b>4.</b> Confira sinais de demanda líquida e preços relativos.', LIGHT_GREEN, GREEN)]
    S += [Spacer(1, .3 * cm),
          P('<b>Nota de transparência:</b> este resumo foi produzido a partir dos arquivos da disciplina '
            'disponíveis no diretório <i>prints</i> do repositório. As equações de custo da Questão 5 da '
            'Lista 1 estavam embutidas como imagem no PDF original e foram recuperadas por renderização: '
            'C₁(Q₁) = 10Q₁² e C₂(Q₂) = 20Q₂². Todos os resultados numéricos são recalculados por '
            '<i>verificar_contas.py</i>, com 114 checagens simbólicas em SymPy. A teoria está coberta, '
            'mas a notação usada em aula deve prevalecer em caso de divergência.', 'Smallx')]
    return S


def main():
    badge = note('Como usar este resumo',
                 'Leia a intuição antes da álgebra e só depois refaça os exercícios sem consultar o '
                 'gabarito. Os gráficos foram reconstruídos a partir dos números dos slides de revisão, '
                 'da Lista 1 e do material de excedente.', LIGHT_BLUE, BLUE)
    story = cover(
        'MICROECONOMIA II', 'Resumo completo para a Prova 1',
        ['Equilíbrio geral • Caixa de Edgeworth • Lei de Walras',
         'Monopólio • Bem-estar • Discriminação de preços',
         '',
         '<b>Disciplina:</b> CE-362D — Microeconomia II',
         '<b>Universidade:</b> Instituto de Economia — Unicamp'],
        badge)

    story += [PageBreak(), P('Sumário', 'H1x')]
    sumario = [
        '1. Escopo provável da P1 e mapa do material',
        '2. Equilíbrio geral em uma economia de trocas',
        '3. Caixa de Edgeworth, eficiência e curva de contrato',
        '4. Álgebra do equilíbrio e Lei de Walras',
        '5. Monopólio: decisão, receita marginal e elasticidade',
        '6. Bem-estar: concorrência versus monopólio',
        '7. Discriminação de preços',
        '8. Método de resolução e pegadinhas',
        '9. Exercícios para resolver',
        '10. Gabaritos comentados',
        '11. Formulário e checklist final',
    ]
    story += [P(x, 'TOC') for x in sumario]
    story += [Spacer(1, .35 * cm),
              note('Os dois resultados que você não pode esquecer',
                   '<b>Equilíbrio geral:</b> os preços relativos coordenam as decisões individuais e zeram '
                   'a demanda excedente agregada. <b>Monopólio:</b> a firma escolhe a quantidade onde '
                   'RMg = CMg e depois lê o preço na demanda, o que resulta em preço acima do custo '
                   'marginal e quantidade abaixo da competitiva.', LIGHT_GREEN, GREEN),
              PageBreak()]

    story += secao_escopo()
    story += secao_equilibrio_geral()
    story += secao_edgeworth()
    story += secao_algebra_walras()
    story += secao_monopolio()
    story += secao_bem_estar()
    story += secao_discriminacao()
    story += secao_metodo()
    story += secao_exercicios()
    story += secao_gabaritos()
    story += secao_formulario()

    caminho = build_pdf(OUT, story,
                        title='Resumo da Prova 1 — Microeconomia II',
                        left_title='MICROECONOMIA II — RESUMO DA PROVA 1',
                        right_title='CE-362D | Unicamp | 2º semestre de 2026',
                        footer_note='Material de estudo — confira a notação usada em aula')
    print(caminho)
    print(os.path.getsize(caminho), 'bytes')


if __name__ == '__main__':
    main()
