# Post 3 — Decade × Liga Empreendedora · versão preto e branco

Quatro variações em `out/`, 1080×1350 (4:5), **monocromáticas estritas**.

| Arquivo | Variação | Fundo | Observação |
|---|---|---|---|
| `v1-infos-claro.png` | "o que vai acontecer." | off-white | **Canônica pelo manual** (p.6: post de infos → Decade lidera, fundo off-white) |
| `v2-infos-escuro.png` | mesma copy, invertida | preto | Só válida se tratada como *post de chamada* (p.6 permite preto ou off-white) |
| `v3-contagem-claro.png` | "faltam vinte dias." | off-white | ⚠️ Conteúdo datado — válido só em 06.10 |
| `v4-cta-claro.png` | "as inscrições estão abertas." + faixa de CTA | off-white | Faixa com 70% da largura, igual à do Post 2 |

Cada peça tem três saídas: `.png` (1080×1350), `.jpg` (qualidade 95, sem subamostragem
de croma — preserva a serifada fina) e `@2x.png` (2160×2700, para reaproveitar em impresso).

---

## Por que vetor e não IA generativa

Modelo de imagem erra acentuação em português, distorce o símbolo e introduz cor. Aqui
cada peça é HTML/CSS renderizado em Chromium headless com supersampling 2×, então:

- os hex saem exatamente como o manual especifica;
- o texto é texto de verdade — "inscrições", "está", "construído" sem deformação;
- o símbolo e os lockups são **recortados das peças originais**, não redesenhados.

## Conformidade com o manual

| Regra | Onde | Status |
|---|---|---|
| Paleta Decade sem cor de acento | p.4 | ✅ saturação máx. 11 (o próprio off-white `#F5F1EC`) |
| Amarelo nunca na arte oficial | p.2, p.7 | ✅ logo da Liga convertido para preto chapado |
| Fundo off-white → ambos os logos em preto | p.5 | ✅ |
| Fundo preto → ambos em off-white | p.5 | ✅ (v2) |
| Decade primeiro, Liga depois, linha fina | p.5 | ✅ mantida a ordem original |
| Serif no título, mono nos dados | p.4, p.6 | ✅ Playfair Display + JetBrains Mono |

As duas peças já publicadas trazem o logo da Liga em amarelo `#F5C518` (4.690 px
coloridos medidos no `Post1`), o que contraria p.2, p.5 e p.7. Estas versões corrigem isso.

---

## Como a identidade foi reconstruída

Nada foi estimado a olho. Tudo medido no `Post1 - Inicio.jpeg` (1280×1600) e convertido
para 1080×1350 pelo fator 0.84375:

**Cores medidas no núcleo dos glifos**

| Bloco | Medido | Palette do manual |
|---|---|---|
| Título | `#040303` | Preto `#000000` |
| Corpo e kicker | `#504D48` | Cinza médio `#514F4D` |
| Fundo | `#F5F1EC` | Off-white `#F5F1EC` |
| Motivo de barras | `#E9E5E0` | — |
| Peça escura: fundo | `#0C0B09` | Preto |
| Peça escura: texto | `#F4F1ED` | Off-white |

**O motivo do fundo é o próprio símbolo ampliado.** Descobri isso amplificando o contraste
do fundo 8× — a silhueta é a mesma elipse de barras. Busca de encaixe confirmou:
escala 1480×1370 no offset (−100, 110) sobre 1280×1600, **IoU = 0.914**. Usar o símbolo
como fonte do motivo elimina os artefatos que a extração tonal deixava onde havia texto.

**Tipografia calibrada por largura de linha**, não por chute. Ajustei o corpo até as
larguras renderizadas baterem com o original:

| Bloco | Corpo final | Erro de largura |
|---|---|---|
| Título | 99 px / entrelinha 108 px | −6 / +5 px |
| Corpo | 36 px / entrelinha 52 px | −1 / +2 / +1 px |
| Kicker mono | 26 px, entreletra 0.39em | +1 px |
| Data mono | 32 px, entreletra 0.20em | +3 px |

## Validação

`validacao-replica-vs-original.png` compara o `Post1` original com uma réplica gerada por
este mesmo pipeline. Todos os blocos caem dentro de **±1 px** na vertical:

```
mono topo   original  100-118   replica  100-118   +0/+0
simbolo     original  355-418   replica  355-419   +0/+1
headline    original  482-677   replica  482-672   +0/-5
corpo       original  752-884   replica  753-884   +1/+0
data mono   original  944-966   replica  944-967   +0/+1
```

Como a réplica reproduz o Post 1, a grade e a tipografia das peças novas estão corretas.

---

## Reproduzir

```bash
cd post3
pip3 install pillow numpy
npm i -D playwright && npx playwright install chromium

python3 extract_assets.py      # recorta símbolo e lockups, converte p/ monocromático
python3 extract_motif.py       # extrai o motivo de barras (diagnóstico)
python3 make_motif_tints.py    # gera o motivo a partir do símbolo
node render.js                 # renderiza todas as variações de variations.json
python3 measure.py             # confere o alinhamento contra o original
```

Para trocar copy, edite `variations.json` — `headline` aceita `<br>` e `<em>` (itálico).

---

## Notas técnicas

**Data oficial: 26.10.2026 · 17H30 · Unicamp**, confirmada pelo marketing. É o que está em
todas as peças. Vale corrigir o manual, cuja p.1 ainda traz 25.10.2026.

**Copy aprovada** sem a transcrição dos áudios — os textos são redação a partir dos fatos
do manual e das fontes públicas listadas adiante.

**O logo mono da Liga é derivado** do colorido do Post 1 por conversão de luminância, não é
o arquivo oficial. Quando o PNG oficial chegar nas versões clara e escura (manual p.7),
basta trocar `assets/liga_lockup_black.png` e `assets/liga_lockup_offwhite.png` e rodar
`node render.js` — nada mais muda.

**A serifada é Playfair Display**, a mesma aproximação que o manual adota (p.7) até a fonte
proprietária da Decade ser definida. Para trocar, substitua o arquivo em `assets/fonts/` e
recalibre os corpos com `measure.py`.

**A v3 tem contagem regressiva.** "faltam vinte dias" vale para 06.10.2026. Publicando em
outra data, ajuste o texto em `variations.json`.

---

# Carrossel — "o que é a Decade"

Evolução do Post 3, em `carrossel/`. Seis telas, 1080×1350, mesma identidade monocromática.
Visão geral em `carrossel/contato-6-telas.png`.

| Tela | Arquivo | Conteúdo |
|---|---|---|
| 01 | `01-capa.png` | "o que é a *Decade.*" — gancho dos US$ 85M + indicador de arraste |
| 02 | `02-o-que-e.png` | "inteligência humana *e artificial.*" — a tagline do manual (p.4) |
| 03 | `03-o-que-fazem.png` | "a sua vida financeira *num só lugar.*" — Open Finance + consultor sênior |
| 04 | `04-como-fazem.png` | "sem comissão. *sem conflito.*" — modelo por assinatura |
| 05 | `05-quem-fundou.png` | "*dois ex-Nubank.*" — Vitor Olivier e Felipe Meneses |
| 06 | `06-convite.png` | "a Decade vai estar *na Unicamp.*" — faixa de CTA + data |

`01-capa-escura.png` é uma capa alternativa em fundo preto, para quem preferir abrir o
carrossel com mais impacto e dar continuidade ao Post 2. O manual p.6 permite preto ou
off-white em post de chamada; as telas internas seguem off-white porque são conteúdo
institucional, onde a Decade lidera em off-white.

Navegação: o rótulo da seção vai no kicker em mono (`03 · O QUE FAZEM`) e o contador
`03 / 06` fica acima do rodapé. O lockup Decade + Liga aparece em **todas** as telas,
porque p.5 trata a segunda marca como assinatura de rodapé.

## Checagem

| Tela | Saturação máx. | Margem lateral mínima |
|---|---|---|
| todas | 11 (o off-white da marca) | 146 px |

## Fatos e fontes

O manual não traz nome de fundador. Em vez de inventar, apurei em fontes públicas —
os dois nomes aparecem de forma consistente em veículos independentes:

- **Vitor Olivier** — co-fundador e CEO; 12 anos de Nubank, de um dos primeiros engenheiros
  a CTO, saindo em agosto de 2025.
- **Felipe Meneses** — co-fundador e head de IA; primeiro brasileiro selecionado para o
  Thiel Fellowship; fundou a Hyperplane, adquirida pelo Nubank em 2024.
- **A empresa** — consultoria de patrimônio nativa em IA, São Paulo e San Francisco,
  26 pessoas entre engenheiros e consultores. Seed de US$ 85 milhões (a maior já levantada
  por uma startup latino-americana) com Greenoaks, Benchmark e Diffusion, mais Atlantico
  e Norte Ventures. Saiu do stealth em 4 de agosto de 2026.
- **O produto** — consolida contas pelo Open Finance (BTG Pactual, XP, Genial, C6),
  monitora carteira e gastos de forma contínua e dá acesso a um consultor humano sênior
  por WhatsApp, por assinatura mensal em vez de comissão por produto.

Fontes: [Business Wire](https://www.businesswire.com/news/home/20260804082552/en/Decade-Raises-$85M-in-Latin-Americas-Largest-Seed-Round-to-Create-a-New-Generation-of-Millionaires-with-AI) ·
[FinTech Futures](https://www.fintechfutures.com/fintech-start-ups/ex-nubank-execs-launch-ai-driven-wealth-manager-decade-with-85m) ·
[LatAm Republic](https://www.latamrepublic.com/decade-raises-us-85m-to-combine-ai-and-human-financial-advisors/) ·
[The Next Web](https://thenextweb.com/news/decade-85m-seed-ai-wealth-brazil-nubank) ·
[PYMNTS](https://www.pymnts.com/news/investment-tracker/2026/nubank-alum-launches-decade-to-give-money-an-ai-copilot/)

Conteúdo reescrito para conformidade com restrições de licenciamento.

## Notas do carrossel

A tela 06 diz "a Decade vai estar na Unicamp" e não nomeia quem comparece, porque nenhuma
fonte confirma presença dos fundadores no evento. Se Olivier ou Meneses forem confirmados,
é só nomear em `carousel.json`.

Preço da assinatura, número de funcionários e instituições conectadas ficaram **fora da
arte** por serem dados voláteis (referência de agosto/setembro de 2026). O que está nas
telas é estrutural, não numérico perecível.
