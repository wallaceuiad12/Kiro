# Dicionário de variáveis — RAIS Vínculos 2025

Documentação das 62 colunas dos arquivos `RAIS_VINC_PUB_*.COMT` do ano-base 2025,
conferida **empiricamente contra o cabeçalho real do arquivo**, não apenas contra
o layout publicado.

- **Fonte dos dados:** `ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2025/`
- **Fonte do layout:** `ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/Layouts/vínculos/RAIS_vinculos_layout2020.xls`
- **Arquivo usado na conferência:** `RAIS_VINC_PUB_NI.COMT` e `RAIS_VINC_PUB_NORTE.COMT`
- **Data da verificação:** 22/09/2026

---

## 1. Formato real do arquivo

O formato divulgado na documentação oficial **não corresponde** ao dos arquivos de
2025. As diferenças abaixo foram verificadas diretamente nos arquivos e custam
horas de depuração se ignoradas.

| Característica | O que a documentação diz | O que o arquivo de 2025 realmente é |
|---|---|---|
| Separador de campos | ponto-e-vírgula `;` | **vírgula `,`** |
| Separador decimal | vírgula `,` (implícito) | **ponto `.`** |
| Encoding | UTF-8 (só p/ Novo CAGED) | **Latin-1 / CP1252** |
| Extensão | `.txt` | **`.COMT`** (texto delimitado) |

Verificação do separador: o arquivo não contém **nenhuma** ocorrência de `;`.
Verificação do encoding: a decodificação em UTF-8 falha (byte `0xf3` inválido);
em Latin-1 funciona.

Em R base, portanto:

```r
read.csv(arquivo, sep = ",", dec = ".", fileEncoding = "latin1")
```

## 2. Layout publicado está desatualizado

O layout mais recente publicado no FTP é o de **2020**, que descreve **59
variáveis**. O arquivo de 2025 tem **62 colunas**. As três colunas sem
descrição na tabela de variáveis do layout são:

| Coluna no arquivo | Situação |
|---|---|
| `Distritos SP - Código` (11ª) | Existe a aba `Distrito SP` no layout com os códigos, mas a variável não aparece na tabela de variáveis |
| `Ind Vínculo Abandonado - Código` (61ª) | Não documentada no layout de 2020 |
| `Categoria Trabalhador - Código` (62ª) | Não documentada no layout de 2020 |

**Implicação para o trabalho:** se o grupo usar qualquer uma dessas três, não há
documentação oficial para justificar a interpretação. Recomendo evitá-las ou
tratá-las como limitação declarada no apêndice metodológico.

## 3. Convenção de dados ausentes

O layout instrui, textualmente, que se considere como ignorado todo dado como
`-1` (com ou sem zeros à esquerda), `{ñ class}` ou `{ñclass}`, inclusive quando
aparece como parte do texto.

Além de `-1`, há sentinelas próprias por campo, que **não** são óbvias e que
entram silenciosamente nas estatísticas se não forem tratadas:

| Campo | Código de ausência |
|---|---|
| `municipio`, `municipio_trab` | `999999` |
| `natureza_juridica` | `9999` |
| bairros (SP, RJ, Fortaleza), `distrito_sp`, `regiao_adm_df` | `999997` |
| `faixa_rem_dez_sm`, `faixa_rem_media_sm` | `99` |

### Sentinelas não documentadas encontradas nos dados

Além das acima, a inspeção dos dados de 2025 revelou códigos de ausência que
**não constam no layout**:

| Campo | Código | Evidência |
|---|---|---|
| `faixa_etaria` | `99` | 27 registros na região Norte; o layout registra `{ñ class}` como ignorado, mas não o código `99` |
| `idade` | `0` | Os mesmos 27 registros; idade zero é impossível para um vínculo formal |

A correlação é perfeita: todos os 27 registros com `faixa_etaria == 99` têm
`idade == 0`, e vice-versa. São 0,0005% da base — desprezível no agregado, mas
o suficiente para gerar uma categoria fantasma num gráfico de faixa etária se
não forem tratados.

Idades de 91 a 100 anos aparecem em contagens pequenas e decrescentes
(42 registros com 91 anos, 5 com 100) e **não** foram tratadas como sentinela,
por serem plausíveis.

## 4. As 62 colunas, na ordem do arquivo

| # | Nome no arquivo | Nome no script | Descrição (layout) |
|---|---|---|---|
| 1 | Bairros SP - Código | `bairro_sp` | Bairros do município de São Paulo |
| 2 | Bairros Fortaleza - Código | `bairro_fortaleza` | Bairros do município de Fortaleza |
| 3 | Bairros RJ - Código | `bairro_rj` | Bairros do município do Rio de Janeiro |
| 4 | Causa Afastamento 1 - Código | `causa_afast_1` | Causa do 1º afastamento no ano-base |
| 5 | Causa Afastamento 2 - Código | `causa_afast_2` | Causa do 2º afastamento no ano-base |
| 6 | Causa Afastamento 3 - Código | `causa_afast_3` | Causa do 3º afastamento no ano-base |
| 7 | Motivo Desligamento - Código | `motivo_desligamento` | Causa do desligamento |
| 8 | CBO 2002 Ocupação - Código | `cbo2002` | Classificação Brasileira de Ocupações (2002) |
| 9 | CNAE 2.0 Classe - Código | `cnae20_classe` | Classe de atividade econômica, CNAE 2.0 |
| 10 | CNAE 95 Classe - Código | `cnae95_classe` | Classe de atividade econômica, CNAE 95 |
| 11 | Distritos SP - Código | `distrito_sp` | Distritos de São Paulo — *ver seção 2* |
| 12 | Ind Vínculo Ativo 31/12 - Código | `vinculo_ativo_3112` | Indicador de vínculo ativo em 31/12 |
| 13 | Faixa Etária - Código | `faixa_etaria` | Faixa etária do trabalhador |
| 14 | Faixa Rem Média (SM) - Código | `faixa_rem_media_sm` | Faixa de remuneração média do ano, em SM |
| 15 | Faixa Hora Contrat - Código | `faixa_hora_contrat` | Faixa de horas contratuais |
| 16 | Faixa Rem Dez (SM) - Código | `faixa_rem_dez_sm` | Faixa de remuneração de dezembro, em SM |
| 17 | Faixa Tempo Emprego - Código | `faixa_tempo_emprego` | Faixa de tempo de emprego |
| 18 | Escolaridade Após 2005 - Código | `escolaridade` | Grau de instrução (a partir da RAIS 2008) |
| 19 | Qtd Hora Contr | `horas_contr` | Horas contratuais por semana |
| 20 | Idade | `idade` | Idade do trabalhador |
| 21 | Ind CEI Vinculado - Código | `ind_cei_vinculado` | Indicador de CEI vinculado |
| 22 | Ind Estabelecimento Participante SIMPLES - Código | `ind_simples` | Optante pelo SIMPLES |
| 23 | Mês Admissão - Código | `mes_admissao` | Mês da admissão |
| 24 | Mês Desligamento - Código | `mes_desligamento` | Mês do desligamento |
| 25 | Município Trab - Código | `municipio_trab` | Município onde presta serviço |
| 26 | Município - Código | `municipio` | Município do estabelecimento |
| 27 | Nacionalidade - Código | `nacionalidade` | Nacionalidade |
| 28 | Natureza Jurídica - Código | `natureza_juridica` | Natureza jurídica (CONCLA/2002) |
| 29 | Ind Portador Defic - Código | `ind_portador_defic` | Indicador de pessoa com deficiência |
| 30 | Qtd Dias Afastamento | `qtd_dias_afastamento` | Total de dias de afastamento no ano-base |
| 31 | Raça Cor - Código | `raca_cor` | Raça/cor do trabalhador |
| 32 | Região Adm DF - Código | `regiao_adm_df` | Regiões administrativas do DF |
| 33 | Vl Rem Dezembro Nom | `rem_dezembro_nom` | Remuneração de dezembro, valor nominal (R$) |
| 34 | Vl Rem Dezembro (SM) | `rem_dezembro_sm` | Remuneração de dezembro, em salários mínimos |
| 35 | Vl Rem Média Nom | `rem_media_nom` | Remuneração média do ano, valor nominal (R$) |
| 36 | Vl Rem Média (SM) | `rem_media_sm` | Remuneração média do ano, em salários mínimos |
| 37 | CNAE 2.0 Subclasse - Codigo | `cnae20_subclasse` | Subclasse de atividade econômica, CNAE 2.0 |
| 38 | Sexo - Código | `sexo` | Sexo |
| 39 | Tamanho Estabelecimento - Código | `tamanho_estab` | Porte do estabelecimento (10 categorias) |
| 40 | Tempo Emprego | `tempo_emprego` | Tempo de emprego, em meses |
| 41 | Tipo Admissão Trabalhador - Código | `tipo_admissao` | Tipo de admissão |
| 42 | Tipo Estabelecimento - Código | `tipo_estab_cod` | Tipo de estabelecimento (código) |
| 43 | Tipo Estabelecimento - Nome | `tipo_estab_nome` | Tipo de estabelecimento (nome, ex. `CNO`, `CAEPF`) |
| 44 | Tipo Deficiência - Código | `tipo_deficiencia` | Tipo de deficiência |
| 45 | Tipo Vínculo - Código | `tipo_vinculo` | Tipo de vínculo empregatício |
| 46 | IBGE Subsetor - Código | `ibge_subsetor` | Subsetor IBGE 80 do estabelecimento |
| 47–57 | Vl Rem Janeiro…Novembro SC | `rem_janeiro`…`rem_novembro` | Remuneração mensal nominal (a partir de 2015) |
| 58 | Ano Chegada Brasil | `ano_chegada_brasil` | Ano de chegada ao Brasil (estrangeiros) |
| 59 | Ind Trabalho Intermitente - Código | `ind_trab_intermitente` | Contrato intermitente (a partir de 2017) |
| 60 | Ind Trabalho Parcial - Código | `ind_trab_parcial` | Contrato parcial (a partir de 2017) |
| 61 | Ind Vínculo Abandonado - Código | `ind_vinculo_abandonado` | *Não documentada — ver seção 2* |
| 62 | Categoria Trabalhador - Código | `categoria_trabalhador` | *Não documentada — ver seção 2* |

> Atenção à ordem das colunas 14–16: no arquivo, `Faixa Rem Média (SM)` vem
> **antes** de `Faixa Hora Contrat`, enquanto o layout lista as faixas em outra
> ordem. Renomear por posição seguindo o layout, e não o arquivo, troca as
> variáveis silenciosamente.

## 5. Códigos das categorias

### Sexo
| Código | Categoria |
|---|---|
| 1 | Masculino |
| 2 | Feminino |
| -1 | Ignorado |

### Raça/Cor
| Código | Categoria |
|---|---|
| 1 | Indígena |
| 2 | Branca |
| 4 | Preta |
| 6 | Amarela |
| 8 | Parda |
| 9 | Não identificada |
| -1 | Ignorado |

Note que os códigos **não são sequenciais** (não há 3, 5, 7). Tratar como
numérico contínuo ou assumir sequência produz recodificação errada.

### Escolaridade (grau de instrução, após 2005)
| Código | Categoria |
|---|---|
| 1 | Analfabeto |
| 2 | Até 5º ano incompleto |
| 3 | 5º ano completo |
| 4 | 6º ao 9º ano fundamental |
| 5 | Fundamental completo |
| 6 | Médio incompleto |
| 7 | Médio completo |
| 8 | Superior incompleto |
| 9 | Superior completo |
| 10 | Mestrado |
| 11 | Doutorado |
| -1 | Ignorado |

### Faixa etária
| Código | Faixa |
|---|---|
| 1 | 10 a 14 anos |
| 2 | 15 a 17 anos |
| 3 | 18 a 24 anos |
| 4 | 25 a 29 anos |
| 5 | 30 a 39 anos |
| 6 | 40 a 49 anos |
| 7 | 50 a 64 anos |
| 8 | 65 anos ou mais |

### Tamanho do estabelecimento (vínculos ativos em 31/12)
| Código | Faixa |
|---|---|
| 1 | Zero |
| 2 | Até 4 |
| 3 | 5 a 9 |
| 4 | 10 a 19 |
| 5 | 20 a 49 |
| 6 | 50 a 99 |
| 7 | 100 a 249 |
| 8 | 250 a 499 |
| 9 | 500 a 999 |
| 10 | 1000 ou mais |

### Subsetor IBGE (25 categorias)
| Código | Subsetor |
|---|---|
| 1 | Extrativa mineral |
| 2 | Indústria de produtos minerais não metálicos |
| 3 | Indústria metalúrgica |
| 4 | Indústria mecânica |
| 5 | Indústria do material elétrico e de comunicações |
| 6 | Indústria do material de transporte |
| 7 | Indústria da madeira e do mobiliário |
| 8 | Indústria do papel, papelão, editorial e gráfica |
| 9 | Ind. da borracha, fumo, couros, peles e diversas |
| 10 | Ind. química, farmacêutica, veterinária, perfumaria |
| 11 | Indústria têxtil, do vestuário e artefatos de tecidos |
| 12 | Indústria de calçados |
| 13 | Indústria de produtos alimentícios, bebidas e álcool etílico |
| 14 | Serviços industriais de utilidade pública |
| 15 | Construção civil |
| 16 | Comércio varejista |
| 17 | Comércio atacadista |
| 18 | Instituições de crédito, seguros e capitalização |
| 19 | Com. e adm. de imóveis, valores mobiliários, serv. técnico |
| 20 | Transportes e comunicações |
| 21 | Serv. de alojamento, alimentação, reparação, manutenção |
| 22 | Serviços médicos, odontológicos e veterinários |
| 23 | Ensino |
| 24 | Administração pública direta e autárquica |
| 25 | Agricultura, silvicultura, criação de animais, extrativismo vegetal |
| `{ñ class}` | Ignorado |

### Faixa de remuneração média do ano (em salários mínimos)
| Código | Faixa |
|---|---|
| 00 | Até 0,50 SM |
| 01 | 0,51 a 1,00 SM |
| 02 | 1,01 a 1,50 SM |
| 03 | 1,51 a 2,00 SM |
| 04 | 2,01 a 3,00 SM |
| 05 | 3,01 a 4,00 SM |
| 06 | 4,01 a 5,00 SM |
| 07 | 5,01 a 7,00 SM |
| 08 | 7,01 a 10,00 SM |
| 09 | 10,01 a 15,00 SM |
| 10 | 15,01 a 20,00 SM |
| 11 | Mais de 20,00 SM |

A faixa de **dezembro** usa escala deslocada: `00` = "Não ativo em dezembro",
`01` = até 0,50 SM, e assim por diante até `12` = mais de 20 SM, com `99` =
não classificado. **Não** são intercambiáveis com as faixas do ano.

### Faixa de tempo de emprego
| Código | Faixa |
|---|---|
| 1 | Até 2,9 meses |
| 2 | 3,0 a 5,9 meses |
| 3 | 6,0 a 11,9 meses |
| 4 | 12,0 a 23,9 meses |
| 5 | 24,0 a 35,9 meses |
| 6 | 36,0 a 59,9 meses |
| 7 | 60,0 a 119,9 meses |
| 8 | 120,0 meses ou mais |

### Faixa de horas contratuais
| Código | Faixa |
|---|---|
| 01 | Até 12 horas |
| 02 | 13 a 15 horas |
| 03 | 16 a 20 horas |
| 04 | 21 a 30 horas |
| 05 | 31 a 40 horas |
| 06 | 41 a 44 horas |

### Vínculo ativo em 31/12
| Código | Categoria |
|---|---|
| 0 | Não |
| 1 | Sim |

## 6. Município e UF

O código de município tem 6 dígitos — é o código IBGE **sem o dígito
verificador**. Os dois primeiros dígitos identificam a UF, o que permite derivar
UF e região sem tabela externa:

```r
uf <- UF_COD[substr(municipio, 1, 2)]
```

A aba `municipio` do layout traz os 5.663 municípios no formato
`110001:Ro-Alta Floresta D Oeste`, útil para nomear municípios específicos.

## 7. Verificações feitas nos dados reais

Rodando `R/01-preparar-rais.R` sobre `RAIS_VINC_PUB_NORTE.COMT`:

- **5.645.037 vínculos** lidos, 15 colunas retidas, 46,8 s de leitura, 0,69 GB
  em memória.
- Derivação de UF confere: os 7 estados do Norte e nada mais — PA (2.297.948),
  AM (1.283.550), TO (664.703), RO (636.798), AC (266.903), AP (262.893),
  RR (232.242).
- `rem_dezembro_nom` tem **41,43% de ausentes**, consistente com vínculos não
  ativos em dezembro (1.734.016 de 5.645.037 vínculos não estavam ativos em
  31/12). Usar essa variável sem filtrar por `vinculo_ativo_3112 == 1`
  descarta 41% da base de forma não intencional.
- `rem_media_nom`: mediana R$ 1.985 contra média R$ 3.015, com máximo de
  R$ 216.537. A distribuição é **fortemente assimétrica à direita** — é
  exatamente o caso em que as diretrizes proíbem usar só a média.
- No arquivo `RAIS_VINC_PUB_NI.COMT`, `municipio` é `999999` em 100% dos
  registros: é o arquivo de UF não identificada. Serve para testar o pipeline,
  **não** para análise regional.

## 8. Limitações da fonte (para o apêndice metodológico)

- A RAIS cobre **apenas vínculos formais declarados**. Informalidade,
  desemprego e pessoas fora da força de trabalho não estão representados.
- A unidade de análise é o **vínculo**, não a pessoa: quem tem dois empregos
  formais aparece duas vezes.
- Os valores de remuneração são **nominais**, sem deflacionamento.
- Os microdados públicos são **não identificados**: não há CPF, CNPJ nem
  identificador de pessoa, o que impede acompanhar trajetórias.
- O layout oficial mais recente é de 2020, e três colunas de 2025 não estão
  documentadas.
