# ============================================================================
# CE242ABC - Metodos de Analise Economica II - 2S2026
# Script 01: leitura e preparacao dos microdados da RAIS (vinculos), ano 2025
#
# Fonte : ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/2025/
# Layout: ftp://ftp.mtps.gov.br/pdet/microdados/RAIS/Layouts/vinculos/
#
# Escrito em R base (sem pacotes externos), conforme o objetivo da disciplina
# de familiarizacao com a plataforma do R base.
#
# ---------------------------------------------------------------------------
# ATENCAO 1 - o formato real dos arquivos de 2025 NAO corresponde a
# documentacao oficial. Verificado empiricamente nos arquivos de 2025:
#   - separador de campos : VIRGULA  (","), e nao ponto-e-virgula (";")
#   - separador decimal   : PONTO    (".")
#   - encoding            : Latin-1 / CP1252, e nao UTF-8
#   - extensao do arquivo : .COMT (texto delimitado, apesar da extensao)
#
# ATENCAO 2 - tamanho. Os arquivos por regiao sao grandes quando
# descompactados (a regiao Norte, a menor, tem 1,5 GB e 5,6 milhoes de
# vinculos; Sao Paulo e varias vezes maior). Ler todas as 62 colunas em
# R base consome muitos GB de RAM. Por isso este script le APENAS as
# colunas declaradas em VARS_USADAS, descartando as demais na propria
# leitura (colClasses = "NULL"). Declare em VARS_USADAS so o que a
# analise do grupo realmente usa.
# ============================================================================


# ---------------------------------------------------------------------------
# 1. Parametros
# ---------------------------------------------------------------------------
# Caminhos relativos a raiz do projeto: rodar com working directory em
# projeto-ce242/, por exemplo  Rscript R/01-preparar-rais.R

ARQUIVO <- "dados-brutos/raw/RAIS_VINC_PUB_NORTE.COMT"
SAIDA   <- "dados/rais_norte_preparada.rds"

# Colunas que a analise vai usar. Ajustar conforme o recorte do grupo.
VARS_USADAS <- c(
  "municipio", "ibge_subsetor", "cnae20_classe",
  "sexo", "raca_cor", "escolaridade", "idade", "faixa_etaria",
  "horas_contr", "tempo_emprego", "tipo_vinculo",
  "rem_media_nom", "rem_dezembro_nom", "tamanho_estab",
  "vinculo_ativo_3112"
)

# Sentinelas de "ignorado" documentadas no layout oficial. O layout instrui:
# 'ao encontrar dados como "-1", com ou sem zeros a esquerda, "{n class}" ou
# "{nclass}", ou parte do texto, considerar como ignorado'.
NA_STRINGS <- c("", "-1", "{ñ class}", "{ñclass}", "{n class}", "{nclass}")

# Nomes das 62 colunas, na ordem exata do cabecalho do arquivo de 2025.
# Conferido contra o cabecalho real; ver dicionario-variaveis.md.
NOMES_62 <- c(
  "bairro_sp", "bairro_fortaleza", "bairro_rj",
  "causa_afast_1", "causa_afast_2", "causa_afast_3",
  "motivo_desligamento", "cbo2002", "cnae20_classe", "cnae95_classe",
  "distrito_sp", "vinculo_ativo_3112", "faixa_etaria",
  "faixa_rem_media_sm", "faixa_hora_contrat", "faixa_rem_dez_sm",
  "faixa_tempo_emprego", "escolaridade", "horas_contr", "idade",
  "ind_cei_vinculado", "ind_simples", "mes_admissao", "mes_desligamento",
  "municipio_trab", "municipio", "nacionalidade", "natureza_juridica",
  "ind_portador_defic", "qtd_dias_afastamento", "raca_cor", "regiao_adm_df",
  "rem_dezembro_nom", "rem_dezembro_sm", "rem_media_nom", "rem_media_sm",
  "cnae20_subclasse", "sexo", "tamanho_estab", "tempo_emprego",
  "tipo_admissao", "tipo_estab_cod", "tipo_estab_nome", "tipo_deficiencia",
  "tipo_vinculo", "ibge_subsetor",
  "rem_janeiro", "rem_fevereiro", "rem_marco", "rem_abril", "rem_maio",
  "rem_junho", "rem_julho", "rem_agosto", "rem_setembro", "rem_outubro",
  "rem_novembro",
  "ano_chegada_brasil", "ind_trab_intermitente", "ind_trab_parcial",
  "ind_vinculo_abandonado", "categoria_trabalhador"
)

desconhecidas <- setdiff(VARS_USADAS, NOMES_62)
if (length(desconhecidas) > 0) {
  stop("VARS_USADAS contem nomes inexistentes: ",
       paste(desconhecidas, collapse = ", "))
}


# ---------------------------------------------------------------------------
# 2. Leitura seletiva
# ---------------------------------------------------------------------------
# colClasses recebe um valor por coluna do ARQUIVO, na ordem do arquivo.
# "NULL" faz o read.csv descartar a coluna sem alocar memoria para ela.

col_classes <- ifelse(NOMES_62 %in% VARS_USADAS, "character", "NULL")

cat("Lendo", ARQUIVO, "\n")
cat("Colunas mantidas:", sum(col_classes == "character"), "de 62\n")

t0 <- Sys.time()
rais <- read.csv(
  ARQUIVO,
  sep          = ",",        # verificado: virgula, nao ponto-e-virgula
  dec          = ".",        # verificado: ponto decimal
  fileEncoding = "latin1",   # verificado: Latin-1, nao UTF-8
  na.strings   = NA_STRINGS,
  check.names  = FALSE,
  strip.white  = TRUE,
  colClasses   = col_classes,
  quote        = "\""
)
cat("Tempo de leitura:",
    round(as.numeric(difftime(Sys.time(), t0, units = "secs")), 1), "s\n")

# Renomeia por posicao, usando apenas os nomes das colunas mantidas.
names(rais) <- NOMES_62[NOMES_62 %in% VARS_USADAS]

cat("Linhas :", format(nrow(rais), big.mark = ",", scientific = FALSE), "\n")
cat("Colunas:", ncol(rais), "\n")

tem <- function(v) v %in% names(rais)


# ---------------------------------------------------------------------------
# 3. Tipagem
# ---------------------------------------------------------------------------

num_vars <- c(
  "horas_contr", "idade", "qtd_dias_afastamento", "tempo_emprego",
  "rem_dezembro_nom", "rem_dezembro_sm", "rem_media_nom", "rem_media_sm",
  "rem_janeiro", "rem_fevereiro", "rem_marco", "rem_abril", "rem_maio",
  "rem_junho", "rem_julho", "rem_agosto", "rem_setembro", "rem_outubro",
  "rem_novembro", "ano_chegada_brasil"
)
for (v in intersect(num_vars, names(rais))) rais[[v]] <- as.numeric(rais[[v]])

int_vars <- c(
  "sexo", "raca_cor", "escolaridade", "tamanho_estab", "ibge_subsetor",
  "faixa_etaria", "faixa_rem_media_sm", "faixa_rem_dez_sm",
  "faixa_hora_contrat", "faixa_tempo_emprego", "tipo_vinculo",
  "vinculo_ativo_3112", "motivo_desligamento", "mes_admissao",
  "mes_desligamento", "ind_simples", "ind_portador_defic"
)
for (v in intersect(int_vars, names(rais))) rais[[v]] <- as.integer(rais[[v]])


# ---------------------------------------------------------------------------
# 4. Sentinelas de "ignorado" que NAO sao "-1"
# ---------------------------------------------------------------------------
# Alguns campos usam codigos proprios para ausencia. Tratamos explicitamente
# para que nao entrem nas estatisticas como categoria valida.

sentinela <- function(v, cod) {
  if (tem(v)) rais[[v]][rais[[v]] == cod] <<- NA
}
sentinela("municipio", "999999")
sentinela("municipio_trab", "999999")
sentinela("natureza_juridica", "9999")
sentinela("bairro_sp", "999997")
sentinela("bairro_rj", "999997")
sentinela("bairro_fortaleza", "999997")
sentinela("distrito_sp", "999997")
sentinela("regiao_adm_df", "999997")
sentinela("faixa_rem_dez_sm", 99L)
sentinela("faixa_rem_media_sm", 99L)

# Sentinelas NAO documentadas no layout, encontradas nos dados de 2025.
# Na regiao Norte, 27 registros tem faixa_etaria == 99 e idade == 0
# simultaneamente (correlacao perfeita). O layout registra "{n class}" como
# ignorado para faixa etaria, mas nao menciona o codigo 99; e idade 0 e
# impossivel para um vinculo formal. Tratamos ambos como ausentes.
sentinela("faixa_etaria", 99L)
sentinela("idade", 0)


# ---------------------------------------------------------------------------
# 5. Rotulos das categorias (conforme layout oficial)
# ---------------------------------------------------------------------------

if (tem("sexo")) {
  rais$sexo_lab <- factor(rais$sexo, levels = c(1, 2),
    labels = c("Masculino", "Feminino"))
}

if (tem("raca_cor")) {
  rais$raca_cor_lab <- factor(rais$raca_cor,
    levels = c(1, 2, 4, 6, 8, 9),
    labels = c("Indigena", "Branca", "Preta", "Amarela", "Parda",
               "Nao identificada"))
}

if (tem("escolaridade")) {
  rais$escolaridade_lab <- factor(rais$escolaridade, levels = 1:11,
    labels = c("Analfabeto", "Ate 5o ano incompleto", "5o ano completo",
               "6o ao 9o ano fundamental", "Fundamental completo",
               "Medio incompleto", "Medio completo", "Superior incompleto",
               "Superior completo", "Mestrado", "Doutorado"),
    ordered = TRUE)
}

if (tem("tamanho_estab")) {
  rais$tamanho_estab_lab <- factor(rais$tamanho_estab, levels = 1:10,
    labels = c("Zero", "Ate 4", "5 a 9", "10 a 19", "20 a 49", "50 a 99",
               "100 a 249", "250 a 499", "500 a 999", "1000 ou mais"),
    ordered = TRUE)
}

if (tem("faixa_etaria")) {
  rais$faixa_etaria_lab <- factor(rais$faixa_etaria, levels = 1:8,
    labels = c("10 a 14", "15 a 17", "18 a 24", "25 a 29", "30 a 39",
               "40 a 49", "50 a 64", "65 ou mais"),
    ordered = TRUE)
}

if (tem("ibge_subsetor")) {
  rais$ibge_subsetor_lab <- factor(rais$ibge_subsetor, levels = 1:25,
    labels = c(
      "Extrativa mineral",
      "Prod. minerais nao metalicos",
      "Industria metalurgica",
      "Industria mecanica",
      "Material eletrico e comunicacoes",
      "Material de transporte",
      "Madeira e mobiliario",
      "Papel, papelao, editorial e grafica",
      "Borracha, fumo, couros e diversas",
      "Quimica, farmaceutica, perfumaria",
      "Textil, vestuario e artefatos",
      "Calcados",
      "Alimentos, bebidas e alcool etilico",
      "Servicos ind. de utilidade publica",
      "Construcao civil",
      "Comercio varejista",
      "Comercio atacadista",
      "Credito, seguros e capitalizacao",
      "Imoveis e servicos tecnicos",
      "Transportes e comunicacoes",
      "Alojamento e alimentacao",
      "Servicos medicos e odontologicos",
      "Ensino",
      "Administracao publica",
      "Agricultura e extrativismo vegetal"))
}

if (tem("vinculo_ativo_3112")) {
  rais$vinculo_ativo_lab <- factor(rais$vinculo_ativo_3112,
    levels = c(0, 1), labels = c("Nao", "Sim"))
}


# ---------------------------------------------------------------------------
# 6. UF e regiao a partir do codigo de municipio
# ---------------------------------------------------------------------------
# O codigo de municipio tem 6 digitos (IBGE sem digito verificador).
# Os dois primeiros digitos identificam a UF.

UF_COD <- c(
  "11" = "RO", "12" = "AC", "13" = "AM", "14" = "RR", "15" = "PA",
  "16" = "AP", "17" = "TO", "21" = "MA", "22" = "PI", "23" = "CE",
  "24" = "RN", "25" = "PB", "26" = "PE", "27" = "AL", "28" = "SE",
  "29" = "BA", "31" = "MG", "32" = "ES", "33" = "RJ", "35" = "SP",
  "41" = "PR", "42" = "SC", "43" = "RS", "50" = "MS", "51" = "MT",
  "52" = "GO", "53" = "DF"
)

REGIAO_DE <- c(
  RO = "Norte", AC = "Norte", AM = "Norte", RR = "Norte", PA = "Norte",
  AP = "Norte", TO = "Norte",
  MA = "Nordeste", PI = "Nordeste", CE = "Nordeste", RN = "Nordeste",
  PB = "Nordeste", PE = "Nordeste", AL = "Nordeste", SE = "Nordeste",
  BA = "Nordeste",
  MG = "Sudeste", ES = "Sudeste", RJ = "Sudeste", SP = "Sudeste",
  PR = "Sul", SC = "Sul", RS = "Sul",
  MS = "Centro-Oeste", MT = "Centro-Oeste", GO = "Centro-Oeste",
  DF = "Centro-Oeste"
)

if (tem("municipio")) {
  rais$uf     <- unname(UF_COD[substr(rais$municipio, 1, 2)])
  rais$regiao <- unname(REGIAO_DE[rais$uf])
}


# ---------------------------------------------------------------------------
# 7. Diagnostico de qualidade (alimenta o apendice de transparencia)
# ---------------------------------------------------------------------------

cat("\n--- Ausentes por variavel ---\n")
algum_na <- FALSE
for (v in names(rais)) {
  n_na <- sum(is.na(rais[[v]]))
  if (n_na > 0) {
    algum_na <- TRUE
    cat(sprintf("  %-22s %11s  (%.3f%%)\n", v,
                format(n_na, big.mark = ",", scientific = FALSE),
                100 * n_na / nrow(rais)))
  }
}
if (!algum_na) cat("  nenhuma variavel com ausentes\n")
cat("  (variaveis nao listadas nao tem ausentes)\n")

if (tem("uf")) {
  cat("\n--- Vinculos por UF ---\n")
  print(sort(table(rais$uf, useNA = "ifany"), decreasing = TRUE))
}

if (tem("vinculo_ativo_lab")) {
  cat("\n--- Vinculo ativo em 31/12 ---\n")
  print(table(rais$vinculo_ativo_lab, useNA = "ifany"))
}

if (tem("rem_media_nom")) {
  cat("\n--- Remuneracao media nominal do ano (R$) ---\n")
  print(summary(rais$rem_media_nom))
}


# ---------------------------------------------------------------------------
# 8. Gravacao
# ---------------------------------------------------------------------------

dir.create("dados", showWarnings = FALSE, recursive = TRUE)
saveRDS(rais, SAIDA)
cat("\nBase gravada em", SAIDA, "\n")
cat("Memoria do objeto:",
    round(as.numeric(object.size(rais)) / 1024^3, 2), "GB\n")
