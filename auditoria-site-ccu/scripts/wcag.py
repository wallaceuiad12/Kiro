#!/usr/bin/env python3
"""Calcula contraste WCAG dos pares de cor reais da paleta do CCU."""

def lum(rgb):
    def f(c):
        c = c / 255.0
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = [f(x) for x in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

def hx(rgb):
    return "#%02X%02X%02X" % rgb

P = {
    "off-white (color_11/0)": (251, 250, 250),
    "branco (color_26/31)": (255, 255, 255),
    "quase-preto (color_15)": (24, 24, 24),
    "preto puro": (0, 0, 0),
    "preto apps (#080808)": (8, 8, 8),
    "vermelho marca (color_18)": (193, 39, 45),
    "vermelho claro (color_2)": (196, 76, 76),
    "vermelho escuro (color_19)": (129, 26, 30),
    "rosa (color_17)": (214, 128, 132),
    "rosa claro (color_16)": (234, 172, 174),
    "cinza 194 (color_7)": (194, 194, 194),
    "cinza 137 (color_8)": (137, 137, 137),
    "cinza 81 (color_9)": (81, 81, 81),
    "cinza 55 (color_24)": (55, 55, 55),
}

PAIRS = [
    ("quase-preto (color_15)", "off-white (color_11/0)", "corpo de texto padrao (font_N)"),
    ("vermelho marca (color_18)", "off-white (color_11/0)", "titulo/destaque vermelho sobre fundo claro"),
    ("branco (color_26/31)", "vermelho marca (color_18)", "texto branco em botao vermelho"),
    ("quase-preto (color_15)", "vermelho marca (color_18)", "texto escuro sobre vermelho"),
    ("vermelho marca (color_18)", "branco (color_26/31)", "vermelho sobre branco puro"),
    ("cinza 137 (color_8)", "off-white (color_11/0)", "texto secundario cinza medio"),
    ("cinza 194 (color_7)", "off-white (color_11/0)", "texto/borda cinza claro"),
    ("cinza 81 (color_9)", "off-white (color_11/0)", "texto secundario cinza escuro"),
    ("cinza 55 (color_24)", "off-white (color_11/0)", "texto secundario"),
    ("rosa (color_17)", "off-white (color_11/0)", "rosa sobre fundo claro"),
    ("rosa claro (color_16)", "off-white (color_11/0)", "rosa claro sobre fundo claro"),
    ("vermelho claro (color_2)", "off-white (color_11/0)", "vermelho claro sobre fundo claro"),
    ("branco (color_26/31)", "vermelho escuro (color_19)", "branco sobre vermelho escuro"),
    ("off-white (color_11/0)", "quase-preto (color_15)", "texto claro em fundo escuro"),
]

print(f"{'PAR':<62} {'RATIO':>7}  {'AA txt':>7} {'AA 18pt+':>9} {'AAA':>5}")
print("-" * 100)
for fg, bg, uso in PAIRS:
    r = ratio(P[fg], P[bg])
    aa = "PASSA" if r >= 4.5 else "FALHA"
    aal = "PASSA" if r >= 3.0 else "FALHA"
    aaa = "PASSA" if r >= 7.0 else "FALHA"
    label = f"{hx(P[fg])} sobre {hx(P[bg])}"
    print(f"{label:<28}{uso:<34} {r:>6.2f}:1  {aa:>7} {aal:>9} {aaa:>5}")
