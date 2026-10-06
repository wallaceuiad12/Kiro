"""
Extrai o motivo de barras verticais do fundo do Post1 como mascara reutilizavel.

Estrategia:
 1. mascara tonal do motivo  (fundo #F5F1EC = lum 241, motivo #E9E5E0 = lum 229)
 2. remove o halo de anti-aliasing do texto, dilatando a mascara de texto
 3. preenche cada coluna do topo ao fim do motivo -> recupera o que estava sob o texto
    (as barras sao verticais e continuas, logo o preenchimento por coluna e exato,
     e as pontas arredondadas se preservam porque cada coluna tem seu proprio limite)
"""
from PIL import Image, ImageFilter
import numpy as np

im = Image.open("../Post1 - Inicio.jpeg").convert("RGB")
arr = np.asarray(im).astype(float)
lum = arr.mean(axis=2)
H, W = lum.shape

# 1. motivo: mais escuro que o fundo, mas muito mais claro que o texto
motif = (lum > 205) & (lum < 236)

# 2. remove halo do texto/logos
text = (lum < 180).astype(np.uint8) * 255
text_img = Image.fromarray(text, "L").filter(ImageFilter.MaxFilter(17))
text_dil = np.asarray(text_img) > 0
motif = motif & ~text_dil

# 3. perfil de topo e base por coluna
top = np.full(W, -1, dtype=float)
bot = np.full(W, -1, dtype=float)
for x in range(W):
    ys = np.nonzero(motif[:, x])[0]
    if len(ys) < 200:         # coluna sem barra de verdade
        continue
    top[x], bot[x] = ys.min(), ys.max()

# 3b. mediana ao longo de x remove os fiapos verticais deixados pelo texto,
#     preservando as pontas arredondadas (que variam suavemente entre colunas)
def median_profile(p, k=61):
    out = p.copy()
    valid = p >= 0
    for x in range(W):
        if not valid[x]:
            continue
        lo, hi = max(0, x - k // 2), min(W, x + k // 2 + 1)
        win = p[lo:hi][valid[lo:hi]]
        if len(win):
            out[x] = np.median(win)
    return out

top = median_profile(top)
bot = median_profile(bot)

# 4. reconstroi as barras a partir dos perfis suavizados
filled = np.zeros_like(motif)
for x in range(W):
    if top[x] < 0:
        continue
    filled[int(round(top[x])):int(round(bot[x])) + 1, x] = True

print(f"cobertura antes do preenchimento: {motif.mean()*100:5.1f}%")
print(f"cobertura depois:                 {filled.mean()*100:5.1f}%")

# suaviza a borda para nao serrilhar ao reescalar
a8 = (filled * 255).astype(np.uint8)
a8 = np.asarray(Image.fromarray(a8, "L").filter(ImageFilter.GaussianBlur(0.6)))

# variantes: tom claro (sobre off-white) e tom escuro (sobre preto)
VARIANTS = {
    "light": (233, 229, 224),   # #E9E5E0 medido no original
    "dark":  (26, 26, 26),      # barra levemente acima do preto, p/ a peca escura
}
for name, rgb in VARIANTS.items():
    canvas = np.zeros((H, W, 4), dtype=np.uint8)
    canvas[:, :, 0], canvas[:, :, 1], canvas[:, :, 2] = rgb
    canvas[:, :, 3] = a8
    Image.fromarray(canvas).save(f"assets/motif_{name}.png")
    print(f"assets/motif_{name}.png  {W}x{H}  rgb={rgb}")

# relatorio das barras (apenas informativo)
colhas = filled.any(axis=0)
runs, inb = [], False
for x in range(W):
    if colhas[x] and not inb:
        s, inb = x, True
    elif not colhas[x] and inb:
        runs.append((s, x)); inb = False
if inb:
    runs.append((s, W))
print(f"\n{len(runs)} grupos de barras detectados:")
for s, e in runs:
    col = filled[:, s:e]
    ys = np.nonzero(col.any(axis=1))[0]
    print(f"  x {s:4d}-{e:4d} (w={e-s:3d})  y {ys.min():4d}-{ys.max():4d}")
