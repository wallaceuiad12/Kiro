# Formação Econômica do Brasil — material de estudo da P1

Resumo do programa da disciplina, organizado a partir do slide **"Seis autores, uma linha"**
(print `../20260924_165705.jpg`).

| Arquivo | O que é |
|---|---|
| `resumo-p1-formacao-brasil.pdf` | **O material de estudo** — 11 páginas, pronto para ler ou imprimir |
| `resumo-p1.md` | Mesmo conteúdo em Markdown, para ler no GitHub |
| `gerar_resumo_pdf.py` | Script que gera o PDF (todo o conteúdo está aqui) |
| `estilo_pdf.py` | Estilos compartilhados: fontes, paleta, capa, tabelas, caixas de destaque |

## Conteúdo

Os **seis autores do slide** recebem tratamento aprofundado (pontos 1 e 2 do programa):
Caio Prado (1942), Novais (1979), Fragoso/Bicalho/Gouvêa (2000), Faoro (1958), Godinho e Neves (2022).
A chave de leitura é a **unidade de análise** de cada um — é a escala que produz a tese.
Inclui a explicação do rodapé do slide (circunscrição em Carneiro, 1970).

Os **pontos 3 a 6** do programa entram como moldura: Atlântico Sul, sociedade escravista,
mineração e crise do Antigo Regime, e a formação do Estado nacional.

Fecha com um **roteiro de revisão em 10 frases** e o **checklist das 7 fontes primárias**.

## Como regerar o PDF

```bash
pip install reportlab
python3 gerar_resumo_pdf.py
```

Para editar o conteúdo, mexa em `gerar_resumo_pdf.py` — o texto está todo lá, em listas de
strings. As tags aceitas nos textos são as do ReportLab (`<b>`, `<i>`, `<br/>`); use `&amp;`
para o "e" comercial. Em `bullets()`, um item que começa com `>` virá recuado como sub-item.
