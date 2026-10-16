#!/usr/bin/env python3
"""
Story 1080x1920 (9:16) do evento Open Bank · Decade x Liga Empreendedora.

Identidade Decade (Manual_Marca_Evento_Decade.pdf)
- fundo off-white #F5F1EC ou preto, sem amarelo na arte oficial do evento
- titulo em serif editorial (Playfair Display como aproximacao da serif Decade)
- dados e detalhes tecnicos em mono (JetBrains Mono)
- acento azul-marinho #233555, a cor-ponte entre as duas marcas
- logos monocromaticos lado a lado no rodape, com area de respiro

Assets em assets/ foram recortados do panfleto oficial (panfleto6.png) para
manter a mesma foto, o mesmo selo "nu EX-CTO DO NUBANK" e os mesmos logos.
Todo o conteudo fica entre y=210 e y=1680 para nao brigar com a interface
do Instagram (topo com avatar, base com a barra de resposta).

Uso:
    python gerar_story_open_bank.py
Saida:
    story-open-bank-offwhite.png   (principal)
    story-open-bank-preto.png      (variante)
"""

from pathlib import Path

import qrcode
from PIL import Image, ImageDraw, ImageFont

BASE = Path(__file__).parent
FONTS = BASE / "fonts"
ASSETS = BASE / "assets"

# ---------------------------------------------------------------- canvas
W, H = 1080, 1920          # story vertical 9:16
SC = 2                     # supersampling: renderiza em 2160x3840 e reduz
M = 80                     # margem lateral
LINK = "https://luma.com/wqw35sxf"

# ---------------------------------------------------------------- cores
OFFWHITE = (245, 241, 236)
BLACK = (11, 11, 11)
GRAPHITE = (52, 51, 50)
GREY = (140, 137, 132)
GREY_SOFT = (161, 158, 153)
NAVY = (35, 53, 85)
NAVY_LIGHT = (131, 150, 185)

SERIF = FONTS / "PlayfairDisplay[wght].ttf"
SERIF_IT = FONTS / "PlayfairDisplay-Italic[wght].ttf"
MONO = FONTS / "JetBrainsMono[wght].ttf"


def font(path, size, weight=400):
    f = ImageFont.truetype(str(path), size * SC)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f


def px(v):
    return int(round(v * SC))


# ---------------------------------------------------------------- helpers
def tracked(draw, xy, text, fnt, fill, tracking=0):
    x, y = px(xy[0]), px(xy[1])
    t = px(tracking)
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + t
    return (x - px(xy[0])) / SC


def tracked_width(draw, text, fnt, tracking=0):
    w = sum(draw.textlength(ch, font=fnt) for ch in text) + px(tracking) * (len(text) - 1)
    return w / SC


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        probe = (cur + " " + wd).strip()
        if draw.textlength(probe, font=fnt) / SC <= max_w:
            cur = probe
        else:
            if cur:
                lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def dotted(draw, y, x0, x1, color, dot=3, gap=9, thick=2):
    x = x0
    while x < x1:
        draw.rectangle([px(x), px(y), px(min(x + dot, x1)), px(y) + px(thick) - 1], fill=color)
        x += dot + gap


def rule(draw, y, x0, x1, color, thick=1):
    draw.rectangle([px(x0), px(y), px(x1), px(y) + px(thick) - 1], fill=color)


def cover(img, box_w, box_h, top_bias=0.05):
    """Preenche a caixa mantendo proporcao, crop centrado e enquadrado no rosto."""
    tw, th = px(box_w), px(box_h)
    r = max(tw / img.width, th / img.height)
    nw, nh = int(img.width * r + 0.5), int(img.height * r + 0.5)
    im = img.resize((nw, nh), Image.LANCZOS)
    left = (nw - tw) // 2
    top = int((nh - th) * top_bias)
    return im.crop((left, top, left + tw, top + th))


def paste_h(canvas, img, x, y, h, align="left", tint=None):
    """Cola com altura h (px de design). align=left|right em relacao a x."""
    hh = px(h)
    ww = int(hh * img.width / img.height + 0.5)
    im = img.resize((ww, hh), Image.LANCZOS)
    if tint is not None:
        solid = Image.new("RGBA", im.size, tint + (255,))
        solid.putalpha(im.getchannel("A"))
        im = solid
    xx = px(x) - ww if align == "right" else px(x)
    canvas.paste(im, (xx, px(y)), im if im.mode == "RGBA" else None)
    return ww / SC


def qr_block(link, size, pad, fg=BLACK, bg=OFFWHITE):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=16, border=0)
    q.add_data(link)
    q.make(fit=True)
    code = q.make_image(fill_color="black", back_color="white").convert("L")
    code = code.resize((px(size), px(size)), Image.NEAREST)
    frame = Image.new("RGB", (px(size + 2 * pad), px(size + 2 * pad)), bg)
    tile = Image.new("RGB", code.size, fg)
    frame.paste(tile, (px(pad), px(pad)), Image.eval(code, lambda v: 255 - v))
    return frame


# ---------------------------------------------------------------- arte
def build(variant="offwhite"):
    dark = variant == "preto"
    bg = BLACK if dark else OFFWHITE
    ink = OFFWHITE if dark else BLACK
    soft = GREY_SOFT if dark else GRAPHITE
    faint = (86, 84, 81) if dark else GREY_SOFT
    label_col = (120, 118, 114) if dark else GREY
    accent = NAVY_LIGHT if dark else NAVY
    block_bg = OFFWHITE if dark else BLACK
    block_ink = BLACK if dark else OFFWHITE
    block_soft = GREY if dark else GREY_SOFT

    canvas = Image.new("RGB", (W * SC, H * SC), bg)
    d = ImageDraw.Draw(canvas)

    f_eyebrow = font(MONO, 23, 600)
    f_t1 = font(SERIF, 120, 700)
    f_t2_it = font(SERIF_IT, 90, 500)
    f_t2 = font(SERIF, 90, 500)
    f_sub = font(MONO, 26, 400)
    f_label = font(MONO, 21, 600)
    f_data = font(MONO, 52, 600)
    f_note = font(MONO, 23, 400)
    f_meta = font(MONO, 20, 500)
    f_cap_it = font(SERIF_IT, 30, 500)
    f_cap = font(SERIF, 30, 500)
    f_cta = font(MONO, 42, 700)
    f_cta2 = font(MONO, 24, 400)
    f_nu = font(MONO, 22, 600)

    # ---- topo: acento + quem realiza
    d.rectangle([px(M), px(210), px(M + 84), px(210) + px(5) - 1], fill=accent)
    tracked(d, (M, 240), "A LIGA EMPREENDEDORA APRESENTA", f_eyebrow, accent, tracking=4.5)

    # ---- titulo
    d.text((px(M), px(296)), "Open Bank", font=f_t1, fill=ink)
    w_it = d.textlength("na ", font=f_t2_it)
    d.text((px(M), px(438)), "na ", font=f_t2_it, fill=ink)
    d.text((px(M) + w_it, px(438)), "Unicamp", font=f_t2, fill=ink)

    # ---- subtitulo
    sub = ("a Liga Empreendedora traz pra Unicamp uma conversa sobre "
           "open banking com quem construiu a engenharia do Nubank")
    y = 582
    for line in wrap(d, sub, f_sub, 790):
        d.text((px(M), px(y)), line, font=f_sub, fill=soft)
        y += 40
    dotted(d, 722, M, W - M, faint)

    # ---- bloco central: dados (esquerda) + retrato (direita)
    top = 760
    photo_x, photo_w, photo_h, bar_h = 556, W - M - 556, 486, 62

    photo = Image.open(ASSETS / "photo_clean.png").convert("RGB")
    canvas.paste(cover(photo, photo_w, photo_h), (px(photo_x), px(top)))
    if dark:
        d.rectangle([px(photo_x), px(top), px(photo_x + photo_w) - 1,
                     px(top + photo_h) - 1], outline=(58, 57, 55), width=px(1))

    # selo nu
    seal_bg = OFFWHITE if dark else BLACK
    seal_ink = BLACK if dark else OFFWHITE
    d.rectangle([px(photo_x), px(top + photo_h), px(photo_x + photo_w),
                 px(top + photo_h + bar_h)], fill=seal_bg)
    nu = Image.open(ASSETS / "nu_mark.png").convert("RGBA")
    nu_h = 21
    nu_w = nu_h * nu.width / nu.height
    seal_txt = "EX-CTO DO NUBANK"
    group = nu_w + 13 + tracked_width(d, seal_txt, f_nu, 2.4)
    gx = photo_x + (photo_w - group) / 2
    paste_h(canvas, nu, gx, top + photo_h + (bar_h - nu_h) / 2 - 1, nu_h, tint=seal_ink)
    tracked(d, (gx + nu_w + 13, top + photo_h + (bar_h - 29) / 2),
            seal_txt, f_nu, seal_ink, tracking=2.4)

    # coluna de dados
    tracked(d, (M, top + 4), "QUANDO  ·  ONDE", f_label, label_col, tracking=5)
    dy = top + 48
    for item in ("26.10", "17h30", "Unicamp"):
        d.text((px(M), px(dy)), item, font=f_data, fill=ink)
        dy += 68
    dy += 6
    d.text((px(M), px(dy)), "Coffee Break", font=f_note, fill=soft)
    d.text((px(M), px(dy + 32)), "incluso", font=f_note, fill=soft)

    dotted(d, top + 352, M, M + 300, faint)
    my = top + 382
    for line in ("↑  DECADE", "US$ 85 MI EM SEED,", "A MAIOR DA AMÉRICA LATINA"):
        tracked(d, (M, my), line, f_meta, label_col, tracking=1.6)
        my += 28

    # ---- legenda do convidado
    cap_y = top + photo_h + bar_h + 32
    nome, resto = "Vitor Olivier ", "· fundador da Decade"
    wn = d.textlength(nome, font=f_cap_it)
    wr = d.textlength(resto, font=f_cap)
    cx = px(W - M) - (wn + wr)
    d.text((cx, px(cap_y)), nome, font=f_cap_it, fill=ink)
    d.text((cx + wn, px(cap_y)), resto, font=f_cap, fill=ink)

    # ---- CTA + QR
    cta_y, cta_h = 1402, 152
    d.rectangle([px(M), px(cta_y), px(W - M), px(cta_y + cta_h)], fill=block_bg)
    tracked(d, (M + 42, cta_y + 36), "INSCREVA-SE", f_cta, block_ink, tracking=3)
    tracked(d, (M + 44, cta_y + 94), "vagas limitadas  →", f_cta2, block_soft, tracking=1.5)
    qs, qpad = 112, 12
    qr = qr_block(LINK, qs, qpad, fg=BLACK, bg=OFFWHITE)
    canvas.paste(qr, (px(W - M - 30) - qr.width,
                      px(cta_y + (cta_h - qs - 2 * qpad) / 2)))

    # ---- rodape: lockup dos dois logos
    foot = cta_y + cta_h + 48
    rule(d, foot, M, W - M, faint)
    liga = Image.open(ASSETS / ("liga_offwhite.png" if dark else "liga_black.png")).convert("RGBA")
    dec = Image.open(ASSETS / ("decade_offwhite.png" if dark else "decade_black.png")).convert("RGBA")
    paste_h(canvas, liga, M, foot + 38, 60)
    paste_h(canvas, dec, W - M, foot + 48, 38, align="right")

    print(f"[{variant}] conteudo termina em y={foot + 100} de {H}")
    return canvas.resize((W, H), Image.LANCZOS)


if __name__ == "__main__":
    for v, name in (("offwhite", "story-open-bank-offwhite.png"),
                    ("preto", "story-open-bank-preto.png")):
        img = build(v)
        img.save(BASE / name)
        print("ok", name, img.size)
