# Save the date, Caminhada pelo Dia de Doar Campinas

Peças e copy da campanha de divulgação assinada pelo NAS, Núcleo de Ação Social, com a Liga Empreendedora.

## Arquivos

| Arquivo | Uso |
|---|---|
| `post-feed-1080x1080.png` | Post de feed, Instagram e Facebook |
| `post-story-1080x1920.png` | Story e Reels capa, com zonas de segurança respeitadas |
| `copy-save-the-date.md` | Legendas de feed, roteiro de story, WhatsApp e LinkedIn |
| `fontes/` | Scripts que geram as peças, para reedição |
| `fontes/assets/` | Logos do NAS e da Liga em PNG com fundo transparente |

Para regerar as peças depois de qualquer ajuste:

```bash
pip install Pillow numpy
cd fontes && python3 gera_posts.py
```

## Paleta, extraída do material oficial do evento

Os valores abaixo saíram de análise de matiz sobre a arte oficial da Caminhada pelo Dia de Doar Campinas, não de estimativa visual.

| Cor | Hex | RGB | Onde usar |
|---|---|---|---|
| Laranja | `#FEA501` | 254, 165, 1 | Faixa de destaque atrás do título |
| Roxo | `#8800C2` | 136, 0, 194 | Forma angular e faixa da data |
| Verde | `#55D72C` | 85, 215, 44 | Caixa da tagline e selo Campinas |
| Verde escuro | `#024C00` | 2, 76, 0 | Texto sobre o verde |
| Ciano | `#07C9FE` | 7, 201, 254 | Andorinhas |
| Amarelo | `#F8D205` | 248, 210, 5 | Sol |
| Creme | `#F9F0E1` | 249, 240, 225 | Caixa do logo do movimento |
| Preto | `#0F0210` | 15, 2, 16 | Títulos |
| Navy | `#0A2A5E` | 10, 42, 94 | Olho e penas das andorinhas |

Cores das organizações que assinam:

| Organização | Hex | RGB |
|---|---|---|
| NAS, vermelho | `#D6322C` | 214, 50, 44 |
| Liga, grafite | `#212121` | 33, 33, 33 |
| Liga, amarelo | `#FDC815` | 253, 200, 21 |

A integração das duas identidades funciona porque o amarelo da Liga, `#FDC815`, é vizinho direto do amarelo do sol do evento, `#F8D205`, e harmoniza com o laranja `#FEA501`. Por isso o logo da Liga entra sem precisar de ajuste cromático. O vermelho do NAS é a única cor estranha à paleta, então ele aparece apenas na barra de assinatura, sobre fundo branco e separado por um filete, para não competir com o laranja do título.

## Decisões de layout

**O título usa faixa sólida atrás do texto**, que é o recurso de destaque da identidade original do evento. Mantivemos as duas linhas mais importantes, "DIA DE DOAR" e "CAMPINAS", sobre laranja, e deixamos "CAMINHADA PELO" sem faixa para criar hierarquia.

**A data ganhou faixa roxa.** No material original o roxo aparece como forma geométrica decorativa. Aqui ele passa a carregar informação, porque save the date precisa que a data seja o segundo elemento mais visível da peça, logo depois do nome do evento.

**A assinatura fica isolada no rodapé**, separada por um filete e sobre branco. Em peça com duas organizações, assinatura disputando espaço com ilustração gera a leitura de patrocínio em vez de realização conjunta.

**No story a data vira uma folha de calendário**, com cabeçalho laranja para o dia da semana e corpo roxo para o dia e o mês. Ao lado dela ficam as três informações práticas, cada uma com um rótulo pequeno e o valor em destaque, marcadas com as cores da paleta. Assim a pessoa lê a data de longe e os detalhes de perto.

**O card do movimento repete a composição da arte original**, logo do Dia de Doar sobre creme e tagline sobre verde, com o sol e a andorinha saindo pela borda direita. É a referência visual mais reconhecível da campanha em Campinas.

**O story não tem links.** Link escrito em imagem de story não é clicável, ocupa espaço e disputa atenção com a assinatura. Se for preciso direcionar para um site, use a figurinha de link do próprio Instagram, posicionada na área livre abaixo da assinatura.

**O story respeita as zonas de segurança** do Instagram. O texto começa em 236 pixels e o último elemento de conteúdo termina em 1662, deixando a base livre para a barra de resposta. As formas roxas e a andorinha pequena ficam nos cantos, só como decoração.

## Ilustrações

A andorinha, o sol, a forma angular roxa e o coração trançado do logo do Dia de Doar foram recriados em vetor programático a partir da arte oficial em JPEG, em resolução alta e com a paleta medida. O coração reproduz o trançado original, com tiras verdes no sentido ascendente e douradas no descendente, alternando quem passa por cima em cada cruzamento.

A andorinha não é um desenho decorativo qualquer. Ela é a imagem que sustenta a assinatura do movimento em Campinas, "uma andorinha só não faz verão", e por isso aparece nas duas peças junto da tagline.

## Ponto de atenção

O logo do Dia de Doar presente nas peças é uma **recriação feita a partir do JPEG**, adequada para mockup e para publicação em rede social. Para material impresso, ou para qualquer peça que vá passar por aprovação do movimento, substitua pelo arquivo vetorial oficial do Dia de Doar Brasil. O mesmo vale se o movimento tiver manual de marca com regras de área de respiro e de aplicação mínima.

Os logos do NAS e da Liga Empreendedora são os arquivos originais, baixados dos sites oficiais das duas organizações, em PNG com fundo transparente.
