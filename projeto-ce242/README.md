# Projeto CE242ABC — Métodos de Análise Econômica II (2S2026)

Análise da RAIS 2025 para o trabalho de avaliação da disciplina
(IE/UNICAMP, Prof.ª Ivette Luna).

**Tema:** igualdade salarial de gênero no emprego formal.
**Recorte:** sexo × UF — Pará vs Amazonas.
**Achado central:** o diferencial agregado é de **4,73%**, mas sobe para
**15,01%** quando se padroniza por escolaridade. Os 10,28 p.p. de diferença são
efeito de composição.

> ⚠️ **Antes de entregar, leia [`GUIA-DE-DEFESA.md`](GUIA-DE-DEFESA.md).** A nota
> final só é atribuída a quem faz a sabatina, que tem 20 a 30 minutos de
> perguntas. O guia explica passo a passo cada decisão e cada número, e lista o
> que ainda falta o grupo fazer.

## Estrutura

```
projeto-ce242/
├── R/
│   ├── 00-baixar-dados.sh       # download dos microdados + layouts do FTP
│   ├── 01-preparar-rais.R       # leitura seletiva, tipagem, rótulos, UF
│   └── 02-analise.R             # filtros, indicadores, 4 figuras
├── relatorio/
│   ├── relatorio-ce242.Rmd      # relatório completo
│   └── apresentacao-ce242.Rmd   # slides para a sabatina (ioslides)
├── figuras/                     # PNGs gerados por 02-analise.R
├── dados-brutos/                # (não versionado) .7z e .COMT do FTP
├── dados/                       # (não versionado) .rds e tabela final
├── dicionario-variaveis.md      # as 62 colunas, códigos e armadilhas
├── GUIA-DE-DEFESA.md            # passo a passo para explicar o trabalho
└── README.md
```

## Como reproduzir

Requisitos: `R` (testado na 4.5.3), `curl`, `7z`. **A análise não usa nenhum
pacote externo** — só R base, conforme o objetivo da ementa. `knitr`, `rmarkdown`
e `pandoc` são necessários apenas para gerar os documentos.

```bash
bash R/00-baixar-dados.sh NORTE   # ~212 MB compactados, 1,5 GB descompactados
Rscript R/01-preparar-rais.R      # ~47 s
Rscript R/02-analise.R            # filtros, indicadores e figuras

# documentos
Rscript -e 'rmarkdown::render("relatorio/relatorio-ce242.Rmd")'
Rscript -e 'rmarkdown::render("relatorio/apresentacao-ce242.Rmd")'
```

Para testar o pipeline rápido, use `bash R/00-baixar-dados.sh NI` — 209 KB.

## Resultados principais

Base analítica: **2.148.907 vínculos** formais ativos em 31/12 no PA e no AM
(38,07% da base bruta da região Norte).

| Grupo | Vínculos | Média | Mediana | P90 | Gini |
|---|---|---|---|---|---|
| PA — Homens | 785.645 | R$ 3.832,28 | R$ 2.425,17 | R$ 7.125,24 | 0,4234 |
| PA — Mulheres | 586.850 | R$ 3.954,86 | R$ 2.296,40 | R$ 8.617,92 | 0,4415 |
| AM — Homens | 434.964 | R$ 4.044,62 | R$ 2.524,38 | R$ 7.602,81 | 0,4434 |
| AM — Mulheres | 341.448 | R$ 3.684,49 | R$ 2.418,76 | R$ 6.798,19 | 0,4188 |

Três resultados que estruturam o relatório:

1. **Média e mediana discordam no Pará.** A média feminina é *maior* que a
   masculina, a mediana é *menor* — uma cauda superior feminina (P90 de
   R$ 8.617 contra R$ 7.125) puxa a média sem deslocar o centro. Um relatório
   baseado em médias concluiria que não há desvantagem feminina no PA.
2. **A desigualdade interna se inverte entre os estados.** Gini maior entre
   mulheres no PA, maior entre homens no AM.
3. **O agregado esconde o diferencial.** Dentro de cada nível de escolaridade o
   gap é de 10% a 16% nos níveis de maior emprego; padronizado, 15,01%.

## Figuras

| Arquivo | Conteúdo |
|---|---|
| `fig1-boxplot-remuneracao.png` | Boxplot da remuneração por UF e sexo, escala log |
| `fig2-lorenz.png` | Curvas de Lorenz por UF e sexo, com Gini |
| `fig3-gap-escolaridade.png` | Diferencial por nível de escolaridade |
| `fig4-composicao-escolaridade.png` | Estrutura de escolaridade por sexo (apêndice) |

## Três armadilhas dos microdados

Detalhadas em [`dicionario-variaveis.md`](dicionario-variaveis.md):

1. **O formato documentado está errado.** A documentação oficial e o tutorial da
   disciplina dizem separador `;`. Os arquivos de 2025 usam **vírgula**, decimal
   com **ponto** e encoding **Latin-1**. `read.csv2()` falha.
2. **O layout publicado é de 2020** e descreve 59 variáveis; o arquivo de 2025
   tem **62 colunas**. Renomear pela ordem do layout troca variáveis em silêncio.
3. **Ler as 62 colunas estoura a memória.** O script lê só as declaradas em
   `VARS_USADAS`, via `colClasses = "NULL"`.

## Ressalva obrigatória

A RAIS cobre **apenas vínculos formais declarados**. Informalidade, desemprego e
pessoas fora da força de trabalho não estão representados. Nada aqui pode ser
generalizado para o mercado de trabalho brasileiro. A unidade de análise é o
**vínculo**, não a pessoa. Os valores são **nominais**.

## Pendências do grupo

- [ ] **Declaração de uso de IA** no fim do relatório — deixada em branco de
      propósito; é uma declaração sobre o processo de vocês.
- [ ] Nomes, RAs e turma no cabeçalho do relatório e da apresentação.
- [ ] Duas fontes adicionais para a rubrica 2.
- [ ] Validar ou trocar o recorte, e conferir a regra de exclusividade
      ("tema + recorte + comparação" único por grupo).
- [ ] Rodar tudo e conseguir explicar — ver `GUIA-DE-DEFESA.md`.

## Calendário

| Etapa | Prazo | Pontos |
|---|---|---|
| 1. Projeto definido | 7/out | 1,0 |
| 2. Plano de análise | 16/out | 2,5 |
| 3. Análise exploratória parcial | 30/out | 2,0 |
| 4. EDA final + Lorenz/Gini + diagnóstico | 13/nov | 3,0 |
| 5. Relatório final + sabatina | 20/nov · última semana de nov | 1,5 |

Os pontos são incrementais: não entregar uma etapa perde aqueles pontos em
definitivo.

## Fontes

- Microdados RAIS/CAGED — MTE:
  [página oficial](https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/acoes-e-programas/programas-projetos-acoes-obras-e-atividades/estatisticas-trabalho/microdados-rais-e-caged)
- Microdados e layouts: `ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/`
