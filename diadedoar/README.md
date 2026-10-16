# Save the date · Caminhada pelo Dia de Doar Campinas

Peças do NAS (Núcleo de Ação Social) com a Liga Empreendedora, em `out/`.

| Arquivo | Formato | Uso |
|---|---|---|
| `A-feed-titulo.png` | 1080×1350 | feed, título dominante com marca-texto laranja |
| `B-feed-data.png` | 1080×1350 | feed, data dominante, o "29.11" ocupa o centro |
| `C-story.png` | 1080×1920 | story, com as zonas de interface livres no topo e na base |

Cada peça tem três saídas, `.png`, `.jpg` (qualidade 95) e `@2x.png` para impresso.

---

## Como as duas identidades foram integradas

A **paleta vem do evento** e a **tipografia vem da Liga**. Isso mantém a peça reconhecível
como Dia de Doar sem abandonar a marca de quem está realizando.

Paleta medida na peça de referência do evento (`6abfdf9462829-lg.jpg`, do Centro
Comunitário Jardim Santa Lúcia), por mediana de cada família de cor.

| Cor | Hex | Onde entra na peça |
|---|---|---|
| laranja | `#FDA501` | marca-texto do título e etiqueta "Save the date" |
| roxo | `#8800C2` | a data e a faixa do rodapé |
| verde | `#55D62C` | bloco da camiseta e variação de marca-texto |
| ciano | `#08C8FC` | acento angular no topo |
| amarelo | `#FACE22` | etiquetas de horário da agenda |
| preto | `#211815` | texto, e é o preto da própria Liga (manual p.3) |

Tipografia da Liga, conforme o manual p.3, que define **Anton** para títulos e
**Montserrat** para corpo e legendas. Ambas são SIL Open Font License.

Um detalhe que facilitou a integração. O amarelo do Dia de Doar (`#FACE22`) é quase o
amarelo da Liga (`#F5C518`), então as duas paletas convivem sem briga de cor.

O logo da Liga entra na versão para fundo escuro, off-white com amarelo, aplicada sobre a
faixa roxa do rodapé. É o mesmo ativo em alta resolução produzido em `post3/assets`.

## Conteúdo das peças

Tudo vem do briefing, sem invenção.

| Dado | Valor |
|---|---|
| Data | 29 de novembro, domingo |
| Concentração | 8h, Bosque Jequitibás |
| Falas sobre o Dia de Doar | 8h30 |
| Início da caminhada | 9h |
| Trajeto | cerca de 1 km, até o Centro de Convivência |
| Inscrição | compra da camiseta oficial, R$ 60 |

**Nota de calendário.** O Dia de Doar de 2026 cai em **01/12**, que é a terça seguinte à
Black Friday (27/11). A caminhada em 29/11 antecede a data, o que é coerente com o
briefing, que fala em conscientizar a população *sobre* o Dia de Doar. As peças não
afirmam que 29/11 é o Dia de Doar.

---

## Legenda sugerida para o post

```
SAVE THE DATE · CAMINHADA PELO DIA DE DOAR

No dia 29 de novembro, Campinas vai caminhar pela cultura da doação.

Bosque Jequitibás
8h, concentração
8h30, falas sobre o Dia de Doar
9h, início da caminhada
Trajeto de cerca de 1 km até o Centro de Convivência

Mais do que uma caminhada, é um encontro de pessoas que acreditam na
generosidade e na força das organizações da sociedade civil.

Você participa adquirindo a camiseta oficial da caminhada, por R$ 60.
Vista essa causa, caminhe com a gente e espalhe a cultura da doação.

Reserve a data. Contamos com você.

@paica_campinas @diadedoacampinas

#DiaDeDoar #DiaDeDoarCampinas #doacampinas #GivingTuesday #Campinas
#LigaEmpreendedora #NucleoDeAcaoSocial
```

---

## Reproduzir

```bash
cd diadedoar
pip3 install pillow numpy
npm i -D playwright && npx playwright install chromium
node render.js pieces.json out
```

Para trocar texto, tamanhos ou cores, edite `pieces.json`. O campo `titulo` é uma lista de
linhas, e cada linha aceita `fundo` com os valores `laranja`, `verde` ou `limpa`, que
controlam o marca-texto.

## Pendências

1. **Logo do NAS.** Não tenho o arquivo, então o nome está composto em tipografia no
   rodapé, em Anton mais Montserrat. Mandando o PNG com fundo transparente, eu troco.

2. **Ilustrações oficiais do Dia de Doar.** A peça de referência traz andorinhas e um sol
   desenhados, que são arte da campanha. Não reproduzi esses desenhos, porque copiar
   ilustração de um JPEG de baixa resolução entregaria um resultado ruim e seria recriar
   arte de terceiro. A linguagem geométrica angular foi mantida, que é o que carrega o
   reconhecimento. Com os arquivos originais, eu encaixo.

3. **Logo oficial do Dia de Doar Campinas.** Mesmo caso. Se a organização liberar o
   lockup, ele pode entrar ao lado do NAS e da Liga no rodapé.

4. **Link de compra da camiseta.** As peças dizem o valor, mas não há link. Quando
   existir, vale entrar como "link na bio" ou QR code na versão story.
