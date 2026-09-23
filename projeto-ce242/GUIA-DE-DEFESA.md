# Guia de defesa — passo a passo do projeto

Este documento existe para uma finalidade: permitir que vocês **expliquem cada
decisão e cada número** do relatório, incluindo na sabatina, onde há 20 a 30
minutos de perguntas depois da apresentação.

Ele não é material de entrega. É material de estudo.

Leia na ordem. Cada passo tem **o que foi feito**, **por que**, e **como
verificar você mesmo**.

---

## Passo 0 — Entenda o que é a RAIS antes de tocar no código

A RAIS é uma **declaração obrigatória anual** que todo estabelecimento formal
entrega ao Ministério do Trabalho. Isso tem três consequências que você precisa
saber de cor:

1. **É censo, não amostra.** Não há erro amostral, intervalo de confiança nem
   peso de expansão. Se alguém na sabatina perguntar o intervalo de confiança do
   seu Gini, a resposta correta é que se trata do universo dos vínculos formais
   declarados, não de uma amostra — o que não significa ausência de erro, apenas
   que o erro é de declaração, não de amostragem.
2. **A unidade é o vínculo.** Uma pessoa com dois empregos formais aparece duas
   vezes. Nunca diga "trabalhadores" quando o número é de vínculos.
3. **Só existe o formal declarado.** Informalidade, desemprego e quem está fora
   da força de trabalho simplesmente não estão na base.

**Pergunta provável:** "Vocês podem dizer que a desigualdade de gênero no Pará é
de X%?"
**Resposta:** Não. Podemos dizer que, entre os vínculos formais declarados em
2025 no Pará, o diferencial mediano é de X%. Sobre o mercado de trabalho paraense
como um todo, a base não permite afirmar.

---

## Passo 1 — De onde vêm os dados

### O que foi feito

`R/00-baixar-dados.sh` baixa do FTP do MTE dois conjuntos de coisas: os
**microdados** do ano-base 2025 (um arquivo `.7z` por região) e os **layouts**
oficiais (`.xls`) que descrevem as variáveis.

```bash
bash R/00-baixar-dados.sh NORTE
```

### Por que

O download é script, não manual, porque a rubrica 8 avalia reprodutibilidade:
qualquer pessoa deve poder refazer o caminho inteiro do zero.

### Três armadilhas que você deve saber explicar

**1. O formato documentado está errado.** A página oficial e o tutorial da
disciplina dizem que o separador é ponto-e-vírgula (`;`). **Não é.** Os arquivos
de 2025 usam **vírgula**, decimal com **ponto** e encoding **Latin-1**.

Como verificar você mesmo:

```bash
# Quantos ';' existem no arquivo? Resposta: zero.
grep -c ';' dados-brutos/raw/RAIS_VINC_PUB_NORTE.COMT

# O arquivo é UTF-8? Não: a decodificação falha.
python3 -c "open('dados-brutos/raw/RAIS_VINC_PUB_NORTE.COMT','rb').read(400).decode('utf-8')"
```

Se você rodar `read.csv2()` (que assume `;` e decimal com vírgula), a base vem
com **uma única coluna** de texto. É o erro mais provável de quem seguir só a
documentação.

**2. O layout publicado está desatualizado.** O mais recente no FTP é de **2020**
e descreve **59 variáveis**. O arquivo de 2025 tem **62 colunas**. Três não têm
descrição oficial: `Distritos SP`, `Ind Vínculo Abandonado`, `Categoria
Trabalhador`. **Não usamos nenhuma delas**, justamente porque não teríamos como
justificar a interpretação.

**3. A ordem das colunas do arquivo não é a do layout.** Nas posições 14 a 16, o
arquivo traz `Faixa Rem Média (SM)` **antes** de `Faixa Hora Contrat`, enquanto o
layout lista em outra ordem. Renomear colunas pela ordem do layout troca
variáveis **sem gerar erro nenhum** — a análise roda e dá resultado errado. Por
isso o vetor `NOMES_62` em `R/01-preparar-rais.R` foi conferido contra o
**cabeçalho real do arquivo**, não contra o layout.

Como verificar:

```bash
head -1 dados-brutos/raw/RAIS_VINC_PUB_NORTE.COMT | tr ',' '\n' | head -20
```

---

## Passo 2 — Leitura e preparação (`R/01-preparar-rais.R`)

### 2.1 Leitura seletiva: por que não lemos as 62 colunas

O arquivo da região Norte tem **1,5 GB** descompactado e **5.645.037** linhas. Ler
as 62 colunas em R base consome vários GB de RAM.

A solução é `colClasses = "NULL"`, que faz o `read.csv` **descartar a coluna na
própria leitura**, sem alocar memória:

```r
col_classes <- ifelse(NOMES_62 %in% VARS_USADAS, "character", "NULL")
rais <- read.csv(ARQUIVO, sep = ",", dec = ".", fileEncoding = "latin1",
                 colClasses = col_classes, ...)
```

Com 15 das 62 colunas: **47 segundos** de leitura e **0,69 GB** em memória.

**Pergunta provável:** "Por que vocês não usaram `data.table` ou `readr`, que são
mais rápidos?"
**Resposta:** A ementa da disciplina tem como objetivo explícito a familiarização
com o **R base**. `colClasses = "NULL"` resolve o problema de memória sem
dependência externa. O custo é tempo de leitura, que é aceitável para uma análise
que roda uma vez.

### 2.2 Tipagem

Tudo é lido como `character` e convertido depois. Isso é deliberado: a conversão
automática do `read.csv` pode transformar códigos com zeros à esquerda em números
e destruir a informação (por exemplo, o município `011234` viraria `11234`).

### 2.3 Dados ausentes — a parte que a rubrica 3 cobra

O layout instrui, textualmente, a considerar como ignorado todo valor `-1` (com
ou sem zeros à esquerda), `{ñ class}` ou `{ñclass}`.

Mas há **sentinelas próprias por campo** que não são óbvias:

| Campo | Código de ausência |
|---|---|
| `municipio`, `municipio_trab` | `999999` |
| `natureza_juridica` | `9999` |
| bairros, `distrito_sp`, `regiao_adm_df` | `999997` |
| `faixa_rem_dez_sm`, `faixa_rem_media_sm` | `99` |

E encontramos **duas sentinelas que não estão no layout**:

- `faixa_etaria == 99`
- `idade == 0`

São **27 registros** na região Norte, e a correlação é **perfeita**: todos os que
têm `faixa_etaria == 99` têm `idade == 0`, e vice-versa. Idade zero é impossível
para um vínculo formal.

Como verificar:

```r
rais <- readRDS("dados/rais_norte_preparada.rds")
table(rais$faixa_etaria, useNA = "ifany")   # aparece o 99
```

São 0,0005% da base — desprezível no agregado, mas bastaria para criar uma
categoria fantasma num gráfico de faixa etária.

**Este é um bom achado para mencionar na sabatina**, porque mostra que vocês
inspecionaram os dados em vez de confiar na documentação.

### 2.4 De onde vem a UF

A RAIS **não tem** uma coluna de UF. Ela tem o código de município de 6 dígitos,
que é o código IBGE **sem o dígito verificador**. Os dois primeiros dígitos
identificam a UF:

```r
rais$uf <- UF_COD[substr(rais$municipio, 1, 2)]
```

Verificação que vale fazer antes da sabatina — a região Norte deve produzir
exatamente 7 UFs e nada mais:

```r
table(rais$uf, useNA = "ifany")
# PA 2297948 | AM 1283550 | TO 664703 | RO 636798 | AC 266903 | AP 262893 | RR 232242
```

Se aparecesse uma UF de outra região, o recorte estaria errado.

### 2.5 Um bug de R base que vocês devem conhecer

No `R/02-analise.R` há um comentário sobre isto, e vale entender porque é uma
pegadinha que aparece em prova e em código real.

Se você cria uma coluna dentro de um laço assim:

```r
gap_nivel <- data.frame(nivel = niveis)
gap_nivel$n[i] <- nrow(s)      # ARMADILHA
```

o operador `$` do R base faz **partial matching**: `"n"` é prefixo de `"nivel"`, e
como `nivel` é o único candidato, a atribuição cai **na coluna `nivel`**, que
vira `character`. Nenhum erro é emitido na hora; o erro aparece muito depois, em
`sum()`.

Aconteceu durante o desenvolvimento deste projeto. A correção foi pré-alocar as
colunas com os tipos certos e usar indexação por `[i, "nome"]`.

---

## Passo 3 — Universo e filtros (`R/02-analise.R`, seção 2)

### O que foi feito

Cinco filtros, com o efeito de cada um contabilizado:

| Passo | Vínculos | Removidos |
|---|---|---|
| Região Norte (bruta) | 5.645.037 | — |
| UF em PA ou AM | 3.581.498 | 2.063.539 |
| Vínculo ativo em 31/12 | 2.487.649 | 1.093.849 |
| Sexo informado | 2.487.649 | 0 |
| Remuneração média > 0 | 2.149.707 | 337.942 |
| Jornada contratual > 0 | 2.148.907 | 800 |

**Base analítica: 2.148.907 vínculos** (38,07% da bruta).

### Por que cada filtro — e este é o ponto que mais rende pergunta

**Vínculo ativo em 31/12** é o filtro mais custoso: remove 1.093.849 vínculos,
31% do subtotal. A justificativa é substantiva, não de conveniência:

A variável `Vl Rem Média Nom` é a **remuneração média do ano**. Um vínculo que
durou três meses tem média calculada sobre os meses trabalhados, mas sua presença
na base junto a vínculos de doze meses mistura duas coisas diferentes: **nível
salarial** e **tempo de exposição ao emprego**. Como a rotatividade não é igual
entre homens e mulheres nem entre setores, isso contaminaria a comparação.

Filtrando por vínculo ativo em 31/12, comparamos uma **foto no mesmo momento**.

**Pergunta provável:** "Vocês descartaram 31% da base. Isso não enviesa?"
**Resposta correta:** Enviesa em relação a qual pergunta? Para a pergunta "quanto
ganha quem está empregado formalmente", o filtro é necessário. Para a pergunta
"como a rotatividade afeta a renda anual de mulheres e homens", o filtro seria
justamente o erro — e essa seria outra pergunta, que a base permite fazer. Nossa
pergunta é a primeira.

**Sexo informado não removeu nenhum registro.** Isso é informação, não acidente:
indica cobertura completa da variável nessas duas UFs. Vale dizer isso em voz
alta, porque mostra que vocês verificaram em vez de supor.

---

## Passo 4 — Os indicadores, um por um

### 4.1 Por que mediana e não média

Este é **o coração do trabalho**. Precisa estar na ponta da língua.

| | Média | Mediana | P90 |
|---|---|---|---|
| PA — Homens | R$ 3.832,28 | R$ 2.425,17 | R$ 7.125,24 |
| PA — Mulheres | R$ 3.954,86 | R$ 2.296,40 | R$ 8.617,92 |

No Pará, a **média feminina é maior** que a masculina, mas a **mediana feminina é
menor**. Não é erro: é uma **cauda superior feminina** mais longa (P90 de
R$ 8.617 contra R$ 7.125) puxando a média sem deslocar o centro da distribuição.

Consequência: um relatório que usasse a média concluiria que **não há desvantagem
feminina no Pará**. As diretrizes proíbem exatamente isso — "evita conclusões
indevidas a partir de médias".

Como verificar você mesmo:

```r
d <- readRDS("dados/base_analitica.rds")
pa <- d[d$uf == "PA", ]
tapply(pa$rem_media_nom, pa$sexo_lab, mean)     # feminina maior
tapply(pa$rem_media_nom, pa$sexo_lab, median)   # feminina menor
```

### 4.2 O diferencial (gap)

Definição: `gap = 1 - (valor das mulheres / valor dos homens)`. Positivo significa
remuneração feminina menor.

Recálculo à mão, PA, mediana: `1 - 2296.40 / 2425.17 = 0.0531` → **5,31%**.

Saiba fazer essa conta ao vivo. É a pergunta mais provável da sabatina.

| UF | Gap mediana | Gap média | Gap mediana/hora |
|---|---|---|---|
| PA | 5,31% | **−3,20%** | 1,29% |
| AM | 4,18% | 8,90% | 1,30% |

### 4.3 Remuneração por hora

```r
rem_hora <- rem_media_nom / (horas_contr * 4.345)
```

`horas_contr` é a jornada **contratual semanal**. O fator 4,345 é 52/12 — média de
semanas por mês.

O gap por hora é ~1,3% nos dois estados, muito menor que o mensal. **Isso importa
interpretar com cuidado.** Não significa "não há problema": significa que a
diferença no valor mensal está associada à **jornada**, não ao valor da hora
contratada. Jornada menor está ligada à divisão sexual do cuidado. O problema se
**desloca**, não desaparece.

### 4.4 Índice de Gini

A fórmula usada:

$$G = \frac{2\sum_{i=1}^{n} i \cdot x_i}{n \sum_{i=1}^{n} x_i} - \frac{n+1}{n}$$

com $x$ **ordenado de forma crescente**. Em R:

```r
gini <- function(x) {
  x <- x[!is.na(x) & x >= 0]
  n <- length(x)
  x <- sort(x)
  2 * sum(seq_len(n) * x) / (n * sum(x)) - (n + 1) / n
}
```

**Por que esta forma e não a área da curva de Lorenz?** São algebricamente
equivalentes. Esta versão é numericamente estável e roda em uma passada depois da
ordenação, o que importa com milhões de observações.

**Como saber se está certo?** Teste em casos que você calcula de cabeça:

```r
gini(c(1, 1, 1, 1))     # 0    -> igualdade perfeita
gini(c(0, 0, 0, 100))   # 0.75 -> para n=4, o máximo é (n-1)/n
```

Faça esses dois testes antes da sabatina. Se alguém questionar sua implementação,
você demonstra que ela está validada.

Resultados:

| Grupo | Gini |
|---|---|
| PA — Homens | 0,4234 |
| PA — Mulheres | 0,4415 |
| AM — Homens | 0,4434 |
| AM — Mulheres | 0,4188 |
| PA total | 0,4319 |
| AM total | 0,4335 |

**Leitura:** a desigualdade interna **se inverte** entre os estados. No PA é maior
entre mulheres; no AM, entre homens. Diferenciais agregados parecidos, estruturas
opostas. É o argumento contra metas nacionais uniformes.

### 4.5 Curva de Lorenz

Eixo x: proporção acumulada de vínculos, do menor salário para o maior.
Eixo y: proporção acumulada da **massa salarial**.

A diagonal é a igualdade perfeita. Quanto mais a curva se afasta dela, maior a
desigualdade. O Gini é o dobro da área entre a diagonal e a curva.

Detalhe de implementação que pode ser questionado: a curva é **reduzida a 500
pontos** para plotagem, mas **o Gini é calculado sobre todas as observações**. A
redução é só visual — plotar 2,1 milhões de coordenadas não acrescenta
informação.

---

## Passo 5 — O achado central: efeito de composição

Esta é a parte que diferencia o trabalho. Entenda bem.

### O problema

O gap agregado é ~5%. Mas dentro de cada nível de escolaridade, ele é de 10% a
16%:

| Escolaridade | Peso | Gap |
|---|---|---|
| Médio completo | 54,79% | 15,53% |
| Superior completo | 25,86% | 12,95% |
| Fundamental completo | 6,40% | 13,74% |
| Mestrado | 0,60% | 24,59% |
| Doutorado | 0,51% | 36,74% |

Como todos os gaps internos são maiores que o agregado, o agregado **não é uma
média** dos internos. Isso parece paradoxal e tem nome: é um caso de **paradoxo de
Simpson** — a direção de uma associação muda quando se condiciona a uma terceira
variável.

### A explicação

As mulheres com vínculo formal em PA e AM são **mais escolarizadas** que os
homens:

| Nível | Homens | Mulheres |
|---|---|---|
| Médio completo | 58,22% | 50,29% |
| **Superior completo** | **18,97%** | **34,93%** |
| Mestrado | 0,49% | 0,75% |
| Doutorado | 0,42% | 0,63% |

Escolaridade mais alta paga mais. Como as mulheres estão concentradas nos níveis
mais bem pagos, essa vantagem de composição **compensa** a desvantagem que elas
sofrem dentro de cada nível — e o agregado sai pequeno.

### A solução: padronização direta

Aritmética simples, e é importante que seja simples, porque vocês precisam
explicá-la:

1. Calcule o gap **dentro** de cada nível de escolaridade.
2. Tire a **média ponderada** desses gaps, usando como peso a participação de cada
   nível no total de vínculos.

```r
gap_padronizado <- sum(gap_nivel$gap * gap_nivel$peso)
```

Isso responde: "qual seria o gap se homens e mulheres tivessem a mesma estrutura
de escolaridade?"

| Indicador | Valor |
|---|---|
| Gap agregado (bruto) | 4,73% |
| Gap **padronizado** | **15,01%** |
| Atribuível à composição | 10,28 p.p. |

**O gap mais que triplica.**

### O que você NÃO pode dizer sobre esse número

Prepare-se para esta pergunta, porque é a mais dura que podem fazer:

> "Então 15% é o efeito da discriminação?"

**Não.** A padronização neutraliza **apenas escolaridade**. Ocupação, setor, porte
do estabelecimento e jornada continuam livres, e todos se distribuem de forma
desigual entre os sexos. Os 15% são o diferencial que **sobra depois de igualar
uma única dimensão** — nada mais.

Para falar de discriminação seria preciso comparar função, responsabilidade e
produtividade equivalentes, que são os critérios da própria Lei 14.611/2023 — e a
RAIS não traz nenhum dos três.

### Cautela com mestrado e doutorado

Os gaps de 24,6% e 36,7% chamam atenção, mas são baseados em 12.896 e 10.954
vínculos, contra 1.177.468 no ensino médio. A diferença entre PA (28,25%) e AM
(53,83%) no doutorado pode refletir **qual instituição emprega** esses
profissionais em cada estado, não um padrão estável. Mencione a cautela **antes**
que alguém aponte.

---

## Passo 6 — Da evidência à recomendação

A cadeia lógica precisa estar clara, porque é a rubrica 7:

1. As propostas prometem **fiscalizar** diferenças salariais de gênero.
2. A fiscalização precisa de um **indicador**.
3. Se o indicador for **agregado** (por UF ou setor), ele mostrará 4% a 5% em PA e
   AM — ou até vantagem feminina, se usar média no Pará.
4. Se for **estratificado**, mostrará 15%.
5. Logo: **a escolha do indicador determina se o problema é visto ou não**.
6. Recomendação: estratificar; reportar mediana; tratar jornada como variável de
   política, não como controle.

Isso também **valida** a arquitetura da Lei de Igualdade Salarial, que opera com
comparações **dentro da empresa** — a decisão metodologicamente correta, segundo
nossa evidência.

E qualifica o número de 21% de Cury: nosso padronizado (15,01%) é da mesma ordem
de grandeza; o bruto (4,73%) não é. Universo e método diferem, então **não são
diretamente comparáveis** — diga isso, não force a comparação.

---

## Passo 7 — Checklist para a noite anterior à sabatina

Sobre o código:

- [ ] Rodar os três scripts do zero, numa pasta limpa, e ver dar certo.
- [ ] Abrir `R/02-analise.R` e explicar em voz alta o que cada bloco faz.
- [ ] Rodar `gini(c(1,1,1,1))` e `gini(c(0,0,0,100))` e conferir 0 e 0,75.
- [ ] Recalcular o gap do PA à mão: `1 - 2296.40/2425.17`.
- [ ] Saber dizer por que `colClasses = "NULL"` é necessário.
- [ ] Saber dizer por que o separador é vírgula e não `;`.

Sobre a interpretação:

- [ ] Explicar por que média e mediana discordam no Pará.
- [ ] Explicar a padronização como média ponderada de gaps internos.
- [ ] Explicar por que o gap por hora é menor, **sem** dizer que o problema
      desapareceu.
- [ ] Recitar a ressalva da RAIS sem hesitar.
- [ ] Dizer o que a análise **não** permite concluir.

Sobre a divisão do grupo:

- [ ] Cada integrante deve conseguir responder sobre **qualquer** parte, não só a
      sua. A rubrica 8 avalia "participação equilibrada".

---

## Passo 8 — O que ainda falta vocês fazerem

Isto **não** está pronto e não pode ser terceirizado:

1. **A declaração de uso de IA**, no fim do relatório. As diretrizes exigem
   indicar com clareza quais ferramentas foram usadas e como. Ela está
   deliberadamente em branco: quem escreve é o grupo, porque é uma declaração
   sobre o processo de vocês.
2. **Nomes, RAs e turma**, no cabeçalho do relatório e da apresentação.
3. **Duas fontes adicionais** para a reconstrução do problema (rubrica 2) — os
   Relatórios de Transparência Salarial do MTE e um estudo do IPEA ou IBGE sobre
   diferencial de rendimentos por sexo são os candidatos naturais.
4. **Validar ou trocar o recorte.** O eixo (igualdade salarial), a proposta-âncora
   (Lula) e a comparação (PA vs AM) são uma **proposta**, não uma decisão de
   vocês. Confiram a regra de exclusividade com a turma: "tema + recorte +
   comparação" tem de ser único por grupo.
5. **Rodar e ler tudo.** Não entreguem nada que vocês não consigam explicar.

---

## Apêndice — Perguntas difíceis e como responder

**"Por que PA e AM, e não duas UFs quaisquer?"**
São os dois maiores mercados formais do Norte (63% dos vínculos da região), com
porte semelhante e estruturas produtivas distintas — AM com o polo industrial de
Manaus, PA com extração mineral e agronegócio. Se o diferencial fosse puramente
composição setorial, esperaríamos vê-lo divergir muito entre os dois. Os
agregados são parecidos, mas as estruturas internas de desigualdade se invertem.

**"O Gini de 0,43 é alto ou baixo?"**
É alto para uma distribuição que **já exclui** a informalidade e o desemprego, que
são as partes mais precárias do mercado. Não compare diretamente com o Gini de
renda domiciliar do país, que tem universo e unidade de análise diferentes.

**"Vocês controlaram por idade e tempo de emprego?"**
Não. A padronização neutraliza apenas escolaridade, e isso é declarado como
limitação. Ampliar para ocupação e jornada é o passo natural seguinte, e a base
permite — mas as diretrizes limitam a dois recortes cruzados no corpo do
relatório, e ultrapassar isso tornaria a análise mais frágil, não mais forte.

**"Por que não fizeram regressão?"**
A disciplina é de análise exploratória descritiva, e as diretrizes pedem medidas
de posição, dispersão e associação, com Lorenz e Gini. Uma regressão sugeriria
identificação causal que o desenho não sustenta — e as próprias diretrizes
advertem contra apresentar associação descritiva como causalidade.

**"A remuneração é nominal. Isso não é problema?"**
Para comparar grupos **dentro do mesmo ano-base**, não: todos os valores estão na
mesma moeda e no mesmo período. Seria problema para comparar 2025 com outros
anos, o que não fazemos.

**"27 registros descartados por idade zero não é arbitrário?"**
Idade zero é impossível para um vínculo formal, e os 27 casos coincidem
exatamente com `faixa_etaria == 99`, que é um código de "não classificado" não
documentado no layout. São 0,0005% da base. A decisão está registrada no apêndice
de transparência, que é o que a rubrica exige.
