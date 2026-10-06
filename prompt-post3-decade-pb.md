# Prompt — Post 3 Decade × Liga (versão preto e branco)

Fontes: `Manual_Marca_Evento_Decade.pdf` (7 páginas, Diretoria de Marketing · Octávio),
`Post1 - Inicio.jpeg` e `SaveClip.App_838195465....jpg`.

---

## ⚠️ Dois achados antes de gerar

**1. O amarelo da Liga no rodapé viola o manual.** As duas peças existentes trazem o logo
da Liga em amarelo `#F5C518`. O manual é explícito em três pontos diferentes:

- p.2 — *NUNCA jogar o amarelo da Liga sobre a estética serifada da Decade*
- p.5 — fundo preto: ambos os logos off-white/monocromático; fundo off-white: ambos preto/monocromático
- p.7 — *o amarelo nunca entra na arte oficial do evento*

Ou seja: o pedido de versão em preto e branco **corrige** uma inconformidade já existente.
O P&B não é só estética — é o que o manual manda.

**2. Conflito de data.** O manual (p.1) diz **25.10.2026**. As duas peças publicadas dizem
**26.10 · 17H30**. Precisa confirmar qual está certa antes de rodar qualquer peça nova.

---

## Identidade extraída (para ancorar o prompt)

| Elemento | Especificação |
|---|---|
| Paleta Decade | Preto `#000000` · Off-white `#F5F1EC` · Cinza claro `#A19E99` · Cinza médio `#514F4D` · Grafite `#343332` |
| Cor de acento | **Nenhuma.** A ausência de cor vibrante é o que dá a sobriedade premium |
| Título | Serif editorial de alto contraste (Playfair Display como aproximação da proprietária) |
| Dados/números | Mono, caixa alta, entreletra aberta |
| Fundo | Motivo de barras verticais do símbolo, superescalado, contraste baixíssimo |
| Lockup | Decade primeiro, linha fina divisória, Liga depois — respiro generoso |
| Tipo de peça | "Post de infos do evento" → **Decade lidera · fundo off-white · serif Decade · mono nos dados** (p.6) |

---

## Prompt principal — Nano Banana / Gemini / ChatGPT

**Anexe as duas peças existentes como referência** antes de enviar.

```
Use as duas imagens anexadas como referência da identidade visual do evento Decade × Liga
Empreendedora. Crie a TERCEIRA peça da sequência, em PRETO E BRANCO ESTRITO.

IDENTIDADE A PRESERVAR
- Fundo off-white #F5F1EC com o motivo de barras verticais do símbolo Decade
  superescalado, em contraste baixíssimo (quase imperceptível), como marca d'água.
- Símbolo Decade (marca circular de barras verticais) centralizado no topo, em preto.
- Título em serif editorial de alto contraste, duas linhas, a segunda em itálico.
- Texto de apoio em serif regular, cinza médio #514F4D.
- Dados e horários em mono caixa alta com entreletra bem aberta.
- Rodapé: lockup Decade + linha fina vertical + logo Liga.
- Composição centralizada, simétrica, com respiro generoso nas quatro margens.

REGRA CROMÁTICA — OBRIGATÓRIA
- Monocromático absoluto: apenas preto, off-white e os cinzas #A19E99 / #514F4D / #343332.
- O logo da Liga Empreendedora deve entrar em PRETO MONOCROMÁTICO, nunca em amarelo.
- Zero cor de acento. Nenhum amarelo, nenhum azul, nenhum degradê colorido.

CONTEÚDO DA PEÇA
- Linha superior (mono): UNICAMP · OUTUBRO
- Título: [TÍTULO — ex: "o que vai acontecer" / "a programação"]
- Apoio: [TEXTO DE APOIO]
- Dados (mono): [DATA] · 17H30 · UNICAMP
- CTA: [CTA — ex: "inscreva-se pelo link na bio"]

FORMATO
- 4:5 vertical (1080 × 1350), mesma proporção das peças de referência.

RESTRIÇÕES
- Não criar elementos gráficos ausentes nas referências.
- Não alterar proporções nem recortes dos logos.
- Português do Brasil, grafia correta, acentuação correta.
- Área de segurança nas bordas para não cortar em nenhum crop do Instagram.
```

---

## Variante Midjourney

Midjourney não compõe texto com precisão. Gere só o fundo e aplique a tipografia no Figma.

```
minimal editorial poster background, off-white #F5F1EC, oversized vertical bar motif in
barely-visible tonal contrast, monochrome, no color, premium sober editorial design,
generous negative space centered for typography
--ar 4:5 --sref [URL_DO_POST1] --sw 100 --style raw
--no text, letters, words, numbers, logo, watermark, yellow, color
```

`--no yellow, color` é essencial aqui: trava a conformidade com o manual.

---

## O que ainda falta

| # | Pendência | Como resolver |
|---|---|---|
| 1 | **Conteúdo dos 2 áudios do Octávio** (23s e 42s) | Preciso em texto — não processo áudio |
| 2 | Título, apoio e CTA desta peça | Vem do áudio |
| 3 | Data correta: 25.10 ou 26.10? | Confirmar com o Octávio |
| 4 | Versão monocromática oficial do logo da Liga | Manual p.7 registra como pendência: *obter PNG transparente nas versões clara e escura* |
| 5 | Fonte serif oficial | Manual p.7: ainda não definida, Playfair é aproximação |

Os campos em `[CORCHETES]` ficaram em aberto de propósito. Preenchê-los por suposição
arriscaria contrariar a linha que o Octávio definiu nos áudios.
