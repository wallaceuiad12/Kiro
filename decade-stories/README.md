# Story Open Bank · Decade x Liga Empreendedora

Arte de story (1080x1920, vertical 9:16) para divulgar o evento de Open Bank com o
ex-CTO do Nubank, seguindo a identidade da Decade e a mesma linguagem dos panfletos
`panfleto6.png` / `panfelto7.png`.

## Arquivos

| Arquivo | O que é |
|---|---|
| `story-open-bank-offwhite.png` | versão principal, fundo off-white |
| `story-open-bank-preto.png` | variante em fundo preto, para feeds escuros ou sequência de stories |
| `gerar_story_open_bank.py` | gerador das duas artes, com todo o layout parametrizado |
| `preparar_assets.py` | reextrai os assets do panfleto, rode só se o panfleto de referência mudar |
| `assets/` | retrato, wordmark "nu" e logos monocromáticos recortados do panfleto oficial |
| `fonts/` | Playfair Display, JetBrains Mono, Montserrat e Anton (Google Fonts, licença OFL inclusa) |

Para regerar, rode `python gerar_story_open_bank.py` com Pillow, numpy e qrcode instalados.
O QR é gerado na hora a partir do link, então não há perda de qualidade em nenhum tamanho.

## Texto da peça

- Chapéu, `A LIGA EMPREENDEDORA APRESENTA`
- Título serif, `Open Bank na Unicamp`
- Linha de apoio, "a Liga Empreendedora traz pra Unicamp uma conversa sobre open banking
  com quem construiu a engenharia do Nubank"
- Dados, `26.10 · 17h30 · Unicamp`, com Coffee Break incluso
- Credencial em mono, `↑ DECADE · US$ 85 MI EM SEED, A MAIOR DA AMÉRICA LATINA`
- Convidado, `Vitor Olivier · fundador da Decade`, com o selo `nu EX-CTO DO NUBANK` sobre o retrato
- CTA, `INSCREVA-SE · vagas limitadas` com QR para https://luma.com/wqw35sxf

## Decisões de identidade

Pelo manual de co-branding, a arte oficial do evento é liderada pela Decade, então a peça
usa off-white `#F5F1EC` e preto `#0B0B0B`, título em serif editorial, dados em mono e nada
de amarelo. O azul-marinho `#233555`, a cor-ponte da Liga, aparece só no chapéu e no filete
do topo, que é justamente onde a autoria da Liga fica explícita. Os logos entram como
assinatura monocromática no rodapé, lado a lado e com área de respiro, como manda o manual
para fundo off-white.

A foto, o selo do Nubank, o QR e os logos foram extraídos do panfleto já aprovado, então a
arte conversa com as outras peças da campanha sem retrabalho de arquivo.

## Área segura do Instagram

Todo o conteúdo vive entre `y=210` e `y=1702`. O topo fica livre para o avatar e o botão de
fechar, e a base deixa espaço para a barra de resposta. Sobra ainda uma faixa confortável
acima do rodapé caso você queira colar o sticker de link em cima do bloco `INSCREVA-SE`.

## Legenda sugerida para repost no feed ou close friends

> A gente trouxe o Open Bank pra Unicamp. Dia 26.10, às 17h30, conversa com Vitor Olivier,
> ex-CTO do Nubank e fundador da Decade, sobre o sistema financeiro aberto e a engenharia
> que sustenta uma fintech desse tamanho. Vagas limitadas, link no QR e na bio.
