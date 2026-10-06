# Formação Econômica do Brasil — material de estudo da P1

Resumo do programa da disciplina, organizado a partir do slide **"Seis autores, uma linha"**
(print `../20260924_165705.jpg`), e três provas dissertativas simuladas com gabarito completo.

| Arquivo | O que é |
|---|---|
| `resumo-p1-formacao-brasil.pdf` | **O material de estudo** — 11 páginas, pronto para ler ou imprimir |
| `resumo-p1.md` | Mesmo conteúdo em Markdown, para ler no GitHub |
| `gerar_resumo_pdf.py` | Script que gera o PDF do resumo (todo o conteúdo está aqui) |
| `provas-dissertativas-gabarito-completo.pdf` | **As três provas simuladas + gabarito de todos os itens** — 26 páginas |
| `provas-dissertativas-gabarito-completo.md` | Mesmo conteúdo em Markdown, para ler no GitHub |
| `gerar_provas_pdf.py` | Script que gera as provas em PDF **e** em Markdown (conteúdo aqui) |
| `verificar_gabarito.py` | Confere as somas de pontos e a presença dos cinco blocos de cada questão |
| `estilo_pdf.py` | Estilos compartilhados: fontes, paleta, capa, tabelas, caixas de destaque |

## O resumo

Os **seis autores do slide** recebem tratamento aprofundado (pontos 1 e 2 do programa):
Caio Prado (1942), Novais (1979), Fragoso/Bicalho/Gouvêa (2000), Faoro (1958), Godinho e Neves (2022).
A chave de leitura é a **unidade de análise** de cada um — é a escala que produz a tese.
Inclui a explicação do rodapé do slide (circunscrição em Carneiro, 1970).

Os **pontos 3 a 6** do programa entram como moldura: Atlântico Sul, sociedade escravista,
mineração e crise do Antigo Regime, e a formação do Estado nacional.

Fecha com um **roteiro de revisão em 10 frases** e o **checklist das 7 fontes primárias**.

## As provas dissertativas

Três simulados de 100 pontos e 2 horas, com três questões cada:

1. **O sentido da colonização e o Antigo Sistema Colonial** — Caio Prado, Novais, Fragoso *et al.*;
   fonte: Frei Vicente do Salvador (1627).
2. **O Estado português: patrimonialismo, fisco e expansão** — Faoro, Godinho; fonte: Zurara (1453).
3. **Escala, Estado e o que havia antes** — prova integradora: Neves, Carneiro e os seis autores.

Cada questão do gabarito tem **cinco blocos**: o que a questão pede, a distribuição de pontos item
por item, uma resposta-modelo redigida, os erros que mais custam nota e os pontos de diferenciação.
Fecha com dois apêndices: a lista dos **dez erros clássicos** e o **quadro de autoavaliação**.

Esta é a **edição completa**: a primeira versão (`../provas-dissertativas-com-gabarito (1).pdf`)
trazia a distribuição de pontos de todas as questões, mas só parte dos outros blocos. Os blocos que
faltavam foram escritos e vêm marcados com **[acrescentado]** no título — nenhum conteúdo da versão
anterior foi alterado. A Parte II abre com um **mapa de cobertura** mostrando o que já existia e o
que entrou agora.

## Como regerar os PDFs

```bash
pip install reportlab
python3 gerar_resumo_pdf.py    # resumo-p1-formacao-brasil.pdf
python3 gerar_provas_pdf.py    # provas-...-completo.pdf e .md
python3 verificar_gabarito.py  # confere as somas de pontos
```

Para editar o conteúdo, mexa no script correspondente — o texto está todo lá, em listas de
strings. As tags aceitas nos textos são as do ReportLab (`<b>`, `<i>`, `<br/>`); use `&amp;`
para o "e" comercial. Em `bullets()`, um item que começa com `>` virá recuado como sub-item.

Em `gerar_provas_pdf.py` o conteúdo fica na lista `DOC`, em blocos `('tipo', dados)`, e dois
renderizadores consomem a mesma lista — um gera o PDF, o outro o Markdown. Assim o texto é escrito
uma única vez e as duas saídas não divergem.
