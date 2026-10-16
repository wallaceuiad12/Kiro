"""
Compara as faixas de tinta da replica renderizada com o Post1 original.

O original e 1280x1600; a replica e 1080x1350 (mesmo 4:5). As faixas do original
sao convertidas pelo fator 1080/1280 = 0.84375 para ficarem comparaveis.
"""
from PIL import Image
import numpy as np
import sys

f = 1080 / 1280

# faixas de tinta medidas no Post1 original, ja convertidas para 1080x1350
TARGETS = [
    ("mono topo",    118, 141),
    ("headline L1",  572, 696),
    ("headline L2",  700, 803),
    ("corpo L1",     891, 925),
    ("corpo L2",     954, 995),
    ("corpo L3",    1015, 1049),
    ("data mono",   1119, 1146),
    ("rodape",      1427, 1505),
]

path = sys.argv[1] if len(sys.argv) > 1 else "out/v0-replica-post1@2x.png"
im = Image.open(path).convert("RGB")
if im.size != (1080, 1350):
    im = im.resize((1080, 1350), Image.LANCZOS)
lum = np.asarray(im).astype(float).mean(axis=2)

# faixas escuras da replica
dark = lum < 150
rows = dark.sum(axis=1)
bands, inb = [], False
for y, v in enumerate(rows):
    if v > 3 and not inb:
        s, inb = y, True
    elif v <= 3 and inb:
        if y - s > 4:
            bands.append((s, y))
        inb = False
if inb:
    bands.append((s, len(rows)))

print(f"arquivo: {path}\n")
print(f"{'bloco':14s} {'alvo (1080)':>14s} {'medido':>14s} {'desvio':>10s}")
print("-" * 56)

for (label, a, b), m in zip(TARGETS, bands):
    ta, tb = a * f, b * f
    d_top = m[0] - ta
    d_bot = m[1] - tb
    flag = "ok" if abs(d_top) <= 4 and abs(d_bot) <= 6 else "AJUSTAR"
    print(f"{label:14s} {ta:6.0f}-{tb:<7.0f} {m[0]:6d}-{m[1]:<7d} "
          f"{d_top:+5.0f}/{d_bot:+5.0f}  {flag}")

if len(bands) != len(TARGETS):
    print(f"\n! numero de faixas difere: alvo {len(TARGETS)}, medido {len(bands)}")
    print("  faixas medidas:", bands)
