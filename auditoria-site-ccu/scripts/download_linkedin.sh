#!/usr/bin/env bash
# Baixa as imagens públicas do LinkedIn do CCU para inventário e proposta de uso.
cd /projects/sandbox/audit-ccu/social
mkdir -p img
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"

dl() { # nome url
  curl -s -A "$UA" -L "$2" -o "img/$1"
  local sz; sz=$(wc -c < "img/$1" 2>/dev/null | tr -d ' ')
  local tp; tp=$(file -b --mime-type "img/$1" 2>/dev/null)
  printf "  %-42s %9s bytes  %s\n" "$1" "$sz" "$tp"
}

echo "=== Identidade ==="
dl "logo-ccu.png"  "https://media.licdn.com/dms/image/v2/C4E0BAQHlYT7GDhRkEQ/company-logo_200_200/company-logo_200_200/0/1630637357788/clube_de_consultoria_universitario_logo?e=2147483647&v=beta&t=FH9VQPE8LIW7Vy9KP6kjRJF5dJp0teqPpMzz2xDKwXY"
dl "capa-ccu.png"  "https://media.licdn.com/dms/image/v2/C4E1BAQFkwNnr82fm6g/company-background_10000/company-background_10000/0/1605822249367/clube_de_consultoria_universitario_cover?e=2147483647&v=beta&t=2xDXdTSAoF6_FAjsBsua8OmBZ24T1Z9_2DUSBEPWxpQ"

echo "=== CWC 2026 (3a edicao, em andamento) ==="
dl "cwc-2026-a.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQEgcu0RhZTM2w/feedshare-image-high-res/B4DaAtH6oDI4AU-/0/1787463445292?e=2147483647&v=beta&t=sbXaU9MMJGI-bPAKvoYuTUBHr6nWPdQrUaoNJHyjBhQ"
dl "cwc-2026-b.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQGCZIf-zW0SSw/feedshare-image-high-res/B4DaAtH6lJJIAY-/0/1787463445038?e=2147483647&v=beta&t=LsjXAg5MBFJ6a9jrfXGcMUGrEvepyG2ld1Z1jXH3bF0"
dl "cwc-2026-c.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQHK1oSwSVhx7w/feedshare-image-high-res/B4DaAtH6nlJ0AU-/0/1787463445267?e=2147483647&v=beta&t=yTHl3SHhm4cAZx2mTmZ-HE-HCUir0AD9yfodQmPi_x4"
dl "cwc-2026-d.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQGtPg6uphft1g/feedshare-shrink_1280/B4DaAtH6llHsAQ-/0/1787463445083?e=2147483647&v=beta&t=C5H60WYVMNFa8IVQBkkWnTbe4hPollObxSuVSedZ0ss"

echo "=== Prep4Consulting 2026.2 ==="
dl "p4c-cronograma.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQGlBvbbKZqvtg/feedshare-shrink_1280/B4DZ9167lxIIAM-/0/1784389810786?e=2147483647&v=beta&t=Uq80FO9HGu4lH4cAN5AsS6R2hFepm2M7OlpAzHNTvNA"
dl "p4c-reta-final.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQHJ6JHPYpUEWQ/feedshare-image-high-res/B4DZ9rUtJfKsAU-/0/1784212018013?e=2147483647&v=beta&t=LzRRFgieTufcj5mJvQSJGOteno_EPwTG3N_ZuQIvBrk"
dl "p4c-parceiros-1.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQG3HculMy517Q/feedshare-image-high-res/B4DZ85U9A9IEAU-/0/1783373222389?e=2147483647&v=beta&t=OHYRes2INEqrWZbplb_DV0bl5XCH8e03riKJ0PJpcPY"
dl "p4c-parceiros-2.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQHWs05-c77M0A/feedshare-image-high-res/B4DZ85U9CNGwAU-/0/1783373222483?e=2147483647&v=beta&t=LLzucWL6RF4or4pzoFnMjSmNRuUcatkkz80wKndKRoc"
dl "p4c-parceiros-3.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQFgKQBjqn7Vhg/feedshare-image-high-res/B4DZ9n4fVbIIAU-/0/1784154289949?e=2147483647&v=beta&t=GmxaiiWtzm8jayAJT1CKaMliQpieOhWMCs4ODez7pUE"
dl "p4c-parceiros-4.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQHnC99DLNnJ1Q/feedshare-shrink_1280/B4DZ9n4fSPKYAM-/0/1784154289541?e=2147483647&v=beta&t=kYLGwX2KFAs6JFSj4WcfJJzz3zEtldN1Wt7EGsRWbzQ"
dl "p4c-parceiros-5.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQGBpWhLJe1pvw/feedshare-shrink_1280/B4DZ9n4fRfJwAM-/0/1784154289491?e=2147483647&v=beta&t=ddhbZcvLxgEYMq0ehP57VEL4FTDBLpR21yQfFW2rwvA"
dl "p4c-parceiros-6.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQEBpxr1B5nw-A/feedshare-image-high-res/B4DZ9n4fPwIIAU-/0/1784154289425?e=2147483647&v=beta&t=aOD3_xE9k-VM6QL1DtgayZcM2KxWgzkmy3ewPIN8oyk"

echo "=== Glossario de consultoria (ativo de conteudo) ==="
dl "glossario-1.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQFtBnRPsDlJDQ/feedshare-image-high-res/B4DZ85VbagKYAU-/0/1783373346723?e=2147483647&v=beta&t=mvBfiNG7-QOmSIRfFMcuzcTpolq76Y50oFLkR91Qtgc"
dl "glossario-2.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQHe6gff7nYYYw/feedshare-shrink_1280/B4DZ85Vbc3I4AM-/0/1783373346854?e=2147483647&v=beta&t=1fkqnd4QO9xbs_QOrAUDdlBiUQYgf78S1d8jaceQeLE"
dl "glossario-3.jpg" "https://media.licdn.com/dms/image/v2/D4D22AQHyixGsPvubRw/feedshare-image-high-res/B4DZ85VbkLHEAU-/0/1783373347327?e=2147483647&v=beta&t=31Zjpe0FH666GvuG8DA0r90RHt0L1_5xpY_SHUWHr9Y"
