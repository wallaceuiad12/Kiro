# Evento Decade × Liga Empreendedora · fatos confirmados

Contexto para qualquer peça de comunicação deste evento.

## Data

**26.10.2026 · 17H30 · Unicamp**, confirmado pela Diretoria de Marketing (Octávio).

O `Manual_Marca_Evento_Decade.pdf`, na p.1, traz 25.10.2026. **Essa data está
desatualizada**; vale 26.10. Não "corrigir" peças para 25.10.

## Logo da Liga em cor padrão, decisão que vale sobre o manual

O manual proíbe o amarelo da Liga (`#F5C518`) na arte oficial do evento em três pontos
distintos (p.2, p.5 e p.7), e manda os dois logos monocromáticos.

**A Diretoria de Marketing decidiu o contrário.** O logo da Liga entra na forma padrão,
preto e amarelo, igual ao do site e das outras publicações, em todas as peças do evento.
Consistência da marca do parceiro pesou mais que a regra do manual.

**Não reverter para monocromático sem combinar antes.** Se uma sessão futura encontrar o
amarelo nas peças e achar que é erro, não é.

As duas variantes oficiais da Liga são usadas conforme o fundo, e isso vem do próprio
material original:

| Fundo da peça | "LIGA" | Foguete, globo e "EMPREENDEDORA" |
|---|---|---|
| off-white `#F5F1EC` | preto `#211815` | amarelo `#F5C518` |
| preto `#0C0B09` | off-white `#FFFEFB` | amarelo `#F5C518` |

A cor fica **confinada ao logo da Liga**. Todo o resto da peça segue monocromático na
paleta da Decade, e isso é verificado peça por peça no pipeline. O lockup da Decade nunca
recebe cor.

Os ativos monocromáticos antigos continuam em `post3/assets/liga_lockup_black.png` e
`liga_lockup_offwhite.png`, caso a decisão mude.

## Paleta Decade

Preto `#000000` · Off-white `#F5F1EC` · Cinza claro `#A19E99` · Cinza médio `#514F4D` ·
Grafite `#343332`. **Sem cor de acento**, porque é a ausência de cor vibrante que dá a sobriedade
da marca.

Tons medidos nas peças reais: título `#040303`, corpo e kicker `#504D48`, motivo de barras
do fundo `#E9E5E0`; na versão escura, fundo `#0C0B09`, texto `#F4F1ED`, barras `#1A1917`.

## Quem lidera cada peça

Na arte oficial do evento e na comunicação institucional a **Decade lidera**, com serifada no título,
mono nos dados, Liga como assinatura de rodapé. Peças de mobilização de campus (stories,
panfleto, reels), a Liga lidera, e aí o amarelo e a Anton são liberados.

## Fundadores da Decade

O manual não os nomeia. Apurado em fontes públicas:

- **Vitor Olivier**: co-fundador e CEO; 12 anos de Nubank, de um dos primeiros engenheiros
  a CTO, saindo em agosto de 2025.
- **Felipe Meneses**: co-fundador e head de IA; primeiro brasileiro no Thiel Fellowship;
  fundou a Hyperplane, adquirida pelo Nubank em 2024.

Nenhuma fonte confirma presença deles no evento. Não afirmar isso em arte sem confirmação.

## Pipeline das peças

As artes ficam em `post3/`, geradas por HTML/CSS renderizado em Chromium headless, e **não
por IA generativa**, que erra acentuação em português e introduz cor. Para novas peças,
edite `variations.json` ou `carousel.json` e rode `node render.js`. Detalhes da grade e da
calibração tipográfica em `post3/README.md`.

O motivo de barras do fundo é o próprio símbolo da Decade ampliado (confirmado por
encaixe, IoU 0.914). Não redesenhe, use `assets/motif_tint_*.png`.
