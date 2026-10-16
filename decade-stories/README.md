# Story Decade na Unicamp · Liga Empreendedora

Arte de story (1080x1920, vertical 9:16) para divulgar o evento da Decade na Unicamp, que
tem Open Bank como tema e o ex-CTO do Nubank como convidado. Segue a identidade da Decade e
a mesma linguagem dos panfletos `panfleto6.png` / `panfelto7.png`.

## Arquivos

| Arquivo | O que é |
|---|---|
| `story-decade-na-unicamp-offwhite.png` | versão principal, fundo off-white |
| `story-decade-na-unicamp-preto.png` | variante em fundo preto, para sequência de stories |
| `gerar_story_decade_unicamp.py` | gerador das duas artes, com todo o layout parametrizado |
| `preparar_assets.py` | reextrai os assets do panfleto, rode só se o panfleto de referência mudar |
| `assets/` | retrato, wordmark "nu" e logos recortados do panfleto oficial |
| `fonts/` | Playfair Display, JetBrains Mono, Montserrat e Anton (Google Fonts, licença OFL inclusa) |

Para regerar, rode `python gerar_story_decade_unicamp.py` com Pillow e numpy instalados.

## Texto da peça

- Chapéu, `A LIGA EMPREENDEDORA APRESENTA`
- Título serif, `Decade na Unicamp`
- Linha de apoio, "uma conversa sobre Open Bank e o futuro do sistema financeiro com quem
  construiu a engenharia do Nubank"
- Dados, `26.10 · 17h30 · Unicamp`, com Coffee Break incluso
- Credencial em mono, `↑ DECADE · US$ 85 MI EM SEED, A MAIOR DA AMÉRICA LATINA`
- Convidado, `Vitor Olivier · fundador da Decade`, com o selo `nu EX-CTO DO NUBANK` sobre o retrato
- CTA, `INSCREVA-SE · VAGAS LIMITADAS` com o link `luma.com/wqw35sxf` em destaque

Quem lidera a leitura é a Decade, que é o nome de peso do evento. Open Bank entra como tema
na linha de apoio, e a autoria da Liga aparece no chapéu e no lockup do rodapé.

## Decisões de identidade

Pelo manual de co-branding, a arte oficial do evento é liderada pela Decade, então a peça
usa off-white `#F5F1EC` e preto `#0B0B0B`, título em serif editorial e dados em mono. O
azul-marinho `#233555`, a cor-ponte da Liga, aparece só no chapéu e no filete do topo.

O logo da Liga entra na versão padrão colorida, igual ao panfleto, com a versão clara
(`LIGA` em off-white, foguete e `EMPREENDEDORA` em amarelo) na arte de fundo preto, como
manda o manual para fundo escuro. O amarelo fica restrito à assinatura e não vira camada
visual da peça.

O retrato, o selo do Nubank e os logos foram extraídos do panfleto já aprovado, então a arte
conversa com as outras peças da campanha sem retrabalho de arquivo.

## Área segura do Instagram

Todo o conteúdo vive entre `y=210` e `y=1702`. O topo fica livre para o avatar e o botão de
fechar, e a base deixa espaço para a barra de resposta.

O link aparece escrito no bloco escuro, então quem vê o story consegue digitar. Vale somar
o sticker de link do Instagram em cima do bloco para deixar o clique direto, já que texto
escrito na imagem não é clicável.

## Legenda sugerida para repost no feed

> A gente trouxe a Decade pra Unicamp. Dia 26.10, às 17h30, conversa com Vitor Olivier,
> ex-CTO do Nubank e fundador da Decade, sobre Open Bank e a engenharia que sustenta uma
> fintech desse tamanho. Vagas limitadas, inscrição em luma.com/wqw35sxf.
