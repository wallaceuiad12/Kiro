# Projeto Leroy Merlin, apresentação da Nunes & Lucato

Apresentação de 4 slides com o projeto de upcycle dos uniformes inservíveis da
Leroy Merlin, na identidade visual da Nunes & Lucato.

## Arquivos para usar

| Arquivo | Para quê |
| --- | --- |
| `slides-projeto-leroy-merlin.pptx` | Abrir no PowerPoint, os 4 slides prontos |
| `slides-projeto-leroy-merlin.pdf` | Enviar por e-mail ou WhatsApp, 464 KB |
| `preview-slide-1.jpg` a `preview-slide-4.jpg` | Visualização rápida |
| `build_slides.py` | Gerar os slides de novo, para ajustar número ou texto |
| `build_mockup.py` | Gerar de novo o mockup do produto finalizado |
| `prompt-slides-projeto-leroy-merlin.md` | O prompt que originou o trabalho |

Os slides têm 1440 x 810 pt, a mesma medida do arquivo original da Nunes, então
entram no deck institucional sem redimensionar.

## Os 4 slides

**1. Capa.** Gradiente e textura diagonal da capa do modelo, foto da ecobag em
monocromia azul, logotipo branco da Nunes & Lucato.

**2. Introdução.** Quem é a Nunes & Lucato e o que o projeto propõe, com o fluxo em
quatro etapas, coleta e transporte, descaracterização, corte e costura e produto
acabado. Foto da necessaire.

**3. O Projeto Leroy Merlin.** Logotipo da Leroy Merlin, estoque detalhado por peça
com a grade completa de tamanhos e a matéria-prima apurada, mais o mockup dos dois
produtos acabados.

| Peça recebida | Estoque | Grade | Matéria-prima |
| --- | --- | --- | --- |
| Jaqueta verde musgo | 626 (618 F, 8 M) | PP 47, P 141, M 205, G 141, GG 40, XG 44 e P 7, XGG 1 | 495 m, cerca de 300 peças |
| Moletom verde Leroy | 297 (37 F, 260 M) | XG 14, EG 13, EXG 10 e P 46, M 54, G 67, GG 13, XG 27, EG 4, EXG 27, EGG 22 | 237 m, cerca de 415 peças |

**4. Volume e valores.** 1.250 necessaires a R$ 25,00 e 1.250 ecobags a R$ 20,00,
total de 2.500 peças por R$ 56.250,00.

## Imagens, uma por slide

Cada slide usa um tratamento de imagem diferente, para nenhuma foto se repetir.

- Capa, ecobag em monocromia azul
- Introdução, foto da necessaire emoldurada
- O projeto, mockup dos dois produtos
- Volume e valores, sem foto, o espaço é da tabela e dos indicadores

O logotipo da Leroy Merlin aparece no topo direito de todos os slides depois da capa,
sempre na mesma posição, como co-marca da proposta.

## O mockup

Montado pelo `build_mockup.py`, que recorta os dois produtos das fotos originais com
GrabCut e compõe sobre o branco da identidade. Três decisões para não parecer
montagem:

1. **A sombra sai da própria silhueta** do produto, achatada e inclinada conforme a
   direção da luz, em duas camadas, uma de contato curta e escura na base e uma
   projetada longa e difusa. Elipse genérica embaixo do objeto é o que mais denuncia
   recorte.
2. **Fundo branco puro**, sem cenário de estúdio nem linha de apoio. Gradiente e
   linha de horizonte deixavam a cena artificial, e o branco faz a imagem se
   integrar ao card do slide em vez de parecer uma foto colada.
3. **Escalas reais**, a ecobag com cerca de 38 cm de altura e a necessaire com 22 cm
   de largura, na mesma proporção que teriam lado a lado.

Na necessaire, recortar só por luminância deixava farrapos de fundo colados na base,
porque a sombra do fundo do estúdio é escura, então a máscara é ancorada no corpo
escuro do produto e depois dilatada para reincorporar o zíper. A máscara também é
erodida 1 px antes de suavizar, senão sobra halo claro na silhueta.

Equalizar a exposição das duas peças foi testado e descartado, lavava o preto da
necessaire e estourava o verde da ecobag.

## Identidade visual

Tudo foi extraído do próprio arquivo `Nunes_Lucato_Bioma_Textil_Ecoponto_Belezinho.pptx.pdf`,
capa e slides 2 e 8.

- Tipografia Montserrat, Light nos títulos, Regular no corpo, Medium nos rótulos
- Margem lateral em 91,5 pt, título em 38,3 pt (49,5 pt na capa), corpo em 16,2 pt
- Azul royal `#3432C9`, azul-marinho `#14142E`, cinzas `#6E7288`, `#3A3C55` e
  `#9A9DB0`, divisórias `#DFE2F0` e verde de upcycle `#12A87B`
- Gradiente da capa de `#090817` a `#2E2CD4`, amostrado do arquivo modelo
- Os dois logotipos da Nunes, o escuro do rodapé e o branco da capa, foram extraídos
  do modelo com transparência

## Como gerar de novo

```sh
pip install reportlab pillow svglib          # slides
pip install opencv-python-headless numpy     # mockup
python3 build_mockup.py
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

## Creditos de terceiros

`leroy-merlin-logo.svg` é o logotipo oficial da Leroy Merlin, obtido do
[Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Leroy_Merlin_-_logo_(France,_1995-).svg),
marcado como domínio público no repositório. É marca registrada da Leroy Merlin e
aparece aqui apenas na identificação do cliente da proposta.

## Ponto que precisa de conferência

As fotos de estoque indicam matéria-prima equivalente a cerca de 715 peças de
produção, somando jaqueta e moletom. A meta do projeto é de 2.500 acessórios. Os dois
números são compatíveis se cada uniforme render mais de um acessório, porém vale
confirmar o rendimento com a produção antes de enviar a proposta.
