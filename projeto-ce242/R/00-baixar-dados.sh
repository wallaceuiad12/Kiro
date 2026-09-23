#!/usr/bin/env bash
# ============================================================================
# CE242ABC - 2S2026
# Script 00: download dos microdados da RAIS 2025 e dos layouts oficiais
#
# Uso:
#   bash R/00-baixar-dados.sh NORTE
#   bash R/00-baixar-dados.sh SP
#   bash R/00-baixar-dados.sh NI          # 209 KB, para testar o pipeline
#
# Regioes validas: NI, NORTE, NORDESTE, CENTRO_OESTE, SUL, SP, MG_ES_RJ
#
# Rodar a partir da raiz do projeto (projeto-ce242/).
#
# Requisitos: curl e 7z (p7zip).
# ============================================================================

set -euo pipefail

FTP="ftp://ftp.mtps.gov.br/pdet/microdados/RAIS"
ANO="2025"
DEST="dados-brutos/raw"
LAYOUTS="dados-brutos/layouts"

REGIAO="${1:-NI}"

case "$REGIAO" in
  NI|NORTE|NORDESTE|CENTRO_OESTE|SUL|SP|MG_ES_RJ) ;;
  *)
    echo "Regiao invalida: $REGIAO"
    echo "Validas: NI, NORTE, NORDESTE, CENTRO_OESTE, SUL, SP, MG_ES_RJ"
    exit 1
    ;;
esac

mkdir -p "$DEST" "$LAYOUTS"

# ---------------------------------------------------------------------------
# Layouts
# ---------------------------------------------------------------------------
# O diretorio de vinculos tem acento no nome, codificado em Latin-1 no
# servidor FTP: "vínculos" -> "v%EDnculos". Usar %C3%AD (UTF-8) falha com
# "Server denied you to change to the given directory".

echo "==> Baixando layouts oficiais"
curl -sS -o "$LAYOUTS/RAIS_vinculos_layout2020.xls" \
  "$FTP/Layouts/v%EDnculos/RAIS_vinculos_layout2020.xls"
curl -sS -o "$LAYOUTS/RAIS_estabelecimento_layout2018e2019.xls" \
  "$FTP/Layouts/estabelecimento/RAIS_estabelecimento_layout2018e2019.xls"
echo "    layouts em $LAYOUTS/"

# ---------------------------------------------------------------------------
# Microdados
# ---------------------------------------------------------------------------
# Os arquivos sao grandes. Alguns tamanhos compactados (.7z) de 2025:
#   NI            209 KB     NORTE      212 MB     CENTRO_OESTE   354 MB
#   NORDESTE      640 MB     SUL        705 MB     MG_ES_RJ       767 MB
#   SP           1,11 GB
# Descompactados, chegam a varias vezes esse tamanho: a regiao Norte, a
# menor, vira 1,5 GB com 5,6 milhoes de vinculos.
#
# O "-C -" retoma downloads interrompidos em vez de comecar de novo.

ARQ="RAIS_VINC_PUB_${REGIAO}.7z"

echo "==> Baixando $ARQ (pode demorar)"
curl -S --progress-bar -C - -o "$DEST/$ARQ" "$FTP/$ANO/$ARQ"

echo "==> Descompactando"
7z x -y -o"$DEST" "$DEST/$ARQ" > /dev/null

echo "==> Pronto"
ls -lh "$DEST"/RAIS_VINC_PUB_"${REGIAO}".* 2>/dev/null

cat <<'EOF'

Proximo passo:
  Rscript R/01-preparar-rais.R

Antes, ajuste no 01-preparar-rais.R:
  - ARQUIVO      : caminho do .COMT baixado
  - VARS_USADAS  : apenas as colunas que a analise vai usar
                   (ler as 62 colunas estoura a memoria de um notebook comum)
EOF
