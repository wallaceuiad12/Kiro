# ============================================================================
# CE242ABC - Metodos de Analise Economica II - 2S2026
# Script 02: analise exploratoria, indicadores de desigualdade e graficos
#
# Rodar DEPOIS de R/01-preparar-rais.R, com working directory em
# projeto-ce242/ :   Rscript R/02-analise.R
#
# Tudo em R base: nenhum pacote externo. Os graficos usam o dispositivo
# png() e as funcoes boxplot(), plot(), lines(), barplot() do R base.
#
# ---------------------------------------------------------------------------
# ESCOLHAS ANALITICAS - O GRUPO PRECISA VALIDAR OU TROCAR
#
# Eixo programatico : igualdade salarial e combate a discriminacao no
#                     mercado de trabalho.
# Proposta ancora   : Lula (PT) - tornar obrigatoria a execucao dos Planos
#                     de Acao da Lei de Igualdade Salarial em empresas com
#                     desigualdade identificada, com metas progressivas.
#                     Augusto Cury (Avante) cita diferenca media de ~21%
#                     entre mulheres e homens em empresas com 100+
#                     empregados, o que da um numero publico para confrontar
#                     com a evidencia.
# Pergunta          : no emprego formal da regiao Norte em 2025, qual o
#                     diferencial de remuneracao entre mulheres e homens, e
#                     ele se comporta do mesmo modo nos dois maiores estados
#                     da regiao (PA e AM)?
# Recorte           : sexo x UF (PA vs AM). Sao dois recortes cruzados, o
#                     maximo permitido pelas diretrizes.
#
# Se o grupo trocar de eixo, o que muda e principalmente a secao 2 (filtros)
# e os rotulos dos graficos; a mecanica dos indicadores continua a mesma.
# ============================================================================


# ---------------------------------------------------------------------------
# 1. Funcoes de indicadores
# ---------------------------------------------------------------------------

# Indice de Gini a partir da formula da covariancia ordenada.
# Para x ordenado de forma crescente, com n observacoes:
#   G = 2 * sum(i * x_i) / (n * sum(x)) - (n + 1) / n
# Essa forma e algebricamente equivalente a razao entre a area entre a
# diagonal e a curva de Lorenz e a area total abaixo da diagonal.
gini <- function(x) {
  x <- x[!is.na(x) & x >= 0]
  n <- length(x)
  if (n < 2 || sum(x) == 0) return(NA_real_)
  x <- sort(x)
  2 * sum(seq_len(n) * x) / (n * sum(x)) - (n + 1) / n
}

# Pontos da curva de Lorenz: proporcao acumulada de pessoas (p) contra
# proporcao acumulada da massa de remuneracao (L).
# Reduz a um numero fixo de pontos para nao carregar milhoes de coordenadas
# em um grafico que so precisa da forma da curva.
lorenz <- function(x, n_pontos = 500) {
  x <- sort(x[!is.na(x) & x >= 0])
  n <- length(x)
  if (n < 2) return(NULL)
  acum <- cumsum(x) / sum(x)
  idx  <- unique(round(seq(1, n, length.out = min(n_pontos, n))))
  list(p = c(0, idx / n), L = c(0, acum[idx]))
}

# Coeficiente de variacao: dispersao relativa, comparavel entre grupos
# com medias diferentes.
cv <- function(x) sd(x, na.rm = TRUE) / mean(x, na.rm = TRUE)


# ---------------------------------------------------------------------------
# 2. Base analitica: universo e filtros
# ---------------------------------------------------------------------------

rais <- readRDS("dados/rais_norte_preparada.rds")
cat("Base preparada:", format(nrow(rais), big.mark = ","), "vinculos\n\n")

UFS <- c("PA", "AM")

# Registro explicito do efeito de cada filtro. As diretrizes cobram
# justificativa de filtros e tratamento de ausentes, entao contamos quanto
# cada passo remove em vez de apenas encadear condicoes.
passos <- data.frame(
  passo = character(), n = integer(), removidos = integer(),
  stringsAsFactors = FALSE
)
reg <- function(nome, n_atual, n_anterior) {
  passos[nrow(passos) + 1, ] <<- list(nome, n_atual, n_anterior - n_atual)
}

n0 <- nrow(rais);                                    reg("Regiao Norte (base bruta)", n0, n0)

# Filtro 1 - as duas UFs do recorte.
d <- rais[!is.na(rais$uf) & rais$uf %in% UFS, ];      reg("UF em PA ou AM", nrow(d), n0)
n1 <- nrow(d)

# Filtro 2 - vinculos ativos em 31/12. Justificativa: garante uma foto
# comparavel no mesmo momento e evita que vinculos de poucos meses puxem
# a remuneracao media do ano para baixo por tempo de exposicao, nao por
# salario.
d <- d[!is.na(d$vinculo_ativo_3112) & d$vinculo_ativo_3112 == 1, ]
reg("Vinculo ativo em 31/12", nrow(d), n1); n2 <- nrow(d)

# Filtro 3 - sexo informado (necessario para o recorte).
d <- d[!is.na(d$sexo_lab), ];  reg("Sexo informado", nrow(d), n2); n3 <- nrow(d)

# Filtro 4 - remuneracao media positiva. Remuneracao zero nao informa
# salario: sao vinculos sem rendimento declarado no ano.
d <- d[!is.na(d$rem_media_nom) & d$rem_media_nom > 0, ]
reg("Remuneracao media > 0", nrow(d), n3); n4 <- nrow(d)

# Filtro 5 - jornada contratual valida, usada no calculo por hora.
d <- d[!is.na(d$horas_contr) & d$horas_contr > 0, ]
reg("Jornada contratual > 0", nrow(d), n4)

cat("--- Efeito dos filtros ---\n")
passos$pct_da_bruta <- round(100 * passos$n / n0, 2)
print(passos, row.names = FALSE)
cat("\nBase analitica final:", format(nrow(d), big.mark = ","), "vinculos\n\n")

# Remuneracao por hora. A jornada e contratual semanal; 4,345 e a media de
# semanas por mes (52/12). Serve para checar se o diferencial observado e
# apenas composicao de jornada.
d$rem_hora <- d$rem_media_nom / (d$horas_contr * 4.345)

# Grupo do recorte cruzado.
d$grupo <- paste(d$uf, d$sexo_lab, sep = " - ")
d$grupo <- factor(d$grupo,
  levels = c("PA - Masculino", "PA - Feminino",
             "AM - Masculino", "AM - Feminino"))

saveRDS(d, "dados/base_analitica.rds")


# ---------------------------------------------------------------------------
# 3. Tabela descritiva por UF e sexo
# ---------------------------------------------------------------------------
# Medidas de posicao e dispersao. Reportamos mediana e quartis junto com a
# media porque a distribuicao salarial e assimetrica a direita: a media
# isolada nao representa o vinculo tipico.

descreve <- function(x) {
  q <- quantile(x, c(.10, .25, .50, .75, .90), na.rm = TRUE)
  c(n = length(x), media = mean(x, na.rm = TRUE), dp = sd(x, na.rm = TRUE),
    cv = cv(x), p10 = q[[1]], p25 = q[[2]], mediana = q[[3]],
    p75 = q[[4]], p90 = q[[5]])
}

tab_desc <- do.call(rbind, lapply(split(d$rem_media_nom, d$grupo), descreve))
tab_desc <- as.data.frame(tab_desc)

cat("--- Remuneracao media do ano, nominal (R$), por UF e sexo ---\n")
print(round(tab_desc, 2))

tab_hora <- do.call(rbind, lapply(split(d$rem_hora, d$grupo), descreve))
cat("\n--- Remuneracao por hora (R$/h), por UF e sexo ---\n")
print(round(as.data.frame(tab_hora), 2))


# ---------------------------------------------------------------------------
# 4. Diferencial de remuneracao entre mulheres e homens
# ---------------------------------------------------------------------------
# Definicao: gap = 1 - (valor das mulheres / valor dos homens).
# Positivo significa remuneracao feminina menor. Calculamos sobre a mediana
# e sobre a media: a diferenca entre os dois gaps ja informa sobre a cauda
# superior da distribuicao.

gap <- function(dados, var) {
  h <- dados[[var]][dados$sexo_lab == "Masculino"]
  m <- dados[[var]][dados$sexo_lab == "Feminino"]
  c(gap_mediana = 1 - median(m, na.rm = TRUE) / median(h, na.rm = TRUE),
    gap_media   = 1 -   mean(m, na.rm = TRUE) /   mean(h, na.rm = TRUE))
}

tab_gap <- do.call(rbind, lapply(UFS, function(u) {
  sub <- d[d$uf == u, ]
  c(gap(sub, "rem_media_nom"),
    setNames(gap(sub, "rem_hora"), c("gap_mediana_hora", "gap_media_hora")))
}))
rownames(tab_gap) <- UFS

cat("\n--- Diferencial mulher/homem (positivo = mulher recebe menos) ---\n")
print(round(100 * as.data.frame(tab_gap), 2))


# ---------------------------------------------------------------------------
# 5. Gini e Lorenz
# ---------------------------------------------------------------------------

tab_gini <- sapply(split(d$rem_media_nom, d$grupo), gini)
gini_uf  <- sapply(split(d$rem_media_nom, d$uf), gini)

cat("\n--- Indice de Gini da remuneracao ---\n")
print(round(c(tab_gini, `PA (total)` = gini_uf[["PA"]],
              `AM (total)` = gini_uf[["AM"]]), 4))


# ---------------------------------------------------------------------------
# 6. Diferencial por escolaridade
# ---------------------------------------------------------------------------
# Serve para responder a objecao obvia: o diferencial seria apenas reflexo
# de mulheres com menos escolaridade? Comparamos dentro de cada nivel.

esc_ok <- c("Fundamental completo", "Medio completo",
            "Superior completo", "Mestrado", "Doutorado")
d_esc <- d[d$escolaridade_lab %in% esc_ok, ]
d_esc$escolaridade_lab <- droplevels(d_esc$escolaridade_lab)

tab_esc <- do.call(rbind, lapply(
  split(d_esc, list(d_esc$escolaridade_lab, d_esc$uf), drop = TRUE),
  function(s) data.frame(
    escolaridade = as.character(s$escolaridade_lab[1]),
    uf           = s$uf[1],
    n            = nrow(s),
    n_h          = sum(s$sexo_lab == "Masculino"),
    n_m          = sum(s$sexo_lab == "Feminino"),
    med_h        = median(s$rem_media_nom[s$sexo_lab == "Masculino"], na.rm = TRUE),
    med_m        = median(s$rem_media_nom[s$sexo_lab == "Feminino"],  na.rm = TRUE),
    stringsAsFactors = FALSE)))
tab_esc$gap <- 1 - tab_esc$med_m / tab_esc$med_h
tab_esc <- tab_esc[order(tab_esc$uf, match(tab_esc$escolaridade, esc_ok)), ]

cat("\n--- Diferencial por escolaridade (mediana) ---\n")
print(transform(tab_esc, gap = round(100 * gap, 2)), row.names = FALSE)


# ---------------------------------------------------------------------------
# 6b. Composicao: por que o gap agregado e menor que os gaps internos
# ---------------------------------------------------------------------------
# O gap agregado saiu pequeno (e negativo na media em PA), mas dentro de cada
# nivel de escolaridade ele e substancial. Isso caracteriza um efeito de
# composicao: as mulheres com vinculo formal no Norte sao mais escolarizadas,
# e escolaridade mais alta paga mais, o que comprime o diferencial agregado.
#
# Para mostrar isso usamos padronizacao direta, que e aritmetica simples:
# calculamos o gap dentro de cada nivel e depois tiramos uma media
# ponderada desses gaps, usando como peso a distribuicao de escolaridade do
# total de vinculos. O resultado responde a pergunta "qual seria o gap se
# homens e mulheres tivessem a mesma estrutura de escolaridade?".

# Distribuicao de escolaridade por sexo (todos os niveis, nao so os 5 do grafico)
comp <- table(d$escolaridade_lab, d$sexo_lab)
comp_pct <- prop.table(comp, margin = 2)
cat("\n--- Distribuicao de escolaridade por sexo (% dentro do sexo) ---\n")
print(round(100 * comp_pct, 2))

# Gap dentro de cada nivel, com todos os niveis
niveis <- levels(droplevels(d$escolaridade_lab))

# Colunas pre-alocadas de proposito. Se criassemos as colunas dentro do laco
# com gap_nivel$n[i] <- ... , o operador $ do R base faria PARTIAL MATCHING:
# "n" e prefixo de "nivel" e seria o unico candidato, entao a atribuicao
# cairia na coluna "nivel" e a transformaria em character. E uma pegadinha
# silenciosa do R base; pre-alocar com os tipos certos evita o problema.
gap_nivel <- data.frame(
  escolaridade = niveis,
  n            = NA_integer_,
  med_h        = NA_real_,
  med_m        = NA_real_,
  stringsAsFactors = FALSE
)
for (i in seq_along(niveis)) {
  s <- d[d$escolaridade_lab == niveis[i], ]
  gap_nivel[i, "n"]     <- nrow(s)
  gap_nivel[i, "med_h"] <- median(s$rem_media_nom[s$sexo_lab == "Masculino"], na.rm = TRUE)
  gap_nivel[i, "med_m"] <- median(s$rem_media_nom[s$sexo_lab == "Feminino"],  na.rm = TRUE)
}
gap_nivel$gap  <- 1 - gap_nivel$med_m / gap_nivel$med_h
gap_nivel$peso <- gap_nivel$n / sum(gap_nivel$n)

gap_bruto        <- 1 - median(d$rem_media_nom[d$sexo_lab == "Feminino"], na.rm = TRUE) /
                         median(d$rem_media_nom[d$sexo_lab == "Masculino"], na.rm = TRUE)
gap_padronizado  <- sum(gap_nivel$gap * gap_nivel$peso, na.rm = TRUE)

cat("\n--- Gap por nivel de escolaridade e padronizacao ---\n")
print(transform(gap_nivel, gap = round(100 * gap, 2),
                peso = round(100 * peso, 2)), row.names = FALSE)
cat(sprintf("\nGap agregado (bruto, mediana)        : %6.2f%%\n", 100 * gap_bruto))
cat(sprintf("Gap padronizado por escolaridade     : %6.2f%%\n", 100 * gap_padronizado))
cat(sprintf("Diferenca atribuivel a composicao    : %6.2f p.p.\n",
            100 * (gap_padronizado - gap_bruto)))

# Participacao feminina por nivel de escolaridade, para contextualizar.
part_fem <- with(d_esc, tapply(sexo_lab == "Feminino", escolaridade_lab, mean))
cat("\n--- Participacao feminina nos vinculos, por escolaridade (%) ---\n")
print(round(100 * part_fem, 2))


# ---------------------------------------------------------------------------
# 7. Graficos
# ---------------------------------------------------------------------------

dir.create("figuras", showWarnings = FALSE)
COR_H <- "#3C6E9F"   # homens
COR_M <- "#C4622D"   # mulheres
CORES <- c(COR_H, COR_M, COR_H, COR_M)

# --- Figura 1: boxplot da remuneracao por UF e sexo -----------------------
# Escala logaritmica no eixo y: a distribuicao salarial e assimetrica e vai
# de ~R$ 1.000 a mais de R$ 200.000, entao em escala linear as caixas
# ficariam achatadas contra o eixo. outline = FALSE omite os pontos
# extremos individuais, que em 2,9 milhoes de vinculos formariam uma mancha
# solida sem informacao visual.
# O eixo y e truncado entre os percentis 1 e 99 da remuneracao. Sem isso, os
# bigodes descem ate perto de R$ 1 (ha vinculos com remuneracao declarada
# irrisoria) e as caixas ficam comprimidas no topo do grafico, ilegiveis.
# O truncamento afeta apenas a visualizacao: nenhuma estatistica reportada no
# relatorio foi calculada sobre a base truncada.
lim <- quantile(d$rem_media_nom, c(0.01, 0.99), na.rm = TRUE)
medianas <- tapply(d$rem_media_nom, d$grupo, median, na.rm = TRUE)

png("figuras/fig1-boxplot-remuneracao.png",
    width = 1800, height = 1200, res = 200)
par(mar = c(6, 5.5, 4.5, 1))
boxplot(rem_media_nom ~ grupo, data = d,
        log = "y", outline = FALSE, col = CORES,
        ylim = lim,
        xlab = "", ylab = "Remuneracao media do ano (R$, escala log)",
        main = "Distribuicao da remuneracao no emprego formal\nPara e Amazonas, por sexo - RAIS 2025",
        las = 1, cex.axis = 0.85)
# Rotulo da mediana sobre cada caixa: e a medida de posicao que o relatorio
# usa para comparar os grupos, entao fica explicita no grafico.
text(seq_along(medianas), medianas, labels = sprintf("%.0f", medianas),
     pos = 3, offset = 0.45, cex = 0.72, font = 2)
legend("topright", legend = c("Homens", "Mulheres"),
       fill = c(COR_H, COR_M), bty = "n", cex = 0.85)
mtext(sprintf("Eixo y truncado nos percentis 1 e 99 (R$ %.0f a R$ %.0f) e em escala log. Valores sobre as caixas: mediana.",
              lim[1], lim[2]),
      side = 1, line = 3.2, cex = 0.62, adj = 0)
mtext("Fonte: RAIS 2025 (MTE). Vinculos formais ativos em 31/12. Valores nominais.",
      side = 1, line = 4.2, cex = 0.62, adj = 0)
dev.off()

# --- Figura 2: curvas de Lorenz -------------------------------------------
png("figuras/fig2-lorenz.png", width = 1800, height = 1000, res = 200)
# oma reserva espaco na margem externa inferior para a nota de fonte, que
# antes colidia com o rotulo do eixo x.
par(mfrow = c(1, 2), mar = c(4.5, 4.5, 3.5, 1), oma = c(2, 0, 0, 0))
for (u in UFS) {
  plot(c(0, 1), c(0, 1), type = "n", asp = 1,
       xlab = "Proporcao acumulada de vinculos",
       ylab = "Proporcao acumulada da massa salarial",
       main = paste0(u, "  (Gini total = ",
                     formatC(gini_uf[[u]], format = "f", digits = 3), ")"),
       cex.main = 1)
  abline(0, 1, lty = 3, col = "grey40")            # igualdade perfeita
  for (s in c("Masculino", "Feminino")) {
    lz <- lorenz(d$rem_media_nom[d$uf == u & d$sexo_lab == s])
    lines(lz$p, lz$L, lwd = 2.2,
          col = if (s == "Masculino") COR_H else COR_M)
  }
  g_h <- gini(d$rem_media_nom[d$uf == u & d$sexo_lab == "Masculino"])
  g_m <- gini(d$rem_media_nom[d$uf == u & d$sexo_lab == "Feminino"])
  legend("topleft", bty = "n", cex = 0.8,
         legend = c(sprintf("Homens (Gini %.3f)", g_h),
                    sprintf("Mulheres (Gini %.3f)", g_m),
                    "Igualdade perfeita"),
         col = c(COR_H, COR_M, "grey40"),
         lwd = c(2.2, 2.2, 1), lty = c(1, 1, 3))
}
mtext("Fonte: RAIS 2025 (MTE). Vinculos formais ativos em 31/12. Quanto mais distante da diagonal, maior a desigualdade.",
      side = 1, line = 0.6, outer = TRUE, cex = 0.62)
dev.off()

# --- Figura 3: diferencial por escolaridade -------------------------------
png("figuras/fig3-gap-escolaridade.png",
    width = 1800, height = 1150, res = 200)
par(mar = c(8.5, 5, 4.5, 1))

# A matriz e montada por INDEXACAO EXPLICITA, nao pela ordem das linhas de
# tab_esc. Montar com matrix(..., byrow = TRUE) daria um grafico errado:
# tab_esc esta ordenada por UF em ordem alfabetica (AM antes de PA), mas
# UFS = c("PA", "AM"), entao as series apareceriam com a legenda trocada.
m <- sapply(esc_ok, function(e)
       sapply(UFS, function(u)
         100 * tab_esc$gap[tab_esc$uf == u & tab_esc$escolaridade == e]))
rownames(m) <- UFS
# Conferencia: os rotulos curtos usados no eixo preservam a ordem de esc_ok.
colnames(m) <- c("Fundamental\ncompleto", "Medio\ncompleto",
                 "Superior\ncompleto", "Mestrado", "Doutorado")

bp <- barplot(m, beside = TRUE, col = c("#3C6E9F", "#8FB4D4"),
              ylab = "Diferencial mulher/homem na mediana (%)",
              main = "O diferencial de remuneracao por nivel de escolaridade\nPara e Amazonas - RAIS 2025",
              las = 1, cex.names = 0.72,
              ylim = c(0, max(m) * 1.18))
abline(h = 0, col = "grey30")
# m ja esta em pontos percentuais: multiplicar de novo por 100 jogaria os
# rotulos fora da area do grafico.
text(bp, as.vector(m) + max(m) * 0.035,
     labels = sprintf("%.1f", as.vector(m)), cex = 0.62)
legend("topleft", legend = UFS, fill = c("#3C6E9F", "#8FB4D4"),
       bty = "n", cex = 0.85)
mtext("Valores positivos: mediana feminina abaixo da masculina. Fonte: RAIS 2025 (MTE), vinculos ativos em 31/12.",
      side = 1, line = 5.2, cex = 0.62, adj = 0)
mtext("Mestrado e doutorado tem poucos vinculos (5 a 8 mil por UF): ler com cautela.",
      side = 1, line = 6.2, cex = 0.62, adj = 0)
dev.off()

# --- Figura 4 (apendice): composicao por escolaridade ---------------------
# Mostra visualmente o efeito de composicao que explica o gap agregado baixo.
png("figuras/fig4-composicao-escolaridade.png",
    width = 1800, height = 1100, res = 200)
par(mar = c(9, 5, 4, 1))
mcomp <- t(100 * comp_pct)
# ylim explicito: sem isso a barra de "Medio completo" (58,2% dos vinculos
# masculinos) e cortada no topo do grafico.
bp2 <- barplot(mcomp, beside = TRUE, col = c(COR_H, COR_M),
               ylab = "% dos vinculos do proprio sexo",
               main = "Estrutura de escolaridade dos vinculos formais, por sexo\nPara e Amazonas - RAIS 2025",
               las = 2, cex.names = 0.7,
               ylim = c(0, max(mcomp) * 1.12))
legend("top", legend = c("Homens", "Mulheres"),
       fill = c(COR_H, COR_M), bty = "n", cex = 0.85, horiz = TRUE)
mtext("Fonte: RAIS 2025 (MTE). Vinculos formais ativos em 31/12. As mulheres concentram 34,9% dos vinculos no superior completo, contra 19,0% dos homens.",
      side = 1, line = 7.8, cex = 0.58, adj = 0)
dev.off()

cat("\nFiguras gravadas em figuras/\n")


# ---------------------------------------------------------------------------
# 8. Exportacao da tabela final
# ---------------------------------------------------------------------------

tab_final <- data.frame(
  uf       = sub(" -.*", "", rownames(tab_desc)),
  sexo     = sub(".*- ", "", rownames(tab_desc)),
  vinculos = tab_desc$n,
  media    = round(tab_desc$media, 2),
  mediana  = round(tab_desc$mediana, 2),
  p10      = round(tab_desc$p10, 2),
  p90      = round(tab_desc$p90, 2),
  cv       = round(tab_desc$cv, 3),
  gini     = round(as.numeric(tab_gini), 4),
  stringsAsFactors = FALSE
)
write.csv(tab_final, "dados/tabela-final.csv", row.names = FALSE)
cat("Tabela final em dados/tabela-final.csv\n")
print(tab_final, row.names = FALSE)

saveRDS(list(tab_desc = tab_desc, tab_hora = tab_hora, tab_gap = tab_gap,
             tab_gini = tab_gini, gini_uf = gini_uf, tab_esc = tab_esc,
             part_fem = part_fem, passos = passos, n_final = nrow(d),
             comp_pct = comp_pct, gap_nivel = gap_nivel,
             gap_bruto = gap_bruto, gap_padronizado = gap_padronizado),
        "dados/resultados.rds")
cat("Resultados em dados/resultados.rds\n")
