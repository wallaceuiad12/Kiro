#!/usr/bin/env python3
"""
Gera a logo do "Processo Trainee 2026.2" do Clube de Consultoria Universitario (CCU),
derivada da identidade visual da logo "Prep4Consulting 2026.1".

Elementos herdados da logo original (medidos em ppt/media/image15.png, 914x435):
  - vermelho da marca ................ #C1272D
  - texto ............................ branco #FFFFFF
  - bloco vermelho solido fechando a 1a linha
  - regua vermelha logo abaixo da linha de base da 1a linha, ate a borda do bloco
  - 2a linha como palavra dominante, em corpo maior
  - "CCU" em corpo pequeno, encaixado embaixo e a direita da palavra dominante
  - selo do semestre: retangulo de cantos arredondados com contorno vermelho,
    digitos brancos e o ultimo digito (o semestre) em vermelho

Tipografia: Trirong Bold (serifa) + Kanit Bold (numerais) -- mesma dupla de
superfamilia da Cadson Demak; Kanit ja e usada na apresentacao.

A composicao e montada em unidades arbitrarias e depois normalizada
(crop no ink + escala) para a proporcao final de 914x435 (2.101:1), do mesmo
jeito que a logo original: sangrando na largura e com uma folga embaixo.
"""

import os
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# ----------------------------------------------------------------------------
# marca
# ----------------------------------------------------------------------------
RED = (193, 39, 45, 255)      # #C1272D -- o mesmo vermelho do tema da apresentacao
WHITE = (255, 255, 255, 255)

# as duas fontes (OFL, Cadson Demak). Baixa na primeira execucao se faltarem;
# use FONT_DIR=... para apontar para uma pasta local que ja as tenha.
FONT_DIR = Path(os.environ.get("FONT_DIR", "fonts"))
FONT_URLS = {
    "Trirong-Bold.ttf":
        "https://github.com/google/fonts/raw/main/ofl/trirong/Trirong-Bold.ttf",
    "Kanit-Bold.ttf":
        "https://github.com/google/fonts/raw/main/ofl/kanit/Kanit-Bold.ttf",
}


def font_path(name):
    p = FONT_DIR / name
    if not p.exists():
        FONT_DIR.mkdir(parents=True, exist_ok=True)
        print(f"baixando {name} ...")
        urllib.request.urlretrieve(FONT_URLS[name], p)
    return str(p)


SERIF = font_path("Trirong-Bold.ttf")       # serifa do logotipo
NUMERALS = font_path("Kanit-Bold.ttf")      # numerais do selo do semestre

OUT_W, OUT_H = 1828, 870      # 2x de 914x435, a proporcao da logo original
BOTTOM_SLACK = 0.085          # folga inferior (34/399 na logo original)

# ----------------------------------------------------------------------------
# proporcoes da composicao (unidades arbitrarias; a normalizacao cuida da escala)
# ----------------------------------------------------------------------------
LINE2_TEXT = "Trainee"
LINE2_WIDTH = 1000.0          # referencia de largura da palavra dominante

LINE1_TEXT = "Processo"
LINE1_RATIO = 0.82            # (texto + folga + bloco) / largura da 2a linha
BLOCK_GAP_R = 0.028           # folga texto->bloco, relativa a LINE2_WIDTH
BLOCK_W_R = 0.72              # largura do bloco (rel. ao cap da 1a linha) -- 104/146 na original
BLOCK_TALLER = 1.12           # bloco e 12% mais alto que a caixa alta da 1a linha

RULE_OFFSET_R = 0.030         # base da 1a linha -> topo da regua (rel. ao cap da 1a linha)
RULE_H_R = 0.070              # espessura da regua (rel. ao cap da 1a linha)
LINE_GAP_R = 0.105            # base da regua -> topo da 2a linha (rel. ao cap da 2a linha)

CCU_TEXT = "CCU"
# o CCU fica encaixado DENTRO da largura da 2a linha (alinhado a direita por ela),
# logo abaixo da linha de base -- como na logo original, aninhado sob "ting".
CCU_CAP_R = 0.240             # rel. ao cap da 2a linha
CCU_DROP_R = 0.045            # base da 2a linha -> topo do CCU (rel. ao cap da 2a linha)

BADGE_HEAD, BADGE_TAIL = "2026.", "2"   # "2" = semestre, em vermelho
# o selo e proporcional a LARGURA do logotipo (e nao ao cap da 2a linha), que e
# como a proporcao se mantem fiel a original: 305/912 = 0.334.
BADGE_W_R = 0.345             # largura do selo (rel. a LINE2_WIDTH)
BADGE_INDENT_R = 0.105        # recuo do selo (rel. a LINE2_WIDTH)
BADGE_TOP_GAP_R = 0.150       # base da 2a linha -> topo do selo (rel. ao cap da 2a linha)
BADGE_PAD_X_R = 0.385         # folga interna horizontal (rel. a altura dos digitos)
BADGE_PAD_Y_R = 0.190         # folga interna vertical  (rel. a altura dos digitos)
BADGE_STROKE_R = 0.082        # espessura do contorno   (rel. a altura dos digitos)


# ----------------------------------------------------------------------------
# tipografia
# ----------------------------------------------------------------------------
def _load(path, size):
    return ImageFont.truetype(path, max(1, int(size)))


def font_for_cap_height(path, cap_px, ref="H"):
    lo, hi = 4.0, 6000.0
    for _ in range(60):
        mid = (lo + hi) / 2
        b = _load(path, mid).getbbox(ref)
        if (b[3] - b[1]) < cap_px:
            lo = mid
        else:
            hi = mid
    return _load(path, lo)


def font_for_width(path, text, width_px):
    lo, hi = 4.0, 6000.0
    for _ in range(60):
        mid = (lo + hi) / 2
        b = _load(path, mid).getbbox(text)
        if (b[2] - b[0]) < width_px:
            lo = mid
        else:
            hi = mid
    return _load(path, lo)


def ink(text, font):
    return font.getbbox(text)


def ink_size(text, font):
    b = font.getbbox(text)
    return b[2] - b[0], b[3] - b[1]


def draw_ink_at(draw, x_left, y_top, text, font, fill):
    """Ancora o canto superior-esquerdo do *ink* de `text` em (x_left, y_top)."""
    b = font.getbbox(text)
    draw.text((x_left - b[0], y_top - b[1]), text, font=font, fill=fill)
    return b[2] - b[0], b[3] - b[1]


# ----------------------------------------------------------------------------
# composicao
# ----------------------------------------------------------------------------
def compose(verbose=False):
    """Desenha a logo em tamanho natural numa tela folgada e devolve a imagem."""
    pad = 400
    canvas = Image.new("RGBA", (int(LINE2_WIDTH) + 2 * pad, int(LINE2_WIDTH) + 2 * pad),
                       (0, 0, 0, 0))
    d = ImageDraw.Draw(canvas)

    x0, y0 = pad, pad

    # ---- 2a linha: palavra dominante -------------------------------------
    f2 = font_for_width(SERIF, LINE2_TEXT, LINE2_WIDTH)
    w2, h2 = ink_size(LINE2_TEXT, f2)
    cap2 = ink("T", f2)[3] - ink("T", f2)[1]

    # ---- 1a linha: texto + bloco vermelho --------------------------------
    # o bloco e quadrado com o lado = caixa alta da 1a linha; resolve-se em
    # ponto fixo porque a largura do bloco depende do corpo da 1a linha.
    line1_total = LINE1_RATIO * LINE2_WIDTH
    block_gap = BLOCK_GAP_R * LINE2_WIDTH
    cap1 = 0.5 * line1_total
    for _ in range(60):
        text_w = line1_total - block_gap - BLOCK_W_R * cap1
        f1 = font_for_width(SERIF, LINE1_TEXT, text_w)
        cap1 = ink("P", f1)[3] - ink("P", f1)[1]
    text_w = line1_total - block_gap - BLOCK_W_R * cap1
    f1 = font_for_width(SERIF, LINE1_TEXT, text_w)
    w1, h1 = ink_size(LINE1_TEXT, f1)
    cap1 = ink("P", f1)[3] - ink("P", f1)[1]

    rule_off = RULE_OFFSET_R * cap1
    rule_h = max(2.0, RULE_H_R * cap1)

    # geometria vertical
    line1_top = y0
    line1_baseline = line1_top + cap1          # "Processo" nao tem ascendente alem do cap
    rule_top = line1_baseline + rule_off
    rule_bottom = rule_top + rule_h

    block_w = BLOCK_W_R * cap1
    block_h = cap1 * BLOCK_TALLER + rule_off + rule_h
    block_bottom = rule_bottom
    block_top = block_bottom - block_h

    line1_right = x0 + line1_total

    # regua + bloco
    d.rectangle([x0, rule_top, line1_right, rule_bottom - 1], fill=RED)
    d.rectangle([line1_right - block_w, block_top, line1_right, block_bottom - 1], fill=RED)
    draw_ink_at(d, x0, line1_top, LINE1_TEXT, f1, WHITE)

    # 2a linha
    line2_top = rule_bottom + LINE_GAP_R * cap2
    draw_ink_at(d, x0, line2_top, LINE2_TEXT, f2, WHITE)
    line2_bottom = line2_top + h2              # "Trainee" nao tem descendente
    line2_right = x0 + w2

    # ---- CCU, aninhado sob a ponta da 2a linha ---------------------------
    fccu = font_for_cap_height(SERIF, CCU_CAP_R * cap2, ref="C")
    wccu, hccu = ink_size(CCU_TEXT, fccu)
    ccu_x = line2_right - wccu                 # alinhado a direita por "Trainee"
    ccu_top = line2_bottom + CCU_DROP_R * cap2
    draw_ink_at(d, ccu_x, ccu_top, CCU_TEXT, fccu, WHITE)

    # ---- selo do semestre ------------------------------------------------
    # resolve a altura dos digitos para o selo fechar na largura alvo
    badge_w = BADGE_W_R * LINE2_WIDTH
    digit_h = badge_w / 4.0
    for _ in range(60):
        f = font_for_cap_height(NUMERALS, digit_h, ref="0")
        dw = ink_size(BADGE_HEAD, f)[0] + ink_size(BADGE_TAIL, f)[0]
        digit_h = badge_w / ((dw / digit_h) + 2 * BADGE_PAD_X_R)
    fnum = font_for_cap_height(NUMERALS, digit_h, ref="0")
    wh, hh = ink_size(BADGE_HEAD, fnum)
    wt, ht = ink_size(BADGE_TAIL, fnum)
    pad_x, pad_y = BADGE_PAD_X_R * digit_h, BADGE_PAD_Y_R * digit_h
    stroke = max(2.0, BADGE_STROKE_R * digit_h)

    badge_w = wh + wt + 2 * pad_x
    badge_h = digit_h + 2 * pad_y
    badge_x0 = x0 + BADGE_INDENT_R * LINE2_WIDTH
    badge_y0 = line2_bottom + BADGE_TOP_GAP_R * cap2

    d.rounded_rectangle([badge_x0, badge_y0, badge_x0 + badge_w, badge_y0 + badge_h],
                        radius=badge_h / 2, outline=RED, width=int(round(stroke)))
    nx, ny = badge_x0 + pad_x, badge_y0 + pad_y
    adv, _ = draw_ink_at(d, nx, ny, BADGE_HEAD, fnum, WHITE)
    draw_ink_at(d, nx + adv, ny, BADGE_TAIL, fnum, RED)

    if verbose:
        print(f"  cap1={cap1:.1f} (corpo {f1.size})  cap2={cap2:.1f} (corpo {f2.size})  "
              f"cap1/cap2={cap1 / cap2:.2f}")
        print(f"  1a linha: texto={w1:.0f} bloco={block_w:.0f} total={line1_total:.0f}")
        print(f"  2a linha: {w2:.0f} + CCU {wccu:.0f}")
        print(f"  selo: {badge_w:.0f}x{badge_h:.0f}  digitos={digit_h:.0f}")

    return canvas


def build(verbose=False):
    """Compoe, recorta no ink e normaliza para OUT_W x OUT_H."""
    raw = compose(verbose=verbose)
    box = raw.getbbox()                       # bbox do ink (alpha > 0)
    art = raw.crop(box)

    # a arte sangra na largura; sobra uma folga embaixo, como na logo original
    usable_h = OUT_H * (1.0 - BOTTOM_SLACK)
    scale = min(OUT_W / art.width, usable_h / art.height)
    tw, th = max(1, int(round(art.width * scale))), max(1, int(round(art.height * scale)))
    art = art.resize((tw, th), Image.LANCZOS)

    out = Image.new("RGBA", (OUT_W, OUT_H), (0, 0, 0, 0))
    out.alpha_composite(art, ((OUT_W - tw) // 2, 0))
    if verbose:
        print(f"  ink {box[2] - box[0]}x{box[3] - box[1]} -> {tw}x{th} em {OUT_W}x{OUT_H}")
    return out


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "logo-processo-trainee-2026-2.png"
    im = build(verbose=True)
    im.save(out)
    print("gravado:", out, im.size)
