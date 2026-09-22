#!/usr/bin/env bash
# Baixa o HTML bruto de todas as URLs do CCU para auditoria offline.
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
BASE="https://www.consultoriaunicamp.com"
OUT="/projects/sandbox/audit-ccu/raw"
mkdir -p "$OUT"

PAGES=(
  "/" "/sobre-nos" "/blank-7" "/mailing"
  "/prep4consulting-2026-2" "/x-ray" "/consulting-women-consulting" "/blank-6"
  "/conteudo" "/blank-2" "/blank-3" "/blank-4" "/blank-5"
  "/revisao-industrias" "/framework" "/guesstimate" "/entrevista" "/getting-the-job" "/blog"
  "/blank" "/members"
  "/shop" "/loyalty" "/book-online" "/forum" "/eventos" "/politica-troca"
  "/blank-1"
  "/service-page/processo-seletivo"
  "/event-details/prep4consulting-2026-2"
  "/event-details/teste-1"
  "/event-details/prep4consulting-2025-1-old"
  "/event-details/getting-the-job"
  "/event-details/prep4consulting-2023-2"
  "/event-details/prep4consulting-2"
  "/event-details/prep4consulting"
  "/event-details/prep4consulting-2024-1-1"
  "/event-details/prep4consulting-2024-2"
  "/event-details/prep4consulting-2025-2-1"
  "/event-details/prep4consulting-2025-1-2"
  "/event-details/prep4consulting-2025-2"
  "/event-details/prep4consulting-2025-2-1-1"
  "/event-details/prep4consulting-3"
  "/event-details/prep4consulting-4"
)

for p in "${PAGES[@]}"; do
  name=$(echo "$p" | sed 's#^/##; s#/#__#g')
  [ -z "$name" ] && name="HOME"
  code=$(curl -s -A "$UA" -w "%{http_code}" -o "$OUT/$name.html" "$BASE$p")
  size=$(wc -c < "$OUT/$name.html" | tr -d ' ')
  printf "%-4s %-9s %s\n" "$code" "$size" "$p"
done
