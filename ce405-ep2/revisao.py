# -*- coding: utf-8 -*-
"""
Sumário de revisão da Lista de Questões I de Economia Política II (CE405, turma C).

Para cada uma das 20 questões:
  'topicos'      esqueleto da resposta em tópicos, agrupados por bloco
  'nota_maxima'  o que precisa aparecer na folha para garantir nota cheia
  'erros'        erros frequentes que derrubam a nota

Referência: MARX, Karl. O Capital, Livro I. São Paulo: Boitempo.
"""

MAPA = [
    ('4', 'A transformação do dinheiro em capital', 'Q1, Q2'),
    ('5', 'Processo de trabalho e processo de valorização', 'Q3'),
    ('6', 'Capital constante e capital variável', 'Q4'),
    ('7', 'A taxa de mais-valor', 'Q5, Q6, Q7'),
    ('9', 'Taxa e massa de mais-valor', 'Q8'),
    ('10', 'Conceito de mais-valor relativo', 'Q9, Q10'),
    ('13', 'Maquinaria e grande indústria', 'Q11'),
    ('21', 'Reprodução simples', 'Q12, Q13'),
    ('22', 'A transformação de mais-valor em capital', 'Q14, Q15'),
    ('23', 'A lei geral da acumulação capitalista', 'Q16, Q17, Q18, Q19'),
    ('24', 'A assim chamada acumulação primitiva', 'Q20'),
]

FORMULAS = [
    ('Valor da mercadoria', 'c + v + m',
     'c é valor transferido, v + m é valor novo criado no período'),
    ('Capital total adiantado', 'C = c + v',
     'm não entra, porque é resultado e não adiantamento'),
    ('Valor do produto', 'c + v + m',
     'a grandeza maior, inclui o valor que só passou pelo processo'),
    ('Produto de valor', 'v + m',
     'só o valor novo. É aqui que a maioria erra'),
    ('Taxa de mais-valor', "m' = m / v  =  trabalho excedente / trabalho necessário",
     'mede o grau de exploração'),
    ('Taxa de lucro', "m / (c + v)",
     'esconde a exploração, só aparece no Livro III'),
    ('Massa de mais-valor', "M = m' × V",
     'taxa multiplicada pelo capital variável total'),
    ('Composição orgânica', 'c / v',
     'quanto maior, mais a taxa de lucro disfarça a taxa de mais-valor'),
]

NUMEROS_Q6 = [
    ('c', '410'), ('v', '90'), ('m', '90'),
    ('Capital total (c+v)', '500'),
    ('Valor do produto (c+v+m)', '590'),
    ('Produto de valor (v+m)', '180'),
    ("Taxa de mais-valor (m/v)", '100%'),
    ('Taxa de lucro (m/C)', '18%'),
    ('Composição (c/v)', '≈ 4,56, ou 82% c e 18% v'),
]

ERROS_TRANSVERSAIS = [
    'Confundir **valor do produto** (c+v+m) com **produto de valor** (v+m). É o erro '
    'que Marx mais combate e aparece em três questões diferentes.',
    'Calcular a taxa de mais-valor sobre o capital total. Isso dá a taxa de lucro e '
    'subestima a exploração.',
    'Dizer que o capital constante "contribui" para o mais-valor. Ele é condição '
    'material indispensável, mas a contribuição para o mais-valor é zero.',
    'Dizer que o capitalista compra trabalho. Ele compra **força de trabalho**. A '
    'distinção sustenta toda a teoria.',
    'Explicar comportamento capitalista por ganância, parcimônia ou maldade pessoal. '
    'Marx sempre deriva da estrutura e da coerção da concorrência.',
    'Tratar a superpopulação como excedente em relação aos alimentos. Ela é excedente '
    'em relação às necessidades de valorização do capital.',
    'Esquecer a dimensão histórica. Separação entre produtor e meios de produção, valor '
    'da força de trabalho e lei de população são todos históricos, não naturais.',
    'Responder só a primeira metade de enunciados com duas perguntas. Várias questões '
    'da lista pedem duas coisas (Q10, Q13, Q16, Q17, Q19, Q20).',
]

ESTRATEGIA = [
    'Leia as questões e marque quantas partes cada enunciado pede. Q16 pede dois '
    'cenários e dois efeitos em cada, o que dá quatro respostas dentro de uma.',
    'Comece pela questão que você domina mais, para garantir pontos e ganhar ritmo.',
    'Com 2 horas, reserve cerca de 20 a 25 minutos por questão dissertativa e deixe 10 '
    'minutos no fim para reler.',
    'Abra cada resposta com a tese direta, em uma frase. O corretor precisa achar a '
    'resposta sem caçar no texto.',
    'Use o vocabulário técnico desde a primeira linha. Mais-valor, capital constante e '
    'variável, composição orgânica, subsunção real, trabalho necessário e excedente.',
    'Se o tempo apertar, corte a qualificação final e entregue tese e mecanismo. É o '
    'núcleo que vale nota.',
    'Cite as passagens pela ideia, sem tentar reproduzir literalmente. Errar a citação '
    'pesa mais que parafrasear bem.',
]

REVISAO = [

# ========================================================================= Q1
{
 'q': 1, 'cap': '4',
 'titulo': "Circulação simples (M–D–M) contra circulação do capital (D–M–D')",
 'pede': 'As diferenças entre os dois circuitos e a maneira como Marx introduz a '
         'categoria de capital.',
 'topicos': [
   ('M–D–M, circulação simples', [
     'Começa e termina em mercadoria. O dinheiro é meio de circulação, gasto e não retorna.',
     'Extremos equivalentes em valor e diferentes em utilidade. É a diferença qualitativa '
     'que dá sentido à troca, pois trocar trigo por trigo seria absurdo.',
     'Finalidade **fora** da circulação, está no consumo.',
     'Tem limite interno. Acaba quando a necessidade é satisfeita.',
     'O valor só muda de forma, não cresce.',
   ]),
   ("D–M–D', dinheiro como capital", [
     'Começa e termina em dinheiro. Agora a **mercadoria** é o intermediário, porque se '
     'compra para vender.',
     'Extremos qualitativamente idênticos, então só podem diferir em quantidade. Voltar '
     'com a mesma soma seria tautológico.',
     "Logo D' = D + ΔD, e o ΔD é o **mais-valor**.",
     'O dinheiro é adiantado, não gasto, porque reflui acrescido. Isso separa o '
     'capitalista do entesourador.',
     'Finalidade **interna** ao movimento, é a valorização do valor. O valor de uso é só '
     'portador do valor.',
     "Sem limite interno, porque quantidade de valor não tem saciedade. D' é o começo do "
     'ciclo seguinte.',
   ]),
   ('Como Marx introduz a categoria', [
     'Pela **forma**, não pela matéria. Capital não é coisa (dinheiro, máquina, estoque), '
     'é movimento, forma determinada de circulação.',
     "D–M–D' é a fórmula geral do capital como ele aparece na esfera da circulação.",
     'Capital é **valor em processo, valor que se valoriza**. O valor vira o "sujeito '
     'automático" do movimento.',
     'O capitalista é **derivado** da forma, é capital personificado. O fim subjetivo dele '
     'coincide com o fim objetivo da estrutura.',
     'Acumulação sem limite é consequência estrutural, não defeito de caráter.',
     'A exposição é provisória de propósito, porque a forma é contraditória no plano da '
     'circulação, o que obriga a ir para a produção.',
     "D–D' (capital a juros) é a forma abreviada e mais mistificada.",
   ]),
 ],
 'nota_maxima': [
   'Contrastar os dois circuitos em pelo menos quatro eixos (extremos, quem faz a '
   'mediação, finalidade, limite).',
   'Explicar **por que** a identidade qualitativa dos extremos obriga a diferença a ser '
   'quantitativa. É o argumento da tautologia, e ele vale ponto.',
   'Nomear o ΔD como mais-valor.',
   'Definir capital como forma e movimento, usando a expressão "valor que se valoriza".',
   'Derivar o capitalista da forma, e não o contrário.',
   'Fechar dizendo que a fórmula é contraditória no plano da circulação, o que já aponta '
   'para a força de trabalho.',
 ],
 'erros': [
   'Definir capital como dinheiro, máquina ou estoque. Perde o ponto central da questão.',
   'Descrever D–M–D\' só como "comprar para vender" sem justificar a necessidade do '
   'incremento.',
   'Confundir capitalista com entesourador, esquecendo que o dinheiro é adiantado e reflui.',
   'Explicar a acumulação ilimitada pela ganância pessoal.',
 ],
},

# ========================================================================= Q2
{
 'q': 2, 'cap': '4',
 'titulo': 'A contradição da origem do mais-valor e a solução pela força de trabalho',
 'pede': 'Os dois termos da contradição e por que a mercadoria força de trabalho a '
         'resolve.',
 'topicos': [
   ('Termo 1, não pode nascer na circulação', [
     'Troca pelos valores, então a circulação só muda o valor de forma, não cria nada.',
     'Todos vendendo acima do valor: cada um é vendedor numa hora e comprador em outra, o '
     'ganho se anula, muda só a denominação dos preços.',
     'Um vendedor privilegiado: ele ganha exatamente o que o comprador perde. Valor muda '
     'de mão, não aumenta.',
     'Fraude e monopólio explicam fortuna individual, mas a **classe** não enriquece '
     'trocando consigo mesma.',
   ]),
   ('Termo 2, não pode nascer fora da circulação', [
     'Fora dela o produtor lida só com a própria mercadoria. Cria valor, mas não '
     'mais-valor, porque não há relação que permita apropriar trabalho alheio não pago.',
     'O dono do dinheiro não produz o acréscimo trabalhando ele mesmo.',
     'O capital precisa passar pela circulação, porque nela compra os elementos e nela '
     'realiza o mais-valor em dinheiro.',
     'Daí a frase: tem de nascer nela e ao mesmo tempo não nascer nela. A solução precisa '
     'encaixar os dois termos, não sacrificar um.',
   ]),
   ('A solução', [
     'Achar, **dentro** da circulação e sem quebrar a lei do valor, uma mercadoria cujo '
     'consumo **fora** dela produza mais valor do que ela vale.',
     'Distinção fundadora: **trabalho** é o gasto em si e não tem valor, porque é a '
     'substância do valor. **Força de trabalho** é a capacidade de trabalhar, e essa é a '
     'mercadoria.',
     'Valor da força de trabalho = tempo de trabalho socialmente necessário para '
     'reproduzi-la, ou seja, valor dos meios de subsistência do trabalhador e da família, '
     'com componente histórico e moral.',
     'A compra paga o valor cheio, sem trapaça. **A exploração não depende de '
     'irregularidade na troca.**',
     'Valor de uso singular: consumi-la é pôr o trabalhador a trabalhar, e trabalhar é '
     'criar valor. Única mercadoria cujo valor de uso é ser fonte de valor.',
     'Ponto decisivo: valor pago e valor criado têm determinantes diferentes. O pago '
     'depende do custo de reprodução, o criado depende da duração e intensidade da jornada.',
     'Exemplo: valor diário = 6h, jornada = 12h. As 6 primeiras são trabalho necessário, '
     'as 6 seguintes são trabalho excedente, de onde vem o mais-valor.',
   ]),
   ('Pressupostos históricos', [
     'O trabalhador precisa ser juridicamente livre e vender por **tempo determinado**, '
     'senão seria escravo e faltaria o vendedor.',
     'E precisa estar separado dos meios de produção e de subsistência.',
     'São condições históricas, produzidas pela acumulação primitiva (cap. 24).',
     'Fecho com a ironia do éden dos direitos inatos do homem, de onde se sai para entrar '
     'na produção, "onde só se entra a negócios".',
   ]),
 ],
 'nota_maxima': [
   'Enunciar os **dois** termos de forma separada e explícita antes de resolver.',
   'Percorrer as três hipóteses de troca desigual e mostrar por que cada uma falha. '
   'Responder só "a troca é de equivalentes" é resposta incompleta.',
   'Usar o argumento de que a **classe** capitalista não pode enriquecer trocando consigo '
   'mesma.',
   'Fazer a distinção força de trabalho contra trabalho de modo explícito, e dizer que o '
   'trabalho não tem valor porque é a substância do valor.',
   'Afirmar que a compra respeita a lei do valor. Esse é o ponto mais fino da questão, '
   'porque mostra que exploração e troca justa convivem.',
   'Explicar a independência entre valor pago e valor criado, e fechar com o exemplo '
   'numérico da jornada.',
   'Mostrar como a solução articula os dois termos (compra na circulação, criação na '
   'produção).',
   'Citar os dois pressupostos históricos.',
 ],
 'erros': [
   'Dizer que o capitalista "paga menos do que o trabalhador vale". Erro grave, porque '
   'ele paga o valor integral da força de trabalho.',
   'Dizer que o mais-valor vem de vender acima do valor. É exatamente a hipótese que Marx '
   'refuta.',
   'Confundir força de trabalho com trabalho ao longo da resposta.',
   'Resolver a contradição negando um dos termos em vez de articular os dois.',
 ],
},

# ========================================================================= Q3
{
 'q': 3, 'cap': '5',
 'titulo': 'Trabalho, valor de uso, valor, processo de trabalho e processo de valorização',
 'pede': 'Como essas cinco categorias se relacionam entre si.',
 'topicos': [
   ('O eixo da resposta', [
     'Tudo se articula em torno do **duplo caráter do trabalho** (cap. 1).',
     'O processo de produção capitalista é a **unidade** de duas determinações do mesmo ato.',
   ]),
   ('Processo de trabalho', [
     'Examinado primeiro sem forma social, como condição permanente da vida humana, '
     'metabolismo entre homem e natureza.',
     'Três momentos simples: atividade com um fim, objeto de trabalho, meios de trabalho. '
     'Os dois últimos formam os meios de produção.',
     'O trabalho se objetiva, trabalho vivo vira trabalho morto no produto.',
     'Resultado: **valor de uso**.',
     'Aqui o trabalho conta como **trabalho concreto e útil**, qualitativamente determinado.',
   ]),
   ('Processo de valorização', [
     'No capitalismo o processo de trabalho é só o meio, o fim é valor e mais-valor.',
     'Aqui o trabalho conta como **trabalho abstrato**, gasto de força humana em geral, '
     'medido só pelo tempo.',
     'Dois graus do mesmo processo: **formação de valor** enquanto cria valor novo, e '
     '**valorização** quando passa do ponto em que repõe o valor da força de trabalho.',
     'Valor do produto = valor dos meios de produção (conservado e repassado) + valor novo.',
   ]),
   ('A dupla função do mesmo trabalho (o núcleo)', [
     'Não são dois trabalhos, é o mesmo trabalho em duas determinações.',
     'Como **concreto**: produz valor de uso e conserva/transfere o valor dos meios de '
     'produção.',
     'Como **abstrato**: cria valor novo e, passando de certo ponto, mais-valor.',
     'Exemplo do fiandeiro: fiando, faz fio e no mesmo ato adiciona valor. Preserva o valor '
     'do algodão justamente enquanto o transforma.',
   ]),
   ('Encaixe e qualificações', [
     'Trabalho é o centro porque é duplo. Valor de uso é resultado do processo de trabalho '
     'e condição material do valor. Valor é objetivação do trabalho abstrato.',
     'A unidade é **contraditória**, porque a valorização subordina e deforma o processo de '
     'trabalho (técnica, duração, intensidade).',
     'Só cria valor o trabalho **socialmente necessário**. Trabalho desperdiçado ou abaixo '
     'da média não gera valor proporcional.',
     'O produto precisa ser valor de uso **para outros**, senão o valor não se valida na '
     'venda.',
     'Inversão que o capítulo anuncia: no processo de trabalho o trabalhador usa os meios '
     'de produção, na valorização os meios de produção usam o trabalhador, como meios de '
     'absorver trabalho alheio.',
   ]),
 ],
 'nota_maxima': [
   'Organizar a resposta pelo duplo caráter do trabalho. Sem esse eixo a resposta vira '
   'lista solta de definições.',
   'Listar os três momentos simples do processo de trabalho.',
   'Distinguir **formação de valor** de **valorização**, com o critério do "ponto" em que '
   'o valor criado repõe o valor da força de trabalho.',
   'Atribuir corretamente as duas funções: concreto conserva e transfere, abstrato cria.',
   'Dizer explicitamente que é o **mesmo** trabalho, e dar um exemplo concreto.',
   'Caracterizar a unidade como contraditória, com a valorização mandando no processo de '
   'trabalho.',
   'Incluir ao menos uma qualificação (trabalho socialmente necessário ou utilidade social '
   'do produto).',
 ],
 'erros': [
   'Tratar trabalho concreto e trabalho abstrato como dois trabalhos distintos ou como '
   'duas etapas sucessivas.',
   'Dizer que o trabalho concreto cria valor, ou que o abstrato cria valor de uso.',
   'Esquecer que o valor precisa de um portador material, e que sem valor de uso não há '
   'valor realizável.',
   'Apresentar processo de trabalho e valorização como processos separados em vez de '
   'unidade contraditória.',
 ],
},

# ========================================================================= Q4
{
 'q': 4, 'cap': '6',
 'titulo': 'Capital constante e capital variável',
 'pede': 'Definir as duas categorias, apontar componentes materiais típicos e explicar a '
         'contribuição de cada uma para o valor da mercadoria e para o mais-valor.',
 'topicos': [
   ('Capital constante (c)', [
     'Parte do capital gasta em **meios de produção**. Constante porque, dentro do '
     'processo, não muda de grandeza em valor.',
     'Componentes: objeto de trabalho (matéria-prima e bruta, algodão, ferro, minério), '
     'matérias auxiliares (combustível, lubrificante, energia) e meios de trabalho '
     '(máquina, ferramenta, instalação, prédio).',
     'Contribuição ao valor: **só repasse, nunca criação**. Quem conserva o valor é o '
     'trabalho vivo na sua forma concreta, ao usar os meios conforme a finalidade deles.',
     'Modo do repasse difere: matéria-prima repassa tudo de uma vez, máquina repassa só o '
     'desgaste. Daí nasce depois a distinção fixo/circulante (Livro II).',
     'Limite rígido: o valor repassado nunca excede o valor que os meios já tinham.',
     'Contribuição ao mais-valor: **zero**. É condição material indispensável, mas função '
     'passiva, serve para absorver trabalho vivo.',
   ]),
   ('Capital variável (v)', [
     'Parte do capital gasta na compra da **força de trabalho**, o fundo de salários. '
     'Variável porque muda de grandeza em valor no processo.',
     'Componente: a força de trabalho dos assalariados, que na prática vira os meios de '
     'subsistência com que eles se reproduzem.',
     'Contribuição ao valor: cria valor novo. Essa grandeza é o **produto de valor**, '
     'v + m, onde v é só o reposto e m é a sobra.',
     'Contribuição ao mais-valor: **exclusiva**, porque o mais-valor só vem do trabalho '
     'vivo.',
     'Precisão que vale ponto: não é o capital variável, como soma de dinheiro, que cria o '
     'mais-valor, é o **trabalho vivo que ele põe para funcionar**.',
   ]),
   ('Fechamento', [
     'Valor da mercadoria = c + v + m. O c é valor que já existia, v + m é o valor novo.',
     'c/v **não** é a mesma coisa que fixo/circulante. Matéria-prima é constante e '
     'circulante ao mesmo tempo, máquina é constante e fixa.',
     'Função crítica do par: para o capitalista todo gasto parece igual e o lucro parece '
     'render do capital inteiro (taxa de lucro). Essa confusão sustenta a aparência de que '
     'o lucro nasce do capital em si.',
     'Separando c de v, Marx mostra a fonte determinada do excedente e que a taxa de lucro '
     'esconde o grau de exploração. Foi por não fazer essa separação que a economia '
     'política clássica não explicou o excedente.',
     'Qualificação: a constância de c vale **dentro** do processo. Por fora, salto de '
     'produtividade no setor fornecedor desvaloriza o capital já investido, fenômeno '
     'importante nas crises.',
   ]),
 ],
 'nota_maxima': [
   'Justificar os **nomes**. Constante porque não muda de grandeza de valor no processo, '
   'variável porque muda. Quem só define sem justificar perde ponto.',
   'Dar componentes materiais dos três tipos em c, não só "máquinas".',
   'Separar com clareza as duas perguntas do enunciado, contribuição ao valor da mercadoria '
   'e contribuição ao mais-valor. São coisas diferentes.',
   'Afirmar que c contribui para o valor da mercadoria (por repasse) mas **não** para o '
   'mais-valor. Essa assimetria é o coração da questão.',
   'Escrever a decomposição c + v + m e identificar v + m como produto de valor.',
   'Distinguir c/v de fixo/circulante.',
   'Fechar com a função crítica do par conceitual contra a taxa de lucro.',
 ],
 'erros': [
   'Dizer que o capital constante não contribui para o valor da mercadoria. Ele contribui, '
   'por repasse. O que ele não faz é criar mais-valor.',
   'Dizer que a máquina agrega valor ao produto além do seu desgaste.',
   'Confundir capital constante com capital fixo.',
   'Dizer que o capital variável cria mais-valor por si, sem mencionar o trabalho vivo.',
 ],
},

# ========================================================================= Q5
{
 'q': 5, 'cap': '7',
 'titulo': 'As duas fórmulas da taxa de mais-valor',
 'pede': 'A fórmula em termos de valores e a fórmula em termos de tempos de trabalho.',
 'topicos': [
   ('Fórmula 1, em valores', [
     'Parte do valor da mercadoria, c + v + m. Como c é só repassado, tira-se o c.',
     'Sobra o **produto de valor**, v + m.',
     "A taxa é **m' = m / v**.",
     'O denominador é o capital variável, **não** o capital total. A ideia é medir quanto '
     'se valorizou a parte que se valoriza.',
   ]),
   ('Fórmula 2, em tempos de trabalho', [
     'A jornada se divide em **trabalho necessário** (reproduz o valor da força de '
     'trabalho) e **trabalho excedente** (valor sem contrapartida).',
     "A taxa é **m' = trabalho excedente / trabalho necessário**.",
   ]),
   ('Por que são equivalentes', [
     'v é a forma-valor do trabalho necessário e m é a forma-valor do trabalho excedente.',
     'Marx escreve a identidade de modo explícito: m/v = trabalho excedente / trabalho '
     'necessário.',
     'Diferença só de ponto de vista. Uma mede em **trabalho objetivado** (já cristalizado '
     'em valor), a outra em **trabalho fluente** (trabalho vivo acontecendo).',
   ]),
   ('Por que não a taxa de lucro', [
     'm/v mede o grau de exploração, porque compara direto trabalho não pago com trabalho '
     'pago. É a "expressão exata do grau de exploração" da passagem citada.',
     'm/(c+v) dilui o mais-valor no gasto inteiro e sempre dá número menor, escondendo a '
     'exploração.',
     'Justamente essa taxa de lucro é a que aparece na superfície e orienta o cálculo '
     'capitalista. Só é desenvolvida no Livro III.',
     'Terceira forma equivalente: mais-produto comparado à parte do produto que corresponde '
     'ao trabalho necessário.',
     'Aplicação polêmica do capítulo: a "última hora" de Nassau Senior. O erro dele foi '
     'calcular o excedente sobre o valor total do produto em vez de sobre v.',
   ]),
 ],
 'nota_maxima': [
   'Escrever as **duas** fórmulas de forma explícita. O enunciado pede duas, e entregar '
   'uma só corta a nota pela metade.',
   'Mostrar a derivação da primeira a partir de c + v + m, com a subtração do c.',
   'Nomear v + m como produto de valor.',
   'Justificar **por que** o denominador é v e não o capital total.',
   'Demonstrar a equivalência, dizendo que v corresponde ao trabalho necessário e m ao '
   'excedente.',
   'Contrastar com a taxa de lucro e explicar o que ela esconde.',
 ],
 'erros': [
   'Apresentar m/(c+v) como se fosse a taxa de mais-valor.',
   'Dar as duas fórmulas sem demonstrar que são equivalentes.',
   'Dizer que o trabalho tem valor. Ele é a substância do valor.',
 ],
},

# ========================================================================= Q6
{
 'q': 6, 'cap': '7',
 'titulo': 'Cálculo com c = 410, v = 90, m = 90',
 'pede': 'Capital total, valor do produto, produto de valor e taxa de mais-valor.',
 'topicos': [
   ('As quatro grandezas pedidas', [
     '**i) Capital total adiantado** = c + v = 410 + 90 = **500**. O m não entra, porque é '
     'resultado e não adiantamento.',
     '**ii) Valor do produto** = c + v + m = 410 + 90 + 90 = **590**. É o maior número, '
     'porque inclui o valor que já existia nos meios de produção.',
     '**iii) Produto de valor** = v + m = 90 + 90 = **180**. Também sai de 590 − 410. Só o '
     'valor novo criado pelo trabalho vivo.',
     "**iv) Taxa de mais-valor** = m / v = 90 / 90 = **100%**.",
   ]),
   ('Interpretação que precisa estar na folha', [
     '100% significa que trabalho excedente e trabalho necessário são iguais, então a '
     'jornada se divide ao meio. Numa jornada de 12h, 6h pagam a força de trabalho e 6h vão '
     'sem contrapartida.',
     'O ponto que o exercício cobra é a diferença entre **valor do produto** (590) e '
     '**produto de valor** (180).',
     'Quem usa 590 como base chega a cerca de 15,25%, número que não mede nada, porque '
     'mistura valor criado com valor só repassado.',
   ]),
   ('Comparação que rende ponto extra', [
     'Taxa de lucro = m/(c+v) = 90/500 = **18%**. É o número que o capitalista olha.',
     'Contraste: 18% contra 100%. A taxa de lucro subestima drasticamente a exploração.',
     'Quanto maior o peso de c, maior a divergência entre as duas taxas.',
     'Composição: c/v ≈ 4,56, ou seja, cerca de 82% c e 18% v, típico de produção '
     'mecanizada.',
   ]),
 ],
 'nota_maxima': [
   'Entregar os quatro itens **numerados como o enunciado pede** (i, ii, iii, iv).',
   'Mostrar a conta, não só o resultado.',
   'Explicar por que o mais-valor não entra no capital adiantado.',
   'Explicitar a diferença entre valor do produto e produto de valor. Sem isso, a questão '
   'fica respondida mecanicamente e perde a parte conceitual.',
   'Interpretar o que significa uma taxa de 100%, dividindo uma jornada concreta.',
   'Acrescentar a taxa de lucro como comparação e comentar o contraste. Não é pedido, mas '
   'mostra domínio.',
 ],
 'erros': [
   'Somar m no capital adiantado, chegando a 590 em vez de 500.',
   'Trocar valor do produto por produto de valor.',
   'Calcular a taxa de mais-valor como 90/500 ou 90/590.',
   'Dar só os números sem interpretar.',
 ],
},

# ========================================================================= Q7
{
 'q': 7, 'cap': '7',
 'titulo': 'Consequência das inovações técnicas para a taxa de mais-valor',
 'pede': 'O efeito esperado e o mecanismo pelo qual ele acontece.',
 'topicos': [
   ('Resposta e cadeia causal', [
     'Resposta: a taxa de mais-valor **sobe**. Mas o caminho é indireto e passa pelo valor '
     'da força de trabalho.',
     '1. Inovação eleva a produtividade, mesma quantidade de trabalho produz mais.',
     '2. Cai o tempo de trabalho socialmente necessário por unidade, então cai o valor '
     'unitário das mercadorias. Valor e produtividade andam em sentido contrário.',
     '3. Se a queda atinge o que o trabalhador consome, cai o valor dos meios de '
     'subsistência e, com ele, o valor da força de trabalho.',
     '4. Com jornada fixa, encurta o trabalho necessário e alarga o trabalho excedente.',
     "5. m sobe e v desce, então m' sobe pelos dois lados. É o mecanismo do **mais-valor "
     'relativo** (caps. 10 a 13).',
     'Exemplo: jornada 12h com 6h necessárias dá 100%. Caindo o necessário para 4h, a taxa '
     'vai a 200%, sem a jornada mudar.',
   ]),
   ('Mais-valor extra, o motor imediato', [
     'Quem inova primeiro produz com valor individual abaixo do valor social, vende pelo '
     'valor social e fica com **mais-valor extra**.',
     'A vantagem é transitória, acaba quando a técnica se espalha e o novo valor social '
     'mais baixo se impõe.',
     'Mas é esse prêmio temporário que faz cada um correr para inovar. O resultado agregado '
     'é não intencional.',
   ]),
   ('Três qualificações que valem nota', [
     'A taxa só sobe se o **salário real** não subir na mesma proporção da produtividade. '
     'Quem fica com o ganho é questão de luta de classes, não de técnica.',
     'Inovação em setores que não produzem bens de consumo dos trabalhadores dá mais-valor '
     'extra ao inovador, mas **não** eleva a taxa geral.',
     'Efeito oposto na **taxa de lucro**, porque a inovação eleva a composição orgânica, e '
     "com m' dada isso derruba m/(c+v). Taxa de mais-valor subindo e taxa de lucro caindo, "
     'desenvolvido no Livro III.',
   ]),
 ],
 'nota_maxima': [
   'Não responder só "sobe". É preciso montar a cadeia causal passo a passo, porque o '
   'mecanismo é a questão.',
   'Deixar claro que o efeito passa pelo **valor da força de trabalho**, e não '
   'diretamente.',
   'Dar um exemplo numérico com jornada dividida.',
   'Mencionar o mais-valor extra como motivação individual e a sua transitoriedade.',
   'Incluir ao menos duas das três qualificações. A do salário real e a da taxa de lucro '
   'são as que mais diferenciam.',
 ],
 'erros': [
   'Dizer que a inovação eleva a taxa de mais-valor porque "o trabalhador produz mais", '
   'sem passar pelo valor da força de trabalho.',
   'Confundir taxa de mais-valor com taxa de lucro e concluir que as duas sobem.',
   'Esquecer que o mais-valor extra desaparece com a generalização da técnica.',
 ],
},

# ========================================================================= Q8
{
 'q': 8, 'cap': '9',
 'titulo': 'A oferta de trabalho que o capital explora fica independente da oferta de '
           'trabalhadores',
 'pede': 'Explicar a passagem citada.',
 'topicos': [
   ('Contexto', [
     "Massa de mais-valor: **M = m' × V**, taxa multiplicada pelo capital variável total.",
     'Em termos de trabalho, é o mais-valor tirado de um trabalhador médio multiplicado '
     'pelo número de trabalhadores.',
   ]),
   ('O argumento da passagem', [
     'O trabalho explorável é o **produto de dois fatores**: número de trabalhadores '
     '(grandeza extensiva) e quantidade tirada de cada um (duração e intensidade).',
     'Sendo multiplicação, os dois fatores são **substituíveis** até certo ponto.',
     'Logo, menos trabalhadores pode ser compensado com jornada mais longa ou trabalho mais '
     'intenso.',
     'Conclusão: o capital aumenta a massa de trabalho explorado sem aumentar o número de '
     'trabalhadores, então a oferta de trabalho (massa) se solta da oferta de trabalhadores '
     '(população).',
     'Exemplo: 100 pessoas × 8h = 800h. As mesmas 800h saem de 80 pessoas × 10h.',
   ]),
   ('Os "certos limites", a parte decisiva', [
     'A jornada tem **limite absoluto**: 24h do dia e, muito antes, limite físico do '
     'trabalhador e limite legal conquistado na luta de classes.',
     'Isso cria barreira à compensação: o mais-valor por trabalhador não passa da jornada '
     'máxima **menos** o trabalho necessário.',
     'Exemplo: necessário 6h, jornada máxima 18h, então o máximo por trabalhador equivale a '
     '12h, não importa a pressão.',
     'Lei formulada por Marx: a barreira absoluta da jornada média é barreira absoluta à '
     'compensação da redução de v pelo aumento de m\'.',
     '**Assimetria**: aumentar o número de trabalhadores amplia M sem limite interno, '
     'apertar um número menor bate em teto rígido.',
   ]),
   ('Consequências que a passagem prepara', [
     'Fundamenta a pressão permanente por jornada mais longa e trabalho mais intenso. Não é '
     'ganância, é o jeito de um capital de tamanho dado aumentar M.',
     'Explica por que colocar maquinaria, mesmo reduzindo trabalhadores, não derruba '
     'necessariamente M.',
     'Antecipa o cap. 23, porque se a massa de trabalho cresce sem a população crescer, a '
     'dinâmica do capital se solta da demografia.',
   ]),
 ],
 'nota_maxima': [
   'Explicar o argumento como **produto de dois fatores substituíveis**. É a chave da '
   'passagem.',
   'Dar exemplo aritmético mostrando a substituição.',
   'Desenvolver os "certos limites". Quem ignora a ressalva responde metade da questão, '
   'porque Marx a transforma em lei.',
   'Enunciar a barreira absoluta da jornada e dar um exemplo numérico dela.',
   'Apontar a assimetria entre os dois fatores.',
   'Ligar a passagem ao cap. 23 e ao exército industrial de reserva.',
 ],
 'erros': [
   'Responder só a primeira metade, dizendo que o capital pode explorar mais sem mais '
   'trabalhadores, e parar aí.',
   'Afirmar que a substituição entre os dois fatores é ilimitada.',
   'Confundir a massa de mais-valor com a taxa de mais-valor.',
 ],
},

# ========================================================================= Q9
{
 'q': 9, 'cap': '10',
 'titulo': 'O expediente para obter e ampliar o mais-valor relativo',
 'pede': 'Qual é o expediente adotado pelos capitalistas.',
 'topicos': [
   ('A distinção prévia', [
     '**Mais-valor absoluto**: alongar a jornada além do ponto em que o trabalhador repõe o '
     'valor da sua força de trabalho, com o trabalho necessário dado.',
     '**Mais-valor relativo**: com jornada dada, ou até menor, encurtar o trabalho '
     'necessário, o que alarga o excedente na mesma medida.',
   ]),
   ('O expediente, em cadeia', [
     'Jornada travada deixa um único caminho: reduzir o tempo de trabalho necessário.',
     'Para isso, reduzir o valor da força de trabalho.',
     'Para isso, reduzir o valor das mercadorias que determinam esse valor.',
     'E o único jeito de reduzir valor de mercadoria é **aumentar a produtividade do '
     'trabalho**.',
     'Resposta: o expediente é a **revolução permanente das condições técnicas e sociais da '
     'produção** para elevar a produtividade.',
   ]),
   ('Formas concretas (caps. 11 a 13)', [
     '**Cooperação** (cap. 11): força produtiva social maior que a soma das individuais, '
     'economia no uso dos meios de produção.',
     '**Divisão do trabalho na manufatura** (cap. 12): quebra o ofício em operações '
     'parciais, especializa e eleva a destreza, ao custo de mutilar o trabalhador.',
     '**Maquinaria e grande indústria** (cap. 13): troca a base subjetiva do ofício por '
     'sistema objetivo de máquinas. Forma mais desenvolvida.',
     '**Intensificação do trabalho**: aumenta o gasto por unidade de tempo, ganha '
     'importância quando a jornada tem limite legal.',
   ]),
   ('O motor imediato e a conclusão', [
     'Nenhum capitalista age pensando em reduzir o valor da força de trabalho. O que move '
     'cada um é o **mais-valor extra**.',
     'Quem adota método melhor produz abaixo do valor social, vende pelo valor social, '
     'fatura acima da média e ganha mercado.',
     'A vantagem se dissolve com a generalização, mas o resultado social fica: o valor das '
     'mercadorias caiu.',
     'Resultado coletivo é **efeito não intencional** da busca individual de vantagem.',
     'Conclusão metodológica: é por isso que o capital é tecnicamente dinâmico e '
     'revolucionário. E a inversão característica, o impulso a elevar a produtividade não '
     'existe para reduzir esforço, existe para baratear mercadoria e encurtar a parte da '
     'jornada que pertence ao trabalhador.',
   ]),
 ],
 'nota_maxima': [
   'Abrir pela distinção entre mais-valor absoluto e relativo. Sem ela, não se entende por '
   'que só sobra um caminho.',
   'Apresentar o expediente como **cadeia de necessidades**, da jornada travada até a '
   'produtividade, e não como afirmação solta.',
   'Nomear as formas concretas dos capítulos 11, 12 e 13.',
   'Explicar o mais-valor extra como motivação individual e marcar a sua transitoriedade.',
   'Dizer que o resultado social é não intencional. Esse ponto mostra compreensão do método '
   'de Marx.',
   'Fechar com a inversão, a produtividade não serve para aliviar o trabalho.',
 ],
 'erros': [
   'Responder "aumentar a produtividade" sem reconstruir a cadeia que leva até lá.',
   'Confundir mais-valor relativo com mais-valor absoluto, falando em alongar jornada.',
   'Dizer que os capitalistas se organizam para reduzir o valor da força de trabalho. Cada '
   'um age pelo mais-valor extra.',
 ],
},

# ======================================================================== Q10
{
 'q': 10, 'cap': '10',
 'titulo': 'Que mercadorias precisam ter o valor reduzido, e por quê',
 'pede': 'O tipo de mercadoria e a justificativa. **Duas perguntas.**',
 'topicos': [
   ('Resposta direta', [
     'As mercadorias que entram no **consumo habitual dos trabalhadores**, isto é, os '
     '**meios de subsistência** necessários para reproduzir a força de trabalho.',
     'Alimento, roupa, moradia e, em geral, os bens do padrão de consumo socialmente '
     'estabelecido da classe trabalhadora.',
   ]),
   ('O porquê, pela determinação do valor da força de trabalho', [
     'O valor da força de trabalho é fixado pelo tempo de trabalho socialmente necessário '
     'para reproduzi-la, ou seja, pelo valor dos meios de subsistência do trabalhador e da '
     'família.',
     'O tempo de trabalho necessário da jornada é exatamente o que produz o equivalente a '
     'esse valor.',
     'Sequência: cai o valor dos meios de subsistência → cai o valor da força de trabalho → '
     'encurta o trabalho necessário → com jornada dada, alarga o excedente → mais-valor '
     'relativo.',
     'Nenhum outro tipo de mercadoria faz isso, porque nenhum outro entra nessa '
     'determinação.',
     'Extensão indireta: vale também para os meios de produção usados para fazer esses '
     'bens. Barateia fertilizante, transporte ou tecido, e cai o valor da força de trabalho '
     'por essa via.',
   ]),
   ('O contraste que confirma', [
     'Salto de produtividade em **bens de luxo** barateia esses bens e dá mais-valor extra '
     'a quem inovou, mas não muda o valor da força de trabalho, então não gera mais-valor '
     'relativo para o capital social.',
     'Conclusão: o mais-valor relativo não vem do aumento da produtividade **em geral**, '
     'vem do aumento nos setores que determinam o custo de reprodução do trabalhador.',
     'Consequência histórica: importância estratégica dos setores de bens de consumo '
     'popular, e o preço dos alimentos como motivo de briga entre capital e trabalho e '
     'entre frações da classe dominante. Exemplo clássico, a revogação das Leis do Trigo.',
   ]),
   ('Qualificação', [
     'O resultado pressupõe que o barateamento vire **queda do valor da força de '
     'trabalho**, e não aumento do padrão de consumo real a valor constante.',
     'Como a determinação tem componente histórico e moral, quem fica com o ganho depende '
     'da relação de forças entre as classes.',
     'Na história as duas coisas andaram juntas, consumo real subindo e taxa de mais-valor '
     'subindo também.',
   ]),
 ],
 'nota_maxima': [
   'Responder as **duas** partes. Identificar o tipo de mercadoria e justificar pela '
   'determinação do valor da força de trabalho.',
   'Escrever a sequência causal completa, dos meios de subsistência até o mais-valor '
   'relativo.',
   'Usar o **contraste com bens de luxo**. É o que prova que você entendeu, e não apenas '
   'memorizou.',
   'Mencionar a extensão indireta aos insumos dos bens de consumo.',
   'Fechar com a qualificação sobre a repartição dos ganhos de produtividade.',
 ],
 'erros': [
   'Responder "todas as mercadorias" ou "as mercadorias em geral".',
   'Dizer que basta aumentar a produtividade em qualquer setor.',
   'Esquecer de justificar, entregando só o tipo de mercadoria.',
 ],
},

# ======================================================================== Q11
{
 'q': 11, 'cap': '13',
 'titulo': 'A relevância da maquinaria na organização do processo produtivo',
 'pede': 'Explicar a relevância da maquinaria segundo Marx.',
 'topicos': [
   ('Finalidade e limite do emprego', [
     'A importância não é só técnica. A maquinaria é o meio pelo qual o capital constrói uma '
     '**base material à sua própria imagem**.',
     'O capítulo a trata como a forma mais desenvolvida de produção de **mais-valor '
     'relativo**.',
     'Finalidade: não entra para aliviar o trabalho, entra para baratear mercadoria e '
     'encurtar a parte da jornada em que o trabalhador trabalha para si.',
     'Critério econômico de adoção: só é adotada quando o valor que ela repassa ao produto é '
     '**menor** que o valor da força de trabalho que substitui.',
     'Consequência aparentemente paradoxal: onde a força de trabalho é barata, a maquinaria '
     'entra mais devagar.',
     'A máquina nunca põe no produto mais valor do que perde pelo desgaste, então não é '
     'fonte de valor, é **capital constante**.',
   ]),
   ('A inversão trabalhador / meio de trabalho (ponto central)', [
     'Na **manufatura** quem organiza é o lado subjetivo. O processo se divide conforme a '
     'habilidade dos trabalhadores e se adapta a eles, a destreza humana é o ponto de '
     'partida.',
     'Na **grande indústria** quem organiza é o lado objetivo. O sistema de máquinas é um '
     'organismo técnico com lógica e ritmo próprios, e o trabalhador é encaixado nele.',
     'Imagem de Marx: na manufatura os trabalhadores são membros de um mecanismo vivo, na '
     'fábrica existe um mecanismo morto, independente deles, ao qual são incorporados como '
     '**apêndices vivos**.',
     'Da inversão sai a distinção **subsunção formal** (capital apenas se apropria de '
     'processos herdados do artesanato) contra **subsunção real** (capital transforma o '
     'processo por dentro e cria um modo de produzir que não existiria sem ele).',
     'Por isso a grande indústria é o primeiro modo de produção cuja base técnica combina '
     'com a sua forma social.',
   ]),
   ('Efeitos sobre a força de trabalho', [
     '**Mulheres e crianças**: a máquina dispensa força muscular e qualificação, amplia o '
     'material humano de exploração e derruba o valor da força de trabalho individual, '
     'porque a família inteira passa a contribuir para reproduzi-la.',
     '**Jornada mais longa** (contraintuitivo): o capital fixo precisa ser valorizado antes '
     'de ficar obsoleto, e a elevação da composição orgânica pressiona a taxa de lucro, '
     'empurrando o capital a buscar compensação no trabalho excedente.',
     '**Intensificação**: quando a lei limita a duração, a pressão vai para a intensidade. '
     'Foi a limitação legal que impulsionou o aperfeiçoamento técnico.',
   ]),
   ('Arma de classe e ambivalência', [
     'Torna o trabalhador substituível, desarma a resistência e é usada para quebrar '
     'greves. Marx a chama de arma mais poderosa para reprimir as revoltas periódicas.',
     'Alimenta a **superpopulação relativa** (cap. 23).',
     'Aprofunda a separação entre trabalho manual e intelectual, porque o saber do processo '
     'passa para dentro da máquina e volta contra o trabalhador como poder alheio.',
     'Dá ao regime de fábrica a forma de **despotismo**, com disciplina, regulamento, multa '
     'e vigilância.',
     'Ambivalência: Marx **não** condena a máquina em si, separa a máquina do uso '
     'capitalista dela. A grande indústria socializa a produção, cria o trabalhador '
     'coletivo e desenvolve as forças produtivas até tornar possível organização social '
     'superior. As mesmas condições que degradam criam as bases da emancipação.',
   ]),
 ],
 'nota_maxima': [
   'Começar pela **finalidade** capitalista da maquinaria, e não pela descrição técnica.',
   'Desenvolver a inversão manufatura contra grande indústria. É o ponto central e sem ele '
   'a resposta fica superficial.',
   'Usar os termos **subsunção formal** e **subsunção real**.',
   'Dizer que a máquina é capital constante e não cria valor.',
   'Explicar o paradoxo da jornada mais longa, porque é onde se mostra raciocínio e não '
   'memória.',
   'Mencionar a função de arma na luta de classes e a ligação com a superpopulação relativa.',
   'Fechar com a ambivalência, separando a máquina do seu emprego capitalista. Isso evita a '
   'leitura ingênua de que Marx era contra a tecnologia.',
 ],
 'erros': [
   'Apresentar Marx como crítico da tecnologia em si.',
   'Dizer que a máquina cria valor ou que agrega mais valor do que o seu desgaste.',
   'Tratar manufatura e grande indústria como diferença de tamanho, e não de princípio '
   'organizador.',
   'Esquecer que o critério de adoção compara o valor da máquina com o valor da força de '
   'trabalho dispensada.',
 ],
},

# ======================================================================== Q12
{
 'q': 12, 'cap': '21',
 'titulo': 'Destinação do mais-valor na reprodução simples',
 'pede': 'Qual destinação o capitalista deve dar ao mais-valor.',
 'topicos': [
   ('Resposta direta', [
     'Consumir **individualmente a totalidade** do mais-valor, gastando como renda, sem '
     'transformar nenhuma parte dele em capital adicional.',
   ]),
   ('A justificativa', [
     'Reprodução simples = repetir a produção **na mesma escala**, período após período.',
     'Logo o capital adiantado no ciclo novo precisa ter o mesmo tamanho do anterior.',
     'Do valor do produto (c + v + m), a parte c volta a ser meios de produção e a parte v '
     'volta a ser força de trabalho. Sobra o m.',
     'Se m fosse capitalizado, inteiro ou em parte, a escala cresceria e seria reprodução '
     'ampliada (cap. 22).',
     'Então m tem de ser todo gasto em **consumo improdutivo** do capitalista, em meios de '
     'consumo individual.',
   ]),
   ('Estatuto da hipótese', [
     'A reprodução simples é **abstração proposital**, não descrição da realidade, porque o '
     'capital tende por natureza a crescer.',
     'Congelar a escala permite isolar um resultado que o crescimento esconderia, que é o '
     'processo reproduzir a própria **relação de classe**.',
   ]),
   ('O resultado que a hipótese revela (ponto extra)', [
     'Consumindo todo o mais-valor por ano, depois de certo número de anos o capitalista '
     'já consumiu valor igual ao capital inicial.',
     'Dali em diante, o capital que ele tem é **inteiro mais-valor capitalizado**, isto é, '
     'trabalho alheio não pago.',
     'O título de propriedade continua o mesmo, mas o conteúdo econômico virou outro.',
     'Mesmo que o capital inicial viesse de trabalho próprio, a continuidade do processo o '
     'converte em valor apropriado sem equivalente. Isso derruba a legitimação da '
     'propriedade capitalista pelo esforço próprio.',
   ]),
 ],
 'nota_maxima': [
   'Dar a resposta direta na primeira frase. A questão é objetiva e o corretor procura '
   'isso.',
   'Justificar pela exigência de **escala constante**, mostrando o destino de cada parte do '
   'valor do produto.',
   'Usar a expressão **consumo improdutivo** ou equivalente.',
   'Contrastar com a reprodução ampliada, explicando o que aconteceria se m fosse '
   'capitalizado.',
   'Acrescentar o estatuto metodológico da hipótese e o resultado sobre o capital virar '
   'todo mais-valor capitalizado. É o que leva a questão de boa para ótima.',
 ],
 'erros': [
   'Dizer que o capitalista deve reinvestir o mais-valor. Isso é reprodução ampliada.',
   'Dizer que ele deve guardar ou poupar. Tem de **consumir**.',
   'Tratar a reprodução simples como se fosse o caso normal do capitalismo.',
 ],
},

# ======================================================================== Q13
{
 'q': 13, 'cap': '21',
 'titulo': 'A reprodução da relação social e o papel do consumo do trabalhador',
 'pede': 'Por que a reprodução do capital inclui a reprodução da relação de classe, e qual '
         'o papel do consumo do trabalhador. **Duas perguntas.**',
 'topicos': [
   ('A mudança de ângulo', [
     'Como **ato isolado**, o processo aparece como produção de mercadoria e de mais-valor.',
     'Como **processo contínuo**, de reprodução, aparece mais coisa. É essa mudança de '
     'ângulo que sustenta a passagem.',
     'Todo processo social de produção é também de reprodução, porque precisa repor sem '
     'parar as próprias condições materiais e sociais.',
     'No capital, os pressupostos são de um lado quem tem dinheiro e meios de produção, de '
     'outro quem só tem força de trabalho. É essa relação que o processo reproduz.',
   ]),
   ('O que a continuidade revela sobre o salário', [
     'No ato isolado, o salário parece dinheiro que o capitalista adianta do bolso dele, e '
     'a troca parece entre dois proprietários livres.',
     'Na repetição, a aparência cai: o valor com que ele paga o salário é **parte do valor '
     'que o próprio trabalhador produziu** no período anterior.',
     'O capital variável não é adiantamento de fundo externo, é pedaço do produto do '
     'trabalho alheio devolvido como salário.',
     'Marx: ele é só a forma histórica particular de aparição do fundo de meios de '
     'subsistência que o trabalhador tem de produzir e reproduzir sempre.',
   ]),
   ('A reprodução das duas classes', [
     'Do lado do capitalista: repõe e amplia a posse de meios de produção e dinheiro, '
     'reproduzindo-o como personificação do capital e comprador de força de trabalho.',
     'Do lado do trabalhador, em **dois sentidos**: reproduz a força de trabalho dele, '
     'mantendo-o apto, e reproduz a condição de **despossuído**, porque sai como entrou.',
     'Conclusão: a relação capitalista não é pressuposto externo dado de uma vez, é '
     'produzida continuamente pelo próprio funcionamento do processo.',
   ]),
   ('O consumo do trabalhador, caráter duplo', [
     '**Consumo produtivo**: dentro do processo, consome meios de produção e os transforma '
     'em produtos do capitalista. É produção direta para o capital.',
     '**Consumo individual**: fora do processo, consome os meios de subsistência comprados '
     'com o salário. Parece assunto particular dele.',
     'Mas pela ótica da reprodução é **momento necessário da reprodução do capital**, porque '
     'ao consumir ele não produz nada além da própria força de trabalho, que é a mercadoria '
     'de que o capital depende.',
     'Marx: é a produção do meio de produção mais indispensável para o capitalista.',
     '**Condição decisiva**: o consumo tem de gastar o salário por completo, sem deixar '
     'sobra que permita acumular e ficar independente. Reproduzir a força de trabalho é '
     'também reproduzir a despossessão.',
     'Comparação com a escravidão: o senhor precisa supervisionar a alimentação do escravo, '
     'o capitalista pode deixar por conta do interesse do próprio trabalhador. A coerção '
     'saiu da pessoa e foi para as **condições econômicas**.',
     'Indivíduo contra classe: o trabalhador pode trocar de patrão, mas não pode sair da '
     'classe capitalista. O trabalhador individual pertence a si mesmo, a classe '
     'trabalhadora pertence à classe capitalista.',
   ]),
 ],
 'nota_maxima': [
   'Responder as **duas** perguntas, e dar ao consumo do trabalhador espaço próprio. A '
   'segunda pergunta costuma ser respondida de passagem, e é metade da nota.',
   'Fazer a mudança de ângulo explícita, ato isolado contra processo contínuo.',
   'Revelar que o capital variável é produto do próprio trabalhador. É o achado da questão.',
   'Dizer que o trabalhador é reproduzido em dois sentidos, apto e despossuído.',
   'Distinguir consumo produtivo de consumo individual e mostrar que o individual também é '
   'produção de capital.',
   'Incluir a **condição de não deixar sobra**. Sem ela, a resposta não explica por que a '
   'despossessão se reproduz.',
   'Usar a comparação com a escravidão e o contraste indivíduo contra classe. Os dois são '
   'diferenciadores fortes.',
 ],
 'erros': [
   'Falar só da reprodução da força de trabalho e esquecer a reprodução da despossessão.',
   'Tratar o consumo individual como irrelevante para o capital.',
   'Dizer que o trabalhador é livre, sem distinguir o plano individual do plano de classe.',
   'Esquecer que o salário é pago com valor produzido pelo próprio trabalhador.',
 ],
},

# ======================================================================== Q14
{
 'q': 14, 'cap': '22',
 'titulo': 'Destinação do mais-valor na reprodução ampliada',
 'pede': 'Qual destinação o capitalista deve dar ao mais-valor para haver acumulação.',
 'topicos': [
   ('Resposta direta', [
     'Consumir individualmente **só uma parte** do mais-valor e **capitalizar o resto**, '
     'usando essa parte como capital adicional.',
     'Definição de Marx: acumulação é empregar o mais-valor como capital, ou reconverter '
     'mais-valor em capital.',
   ]),
   ('Como se dá a capitalização', [
     'Não é só guardar dinheiro. A parte capitalizada precisa se dividir entre **capital '
     'constante adicional** e **capital variável adicional**, nas proporções da composição '
     'técnica.',
     'Dinheiro parado não é capital. Ele só vira capital adicional quando se converte em '
     'meios de produção a mais e força de trabalho a mais, funcionando juntos.',
     'Isso exige que as duas coisas existam no mercado, e o **próprio sistema** fornece as '
     'duas.',
     'Os meios de produção adicionais já estão no **mais-produto** do período anterior, '
     'porque a produção capitalista produz máquina, matéria-prima e instalação acima da '
     'simples reposição.',
     'A força de trabalho adicional vem da **superpopulação relativa**, resultado da própria '
     'acumulação (cap. 23).',
     'Logo a acumulação é autossustentada, o capital produz as condições de crescer.',
   ]),
   ('Consequências e crítica', [
     'O capital adicional é, na origem, **mais-valor capitalizado**, trabalho alheio sem '
     'equivalente. A propriedade sobre produto alheio não pago se reproduz em escala '
     'crescente. Caráter cumulativo.',
     'A relação de classe não é só reproduzida, é reproduzida **em escala ampliada**.',
     'Crítica à **teoria da abstinência** (Senior): o fundo capitalizado não vem do trabalho '
     'nem da privação do capitalista, vem do mais-valor.',
     'E capitalizar não é escolha moral, é **coerção da concorrência**, que obriga cada '
     'capital a crescer sob pena de quebrar. O capitalista é forçado a acumular.',
   ]),
 ],
 'nota_maxima': [
   'Dar a resposta direta e citar a definição de acumulação como emprego do mais-valor como '
   'capital.',
   'Explicar que capitalizar exige **dividir** entre c e v adicionais, e não apenas poupar. '
   'É o que separa quem entendeu de quem decorou.',
   'Mostrar que o sistema fornece os dois elementos, com o mais-produto de um lado e a '
   'superpopulação relativa de outro.',
   'Afirmar o caráter autossustentado da acumulação.',
   'Incluir a crítica à teoria da abstinência e a coerção da concorrência.',
 ],
 'erros': [
   'Dizer que a acumulação depende de o capitalista ser poupador ou virtuoso.',
   'Tratar dinheiro acumulado como capital.',
   'Esquecer de dividir a parte capitalizada entre capital constante e variável.',
 ],
},

# ======================================================================== Q15
{
 'q': 15, 'cap': '22',
 'titulo': 'As circunstâncias que determinam o volume da acumulação',
 'pede': 'Quais são e explicar cada uma. **São quatro.**',
 'topicos': [
   ('Enquadramento', [
     'Com a proporção entre renda e capital já dada, o volume da acumulação depende do '
     '**tamanho do mais-valor**.',
     'Então tudo que determina esse tamanho determina o quanto se pode acumular.',
   ]),
   ('1. Grau de exploração da força de trabalho', [
     'Fator mais direto, age levantando a taxa de mais-valor por três caminhos.',
     'Alongar a jornada amplia o trabalho excedente sem mexer no necessário.',
     'Intensificar o trabalho aumenta o gasto por unidade de tempo.',
     'Comprimir o salário abaixo do valor da força de trabalho faz o fundo de consumo '
     'necessário do trabalhador virar fundo de acumulação do capital.',
     'Efeito extra que Marx destaca: alongar a jornada tira mais mais-valor **economizando '
     'capital fixo**, porque as mesmas instalações são usadas por mais horas.',
   ]),
   ('2. Produtividade social do trabalho', [
     'Barateia as mercadorias, então o mesmo valor de mais-valor comanda massa física maior. '
     'Em termos reais a acumulação cresce sem o mais-valor crescer em valor.',
     'Barateia os **elementos do próprio capital**, permitindo a mesma soma movimentar mais '
     'trabalho e mais matéria.',
     'Amplia o mais-produto, deixando disponíveis os elementos materiais do capital '
     'adicional.',
     'Permite aumentar consumo e acumulação ao mesmo tempo, aliviando o conflito entre os '
     'dois destinos.',
     'Provoca **desvalorização moral** do capital existente, forçando renovação em bases '
     'mais produtivas.',
   ]),
   ('3. Diferença entre capital empregado e capital consumido (a mais original)', [
     'Os meios de trabalho funcionam **inteiros** durante toda a vida útil, mas repassam ao '
     'produto só a fração do desgaste do período.',
     'A diferença entre o conjunto em operação e o valor efetivamente repassado é **serviço '
     'gratuito** do trabalho passado ao capital.',
     'Marx compara isso à ação gratuita das forças da natureza.',
     'Quanto maior e mais durável o aparato já acumulado, maior a diferença.',
     'Vale o mesmo para **ciência e conhecimento técnico**, que o capital usa sem pagar.',
   ]),
   ('4. Grandeza do capital adiantado', [
     "Com m' dada, a massa de mais-valor é proporcional ao capital variável, isto é, ao "
     'número de trabalhadores explorados.',
     'Logo, maior capital significa maior volume absoluto de acumulação.',
     'Isso torna o processo **cumulativo** e forma a base material da concentração e da '
     'centralização (cap. 23).',
   ]),
   ('Fecho crítico', [
     'Marx encerra criticando o **dogma do fundo de trabalho** (wage fund), que supõe fundo '
     'de salários de tamanho tecnicamente dado.',
     'Dele sairia a conclusão de que salário só sobe à custa de emprego, e que reivindicação '
     'operária é autodestrutiva.',
     'O exame das quatro circunstâncias mostra que a divisão do produto **não** é dada por '
     'necessidade técnica. O fundo é elástico, resultado da repartição do produto de valor, '
     'determinada pela relação de forças entre as classes.',
     'O dogma transforma resultado histórico em limite natural.',
   ]),
 ],
 'nota_maxima': [
   'Entregar as **quatro** circunstâncias, nomeadas e numeradas. Faltar uma custa um quarto '
   'da questão.',
   'Explicar cada uma, não apenas listar. O enunciado diz "Explique".',
   'Nas três vias do grau de exploração, incluir a compressão salarial, que costuma ser '
   'esquecida.',
   'Desenvolver a terceira circunstância com cuidado, porque é a menos intuitiva e a que '
   'mais diferencia. Use a comparação com as forças da natureza.',
   'Mencionar o caráter cumulativo na quarta.',
   'Fechar com a crítica ao dogma do fundo de trabalho. Mostra que você leu a seção final '
   'do capítulo.',
 ],
 'erros': [
   'Listar só duas ou três circunstâncias.',
   'Confundir a terceira com depreciação contábil. O ponto é o serviço gratuito do capital '
   'empregado além do consumido.',
   'Tratar o fundo de salários como grandeza tecnicamente fixa.',
 ],
},

# ======================================================================== Q16
{
 'q': 16, 'cap': '23',
 'titulo': 'Acumulação com composição orgânica constante e com composição crescente',
 'pede': 'Em cada cenário, os resultados quanto a (i) produtividade do trabalho e (ii) '
         'relação entre oferta e demanda de trabalho. **Dois cenários × dois efeitos = '
         'quatro respostas.**',
 'topicos': [
   ('Definição de partida', [
     'Composição orgânica = relação **c / v**, considerada enquanto reflete a composição '
     '**técnica**, isto é, a proporção entre massa de meios de produção e trabalho vivo '
     'necessário para operá-la.',
     'Cenário 1 é abstração de método. Cenário 2 é o caso que realmente acontece.',
   ]),
   ('Cenário 1, composição constante', [
     '**(i) Produtividade**: constante por hipótese. A composição técnica não muda e a '
     'escala cresce multiplicando unidades produtivas com a mesma técnica. Acumulação '
     'puramente quantitativa, extensiva.',
     '**(ii) Oferta e demanda**: v cresce na mesma proporção de C, e como é v que determina '
     'a demanda, ela cresce proporcionalmente à acumulação, exigindo mais trabalhadores na '
     'mesma proporção.',
     'Se a acumulação corre mais rápido que a população, demanda passa oferta e o **salário '
     'sobe**.',
     'Salário subindo derruba a taxa de mais-valor e a massa para capitalizar, o que freia a '
     'acumulação, reduz a demanda e traz a proporção de volta. Movimento oscilatório.',
     'Marx: é o mecanismo pelo qual a produção capitalista **remove sozinha os obstáculos '
     'que ela mesma cria**.',
     'Limite da alta salarial: é melhora apenas **quantitativa** que não suprime a '
     'dependência, porque o trabalhador segue despossuído e obrigado a vender a força de '
     'trabalho.',
     'Já aqui se estabelece a inversão da explicação clássica, pois é a acumulação que '
     'governa a demanda por trabalho, e não a população que governa a acumulação.',
   ]),
   ('Cenário 2, composição crescente', [
     '**(i) Produtividade**: **cresce**, e o crescimento é ao mesmo tempo causa e efeito da '
     'elevação da composição orgânica, porque a produtividade aparece materialmente no '
     'aumento da massa de meios de produção por trabalhador.',
     'Em valor o movimento é parcialmente amortecido, porque a produtividade barateia também '
     'os meios de produção, então a composição em valor cresce **menos** que a técnica.',
     'Tendência inequívoca: v cai em termos relativos e, em alguns setores, até em termos '
     'absolutos.',
     '**(ii) Demanda**: cresce **menos que proporcionalmente** ao capital. Um capital que '
     'dobra pode precisar de bem menos que o dobro de trabalhadores.',
     '**(ii) Oferta**: o capital faz **atração e repulsão** ao mesmo tempo, atraindo quando '
     'amplia escala e abre setores, repelindo quando substitui por máquina.',
     'Saldo: produção contínua de população relativamente excedente, o **exército industrial '
     'de reserva**. A própria acumulação produz a oferta de que precisa.',
     'A oferta deixa de ser dado demográfico externo e passa a ser produto interno do '
     'movimento do capital.',
     'A pressão da reserva regula os salários, viabiliza a intensificação e enfraquece a '
     'resistência. Os salários passam a ser regulados pela expansão e contração dela ao '
     'longo do ciclo industrial.',
   ]),
   ('Fecho, a lei geral absoluta', [
     'Quanto maiores a riqueza social e a produtividade do trabalho, maior o exército '
     'industrial de reserva e maior a massa do pauperismo.',
     'Riqueza crescente e miséria crescente saem do **mesmo** processo, não apesar dele.',
     'Imagem final: a lei que mantém a superpopulação em equilíbrio com a acumulação prende '
     'o trabalhador ao capital mais firmemente que as cunhas de Hefesto prendiam Prometeu.',
   ]),
 ],
 'nota_maxima': [
   'Organizar a resposta em **quatro blocos** explícitos, cenário 1 com (i) e (ii), cenário '
   '2 com (i) e (ii). O enunciado pede exatamente isso e a estrutura já vale nota.',
   'Definir composição orgânica antes de usar.',
   'No cenário 1, descrever o **movimento oscilatório** completo, não só "o salário sobe".',
   'Incluir o limite da alta salarial, que é melhora quantitativa sem suprimir a '
   'dependência.',
   'No cenário 2, explicar que a composição em **valor** cresce menos que a técnica, por '
   'causa do barateamento dos meios de produção. Detalhe fino que diferencia.',
   'Usar o par **atração e repulsão** e nomear o exército industrial de reserva.',
   'Afirmar que a acumulação produz a própria oferta de trabalho.',
   'Fechar com a lei geral absoluta da acumulação capitalista.',
 ],
 'erros': [
   'Responder os dois cenários sem separar os dois efeitos pedidos, deixando o corretor '
   'caçar as quatro respostas.',
   'Dizer que no cenário 1 a produtividade cresce. Ela é constante por hipótese.',
   'Dizer que a demanda por trabalho é determinada pelo capital total. É determinada por v.',
   'Tratar a alta de salários do cenário 1 como ganho estrutural para o trabalhador.',
 ],
},

# ======================================================================== Q17
{
 'q': 17, 'cap': '23',
 'titulo': 'Concentração e centralização do capital, com o papel do crédito e da sociedade '
           'por ações',
 'pede': 'No que consistem os dois processos e a importância do crédito e da sociedade por '
         'ações para a **centralização**. **Duas perguntas.**',
 'topicos': [
   ('Concentração', [
     'Crescimento do tamanho dos **capitais individuais** como resultado direto da '
     'acumulação.',
     'Cada capitalista, capitalizando parte do mais-valor, aumenta o capital sob o comando '
     'dele e junta mais meios de produção e mais trabalhadores.',
     'Limites e forças contrárias: é limitada pelo crescimento da riqueza social, porque '
     'cada capital é fração do capital social.',
     'E é contrariada pelo **aumento do número de capitais**, tanto por capitais novos como '
     'por fragmentação dos existentes, sobretudo na divisão de herança.',
     'Logo é processo **lento**, que anda no ritmo da acumulação.',
   ]),
   ('Centralização', [
     'Concentração de capitais **já formados**. Atração de capital por capital, reunião de '
     'muitos capitais menores em poucos maiores.',
     'Marx a caracteriza como **expropriação de capitalista por capitalista**.',
     '**Diferença essencial**: não altera a magnitude do capital social total, altera só a '
     'distribuição. É redistribuição, não criação de capital novo.',
     'Daí a consequência decisiva: **não depende do ritmo da acumulação** e pode andar muito '
     'mais rápido, por simples mudança de propriedade e de comando.',
     'Marx: o mundo continuaria sem ferrovias se fosse preciso esperar a acumulação '
     'individual levar capitais ao tamanho necessário.',
     'Mecanismo 1, **concorrência**: a briga se trava no barateamento, que depende da '
     'produtividade, que depende da escala. Capitais maiores derrotam menores, cujos '
     'capitais vão em parte para os vencedores.',
   ]),
   ('O papel do crédito', [
     'Trajetória em três etapas: auxiliar modesto da acumulação, depois **arma nova e '
     'terrível** na luta da concorrência, por fim **imenso mecanismo social de '
     'centralização**.',
     'Permite ao capitalista individual usar o capital alheio e as poupanças dispersas de '
     'toda a sociedade.',
     'Desconecta a escala de operação do **patrimônio pessoal** do dono. Quem comanda a '
     'produção deixa de ser quem tem riqueza própria e passa a ser quem mobiliza capital '
     'social.',
     'Transforma dinheiro parado, que não funcionaria como capital, em capital ativo '
     'concentrado em poucas mãos.',
     'Dá aos capitais maiores vantagem extra, porque conseguem crédito melhor, o que acelera '
     'a eliminação dos menores.',
     'Marx o chama de uma das **alavancas mais poderosas** da centralização.',
   ]),
   ('O papel da sociedade por ações', [
     'Junta capitais individualmente pequenos num capital único de grande porte, viabilizando '
     'escala impossível para capital isolado, como ferrovia e siderurgia.',
     'Separa **propriedade** de **gestão**. Acionista é proprietário sem função produtiva, a '
     'direção fica com administradores assalariados.',
     'O capital assume **forma diretamente social** dentro do próprio capitalismo, tema '
     'desenvolvido no Livro III.',
     'Acelera muito a centralização, porque dá para comprar o controle adquirindo '
     'participação, sem comprar a empresa inteira.',
   ]),
   ('Articulação final', [
     'A centralização **não substitui** a acumulação, ela potencia os efeitos dela.',
     'Permitindo ampliar a escala de repente, acelera a revolução na composição técnica e '
     'intensifica a repulsão de trabalhadores.',
     'Enquanto a acumulação eleva a composição orgânica gradualmente, a centralização produz '
     '**saltos** que tornam massas de trabalhadores supérfluas de uma vez.',
     'Por isso concentração e centralização são mediações entre a acumulação e a produção do '
     'exército industrial de reserva.',
   ]),
 ],
 'nota_maxima': [
   'Marcar a diferença essencial, concentração altera o tamanho dos capitais pela '
   'acumulação, centralização só redistribui capital existente.',
   'Explicar **por que** a centralização é mais rápida, ligando a velocidade ao fato de não '
   'depender da acumulação.',
   'Mencionar as contratendências da concentração, principalmente a fragmentação por '
   'herança.',
   'Tratar crédito e sociedade por ações **separadamente**, porque o enunciado pede os dois.',
   'No crédito, destacar que ele desliga a escala do patrimônio pessoal e mobiliza capital '
   'social.',
   'Na sociedade por ações, destacar a separação entre propriedade e gestão.',
   'Fechar ligando a centralização à produção da superpopulação relativa. Essa articulação '
   'é o diferencial.',
 ],
 'erros': [
   'Usar concentração e centralização como sinônimos.',
   'Dizer que a centralização aumenta o capital social total.',
   'Falar do crédito e esquecer a sociedade por ações, ou o contrário.',
   'Tratar o crédito apenas como financiamento, sem o papel de centralizar.',
 ],
},

# ======================================================================== Q18
{
 'q': 18, 'cap': '23',
 'titulo': 'Por que o exército industrial de reserva é funcional para o capital',
 'pede': 'Explicar a funcionalidade da superpopulação relativa.',
 'topicos': [
   ('Preliminar que precisa abrir a resposta', [
     'A superpopulação relativa **não** é excedente em relação aos meios de subsistência, '
     'como supõe Malthus.',
     'É excedente em relação às **necessidades médias de valorização do capital**. O '
     'critério é a rentabilidade, não um limite natural.',
     'E ela é **produzida pela própria acumulação**, pela elevação da composição orgânica. A '
     'funcionalidade vem dessas duas características.',
   ]),
   ('1. Elasticidade para a acumulação', [
     'A acumulação não é movimento regular, acontece em saltos, por setor e por região, '
     'seguindo o ciclo industrial (prosperidade, crise, estagnação).',
     'Nas fases de expansão o capital precisa jogar massas de trabalhadores em pontos '
     'decisivos, de repente, sem tirar ninguém dos setores que já funcionam.',
     'Só é possível com contingente disponível pronto para ser absorvido. A reserva é esse '
     '**reservatório**.',
     'Ela solta a oferta de trabalho dos limites naturais do crescimento populacional, que é '
     'lento e demora uma geração para responder.',
   ]),
   ('2. Regulação dos salários', [
     'A pressão de quem está desempregado sobre quem está empregado mantém o salário no que '
     'a valorização suporta.',
     'Na expansão, impede que a demanda crescente comprometa a taxa de mais-valor. Na '
     'contração, deprime o salário.',
     'Marx: os movimentos gerais do salário são regulados **exclusivamente** pela expansão e '
     'contração do exército industrial de reserva, e não pelo número absoluto da população.',
   ]),
   ('3. Disciplina e 4. círculo do sobretrabalho', [
     'Massa disponível aumenta a concorrência **entre os próprios trabalhadores**.',
     'Quem está empregado sabe que pode ser trocado, o que reduz a capacidade de recusar '
     'jornada longa e ritmo intenso.',
     'Enfraquece sindicato e greve, porque o capital tem substituto na hora.',
     'Permite impor disciplina de fábrica gastando menos com coerção direta.',
     'Círculo perverso: o sobretrabalho de quem está empregado **engrossa** a fila dos '
     'desempregados, e a pressão dessa fila obriga os empregados a aceitar ainda mais '
     'sobretrabalho. Os dois se alimentam.',
     'É também por isso que o capital resiste tanto à redução da jornada, porque dividir o '
     'trabalho disponível entre mais gente diminuiria a reserva.',
   ]),
   ('5 e 6. Independência demográfica e sustentação da taxa', [
     'Como a acumulação produz a própria oferta, o capital se solta da **dependência '
     'demográfica**, criando e destruindo disponibilidade em prazos muito mais curtos.',
     'A lei de oferta e demanda passa a funcionar dentro de limites que o próprio capital '
     'estabelece.',
     'Segurando os salários, a reserva ajuda a sustentar a taxa de mais-valor, compensando '
     'em parte a pressão da composição orgânica sobre a taxa de lucro.',
   ]),
   ('Ressalva final', [
     'Reconhecer a funcionalidade não é dizer que existe harmonia.',
     'A mesma superpopulação é a forma de existência do **pauperismo** e da degradação.',
     'As formas que Marx distingue, **flutuante, latente e estagnada**, mais o pauperismo '
     'propriamente dito, mostram condição permanente e estruturada, não acidente de '
     'conjuntura.',
     'Funcionalidade para o capital e destruição para os trabalhadores são o mesmo fato '
     'visto de dois lados.',
   ]),
 ],
 'nota_maxima': [
   'Abrir esclarecendo **em que sentido** a população é excedente. Sem isso a resposta cai '
   'na leitura malthusiana.',
   'Dizer que a reserva é produzida pela própria acumulação, e não herdada de fora.',
   'Entregar no mínimo três funções distintas. Elasticidade, regulação salarial e disciplina '
   'são as essenciais.',
   'Incluir o **círculo entre sobretrabalho e desemprego**, que é o ponto mais fino.',
   'Citar a tese de que os salários são regulados pela reserva e não pela população '
   'absoluta.',
   'Fechar com a ressalva do pauperismo, mostrando que funcionalidade não significa '
   'harmonia. Evita a leitura cínica da questão.',
 ],
 'erros': [
   'Tratar a superpopulação como excesso de gente em relação aos alimentos.',
   'Apresentar o desemprego como falha ou disfunção do sistema, quando a questão pede '
   'justamente a **funcionalidade**.',
   'Dar só uma função, normalmente a de rebaixar salários.',
   'Esquecer que a reserva é produto da acumulação.',
 ],
},

# ======================================================================== Q19
{
 'q': 19, 'cap': '23',
 'titulo': 'Les dés sont pipés, o capital agindo sobre demanda e oferta de trabalho',
 'pede': 'Explicar a passagem, mostrar como o capital atua nos dois lados e por que a '
         'dinâmica da acumulação se sobrepõe à dinâmica demográfica. **Três perguntas.**',
 'topicos': [
   ('O alvo da crítica', [
     'A visão corrente trata demanda e oferta de trabalho como **duas forças '
     'independentes** que se encontram no mercado, e da interação sairia o salário.',
     'A demanda viria do crescimento do capital, a oferta do crescimento da população, '
     'governado por leis demográficas supostamente naturais (Malthus).',
     'O salário seria resultado neutro do encontro de duas cadeias causais separadas.',
     'Marx responde que o jogo é fraudado, **os dados estão viciados**, porque o capital age '
     'nos dois lados ao mesmo tempo. O resultado já está decidido por um movimento só, o da '
     'acumulação.',
   ]),
   ('Lado da demanda, três passos', [
     'Quem compra força de trabalho é o **capital variável**, não o capital total. A demanda '
     'depende só de uma parte.',
     'Com o avanço da acumulação a composição orgânica sobe, e v cresce menos que C, podendo '
     'cair em termos absolutos. Logo a demanda **não é idêntica** ao crescimento do capital.',
     'Além disso o capital amplia a massa de trabalho sem ampliar o número de trabalhadores, '
     'alongando a jornada e intensificando (cap. 9). Nem demanda por horas vira demanda por '
     'trabalhadores.',
   ]),
   ('Lado da oferta, o ponto que a visão corrente ignora', [
     '**Repulsão** de trabalhadores já empregados: a maquinaria torna supérfluo quem estava '
     'em atividade e joga essa gente no mercado. O capital não só encontra trabalhador '
     'disponível, ele **fabrica** trabalhador disponível.',
     '**Proletarização** de produtores independentes: destruição do artesanato e da pequena '
     'produção rural expropria camadas que viviam fora da relação assalariada.',
     '**Incorporação de novas camadas**: mulheres e crianças, atraídas pela própria mudança '
     'técnica que dispensa força física e qualificação. Amplia a oferta sem nenhuma mudança '
     'demográfica. Vale também para população rural (superpopulação latente) e migração.',
     '**Prolongamento e intensificação**: o sobretrabalho substitui o trabalho de outros, '
     'engrossa a reserva e desgasta o trabalhador prematuramente.',
     'Síntese de todos: o **exército industrial de reserva**, que é a oferta que de fato '
     'importa para o capital.',
   ]),
   ('Por que a acumulação se sobrepõe à demografia, três razões', [
     '**Velocidade**: população demora uma geração entre nascimento e entrada no mercado, '
     'enquanto a acumulação mobiliza ou descarta massas em poucos anos. A variável rápida '
     'manda na lenta.',
     '**O que conta é a disponibilidade, não a população**: gente que existe mas não está '
     'disponível como força de trabalho não é oferta de trabalho. Converter população em '
     'oferta é o que a acumulação faz.',
     '**Lei histórica no lugar de lei natural**: cada modo de produção tem a sua lei de '
     'população, e no capitalismo ela é a produção de superpopulação relativa pela '
     'acumulação.',
     'Inversão completa: não é a população que pressiona os meios de subsistência, é o '
     'capital que produz a população excedente de que precisa. A miséria é efeito da '
     'riqueza, não do contrário.',
   ]),
   ('Consequência política', [
     'A lei de oferta e demanda continua funcionando, mas dentro de limites que o próprio '
     'capital estabelece, o que tira dela o caráter de **árbitro neutro**.',
     'Daí a necessidade de ação coletiva, organização sindical e legislação protetora, que '
     'são a tentativa de interferir num jogo cujas regras já estão viciadas.',
   ]),
 ],
 'nota_maxima': [
   'Começar reconstruindo a **visão que Marx ataca**. Sem o alvo, a crítica não faz sentido.',
   'Tratar os dois lados **separadamente** e com igual cuidado. O lado da oferta é o que '
   'diferencia, porque é o que a visão corrente ignora.',
   'Dar no mínimo três mecanismos pelos quais o capital produz a oferta.',
   'Responder explicitamente a terceira pergunta, sobre acumulação contra demografia, com ao '
   'menos duas das três razões.',
   'Usar a formulação de que cada modo de produção tem a sua própria lei de população.',
   'Fechar com a inversão em relação a Malthus, miséria como efeito da riqueza.',
 ],
 'erros': [
   'Explicar só o lado da demanda e deixar a oferta de fora. Perde mais da metade.',
   'Dizer que a demanda por trabalho é dada pelo capital total.',
   'Deixar a terceira pergunta sem resposta, que é o caso mais comum nessa questão.',
   'Tratar a superpopulação como fenômeno natural ou demográfico.',
 ],
},

# ======================================================================== Q20
{
 'q': 20, 'cap': '24',
 'titulo': 'A história real da acumulação primitiva e a formação das duas classes',
 'pede': 'Os contornos da história real e os elementos que explicam (a) a formação da classe '
         'trabalhadora e (b) a formação da classe capitalista. **Três partes.**',
 'topicos': [
   ('A crítica da anedota e o conceito', [
     'A anedota é a versão que a economia política dá da origem do capital. Marx a trata '
     'como equivalente, na economia, do **pecado original** na teologia.',
     'Dois defeitos lógicos: explica o resultado pelo próprio resultado, colocando como '
     'causa a desigualdade que deveria explicar, e **naturaliza** um processo histórico, '
     'apresentando como virtude individual o que foi expropriação violenta e ação do Estado.',
     'Conceito: a acumulação primitiva não resulta do capitalismo, é a acumulação que **vem '
     'antes dele e o constitui**, o ponto de partida.',
     'Conteúdo: processo de **separação**, a cisão entre o produtor e os meios de produção.',
     'A relação capitalista exige duas condições que não existem na natureza, de um lado '
     'trabalhadores livres e despossuídos, de outro meios de produção e dinheiro '
     'concentrados em poucas mãos. A acumulação primitiva produz as duas ao mesmo tempo.',
     'Tese sobre o processo efetivo: na história real o papel principal é da conquista, da '
     'escravização, do roubo e do assassinato, em resumo, da **violência**. História '
     'inscrita com traços de sangue e fogo.',
   ]),
   ('(a) Formação da classe trabalhadora, expropriação', [
     '**Caráter duplo**, e é o que importa guardar. O produtor é libertado da servidão e, ao '
     'mesmo tempo, despojado dos meios de produção e subsistência. Fica livre **do** senhor e '
     'livre **de** propriedade. Sem o segundo, o primeiro não produziria assalariado.',
     'Dissolução dos **séquitos feudais**, que joga no mercado massas de homens sem meio de '
     'vida.',
     '**Cercamento das terras comuns** e usurpação dos campos comunais.',
     'Conversão de terra de lavoura em **pasto para ovelha**, sob o impulso da indústria da '
     'lã.',
     '**Limpeza das propriedades**, com demolição de casas e expulsão de aldeias inteiras.',
     'Confisco dos bens da **Igreja** na Reforma, vendidos a preço nominal, mais usurpação '
     'dos domínios do Estado.',
     'Nos séculos XVIII e XIX, forma legal com os **decretos de cercamento**, que Marx chama '
     'de forma parlamentar do roubo.',
     '*Clearances* das Terras Altas da **Escócia**, população substituída por ovelha e '
     'depois por reserva de caça.',
   ]),
   ('(a) Formação da classe trabalhadora, coerção', [
     'O expropriado não vira operário disciplinado sozinho, vira primeiro **vagabundo e '
     'mendigo**.',
     '**Legislação sanguinária** dos séculos XV a XVII, com açoite, marca de ferro, '
     'escravização e execução de vagabundos sob Henrique VIII, Eduardo VI e Isabel. Objetivo, '
     'empurrar para o trabalho assalariado.',
     'Estatutos que fixam **salário máximo** e proíbem associação de trabalhadores, vigentes '
     'até o século XIX. O Estado atuando direto para rebaixar o preço do trabalho.',
     'Formação do **mercado interno**, porque a destruição da indústria doméstica rural e a '
     'separação entre agricultura e manufatura transformam camponeses em compradores de '
     'mercadoria.',
     'Marx insiste que leva **tempo e coerção prolongada** para a classe nova enxergar as '
     'exigências do capital como leis naturais óbvias. Disciplina de fábrica é resultado '
     'histórico, não disposição espontânea.',
   ]),
   ('(b) Formação da classe capitalista', [
     '**Vertente interna**: gênese do **arrendatário capitalista** inglês, favorecida por '
     'arrendamento de longo prazo, pela desvalorização dos metais preciosos, que derrubou o '
     'valor real das rendas e dos salários fixados em termos nominais, e pela usurpação das '
     'terras comuns.',
     'Também na interna, conversão de mestres de corporação e, principalmente, de '
     '**comerciantes e usurários** em capitalistas industriais.',
     '**Vertente externa**, que Marx apresenta com ironia como o *idílio* da acumulação '
     'primitiva, e é a decisiva.',
     'Pilhagem colonial, descoberta da América e da rota para as Índias, saque das Índias '
     'Orientais, extermínio e escravização das populações indígenas, minas de **Potosí**.',
     '**Tráfico de escravos e escravidão nas Américas**, com a África transformada em '
     'reserva para a caça comercial de pele negra, o comércio triangular, Liverpool e '
     'Bristol. A escravidão colonial é o **pedestal** da indústria inglesa, inclusive em '
     'sentido material, porque o algodão das plantações escravistas era a matéria-prima de '
     'Lancashire.',
     '**Sistema colonial**, monopólios, Companhias das Índias holandesa e inglesa, monopólio '
     'do sal e do ópio, arrecadação extorsiva em Bengala e as fomes que dela resultaram.',
     '**Dívida pública**, uma das alavancas mais poderosas. Transforma dinheiro improdutivo '
     'em capital, cria classe de rentistas, dá aos títulos a aptidão de circular como '
     'capital e origina o sistema bancário moderno e as bolsas.',
     '**Sistema tributário**, complemento da dívida. Incidindo sobre os meios de '
     'subsistência, acelera a proletarização.',
     '**Protecionismo** e guerras comerciais, meio artificial de fabricar fabricantes.',
   ]),
   ('O papel do Estado e o fecho teórico', [
     'O fio que une tudo é a **ação sistemática do poder estatal**. A expropriação não foi '
     'obra do mercado, foi de lei, decreto, tribunal, exército, frota e companhia '
     'privilegiada.',
     'Formulação central: a **violência é a parteira** de toda sociedade velha grávida de '
     'uma nova, e ela mesma é uma **potência econômica**. Isso desfaz a oposição entre '
     'economia e política que a anedota pressupõe.',
     'Sentença famosa: o capital vem ao mundo escorrendo sangue e sujeira por todos os poros.',
     '**Resultado teórico, o que mais importa**: se a separação entre produtores e meios de '
     'produção é histórica e não natural, então ela é **transitória**, e a propriedade '
     'privada capitalista não tem fundamento em nenhum direito originário vindo do trabalho '
     'próprio.',
     'Fecho de Marx: tendência histórica da acumulação, a **expropriação dos '
     'expropriadores**, formulada como negação da negação.',
     'O cap. 25, sobre a teoria moderna da colonização, confirma por outro caminho, porque '
     'nas colônias com terra acessível a relação capitalista não se formava sozinha e '
     'precisava ser criada por meio estatal, como vender terra a preço proibitivo.',
   ]),
 ],
 'nota_maxima': [
   'Atacar a anedota com os **dois defeitos lógicos** nomeados, circularidade e '
   'naturalização. Não basta dizer que Marx discorda.',
   'Definir a acumulação primitiva como **processo de separação** e como pré-história do '
   'capital, não como acumulação dentro do capitalismo.',
   'Explicitar as **duas condições** que ela produz simultaneamente.',
   'Na parte (a), usar o **caráter duplo** da libertação, livre do senhor e livre de '
   'propriedade. É o núcleo conceitual.',
   'Na parte (a), não parar na expropriação. Incluir a **coerção legal** que transforma '
   'expropriado em operário disciplinado.',
   'Na parte (b), separar vertente interna de externa e dizer que a externa é decisiva.',
   'Na parte (b), citar no mínimo quatro elementos da vertente externa. Tráfico e dívida '
   'pública são os que mais contam.',
   'Afirmar o papel do **Estado** e citar a violência como potência econômica.',
   'Fechar com o resultado teórico, a transitoriedade da separação. É o que transforma '
   'descrição histórica em argumento.',
 ],
 'erros': [
   'Narrar os fatos históricos sem o conceito de separação. Vira aula de história e perde o '
   'ponto teórico.',
   'Esquecer a parte da coerção legal e tratar a formação do proletariado só como '
   'expropriação.',
   'Desenvolver (a) bem e correr em (b), que é o desequilíbrio mais comum nessa questão.',
   'Deixar de fora o papel do Estado, apresentando o processo como econômico apenas.',
   'Não chegar ao resultado teórico, que é onde a questão fecha.',
 ],
},
]
