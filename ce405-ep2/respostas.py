# -*- coding: utf-8 -*-
"""
Conteúdo das respostas da Lista de Questões I de Economia Política II (CE405, turma C, 2025).

Referência: MARX, Karl. O Capital, Livro I. São Paulo: Boitempo. A numeração dos
capítulos (4, 5, 6, 7, 9, 10, 13, 21, 22, 23, 24) segue a edição Boitempo.

Estrutura dos dados
  RESPOSTAS é uma lista de dicionários, um por questão, com as chaves:
    'depois'  índice do parágrafo do .docx original após o qual a resposta entra
    'rotulo'  cabeçalho da resposta
    'blocos'  lista de tuplas (tipo, conteudo), onde tipo é:
                'h'  subtítulo
                'p'  parágrafo corrido
                'b'  item de lista
                'd'  item de lista com rótulo em negrito ('Rótulo||texto')
                't'  tabela, conteúdo = lista de linhas, a primeira é o cabeçalho

Marcação inline: **negrito** e *itálico*.
"""

RESPOSTAS = [

# ===================================================================== cap. 4
{
 'depois': 4,
 'rotulo': 'Resposta 1 (cap. 4, "A transformação do dinheiro em capital")',
 'blocos': [
  ('p', 'A exposição parte da forma de troca já analisada nos capítulos anteriores e '
        'mostra que ela contém uma segunda forma, qualitativamente distinta, na qual o '
        'dinheiro deixa de ser simples mediador e passa a ser o sujeito do movimento. A '
        'diferença entre as duas formas não é de grau nem de volume, é de finalidade e de '
        'estrutura.'),

  ('h', '1. A circulação simples de mercadorias (M–D–M)'),
  ('d', 'Extremos||Ponto de partida e ponto de chegada são mercadorias, isto é, valores de '
        'uso qualitativamente diferentes. Quem vende trigo para comprar roupa realiza M–D–M.'),
  ('d', 'Papel do dinheiro||Funciona como meio de circulação, intermediário evanescente. É '
        'gasto definitivamente e não retorna ao ponto de partida.'),
  ('d', 'Finalidade||A troca de valores de uso. O fim está *fora* da circulação, no consumo, '
        'na satisfação de uma necessidade determinada.'),
  ('d', 'Relação entre os extremos||São quantitativamente equivalentes em valor e '
        'qualitativamente distintos em utilidade. É justamente a diferença qualitativa que '
        'dá sentido à operação, pois trocar trigo por trigo seria absurdo.'),
  ('d', 'Limite||O movimento tem limite interno. Satisfeita a necessidade, ele se encerra. A '
        'repetição depende de uma nova necessidade, e as necessidades são finitas.'),
  ('d', 'Comportamento do valor||O valor se conserva, não se amplia. Ganhos ocasionais por '
        'troca desigual são acidentais e não constituem a lógica da forma.'),

  ('h', '2. A circulação do dinheiro como capital (D–M–D\')'),
  ('d', 'Extremos||Ponto de partida e de chegada são dinheiro. Compra-se para vender, e não '
        'se vende para comprar. Agora é a mercadoria que se torna o intermediário, numa '
        'inversão exata dos papéis.'),
  ('d', 'Relação entre os extremos||São qualitativamente idênticos, ambos dinheiro, valor na '
        'sua forma universal. Por isso só podem diferir em *quantidade*. Um movimento '
        'D–M–D que terminasse com a mesma soma seria tautológico e sem motivo algum.'),
  ('d', 'O incremento||Logo, a forma só tem sentido se o retorno exceder o adiantamento, '
        'D\' = D + ΔD. Esse incremento é o que Marx chama **mais-valor** (*Mehrwert*).'),
  ('d', 'Destino do dinheiro||Ele é apenas *adiantado*, não gasto. Reflui ao ponto de partida '
        'acrescido. É essa diferença que separa o capitalista tanto do consumidor da '
        'circulação simples quanto do entesourador, que retira o dinheiro da circulação.'),
  ('d', 'Finalidade||Interna ao próprio movimento, é a valorização do valor. O valor de uso '
        'aparece apenas como portador necessário do valor, nunca como fim.'),
  ('d', 'Limite||Não há limite interno. Como o fim é a quantidade de valor, e quantidade não '
        'tem medida qualitativa de saciedade, o processo é em princípio infinito. D\' é '
        'apenas o ponto de partida de um novo ciclo. A acumulação sem fim não é vício moral '
        'do capitalista, é a forma objetiva do movimento.'),

  ('h', '3. Quadro comparativo'),
  ('t', [
    ['Critério', 'M–D–M (circulação simples)', 'D–M–D\' (dinheiro como capital)'],
    ['Extremos', 'Mercadoria', 'Dinheiro'],
    ['Intermediário', 'O dinheiro medeia', 'A mercadoria medeia'],
    ['Extremos entre si', 'Qualitativamente distintos', 'Qualitativamente idênticos, diferem em quantidade'],
    ['Finalidade', 'Valor de uso, consumo', 'Valor de troca, valorização'],
    ['Dinheiro', 'Gasto, não retorna', 'Adiantado, reflui acrescido'],
    ['Limite', 'Finito, dado pela necessidade', 'Tendencialmente infinito'],
    ['Sujeito do movimento', 'O produtor que consome', 'O valor que se valoriza'],
  ]),

  ('h', '4. A maneira como Marx introduz a categoria de capital'),
  ('d', 'Pela forma, não pela matéria||A introdução é metodologicamente decisiva. Capital não '
        'é definido como um conjunto de coisas (dinheiro, máquinas, estoques), e sim como um '
        'movimento, uma forma de circulação determinada. D–M–D\' é apresentada como a '
        'fórmula geral do capital tal como ele aparece imediatamente na esfera da circulação.'),
  ('d', 'Valor em processo||O capital é valor que se valoriza. O valor se torna "sujeito '
        'automático" do movimento, assumindo e abandonando alternadamente as formas dinheiro '
        'e mercadoria, conservando-se e ampliando-se nessas metamorfoses.'),
  ('d', 'O capitalista é derivado da forma||Ele não é o ponto de partida da definição, é o '
        'portador consciente do movimento, o capital personificado. Seu fim subjetivo '
        'coincide com o fim objetivo da forma, o enriquecimento abstrato.'),
  ('d', 'Exposição deliberadamente provisória||Marx apresenta D–M–D\' como ela se mostra na '
        'superfície, para em seguida demonstrar que, mantida no plano da circulação, essa '
        'forma é contraditória, pois ΔD não pode ser explicado pela troca. É esse impasse '
        'que exige a passagem à esfera da produção e a descoberta da mercadoria força de '
        'trabalho, objeto da questão seguinte.'),
  ('d', 'A forma mais mistificada||O capital portador de juros, D–D\', é mencionado como a '
        'forma abreviada em que a mediação produtiva desaparece por completo e o dinheiro '
        'parece gerar dinheiro por natureza própria, como a pereira dá peras.'),
 ],
},

{
 'depois': 8,
 'rotulo': 'Resposta 2 (cap. 4). A contradição e a mercadoria força de trabalho',
 'blocos': [
  ('h', '1. Primeiro termo. O mais-valor não pode ter origem na circulação'),
  ('p', 'Marx examina a circulação supondo a troca de equivalentes. Se as mercadorias se '
        'trocam pelos seus valores, a circulação é mera metamorfose de forma, o mesmo valor '
        'passando de mercadoria a dinheiro e de dinheiro a mercadoria. Nenhuma grandeza de '
        'valor é criada, a soma total permanece a mesma. Ele então testa as hipóteses de '
        'troca desigual, e todas falham.'),
  ('d', 'Aumento geral dos preços||Se todos os vendedores vendem 10% acima do valor, todos '
        'também compram 10% acima. O ganho nominal se anula, pois cada um é alternadamente '
        'vendedor e comprador. Trata-se de mudança de denominação, não de grandeza.'),
  ('d', 'Vendedor privilegiado||Se alguém vende sistematicamente acima do valor, ele ganha, '
        'mas o comprador perde exatamente o mesmo. Há transferência de valor, não criação. O '
        'que um ganha, o outro perde.'),
  ('d', 'Fraude e monopólio comercial||Explicam fortunas individuais pela redistribuição de '
        'valor preexistente, mas não explicam como a *classe* capitalista em conjunto se '
        'enriquece, pois ela não pode enriquecer trocando consigo mesma.'),
  ('p', 'Conclusão parcial. Considerada em si mesma, a circulação é estéril do ponto de vista '
        'da criação de valor.'),

  ('h', '2. Segundo termo. O mais-valor tampouco pode ter origem fora da circulação'),
  ('d', 'Isolamento do produtor||Fora da circulação, o possuidor de mercadoria se relaciona '
        'apenas com a sua própria mercadoria. Pelo seu trabalho ele pode criar valor novo, '
        'mas não mais-valor, porque não existe aí nenhuma relação pela qual trabalho alheio '
        'não pago possa ser apropriado.'),
  ('d', 'O capitalista não trabalha||O incremento não é produzido por trabalho próprio do '
        'possuidor de dinheiro. E o valor criado em isolamento privado não é sequer valor em '
        'sentido pleno, pois o valor só se valida socialmente na troca.'),
  ('d', 'A circulação é indispensável||O capital precisa necessariamente passar por ela, pois '
        'é nela que compra os seus elementos e é nela que o mais-valor se realiza em '
        'dinheiro. Sem venda, não há D\'.'),
  ('p', 'Daí a formulação do enunciado. O capital tem de ter origem na circulação e, ao mesmo '
        'tempo, não ter origem nela. A solução não pode negar nenhum dos dois termos, '
        'precisa articulá-los, localizando a criação do excedente fora da troca sem '
        'dispensar a troca.'),

  ('h', '3. A solução pela mercadoria força de trabalho'),
  ('p', 'A saída consiste em identificar, dentro da circulação e respeitando integralmente a '
        'lei do valor, uma mercadoria cujo consumo, que ocorre fora da circulação, produza '
        'mais valor do que ela própria vale.'),
  ('d', 'A distinção fundadora||O capitalista não compra trabalho, compra **força de '
        'trabalho**, a capacidade de trabalhar. Trabalho é atividade, dispêndio efetivo, e '
        'como tal não tem valor, ele *é* a substância do valor. Força de trabalho é a '
        'capacidade de exercer essa atividade, e essa capacidade é uma mercadoria com valor '
        'determinado. Toda a solução repousa nessa distinção.'),
  ('d', 'O valor da força de trabalho||É determinado como o de qualquer mercadoria, pelo '
        'tempo de trabalho socialmente necessário à sua produção e reprodução, ou seja, pelo '
        'valor dos meios de subsistência necessários para manter o trabalhador apto e '
        'reproduzir a sua família. Nessa determinação entra um elemento histórico e moral, '
        'pois o que conta como necessário varia com o grau de civilização e com as '
        'conquistas da luta de classes.'),
  ('d', 'A compra é legítima||Ela se dá na circulação e paga o valor integral da mercadoria. '
        'Não há fraude, nem troca desigual, nem violação da equivalência. Esse ponto é '
        'essencial, a exploração não depende de nenhuma irregularidade na troca.'),
  ('d', 'O valor de uso peculiar||Consumir força de trabalho significa pôr o trabalhador a '
        'trabalhar, e trabalho é criação de valor. É a única mercadoria cujo valor de uso '
        'consiste em ser fonte de valor.'),
  ('d', 'A independência das duas grandezas||O valor pago depende do custo de reprodução do '
        'trabalhador. O valor criado depende da duração e da intensidade da jornada '
        'efetivamente trabalhada. São determinações independentes, e nada na equivalência da '
        'troca fixa a jornada no ponto em que o trabalhador apenas repõe o valor da sua '
        'força de trabalho.'),
  ('p', 'Ilustração numérica. Se o valor diário da força de trabalho corresponde a 6 horas de '
        'trabalho, o capitalista paga esse equivalente e adquire o direito de usá-la pela '
        'jornada contratada, digamos 12 horas. Nas primeiras 6 horas o trabalhador produz o '
        'equivalente ao próprio salário, é o tempo de trabalho necessário. Nas 6 horas '
        'restantes ele continua criando valor sem contrapartida, é o tempo de trabalho '
        'excedente, fonte do mais-valor.'),
  ('p', 'O resultado articula os dois termos da contradição. A compra e a venda ocorrem na '
        'circulação, por isso o capital tem origem nela. A criação do mais-valor ocorre na '
        'produção, no consumo da mercadoria comprada, por isso o capital não tem origem na '
        'circulação. A contradição se resolve porque a circulação fornece precisamente a '
        'mercadoria cujo uso, fora dela, gera o excedente.'),

  ('h', '4. Os pressupostos históricos da solução'),
  ('d', 'Liberdade jurídica||O trabalhador deve ser proprietário da sua própria capacidade de '
        'trabalho e vendê-la por tempo determinado. Vendê-la de uma vez por todas o tornaria '
        'escravo, e à mercadoria faltaria o vendedor.'),
  ('d', 'Despossessão||Ele deve estar separado dos meios de produção e dos meios de '
        'subsistência, de modo que vender a força de trabalho seja a única via de acesso ao '
        'que precisa para viver.'),
  ('d', 'Caráter histórico||Essas condições não são naturais, são resultado de um processo '
        'violento de expropriação, o que remete à acumulação primitiva do cap. 24.'),
  ('p', 'Marx fecha o capítulo com a ironia sobre a saída da esfera da circulação, o éden dos '
        'direitos inatos do homem, onde reinam liberdade, igualdade e propriedade, para '
        'entrar na produção, cuja porta traz o aviso de que ali só se entra a negócios. A '
        'igualdade formal da troca é perfeitamente compatível com a exploração material na '
        'produção, e é justamente ela que a torna possível e a oculta.'),
 ],
},

# ===================================================================== cap. 5
{
 'depois': 12,
 'rotulo': 'Resposta 3 (cap. 5, "Processo de trabalho e processo de valorização")',
 'blocos': [
  ('p', 'O capítulo articula as cinco categorias em torno de um eixo, o **duplo caráter do '
        'trabalho** estabelecido no cap. 1. O processo de produção capitalista é a unidade de '
        'duas determinações do mesmo ato, e cada categoria da questão pertence a um desses '
        'dois níveis.'),

  ('h', '1. O processo de trabalho'),
  ('d', 'Nível de abstração||Marx o examina primeiro independentemente de qualquer forma '
        'social determinada, como condição eterna da vida humana, metabolismo entre o homem '
        'e a natureza. Ele existe em toda sociedade, e não apenas no capitalismo.'),
  ('d', 'Os três momentos simples||A atividade orientada a um fim, isto é, o trabalho '
        'propriamente dito. O objeto de trabalho, matéria bruta ou matéria-prima. Os meios '
        'de trabalho, instrumentos pelos quais o trabalhador atua sobre o objeto. Objeto e '
        'meios formam os meios de produção.'),
  ('d', 'O resultado||O trabalho se objetiva. O trabalho vivo, atividade em fluxo, converte-se '
        'em trabalho morto, fixado no produto. O produto é um **valor de uso**.'),
  ('d', 'Determinação do trabalho aqui||Ele conta como trabalho concreto e útil, '
        'qualitativamente determinado (fiar, tecer, forjar). É por ser trabalho útil '
        'determinado que ele consegue consumir produtivamente aqueles meios de produção '
        'específicos e produzir aquele valor de uso específico.'),

  ('h', '2. O processo de valorização'),
  ('d', 'Subordinação do processo de trabalho||Sob a forma capitalista, o processo de trabalho '
        'é apenas o meio. O fim é a produção de valor e, mais precisamente, de mais-valor. O '
        'capitalista não produz para satisfazer necessidades, produz mercadorias para vender '
        'com acréscimo.'),
  ('d', 'Determinação do trabalho aqui||Ele conta como trabalho abstrato, dispêndio de força '
        'humana de trabalho em geral, indiferente à forma concreta e por isso mensurável '
        'apenas pelo tempo. É nessa determinação que ele cria **valor**.'),
  ('d', 'Formação de valor e valorização||Marx distingue dois graus do mesmo processo. O '
        'processo de formação de valor é o processo enquanto o trabalho vivo apenas cria '
        'valor novo. O processo de valorização é esse mesmo processo prolongado além do '
        'ponto em que o valor criado basta para repor o valor da força de trabalho. A '
        'valorização é, na formulação de Marx, o processo de formação de valor prolongado '
        'além de certo ponto.'),
  ('d', 'Decomposição do valor do produto||Valor dos meios de produção consumidos, conservado '
        'e transferido, mais valor novo criado pelo trabalho vivo. Se o valor novo excede o '
        'valor da força de trabalho, há mais-valor.'),

  ('h', '3. A dupla função do mesmo trabalho'),
  ('t', [
    ['Determinação do trabalho', 'O que produz', 'Efeito sobre o valor'],
    ['Trabalho concreto, útil',
     'Valor de uso, o produto',
     'Conserva e transfere ao produto o valor dos meios de produção, ao usá-los conforme a sua finalidade'],
    ['Trabalho abstrato, medido pelo tempo',
     'Valor',
     'Cria valor novo e, além de certo ponto, mais-valor'],
  ]),
  ('p', 'Observação decisiva. Não são dois trabalhos, é o *mesmo* trabalho sob duas '
        'determinações. O fiandeiro, ao fiar, produz fio e, pelo mesmo e único ato, adiciona '
        'valor. É por isso que ele preserva o valor do algodão exatamente na medida em que o '
        'transforma em fio.'),

  ('h', '4. O encadeamento das cinco categorias'),
  ('d', 'Trabalho||É a categoria central porque é duplo. Como trabalho útil, é o criador de '
        'valores de uso, em conjunto com a natureza. Como trabalho abstrato, é a única '
        'substância do valor.'),
  ('d', 'Valor de uso||É o resultado do processo de trabalho e condição material do valor, '
        'pois o valor precisa de um portador corpóreo. Sem valor de uso não há valor '
        'realizável. Para o capitalista, interessa apenas como suporte do valor e condição '
        'de venda.'),
  ('d', 'Valor||É o resultado do trabalho abstrato, a objetivação de tempo de trabalho '
        'socialmente necessário.'),
  ('d', 'Processo de trabalho||É o lado material, a produção de valores de uso. Pressuposto '
        'indispensável, pois não há criação de valor sem dispêndio real de trabalho sobre '
        'objetos reais.'),
  ('d', 'Processo de valorização||É o lado da forma social, a produção de valor e de '
        'mais-valor, finalidade determinante sob o capital.'),
  ('d', 'A unidade||O processo de produção capitalista é a unidade *contraditória* dos dois. '
        'Contraditória porque a finalidade da valorização subordina e deforma o processo de '
        'trabalho, submetendo a técnica, a duração e a intensidade da jornada ao imperativo '
        'do excedente.'),

  ('h', '5. Condições e qualificações'),
  ('d', 'Trabalho socialmente necessário||O trabalho só cria valor na medida em que é '
        'socialmente necessário. Trabalho despendido com intensidade ou destreza abaixo da '
        'média social, ou simplesmente desperdiçado, não cria valor proporcional. Algodão '
        'estragado por descuido não transfere valor ao produto.'),
  ('d', 'Utilidade social||O produto precisa ser valor de uso para outros, satisfazendo uma '
        'necessidade social, do contrário o trabalho se revela socialmente inútil e o valor '
        'não se valida na venda.'),
  ('d', 'A inversão característica||No processo de trabalho considerado em si, o trabalhador '
        'usa os meios de produção. No processo de valorização capitalista, os meios de '
        'produção, como capital, usam o trabalhador, e se convertem em meios de absorção de '
        'trabalho alheio. Essa inversão é retomada e plenamente desenvolvida no cap. 13, com '
        'a maquinaria.'),
 ],
},

# ===================================================================== cap. 6
{
 'depois': 19,
 'rotulo': 'Resposta 4 (cap. 6, "Capital constante e capital variável")',
 'blocos': [
  ('h', '1. Capital constante (c)'),
  ('d', 'Definição||Parte do valor-capital adiantada na compra de meios de produção. Marx a '
        'chama constante porque, no interior do processo de produção, ela não altera a sua '
        'grandeza de valor. O seu valor é apenas conservado e transferido ao produto, '
        'reaparecendo nele sem acréscimo.'),
  ('d', 'Componentes materiais, objeto de trabalho||Matérias-primas e matérias brutas, como '
        'algodão, ferro, minério, madeira.'),
  ('d', 'Componentes materiais, matérias auxiliares||Combustível, lubrificantes, produtos '
        'químicos, energia. Não compõem a substância do produto, mas são consumidas no '
        'processo.'),
  ('d', 'Componentes materiais, meios de trabalho||Máquinas, ferramentas, instrumentos, '
        'instalações, edifícios, a terra como base de operação.'),
  ('d', 'Contribuição ao valor da mercadoria||Transferência, nunca criação. O trabalho vivo, '
        'na sua determinação concreta, conserva o valor dos meios de produção ao consumi-los '
        'produtivamente, e esse valor reaparece no produto.'),
  ('d', 'Modos distintos de transferência||Matérias-primas e auxiliares são consumidas '
        'inteiramente em cada período e transferem todo o seu valor ao produto desse '
        'período. Máquinas e instalações continuam funcionando integralmente na sua forma '
        'material por muitos períodos e cedem valor apenas fracionadamente, na medida do '
        'desgaste. Daí a diferença, desenvolvida no Livro II, entre capital circulante e '
        'capital fixo.'),
  ('d', 'Limite quantitativo||O valor transferido nunca excede o valor que os meios de '
        'produção efetivamente possuíam. Não há como extrair do algodão mais valor do que o '
        'que nele estava objetivado.'),
  ('d', 'Contribuição ao mais-valor||Nula. O capital constante é condição material '
        'absolutamente indispensável, pois sem meios de produção não há processo de trabalho '
        'e nenhum trabalho vivo pode ser posto em movimento. Mas ele não é fonte de valor '
        'novo. A sua função na valorização é passiva, ele é o meio pelo qual o trabalho vivo '
        'é absorvido.'),

  ('h', '2. Capital variável (v)'),
  ('d', 'Definição||Parte do valor-capital adiantada na compra da força de trabalho, isto é, '
        'o fundo de salários. Marx a chama variável porque, no curso do processo, ela altera '
        'a sua grandeza de valor. O valor adiantado é reposto pelo trabalhador e, além '
        'disso, é produzido um excedente.'),
  ('d', 'Componentes materiais||A força de trabalho dos trabalhadores assalariados. '
        'Materialmente, o capital variável se converte nos meios de subsistência que os '
        'trabalhadores consomem e pelos quais reproduzem a sua capacidade de trabalho.'),
  ('d', 'Contribuição ao valor da mercadoria||É pela mobilização do trabalho vivo, comprado '
        'com v, que se cria valor novo. O valor novo criado no período é v + m, grandeza que '
        'Marx chama *produto de valor* (cap. 7). A parte v é apenas o equivalente reposto, m '
        'é o excedente.'),
  ('d', 'Contribuição ao mais-valor||Exclusiva. O mais-valor provém apenas do trabalho vivo e, '
        'portanto, apenas da parte variável do capital, pois é ela que compra a única '
        'mercadoria cujo valor de uso consiste em criar valor. Cabe uma precisão. Não é o '
        'capital variável, como soma de valor, que cria o mais-valor, é o trabalho vivo que '
        'ele põe em movimento. O capital variável é a forma pela qual o capital se apropria '
        'dessa capacidade.'),

  ('h', '3. Quadro comparativo'),
  ('t', [
    ['Critério', 'Capital constante (c)', 'Capital variável (v)'],
    ['Forma de adiantamento', 'Meios de produção', 'Força de trabalho, salários'],
    ['Componentes materiais',
     'Matérias-primas e auxiliares, máquinas, instalações, edifícios',
     'Trabalhadores assalariados, mediados pelos meios de subsistência'],
    ['Comportamento do valor', 'Conservado e transferido, inalterado', 'Reposto e acrescido'],
    ['Papel no valor da mercadoria', 'c, valor preexistente que reaparece', 'v + m, valor novo criado'],
    ['Papel no mais-valor', 'Nenhum, apenas condição material', 'Único, é a fonte'],
  ]),
  ('p', 'Decomposição resultante do valor da mercadoria: **valor = c + v + m**, em que c é '
        'valor transferido e (v + m) é o produto de valor, isto é, o valor novo criado no '
        'período.'),

  ('h', '4. Observações'),
  ('d', 'Distinção diferente de fixo e circulante||O par c/v é qualitativo e diz respeito ao '
        'papel de cada parte na valorização. Não se confunde com o par fixo/circulante, que '
        'deriva do modo de rotação do valor e aparece no Livro II. Matérias-primas são '
        'capital constante e circulante, máquinas são capital constante e fixo.'),
  ('d', 'Função crítica do par conceitual||Para o capitalista, todo desembolso aparece como '
        'adiantamento homogêneo, e o excedente aparece como rendimento do capital total, '
        'expresso na taxa de lucro m/(c+v). Essa indistinção é a base objetiva da aparência '
        'de que o capital em geral é produtivo e de que o lucro nasce do capital como tal. '
        'Separando c de v, Marx mostra que o excedente tem fonte determinada, o trabalho '
        'excedente não pago, e que a taxa de lucro oculta o grau de exploração. A economia '
        'política clássica, por não fazer essa distinção, não conseguiu explicar a origem do '
        'excedente de modo consistente.'),
  ('d', 'Uma qualificação||Dizer que c é constante vale para o interior do processo de '
        'produção. O valor dos meios de produção já comprados pode variar por causas '
        'externas, como um salto de produtividade no setor que os produz, provocando a '
        'desvalorização do capital já investido, fenômeno importante nas crises. Isso não '
        'contradiz a determinação do cap. 6, que se refere ao comportamento do valor *no* '
        'processo.'),
 ],
},

# ===================================================================== cap. 7
{
 'depois': 25,
 'rotulo': 'Resposta 5 (cap. 7, "A taxa de mais-valor"). As duas fórmulas',
 'blocos': [
  ('h', '1. Primeira fórmula, em termos de valores'),
  ('p', 'Marx parte do valor da mercadoria produzida, C\' = c + v + m. Como c é valor apenas '
        'transferido, e não criado no processo, para isolar o que foi efetivamente produzido '
        'subtrai-se c, restando o produto de valor, v + m. A taxa de mais-valor é a razão '
        'entre o mais-valor e o capital variável.'),
  ('f', "m' = m / v"),
  ('p', 'O denominador é o capital variável, e não o capital total. O sentido da fórmula é '
        'medir o grau de valorização justamente da parte do capital que se valoriza.'),

  ('h', '2. Segunda fórmula, em termos de tempos de trabalho'),
  ('p', 'A mesma relação expressa na divisão da jornada de trabalho. A jornada se decompõe em '
        'tempo de trabalho necessário, no qual o trabalhador produz o equivalente ao valor '
        'da sua força de trabalho, e tempo de trabalho excedente, no qual produz valor sem '
        'contrapartida.'),
  ('f', "m' = trabalho excedente / trabalho necessário"),

  ('h', '3. Por que as duas são equivalentes'),
  ('p', 'As fórmulas expressam a mesma relação porque v é a forma-valor do trabalho '
        'necessário e m é a forma-valor do trabalho excedente. Marx escreve a identidade '
        'entre as duas razões e observa que ambas dizem o mesmo, uma em trabalho objetivado, '
        'trabalho morto já cristalizado em valor, a outra em trabalho fluente, trabalho vivo '
        'em processo. A primeira é a expressão da relação tal como aparece no resultado, a '
        'segunda é a sua expressão na própria atividade.'),
  ('f', "m / v  =  trabalho excedente / trabalho necessário"),

  ('h', '4. Por que a taxa de mais-valor, e não a taxa de lucro'),
  ('d', 'O que m/v mede||O grau de exploração, porque confronta diretamente o trabalho não '
        'pago com o trabalho pago. É, nas palavras do enunciado da questão, a expressão '
        'exata do grau de exploração da força de trabalho pelo capital.'),
  ('d', 'O que m/(c+v) oculta||A taxa de lucro dilui o mais-valor no capital total e produz '
        'sempre um número menor, encobrindo a exploração. Marx insiste na distinção '
        'precisamente porque é a taxa de lucro que aparece na superfície e orienta o cálculo '
        'capitalista, enquanto a taxa de mais-valor é a relação essencial. A taxa de lucro é '
        'desenvolvida no Livro III.'),
  ('d', 'Uma terceira expressão equivalente||Marx menciona ainda a relação entre o '
        'mais-produto, parte do produto que corporifica o trabalho excedente, e a parte do '
        'produto correspondente ao trabalho necessário. Com produtividade dada, essa relação '
        'em quantidades físicas reproduz a mesma proporção.'),
  ('d', 'Aplicação polêmica||É neste capítulo que Marx desmonta o argumento da "última hora" '
        'de Nassau Senior, segundo o qual a redução da jornada eliminaria todo o lucro. O '
        'erro consiste exatamente em confundir as grandezas, calculando o excedente sobre o '
        'valor total do produto em vez de sobre o capital variável.'),
 ],
},

{
 'depois': 27,
 'rotulo': 'Resposta 6 (cap. 7). Cálculo com c = 410, v = 90, m = 90',
 'blocos': [
  ('p', 'As grandezas do enunciado são exatamente as que Marx utiliza no capítulo, o que torna '
        'o exercício uma reconstrução direta da sua exposição.'),

  ('h', 'i) Valor do capital total adiantado'),
  ('f', 'C = c + v = 410 + 90 = 500'),
  ('p', 'É o valor efetivamente desembolsado para iniciar o processo. Note que m não entra '
        'aqui, pois ele é resultado, não adiantamento.'),

  ('h', 'ii) Valor do produto (*Produktenwert*)'),
  ('f', 'c + v + m = 410 + 90 + 90 = 590'),
  ('p', 'É o valor da mercadoria que sai do processo. Inclui o valor preexistente transferido '
        'dos meios de produção, e por isso é a maior das grandezas.'),

  ('h', 'iii) Produto de valor (*Wertprodukt*)'),
  ('f', 'v + m = 90 + 90 = 180        ou        590 − 410 = 180'),
  ('p', 'É apenas o valor *novo* criado pelo trabalho vivo no período. Obtém-se subtraindo c '
        'do valor do produto, pois o capital constante não cria valor, apenas o repassa.'),

  ('h', 'iv) Taxa de mais-valor'),
  ('f', "m' = m / v = 90 / 90 = 1 = 100%"),

  ('h', 'Quadro resumo'),
  ('t', [
    ['Grandeza', 'Fórmula', 'Resultado'],
    ['Capital constante', 'c', '410'],
    ['Capital variável', 'v', '90'],
    ['Mais-valor', 'm', '90'],
    ['i) Capital total adiantado', 'c + v', '500'],
    ['ii) Valor do produto', 'c + v + m', '590'],
    ['iii) Produto de valor', 'v + m', '180'],
    ['iv) Taxa de mais-valor', 'm / v', '100%'],
    ['(taxa de lucro, para comparação)', 'm / (c + v)', '18%'],
  ]),

  ('h', 'Interpretação dos resultados'),
  ('d', 'O sentido dos 100%||O trabalhador produz, em trabalho excedente, exatamente o mesmo '
        'valor que produz em trabalho necessário. A jornada se divide em partes iguais. Numa '
        'jornada de 12 horas, 6 horas repõem o valor da força de trabalho e 6 horas são '
        'apropriadas gratuitamente pelo capitalista.'),
  ('d', 'O ponto central do exercício||A distinção entre os itens ii e iii. Marx insiste nela '
        'porque a confusão entre valor do produto (590) e produto de valor (180) é fonte de '
        'erros graves. Quem toma 590 como base obtém 90/590 ≈ 15,25%, número que não mede '
        'nenhuma relação determinada, pois mistura no denominador valor criado com valor '
        'meramente transferido.'),
  ('d', 'Comparação com a taxa de lucro||Sobre o capital total, m/(c+v) = 90/500 = 18%. É esse '
        'o número que interessa ao capitalista e que aparece na contabilidade, mas ele '
        'subestima drasticamente o grau de exploração, 18% contra 100%. A divergência entre '
        'as duas taxas é tanto maior quanto maior o peso de c, isto é, quanto mais elevada a '
        'composição orgânica do capital.'),
  ('d', 'Composição do capital, a título de complemento||c/v = 410/90 ≈ 4,56. Em termos '
        'percentuais, o capital adiantado se reparte em cerca de 82% constante e 18% '
        'variável, composição típica de produção já mecanizada.'),
 ],
},

{
 'depois': 29,
 'rotulo': 'Resposta 7 (cap. 7). Inovações técnicas e taxa de mais-valor',
 'blocos': [
  ('p', 'A consequência esperada é a **elevação da taxa de mais-valor**. O mecanismo, porém, é '
        'indireto, e passa necessariamente pelo valor da força de trabalho.'),

  ('h', '1. A cadeia causal'),
  ('b', '1. A inovação técnica eleva a força produtiva do trabalho, de modo que a mesma '
        'quantidade de trabalho produz uma massa maior de produtos.'),
  ('b', '2. Cai o tempo de trabalho socialmente necessário por unidade de mercadoria e, '
        'portanto, cai o valor unitário das mercadorias. O valor das mercadorias varia em '
        'razão inversa à produtividade do trabalho.'),
  ('b', '3. Se a queda atinge as mercadorias que compõem o consumo dos trabalhadores, cai o '
        'valor dos meios de subsistência e, por consequência, cai o valor da força de '
        'trabalho.'),
  ('b', '4. Com jornada dada, a redução do valor da força de trabalho encurta o tempo de '
        'trabalho necessário e amplia, na mesma medida, o tempo de trabalho excedente.'),
  ('b', '5. Logo m aumenta e v diminui, e a razão m/v sobe por efeito combinado do numerador e '
        'do denominador. Esse é o mecanismo do mais-valor relativo, desenvolvido nos '
        'capítulos 10 a 13.'),
  ('p', 'Exemplo. Jornada de 12 horas com 6 horas necessárias, m\' = 6/6 = 100%. Um avanço de '
        'produtividade que reduza o trabalho necessário a 4 horas eleva o excedente a 8 '
        'horas, e m\' = 8/4 = 200%, sem que a jornada tenha aumentado um único minuto.'),

  ('h', '2. O mais-valor extra como motor imediato'),
  ('p', 'Para o capitalista individual que inova primeiro, o efeito é mais direto. Ele produz '
        'com valor individual inferior ao valor social vigente, vende ao valor social, ou '
        'pouco abaixo dele, e se apropria de um mais-valor extra. A vantagem é transitória, '
        'pois desaparece quando a técnica se generaliza e o novo valor social, mais baixo, se '
        'impõe. Mas é exatamente essa recompensa temporária que impulsiona cada capitalista '
        'individualmente a inovar, produzindo como resultado agregado e não intencional a '
        'queda geral do valor das mercadorias.'),

  ('h', '3. Qualificações necessárias'),
  ('d', 'O salário real||A elevação da taxa pressupõe que o salário real não aumente na mesma '
        'proporção da produtividade. Se o valor da força de trabalho cai mas o trabalhador '
        'passa a consumir proporcionalmente mais valores de uso, a taxa pode não se alterar. '
        'A repartição dos ganhos de produtividade é objeto de luta de classes, não um dado '
        'técnico.'),
  ('d', 'Setores que não contam||Inovações em ramos que não produzem bens de consumo dos '
        'trabalhadores, nem os insumos destes, dão mais-valor extra ao inovador mas não '
        'elevam a taxa geral de mais-valor, ponto desenvolvido no cap. 10.'),
  ('d', 'Efeito oposto sobre a taxa de lucro||A inovação aumenta a massa de meios de produção '
        'posta em movimento por cada trabalhador, elevando a composição orgânica c/v. Com '
        'uma dada taxa de mais-valor, a elevação de c/v *reduz* a taxa de lucro m/(c+v). '
        'Essa divergência, taxa de mais-valor crescente com taxa de lucro tendencialmente '
        'declinante, é desenvolvida no Livro III e é um dos resultados mais importantes da '
        'análise. Já no cap. 7 ela está implícita, pois a mesma transformação técnica que '
        'intensifica a exploração corrói a rentabilidade.'),
 ],
},

# ===================================================================== cap. 9
{
 'depois': 35,
 'rotulo': 'Resposta 8 (cap. 9, "Taxa e massa de mais-valor")',
 'blocos': [
  ('h', '1. O contexto do capítulo'),
  ('p', 'O cap. 9 trata da relação entre a taxa e a massa de mais-valor. A massa de mais-valor '
        'produzida por um capital é dada pela taxa de mais-valor multiplicada pelo capital '
        'variável total, ou, em termos de trabalho, pelo mais-valor extraído de um '
        'trabalhador médio multiplicado pelo número de trabalhadores empregados.'),
  ('f', "M = m' × V"),

  ('h', '2. O sentido da passagem'),
  ('p', 'A quantidade de trabalho que um capital pode explorar é o produto de dois fatores, '
        'uma grandeza extensiva, o número de trabalhadores, e uma grandeza de duração e '
        'intensidade, a quantidade de trabalho extraída de cada trabalhador. Como se trata '
        'de um produto, os dois fatores são, dentro de certos limites, substituíveis entre '
        'si. Uma redução no número de trabalhadores pode ser compensada pelo prolongamento '
        'da jornada ou pela intensificação do trabalho, e o inverso também vale.'),
  ('p', 'Daí a conclusão da passagem. O capital não depende estritamente do número de '
        'trabalhadores disponíveis para ampliar a massa de trabalho que explora e, portanto, '
        'a massa de mais-valor que extrai. Ele pode aumentar a quantidade de trabalho '
        'explorado mantendo, ou mesmo reduzindo, o número de trabalhadores, apenas fazendo '
        'cada um trabalhar mais tempo ou com maior intensidade. Nesse sentido, a oferta de '
        'trabalho, entendida como a massa de trabalho efetivamente à disposição do capital, '
        'se torna relativamente independente da oferta de trabalhadores, isto é, do tamanho '
        'da população trabalhadora.'),
  ('p', 'Ilustração. Um capital que emprega 100 trabalhadores por 8 horas mobiliza 800 horas '
        'de trabalho. O mesmo capital pode mobilizar as mesmas 800 horas empregando 80 '
        'trabalhadores por 10 horas, ou cerca de 66 trabalhadores por 12 horas. Para a massa '
        'de trabalho o resultado é idêntico, embora não o seja para a massa de mais-valor, '
        'como se verá a seguir.'),

  ('h', '3. Os "certos limites", que são a parte decisiva da ressalva'),
  ('d', 'Limite absoluto da jornada||Ela não pode exceder as 24 horas do dia e, muito antes '
        'disso, encontra limites físicos e fisiológicos de resistência do trabalhador, além '
        'dos limites legais conquistados pela luta de classes.'),
  ('d', 'A barreira à compensação||O mais-valor extraível de cada trabalhador não pode '
        'exceder a jornada máxima menos o tempo de trabalho necessário. Se o trabalho '
        'necessário é de 6 horas e a jornada máxima tolerável é de 18, o mais-valor máximo '
        'por trabalhador equivale a 12 horas, qualquer que seja a pressão exercida. Marx '
        'formula a lei, a barreira absoluta da jornada média é uma barreira absoluta à '
        'compensação da redução do capital variável pelo aumento da taxa de mais-valor.'),
  ('d', 'A assimetria entre os dois fatores||Aumentar o número de trabalhadores amplia a massa '
        'de mais-valor sem limite interno. Aumentar a taxa de exploração sobre um número '
        'menor encontra um teto rígido. Por isso a produção em grande escala e o crescimento '
        'do capital variável total continuam decisivos para a massa de mais-valor, e a '
        'substituição de um fator pelo outro só opera em margens estreitas.'),

  ('h', '4. As consequências que a passagem prepara'),
  ('d', 'O impulso à jornada e à intensidade||Explica o impulso permanente do capital ao '
        'prolongamento da jornada e à intensificação do trabalho, tema do cap. 8 e retomado '
        'no cap. 13. Esse impulso não é ganância pessoal, é a forma pela qual um capital de '
        'magnitude dada amplia a massa de mais-valor.'),
  ('d', 'Maquinaria e massa de mais-valor||Explica por que a introdução de maquinaria, que '
        'reduz o número de trabalhadores empregados, não implica necessariamente redução da '
        'massa de mais-valor, pois o capital busca compensar a queda de v com a elevação de '
        'm\' pela via da jornada e da intensidade.'),
  ('d', 'Antecipação do cap. 23||Se a massa de trabalho explorável pode crescer sem '
        'crescimento da população trabalhadora, então a dinâmica do capital se desliga da '
        'dinâmica demográfica, e a oferta de trabalho deixa de ser variável independente '
        'determinada pela natureza. Esse é um dos fundamentos do argumento posterior de que '
        'os dados estão viciados, porque o capital atua também sobre o lado da oferta.'),
 ],
},

# ==================================================================== cap. 10
{
 'depois': 39,
 'rotulo': 'Resposta 9 (cap. 10, "Conceito de mais-valor relativo"). O expediente',
 'blocos': [
  ('h', '1. A distinção prévia'),
  ('d', 'Mais-valor absoluto||Obtido pelo prolongamento da jornada de trabalho além do ponto '
        'em que o trabalhador repõe o valor da sua força de trabalho, mantendo-se dado o '
        'tempo de trabalho necessário.'),
  ('d', 'Mais-valor relativo||Obtido com jornada dada, e mesmo com jornada reduzida, pela '
        'contração do tempo de trabalho necessário, o que amplia na mesma medida o tempo de '
        'trabalho excedente.'),

  ('h', '2. O expediente'),
  ('p', 'Como a jornada está dada, existe um único caminho. É preciso reduzir o tempo de '
        'trabalho necessário, e isso exige reduzir o valor da força de trabalho. Para reduzir '
        'o valor da força de trabalho é preciso reduzir o valor das mercadorias que o '
        'determinam, e o único meio de reduzir o valor de uma mercadoria é elevar a força '
        'produtiva do trabalho que a produz. O expediente é, portanto, a **revolução '
        'permanente das condições técnicas e sociais do processo de produção**, com o '
        'objetivo de aumentar a produtividade do trabalho.'),

  ('h', '3. As formas concretas que o expediente assume'),
  ('d', 'Cooperação (cap. 11)||A reunião de muitos trabalhadores no mesmo processo, que gera '
        'uma força produtiva social superior à soma das forças individuais e permite '
        'economias de escala no uso de meios de produção.'),
  ('d', 'Divisão do trabalho na manufatura (cap. 12)||A decomposição do ofício em operações '
        'parciais, que especializa o trabalhador, elimina poros na jornada e eleva a '
        'destreza, ao custo da mutilação do trabalhador parcial.'),
  ('d', 'Maquinaria e grande indústria (cap. 13)||A substituição da base subjetiva do ofício '
        'por um sistema objetivo de máquinas. É a forma mais desenvolvida e especificamente '
        'capitalista do expediente.'),
  ('d', 'Intensificação do trabalho||Mecanismo correlato, que aumenta o dispêndio de trabalho '
        'por unidade de tempo. Torna-se central quando a jornada é legalmente limitada.'),

  ('h', '4. O motor imediato, o mais-valor extra'),
  ('p', 'Nenhum capitalista individual age com o propósito de reduzir o valor da força de '
        'trabalho. O móvel imediato de cada um é o mais-valor extra. O capitalista que adota '
        'um método superior produz a sua mercadoria com valor individual inferior ao valor '
        'social, vende-a ao valor social ou pouco abaixo dele, realiza um mais-valor acima da '
        'média e amplia o seu mercado às custas dos concorrentes.'),
  ('p', 'Essa vantagem é transitória, pois se dissolve quando o novo método se generaliza por '
        'força da concorrência, estabelecendo um novo valor social mais baixo. Nesse momento '
        'o mais-valor extra individual desaparece, mas o resultado social permanece, o valor '
        'das mercadorias caiu. Se essas mercadorias determinam o valor da força de trabalho, '
        'o mais-valor relativo se torna geral e se incorpora às condições normais da '
        'produção. O resultado coletivo é, portanto, efeito não intencional da busca '
        'individual de vantagem.'),

  ('h', '5. A conclusão metodológica'),
  ('p', 'O mais-valor relativo explica por que o capital é intrinsecamente dinâmico e '
        'revolucionário no plano técnico. A busca de excedente deixa de depender apenas do '
        'prolongamento da jornada, limite que a resistência operária e a legislação acabam '
        'por fixar, e passa a depender da transformação incessante do processo produtivo. '
        'Marx destaca a inversão característica, o impulso imanente do capital a elevar a '
        'força produtiva do trabalho não existe para reduzir o esforço humano, e sim para '
        'baratear a mercadoria e encurtar a parte da jornada que pertence ao trabalhador.'),
 ],
},

{
 'depois': 41,
 'rotulo': 'Resposta 10 (cap. 10). Que mercadorias devem ter o valor reduzido',
 'blocos': [
  ('h', '1. A resposta'),
  ('p', 'Devem ter o seu valor reduzido as mercadorias que **entram no consumo habitual dos '
        'trabalhadores**, isto é, os meios de subsistência necessários à reprodução da força '
        'de trabalho. Alimentos, vestuário, habitação e, em geral, os bens que compõem o '
        'padrão de consumo socialmente estabelecido da classe trabalhadora.'),

  ('h', '2. Por quê'),
  ('p', 'A razão está na determinação do valor da força de trabalho. Como qualquer mercadoria, '
        'a força de trabalho tem o seu valor determinado pelo tempo de trabalho socialmente '
        'necessário à sua produção e reprodução, o que significa, concretamente, pelo valor '
        'dos meios de subsistência necessários para manter o trabalhador e reproduzir a sua '
        'família. O tempo de trabalho necessário da jornada é precisamente o tempo em que o '
        'trabalhador produz o equivalente a esse valor. Daí a sequência:'),
  ('b', 'Cai o valor dos meios de subsistência.'),
  ('b', 'Cai o valor da força de trabalho, que é determinado por eles.'),
  ('b', 'Encurta-se o tempo de trabalho necessário.'),
  ('b', 'Com jornada dada, amplia-se na mesma medida o tempo de trabalho excedente, e o '
        'mais-valor relativo é obtido.'),
  ('p', 'Nenhum outro tipo de mercadoria produz esse efeito, porque nenhum outro entra na '
        'determinação do valor da força de trabalho.'),

  ('h', '3. A extensão à cadeia produtiva'),
  ('p', 'O raciocínio se estende aos meios de produção empregados na produção desses bens de '
        'consumo. O barateamento de fertilizantes, de maquinaria agrícola, de transporte ou '
        'de fios e tecidos reduz o valor dos alimentos e do vestuário e, por essa via '
        'indireta, o valor da força de trabalho. Importa, portanto, o conjunto dos setores '
        'que direta ou indiretamente determinam o valor dos meios de subsistência.'),

  ('h', '4. O contraste que confirma o argumento'),
  ('p', 'Um salto de produtividade na produção de bens de luxo, que não entram no consumo dos '
        'trabalhadores, barateia esses bens e proporciona mais-valor extra ao capitalista que '
        'inova primeiro, mas não altera o valor da força de trabalho e, portanto, não gera '
        'mais-valor relativo para o capital social. O contraste mostra que o mais-valor '
        'relativo não decorre do aumento da produtividade em geral, e sim do aumento da '
        'produtividade nos setores que determinam o custo de reprodução do trabalhador.'),

  ('h', '5. Consequências de interesse'),
  ('d', 'Importância estratégica de certos setores||Explica o peso, no capitalismo, dos ramos '
        'produtores de bens de consumo popular e dos seus insumos, e esclarece por que o '
        'preço dos alimentos é historicamente objeto de conflito direto entre capital e '
        'trabalho, e também entre frações da própria classe dominante. A revogação das Leis '
        'do Trigo na Inglaterra é o exemplo clássico, pois o capital industrial tinha '
        'interesse em alimentos baratos para reduzir o valor da força de trabalho, enquanto a '
        'propriedade fundiária tinha interesse oposto.'),
  ('d', 'Uma qualificação||O resultado pressupõe que o barateamento se traduza em queda do '
        'valor da força de trabalho, e não em elevação do padrão de consumo real dos '
        'trabalhadores a valor constante. Como a determinação do valor da força de trabalho '
        'contém um elemento histórico e moral, a repartição dos ganhos de produtividade '
        'depende da relação de forças entre as classes. Historicamente observam-se as duas '
        'coisas simultaneamente, elevação do consumo real dos trabalhadores e elevação da '
        'taxa de mais-valor.'),
 ],
},

# ==================================================================== cap. 13
{
 'depois': 45,
 'rotulo': 'Resposta 11 (cap. 13, "Maquinaria e grande indústria")',
 'blocos': [
  ('p', 'A relevância da maquinaria não é, para Marx, apenas técnica. Ela é o meio pelo qual o '
        'capital constrói uma base material adequada a si mesmo e reorganiza integralmente o '
        'processo de trabalho, as relações no interior da fábrica e a posição da classe '
        'trabalhadora. O capítulo trata a maquinaria como a forma mais desenvolvida de '
        'produção de mais-valor relativo.'),

  ('h', '1. A finalidade capitalista da maquinaria'),
  ('p', 'A maquinaria não é introduzida para aliviar o trabalho. Como todo desenvolvimento da '
        'força produtiva sob o capital, ela serve a baratear mercadorias e a encurtar a parte '
        'da jornada em que o trabalhador trabalha para si, ampliando a parte que ele entrega '
        'gratuitamente ao capital. Marx é explícito, a maquinaria é um meio de produzir '
        'mais-valor.'),

  ('h', '2. O limite do emprego capitalista da maquinaria'),
  ('p', 'Há um critério econômico preciso. A máquina só é adotada quando o valor que ela '
        'transfere ao produto é menor que o valor da força de trabalho que ela substitui. O '
        'capitalista não compara trabalho com trabalho, compara o preço da máquina com o '
        'preço da força de trabalho dispensada. Daí uma consequência aparentemente '
        'paradoxal, em países ou setores onde a força de trabalho é muito barata a '
        'maquinaria é adotada mais lentamente, ainda que tecnicamente disponível. A máquina '
        'nunca adiciona ao produto mais valor do que perde pelo desgaste, portanto ela não é '
        'fonte de valor, é capital constante.'),

  ('h', '3. A inversão da relação entre trabalhador e meio de trabalho'),
  ('p', 'Este é o ponto central do capítulo. Na manufatura, o princípio organizador é '
        'subjetivo, o processo é decomposto conforme a habilidade dos trabalhadores e se '
        'adapta a eles, de modo que o ponto de partida ainda é a destreza humana. Na grande '
        'indústria, o princípio organizador se torna objetivo. O sistema de máquinas existe '
        'como organismo técnico autônomo, com lógica, ritmo e sequência próprios, e o '
        'trabalhador é incorporado a ele.'),
  ('p', 'Marx formula a imagem com precisão. Na manufatura, os trabalhadores são membros de um '
        'mecanismo vivo. Na fábrica, existe um mecanismo morto, independente deles, ao qual '
        'são incorporados como apêndices vivos. A máquina detém a habilidade e a força, o '
        'trabalhador se torna o seu vigilante e servidor. O movimento do instrumento de '
        'trabalho deixa de partir do trabalhador e passa a lhe ser imposto.'),

  ('h', '4. Da subsunção formal à subsunção real'),
  ('p', 'Enquanto o capital apenas se apropria de processos de trabalho herdados do '
        'artesanato, prolongando a jornada e organizando a cooperação, a subsunção do '
        'trabalho ao capital é apenas formal. Com a maquinaria, o capital transforma o '
        'processo de trabalho desde dentro, criando um modo de produzir que não existiria sem '
        'ele. É a subsunção real. A grande indústria é o primeiro modo de produção cuja base '
        'técnica corresponde à sua forma social, razão pela qual Marx a trata como o ponto em '
        'que o capitalismo se torna um modo de produção específico, e não apenas uma forma de '
        'apropriação sobreposta a técnicas antigas.'),

  ('h', '5. A decomposição da máquina e o ponto de partida da revolução industrial'),
  ('p', 'A máquina desenvolvida compreende três partes, o mecanismo motor, o mecanismo de '
        'transmissão e a máquina-ferramenta, ou máquina de trabalho. A revolução industrial '
        'não parte do motor, parte da máquina-ferramenta, isto é, da parte que executa a '
        'operação antes feita pela mão do trabalhador com a ferramenta. Resolvido esse ponto, '
        'a necessidade de uma força motriz maior e regular impulsiona o desenvolvimento do '
        'motor, e a cooperação de muitas máquinas semelhantes dá origem ao sistema de '
        'máquinas, até o momento em que máquinas passam a produzir máquinas e a grande '
        'indústria ganha base técnica própria.'),

  ('h', '6. Efeitos sobre a composição e o uso da força de trabalho'),
  ('d', 'Incorporação de mulheres e crianças||A máquina dispensa força muscular e habilidade '
        'especializada, o que permite substituir o trabalhador adulto do sexo masculino por '
        'mulheres e crianças. Isso amplia o material humano de exploração e, ao fazer com que '
        'toda a família contribua para a reprodução da força de trabalho, reduz o valor da '
        'força de trabalho individual sem que o conjunto familiar melhore a sua situação.'),
  ('d', 'Prolongamento da jornada||Parece contraditório que a máquina, ao poupar trabalho, '
        'leve ao aumento da jornada, mas a lógica do capital explica o resultado. O capital '
        'fixo investido precisa ser valorizado antes de ser desvalorizado moralmente pelo '
        'progresso técnico, o que impele à utilização contínua das instalações. Além disso, '
        'como a máquina eleva c em relação a v e pressiona a taxa de lucro, o capital busca '
        'compensação na ampliação da massa de trabalho excedente.'),
  ('d', 'Intensificação do trabalho||Quando a luta de classes e a legislação fixam limites à '
        'duração da jornada, o capital desloca a pressão para a intensidade. Aumenta a '
        'velocidade das máquinas, amplia o número de máquinas sob a responsabilidade de cada '
        'trabalhador e elimina as pausas. A jornada menor passa a conter mais trabalho. Marx '
        'mostra que foi justamente a limitação legal da jornada que impulsionou o '
        'aperfeiçoamento técnico e a condensação do trabalho.'),

  ('h', '7. A maquinaria como arma na luta de classes'),
  ('d', 'Substituibilidade do trabalhador||A máquina torna o trabalhador substituível e, com '
        'isso, desarma a sua resistência. Ela é mobilizada deliberadamente para derrotar '
        'greves e quebrar a posição de grupos de trabalhadores qualificados. Marx registra '
        'que a maquinaria se torna a arma mais poderosa para reprimir as revoltas periódicas '
        'dos trabalhadores.'),
  ('d', 'Produção da superpopulação relativa||Ao repelir trabalhadores do processo produtivo, '
        'a maquinaria alimenta o exército industrial de reserva, cujo papel disciplinador é '
        'analisado no cap. 23.'),
  ('d', 'Separação entre trabalho manual e intelectual||O saber do processo se objetiva na '
        'máquina e na ciência aplicada, confrontando o trabalhador como poder alheio. O '
        'conhecimento que era atributo do ofício passa a ser propriedade do capital.'),
  ('d', 'Despotismo de fábrica||O regime fabril assume a forma de um despotismo, com '
        'disciplina, regulamentos, multas e vigilância contínua, substituindo a autonomia '
        'relativa do artesão.'),

  ('h', '8. A ambivalência histórica'),
  ('p', 'Marx não condena a maquinaria em si, e distingue rigorosamente a máquina do seu '
        'emprego capitalista. A grande indústria socializa o processo de produção, cria o '
        'trabalhador coletivo em escala inédita, exige variabilidade e mobilidade da força de '
        'trabalho, impõe a necessidade de educação técnica e politécnica e desenvolve as '
        'forças produtivas a um ponto que torna possível uma organização social superior. As '
        'mesmas condições que degradam o trabalhador criam os pressupostos materiais e '
        'sociais da sua emancipação. O sofrimento imposto pela máquina decorre não da '
        'técnica, e sim das relações sociais sob as quais ela é empregada.'),

  ('h', 'Síntese'),
  ('p', 'A relevância da maquinaria consiste em ser, simultaneamente, o meio mais eficaz de '
        'produção de mais-valor relativo, o instrumento pelo qual o capital reorganiza '
        'objetivamente o processo de trabalho e consuma a subsunção real, a arma com que '
        'submete a resistência operária e produz a superpopulação relativa, e a base material '
        'a partir da qual se desenvolvem as contradições que apontam para além do próprio '
        'capitalismo.'),
 ],
},

# ==================================================================== cap. 21
{
 'depois': 49,
 'rotulo': 'Resposta 12 (cap. 21, "Reprodução simples"). Destinação do mais-valor',
 'blocos': [
  ('h', '1. A resposta direta'),
  ('p', 'Para que a reprodução seja simples, o capitalista deve **consumir individualmente a '
        'totalidade do mais-valor**, gastando-o como renda. Nenhuma fração do mais-valor pode '
        'ser convertida em capital adicional.'),

  ('h', '2. Por que é assim'),
  ('d', 'O que significa reprodução simples||Repetição do processo produtivo na mesma escala, '
        'período após período. Para isso, o capital adiantado no novo ciclo deve ter '
        'exatamente a mesma magnitude do anterior.'),
  ('d', 'A destinação de cada parte do produto||O valor do produto é c + v + m. A parte c deve '
        'ser reconvertida em meios de produção e a parte v em força de trabalho, repondo '
        'materialmente e em valor as condições de produção na escala anterior. Resta m.'),
  ('d', 'Por que m precisa ser inteiramente consumido||Se m fosse total ou parcialmente '
        'capitalizado, o capital adiantado no ciclo seguinte seria maior e a escala se '
        'ampliaria, caracterizando reprodução ampliada, tema do cap. 22. Para que a escala '
        'permaneça constante, m precisa ser integralmente dissipado em consumo improdutivo '
        'do capitalista, em meios de consumo individual.'),

  ('h', '3. O estatuto metodológico da hipótese'),
  ('p', 'A reprodução simples é uma abstração deliberada. Marx a introduz não porque descreva '
        'a realidade, já que o capital tende por natureza a se ampliar, mas porque, ao '
        'congelar a escala, ela permite isolar e tornar visível um resultado que a ampliação '
        'encobriria, o de que o processo reproduz a própria relação de classe. É o caso mais '
        'simples no qual a estrutura essencial aparece com nitidez.'),

  ('h', '4. Um resultado notável que a hipótese revela'),
  ('p', 'Se o capitalista consome anualmente todo o mais-valor, basta um certo número de anos '
        'para que ele tenha consumido um valor igual ao capital originalmente adiantado. A '
        'partir desse momento, o capital que ele ainda possui é integralmente mais-valor '
        'capitalizado, isto é, trabalho alheio apropriado sem equivalente. O título jurídico '
        'de propriedade permanece o mesmo, mas o conteúdo econômico se inverteu por completo. '
        'Mesmo que o capital inicial tivesse origem no trabalho próprio do seu possuidor, a '
        'simples continuidade do processo o converte, em prazo determinado, em valor '
        'apropriado gratuitamente.'),
 ],
},

{
 'depois': 53,
 'rotulo': 'Resposta 13 (cap. 21). A reprodução da relação social e o consumo do trabalhador',
 'blocos': [
  ('h', '1. O deslocamento de perspectiva'),
  ('p', 'Considerado como ato isolado, o processo de produção aparece como produção de '
        'mercadorias e de mais-valor. Considerado em sua continuidade, como processo de '
        'reprodução, ele revela algo mais. Todo processo social de produção é também processo '
        'de reprodução, porque precisa repor continuamente as suas próprias condições '
        'materiais e sociais. Nenhuma sociedade pode parar de produzir, e nenhuma pode '
        'produzir sem reproduzir os pressupostos de que parte. No caso do capital, esses '
        'pressupostos são a existência, de um lado, de possuidores de dinheiro e de meios de '
        'produção, e de outro, de possuidores apenas de força de trabalho. É essa relação que '
        'o processo reproduz.'),

  ('h', '2. O que a continuidade revela sobre o salário'),
  ('p', 'No ato isolado da troca, o salário aparece como dinheiro que o capitalista adianta do '
        'seu próprio fundo, e a transação se apresenta como troca de equivalentes entre '
        'proprietários livres. Considerado o processo em sua repetição, a aparência se '
        'dissolve. O valor com que o capitalista paga o salário é parte do valor que o '
        'próprio trabalhador produziu no período anterior. O capital variável não é um '
        'adiantamento feito a partir de um fundo externo, é uma fração do produto do trabalho '
        'alheio devolvida ao trabalhador sob a forma de salário.'),
  ('p', 'Marx observa que o capital variável é apenas a forma histórica particular de aparição '
        'do fundo de meios de subsistência de que o trabalhador precisa para a sua própria '
        'conservação, fundo que ele mesmo tem de produzir e reproduzir continuamente. O '
        'trabalhador recebe de volta, em parte, o que produziu, e produz o fundo com que será '
        'pago novamente.'),

  ('h', '3. A reprodução das duas classes'),
  ('d', 'Do lado do capitalista||O processo repõe e amplia a sua posse de meios de produção e '
        'de dinheiro, reproduzindo-o como capitalista, isto é, como personificação do capital '
        'e comprador de força de trabalho.'),
  ('d', 'Do lado do trabalhador||O processo o reproduz como trabalhador assalariado, e isso '
        'tem sentido duplo e preciso. Reproduz a sua força de trabalho, mantendo-o '
        'fisicamente apto a trabalhar, e reproduz a sua condição de despossuído, pois ele sai '
        'do processo como entrou, sem meios de produção, com nada além da capacidade de '
        'trabalho e da necessidade de vendê-la novamente.'),
  ('d', 'O resultado||A relação capitalista não é um pressuposto externo, dado uma vez por '
        'todas, que o processo encontra pronto. Ela é continuamente produzida e reproduzida '
        'pelo próprio funcionamento do processo. É nesse sentido que a produção capitalista '
        'produz e reproduz, além de mercadorias e mais-valor, a própria relação social entre '
        'as classes.'),

  ('h', '4. O papel do consumo do trabalhador'),
  ('p', 'O consumo do trabalhador tem caráter duplo, e é nele que a questão se concentra.'),
  ('d', 'Consumo produtivo||No interior do processo de trabalho, o trabalhador consome meios '
        'de produção, convertendo-os em produtos que pertencem ao capitalista. Esse consumo é '
        'diretamente consumo de capital e produção para o capital.'),
  ('d', 'Consumo individual||Fora do processo de trabalho, o trabalhador consome os meios de '
        'subsistência comprados com o salário. Esse consumo aparece como assunto privado seu, '
        'exercício da sua liberdade, exterior à relação de trabalho. Na perspectiva da '
        'reprodução, porém, revela-se como momento necessário da reprodução do capital. Ao '
        'consumir, o trabalhador não produz nada além da sua própria força de trabalho, isto '
        'é, justamente a mercadoria de que o capital depende. Nas palavras de Marx, o consumo '
        'individual do trabalhador é a produção e reprodução do meio de produção mais '
        'indispensável ao capitalista, o próprio trabalhador. É produção de capital, embora '
        'ocorra fora do processo imediato de produção e sob a aparência de consumo privado.'),
  ('d', 'A condição decisiva||O consumo individual deve absorver integralmente o salário, não '
        'deixando excedente que permita ao trabalhador acumular e tornar-se independente. Por '
        'isso a reprodução da força de trabalho é, ao mesmo tempo, a reprodução da sua '
        'despossessão. O trabalhador se reproduz como trabalhador, e não como proprietário. O '
        'consumo que o mantém vivo é o mesmo que o devolve ao mercado de trabalho na manhã '
        'seguinte, nas mesmas condições em que estava.'),
  ('d', 'A comparação esclarecedora||O proprietário de escravos precisa supervisionar '
        'diretamente a alimentação do escravo, pois este não tem interesse próprio em se '
        'conservar para o trabalho. O capitalista não precisa fazê-lo. Ele pode confiar o '
        'consumo do trabalhador ao interesse deste e à sua aparente liberdade, com resultado '
        'mais eficiente e menos custoso. A coerção se desloca da pessoa para as condições '
        'econômicas. Marx observa que as condições econômicas amarram o trabalhador ao '
        'capital com correntes mais sólidas do que as usadas pelo traficante de escravos, e '
        'fala dos fios invisíveis que o prendem à classe capitalista.'),

  ('h', '5. O nível individual e o nível de classe'),
  ('p', 'A aparência de liberdade se sustenta no plano do indivíduo. O trabalhador pode deixar '
        'este ou aquele capitalista, negociar, mudar de emprego. Mas não pode deixar a classe '
        'capitalista, porque fora dela não há acesso aos meios de produção. Marx formula o '
        'contraste, o trabalhador individual pertence a si mesmo, a classe trabalhadora '
        'pertence à classe capitalista. A liberdade do contrato individual é real e, '
        'exatamente por ser real, é o mecanismo pelo qual a dependência de classe se reproduz '
        'como se fosse resultado natural de escolhas livres. A reprodução do capital é, nesse '
        'sentido, também a reprodução da aparência que a legitima.'),
 ],
},

# ==================================================================== cap. 22
{
 'depois': 57,
 'rotulo': 'Resposta 14 (cap. 22, "A transformação de mais-valor em capital")',
 'blocos': [
  ('h', '1. A resposta direta'),
  ('p', 'Para que ocorra a reprodução ampliada, o capitalista deve consumir individualmente '
        'apenas **uma parte** do mais-valor e **capitalizar a parte restante**, isto é, '
        'empregá-la como capital adicional. Acumulação é, na definição de Marx, o emprego do '
        'mais-valor como capital, ou a reconversão do mais-valor em capital.'),

  ('h', '2. Como se dá a capitalização'),
  ('d', 'Repartição entre c e v||A parte capitalizada precisa se dividir entre capital '
        'constante adicional e capital variável adicional, nas proporções exigidas pela '
        'composição técnica do capital. Dinheiro acumulado não é capital. Ele só se torna '
        'capital adicional quando se converte em meios de produção adicionais e em força de '
        'trabalho adicional, que serão postos a funcionar conjuntamente.'),
  ('d', 'Os elementos materiais estão disponíveis||A operação exige que existam no mercado, '
        'simultaneamente, meios de produção adicionais e força de trabalho adicional. Marx '
        'mostra que o próprio sistema fornece as duas condições. O mais-produto do período '
        'anterior já contém, na sua forma material, os elementos do capital adicional, pois a '
        'produção capitalista produz máquinas, matérias-primas e instalações em quantidade '
        'superior à simples reposição.'),
  ('d', 'A força de trabalho adicional||É fornecida pela superpopulação relativa, resultado da '
        'própria acumulação, ponto desenvolvido no cap. 23.'),
  ('d', 'Caráter autossustentado||Portanto a acumulação não depende de nenhum fator externo ao '
        'processo. O capital produz as condições da sua própria ampliação.'),

  ('h', '3. Consequências de princípio'),
  ('d', 'A origem do capital adicional||Ele é, por origem, mais-valor capitalizado, isto é, '
        'trabalho alheio apropriado sem equivalente. A propriedade sobre produto alheio não '
        'pago se reproduz em escala crescente, e cada ciclo amplia a base sobre a qual o '
        'mais-valor é extraído. A acumulação é cumulativa, mais-valor capitalizado gera mais '
        'mais-valor, que é novamente capitalizado.'),
  ('d', 'Reprodução ampliada da relação de classe||Com a acumulação, a relação de classe não é '
        'apenas reproduzida, como no cap. 21, mas reproduzida em escala crescente. Mais '
        'trabalhadores são incorporados à relação assalariada, e a massa de meios de produção '
        'que os confronta como capital se amplia.'),
  ('d', 'A crítica à teoria da abstinência||Marx recusa a explicação da acumulação pela '
        'virtude da parcimônia do capitalista, defendida por Senior e outros. O fundo '
        'capitalizado não é fruto do trabalho nem da privação do capitalista, é mais-valor, '
        'trabalho excedente alheio. E a sua capitalização não resulta de escolha moral, e sim '
        'da coerção da concorrência, que impõe a cada capital a necessidade de crescer sob '
        'pena de sucumbir. O capitalista é *forçado* a acumular, independentemente de suas '
        'inclinações pessoais. A divisão do mais-valor entre renda e capital é, nesse '
        'sentido, socialmente determinada, e não ato de virtude individual.'),
 ],
},

{
 'depois': 59,
 'rotulo': 'Resposta 15 (cap. 22). Circunstâncias que determinam o volume da acumulação',
 'blocos': [
  ('h', 'O enunciado do problema'),
  ('p', 'Dada a proporção em que o mais-valor se divide entre renda consumida e capital '
        'acumulado, o volume da acumulação depende da grandeza do mais-valor. Logo, tudo o '
        'que determina a grandeza do mais-valor determina também, independentemente daquela '
        'proporção, o volume possível da acumulação. Marx examina quatro circunstâncias.'),

  ('h', '1. O grau de exploração da força de trabalho'),
  ('p', 'A taxa de mais-valor é o fator mais direto, e ela é elevada por três vias.'),
  ('b', 'Prolongamento da jornada de trabalho, que amplia o trabalho excedente sem alterar o '
        'trabalho necessário.'),
  ('b', 'Intensificação do trabalho, que aumenta o dispêndio de trabalho por unidade de tempo.'),
  ('b', 'Compressão do salário abaixo do valor da força de trabalho. Marx observa que essa via '
        'tem peso prático considerável, e que por ela o fundo de consumo necessário do '
        'trabalhador é convertido em fundo de acumulação do capital.'),
  ('p', 'Há um efeito adicional que Marx destaca. O prolongamento da jornada permite extrair '
        'mais mais-valor com economia no adiantamento de capital fixo, pois as mesmas '
        'instalações e máquinas são utilizadas por mais horas. O adiantamento necessário '
        'cresce menos que proporcionalmente ao mais-valor obtido.'),

  ('h', '2. A produtividade social do trabalho'),
  ('d', 'Barateia as mercadorias||Com uma dada grandeza de valor do mais-valor, o capitalista '
        'comanda uma massa física maior de meios de produção e de meios de subsistência. Em '
        'termos reais, a acumulação cresce mesmo sem aumento do mais-valor em valor.'),
  ('d', 'Barateia os elementos do capital||Tanto os meios de produção quanto os meios de '
        'subsistência que compõem o capital variável, permitindo que a mesma soma de valor '
        'ponha em movimento mais trabalho e mais matéria.'),
  ('d', 'Permite consumir e acumular mais ao mesmo tempo||O mesmo valor destinado à renda do '
        'capitalista compra mais valores de uso, de modo que o conflito entre consumo e '
        'acumulação se atenua.'),
  ('d', 'Amplia o mais-produto||Os elementos materiais do capital adicional ficam disponíveis '
        'em quantidade crescente.'),
  ('d', 'Desvaloriza e renova o capital existente||A produtividade crescente provoca a '
        'desvalorização moral do capital já investido e impõe a sua renovação em bases mais '
        'produtivas, mecanismo destrutivo no plano individual e de reposição no plano social.'),

  ('h', '3. A diferença crescente entre o capital empregado e o capital consumido'),
  ('p', 'Esta é a circunstância mais original da análise. Os meios de trabalho, como edifícios, '
        'máquinas e instalações, funcionam integralmente na sua forma material durante todo o '
        'seu período de vida, mas transferem ao produto apenas a fração correspondente ao '
        'desgaste do período. A diferença entre o capital *empregado*, o conjunto de meios de '
        'trabalho em operação, e o capital *consumido*, a parte do seu valor efetivamente '
        'transferida, constitui um serviço gratuito prestado ao capital pelo trabalho '
        'passado. Marx compara esse serviço à ação gratuita das forças naturais.'),
  ('p', 'Quanto maior a escala e a durabilidade do aparato produtivo já acumulado, maior essa '
        'diferença e maior o volume de acumulação possível. O mesmo raciocínio se aplica à '
        'ciência e ao conhecimento técnico acumulado, que o capital apropria sem pagar, pois '
        'o progresso científico não lhe custa nada próximo do que rende.'),

  ('h', '4. A grandeza do capital adiantado'),
  ('p', 'Dada a taxa de mais-valor, a massa de mais-valor é proporcional ao capital variável, '
        'isto é, ao número de trabalhadores explorados. Logo, quanto maior o capital, maior a '
        'massa de mais-valor e maior o volume absoluto da acumulação. Isso confere à '
        'acumulação caráter cumulativo, a acumulação engendra acumulação, e capitais maiores '
        'acumulam em volumes absolutos maiores. É a base material da concentração e, '
        'indiretamente, da centralização analisadas no cap. 23.'),

  ('h', '5. A crítica ao dogma do fundo de trabalho'),
  ('p', 'Marx encerra criticando a teoria do *wage fund*, segundo a qual existiria um fundo de '
        'salários de magnitude tecnicamente dada, do que decorreria que os salários só '
        'poderiam subir à custa do emprego e que qualquer reivindicação operária seria '
        'autodestrutiva. A análise das quatro circunstâncias mostra que a divisão do produto '
        'não é dada por nenhuma necessidade técnica. O fundo de salários é grandeza elástica, '
        'resultado da repartição do produto de valor, e essa repartição é determinada pela '
        'relação de forças entre as classes. O dogma converte um resultado histórico em '
        'limite natural, e serve para apresentar a distribuição vigente como intransponível.'),

  ('h', 'Síntese'),
  ('t', [
    ['Circunstância', 'Como atua sobre o volume da acumulação'],
    ['1. Grau de exploração',
     'Eleva a taxa de mais-valor por jornada, intensidade e compressão salarial'],
    ['2. Produtividade do trabalho',
     'Barateia mercadorias e elementos do capital, ampliando a acumulação em termos reais'],
    ['3. Diferença entre capital empregado e consumido',
     'Serviço gratuito do trabalho passado e da ciência, que não custa ao capital'],
    ['4. Grandeza do capital adiantado',
     'Com m\' dada, a massa de mais-valor é proporcional a v, o que torna a acumulação cumulativa'],
  ]),
 ],
},

# ==================================================================== cap. 23
{
 'depois': 65,
 'rotulo': 'Resposta 16 (cap. 23, "A lei geral da acumulação capitalista"). Os dois cenários',
 'blocos': [
  ('h', 'Preliminar. O que é a composição orgânica'),
  ('p', 'A composição orgânica do capital é a relação entre capital constante e capital '
        'variável, c/v, considerada na medida em que reflete a composição *técnica*, isto é, '
        'a proporção entre a massa de meios de produção e a quantidade de trabalho vivo '
        'necessária para operá-la. Marx examina os efeitos da acumulação sobre a classe '
        'trabalhadora em dois cenários sucessivos. O primeiro, com composição constante, é '
        'abstração metodológica. O segundo, com composição crescente, é o caso '
        'historicamente efetivo.'),

  ('h', 'Cenário 1. Composição orgânica constante'),
  ('d', 'i) Produtividade do trabalho||Permanece constante, por hipótese. A composição técnica '
        'não se altera, de modo que a escala da produção cresce pela simples multiplicação de '
        'unidades produtivas com a mesma técnica. Cada trabalhador adicional é equipado com a '
        'mesma massa de meios de produção que os anteriores. A acumulação é puramente '
        'quantitativa, extensiva.'),
  ('d', 'ii) Oferta e demanda de trabalho||O capital variável cresce na mesma proporção do '
        'capital total. Como a demanda por trabalho é determinada por v, ela cresce '
        'proporcionalmente à acumulação, que exige um aumento proporcional do número de '
        'trabalhadores empregados.'),
  ('d', 'O movimento dos salários||Se a acumulação avança mais rápido que o crescimento da '
        'população trabalhadora, a demanda supera a oferta e os salários sobem. A elevação '
        'dos salários reduz a taxa de mais-valor, o que reduz a massa disponível para '
        'capitalização e desacelera a acumulação. A desaceleração reduz a demanda por '
        'trabalho e restabelece a proporção anterior, com os salários voltando a cair. Marx '
        'descreve o resultado como o mecanismo pelo qual a produção capitalista remove por si '
        'mesma os obstáculos que cria.'),
  ('d', 'O limite de uma alta salarial||Marx é enfático. Mesmo no cenário mais favorável, a '
        'elevação do salário é melhora apenas quantitativa, que não altera a natureza da '
        'relação. Ela não suprime a dependência, porque o trabalhador continua despossuído e '
        'continua obrigado a vender a sua força de trabalho. No melhor dos casos ele é um '
        'assalariado melhor pago, e o aumento do preço do trabalho significa apenas que o '
        'tamanho da corrente de ouro forjada pelo próprio trabalhador permite afrouxá-la um '
        'pouco.'),
  ('d', 'A inversão da explicação clássica||Já aqui Marx estabelece que não é o movimento da '
        'população que governa a acumulação, e sim a acumulação que governa a demanda por '
        'trabalho e, por essa via, o salário. A relação de dependência é oposta à suposta '
        'pela doutrina malthusiana e pelo dogma do fundo de trabalho.'),

  ('h', 'Cenário 2. Composição orgânica crescente'),
  ('d', 'i) Produtividade do trabalho||Cresce, e o crescimento é simultaneamente causa e '
        'efeito da elevação da composição orgânica. O aumento da produtividade se expressa '
        'materialmente no aumento da massa de meios de produção posta em movimento por cada '
        'trabalhador, e essa mesma transformação eleva c relativamente a v. Em termos de '
        'valor o movimento é parcialmente atenuado, porque o aumento da produtividade '
        'barateia também os meios de produção, de modo que a composição em valor cresce '
        'menos que a composição técnica. Mas a tendência é inequívoca, a parte variável '
        'decresce relativamente e, em certos ramos, pode decrescer em termos absolutos.'),
  ('d', 'ii) Demanda de trabalho||Cresce menos que proporcionalmente ao capital, porque v '
        'cresce menos que C. Um capital que dobra pode demandar bem menos que o dobro de '
        'trabalhadores, e em ramos específicos pode demandar menos trabalhadores em termos '
        'absolutos.'),
  ('d', 'Atração e repulsão||O capital exerce dois movimentos simultâneos sobre a força de '
        'trabalho. Atrai trabalhadores ao ampliar a escala e abrir novos ramos, e repele '
        'trabalhadores ao substituí-los por maquinaria. O saldo é a produção contínua de uma '
        'população trabalhadora relativamente excedente, o exército industrial de reserva.'),
  ('d', 'ii) Oferta de trabalho||A própria acumulação produz a oferta de trabalho de que '
        'necessita. A oferta deixa de ser um dado demográfico externo e se torna produto '
        'interno do movimento do capital.'),
  ('d', 'Efeito sobre salários e condições||A pressão do exército de reserva sobre os '
        'empregados regula os salários, viabiliza a intensificação do trabalho e enfraquece a '
        'capacidade de resistência. Os movimentos gerais do salário passam a ser regulados '
        'pela expansão e contração da reserva, acompanhando as fases do ciclo industrial, e '
        'não pelo movimento do número absoluto da população.'),
  ('d', 'A lei geral absoluta da acumulação capitalista||Quanto maiores a riqueza social, o '
        'capital em funcionamento e a produtividade do trabalho, maior é também o exército '
        'industrial de reserva, e maior a massa da superpopulação consolidada e do pauperismo '
        'oficial. Riqueza crescente e miséria crescente são produzidas pelo *mesmo* processo, '
        'e não apesar dele. Marx fecha com a imagem de que a lei que mantém a superpopulação '
        'relativa em equilíbrio com o volume e a energia da acumulação prende o trabalhador '
        'ao capital mais firmemente do que as cunhas de Hefesto prendiam Prometeu ao '
        'rochedo.'),

  ('h', 'Quadro comparativo'),
  ('t', [
    ['Critério', 'Composição orgânica constante', 'Composição orgânica crescente'],
    ['Caráter da acumulação', 'Extensiva, quantitativa', 'Intensiva, com revolução técnica'],
    ['i) Produtividade do trabalho', 'Constante', 'Crescente'],
    ['Comportamento de v', 'Cresce na mesma proporção de C',
     'Cresce menos que C, podendo cair em termos absolutos'],
    ['ii) Demanda de trabalho', 'Cresce proporcionalmente ao capital',
     'Cresce menos que proporcionalmente'],
    ['ii) Oferta de trabalho', 'Dada pelo crescimento da população',
     'Produzida pela acumulação, exército de reserva'],
    ['Efeito sobre os salários', 'Tendem a subir, com oscilação autocorretiva',
     'Contidos pela pressão do exército de reserva'],
    ['Situação da classe trabalhadora', 'Melhora quantitativa, dependência mantida',
     'Insegurança, intensificação, pauperismo relativo'],
  ]),
 ],
},

{
 'depois': 67,
 'rotulo': 'Resposta 17 (cap. 23). Concentração, centralização, crédito e sociedade por ações',
 'blocos': [
  ('h', '1. Concentração do capital'),
  ('p', 'É o crescimento da magnitude dos capitais individuais como resultado direto da '
        'acumulação. Cada capitalista, ao capitalizar parte do mais-valor que se apropria, '
        'amplia o capital sob o seu comando e concentra em suas mãos uma massa maior de meios '
        'de produção e um contingente maior de trabalhadores. Nesse sentido, concentração é '
        'outro nome para o resultado da acumulação no plano do capital individual, '
        'acompanhada do aumento da escala da produção.'),
  ('p', 'A concentração tem, porém, limites e contratendências.'),
  ('b', 'Está limitada pelo crescimento da riqueza social, pois cada capital individual é '
        'apenas uma fração alíquota do capital social.'),
  ('b', 'A acumulação é acompanhada do aumento do número de capitais, por surgimento de novos '
        'capitais e por fragmentação dos existentes, sobretudo pela divisão de patrimônios '
        'entre herdeiros. Esse movimento dispersivo atua em sentido contrário.'),
  ('b', 'Por isso a concentração baseada apenas na acumulação própria é um processo lento, cujo '
        'ritmo é o ritmo da acumulação.'),

  ('h', '2. Centralização do capital'),
  ('p', 'É a concentração de capitais **já formados**, a atração de capital por capital, a '
        'reunião de muitos capitais menores em poucos capitais maiores. Marx a caracteriza '
        'como expropriação de capitalista por capitalista.'),
  ('d', 'A diferença essencial||A centralização não altera a magnitude do capital social '
        'total, altera apenas a sua distribuição. É redistribuição de capital existente, não '
        'criação de capital novo. Por isso ela não depende do ritmo da acumulação e pode '
        'operar com rapidez muito maior, por simples mudança na propriedade e no comando. '
        'Marx observa que o mundo continuaria sem ferrovias se fosse preciso esperar que a '
        'acumulação individual elevasse alguns capitais ao nível exigido para construí-las.'),
  ('d', 'Mecanismo 1, a concorrência||A batalha da concorrência é travada pelo barateamento '
        'das mercadorias, que depende da produtividade, que por sua vez depende da escala de '
        'produção. Os capitais maiores derrotam os menores, que são arruinados e cujos '
        'capitais passam, em parte, às mãos dos vencedores e, em parte, desaparecem. A '
        'concorrência atua como mecanismo de seleção que destrói os capitais pequenos e '
        'centraliza os sobreviventes.'),
  ('d', 'Mecanismo 2, o crédito||Inicialmente auxiliar modesto da acumulação, o crédito se '
        'torna uma arma nova e terrível na luta da concorrência e, por fim, se transforma em '
        'um imenso mecanismo social de centralização dos capitais.'),

  ('h', '3. O papel do crédito'),
  ('p', 'O crédito permite ao capitalista individual dispor, dentro de certos limites, do '
        'capital alheio e das poupanças monetárias dispersas de toda a sociedade. Os efeitos '
        'sobre a centralização são diretos.'),
  ('b', 'Desliga a escala de operação de um capital da magnitude do patrimônio pessoal do seu '
        'proprietário. O que comanda a produção deixa de ser a riqueza própria e passa a ser '
        'a capacidade de mobilizar capital social.'),
  ('b', 'Converte somas monetárias ociosas, que não funcionariam como capital, em capital '
        'ativo concentrado nas mãos de poucos.'),
  ('b', 'Confere aos capitais maiores vantagem adicional na concorrência, pois eles obtêm '
        'crédito em condições melhores, o que acelera a eliminação dos menores e realimenta a '
        'centralização.'),
  ('b', 'Torna-se, nas palavras de Marx, uma das alavancas mais poderosas da centralização.'),

  ('h', '4. O papel da sociedade por ações'),
  ('b', 'Permite reunir capitais individualmente insuficientes em um único capital de grandes '
        'dimensões, viabilizando empreendimentos de escala impossível para qualquer capital '
        'isolado, como ferrovias, siderurgia, mineração e grandes obras de infraestrutura.'),
  ('b', 'Separa a propriedade do capital da sua gestão funcional. O acionista é proprietário '
        'sem função produtiva, e a direção é exercida por administradores assalariados. O '
        'capital assume forma diretamente social no interior do próprio capitalismo, tema que '
        'Marx desenvolve no Livro III como a forma mais acabada do capital e, ao mesmo tempo, '
        'a sua superação no interior do modo de produção.'),
  ('b', 'Acelera enormemente a centralização, porque o controle pode ser adquirido pela compra '
        'de participações, sem necessidade de adquirir empresas integralmente.'),

  ('h', '5. A articulação entre os dois processos'),
  ('p', 'A centralização não substitui a acumulação, ela potencia os seus efeitos. Ao permitir '
        'a ampliação súbita da escala de produção, acelera e amplia a revolução na composição '
        'técnica do capital, elevando c em relação a v em ritmo muito superior ao que a '
        'acumulação isolada permitiria. Em consequência, intensifica a repulsão de '
        'trabalhadores e a produção da superpopulação relativa. Enquanto a acumulação simples '
        'eleva a composição orgânica gradualmente, a centralização produz saltos técnicos que '
        'tornam massas de trabalhadores subitamente supérfluas. Concentração e centralização '
        'são, portanto, mediações indispensáveis entre a acumulação e a produção do exército '
        'industrial de reserva.'),
 ],
},

{
 'depois': 71,
 'rotulo': 'Resposta 18 (cap. 23). A funcionalidade do exército industrial de reserva',
 'blocos': [
  ('h', 'Preliminar. Em que sentido a população é "excedente"'),
  ('p', 'A superpopulação relativa não é excedente em relação aos meios de subsistência '
        'disponíveis, como supõe Malthus. É excedente em relação às **necessidades médias de '
        'valorização do capital**. A população é declarada supérflua por um critério social '
        'determinado, a rentabilidade, e não por um limite natural. E ela é produzida pela '
        'própria acumulação, por meio da elevação da composição orgânica. A funcionalidade '
        'decorre justamente dessas duas características.'),

  ('h', '1. Fornece a elasticidade que a acumulação exige'),
  ('p', 'A acumulação capitalista não é movimento uniforme. Ela se dá em saltos, por ramos, '
        'por regiões, e segue o ciclo industrial com suas fases de prosperidade, '
        'superprodução, crise e estagnação. Nas fases de expansão e na abertura de novos '
        'ramos, o capital precisa lançar massas de trabalhadores em pontos decisivos, '
        'subitamente e sem retirá-los dos ramos já em funcionamento. Isso só é possível se '
        'existir um contingente disponível, não empregado, pronto a ser absorvido. O exército '
        'de reserva é esse reservatório, e é ele que torna a oferta de trabalho elástica, '
        'desligando-a dos limites naturais do crescimento populacional, que é lento e sujeito '
        'a defasagens de uma geração.'),

  ('h', '2. Regula os salários'),
  ('p', 'A pressão dos desempregados sobre os empregados mantém o salário dentro dos limites '
        'compatíveis com a valorização do capital. Nas fases de expansão, a existência da '
        'reserva impede que a demanda crescente por trabalho eleve os salários ao ponto de '
        'comprometer a taxa de mais-valor. Nas fases de contração, o seu engrossamento os '
        'deprime. É nesse sentido que Marx afirma que os movimentos gerais do salário são '
        'regulados exclusivamente pela expansão e contração do exército industrial de '
        'reserva, correspondentes às mudanças periódicas do ciclo industrial, e não pelo '
        'movimento do número absoluto da população trabalhadora.'),

  ('h', '3. Disciplina a classe trabalhadora e enfraquece a resistência'),
  ('p', 'A existência de uma massa de trabalhadores disponíveis acirra a concorrência entre os '
        'próprios trabalhadores. Quem está empregado sabe que pode ser substituído, com '
        'efeitos precisos.'),
  ('b', 'Reduz a capacidade de recusar jornadas longas, ritmos intensos e condições degradadas.'),
  ('b', 'Enfraquece a organização sindical e a eficácia das greves, pois o capital dispõe de '
        'substitutos imediatos.'),
  ('b', 'Permite impor a disciplina de fábrica com menor custo de coerção direta.'),
  ('p', 'A reserva opera, assim, como instrumento permanente de dominação na luta de classes, '
        'e não apenas como mecanismo de mercado.'),

  ('h', '4. Permite intensificar a exploração dos empregados, em círculo que se realimenta'),
  ('p', 'Marx destaca a conexão perversa entre as duas partes da classe. O trabalho excessivo '
        'da parte empregada engrossa as fileiras da parte desempregada, e a pressão desta '
        'obriga a parte empregada a aceitar trabalho ainda mais excessivo. Sobretrabalho de '
        'uns e desemprego forçado de outros se condicionam mutuamente, e ambos se tornam '
        'meios de enriquecimento do capitalista individual. É também por isso que o capital '
        'resiste tanto à redução da jornada, pois a distribuição do trabalho disponível entre '
        'mais trabalhadores reduziria a reserva e a sua eficácia disciplinadora.'),

  ('h', '5. Liberta o capital da dependência demográfica'),
  ('p', 'Como a acumulação produz a sua própria oferta de trabalho, o capital não fica '
        'subordinado ao ritmo do crescimento populacional. Ele cria e destrói disponibilidade '
        'de trabalho em prazos muito mais curtos do que a demografia opera. A lei de oferta e '
        'demanda de trabalho passa a funcionar dentro de limites que o próprio capital '
        'estabelece, o que é a base do argumento de que os dados estão viciados.'),

  ('h', '6. Sustenta a taxa de mais-valor'),
  ('p', 'Ao conter os salários e permitir maior intensidade e duração do trabalho, a reserva '
        'ajuda a elevar ou a sustentar a taxa de mais-valor, o que contrabalança parcialmente '
        'a pressão descendente que a elevação da composição orgânica exerce sobre a taxa de '
        'lucro.'),

  ('h', 'Observação final'),
  ('p', 'Reconhecer a funcionalidade não equivale a tratá-la como harmonia. A mesma '
        'superpopulação que serve ao capital constitui a forma de existência do pauperismo e '
        'da degradação, e Marx a apresenta como expressão do caráter antagônico da '
        'acumulação. As formas que ele distingue, flutuante, latente e estagnada, além do '
        'pauperismo propriamente dito, mostram que se trata de condição permanente e '
        'estruturada, e não de acidente conjuntural. A funcionalidade para o capital e a '
        'destrutividade para os trabalhadores são o mesmo fato visto de dois lados.'),
 ],
},

{
 'depois': 75,
 'rotulo': 'Resposta 19 (cap. 23). "Les dés sont pipés", a ação do capital sobre os dois lados',
 'blocos': [
  ('h', '1. O alvo da crítica'),
  ('p', 'A passagem se dirige à representação corrente, clássica e vulgar, do mercado de '
        'trabalho. Nessa representação, demanda e oferta de trabalho são duas potências '
        'independentes que se encontram no mercado e cuja interação determina o salário. A '
        'demanda seria dada pelo crescimento do capital, e a oferta pelo crescimento da '
        'população trabalhadora, regido por leis demográficas supostamente naturais, à '
        'maneira de Malthus. O salário seria, então, o resultado neutro do encontro de duas '
        'séries causais autônomas.'),
  ('p', 'Marx responde que o jogo é fraudulento, os dados estão viciados, porque as duas '
        'potências não são independentes. O capital age simultaneamente sobre os dois lados, '
        'de modo que o resultado do suposto encontro já está determinado por um único '
        'movimento, o da acumulação.'),

  ('h', '2. Como o capital atua sobre a demanda de trabalho'),
  ('d', 'A demanda depende de v, não de C||O que compra força de trabalho é o capital '
        'variável, e não o capital total. Essa distinção é o primeiro passo do argumento.'),
  ('d', 'A composição orgânica se eleva||Com o progresso da acumulação, v cresce menos que C e '
        'pode até decrescer em termos absolutos. Portanto a demanda de trabalho não é '
        'idêntica ao crescimento do capital, e um capital que cresce rapidamente pode '
        'demandar proporcionalmente menos trabalho, ou mesmo menos trabalho em termos '
        'absolutos.'),
  ('d', 'Mais trabalho sem mais trabalhadores||O capital pode ampliar a massa de trabalho que '
        'explora sem ampliar o número de trabalhadores, prolongando a jornada e '
        'intensificando o trabalho, conforme estabelecido no cap. 9. Mesmo a demanda por '
        'horas de trabalho não se traduz diretamente em demanda por trabalhadores.'),

  ('h', '3. Como o capital atua sobre a oferta de trabalho'),
  ('p', 'Este é o ponto que a representação corrente ignora por completo. A oferta de trabalho '
        'não é idêntica ao crescimento da classe trabalhadora, porque o capital a produz '
        'ativamente.'),
  ('d', 'Repulsão de trabalhadores empregados||A maquinaria e o aumento da produtividade '
        'tornam supérfluos trabalhadores em atividade, lançando-os no mercado. O capital não '
        'apenas encontra trabalhadores disponíveis, ele os fabrica.'),
  ('d', 'Proletarização de produtores independentes||A destruição do artesanato, da pequena '
        'produção rural e da indústria doméstica expropria camadas que viviam fora da relação '
        'assalariada e as converte em vendedores de força de trabalho.'),
  ('d', 'Incorporação de novas camadas||Mulheres e crianças são atraídas pela própria '
        'transformação técnica que dispensa força física e qualificação, ampliando a oferta '
        'sem qualquer alteração demográfica. O mesmo vale para o deslocamento de populações '
        'rurais, a superpopulação latente, e para os fluxos migratórios atraídos pela '
        'acumulação.'),
  ('d', 'Prolongamento e intensificação da jornada||O sobretrabalho dos empregados substitui o '
        'trabalho de outros e engrossa a reserva, além de desgastar prematuramente os '
        'trabalhadores e acelerar a sua substituição.'),
  ('d', 'Produção do exército industrial de reserva||É a síntese dos mecanismos anteriores, e '
        'constitui a oferta efetivamente relevante para o capital, aquela que pressiona os '
        'salários.'),

  ('h', '4. A conclusão'),
  ('p', 'Tanto a demanda quanto a oferta de trabalho são determinações internas do movimento '
        'do capital. O que aparece na superfície como livre jogo de duas forças de mercado é, '
        'na realidade, o automovimento do capital se desdobrando em dois lados. Por isso os '
        'salários são regulados pela expansão e contração do exército industrial de reserva, '
        'que é produto da acumulação, e não pelo movimento absoluto da população. A lei de '
        'oferta e demanda do trabalho continua operando, mas dentro de limites que o próprio '
        'capital estabelece, o que lhe retira o caráter de árbitro neutro. Daí decorre, para '
        'Marx, a necessidade da ação coletiva dos trabalhadores, da organização sindical e da '
        'legislação protetora, que constituem a tentativa de interferir num jogo cujas '
        'regras, deixadas ao mercado, já estão determinadas em favor do capital.'),

  ('h', '5. Por que a dinâmica da acumulação se sobrepõe à dinâmica demográfica'),
  ('d', 'Diferença de velocidade||O crescimento populacional é lento e opera com defasagens de '
        'uma geração entre o nascimento e o ingresso no mercado de trabalho. A acumulação '
        'pode mobilizar ou tornar supérflua uma massa enorme de trabalhadores em poucos anos, '
        'pela introdução de maquinaria, pela centralização de capitais ou pela abertura e '
        'fechamento de ramos inteiros. A variável rápida subordina a variável lenta.'),
  ('d', 'O que conta não é a população, é a disponibilidade||Pessoas existentes mas não '
        'disponíveis como força de trabalho não constituem oferta de trabalho. A conversão de '
        'população em oferta de trabalho é exatamente o que a acumulação realiza, por '
        'expropriação, por repulsão e por incorporação de novas camadas.'),
  ('d', 'Substituibilidade entre número e duração||Como visto no cap. 9, o capital pode '
        'ampliar a massa de trabalho explorado sem ampliar o número de trabalhadores, o que '
        'rompe o vínculo direto entre as necessidades do capital e o tamanho da população.'),
  ('d', 'A consequência teórica||Marx substitui a lei natural da população por uma lei '
        'histórica específica. Cada modo de produção tem a sua própria lei de população, e no '
        'capitalismo essa lei é a produção de uma superpopulação relativa pela acumulação. O '
        'excedente populacional deixa de ser fato natural que explica a miséria e passa a ser '
        'produto social que a acumulação engendra. A inversão é completa. Não é a população '
        'que pressiona os meios de subsistência, é o capital que produz a população excedente '
        'de que necessita, e a miséria resultante é efeito da riqueza, e não do seu '
        'contrário.'),
 ],
},

# ==================================================================== cap. 24
{
 'depois': 83,
 'rotulo': 'Resposta 20 (cap. 24, "A assim chamada acumulação primitiva")',
 'blocos': [
  ('h', '1. O que Marx está criticando'),
  ('p', 'A anedota do passado é a versão que a economia política dá da origem do capital, e '
        'Marx a trata como o equivalente, na economia, do pecado original na teologia. Nessa '
        'narrativa, a divisão entre proprietários e despossuídos resulta de diferenças de '
        'conduta, uns foram laboriosos, inteligentes e parcimoniosos, outros preguiçosos e '
        'dissipadores. Dois vícios lógicos estruturam o relato.'),
  ('b', 'Ele explica o resultado pelo próprio resultado, pressupondo como causa a desigualdade '
        'que deveria explicar.'),
  ('b', 'Ele naturaliza e moraliza um processo histórico determinado, apresentando como '
        'consequência de virtudes individuais aquilo que foi produto de expropriação violenta '
        'e de ação estatal sistemática.'),

  ('h', '2. O que a acumulação primitiva é, conceitualmente'),
  ('p', 'Ela não é acumulação resultante do modo de produção capitalista, é a acumulação que o '
        'precede e o constitui, o ponto de partida. O seu conteúdo é um processo de '
        '**separação**, a cisão entre o produtor e os meios de produção. A relação capitalista '
        'pressupõe duas condições que não existem naturalmente. De um lado, trabalhadores '
        'livres e despossuídos, obrigados a vender a sua força de trabalho. De outro, meios de '
        'produção e dinheiro concentrados em poucas mãos. A acumulação primitiva é o processo '
        'histórico que produz simultaneamente essas duas condições, e portanto a pré-história '
        'do capital.'),
  ('p', 'À anedota Marx contrapõe a sua tese sobre o processo efetivo. Na história real '
        'desempenham o papel principal a conquista, a escravização, o roubo e o assassinato, '
        'em suma, a violência. E a história dessa expropriação está inscrita nos anais da '
        'humanidade com traços de sangue e fogo.'),

  ('h', '3. a) A formação da classe trabalhadora'),
  ('p', 'O processo tem caráter duplo, e é essa duplicidade que importa. O produtor direto é '
        'liberado das relações de servidão e de dependência pessoal e, ao mesmo tempo, '
        'despojado dos seus meios de produção e de subsistência. Ele se torna livre em dois '
        'sentidos, livre da sujeição ao senhor e livre *de* propriedade. Sem o segundo, o '
        'primeiro não produziria assalariados. Os elementos concretos, tomados sobretudo do '
        'caso inglês, que Marx considera clássico:'),
  ('d', 'Dissolução dos séquitos feudais||O desmantelamento das relações de vassalagem lança '
        'no mercado massas de homens sem meios de vida.'),
  ('d', 'Expropriação da população rural||Cercamento das terras comuns, usurpação dos campos '
        'comunais, conversão de terras aráveis em pastagens para ovelhas sob o impulso da '
        'indústria da lã, e a prática da limpeza das propriedades, com demolição de casas de '
        'camponeses e expulsão de aldeias inteiras.'),
  ('d', 'Confisco dos bens da Igreja||A Reforma permite a venda ou doação dessas terras a '
        'preços nominais, eliminando um amparo tradicional dos pobres rurais. A isso se soma '
        'a usurpação dos domínios do Estado.'),
  ('d', 'A forma legal da expropriação||Nos séculos XVIII e XIX os *Bills for Inclosures of '
        'Commons* convertem o roubo em lei. Marx os chama de decretos pelos quais os senhores '
        'se presenteiam com as terras do povo, a forma parlamentar do roubo.'),
  ('d', 'As *clearances* das Terras Altas da Escócia||Populações inteiras são substituídas por '
        'criações de ovelhas e, depois, por reservas de caça, caso em que a violência aparece '
        'de forma particularmente nua.'),
  ('d', 'A legislação sanguinária||Os expropriados não se transformam espontaneamente em '
        'operários disciplinados. Convertem-se primeiro em vagabundos e mendigos, e é contra '
        'eles que se volta a legislação dos séculos XV a XVII, com açoitamento, marcação a '
        'ferro, mutilação, escravização e execução dos vagabundos sob Henrique VIII, Eduardo '
        'VI e Isabel. O objetivo é forçar os despossuídos ao trabalho assalariado.'),
  ('d', 'Compressão salarial por lei e proibição de coligações||Estatutos que fixam salários '
        'máximos e proíbem a associação de trabalhadores, vigentes na Inglaterra até o século '
        'XIX, mostram que o Estado atuou diretamente para rebaixar o preço do trabalho.'),
  ('d', 'A formação do mercado interno||A destruição da indústria doméstica rural e a '
        'separação entre agricultura e manufatura transformam os camponeses, que antes '
        'produziam os seus próprios meios de subsistência e instrumentos, em compradores de '
        'mercadorias, criando o mercado interno que o capital industrial requer.'),
  ('d', 'A duração do processo||Marx insiste que são necessários tempo e coerção prolongada '
        'para que a nova classe passe a considerar as exigências do modo de produção '
        'capitalista como leis naturais evidentes. A disciplina fabril é resultado histórico, '
        'não disposição espontânea.'),

  ('h', '4. b) A formação da classe capitalista'),
  ('p', 'A gênese do capitalista tem uma vertente interna à economia e outra externa, e a '
        'segunda é decisiva.'),
  ('h', 'Vertente interna'),
  ('d', 'O arrendatário capitalista||A sua gênese na agricultura inglesa foi favorecida por '
        'arrendamentos de longo prazo, pela desvalorização dos metais preciosos, que reduziu '
        'o valor real das rendas e dos salários fixados nominalmente, e pela usurpação das '
        'terras comuns, que lhe permitiu ampliar rebanho e capital sem desembolso.'),
  ('d', 'Conversão de mestres e comerciantes||Mestres de corporação e, principalmente, '
        'comerciantes e usurários se transformam em capitalistas industriais, processo em que '
        'o capital mercantil e o usurário preexistentes se convertem em capital industrial.'),
  ('h', 'Vertente externa, que Marx apresenta com ironia como o "idílio" da acumulação primitiva'),
  ('d', 'Pilhagem colonial||A descoberta da América e da rota marítima para as Índias, o saque '
        'das Índias Orientais, o extermínio e a escravização das populações indígenas, as '
        'minas de prata de Potosí.'),
  ('d', 'Tráfico de escravos e escravidão nas Américas||Marx menciona a transformação da '
        'África numa reserva para a caça comercial de pele negra. O comércio triangular e o '
        'crescimento de Liverpool e Bristol sobre o tráfico. A escravidão colonial como '
        'pedestal da indústria inglesa, inclusive materialmente, pois o algodão das '
        'plantações escravistas era a matéria-prima da indústria de Lancashire.'),
  ('d', 'O sistema colonial||Monopólios comerciais, a atuação das Companhias das Índias '
        'holandesa e inglesa, o monopólio do sal e do ópio, a arrecadação extorsiva em Bengala '
        'e as fomes que dela resultaram.'),
  ('d', 'A dívida pública||Marx a trata como uma das alavancas mais poderosas da acumulação '
        'primitiva. Ela transforma dinheiro improdutivo em capital, cria uma classe de '
        'rentistas que se apropria de receitas fiscais sem função produtiva, confere aos '
        'títulos a aptidão de circular como capital e dá origem ao sistema bancário moderno, '
        'às bolsas e à agiotagem de papéis.'),
  ('d', 'O sistema tributário moderno||Complemento necessário do endividamento. A sua '
        'incidência sobre os meios de subsistência expropria camponeses, artesãos e pequenos '
        'produtores, acelerando a proletarização.'),
  ('d', 'Protecionismo e guerras comerciais||Meios artificiais de fabricar fabricantes, de '
        'expropriar trabalhadores independentes e de capitalizar os meios nacionais de '
        'produção.'),

  ('h', '5. O papel do Estado e da violência'),
  ('p', 'O fio que une todos esses elementos é a ação sistemática do poder estatal. A '
        'expropriação não foi obra do mercado, e sim de leis, decretos, tribunais, exércitos, '
        'frotas e companhias privilegiadas. É nesse contexto que se entende a formulação de '
        'Marx, a violência é a parteira de toda sociedade velha que está grávida de uma nova, '
        'e ela mesma é uma potência econômica. O enunciado desfaz a oposição entre economia e '
        'política que a anedota pressupõe, pois mostra que a constituição das próprias '
        'relações econômicas foi obra de poder político concentrado.'),

  ('h', '6. O fechamento do argumento'),
  ('p', 'A conclusão polêmica do capítulo é a sentença de que o capital vem ao mundo escorrendo '
        'sangue e sujeira por todos os poros. Mais importante que a imagem é o resultado '
        'teórico. Se a separação entre produtores e meios de produção é histórica, e não '
        'natural, então ela é transitória, e a propriedade privada capitalista não tem '
        'fundamento em nenhum direito originário derivado do trabalho próprio.'),
  ('p', 'Marx conclui com a tendência histórica da acumulação, a expropriação dos '
        'expropriadores, na qual a propriedade privada fundada no trabalho próprio é primeiro '
        'negada pela propriedade capitalista, que por sua vez será negada pela propriedade '
        'social, movimento formulado como negação da negação. O capítulo seguinte, sobre a '
        'teoria moderna da colonização, confirma o argumento por outro caminho, pois mostra '
        'que nas colônias, onde o acesso à terra permanecia aberto, a relação capitalista não '
        'se estabelecia espontaneamente e precisava ser criada por meios artificiais e '
        'estatais, como a venda de terras a preços proibitivos para impedir que o trabalhador '
        'se tornasse proprietário.'),
 ],
},
]
