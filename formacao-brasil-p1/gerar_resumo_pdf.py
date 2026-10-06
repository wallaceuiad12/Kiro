"""
Gera o PDF de resumo para a P1 de Formação Econômica / História do Brasil Colonial.

Conteúdo organizado a partir do slide "Seis autores, uma linha" (print
20260924_165705.jpg) e do programa completo do curso. Os seis autores do slide
recebem tratamento aprofundado; os pontos 3 a 6 do programa vêm como moldura.

Uso: python3 gerar_resumo_pdf.py
Saída: resumo-p1-formacao-brasil.pdf
"""
import os

from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Spacer

from estilo_pdf import (
    BLUE, CONTENT_W, GOLD, GRAY, GREEN, LIGHT_BLUE, LIGHT_GREEN, LIGHT_PURPLE,
    LIGHT_RED, NAVY, PURPLE, RED, P, build_pdf, bullets, cover, note, rule, table,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.join(ROOT, 'resumo-p1-formacao-brasil.pdf')

S = []

# ===========================================================================
# CAPA
# ===========================================================================
S += cover(
    'Formação Econômica do Brasil',
    'Resumo para a Prova 1',
    [
        'Construído a partir do slide <b>“Seis autores, uma linha”</b>',
        'e do programa completo da disciplina',
    ],
    badge=note(
        'Seis autores, uma linha',
        'Caio Prado (1942) · Novais (1979) · Fragoso, Bicalho &amp; Gouvêa (2000) · '
        'Faoro (1958) · Godinho · Neves (2022)<br/><br/>'
        'A “linha” do slide é a <b>unidade de análise</b>: todos tratam do mesmo objeto — '
        'a colonização e a formação do Brasil e de Portugal —, mas cada um recorta uma '
        '<b>escala diferente</b>, e é a escala que produz a tese.',
        LIGHT_BLUE, BLUE, width=CONTENT_W * .88),
)

S += [Spacer(1, 1.1 * cm)]
S += [P('Sumário', 'H2x')]
S += [P(linha, 'TOC') for linha in [
    '<b>0.</b>  A chave do slide: a “linha” é a unidade de análise',
    '<b>1.</b>  Caio Prado Jr. (1942) — o sentido da colonização',
    '<b>2.</b>  Fernando Novais (1979) — estrutura e dinâmica do sistema',
    '<b>3.</b>  Fragoso, Bicalho &amp; Gouvêa (2000) — materialidade e governabilidade',
    '<b>4.</b>  Raimundo Faoro (1958) — origem do Estado português',
    '<b>5.</b>  Vitorino M. Godinho — a formação do Estado e as finanças públicas',
    '<b>6.</b>  Eduardo Góes Neves (2022) — a floresta e quem a produziu',
    '<b>7.</b>  Síntese comparativa e as três controvérsias',
    '<b>8.</b>  Pontos 3 a 6 do programa (moldura essencial)',
    '<b>9.</b>  Roteiro de revisão em 10 frases',
    '<b>10.</b> Checklist das fontes primárias',
]]
S += [PageBreak()]

# ===========================================================================
# 0. A CHAVE DO SLIDE
# ===========================================================================
S += [P('0. A chave do slide: a “linha” é a unidade de análise', 'H1x')]
S += [P(
    'O slide alinha seis autores numa coluna e, ao lado, a <b>unidade de análise</b> que cada um '
    'escolhe. Esse é o fio condutor da matéria: todos falam do <i>mesmo objeto</i>, mas '
    '<b>recortam escalas diferentes</b> — e é a escala que produz a tese. Guardar esse quadro '
    'vale mais do que decorar frases soltas de cada autor.', 'Bodyx')]

S += table([
    ['#', 'Autor', 'Unidade de análise', 'Tese em uma linha'],
    ['1', '<b>Caio Prado Jr.</b><br/>(1942)', 'A <b>colônia</b> no quadro da expansão comercial europeia',
     'A colônia existe <i>para fora</i>: produzir gêneros tropicais para o mercado europeu — '
     'o “sentido da colonização”'],
    ['2', '<b>Fernando Novais</b><br/>(1979)', 'O <b>Antigo Sistema Colonial</b> / a economia metropolitana',
     'A colônia é peça de um <i>sistema</i> de acumulação primitiva, articulado pelo '
     '<b>exclusivo metropolitano</b>'],
    ['3', '<b>Fragoso, Bicalho &amp; Gouvêa</b><br/>(2000)', 'O <b>império como um todo</b> (rede pluricontinental)',
     'Há <b>acumulação e poder endógenos</b> na colônia: um “Antigo Regime nos trópicos”'],
    ['4', '<b>Raimundo Faoro</b><br/>(1958)', 'O <b>Estado português</b> e seu estamento',
     '<b>Patrimonialismo</b>: o Estado precede e organiza a economia — capitalismo '
     'politicamente orientado'],
    ['5', '<b>Vitorino M. Godinho</b>', 'As <b>finanças públicas</b> e a formação do Estado',
     'A estrutura <b>fiscal-financeira</b> da Coroa explica o Estado e a expansão marítima'],
    ['6', '<b>Eduardo G. Neves</b><br/>(2022)', 'A <b>floresta</b> e quem a produziu (Amazônia pré-colonial)',
     'A floresta é em parte <b>artefato humano</b>: oito mil anos de história antes de 1500'],
], [0.8 * cm, 3.5 * cm, 5.3 * cm, 8.1 * cm])

S += note('O rodapé do slide: “sem cerco = sem circunscrição, no sentido de Carneiro (1970)”', [
    'Robert Carneiro (<i>A Theory of the Origin of the State</i>, <b>Science</b>, v. 169, n. 3947, '
    '1970, p. 733-738) explica a formação do Estado pela combinação de <b>pressão demográfica + '
    'circunscrição ambiental + guerra</b>: onde a terra agricultável é <b>cercada</b> por áreas '
    'improdutivas (mar, deserto, montanha), os derrotados na guerra <b>não podem fugir</b> e são '
    'incorporados como subordinados tributários — e daí nasce o Estado coercitivo.',
    'Carneiro constrói o argumento <b>comparando justamente os vales costeiros do Peru '
    '(circunscritos) com a bacia amazônica (não circunscrita)</b>: na Amazônia a terra é aberta, '
    'a fissão e a fuga são sempre possíveis, logo há <b>adensamento e complexidade social sem '
    'Estado coercitivo</b>.',
    'É exatamente o contraste que amarra a aula: <b>Faoro e Godinho</b> descrevem um Estado '
    'formado sob cerco (Reconquista, território delimitado, guerra caríssima, fisco pressionado); '
    '<b>Neves + Carneiro</b> descrevem sociedades complexas <i>sem</i> esse cerco. Mesma pergunta '
    '— “como se organizam poder e produção?” — duas respostas, porque geografia e escala mudam.',
], LIGHT_PURPLE, PURPLE)

S += [P('O movimento da “linha”, em sequência', 'H3x')]
S += [P(
    'Externalismo (1 → 2) → internalismo revisionista (3) → o Estado como sujeito (4 → 5) → '
    'a profundidade pré-colonial (6). Ou seja: o curso <b>começa fora</b> (mercado europeu), '
    '<b>traz para dentro</b> (elites coloniais), <b>vai ao Estado</b> que viabiliza tudo e, por '
    'fim, <b>recua no tempo</b> para mostrar que o “dentro” já existia antes do colonizador.',
    'Bodyx')]

S += rule()

# ===========================================================================
# 1. CAIO PRADO
# ===========================================================================
S += [P('1. Caio Prado Jr. (1942)', 'H1x')]
S += [P('<i>Formação do Brasil Contemporâneo</i> — “Introdução” e cap. 1 '
        '“O sentido da colonização”', 'Smallx')]

S += [P('Método (a Introdução)', 'H2x')]
S += bullets([
    'Olha para o <b>presente</b> e pergunta o que nele é herança colonial: “todo povo tem na sua '
    'evolução, vista a distância, um certo <b>sentido</b>”. Não é cronologia — é <b>linha geral '
    'de evolução</b>.',
    'O Brasil de 1942 é lido como um país ainda marcado pela <b>estrutura colonial</b>. Daí o '
    'título: a <i>formação</i> explica o <i>contemporâneo</i>.',
])

S += [P('A tese', 'H2x')]
S += bullets([
    'A colonização do Brasil é <b>capítulo da expansão comercial europeia</b>. Não é migração, '
    'não é povoamento: é <b>empresa comercial</b>.',
    'Nos trópicos o europeu não vem morar e reproduzir sua sociedade; vem <b>organizar a '
    'produção</b> de gêneros de alto valor no mercado europeu. Daí a distinção entre '
    '<b>colônias de povoamento</b> (zona temperada, Nova Inglaterra) e <b>colônias de '
    'exploração</b> (trópicos).',
    '<b>O “sentido da colonização”</b> = fornecer ao comércio europeu açúcar, tabaco, algodão, '
    'ouro e outros gêneros tropicais e minerais. Todo o resto decorre disso.',
])

S += [P('Os decorrentes — memorize como cadeia causal', 'H2x')]
S += table([
    ['Passo', 'Consequência'],
    ['1', 'Produção para o <b>mercado externo</b> → economia <b>voltada para fora</b>'],
    ['2', 'Gênero de exportação em escala → <b>grande lavoura / monocultura</b>'],
    ['3', 'Grande lavoura → <b>latifúndio</b> e concentração da terra'],
    ['4', 'Falta de mão de obra disposta → <b>escravidão</b> (indígena, depois africana)'],
    ['5', 'Resultado social: sociedade <b>sem coesão</b> e <b>instável</b>, população majoritariamente '
          'escrava e mestiça, instituições precárias, ausência de um “nexo” orgânico — feição de algo '
          '<b>improvisado</b>'],
    ['6', 'Longo prazo: a economia interna é <b>subsidiária</b>; mercado interno e vida urbana '
          'raquíticos; a sociedade não se organiza em torno de si mesma'],
], [1.6 * cm, 16.1 * cm])

S += note('Para a prova', [
    '<b>Palavras-chave:</b> sentido, empresa comercial, colônia de exploração, grande lavoura, '
    'latifúndio, trabalho compulsório, “voltada para fora”, herança colonial.',
    '<b>Crítica clássica:</b> o modelo <b>subestima o mercado interno e a dinâmica própria</b> da '
    'sociedade colonial — é precisamente por aí que entram Fragoso, Bicalho &amp; Gouvêa (e, para '
    'o século XVIII, Furtado e depois Carrara).',
], GOLD)

# ===========================================================================
# 2. NOVAIS
# ===========================================================================
S += rule()
S += [P('2. Fernando Novais (1979)', 'H1x')]
S += [P('<i>Portugal e Brasil na crise do Antigo Sistema Colonial (1776-1808)</i> — '
        'cap. II “Estrutura e Dinâmica do Sistema”', 'Smallx')]
S += [P(
    'Novais <b>formaliza</b> Caio Prado: transforma o “sentido” em <b>sistema</b>, com '
    '<i>estrutura</i> (como funciona) e <i>dinâmica</i> (como entra em crise). Inscreve a '
    'colonização no <b>debate marxista da transição</b> feudalismo → capitalismo.', 'Bodyx')]

S += [P('Estrutura', 'H2x')]
S += bullets([
    'A colonização moderna é um <b>mecanismo de acumulação primitiva de capital</b> na escala da '
    'Europa: a colônia financia a formação do capital que, depois, viabiliza a Revolução Industrial.',
    'Peça central: o <b>exclusivo metropolitano</b> (monopólio, “pacto colonial”). A colônia só '
    'pode comerciar com a metrópole, em navios e por mãos metropolitanas.',
    'Mecânica do exclusivo: a metrópole <b>compra barato</b> o produto colonial e <b>vende caro</b> '
    'manufaturas e escravos. Há <b>troca desigual</b> e transferência de excedente — da colônia '
    'para a metrópole e, dentro da metrópole, para o <b>capital mercantil</b> e, via fisco, para o '
    'Estado absolutista.',
    'A <b>escravidão não é atraso nem resíduo</b>: é <i>funcional</i> ao sistema. Trabalho livre '
    'exigiria salários, consumo e <b>mercado interno</b> colonial — o que contradiria o exclusivo. '
    'Além disso, o <b>tráfico negreiro</b> é, ele mesmo, um dos negócios mais lucrativos do '
    'sistema: a articulação é <b>dupla</b> (tráfico + <i>plantation</i>).',
    'Articulação dos três vértices: <b>metrópole — colônia agroexportadora — África fornecedora '
    'de cativos</b>.',
])

S += [P('Dinâmica (e a crise)', 'H2x')]
S += bullets([
    'O sistema é <b>contraditório</b>: ao promover a acumulação, faz amadurecer o capitalismo '
    'industrial, para o qual o monopólio deixa de ser estímulo e passa a ser <b>obstáculo</b> — '
    'ele quer mercados abertos, não exclusivos.',
    'Logo: <b>“o sistema colonial engendra a sua própria negação”</b>. A crise do Antigo Sistema '
    'Colonial (1776-1808) aparece como crise <i>do sistema</i>, não como soma de acidentes: '
    'independência dos EUA, Revolução Francesa, Haiti, liberalismo econômico, independências '
    'ibero-americanas.',
    'Lado português: Portugal é metrópole <b>frágil</b> e intermediária (reexportadora); a crise '
    'do sistema é, para ela, crise de <b>viabilidade do próprio império</b> — o que leva ao '
    'reformismo ilustrado e, em 1808, à transferência da corte e à abertura dos portos.',
])

S += note('Para a prova — Prado × Novais', [
    'Prado identifica o <b>sentido</b> (empírico-histórico, voltado ao presente brasileiro); '
    'Novais constrói o <b>modelo do sistema</b> (teórico, voltado à transição europeia e à sua crise).',
    '<b>Palavras-chave:</b> acumulação primitiva, exclusivo metropolitano, troca desigual, tráfico '
    'como peça do sistema, contradição interna, crise do Antigo Sistema Colonial.',
], GOLD)

S += rule()

# ===========================================================================
# 3. FRAGOSO, BICALHO & GOUVÊA
# ===========================================================================
S += [P('3. Fragoso, Bicalho &amp; Gouvêa (2000)', 'H1x')]
S += [P('“Uma leitura do Brasil colonial: bases da materialidade e da governabilidade no '
        'império”, <i>Penélope</i>, n. 23, p. 67-88', 'Smallx')]
S += [P(
    'O <b>giro revisionista</b>. Mantém a existência do exclusivo, mas nega que ele <b>explique</b> '
    'a sociedade colonial. A unidade de análise passa a ser <b>o império inteiro</b> — e o olhar '
    'vai <b>de dentro para fora</b>.', 'Bodyx')]

S += [P('Bases da materialidade (a economia)', 'H2x')]
S += bullets([
    'Existe um <b>mercado interno</b> vigoroso: agricultura de abastecimento, pecuária, farinha, '
    'aguardente, transporte, abastecimento das cidades e das Minas.',
    'Existem <b>circuitos intra e intercoloniais</b> não redutíveis ao eixo metrópole-colônia: '
    'Rio de Janeiro–Angola, Rio–Rio da Prata (prata de Potosí), Rio–Minas, Bahia–Costa da Mina '
    '(tabaco de terceira por cativos).',
    'Há <b>acumulação endógena</b>: os grandes <i>homens de negócio</i> do Rio e da Bahia acumulam '
    '<b>na colônia</b>, controlam crédito, tráfico e abastecimento, e reinvestem localmente — '
    'terra, engenhos, escravos, cargos.',
    'Consequência: a colônia <b>não é um simples apêndice</b> que transfere todo o excedente; '
    'parte dele se <b>fixa e se reproduz</b> aqui. Isso relativiza (não anula) a leitura de '
    'Prado e Novais.',
])

S += [P('Bases da governabilidade (o poder)', 'H2x')]
S += bullets([
    '<b>“Antigo Regime nos trópicos”</b>: a sociedade colonial reproduz, adaptando, as hierarquias '
    'e os valores do Antigo Regime europeu — honra, qualidade, privilégio, serviço ao rei.',
    'Instituições-chave da autonomia local: <b>câmaras municipais</b> (“repúblicas”), '
    '<b>Santas Casas de Misericórdia</b>, irmandades, <b>ordens militares</b> (hábitos de Cristo), '
    'milícias.',
    '<b>Economia política do privilégio / economia da mercê</b>: o rei remunera serviços com '
    '<b>mercês</b> — cargos, hábitos, sesmarias, contratos de arrematação de tributos. '
    'Serviço → mercê → poder local → mais serviço. É assim que se forja a <b>“nobreza da terra”</b>: '
    'elites que descendem de conquistadores e primeiros povoadores e se nobilitam no Ultramar.',
    'O império funciona por <b>negociação</b>, não por imposição linear: a Coroa precisa das elites '
    'locais para governar e arrecadar; as elites precisam da Coroa para legitimar sua primazia. '
    'É uma <b>rede</b> — depois descrita por Fragoso como <b>monarquia pluricontinental</b>.',
])

S += note('Para a prova', [
    'Guarde o <b>par conceitual do título</b>: <i>materialidade</i> (mercado interno, acumulação '
    'endógena) + <i>governabilidade</i> (negociação, mercê, câmaras, nobreza da terra).',
    'É o contraponto direto ao “sentido da colonização”: onde Prado vê sociedade <b>sem nexo</b>, '
    'eles veem uma sociedade com <b>hierarquia, lógica e reprodução próprias</b>.',
    '<b>Crítica que se faz a eles:</b> risco de <b>diluir a exploração</b> — a escravidão e a '
    'drenagem de excedente podem ficar em segundo plano atrás da linguagem de “negociação” e '
    '“privilégio”.',
], GOLD)

S += rule()

# ===========================================================================
# 4. FAORO
# ===========================================================================
S += [P('4. Raimundo Faoro (1958)', 'H1x')]
S += [P('<i>Os Donos do Poder: formação do patronato político brasileiro</i> — '
        'cap. 1 “Origem do Estado português” e cap. 2 “A Revolução Portuguesa”', 'Smallx')]
S += [P(
    'Marco <b>weberiano</b>. A unidade de análise é o <b>Estado português</b> — e a tese é de '
    '<b>continuidade de longuíssima duração</b>: de D. João I ao Brasil do século XX.', 'Bodyx')]

S += [P('Cap. 1 — Origem do Estado português', 'H2x')]
S += bullets([
    'Portugal se forma na <b>Reconquista</b>: guerra, terra conquistada e <b>redistribuída pelo '
    'rei</b>. O rei é o grande senhor da terra e a <b>fonte</b> de direitos, não um '
    '<i>primus inter pares</i> entre barões.',
    'Por isso <b>não há feudalismo pleno</b>: existem formas jurídicas aparentadas (senhorios, '
    'doações), mas a <b>soberania não se fragmenta</b>; as terras <b>revertem</b> à Coroa e a '
    'jurisdição última é régia.',
    'Base da análise: <b>patrimonialismo</b> — o rei não distingue bem o patrimônio público do '
    'seu próprio; o Estado é a “casa” ampliada do soberano. Daí a tipologia weberiana: domínio '
    '<b>patrimonial</b> (e seu desdobramento, o <b>estamento burocrático</b>) em contraste com a '
    'dominação feudal e com a burocracia racional-legal.',
])

S += [P('Cap. 2 — A Revolução Portuguesa (1383-85, a Revolução de Avis)', 'H2x')]
S += bullets([
    'A crise dinástica e a aliança da monarquia com <b>setores urbanos e mercantis</b> (e parte da '
    'pequena nobreza) contra a alta nobreza castelhanizada consolidam um Estado '
    '<b>centralizado precocemente</b> — antes das demais monarquias nacionais.',
    'O resultado não é uma burguesia autônoma: o <b>Estado absorve o comércio</b>. A expansão '
    'marítima é <b>empresa régia</b> (Casa da Guiné, Casa da Índia), com <b>monopólios</b>, '
    'estancos e concessões.',
    'Conceito-chave (Weber): <b>capitalismo politicamente orientado</b> — o lucro depende do '
    '<b>favor do príncipe</b> (contratos, monopólios, cargos, privilégios), não da concorrência '
    'no mercado.',
    'O <b>estamento burocrático</b>: camada de letrados, oficiais e cortesãos que <b>se apropria '
    'do Estado</b> e vive dele, com ética e interesses próprios. Transplantado para a América, '
    'produz o <b>patronato político brasileiro</b> — a tese que dá nome ao livro.',
])

S += note('Para a prova — os confrontos', [
    '<b>A pergunta do programa é literal: “patrimonialismo ou feudalismo?”</b> Faoro responde '
    '<b>patrimonialismo</b>; a historiografia de matriz marxista (e boa parte dos lusitanistas) '
    'insiste em elementos <b>feudais/senhoriais</b> na estrutura agrária portuguesa.',
    '<b>Confronto obrigatório: Faoro × Fragoso et al.</b> Faoro vê o Estado estamental '
    '<b>de cima para baixo</b>, sufocando a sociedade; Fragoso et al. veem <b>negociação</b> e '
    'protagonismo das elites locais. Os dois usam o mesmo material (mercês, cargos, privilégio) '
    'e chegam a diagnósticos opostos sobre <i>quem manda</i>.',
    '<b>Confronto secundário: Faoro × Sérgio Buarque</b> (personalismo, cordialidade) — ambos '
    'buscam a “raiz” ibérica do Estado brasileiro, mas um pela via institucional-jurídica, '
    'outro pela via cultural.',
], GOLD)

# ===========================================================================
# 5. GODINHO
# ===========================================================================
S += rule()
S += [P('5. Vitorino Magalhães Godinho', 'H1x')]
S += [P('“A formação do Estado e as finanças públicas”, in <i>Ensaios e estudos. Uma maneira de '
        'pensar</i>. Lisboa: Sá da Costa, 2009, p. 123-173 — <b>leitura complementar</b>', 'Smallx')]
S += [P(
    'É o <b>lastro material</b> da discussão do ponto 2. Onde Faoro argumenta por tipos de '
    'dominação, Godinho vai às <b>contas da Coroa</b>.', 'Bodyx')]
S += bullets([
    'Pergunta: <b>com o que se paga</b> o Estado português? A resposta muda a natureza do Estado.',
    'Recomposição das <b>receitas régias</b>: direitos alfandegários, sisas, almoxarifados, '
    'monopólios (estancos), rendas das ordens militares, manipulação monetária '
    '(<b>quebra da moeda</b>), empréstimos.',
    'Tendência central: a Coroa desloca sua base das <b>rendas da terra</b> para as rendas do '
    '<b>comércio e da alfândega</b> — ouro da Guiné, açúcar, especiaria, direitos de entrada. '
    'O fisco <b>mercantiliza</b> o Estado.',
    'Daí a inversão do argumento: a expansão não é só apetite de glória ou de fé; é '
    '<b>necessidade fiscal</b>. O Estado precisa do comércio para sobreviver; o comércio precisa '
    'do Estado para se garantir militarmente. É um <b>Estado empresário</b>, mas estruturalmente '
    '<b>pressionado</b> — guerra, armadas, fortalezas, dívida.',
    'Godinho insiste também na <b>fragilidade</b> por trás da aparência imperial: receita '
    'insuficiente, déficit crônico, dependência de capital estrangeiro (genovês, flamengo, alemão) '
    '— o que prepara o retrato de Portugal como <b>metrópole pobre e intermediária</b> que Novais '
    'usará no século XVIII.',
])

S += note('Para a prova', [
    'Use Godinho para <b>sustentar com números</b> o que Faoro afirma com conceitos: o '
    '“capitalismo politicamente orientado” tem uma contabilidade. E para <b>qualificar</b> Faoro: '
    'o Estado não é onipotente, é <b>fiscalmente acossado</b> — tão dependente dos financistas '
    'quanto eles dele.',
], GOLD)

S += rule()

# ===========================================================================
# 6. NEVES
# ===========================================================================
S += [P('6. Eduardo Góes Neves (2022)', 'H1x')]
S += [P('<i>Sob os tempos do equinócio. Oito mil anos de história na Amazônia Central</i>. '
        'São Paulo: Ubu / EDUSP — cap. 2', 'Smallx')]
S += [P('A unidade de análise do slide — <b>“a floresta e quem a produziu”</b> — já é a tese.',
        'Bodyx')]
S += bullets([
    '<b>Rompe com o mito da natureza intocada</b> e com o <b>determinismo ambiental</b> — a tese '
    'clássica de Betty Meggers: solos pobres de terra firme → sociedades necessariamente pequenas, '
    'móveis e simples.',
    'Evidências arqueológicas na Amazônia Central (Manaus, foz do Negro, Iranduba, Hatahara):',
    '> <b>terras pretas de índio</b> (antrossolos férteis, formados por ocupação prolongada) — '
    'assinatura de sedentarismo e densidade;',
    '> <b>tradições cerâmicas</b> elaboradas e de longa duração, montículos, estruturas de terra, valas;',
    '> sítios <b>grandes e densos</b>, com ocupação contínua por séculos.',
    '<b>Domesticação de plantas e da paisagem</b>: mandioca, pupunha, cacau, castanha, açaí. '
    'Grande parte da floresta de hoje carrega <b>concentrações de espécies úteis</b> herdadas de '
    'manejo humano milenar → a floresta é, em medida significativa, <b>um produto histórico</b>, '
    'não um dado da natureza.',
    'Portanto: <b>oito mil anos de história</b>, com sociedades complexas, populosas e '
    'hierarquizadas <b>antes de 1492</b>, seguidas de <b>colapso demográfico</b> (epidemias, '
    'escravização, guerra) — o que <i>criou</i> a aparência de vazio que o colonizador descreveu '
    'e a historiografia naturalizou.',
    '<b>Complexidade sem Estado</b>: é aqui que entra o rodapé. <b>Sem cerco → sem '
    'circunscrição</b> (Carneiro, 1970). A terra aberta permite a fissão e a fuga; não há como '
    'converter vitória militar em sujeição permanente. Logo, adensamento e hierarquia <b>sem</b> o '
    'Estado coercitivo centralizado dos Andes ou do Vale do México.',
])

S += note('Função deste texto no programa (ponto 2.3)', [
    '“A presença humana no território da futura América Portuguesa”: <b>a história do Brasil não '
    'começa em 1500</b>. A “materialidade” da colônia inclui <b>plantas domesticadas, solos '
    'construídos, caminhos, conhecimento e trabalho indígenas</b> — sem os quais nem a ocupação '
    'nem a alimentação da empresa colonial funcionariam. Ligação direta com Schwartz, cap. 3, '
    'sobre a primeira escravidão.',
], LIGHT_GREEN, GREEN)

S += rule()

# ===========================================================================
# 7. SÍNTESE COMPARATIVA
# ===========================================================================
S += [P('7. Síntese comparativa e as três controvérsias', 'H1x')]
S += [P('Tabela de revisão dos seis autores', 'H2x')]
S += table([
    ['Autor', 'Escala', 'Motor da história', 'O que a colônia é', 'Ponto cego apontado pelos outros'],
    ['<b>Caio Prado</b>', 'Colônia no mundo', 'Mercado europeu / comércio',
     'Empresa de exportação', 'Mercado interno e dinâmica social própria'],
    ['<b>Novais</b>', 'Sistema colonial', 'Acumulação primitiva + exclusivo',
     'Peça funcional do sistema', 'Modelo muito dedutivo; pouca variação regional'],
    ['<b>Fragoso et al.</b>', 'Império / rede', 'Hierarquia, mercê, acumulação local',
     'Sociedade de Antigo Regime com elite própria', 'Risco de minimizar exploração e escravidão'],
    ['<b>Faoro</b>', 'Estado português', 'Patrimonialismo / estamento',
     'Extensão do patrimônio régio', 'Estado tratado como quase onipotente e a-histórico'],
    ['<b>Godinho</b>', 'Finanças da Coroa', 'Fisco e guerra',
     'Fonte de receita alfandegária', 'Economia política vista do centro, não da colônia'],
    ['<b>Neves</b>', 'Floresta / longa duração', 'Manejo humano do ambiente',
     'Território já densamente habitado e transformado',
     'Difícil de articular ao debate econômico colonial'],
], [2.6 * cm, 2.5 * cm, 3.5 * cm, 4.2 * cm, 4.9 * cm])

S += [P('Três controvérsias que podem virar questão dissertativa', 'H2x')]
S += bullets([
    '<b>1. Externalismo × internalismo</b> — o que explica a colônia: o mercado europeu '
    '(Prado, Novais) ou a lógica interna da sociedade colonial (Fragoso et al.)? '
    '<i>Resposta forte:</i> são <b>escalas complementares</b>; o exclusivo é a moldura, mas não '
    'determina a distribuição interna do excedente nem a reprodução das hierarquias locais.',
    '<b>2. Patrimonialismo × feudalismo</b> — Faoro (dominação patrimonial-estamental, Estado '
    'precoce e centralizado) × leituras que enfatizam estruturas senhoriais e, no caso de Godinho, '
    'a <b>restrição fiscal</b> que limita a Coroa.',
    '<b>3. Formação do Estado e circunscrição</b> — por que Portugal produz um Estado centralizado '
    'e as sociedades amazônicas não? Carneiro (1970) oferece o eixo: <b>cerco</b> (território '
    'delimitado + pressão + guerra) <i>vs.</i> <b>ausência de cerco</b> (possibilidade de fuga).',
])

S += [PageBreak()]

# ===========================================================================
# 8. PONTOS 3 A 6
# ===========================================================================
S += [P('8. Pontos 3 a 6 do programa (moldura essencial)', 'H1x')]

S += [P('Ponto 3 — O império português e o Brasil no Atlântico Sul (XIV-XVI)', 'H2x')]
S += bullets([
    '<b>Boxer</b>, <i>O império marítimo português</i>, cap. 1 (“O ouro da Guiné e o Preste João”): '
    'os móveis da expansão são <b>plurais</b> — ouro sudanês, cruzada e combate ao Islã, busca do '
    'aliado cristão <b>Preste João</b>, especiaria, honra cavaleiresca. Expansão como '
    '<b>cruzada que dá lucro</b>.',
    '<b>Zurara</b>, <i>Crónica da Guiné</i> (1453), cap. VII — <b>Fonte 1</b>: as “cinco razões” do '
    'Infante D. Henrique (conhecer as terras além do Cabo; comerciar com cristãos eventualmente lá '
    'existentes; medir a força do “infiel”; achar algum príncipe cristão aliado; salvar almas), '
    'mais a inclinação do Infante. Serve para discutir <b>mentalidade × economia</b>: a fonte '
    'justifica em linguagem religiosa-cavaleiresca o que a historiografia lê como projeto mercantil.',
    '<b>Thomaz</b>, “D. Manuel, a Índia e o Brasil” (2009): o projeto de D. Manuel é <b>imperial e '
    'messiânico</b> (título de “Senhor da conquista, navegação e comércio da Etiópia, Arábia, '
    'Pérsia e Índia”, reconquista de Jerusalém), e dentro dele o <b>Brasil é periférico</b> — o que '
    'explica a ocupação tardia e barata (feitorias, pau-brasil, capitanias) antes do açúcar.',
    '<b>Alencastro</b>, <i>O trato dos viventes</i> (2000), Prefácio e cap. 1: o Brasil <b>não se '
    'forma dentro de suas fronteiras</b>. Forma-se no <b>Atlântico Sul</b>, numa articulação '
    '<b>bipolar Brasil–Angola</b>: a colônia americana depende do tráfico, e o tráfico organiza '
    'uma <b>“colônia da colônia”</b> na África Central. O negócio estruturante é o <b>trato dos '
    'viventes</b> — o comércio de seres humanos. A elite senhorial brasileira é <b>agente</b>, não '
    'espectadora, dessa engrenagem.',
    '<b>Base Voyages</b> (slavevoyages.org): ordem de grandeza para citar — cerca de '
    '<b>12,5 milhões</b> de africanos <b>embarcados</b> no tráfico transatlântico (c. 1514-1866), '
    'aproximadamente <b>10,7 milhões desembarcados</b> (a diferença é a mortalidade da travessia), '
    'e o <b>Brasil como maior destino único da história do tráfico</b>, com praticamente '
    '<b>metade do total</b> (as estimativas correntes ficam na faixa de 4,9 a 5,5 milhões, conforme '
    'o recorte). A base é periodicamente revista: na prova, apresente como <b>estimativa</b> e '
    'indique a fonte.',
])

S += [P('Ponto 4 — Economia e sociedade no Brasil colonial', 'H2x')]
S += bullets([
    '<b>Schwartz</b>, <i>Segredos internos</i>, cap. 3 (“Primeira escravidão: do indígena ao '
    'africano”): a transição <b>não é automática nem instantânea</b>; é processo de décadas '
    '(Bahia, c. 1570-1700) movido por <b>colapso demográfico indígena</b> (epidemias de 1562-63), '
    '<b>fuga e resistência</b>, <b>legislação e pressão jesuítica</b>, e pela <b>economia da '
    'oferta</b> de cativos africanos — preço, crédito, qualificação técnica no açúcar, '
    'impossibilidade de fuga para um território conhecido. Houve longo período de <b>mão de obra '
    'mista</b>.',
    '<b>Schwartz</b>, cap. 9 (“Uma sociedade escravista colonial”): a Bahia é uma <b>sociedade '
    'escravista</b>, não apenas uma sociedade <i>com</i> escravos — a escravidão define hierarquia, '
    'direito, família, religião e política. Eixos sobrepostos: <b>condição jurídica</b> '
    '(livre/liberto/escravo), <b>cor e qualidade</b>, <b>ocupação</b>. O <b>engenho</b> é a unidade '
    'produtiva e social; os <b>senhores de engenho</b> operam como nobreza; abaixo, '
    '<b>lavradores de cana</b>, artesãos, livres pobres.',
    '<b>Gilberto Freyre</b>, <i>Casa Grande e Senzala</i>, cap. I: colonização portuguesa marcada '
    'por <b>plasticidade, mobilidade e miscibilidade</b> (bicontinentalidade ibérica, experiência '
    'africana prévia); daí uma sociedade <b>agrária, escravocrata e híbrida</b>, organizada na '
    '<b>família patriarcal</b> e na casa-grande. Valoriza a <b>mestiçagem</b> como força. '
    '<b>Crítica obrigatória:</b> a leitura <b>harmoniza</b> a violência da escravidão e alimenta o '
    'mito da “democracia racial”.',
    '<b>Sérgio Buarque de Holanda</b>, <i>Raízes do Brasil</i>, caps. 1-2 (complementar): '
    '“Fronteiras da Europa” — a herança <b>ibérica</b> (personalismo, frouxidão das hierarquias '
    'impessoais, cultura da personalidade); “Trabalho e aventura” — a oposição <b>semeador × '
    'ladrilhador</b>: o português do tipo <b>aventureiro</b> (resultado imediato, pouco método) '
    'contra o colono <b>ordenado</b> da América espanhola e inglesa. Fundamenta a tese do '
    '<b>predomínio do rural</b> e do personalismo na formação brasileira.',
    '<b>Fontes 2 e 3</b> — ótimas para questão de documento:',
    '> <b><i>Diálogos das Grandezas do Brasil</i></b> (1618, atribuído a Ambrósio Fernandes '
    'Brandão): diálogo entre <b>Brandônio</b> (entusiasta, residente) e <b>Alviano</b> (cético, '
    'recém-chegado) — um <b>inventário elogioso</b> das riquezas: açúcar e engenhos, pau-brasil, '
    'algodão, fertilidade, possibilidades de enriquecimento. É <b>apologia</b> e, ao mesmo tempo, '
    'descrição técnica da economia açucareira.',
    '> <b>Frei Vicente do Salvador</b>, <i>História do Brasil</i> (1627): o contraponto '
    '<b>crítico</b>. Os colonos usam a terra “não como senhores, mas como usufrutuários”, vivendo '
    'como se estivessem de passagem — a imagem célebre dos que se contentam de <b>“andar '
    'arranhando a terra como caranguejos”</b>, voltados para a costa e para o reino. Fonte canônica '
    'para discutir <b>ausência de projeto de povoamento</b> — e, portanto, o “sentido” de Caio '
    'Prado dito por um contemporâneo.',
])

S += [P('Ponto 5 — Entre a Restauração e a crise do Antigo Regime (1640-1808)', 'H2x')]
S += bullets([
    '<b>Puntoni</b>, “Os holandeses no comércio colonial e a conquista do Brasil”: antes da invasão, '
    'os <b>holandeses já eram peça do circuito</b> do açúcar (frete, refino, distribuição, crédito). '
    'A <b>WIC</b> ataca a fonte: Bahia (1624-25) e <b>Pernambuco (1630-1654)</b>, além de '
    '<b>Angola (1641-1648)</b>, porque açúcar e cativos são o mesmo negócio. Inserir no quadro da '
    '<b>crise geral do século XVII</b>. Consequências duradouras: difusão da <b>tecnologia '
    'açucareira</b> para as <b>Antilhas</b>, queda dos preços, perda da primazia brasileira, e uma '
    'Coroa restaurada (<b>1640</b>) que precisa reorganizar fisco, defesa e comércio '
    '(companhias de comércio, frotas).',
    '<b>Furtado</b>, <i>Formação Econômica do Brasil</i>, parte sobre a <b>economia escravista '
    'mineira</b>: o ouro desloca o centro econômico para o <b>Centro-Sul</b>, provoca '
    '<b>urbanização</b>, uma distribuição de renda <b>menos concentrada</b> (mineração de aluvião, '
    'faiscadores, escravos de ganho, possibilidade de alforria), alta <b>monetização</b> e um '
    '<b>mercado interno</b> articulado pelo abastecimento (tropas de muares, gado do Sul e do '
    'Nordeste, roças). Mas, esgotado o aluvião, não há conversão em atividade autossustentada: '
    '<b>regressão à economia de subsistência</b> e dispersão demográfica.',
    '<b>Antonil</b>, <i>Cultura e Opulência do Brasil por suas Drogas e Minas</i> (1711) — '
    '<b>Fonte 4</b>: o grande manual descritivo (açúcar, tabaco, gado, ouro), com dados de '
    'produção, custos e organização do engenho. <b>Recolhido pela Coroa</b> logo após a publicação '
    '— a riqueza descrita era informação estratégica. Fonte ideal para discutir <b>segredo, fisco '
    'e controle colonial</b>.',
    '<b>Sublevação de 1720</b> (<i>Discurso histórico e político...</i>, org. Laura de Mello e '
    'Souza) — <b>Fonte 6</b>: a revolta de <b>Vila Rica (Filipe dos Santos)</b> contra as '
    '<b>casas de fundição</b> e a cobrança do quinto. O “Discurso” é texto <b>político</b>: '
    'legitima a repressão do <b>Conde de Assumar</b>. Serve para analisar a tensão entre '
    '<b>potentados locais</b> e <b>autoridade régia</b> — exatamente o tema da <i>governabilidade</i> '
    'de Fragoso et al., agora no limite do conflito.',
    '<b>Cardoso</b> (2011), “Discurso econômico e política colonial no império luso-brasileiro '
    '(1750-1808)”: a <b>ilustração luso-brasileira</b> e a formação de um discurso de '
    '<b>economia política</b> que pensa o império como <b>unidade a ser reformada</b> — não mais o '
    'exclusivo puro, mas a articulação produtiva entre as partes.',
    '<b>D. Rodrigo de Souza Coutinho</b>, “Memória sobre o melhoramento dos domínios de Sua '
    'Majestade na América” (1797/98) — <b>Fonte 5</b>: o programa reformista. Portugal e seus '
    'domínios como <b>um só império</b> e uma só nação; o <b>Brasil é a parte mais valiosa</b> do '
    'conjunto; propostas de reforma fiscal, estímulo à agricultura e à circulação interna, obras, '
    'ciência útil, integração dos domínios. É a tentativa <b>de dentro</b> de salvar o império na '
    'crise — e, lida com Novais, a prova de que os contemporâneos <b>percebiam</b> o esgotamento '
    'do sistema.',
    '<b>Carrara et al.</b> (2023), “The Brazilian Economy during the Old Regime Crisis (1750-1807)”, '
    '<i>Revista de Historia Económica</i> 41(1): reconstrução <b>quantitativa</b> da economia '
    'colonial tardia. Resultado que importa para a prova: o setor <b>doméstico / de '
    'abastecimento</b> é muito maior do que a historiografia clássica supunha em relação às '
    'exportações, e há <b>crescimento</b> no período — revisão empírica da ênfase exclusiva na '
    'exportação (Prado) e da tese de estagnação pós-ouro (Furtado), convergente com a '
    '“materialidade” de Fragoso et al.',
    '<b>1808</b>: transferência da corte; <b>abertura dos portos (28 de janeiro de 1808)</b>; '
    'alvará de liberdade industrial (1808); tratados de <b>1810</b> com a Grã-Bretanha (tarifa '
    'preferencial de 15%). O <b>exclusivo acaba de fato</b> — a crise do Antigo Sistema Colonial se '
    'resolve, no caso luso-brasileiro, por <b>inversão</b> (a metrópole se muda para a colônia) '
    'antes de se resolver por independência.',
])

S += [P('Ponto 6 — Estado-nação e economia capitalista (fins do XVIII-XIX)', 'H2x')]
S += bullets([
    '<b>Emília Viotti da Costa</b>, “Introdução ao estudo da emancipação política”: a Independência '
    'é <b>processo</b>, não ato; conduzida <b>pelas elites</b> e para preservar a ordem — '
    '<b>continuidade</b> da escravidão, do latifúndio e da monocultura de exportação. Há '
    '<b>ruptura política</b> sem <b>ruptura socioeconômica</b>; os interesses são '
    '<b>regionalmente divergentes</b> (Rio/Centro-Sul × Nordeste × Norte), e o medo da desordem '
    'social explica o desenho conservador do novo Estado.',
    '<b>Bernardo Pereira de Vasconcelos</b>, <i>Carta aos senhores eleitores da província de Minas '
    'Gerais</i> (1827) — <b>Fonte 7</b>: a plataforma de um liberalismo <b>de elite</b> — governo '
    'representativo, legalidade, liberdade de imprensa, limites ao Executivo e crítica ao arbítrio '
    '—, combinada com defesa intransigente da <b>ordem</b> e da <b>propriedade</b>. Vasconcelos é a '
    'figura que encarna a trajetória <b>do liberalismo ao Regresso</b> conservador dos anos 1830-40.',
    '<b>Wilma Peres Costa</b>, “A economia mercantil escravista nacional e o processo de construção '
    'do Estado no Brasil (1808-1850)”: a construção do Estado é um <b>problema fiscal e '
    'territorial</b>. O Estado nasce com encargos herdados (dívida, aparato de corte, guerras), e '
    'sua receita depende esmagadoramente de <b>direitos de importação</b> — ou seja, da própria '
    'economia de exportação e do comércio atlântico. Daí: tensão <b>centro × províncias</b> '
    '(crise regencial, revoltas), reconstrução centralizadora, <b>tarifa Alves Branco (1844)</b> e '
    'consolidação do núcleo <b>mercantil-escravista do Rio de Janeiro</b>. A classificação é '
    'precisa: economia <b>mercantil escravista nacional</b> — mercantil e escravista como antes, '
    'mas agora <b>nacional</b>, com um Estado próprio a ser financiado.',
    '<b>Tamis Parron</b>, <i>A política da escravidão no Império do Brasil (1826-1865)</i>, cap. '
    '“Grã-Bretanha, hegemonia saquarema e contrabando: um Brasil todo africano”: a escravidão é '
    '<b>política de Estado</b>, não inércia. Sequência: tratado de 1826 e <b>lei de 1831</b> '
    '(que proíbe o tráfico e se torna “<b>para inglês ver</b>”) → <b>contrabando massivo</b> nos '
    'anos 1830-40, financiando a expansão cafeeira do Vale do Paraíba → <b>Bill Aberdeen (1845)</b> '
    'e pressão naval britânica → <b>hegemonia saquarema</b> (o partido conservador do Rio '
    'articulando café, tráfico e Estado) → <b>lei Eusébio de Queirós (1850)</b>, que encerra o '
    'tráfico quando ele passa a ameaçar a própria ordem (pressão externa, risco de africanização e '
    'de insurreição, redirecionamento do capital).',
    '<b>Quantitativo (6.2)</b> a ter na cabeça: ascensão do <b>café</b> a principal produto de '
    'exportação a partir dos anos 1830; permanência de açúcar e algodão; enorme volume de '
    '<b>entradas de africanos</b> nas décadas de 1830 e 1840 (contrabando); primazia do porto do '
    '<b>Rio de Janeiro</b>; após 1850, o capital do tráfico migra para o <b>tráfico interno '
    'interprovincial</b>, crédito e infraestrutura.',
])

S += [PageBreak()]

# ===========================================================================
# 9. ROTEIRO DE REVISÃO
# ===========================================================================
S += [P('9. Roteiro de revisão em 10 frases', 'H1x')]
S += table([
    ['#', 'Se sobrar pouco tempo, leia só isto'],
    ['1', '<b>Caio Prado:</b> a colônia existe para o mercado europeu — grande lavoura, latifúndio, '
          'escravidão, economia voltada para fora.'],
    ['2', '<b>Novais:</b> isso é um <i>sistema</i> de acumulação primitiva cujo coração é o '
          '<b>exclusivo metropolitano</b>, e cuja maturação <b>o destrói</b>.'],
    ['3', '<b>Fragoso, Bicalho &amp; Gouvêa:</b> mas dentro da colônia há <b>mercado interno, '
          'acumulação própria e uma elite nobilitada</b> — um Antigo Regime nos trópicos, governado '
          'por <b>negociação e mercê</b>.'],
    ['4', '<b>Faoro:</b> tudo isso é possível porque o <b>Estado português</b> é patrimonial e '
          'precoce (Avis, 1383-85), com um <b>estamento</b> que se apropria do público e pratica '
          '<b>capitalismo politicamente orientado</b>.'],
    ['5', '<b>Godinho:</b> e esse Estado se sustenta no <b>fisco do comércio</b> — logo a expansão '
          'é também <b>necessidade financeira</b>, num Estado cronicamente endividado.'],
    ['6', '<b>Neves:</b> antes de tudo, o território já tinha <b>oito mil anos de história</b> e uma '
          'floresta <b>em parte produzida</b> por sociedades complexas — que, <b>sem cerco</b> '
          '(Carneiro, 1970), não geraram Estado coercitivo.'],
    ['7', '<b>Alencastro:</b> a formação do Brasil se dá no <b>Atlântico Sul</b>, com Angola como a '
          'outra margem obrigatória.'],
    ['8', '<b>Schwartz:</b> a passagem do cativo indígena ao africano é lenta e produz uma '
          '<b>sociedade escravista</b> integral.'],
    ['9', '<b>Furtado × Carrara:</b> o ouro cria mercado interno e depois reflui — mas a '
          'quantificação recente mostra uma economia interna <b>maior e mais dinâmica</b> do que a '
          'tese da estagnação admitia.'],
    ['10', '<b>Viotti, Wilma Costa, Parron:</b> a Independência conserva a escravidão e o latifúndio; '
           'o novo Estado é financiado pelo comércio atlântico e <b>defende politicamente</b> o '
           'tráfico até 1850.'],
], [1.1 * cm, 16.6 * cm])

# ===========================================================================
# 10. FONTES PRIMÁRIAS
# ===========================================================================
S += rule()
S += [P('10. Checklist das fontes primárias', 'H1x')]
S += table([
    ['Fonte', 'Documento', 'Serve para discutir'],
    ['1', 'Zurara, <i>Crónica do descobrimento e conquista de Guiné</i> (1453), cap. VII',
     'Móveis da expansão: fé, honra e lucro'],
    ['2', '<i>Diálogos das Grandezas do Brasil</i> (1618)',
     'Apologia e descrição da economia açucareira'],
    ['3', 'Frei Vicente do Salvador, <i>História do Brasil</i> (1627)',
     'Crítica à ausência de povoamento; “arranhar a terra como caranguejos”'],
    ['4', 'Antonil, <i>Cultura e Opulência do Brasil</i> (1711)',
     'Engenho, ouro, fisco e segredo de Estado'],
    ['5', 'D. Rodrigo de Souza Coutinho, <i>Memória sobre o melhoramento dos domínios</i> (1797/98)',
     'Reformismo ilustrado; o império como unidade'],
    ['6', '<i>Discurso histórico e político sobre a sublevação que nas Minas houve no ano de 1720</i>',
     'Potentados locais × autoridade régia'],
    ['7', 'Vasconcelos, <i>Carta aos senhores eleitores</i> (1827)',
     'Liberalismo de elite; ordem e propriedade'],
], [1.4 * cm, 8.3 * cm, 8.0 * cm])

S += [Spacer(1, 0.4 * cm)]
S += [P(
    'Resumo elaborado a partir do programa da disciplina e do slide “Seis autores, uma linha” '
    '(print <font face="DejaVuSans-Italic">20260924_165705.jpg</font>). As indicações bibliográficas '
    'seguem as edições listadas no programa. Dados do tráfico transatlântico: Voyages — The '
    'Transatlantic Slave Trade Database, Universidade de Emory (slavevoyages.org). Teoria da '
    'circunscrição: R. Carneiro, “A Theory of the Origin of the State”, Science 169(3947), 1970.',
    'Smallx')]


# ===========================================================================
if __name__ == '__main__':
    build_pdf(SAIDA, S,
              title='Resumo P1 — Formação Econômica do Brasil',
              left_title='FORMAÇÃO ECONÔMICA DO BRASIL — RESUMO P1',
              right_title='Seis autores, uma linha',
              footer_note='Material de estudo — Prova 1')
    print('PDF gerado:', SAIDA)
