# Auditoria do site do CCU — Clube de Consultoria Universitário

Diagnóstico, plano de ação priorizado e guia de execução no Wix para
[consultoriaunicamp.com](https://www.consultoriaunicamp.com/).

**Coleta:** 16 de setembro de 2026 · **Plataforma auditada:** Wix Editor clássico (não Studio)
**Escopo:** 44 URLs indexáveis verificadas por HTTP · 4 sites de benchmark medidos com o mesmo método

---

## Comece por aqui

| Documento | O que é | Abrir |
|---|---|---|
| **Guia de execução no Wix** (PDF, 27 páginas) | Passo a passo ilustrado, tarefa por tarefa, com capturas do site, diagramas dos painéis do Wix e checklists para imprimir | [`Guia-Execucao-Wix-CCU.pdf`](Guia-Execucao-Wix-CCU.pdf) |
| **Relatório completo** (Markdown) | Diagnóstico integral: inventário das 44 URLs, 23 achados críticos, rubrica comparativa, mapa do site, design system, tabela de SEO e backlog em 3 ondas | [`RELATORIO-CCU.md`](RELATORIO-CCU.md) |

> O GitHub abre os dois direto no navegador — o PDF tem visualizador próprio e o Markdown é renderizado.
> Para baixar o PDF, use o botão **Download raw file** no canto superior direito do visualizador.

---

## Os cinco achados que mais importam

1. **Os dois funis de inscrição estão quebrados ao mesmo tempo.** O botão do Processo Seletivo aponta
   para o *"Formulário de Inscrição PS Interno CCU 2022.1"*, que está fechado. Os dois botões
   "Compre agora" do curso levam a uma página que responde *"Vendas encerradas"*. Não há caminho de
   entrada funcionando, nem para membro nem para aluno pagante.

2. **A página do Processo Seletivo não recebe nenhum link em todo o site.** Não está no menu, nem no
   rodapé, nem em nenhuma outra página. O funil de recrutamento existe e é inalcançável por navegação.

3. **Um link errado esconde 15 casebooks que funcionam.** Em `/conteudo`, o botão "Ver mais" do card
   "Cases completos" aponta para a raiz do site. Isso orfana a vertical inteira de casebooks — cujos
   15 PDFs (MIT, Harvard, Wharton, Kellogg, Ross…) respondem HTTP 200 normalmente.

4. **O Consulting Women's Community aconteceu com 7 consultorias e o site não mencionou nenhuma.**
   3ª edição, 19/08 a 24/09/2026, com McKinsey, Accenture, Kearney, Roland Berger, Bain, Peers e BCG.
   A página do CWC tem 236 palavras de adjetivos, zero data, zero parceiro, zero botão de inscrição.

5. **48% das URLs são órfãs.** 21 das 44 não recebem link interno, incluindo uma página
   *"Site em manutenção"* indexável com o mesmo título SEO da home, e duas páginas de evento
   chamadas literalmente *"teste"*.

**Recomendação central:** o site não precisa de redesign. Precisa de religamento e poda. O clube já
tem os ativos que faltam à concorrência (82 alunos, nota 9,7, NPS 86, 44 alumni nomeados em
BCG/Bain/McKinsey/Kearney, 15 casebooks) e já tem um sistema de estilos coerente configurado — o
problema é que os ativos estão em páginas órfãs e o sistema de estilos é sobrescrito 3.948 vezes.

---

## A causa por trás dos defeitos

O CCU **não tem** problema de produção de conteúdo. Produz cronograma detalhado com a consultoria de
cada módulo, prova de parceria, glossário de termos, política de desconto de grupo e campanhas de PS —
com regularidade e qualidade gráfica melhor que a do site.

A hipótese que fecha o diagnóstico: **o site não está no fluxo de trabalho do clube.** As campanhas
nascem e morrem no Instagram e no LinkedIn, e o site virou um arquivo de 2022–2023. Isso explica as 21
páginas órfãs, o rodapé em `©2023` e o botão do PS apontando para um formulário de 2022.1.

Daí o único item do plano que não corrige um defeito, e sim a causa:
**a cada post de campanha nas redes, atualizar a página correspondente do site no mesmo dia.**

---

## O que tem em cada pasta

```
auditoria-site-ccu/
├── Guia-Execucao-Wix-CCU.pdf     Guia ilustrado, 27 páginas (comece aqui)
├── RELATORIO-CCU.md              Relatório completo, 12 seções
├── evidencias/
│   ├── capturas/                 11 capturas reais do site público (1440×1000, 16/09/2026)
│   └── linkedin/                 17 peças gráficas do CCU recuperadas do LinkedIn público
├── diagramas/                    10 diagramas dos painéis do Wix (PNG) + fonte SVG
├── dados/
│   ├── meta.json                 título, descrição, robots, canonical e H1 das 44 URLs
│   ├── inbound.json              grafo de links internos (base do cálculo de páginas órfãs)
│   ├── style.json                tamanhos de fonte, famílias e cores em uso
│   └── texto-paginas/            texto visível extraído de cada uma das 44 URLs
└── scripts/                      tudo que é reproduzível
```

### Scripts — a auditoria é reproduzível

| Script | O que faz |
|---|---|
| `fetch.sh` | Baixa o HTML bruto das 44 URLs |
| `extract_meta.py` | Extrai título, descrição, robots, canonical e headings |
| `extract_text.py` | Extrai o texto visível de cada página |
| `extract_links.py` | Monta o grafo de links e identifica as páginas órfãs |
| `analyze_style.py` | Conta tamanhos de fonte, famílias e sobrescritas inline |
| `wcag.py` | Calcula o contraste WCAG dos pares de cor da paleta |
| `download_linkedin.sh` | Baixa as peças públicas do LinkedIn |
| `build_diagramas.py` | Gera os 10 diagramas em SVG |
| `build_pdf.py` | Monta o PDF final (requer `weasyprint`) |

Para refazer a coleta do zero:

```bash
bash fetch.sh && python3 extract_meta.py && python3 extract_text.py \
  && python3 extract_links.py && python3 analyze_style.py && python3 wcag.py
```

---

## Sobre as imagens do guia

O PDF usa três tipos de imagem e os distingue explicitamente:

- **Capturas reais do site do CCU** (moldura cinza) — evidência, tiradas do site público.
- **Diagramas esquemáticos dos painéis do Wix** — marcados *"ESQUEMA — não é captura de tela do Wix"*.
  São ilustrações originais. **Não foi possível gerar capturas reais do editor Wix**, porque isso
  exigiria acesso logado à conta do clube.
- **Peças gráficas do próprio CCU**, recuperadas do LinkedIn público.

---

## Limites desta auditoria

- **Instagram não verificado.** `@ccuclubedeconsultoria` exige autenticação e bloqueou o acesso
  (redirecionou para `/accounts/login`). Nada do Instagram foi analisado.
- **Avaliação sobre o HTML servido, não sobre renderização pixel-a-pixel.** Contraste, tipografia e
  divergência entre desktop e mobile vêm dos tokens CSS e do texto realmente entregue a cada
  *user-agent*.
- **Sem acesso ao painel Wix do clube.** Os caminhos de clique seguem a estrutura do Wix Editor
  clássico, confirmada pelo código do site (`"isResponsive":false`, `id="wixDesktopViewport"`).
  Rótulos de menu podem variar conforme a versão da conta.
- Os documentos separam `[FATO OBSERVADO]`, `[HIPÓTESE]` e `[RECOMENDAÇÃO]`, e escrevem
  **"não verificado"** onde a checagem não foi possível.

---

## Aviso de conteúdo

Este material cita **nomes de membros da diretoria** e documenta erros associados a eles (cargos
trocados, grafia incorreta de nomes e cursos), além de conter peças gráficas de autoria do CCU.
O repositório em que está hospedado é **público**. Se a intenção era circulação restrita, mova estes
arquivos para um repositório privado antes de compartilhar o link.
