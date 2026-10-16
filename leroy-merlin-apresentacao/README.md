# Projeto Leroy Merlin, 2 slides para a apresentação da Nunes & Lucato

Slides 12 e 13 para entrar na apresentação institucional da Nunes & Lucato, com o
projeto de upcycle dos uniformes inservíveis da Leroy Merlin.

## Arquivos para usar

| Arquivo | Para quê |
| --- | --- |
| `slides-projeto-leroy-merlin.pptx` | Abrir no PowerPoint e copiar os 2 slides para dentro do deck |
| `slides-projeto-leroy-merlin.pdf` | Enviar por e-mail ou WhatsApp, 384 KB |
| `preview-slide-12.png`, `preview-slide-13.png` | Visualização rápida |
| `prompt-slides-projeto-leroy-merlin.md` | O prompt que originou os slides |
| `build_slides.py` | Script que gera os slides, para ajustar número ou texto depois |

Os dois slides têm 1440 x 810 pt, a mesma medida do arquivo original, então entram
no deck sem redimensionar.

## Conteúdo

**Slide 12, O Projeto Leroy Merlin.** Peças recebidas à esquerda (jaqueta verde
musgo com 626 peças e 495 metros de tecido, moletom verde Leroy com 297 peças e 237
metros), totalizando 923 uniformes e 732 metros. Peças criadas à direita, necessaire
e ecobag, com as fotos dos produtos.

**Slide 13, Volume e valores.** Tabela com 1.250 necessaires a R$ 25,00 e 1.250
ecobags a R$ 20,00, total de 2.500 peças por R$ 56.250,00.

## Identidade visual

Tudo foi extraído do próprio arquivo `Nunes_Lucato_Bioma_Textil_Ecoponto_Belezinho.pptx.pdf`,
slides 2 e 8, para os slides novos não parecerem um anexo externo.

- Tipografia Montserrat, Light nos títulos, Regular no corpo, Medium nos rótulos
- Margem lateral em 91,5 pt, título em 38,3 pt, corpo em 16,2 pt
- Azul royal `#3432C9`, azul-marinho `#14142E`, cinzas `#6E7288`, `#3A3C55` e `#9A9DB0`,
  divisórias `#DFE2F0` e verde de upcycle `#12A87B`
- Kicker com traço azul, título em dois pesos, cards com barra superior colorida e
  rodapé com o logotipo original, recortado do próprio arquivo modelo

## Como gerar de novo

```sh
pip install reportlab pillow
python3 build_slides.py
```

As fontes estáticas em `fontes/` foram geradas a partir da fonte variável oficial do
Google Fonts, sob licença OFL (veja `fontes/OFL.txt`).

```sh
curl -sL -o MontserratVF.ttf \
  "https://raw.githubusercontent.com/google/fonts/main/ofl/montserrat/Montserrat%5Bwght%5D.ttf"
python3 -c "
from fontTools import ttLib
from fontTools.varLib import instancer
for nome, peso in [('Light',300),('Regular',400),('Medium',500),('SemiBold',600)]:
    f = ttLib.TTFont('MontserratVF.ttf')
    instancer.instantiateVariableFont(f, {'wght': peso}, updateFontNames=True).save(f'Montserrat-{nome}.ttf')
"
```

O `updateFontNames=True` é necessário, sem ele as quatro instâncias saem com o mesmo
nome interno e o PDF acaba usando um único peso em tudo.

## Ponto que precisa de conferência

As fotos de estoque indicam matéria-prima equivalente a cerca de 715 peças de
produção, somando jaqueta e moletom. A meta do projeto é de 2.500 acessórios. Os dois
números são compatíveis se cada uniforme render mais de um acessório, porém vale
confirmar o rendimento com a produção antes de enviar a proposta.
