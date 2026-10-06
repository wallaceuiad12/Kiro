"""
Extrai os ativos de marca do Post1 em versoes monocromaticas transparentes.

O Post1 tem DOIS tons de fundo: o off-white #F5F1EC e o tom do motivo de barras
#E9E5E0 (o simbolo central cai justamente sobre uma barra). Por isso o alfa e
calculado pela distancia ao fundo MAIS PROXIMO dos dois, o que evita o halo cinza
e ao mesmo tempo captura o amarelo #F5C518 da Liga -- que o manual proibe na arte
oficial do evento e que aqui e convertido para preto chapado.
"""
from PIL import Image
import numpy as np
import os

SRC = "../Post1 - Inicio.jpeg"
OUT = "assets"
BG1 = np.array([245, 241, 236], dtype=float)   # off-white da marca
BG2 = np.array([233, 229, 224], dtype=float)   # tom do motivo de barras
PAD = 4

# bbox exatas, medidas por mascara de tinta
BOXES = {
    "symbol":        (599, 420, 681, 497),
    "decade_lockup": (362, 1453, 623, 1505),
    "liga_lockup":   (728, 1427, 917, 1505),
}

os.makedirs(OUT, exist_ok=True)
arr = np.asarray(Image.open(SRC).convert("RGB")).astype(float)

for name, (x0, y0, x1, y1) in BOXES.items():
    sub = arr[y0 - PAD:y1 + PAD, x0 - PAD:x1 + PAD]

    d1 = np.sqrt(((sub - BG1) ** 2).sum(axis=2))
    d2 = np.sqrt(((sub - BG2) ** 2).sum(axis=2))
    dist = np.minimum(d1, d2)

    alpha = np.clip((dist - 25.0) / 85.0, 0.0, 1.0)
    alpha[alpha < 0.10] = 0.0
    alpha[alpha > 0.90] = 1.0

    a8 = (alpha * 255).astype(np.uint8)
    h, w = a8.shape

    for variant, rgb in (("black", (0, 0, 0)), ("offwhite", (245, 241, 236))):
        canvas = np.zeros((h, w, 4), dtype=np.uint8)
        canvas[:, :, 0], canvas[:, :, 1], canvas[:, :, 2] = rgb
        canvas[:, :, 3] = a8
        Image.fromarray(canvas).save(f"{OUT}/{name}_{variant}.png")

    semi = ((a8 > 10) & (a8 < 245)).sum() / max((a8 > 10).sum(), 1) * 100
    print(f"{name:15s} {w:4d}x{h:3d}px   opacos {(a8>245).mean()*100:5.1f}%"
          f"   borda_suave {semi:4.1f}%")

print("\nativos monocromaticos gerados em", os.path.abspath(OUT))
