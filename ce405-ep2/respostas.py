# -*- coding: utf-8 -*-
"""
Respostas dissertativas e concisas da Lista de Questões I de Economia Política II
(CE405, turma C, 2025).

Referência: MARX, Karl. O Capital, Livro I. São Paulo: Boitempo. A numeração dos
capítulos (4, 5, 6, 7, 9, 10, 13, 21, 22, 23, 24) segue a edição Boitempo.

Calibragem: prova de 2 horas. Cada resposta tem no máximo 4 parágrafos, entre
cerca de 300 e 420 palavras, o que corresponde a algo entre 12 e 18 minutos de
redação à mão. Prosa corrida, sem tópicos, sem subtítulos e sem tabelas.

Critério de corte: preservar a tese, o mecanismo causal e as qualificações que
diferenciam a resposta. Suprimir ilustrações históricas extensas, exemplos
redundantes e reformulações da mesma ideia.

Estrutura dos dados
  RESPOSTAS é uma lista de dicionários, um por questão, com as chaves:
    'depois'     índice do parágrafo do .docx original após o qual a resposta entra
    'rotulo'     cabeçalho que amarra a resposta à questão
    'paragrafos' lista de parágrafos de prosa, no máximo 4

Marcação inline: **negrito** e *itálico*, usados com parcimônia.
"""

RESPOSTAS = [

# ===================================================================== cap. 4
{
 'depois': 4,
 'rotulo': 'Resposta 1 (cap. 4)',
 'paragrafos': [

  'Na circulação simples de mercadorias, representada por M–D–M, o ponto de partida e o de '
  'chegada são mercadorias, e o dinheiro funciona como meio de circulação, intermediário '
  'evanescente que é gasto definitivamente e não retorna a quem o despendeu. Como os '
  'extremos se equivalem em valor e diferem em utilidade, é essa diferença qualitativa que '
  'confere sentido à operação, pois trocar trigo por trigo seria absurdo. Daí decorre que a '
  'finalidade do movimento se situa fora da circulação, no consumo, e que o processo possui '
  'limite interno, já que se encerra com a satisfação da necessidade e a sua repetição '
  'depende do surgimento de outra. O valor, nesse percurso, apenas se conserva e muda de '
  'forma.',

  'Na circulação do dinheiro como capital, representada por D–M–D\', a estrutura se inverte '
  'termo a termo, pois os extremos são dinheiro e é a mercadoria que se torna o '
  'intermediário, uma vez que se compra para vender em lugar de vender para comprar. Sendo '
  'os extremos qualitativamente idênticos, eles só podem diferir em quantidade, e um '
  'retorno igual ao adiantamento seria tautológico, razão pela qual a forma só tem sentido '
  'se o refluxo exceder o adiantamento, diferença que Marx denomina mais-valor. O dinheiro '
  'não é gasto mas adiantado, pois reflui acrescido, o que distingue o capitalista do '
  'entesourador, que o subtrai da circulação. A finalidade passa a ser interna ao próprio '
  'movimento, pois é a valorização do valor, e o valor de uso comparece apenas como '
  'portador necessário do valor. Por isso o movimento perde todo limite interno, visto que '
  'a quantidade de valor não conhece saciedade e D\' é sempre o início de um novo ciclo.',

  'Quanto à maneira de introduzir a categoria, o procedimento de Marx é deliberadamente '
  'formal, e nisso reside a sua originalidade. O capital não é definido como um conjunto de '
  'coisas, dinheiro ou máquinas, e sim como um movimento, uma forma determinada de '
  'circulação, sendo D–M–D\' apresentada como a fórmula geral do capital tal como ele '
  'aparece imediatamente na esfera da circulação. O capital é, portanto, valor em processo, '
  'valor que se valoriza, e o valor se converte naquilo que Marx chama de sujeito '
  'automático do movimento, assumindo e abandonando alternadamente as formas dinheiro e '
  'mercadoria enquanto se conserva e se amplia. O capitalista é derivado dessa forma e não '
  'o contrário, pois comparece como capital personificado, cujo fim subjetivo, o '
  'enriquecimento abstrato, coincide com o fim objetivo da estrutura, de modo que a '
  'acumulação sem termo deixa de ser explicada por um vício moral e passa a ser exigência '
  'objetiva.',

  'Convém observar que essa introdução é provisória por desígnio. Marx expõe D–M–D\' como '
  'ela se apresenta na superfície justamente para demonstrar, em seguida, que mantida no '
  'plano da circulação a forma é contraditória, pois a troca de equivalentes não pode '
  'explicar o incremento de valor. É esse impasse que impõe a passagem à esfera da produção '
  'e a descoberta da mercadoria força de trabalho.',
 ],
},

{
 'depois': 8,
 'rotulo': 'Resposta 2 (cap. 4)',
 'paragrafos': [

  'O primeiro termo da contradição afirma que o mais-valor não pode ter origem na '
  'circulação. Trocando-se as mercadorias pelos seus valores, a circulação é mera '
  'metamorfose de forma e nenhuma grandeza nova é criada. As hipóteses de troca desigual '
  'igualmente fracassam, pois se todos os vendedores vendem acima do valor todos também '
  'compram acima dele, de maneira que o ganho é apenas nominal e o que se altera é a '
  'denominação dos preços, e se apenas um vendedor privilegiado o faz, ele ganha exatamente '
  'aquilo que o comprador perde, havendo transferência de valor preexistente e não criação '
  'de valor novo. Fraude e monopólio comercial explicam fortunas individuais, mas não '
  'explicam o enriquecimento da classe capitalista em conjunto, que não poderia enriquecer '
  'trocando consigo mesma.',

  'O segundo termo afirma que o mais-valor tampouco pode ter origem fora da circulação. '
  'Fora dela o produtor relaciona-se apenas com a sua própria mercadoria e pode criar valor '
  'mediante o seu trabalho, mas não mais-valor, porque não existe aí relação alguma que '
  'permita apropriar trabalho alheio não pago, e o possuidor de dinheiro não produz o '
  'incremento com trabalho próprio. Acrescente-se que o capital precisa necessariamente '
  'atravessar a circulação, já que nela adquire os seus elementos e nela realiza o '
  'mais-valor em dinheiro. Daí a formulação citada, segundo a qual o capital tem de ter '
  'origem na circulação e simultaneamente não ter origem nela, formulação que exige '
  'articular os dois termos em vez de sacrificar um deles.',

  'A solução consiste em localizar, dentro da circulação e sem violar a lei do valor, uma '
  'mercadoria cujo consumo, que se dá fora dela, produza mais valor do que ela própria '
  'vale. Essa mercadoria é a força de trabalho, e todo o argumento repousa na distinção '
  'entre força de trabalho e trabalho. O trabalho é dispêndio efetivo e não tem valor, pois '
  'ele é a substância do valor, enquanto a força de trabalho é a capacidade de trabalhar, '
  'mercadoria cujo valor é determinado, como o de qualquer outra, pelo tempo de trabalho '
  'socialmente necessário à sua reprodução, isto é, pelo valor dos meios de subsistência do '
  'trabalhador e da sua família, determinação na qual intervém um elemento histórico e '
  'moral. O capitalista a compra na circulação pagando o seu valor integral, sem fraude e '
  'sem troca desigual, o que é decisivo, porque mostra que a exploração não depende de '
  'nenhuma irregularidade na troca. Ocorre que o seu valor de uso é singular, pois '
  'consumi-la significa pôr o trabalhador a trabalhar, e trabalhar é criar valor, sendo '
  'esta a única mercadoria cujo valor de uso consiste em ser fonte de valor.',

  'O ponto decisivo é que o valor pago e o valor criado se determinam de modo independente, '
  'pois o primeiro depende do custo de reprodução do trabalhador e o segundo da duração e '
  'da intensidade da jornada, e nada na equivalência da troca obriga a jornada a cessar no '
  'ponto em que o trabalhador repõe o valor da sua força de trabalho. Se este equivale a '
  'seis horas e a jornada contratada é de doze, as seis primeiras constituem trabalho '
  'necessário e as seis restantes trabalho excedente, fonte do mais-valor. A contradição se '
  'resolve, assim, porque a compra e a venda ocorrem na circulação, razão pela qual o '
  'capital tem origem nela, enquanto a criação do mais-valor ocorre na produção, razão pela '
  'qual não tem origem nela. Historicamente, isso pressupõe que o trabalhador seja livre '
  'para vender a sua força de trabalho por tempo determinado e esteja separado dos meios de '
  'produção, condições produzidas pela acumulação primitiva, e explica a ironia final do '
  'capítulo sobre o abandono do éden dos direitos inatos do homem para o ingresso na '
  'produção, onde só se entra a negócios.',
 ],
},

# ===================================================================== cap. 5
{
 'depois': 12,
 'rotulo': 'Resposta 3 (cap. 5)',
 'paragrafos': [

  'As cinco categorias se articulam em torno do duplo caráter do trabalho, e o capítulo '
  'consiste em mostrar que o processo de produção capitalista é a unidade de duas '
  'determinações do mesmo ato. Marx examina primeiro o processo de trabalho '
  'independentemente de qualquer forma social, como condição eterna da vida humana e '
  'metabolismo entre o homem e a natureza, distinguindo nele três momentos simples, a '
  'atividade orientada a um fim, o objeto de trabalho e os meios de trabalho, sendo os dois '
  'últimos os meios de produção. Nesse processo o trabalho se objetiva, pois o trabalho '
  'vivo converte-se em trabalho morto fixado no produto, e o produto resultante é um valor '
  'de uso. Aqui o trabalho conta como trabalho concreto e útil, qualitativamente '
  'determinado, e é por ser trabalho útil determinado que ele consegue consumir '
  'produtivamente aqueles meios de produção e produzir aquele valor de uso específico.',

  'Sob a forma capitalista, porém, o processo de trabalho é apenas o meio, e o fim é a '
  'produção de valor e de mais-valor, pois o capitalista não produz para satisfazer '
  'necessidades mas para vender com acréscimo. Nesse segundo plano o trabalho conta como '
  'trabalho abstrato, dispêndio de força humana de trabalho em geral, indiferente à forma '
  'concreta e mensurável apenas pelo tempo, e é nessa determinação que ele cria valor. Marx '
  'distingue dois graus do mesmo processo, pois há processo de formação de valor enquanto o '
  'trabalho vivo apenas cria valor novo, e há processo de valorização quando esse mesmo '
  'processo se prolonga além do ponto em que o valor criado basta para repor o valor da '
  'força de trabalho. Quantitativamente, o valor do produto se decompõe no valor dos meios '
  'de produção consumidos, que é conservado e transferido, somado ao valor novo criado pelo '
  'trabalho vivo, havendo mais-valor sempre que este excede o valor da força de trabalho.',

  'O núcleo da articulação está em que não se trata de dois trabalhos, mas do mesmo '
  'trabalho sob duas determinações, com efeitos distintos sobre o valor. Como trabalho '
  'concreto, ele produz o valor de uso e, ao consumir os meios de produção conforme a sua '
  'finalidade, conserva e transfere ao produto o valor que neles estava objetivado. Como '
  'trabalho abstrato, ele cria valor novo e, além de certo ponto, mais-valor. O fiandeiro, '
  'ao fiar, produz fio e pelo mesmo ato adiciona valor, e é por isso que preserva o valor '
  'do algodão na medida em que o transforma. Daí o encadeamento das demais categorias, pois '
  'o trabalho é central por ser duplo, o valor de uso é resultado do processo de trabalho e '
  'condição material do valor, já que este requer portador corpóreo, e o valor é a '
  'objetivação do trabalho abstrato socialmente necessário.',

  'Os dois processos formam, portanto, uma unidade contraditória, porque a finalidade da '
  'valorização subordina e deforma o processo de trabalho, submetendo a técnica, a duração '
  'e a intensidade da jornada ao imperativo do excedente. Duas qualificações completam o '
  'quadro. O trabalho só cria valor na medida em que é socialmente necessário, de sorte que '
  'trabalho desperdiçado ou despendido abaixo da média social não cria valor proporcional, '
  'e o produto precisa ser valor de uso para outros, sem o que o trabalho se revela '
  'socialmente inútil e o valor não se valida na venda. Cabe registrar, por fim, a inversão '
  'que o capítulo anuncia, pois no processo de trabalho considerado em si é o trabalhador '
  'que usa os meios de produção, enquanto no processo de valorização são os meios de '
  'produção que, como capital, usam o trabalhador, convertendo-se em meios de absorção de '
  'trabalho alheio.',
 ],
},

# ===================================================================== cap. 6
{
 'depois': 19,
 'rotulo': 'Resposta 4 (cap. 6)',
 'paragrafos': [

  'Capital constante é a parte do valor-capital adiantada na compra de meios de produção, e '
  'Marx a qualifica como constante porque, no interior do processo de produção, ela não '
  'altera a sua grandeza de valor, sendo este apenas conservado e transferido ao produto, '
  'no qual reaparece sem acréscimo. Os seus componentes materiais típicos são o objeto de '
  'trabalho, que compreende as matérias-primas e brutas como algodão, ferro e minério, as '
  'matérias auxiliares, como combustível, lubrificantes e energia, que não compõem a '
  'substância do produto mas são consumidas no processo, e os meios de trabalho, que '
  'compreendem máquinas, ferramentas, instalações e edifícios.',

  'A sua contribuição ao valor da mercadoria é de transferência e nunca de criação, pois é o '
  'trabalho vivo, na sua determinação concreta, que conserva o valor dos meios de produção '
  'ao consumi-los produtivamente, fazendo-o reaparecer no produto. O modo da transferência '
  'difere conforme o componente, visto que matérias-primas e auxiliares são consumidas '
  'inteiramente em cada período e transferem todo o seu valor, enquanto máquinas e '
  'instalações seguem funcionando integralmente na sua forma material por muitos períodos e '
  'cedem valor apenas na medida do desgaste, diferença que fundamenta a distinção posterior '
  'entre capital circulante e capital fixo. Há também um limite rigoroso, pois o valor '
  'transferido nunca excede o valor que os meios de produção possuíam. Quanto à criação de '
  'mais-valor, a contribuição do capital constante é nula, uma vez que ele é condição '
  'material indispensável, já que sem meios de produção não há processo de trabalho, mas '
  'não é fonte de valor novo, cabendo-lhe função passiva de meio pelo qual o trabalho vivo '
  'é absorvido.',

  'Capital variável é a parte do valor-capital adiantada na compra da força de trabalho, '
  'isto é, o fundo de salários, e Marx a qualifica como variável porque, no curso do '
  'processo, ela altera a sua grandeza de valor, já que o valor adiantado é reposto pelo '
  'trabalhador e além dele é produzido um excedente. O seu componente material é a força de '
  'trabalho dos assalariados, convertendo-se materialmente nos meios de subsistência pelos '
  'quais eles reproduzem a sua capacidade de trabalho. É pela mobilização do trabalho vivo '
  'comprado com essa parte do capital que se cria valor novo, grandeza que Marx designa '
  'produto de valor e que corresponde à soma de v e m, sendo v o equivalente reposto e m o '
  'excedente. A sua contribuição à criação do mais-valor é exclusiva, pois o mais-valor '
  'provém apenas do trabalho vivo e, portanto, apenas da parte do capital que compra a '
  'única mercadoria cujo valor de uso consiste em criar valor. Convém a precisão de que não '
  'é o capital variável, como soma de valor, que cria o mais-valor, e sim o trabalho vivo '
  'que ele põe em movimento.',

  'Dessas determinações resulta a decomposição do valor da mercadoria na soma de c, v e m, '
  'em que c é valor preexistente que apenas reaparece enquanto v somado a m constitui o '
  'valor novo criado no período. Importa notar que a distinção entre capital constante e '
  'variável é qualitativa e diz respeito ao papel na valorização, não se confundindo com a '
  'distinção entre capital fixo e circulante, que deriva do modo de rotação do valor, de '
  'sorte que matérias-primas são capital constante e circulante ao mesmo tempo. O par '
  'conceitual cumpre, sobretudo, função crítica, pois para o capitalista todo desembolso '
  'aparece como adiantamento homogêneo e o excedente aparece como rendimento do capital '
  'total, expresso na taxa de lucro, sendo essa indistinção a base objetiva da aparência de '
  'que o lucro nasce do capital como tal. Ao separar c de v, Marx demonstra que o excedente '
  'tem fonte determinada no trabalho excedente não pago e que a taxa de lucro oculta o grau '
  'de exploração, tendo sido justamente a ausência dessa distinção o que impediu a economia '
  'política clássica de explicar consistentemente a origem do excedente.',
 ],
},

# ===================================================================== cap. 7
{
 'depois': 25,
 'rotulo': 'Resposta 5 (cap. 7)',
 'paragrafos': [

  'A primeira fórmula expressa a taxa de mais-valor em termos de valores. Marx parte do '
  'valor da mercadoria, que se decompõe na soma de c, v e m, e observa que, sendo c valor '
  'meramente transferido e não criado no processo, é preciso subtraí-lo para isolar aquilo '
  'que foi efetivamente produzido, restando o produto de valor, dado pela soma de v e m. A '
  'taxa de mais-valor é então a razão entre o mais-valor e o capital variável, isto é, m '
  'sobre v. O essencial é que o denominador seja o capital variável e não o capital total, '
  'pois o sentido da fórmula consiste em medir o grau de valorização justamente daquela '
  'parte do capital que se valoriza.',

  'A segunda fórmula expressa a mesma relação em termos de tempos de trabalho, tomando a '
  'jornada na sua divisão interna. A jornada se decompõe em tempo de trabalho necessário, '
  'no qual o trabalhador produz o equivalente ao valor da sua força de trabalho, e tempo de '
  'trabalho excedente, no qual produz valor sem contrapartida, de modo que a taxa de '
  'mais-valor é a razão entre o trabalho excedente e o trabalho necessário. As duas '
  'fórmulas expressam a mesma relação porque v é a forma-valor do trabalho necessário e m é '
  'a forma-valor do trabalho excedente, e Marx estabelece explicitamente a identidade entre '
  'as razões, observando que ambas dizem o mesmo, uma em trabalho objetivado, já '
  'cristalizado em valor, e a outra em trabalho fluente, trabalho vivo em processo. A '
  'primeira apresenta a relação tal como ela aparece no resultado, a segunda a apresenta na '
  'atividade de que resulta.',

  'Importa justificar por que Marx insiste na taxa de mais-valor e não na taxa de lucro. A '
  'razão entre m e v mede o grau de exploração porque confronta diretamente o trabalho não '
  'pago com o trabalho pago, constituindo, como diz a passagem citada, a expressão exata do '
  'grau de exploração da força de trabalho pelo capital. Já a razão entre m e o capital '
  'total dilui o mais-valor no conjunto do adiantamento e produz sempre um número menor, '
  'encobrindo a exploração, e é precisamente essa taxa de lucro que aparece na superfície e '
  'orienta o cálculo capitalista, sendo desenvolvida apenas no Livro III. Marx menciona '
  'ainda uma terceira expressão equivalente, a relação entre o mais-produto e a parte do '
  'produto correspondente ao trabalho necessário, que com produtividade dada reproduz em '
  'quantidades físicas a mesma proporção. É também neste capítulo que ele desmonta o '
  'argumento da última hora de Nassau Senior, mostrando que o erro consiste exatamente em '
  'confundir essas grandezas, calculando o excedente sobre o valor total do produto em vez '
  'de sobre o capital variável.',
 ],
},

{
 'depois': 27,
 'rotulo': 'Resposta 6 (cap. 7)',
 'paragrafos': [

  'As grandezas propostas são exatamente aquelas que Marx utiliza no capítulo. O valor do '
  'capital total adiantado corresponde à soma do capital constante e do variável, isto é, '
  '410 somado a 90, resultando em **500**, não entrando nesse cálculo o mais-valor, que é '
  'resultado do processo e não adiantamento. O valor do produto corresponde à soma das três '
  'grandezas, 410 somado a 90 e a 90, resultando em **590**, e é a maior delas porque '
  'inclui o valor preexistente transferido dos meios de produção. O produto de valor '
  'corresponde apenas à soma de v e m, isto é, 90 somado a 90, resultando em **180**, '
  'grandeza que se obtém igualmente subtraindo c do valor do produto, pois 590 menos 410 '
  'resulta em 180, e que expressa somente o valor novo criado pelo trabalho vivo no '
  'período. A taxa de mais-valor, finalmente, é a razão entre o mais-valor e o capital '
  'variável, 90 divididos por 90, o que resulta em **100 por cento**.',

  'A taxa de 100 por cento significa que o trabalhador produz, em trabalho excedente, '
  'exatamente o mesmo valor que produz em trabalho necessário, de sorte que a jornada se '
  'divide em partes iguais, e numa jornada de doze horas seis repõem o valor da força de '
  'trabalho enquanto seis são apropriadas gratuitamente. O ponto central do exercício, '
  'porém, está na distinção entre valor do produto e produto de valor, sobre a qual Marx '
  'insiste porque a confusão entre as duas é fonte de erros graves. Quem tomasse 590 como '
  'base do cálculo obteria algo em torno de 15,25 por cento, número que não mede nenhuma '
  'relação determinada, visto que mistura no denominador valor criado com valor meramente '
  'transferido.',

  'Igualmente instrutiva é a comparação com a taxa de lucro, obtida dividindo o mais-valor '
  'pelo capital total, 90 sobre 500, o que resulta em 18 por cento. É esse o número que '
  'interessa ao capitalista e que figura na contabilidade, mas ele subestima drasticamente '
  'o grau de exploração, 18 por cento contra 100 por cento, e a divergência entre as duas '
  'taxas é tanto maior quanto maior for o peso do capital constante, isto é, quanto mais '
  'elevada for a composição orgânica do capital. Note-se, a título de complemento, que a '
  'relação entre c e v é de aproximadamente 4,56, o que significa que o capital adiantado '
  'se reparte em cerca de 82 por cento de capital constante e 18 por cento de capital '
  'variável, composição característica de produção já mecanizada.',
 ],
},

{
 'depois': 29,
 'rotulo': 'Resposta 7 (cap. 7)',
 'paragrafos': [

  'A consequência esperada é a elevação da taxa de mais-valor, mas o mecanismo é indireto e '
  'passa pelo valor da força de trabalho, razão pela qual é preciso reconstituir a cadeia '
  'causal inteira. A inovação técnica eleva a força produtiva do trabalho, de modo que a '
  'mesma quantidade de trabalho passa a produzir uma massa maior de produtos. Em '
  'consequência, cai o tempo de trabalho socialmente necessário por unidade de mercadoria '
  'e, com ele, o valor unitário das mercadorias, já que o valor varia em razão inversa à '
  'produtividade. Se essa queda atinge as mercadorias que compõem o consumo dos '
  'trabalhadores, cai o valor dos meios de subsistência e, por consequência, o valor da '
  'força de trabalho. Dada a jornada, essa redução encurta o tempo de trabalho necessário e '
  'amplia na mesma medida o tempo de trabalho excedente, de sorte que m aumenta enquanto v '
  'diminui e a razão entre ambos se eleva por efeito combinado. Numa jornada de doze horas '
  'com seis necessárias a taxa é de 100 por cento, e um avanço que reduza o trabalho '
  'necessário a quatro horas a eleva a 200 por cento sem que a jornada tenha aumentado um '
  'minuto. Esse é o mecanismo do mais-valor relativo.',

  'Para o capitalista individual que inova primeiro, o efeito é mais direto, pois ele '
  'produz com valor individual inferior ao valor social vigente, vende ao valor social ou '
  'pouco abaixo dele e se apropria de um mais-valor extra. Tal vantagem é transitória, já '
  'que desaparece quando a técnica se generaliza e o novo valor social, mais baixo, se '
  'impõe, mas é exatamente essa recompensa temporária que impulsiona cada capitalista a '
  'inovar, produzindo como resultado agregado e não intencional a queda geral do valor das '
  'mercadorias.',

  'Três qualificações precisam acompanhar a resposta. A elevação da taxa pressupõe que o '
  'salário real não aumente na mesma proporção da produtividade, pois se o trabalhador '
  'passa a consumir proporcionalmente mais valores de uso a taxa pode não se alterar, de '
  'maneira que a repartição dos ganhos de produtividade é objeto de luta de classes e não '
  'um dado técnico. Inovações em ramos que não produzem bens de consumo dos trabalhadores '
  'nem os seus insumos proporcionam mais-valor extra ao inovador mas não elevam a taxa '
  'geral de mais-valor. E, mais importante teoricamente, a inovação produz efeito oposto '
  'sobre a taxa de lucro, porque aumenta a massa de meios de produção posta em movimento '
  'por cada trabalhador e eleva a composição orgânica do capital, o que, dada a taxa de '
  'mais-valor, reduz a razão entre o mais-valor e o capital total. Essa divergência, taxa '
  'de mais-valor crescente acompanhada de taxa de lucro tendencialmente declinante, é '
  'desenvolvida no Livro III e já está implícita aqui, na medida em que a mesma '
  'transformação técnica que intensifica a exploração corrói a rentabilidade.',
 ],
},

# ===================================================================== cap. 9
{
 'depois': 35,
 'rotulo': 'Resposta 8 (cap. 9)',
 'paragrafos': [

  'A passagem se insere na análise da relação entre a taxa e a massa de mais-valor. A massa '
  'de mais-valor produzida por um capital resulta da taxa de mais-valor multiplicada pelo '
  'capital variável total, ou, em termos de trabalho, do mais-valor extraído de um '
  'trabalhador médio multiplicado pelo número de trabalhadores empregados. Disso decorre o '
  'ponto da passagem, pois a quantidade de trabalho que um capital pode explorar é o '
  'produto de dois fatores, uma grandeza extensiva, que é o número de trabalhadores, e uma '
  'grandeza de duração e intensidade, que é a quantidade de trabalho extraída de cada um. '
  'Tratando-se de um produto, os dois fatores são, dentro de certos limites, substituíveis '
  'entre si, de modo que a redução no número de trabalhadores pode ser compensada pelo '
  'prolongamento da jornada ou pela intensificação do trabalho.',

  'Daí a conclusão que a passagem formula. O capital não depende estritamente do número de '
  'trabalhadores disponíveis para ampliar a massa de trabalho que explora e, portanto, a '
  'massa de mais-valor que extrai, pois pode aumentar a quantidade de trabalho explorado '
  'mantendo, ou mesmo reduzindo, o número de trabalhadores, bastando que faça cada um '
  'trabalhar mais tempo ou com maior intensidade. Nesse sentido, a oferta de trabalho, '
  'entendida como a massa de trabalho efetivamente à disposição do capital, torna-se '
  'relativamente independente da oferta de trabalhadores, isto é, do tamanho da população '
  'trabalhadora. Um capital que emprega cem trabalhadores por oito horas mobiliza '
  'oitocentas horas, e pode mobilizar as mesmas oitocentas empregando oitenta trabalhadores '
  'por dez horas.',

  'A ressalva contida na expressão dentro de certos limites é, no entanto, a parte decisiva, '
  'e Marx a desenvolve como uma lei. A jornada possui limite absoluto, pois não pode '
  'exceder as vinte e quatro horas do dia e, muito antes disso, encontra limites '
  'fisiológicos de resistência do trabalhador e limites legais conquistados pela luta de '
  'classes. Esse limite estabelece uma barreira à compensação, uma vez que o mais-valor '
  'extraível de cada trabalhador não pode exceder a jornada máxima descontado o tempo de '
  'trabalho necessário, de sorte que, sendo este de seis horas e a jornada máxima tolerável '
  'de dezoito, o mais-valor máximo por trabalhador equivale a doze horas, qualquer que seja '
  'a pressão exercida. Marx formula exatamente essa lei ao afirmar que a barreira absoluta '
  'da jornada média constitui barreira absoluta à compensação da redução do capital '
  'variável pelo aumento da taxa de mais-valor. Existe, assim, assimetria essencial entre '
  'os dois fatores, pois aumentar o número de trabalhadores amplia a massa de mais-valor '
  'sem limite interno, enquanto intensificar a exploração sobre um número menor encontra '
  'teto rígido.',

  'As consequências explicam a importância da passagem na arquitetura da obra. Ela '
  'fundamenta o impulso permanente do capital ao prolongamento da jornada e à intensificação '
  'do trabalho, que deixa de ser atribuído à ganância pessoal e passa a ser compreendido '
  'como a forma pela qual um capital de magnitude dada amplia a massa de mais-valor. '
  'Esclarece também por que a introdução de maquinaria, ao reduzir o número de '
  'trabalhadores, não implica necessariamente redução da massa de mais-valor, visto que o '
  'capital compensa a queda do capital variável com a elevação da taxa. E antecipa o '
  'capítulo 23, pois se a massa de trabalho explorável pode crescer sem crescimento da '
  'população, então a dinâmica do capital se desliga da dinâmica demográfica e a oferta de '
  'trabalho deixa de ser variável independente determinada pela natureza.',
 ],
},

# ==================================================================== cap. 10
{
 'depois': 39,
 'rotulo': 'Resposta 9 (cap. 10)',
 'paragrafos': [

  'A resposta exige recuperar a distinção que o capítulo estabelece. O mais-valor absoluto é '
  'obtido pelo prolongamento da jornada além do ponto em que o trabalhador repõe o valor da '
  'sua força de trabalho, permanecendo dado o tempo de trabalho necessário. O mais-valor '
  'relativo é obtido com jornada dada, e mesmo reduzida, pela contração do tempo de '
  'trabalho necessário, o que amplia na mesma medida o tempo de trabalho excedente. Estando '
  'a jornada fixada, existe um único caminho disponível, que consiste em reduzir o tempo de '
  'trabalho necessário, e isso exige reduzir o valor da força de trabalho, o que por sua '
  'vez exige reduzir o valor das mercadorias que o determinam, sendo o único meio de fazê-lo '
  'a elevação da força produtiva do trabalho que as produz. O expediente adotado é, '
  'portanto, a revolução permanente das condições técnicas e sociais do processo de '
  'produção com o objetivo de aumentar a produtividade do trabalho.',

  'Esse expediente assume formas concretas que os capítulos seguintes desenvolvem. A '
  'cooperação consiste na reunião de muitos trabalhadores no mesmo processo, o que gera '
  'força produtiva social superior à soma das forças individuais e permite economias no uso '
  'dos meios de produção. A divisão do trabalho na manufatura consiste na decomposição do '
  'ofício em operações parciais, o que especializa o trabalhador e eleva a destreza ao custo '
  'da sua mutilação. A maquinaria e a grande indústria consistem na substituição da base '
  'subjetiva do ofício por um sistema objetivo de máquinas, e constituem a forma mais '
  'desenvolvida e especificamente capitalista do expediente. A intensificação do trabalho, '
  'mecanismo correlato, aumenta o dispêndio de trabalho por unidade de tempo e torna-se '
  'central quando a jornada passa a ser legalmente limitada.',

  'É preciso notar que nenhum capitalista individual age com o propósito de reduzir o valor '
  'da força de trabalho, pois o seu móvel imediato é o mais-valor extra. Quem adota um '
  'método superior produz com valor individual inferior ao valor social, vende ao valor '
  'social ou pouco abaixo dele, realiza mais-valor acima da média e amplia o seu mercado às '
  'custas dos concorrentes. Tal vantagem é transitória, dissolvendo-se quando o método se '
  'generaliza por força da concorrência e estabelece novo valor social mais baixo, momento '
  'em que o mais-valor extra individual desaparece, embora o resultado social permaneça, já '
  'que o valor das mercadorias caiu. Se essas mercadorias determinam o valor da força de '
  'trabalho, o mais-valor relativo se torna geral e se incorpora às condições normais da '
  'produção, de modo que o resultado coletivo é efeito não intencional da busca individual '
  'de vantagem.',

  'A conclusão metodológica merece registro, pois o mais-valor relativo explica por que o '
  'capital é intrinsecamente dinâmico e revolucionário no plano técnico. A busca de '
  'excedente deixa de depender apenas do prolongamento da jornada, limite que a resistência '
  'operária e a legislação acabam por fixar, e passa a depender da transformação incessante '
  'do processo produtivo. Marx destaca a inversão característica dessa dinâmica, pois o '
  'impulso imanente do capital a elevar a força produtiva do trabalho não existe para '
  'reduzir o esforço humano, e sim para baratear a mercadoria e encurtar a parte da jornada '
  'que pertence ao trabalhador.',
 ],
},

{
 'depois': 41,
 'rotulo': 'Resposta 10 (cap. 10)',
 'paragrafos': [

  'Devem ter o seu valor reduzido as mercadorias que entram no consumo habitual dos '
  'trabalhadores, isto é, os meios de subsistência necessários à reprodução da força de '
  'trabalho, o que abrange alimentos, vestuário, habitação e em geral os bens que compõem o '
  'padrão de consumo socialmente estabelecido da classe trabalhadora.',

  'A razão está na determinação do valor da força de trabalho. Como qualquer mercadoria, '
  'ela tem o seu valor determinado pelo tempo de trabalho socialmente necessário à sua '
  'produção e reprodução, o que significa, concretamente, pelo valor dos meios de '
  'subsistência necessários para manter o trabalhador e reproduzir a sua família, e o tempo '
  'de trabalho necessário da jornada é precisamente aquele em que o trabalhador produz o '
  'equivalente a esse valor. Da queda do valor dos meios de subsistência decorre, portanto, '
  'a queda do valor da força de trabalho, dela o encurtamento do tempo de trabalho '
  'necessário e, dada a jornada, a ampliação na mesma medida do tempo de trabalho '
  'excedente, com o que o mais-valor relativo é obtido. Nenhum outro tipo de mercadoria '
  'produz esse efeito, pelo simples motivo de que nenhum outro entra na determinação do '
  'valor da força de trabalho. O raciocínio se estende, por mediação, aos meios de produção '
  'empregados na produção desses bens, pois o barateamento de fertilizantes, de transporte '
  'ou de fios e tecidos reduz o valor dos alimentos e do vestuário e, por via indireta, o '
  'valor da força de trabalho.',

  'O contraste que confirma o argumento é esclarecedor. Um salto de produtividade na '
  'produção de bens de luxo, que não entram no consumo dos trabalhadores, barateia esses '
  'bens e proporciona mais-valor extra ao capitalista que inova primeiro, mas não altera o '
  'valor da força de trabalho e, por isso, não gera mais-valor relativo para o capital '
  'social. Esse contraste demonstra que o mais-valor relativo não decorre do aumento da '
  'produtividade em geral, e sim do aumento da produtividade nos setores que determinam o '
  'custo de reprodução do trabalhador. Daí se compreende a importância estratégica que os '
  'ramos produtores de bens de consumo popular assumem no capitalismo, e também por que o '
  'preço dos alimentos é historicamente objeto de conflito direto entre capital e trabalho '
  'e mesmo entre frações da classe dominante, sendo a revogação das Leis do Trigo na '
  'Inglaterra o exemplo clássico.',

  'Cabe qualificar, por fim, que o resultado pressupõe que o barateamento se traduza em '
  'queda do valor da força de trabalho, e não em elevação do padrão de consumo real dos '
  'trabalhadores a valor constante. Contendo a determinação do valor da força de trabalho um '
  'elemento histórico e moral, a repartição dos ganhos de produtividade depende da relação '
  'de forças entre as classes, e historicamente observam-se as duas coisas em conjunto, '
  'elevação do consumo real dos trabalhadores e elevação simultânea da taxa de mais-valor.',
 ],
},

# ==================================================================== cap. 13
{
 'depois': 45,
 'rotulo': 'Resposta 11 (cap. 13)',
 'paragrafos': [

  'A relevância da maquinaria não é, para Marx, de ordem meramente técnica, pois ela é o '
  'meio pelo qual o capital constrói uma base material adequada a si mesmo e reorganiza '
  'integralmente o processo produtivo, sendo tratada no capítulo como a forma mais '
  'desenvolvida de produção de mais-valor relativo. O primeiro ponto é o da finalidade, já '
  'que a maquinaria não é introduzida para aliviar o trabalho, mas para baratear '
  'mercadorias e encurtar a parte da jornada em que o trabalhador trabalha para si. Dessa '
  'finalidade decorre um critério econômico preciso, pois a máquina só é adotada quando o '
  'valor que ela transfere ao produto é menor que o valor da força de trabalho que '
  'substitui, do que resulta a consequência aparentemente paradoxal de que, onde a força de '
  'trabalho é muito barata, a maquinaria é adotada mais lentamente. Note-se que ela nunca '
  'adiciona ao produto mais valor do que perde pelo desgaste, razão pela qual não é fonte '
  'de valor mas capital constante.',

  'O ponto central é a inversão da relação entre o trabalhador e o meio de trabalho. Na '
  'manufatura o princípio organizador é subjetivo, pois o processo é decomposto conforme a '
  'habilidade dos trabalhadores e se adapta a eles, permanecendo a destreza humana como '
  'ponto de partida. Na grande indústria o princípio torna-se objetivo, pois o sistema de '
  'máquinas existe como organismo técnico autônomo, com lógica e ritmo próprios, ao qual o '
  'trabalhador é incorporado. Marx formula a imagem ao dizer que na manufatura os '
  'trabalhadores são membros de um mecanismo vivo, enquanto na fábrica existe um mecanismo '
  'morto, independente deles, ao qual são incorporados como apêndices vivos. Essa inversão '
  'permite distinguir subsunção formal de subsunção real, pois enquanto o capital apenas se '
  'apropria de processos herdados do artesanato a subsunção é formal, e com a maquinaria ele '
  'transforma o processo desde dentro, criando um modo de produzir que não existiria sem '
  'ele, de sorte que a grande indústria é o primeiro modo de produção cuja base técnica '
  'corresponde à sua forma social.',

  'Os efeitos sobre a força de trabalho são de três ordens. A máquina dispensa força '
  'muscular e habilidade especializada, o que permite substituir o trabalhador adulto por '
  'mulheres e crianças, ampliando o material humano de exploração e reduzindo o valor da '
  'força de trabalho individual, já que toda a família passa a contribuir para a sua '
  'reprodução. Contra o que a intuição sugeriria, ela conduz ao prolongamento da jornada, '
  'pois o capital fixo precisa ser valorizado antes de ser desvalorizado moralmente pelo '
  'progresso técnico, e porque, elevando a composição orgânica e pressionando a taxa de '
  'lucro, leva o capital a buscar compensação na ampliação do trabalho excedente. E quando '
  'a legislação limita a duração da jornada, o capital desloca a pressão para a '
  'intensidade. A maquinaria funciona, além disso, como arma na luta de classes, pois ao '
  'tornar o trabalhador substituível desarma a sua resistência e é mobilizada para derrotar '
  'greves, alimentando a superpopulação relativa e aprofundando a separação entre trabalho '
  'manual e intelectual, já que o saber do processo se objetiva na máquina e confronta o '
  'trabalhador como poder alheio.',

  'Importa concluir registrando que Marx não condena a maquinaria em si, distinguindo a '
  'máquina do seu emprego capitalista, pois a grande indústria socializa o processo de '
  'produção, cria o trabalhador coletivo em escala inédita e desenvolve as forças '
  'produtivas a ponto de tornar possível uma organização social superior, de sorte que as '
  'mesmas condições que degradam o trabalhador criam os pressupostos da sua emancipação. Em '
  'síntese, a relevância da maquinaria consiste em ser simultaneamente o meio mais eficaz '
  'de produção de mais-valor relativo, o instrumento pelo qual o capital consuma a '
  'subsunção real do trabalho, a arma com que submete a resistência operária e produz a '
  'superpopulação relativa, e a base material a partir da qual se desenvolvem as '
  'contradições que apontam para além do capitalismo.',
 ],
},

# ==================================================================== cap. 21
{
 'depois': 49,
 'rotulo': 'Resposta 12 (cap. 21)',
 'paragrafos': [

  'Para que ocorra a reprodução simples, o capitalista deve consumir individualmente a '
  'totalidade do mais-valor, gastando-o como renda, sem que nenhuma fração dele seja '
  'convertida em capital adicional.',

  'A razão é imediata. Reprodução simples significa repetição do processo produtivo na mesma '
  'escala, período após período, o que exige que o capital adiantado no novo ciclo tenha '
  'exatamente a mesma magnitude do anterior. Sendo o valor do produto a soma de c, v e m, a '
  'parte correspondente a c deve ser reconvertida em meios de produção e a parte '
  'correspondente a v em força de trabalho, repondo materialmente e em valor as condições '
  'de produção na escala precedente, de modo que resta o mais-valor. Se este fosse total ou '
  'parcialmente capitalizado, o capital adiantado no ciclo seguinte seria maior e a escala '
  'se ampliaria, caracterizando reprodução ampliada. Para que a escala permaneça constante, '
  'portanto, o mais-valor precisa ser integralmente dissipado em consumo improdutivo do '
  'capitalista, isto é, em meios de consumo individual.',

  'Cabe observar que a reprodução simples é abstração deliberada, e não descrição da '
  'realidade. Marx a introduz justamente porque o capital tende por natureza a se ampliar, '
  'e congelar a escala permite isolar e tornar visível um resultado que a ampliação '
  'encobriria, a saber, que o processo reproduz a própria relação de classe. Trata-se do '
  'caso mais simples no qual a estrutura essencial aparece com nitidez.',

  'A hipótese revela, além disso, um resultado notável. Se o capitalista consome anualmente '
  'todo o mais-valor, basta certo número de anos para que tenha consumido valor igual ao '
  'capital originalmente adiantado, e a partir desse momento o capital que ainda possui é '
  'integralmente mais-valor capitalizado, isto é, trabalho alheio apropriado sem '
  'equivalente. O título jurídico de propriedade permanece o mesmo, mas o seu conteúdo '
  'econômico se inverteu por completo, pois ainda que o capital inicial tivesse origem no '
  'trabalho próprio do seu possuidor, a simples continuidade do processo o converte, em '
  'prazo determinado, em valor apropriado gratuitamente, o que desfaz qualquer legitimação '
  'da propriedade capitalista fundada na origem laboriosa do patrimônio.',
 ],
},

{
 'depois': 53,
 'rotulo': 'Resposta 13 (cap. 21)',
 'paragrafos': [

  'Considerado como ato isolado, o processo de produção aparece como produção de mercadorias '
  'e de mais-valor, mas considerado em sua continuidade, como processo de reprodução, ele '
  'revela algo mais, e é esse deslocamento de perspectiva que fundamenta a passagem citada. '
  'Todo processo social de produção é também processo de reprodução, pois precisa repor '
  'continuamente as suas próprias condições materiais e sociais, já que nenhuma sociedade '
  'pode produzir sem reproduzir os pressupostos de que parte. No caso do capital, esses '
  'pressupostos são a existência, de um lado, de possuidores de dinheiro e de meios de '
  'produção e, de outro, de possuidores apenas de força de trabalho, e é essa relação que o '
  'processo necessariamente reproduz.',

  'O que a continuidade revela com mais força diz respeito ao salário. No ato isolado da '
  'troca, ele aparece como dinheiro que o capitalista adianta do seu próprio fundo, e a '
  'transação se apresenta como troca de equivalentes entre proprietários livres. '
  'Considerado o processo em sua repetição, essa aparência se dissolve, porque o valor com '
  'que o capitalista paga o salário é parte do valor que o próprio trabalhador produziu no '
  'período anterior. O capital variável não é adiantamento feito a partir de fundo externo, '
  'e sim fração do produto do trabalho alheio devolvida ao trabalhador sob a forma de '
  'salário, sendo, como observa Marx, apenas a forma histórica particular de aparição do '
  'fundo de meios de subsistência que o trabalhador precisa para a sua conservação e que ele '
  'mesmo tem de produzir e reproduzir continuamente.',

  'Desse movimento resulta a reprodução simultânea das duas classes. Do lado do capitalista, '
  'o processo repõe e amplia a sua posse de meios de produção e de dinheiro, '
  'reproduzindo-o como personificação do capital e comprador de força de trabalho. Do lado '
  'do trabalhador, o processo o reproduz como assalariado em sentido duplo, pois reproduz a '
  'sua força de trabalho, mantendo-o apto a trabalhar, e reproduz a sua condição de '
  'despossuído, já que ele sai do processo tal como entrou, sem meios de produção e com nada '
  'além da necessidade de vender outra vez a sua capacidade de trabalho. A relação '
  'capitalista não é, portanto, pressuposto externo dado uma vez por todas, e sim algo '
  'continuamente produzido pelo próprio funcionamento do processo.',

  'O consumo do trabalhador desempenha nesse movimento papel de caráter duplo. No interior '
  'do processo de trabalho ele consome meios de produção, convertendo-os em produtos que '
  'pertencem ao capitalista, e esse consumo produtivo é diretamente produção para o '
  'capital. Fora do processo ele consome os meios de subsistência comprados com o salário, '
  'e esse consumo individual aparece como assunto privado seu, mas na perspectiva da '
  'reprodução revela-se momento necessário da reprodução do capital, pois ao consumir o '
  'trabalhador não produz nada além da sua própria força de trabalho, isto é, justamente a '
  'mercadoria de que o capital depende, sendo por isso, nas palavras de Marx, a produção do '
  'meio de produção mais indispensável ao capitalista. A condição decisiva é que esse '
  'consumo absorva integralmente o salário, não deixando excedente que lhe permita acumular '
  'e tornar-se independente, razão pela qual a reprodução da força de trabalho é também a '
  'reprodução da sua despossessão. Diferentemente do senhor de escravos, o capitalista pode '
  'confiar esse consumo ao interesse do próprio trabalhador, pois a coerção se desloca da '
  'pessoa para as condições econômicas. A liberdade subsiste apenas no plano individual, '
  'visto que o trabalhador pode deixar este ou aquele capitalista mas não a classe '
  'capitalista, e é nesse sentido que o trabalhador individual pertence a si mesmo enquanto '
  'a classe trabalhadora pertence à classe capitalista.',
 ],
},

# ==================================================================== cap. 22
{
 'depois': 57,
 'rotulo': 'Resposta 14 (cap. 22)',
 'paragrafos': [

  'Para que ocorra a reprodução ampliada, o capitalista deve consumir individualmente apenas '
  'uma parte do mais-valor e capitalizar a parte restante, isto é, empregá-la como capital '
  'adicional. Acumulação é, na definição de Marx, o emprego do mais-valor como capital, ou a '
  'reconversão do mais-valor em capital, e a diferença em relação à reprodução simples '
  'reside inteiramente nessa destinação.',

  'A capitalização, no entanto, não se reduz a poupar dinheiro. A parte capitalizada precisa '
  'repartir-se entre capital constante adicional e capital variável adicional, nas '
  'proporções exigidas pela composição técnica do capital, pois dinheiro acumulado não é '
  'capital e só se torna capital adicional quando se converte em meios de produção '
  'adicionais e em força de trabalho adicional postos a funcionar conjuntamente. Isso exige '
  'que ambos existam no mercado, e Marx demonstra que o próprio sistema os fornece, visto '
  'que o mais-produto do período anterior já contém, na sua forma material, os elementos do '
  'capital adicional, porque a produção capitalista produz máquinas, matérias-primas e '
  'instalações em quantidade superior à simples reposição, enquanto a força de trabalho '
  'adicional é fornecida pela superpopulação relativa, resultado da própria acumulação. A '
  'acumulação não depende, portanto, de nenhum fator externo ao processo, pois o capital '
  'produz as condições da sua própria ampliação.',

  'Duas consequências de princípio decorrem disso. A primeira é que o capital adicional é, '
  'por origem, mais-valor capitalizado, isto é, trabalho alheio apropriado sem equivalente, '
  'de sorte que a propriedade sobre produto alheio não pago se reproduz em escala crescente '
  'e cada ciclo amplia a base sobre a qual o mais-valor é extraído, conferindo à acumulação '
  'caráter cumulativo. A segunda é que a relação de classe não é apenas reproduzida, como no '
  'capítulo anterior, mas reproduzida em escala ampliada, pois mais trabalhadores são '
  'incorporados à relação assalariada e a massa de meios de produção que os confronta como '
  'capital se amplia.',

  'Cabe registrar, por fim, a recusa da teoria da abstinência, defendida por Senior e '
  'outros, que explicaria a acumulação pela virtude da parcimônia do capitalista. Marx a '
  'rejeita porque o fundo capitalizado não é fruto do trabalho nem da privação do '
  'capitalista, e sim mais-valor, trabalho excedente alheio, e porque a sua capitalização '
  'não resulta de escolha moral mas da coerção da concorrência, que impõe a cada capital a '
  'necessidade de crescer sob pena de sucumbir. O capitalista é forçado a acumular '
  'independentemente das suas inclinações pessoais, de modo que a divisão do mais-valor '
  'entre renda e capital é socialmente determinada e não um ato de virtude individual.',
 ],
},

{
 'depois': 59,
 'rotulo': 'Resposta 15 (cap. 22)',
 'paragrafos': [

  'Dada a proporção em que o mais-valor se divide entre renda consumida e capital acumulado, '
  'o volume da acumulação depende da grandeza do mais-valor, de modo que tudo aquilo que '
  'determina essa grandeza determina também o volume possível da acumulação. Marx examina '
  'quatro circunstâncias. A primeira é o grau de exploração da força de trabalho, fator mais '
  'direto, que atua por elevação da taxa de mais-valor mediante três vias, o prolongamento '
  'da jornada, que amplia o trabalho excedente sem alterar o necessário, a intensificação do '
  'trabalho, que aumenta o dispêndio por unidade de tempo, e a compressão do salário abaixo '
  'do valor da força de trabalho, pela qual o fundo de consumo necessário do trabalhador é '
  'convertido em fundo de acumulação do capital. Há aqui um efeito adicional que Marx '
  'destaca, pois o prolongamento da jornada permite extrair mais mais-valor com economia no '
  'adiantamento de capital fixo, já que as mesmas instalações são utilizadas por mais horas.',

  'A segunda circunstância é a produtividade social do trabalho, que atua por vários canais. '
  'Ela barateia as mercadorias, de sorte que, com uma dada grandeza de valor do mais-valor, '
  'o capitalista comanda massa física maior de meios de produção e de subsistência, e em '
  'termos reais a acumulação cresce mesmo sem aumento do mais-valor em valor. Barateia '
  'igualmente os elementos do capital, permitindo que a mesma soma de valor ponha em '
  'movimento mais trabalho e mais matéria, e amplia o mais-produto, tornando disponíveis em '
  'quantidade crescente os elementos materiais do capital adicional. Permite ainda ao '
  'capitalista ampliar simultaneamente consumo e acumulação, atenuando o conflito entre os '
  'dois destinos do mais-valor, e provoca a desvalorização moral do capital existente, '
  'impondo a sua renovação em bases mais produtivas.',

  'A terceira circunstância é a mais original e consiste na diferença crescente entre o '
  'capital empregado e o capital consumido. Os meios de trabalho funcionam integralmente na '
  'sua forma material durante todo o seu período de vida, mas transferem ao produto apenas a '
  'fração correspondente ao desgaste do período, e a diferença entre o conjunto de meios de '
  'trabalho em operação e a parte do seu valor efetivamente transferida constitui serviço '
  'gratuito prestado ao capital pelo trabalho passado, que Marx compara à ação gratuita das '
  'forças naturais. Quanto maior a escala e a durabilidade do aparato já acumulado, maior '
  'essa diferença, valendo o mesmo raciocínio para a ciência e o conhecimento técnico, que '
  'o capital apropria sem pagar. A quarta circunstância é a grandeza do capital adiantado, '
  'pois dada a taxa de mais-valor a sua massa é proporcional ao capital variável, isto é, ao '
  'número de trabalhadores explorados, de maneira que quanto maior o capital maior o volume '
  'absoluto da acumulação, o que confere ao processo caráter cumulativo e constitui a base '
  'material da concentração e da centralização.',

  'Marx encerra criticando o dogma do fundo de trabalho, segundo o qual existiria um fundo '
  'de salários de magnitude tecnicamente dada, do que decorreria que os salários só '
  'poderiam subir à custa do emprego e que qualquer reivindicação operária seria '
  'autodestrutiva. O exame das quatro circunstâncias mostra que a divisão do produto não é '
  'dada por nenhuma necessidade técnica, pois o fundo de salários é grandeza elástica, '
  'resultado da repartição do produto de valor, repartição determinada pela relação de '
  'forças entre as classes. O dogma converte, assim, um resultado histórico em limite '
  'natural, servindo para apresentar a distribuição vigente como intransponível.',
 ],
},

# ==================================================================== cap. 23
{
 'depois': 65,
 'rotulo': 'Resposta 16 (cap. 23)',
 'paragrafos': [

  'A composição orgânica do capital é a relação entre capital constante e capital variável, '
  'considerada na medida em que reflete a composição técnica, isto é, a proporção entre a '
  'massa de meios de produção e a quantidade de trabalho vivo necessária para operá-la. '
  'Marx examina os efeitos da acumulação em dois cenários, o primeiro supondo essa '
  'composição constante, que é abstração metodológica, e o segundo supondo-a crescente, que '
  'é o caso historicamente efetivo.',

  'No primeiro cenário a produtividade do trabalho permanece constante por hipótese, pois a '
  'composição técnica não se altera e a escala da produção cresce pela simples multiplicação '
  'de unidades produtivas com a mesma técnica, sendo a acumulação puramente quantitativa. '
  'Quanto à oferta e à demanda de trabalho, o capital variável cresce na mesma proporção do '
  'capital total e, sendo a demanda determinada por ele, cresce também proporcionalmente à '
  'acumulação, que exige por isso aumento proporcional do número de trabalhadores. Se a '
  'acumulação avança mais rápido que o crescimento da população trabalhadora, a demanda '
  'supera a oferta e os salários sobem, o que reduz a taxa de mais-valor e a massa '
  'disponível para capitalização, desacelerando a acumulação e restabelecendo a proporção '
  'anterior. Marx descreve esse resultado como o mecanismo pelo qual a produção capitalista '
  'remove por si mesma os obstáculos que cria, e sublinha que mesmo nessa situação favorável '
  'a elevação do salário é melhora apenas quantitativa que não suprime a dependência, pois '
  'o trabalhador segue despossuído e obrigado a vender a sua força de trabalho.',

  'No segundo cenário a produtividade cresce, e o seu crescimento é simultaneamente causa e '
  'efeito da elevação da composição orgânica, pois o aumento da produtividade se expressa '
  'materialmente no aumento da massa de meios de produção posta em movimento por cada '
  'trabalhador, e essa mesma transformação eleva o capital constante relativamente ao '
  'variável. Em termos de valor o movimento é parcialmente atenuado, porque o aumento da '
  'produtividade barateia também os meios de produção, de sorte que a composição em valor '
  'cresce menos que a técnica, mas a tendência é inequívoca, pois a parte variável decresce '
  'relativamente e em certos ramos pode decrescer em termos absolutos. Em consequência, a '
  'demanda por trabalho cresce menos que proporcionalmente ao capital, e um capital que '
  'dobra pode demandar bem menos que o dobro de trabalhadores.',

  'Quanto à oferta, está aqui o resultado decisivo. O capital exerce dois movimentos '
  'simultâneos sobre a força de trabalho, pois atrai trabalhadores ao ampliar a escala e '
  'abrir novos ramos e os repele ao substituí-los por maquinaria, cujo saldo é a produção '
  'contínua de uma população trabalhadora relativamente excedente, o exército industrial de '
  'reserva. A própria acumulação produz, assim, a oferta de trabalho de que necessita, que '
  'deixa de ser dado demográfico externo para se tornar produto interno do movimento do '
  'capital, e a pressão dessa reserva sobre os empregados regula os salários, viabiliza a '
  'intensificação do trabalho e enfraquece a resistência, de maneira que os movimentos '
  'gerais do salário passam a ser regulados pela sua expansão e contração ao longo do ciclo '
  'industrial, e não pelo movimento do número absoluto da população. Daí Marx extrai a lei '
  'geral absoluta da acumulação capitalista, segundo a qual quanto maiores a riqueza social '
  'e a produtividade do trabalho, maior é também o exército industrial de reserva e maior a '
  'massa do pauperismo, pois riqueza crescente e miséria crescente são produzidas pelo mesmo '
  'processo e não apesar dele.',
 ],
},

{
 'depois': 67,
 'rotulo': 'Resposta 17 (cap. 23)',
 'paragrafos': [

  'A concentração do capital é o crescimento da magnitude dos capitais individuais como '
  'resultado direto da acumulação, pois cada capitalista, ao capitalizar parte do mais-valor '
  'de que se apropria, amplia o capital sob o seu comando e concentra em suas mãos massa '
  'maior de meios de produção e contingente maior de trabalhadores. Esse processo encontra, '
  'porém, limites e contratendências, visto que está limitado pelo crescimento da riqueza '
  'social, já que cada capital individual é apenas fração alíquota do capital social, e '
  'porque a acumulação é acompanhada do aumento do número de capitais, por surgimento de '
  'novos e por fragmentação dos existentes mediante a divisão de patrimônios entre '
  'herdeiros, movimento dispersivo que atua em sentido contrário. Por isso a concentração '
  'baseada apenas na acumulação própria é processo lento, cujo ritmo é o próprio ritmo da '
  'acumulação.',

  'A centralização, ao contrário, é a concentração de capitais já formados, a atração de '
  'capital por capital, a reunião de muitos capitais menores em poucos maiores, e Marx a '
  'caracteriza como expropriação de capitalista por capitalista. A diferença essencial é que '
  'ela não altera a magnitude do capital social total, alterando apenas a sua distribuição, '
  'pois se trata de redistribuição de capital existente e não de criação de capital novo. '
  'Dessa natureza decorre a sua característica mais importante, a saber, que não depende do '
  'ritmo da acumulação e pode operar com rapidez muito maior, por simples mudança na '
  'propriedade e no comando, e Marx observa a esse respeito que o mundo continuaria sem '
  'ferrovias se fosse preciso esperar que a acumulação individual elevasse alguns capitais '
  'ao nível exigido para construí-las. Um dos seus mecanismos é a concorrência, cuja batalha '
  'é travada pelo barateamento das mercadorias, que depende da produtividade e esta da '
  'escala, de modo que os capitais maiores derrotam os menores, cujos capitais passam em '
  'parte às mãos dos vencedores.',

  'O outro mecanismo é o crédito, inicialmente auxiliar modesto da acumulação, que se '
  'converte numa arma nova e terrível na luta da concorrência e, por fim, num imenso '
  'mecanismo social de centralização dos capitais. A sua importância decorre de permitir ao '
  'capitalista individual dispor, dentro de certos limites, do capital alheio e das '
  'poupanças monetárias dispersas de toda a sociedade. Com isso ele desliga a escala de '
  'operação de um capital da magnitude do patrimônio pessoal do seu proprietário, de modo '
  'que o que comanda a produção deixa de ser a riqueza própria e passa a ser a capacidade de '
  'mobilizar capital social, converte somas monetárias ociosas, que não funcionariam como '
  'capital, em capital ativo concentrado em poucas mãos, e confere aos capitais maiores '
  'vantagem adicional na concorrência, visto que obtêm crédito em condições melhores, o que '
  'acelera a eliminação dos menores. É por essas razões que Marx o designa uma das alavancas '
  'mais poderosas da centralização.',

  'A sociedade por ações leva esse movimento ao seu desenvolvimento mais avançado, pois '
  'permite reunir capitais individualmente insuficientes em um único capital de grandes '
  'dimensões, viabilizando empreendimentos de escala impossível para qualquer capital '
  'isolado, como ferrovias e siderurgia. Ela separa, além disso, a propriedade do capital da '
  'sua gestão funcional, já que o acionista é proprietário sem função produtiva enquanto a '
  'direção é exercida por administradores assalariados, de sorte que o capital assume forma '
  'diretamente social no interior do próprio capitalismo, e acelera enormemente a '
  'centralização, porque o controle pode ser adquirido pela compra de participações sem '
  'necessidade de adquirir empresas integralmente. Convém concluir articulando os dois '
  'processos, pois a centralização não substitui a acumulação mas potencia os seus efeitos, '
  'já que ao permitir a ampliação súbita da escala acelera a revolução na composição técnica '
  'do capital e intensifica a repulsão de trabalhadores, produzindo saltos técnicos que '
  'tornam massas de trabalhadores subitamente supérfluas. Concentração e centralização são, '
  'assim, mediações indispensáveis entre a acumulação e a produção do exército industrial de '
  'reserva.',
 ],
},

{
 'depois': 71,
 'rotulo': 'Resposta 18 (cap. 23)',
 'paragrafos': [

  'Antes de examinar a funcionalidade, é preciso fixar em que sentido a população é dita '
  'excedente, pois a superpopulação relativa não é excedente em relação aos meios de '
  'subsistência disponíveis, como supõe Malthus, mas em relação às necessidades médias de '
  'valorização do capital. A população é declarada supérflua por um critério social '
  'determinado, a rentabilidade, e não por limite natural, e além disso é produzida pela '
  'própria acumulação mediante a elevação da composição orgânica. A funcionalidade decorre '
  'justamente dessas duas características.',

  'A primeira função é fornecer a elasticidade que a acumulação exige. A acumulação não é '
  'movimento uniforme, pois se dá em saltos, por ramos e por regiões, seguindo o ciclo '
  'industrial com suas fases de prosperidade, crise e estagnação, e nas fases de expansão o '
  'capital precisa lançar massas de trabalhadores em pontos decisivos, subitamente e sem '
  'retirá-los dos ramos já em funcionamento, o que só é possível se existir contingente '
  'disponível pronto a ser absorvido. A reserva é esse reservatório, e é ela que torna a '
  'oferta de trabalho elástica, desligando-a dos limites naturais do crescimento '
  'populacional, que é lento e sujeito a defasagens de uma geração. A segunda função é '
  'regular os salários, pois a pressão dos desempregados sobre os empregados os mantém '
  'dentro dos limites compatíveis com a valorização do capital, impedindo nas fases de '
  'expansão que a demanda crescente por trabalho comprometa a taxa de mais-valor e '
  'deprimindo-os nas fases de contração. É nesse sentido que Marx afirma que os movimentos '
  'gerais do salário são regulados exclusivamente pela expansão e contração do exército '
  'industrial de reserva, e não pelo movimento do número absoluto da população.',

  'A terceira função é disciplinar a classe trabalhadora e enfraquecer a sua resistência, '
  'pois a existência de uma massa disponível acirra a concorrência entre os próprios '
  'trabalhadores, e quem está empregado sabe que pode ser substituído, o que reduz a '
  'capacidade de recusar jornadas longas e ritmos intensos, enfraquece a organização '
  'sindical e a eficácia das greves, visto que o capital dispõe de substitutos imediatos, e '
  'permite impor a disciplina de fábrica com menor custo de coerção direta. A isso se liga '
  'uma quarta função, que Marx destaca pela sua perversidade, pois o trabalho excessivo da '
  'parte empregada engrossa as fileiras da parte desempregada, e a pressão desta obriga a '
  'parte empregada a aceitar trabalho ainda mais excessivo, de modo que sobretrabalho de uns '
  'e desemprego forçado de outros se condicionam mutuamente e ambos se tornam meios de '
  'enriquecimento do capitalista. É também por isso que o capital resiste tanto à redução da '
  'jornada, já que distribuir o trabalho disponível entre mais trabalhadores reduziria a '
  'reserva e a sua eficácia disciplinadora.',

  'Como a acumulação produz a sua própria oferta de trabalho, o capital se liberta ainda da '
  'dependência demográfica, criando e destruindo disponibilidade de trabalho em prazos muito '
  'mais curtos do que a demografia opera, de maneira que a lei de oferta e demanda de '
  'trabalho passa a funcionar dentro de limites que o próprio capital estabelece, e ao '
  'conter os salários a reserva contribui para sustentar a taxa de mais-valor, '
  'contrabalançando a pressão que a elevação da composição orgânica exerce sobre a taxa de '
  'lucro. Reconhecer essa funcionalidade, porém, não equivale a tratá-la como harmonia, pois '
  'a mesma superpopulação que serve ao capital constitui a forma de existência do pauperismo '
  'e da degradação, e as formas que Marx distingue, flutuante, latente e estagnada, além do '
  'pauperismo propriamente dito, demonstram que se trata de condição permanente e '
  'estruturada, e não de acidente conjuntural. A funcionalidade para o capital e a '
  'destrutividade para os trabalhadores são o mesmo fato observado de dois lados.',
 ],
},

{
 'depois': 75,
 'rotulo': 'Resposta 19 (cap. 23)',
 'paragrafos': [

  'A passagem se dirige à representação corrente do mercado de trabalho, segundo a qual '
  'demanda e oferta de trabalho seriam duas potências independentes que se encontram no '
  'mercado e cuja interação determina o salário, sendo a demanda dada pelo crescimento do '
  'capital e a oferta pelo crescimento da população trabalhadora, regido por leis '
  'demográficas supostamente naturais à maneira de Malthus. O salário seria, nessa leitura, '
  'resultado neutro do encontro de duas séries causais autônomas. Marx responde que o jogo é '
  'fraudulento, que os dados estão viciados, porque as duas potências não são independentes, '
  'uma vez que o capital age simultaneamente sobre os dois lados, de modo que o resultado do '
  'suposto encontro já se encontra determinado por um único movimento, o da acumulação.',

  'Quanto à demanda, o argumento se desenvolve em três passos. O que compra força de '
  'trabalho é o capital variável e não o capital total, de sorte que a demanda depende '
  'apenas de uma parte do capital. Com o progresso da acumulação a composição orgânica se '
  'eleva, e o capital variável cresce menos que o capital total podendo até decrescer em '
  'termos absolutos, razão pela qual a demanda de trabalho não é idêntica ao crescimento do '
  'capital e um capital que cresce rapidamente pode demandar proporcionalmente menos '
  'trabalho. Acrescente-se que o capital pode ampliar a massa de trabalho que explora sem '
  'ampliar o número de trabalhadores, prolongando a jornada e intensificando o trabalho, '
  'conforme o capítulo 9 estabelece, de modo que nem mesmo a demanda por horas de trabalho '
  'se traduz diretamente em demanda por trabalhadores.',

  'Quanto à oferta, está aqui o ponto que a representação corrente ignora, pois ela não é '
  'idêntica ao crescimento da classe trabalhadora pela razão de que o capital a produz '
  'ativamente. Ele a produz pela repulsão de trabalhadores já empregados, visto que a '
  'maquinaria torna supérfluos trabalhadores em atividade e os lança no mercado, de maneira '
  'que o capital não apenas encontra trabalhadores disponíveis mas os fabrica. Produz também '
  'pela proletarização de produtores independentes, já que a destruição do artesanato e da '
  'pequena produção rural expropria camadas que viviam fora da relação assalariada. Produz '
  'ainda pela incorporação de novas camadas, pois mulheres e crianças são atraídas pela '
  'própria transformação técnica que dispensa força física e qualificação, ampliando a '
  'oferta sem qualquer alteração demográfica, valendo o mesmo para o deslocamento de '
  'populações rurais e para os fluxos migratórios. E produz, como síntese desses mecanismos, '
  'o exército industrial de reserva, que constitui a oferta efetivamente relevante para o '
  'capital.',

  'Conclui-se que tanto a demanda quanto a oferta são determinações internas do movimento do '
  'capital, e que aquilo que aparece como livre jogo de duas forças de mercado é, na '
  'realidade, o automovimento do capital desdobrando-se em dois lados, razão pela qual a lei '
  'de oferta e demanda continua operando mas dentro de limites que o próprio capital '
  'estabelece, o que lhe retira o caráter de árbitro neutro. A dinâmica da acumulação se '
  'sobrepõe à dinâmica demográfica por três razões. A primeira é de velocidade, pois o '
  'crescimento populacional opera com defasagens de uma geração entre o nascimento e o '
  'ingresso no mercado de trabalho, enquanto a acumulação pode mobilizar ou tornar supérflua '
  'massa enorme de trabalhadores em poucos anos, de modo que a variável rápida subordina a '
  'lenta. A segunda é que o que conta para o capital não é a população mas a '
  'disponibilidade para a valorização, pois pessoas existentes e não disponíveis como força '
  'de trabalho não constituem oferta. A terceira é que Marx substitui a lei natural da '
  'população por uma lei histórica específica, visto que cada modo de produção possui a sua '
  'própria lei de população, e no capitalismo ela é a produção de uma superpopulação '
  'relativa pela acumulação. A inversão é completa, pois não é a população que pressiona os '
  'meios de subsistência, e sim o capital que produz a população excedente de que necessita, '
  'sendo a miséria resultante efeito da riqueza e não do seu contrário.',
 ],
},

# ==================================================================== cap. 24
{
 'depois': 83,
 'rotulo': 'Resposta 20 (cap. 24)',
 'paragrafos': [

  'A anedota a que Marx se refere é a versão que a economia política oferece da origem do '
  'capital, e ele a trata como o equivalente, na economia, do pecado original na teologia. '
  'Esse relato apresenta dois vícios lógicos, pois explica o resultado pelo próprio '
  'resultado, pressupondo como causa a desigualdade que deveria explicar, e naturaliza um '
  'processo histórico determinado, apresentando como consequência de virtudes individuais '
  'aquilo que foi produto de expropriação violenta e de ação estatal sistemática. Contra '
  'essa versão, Marx estabelece que a acumulação primitiva não é acumulação resultante do '
  'modo de produção capitalista, e sim a que o precede e o constitui, cujo conteúdo é um '
  'processo de separação, a cisão entre o produtor e os meios de produção. A relação '
  'capitalista pressupõe duas condições que não existem naturalmente, de um lado '
  'trabalhadores livres e despossuídos, obrigados a vender a sua força de trabalho, e de '
  'outro meios de produção e dinheiro concentrados em poucas mãos, sendo a acumulação '
  'primitiva o processo que produz simultaneamente ambas. Daí a tese de que na história '
  'real desempenham o papel principal a conquista, a escravização, o roubo e o assassinato, '
  'em suma, a violência.',

  'Quanto à formação da classe trabalhadora, o processo tem caráter duplo, e é essa '
  'duplicidade que importa reter, pois o produtor direto é liberado das relações de servidão '
  'e, ao mesmo tempo, despojado dos seus meios de produção e de subsistência, tornando-se '
  'livre em dois sentidos, livre da sujeição ao senhor e livre de propriedade, sem o que o '
  'primeiro sentido não produziria assalariados. Tomando o caso inglês, que Marx considera '
  'clássico, a dissolução dos séquitos feudais lança no mercado massas de homens sem meios '
  'de vida, e a expropriação da população rural se realiza pelo cercamento das terras '
  'comuns, pela conversão de terras aráveis em pastagens para ovelhas sob o impulso da '
  'indústria da lã e pela limpeza das propriedades, com expulsão de aldeias inteiras. O '
  'confisco dos bens da Igreja na Reforma permite a sua venda a preços nominais, e nos '
  'séculos XVIII e XIX a expropriação assume forma legal mediante os decretos de cercamento, '
  'que Marx qualifica como a forma parlamentar do roubo.',

  'A esse movimento de expropriação acrescenta-se um movimento de coerção, sem o qual a '
  'classe trabalhadora não se constituiria, pois os expropriados não se transformam '
  'espontaneamente em operários disciplinados, convertendo-se primeiro em vagabundos e '
  'mendigos, contra os quais se volta a legislação sanguinária dos séculos XV a XVII, com '
  'açoitamento, marcação a ferro, escravização e execução sob Henrique VIII, Eduardo VI e '
  'Isabel, cujo objetivo é forçá-los ao trabalho assalariado. Somam-se os estatutos que '
  'fixam salários máximos e proíbem a associação de trabalhadores, vigentes até o século '
  'XIX, que demonstram a atuação direta do Estado para rebaixar o preço do trabalho. Marx '
  'insiste em que são necessários tempo e coerção prolongada para que a nova classe passe a '
  'considerar as exigências do modo de produção capitalista como leis naturais evidentes, '
  'sendo a disciplina fabril resultado histórico e não disposição espontânea.',

  'Quanto à formação da classe capitalista, a gênese possui vertente interna e vertente '
  'externa, sendo a segunda decisiva. Na interna situam-se o arrendatário capitalista '
  'inglês, favorecido por arrendamentos de longo prazo, pela desvalorização dos metais '
  'preciosos, que reduziu o valor real das rendas e dos salários fixados nominalmente, e '
  'pela usurpação das terras comuns, e a conversão de comerciantes e usurários em '
  'capitalistas industriais. Na externa, que Marx apresenta com ironia como o idílio da '
  'acumulação primitiva, figuram a pilhagem colonial, o saque das Índias Orientais e o '
  'extermínio das populações indígenas, e sobretudo o tráfico de escravos e a escravidão nas '
  'Américas, que constitui o pedestal da indústria inglesa inclusive em sentido material, '
  'pois o algodão das plantações escravistas era a matéria-prima de Lancashire. Somam-se a '
  'dívida pública, uma das alavancas mais poderosas do processo, que transforma dinheiro '
  'improdutivo em capital e dá origem ao sistema bancário moderno, o sistema tributário, '
  'cuja incidência sobre os meios de subsistência acelera a proletarização, e o '
  'protecionismo. O fio que une esses elementos é a ação sistemática do poder estatal, e daí '
  'a formulação de que a violência é a parteira de toda sociedade velha grávida de uma nova, '
  'sendo ela mesma uma potência econômica. O resultado teórico é decisivo, pois se a '
  'separação entre produtores e meios de produção é histórica e não natural, então ela é '
  'transitória, e a propriedade privada capitalista não tem fundamento em nenhum direito '
  'originário derivado do trabalho próprio.',
 ],
},
]
