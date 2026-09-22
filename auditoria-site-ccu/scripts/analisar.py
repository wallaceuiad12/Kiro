#!/usr/bin/env python3
"""Diagnostica a qualidade real de cada foto antes de processar."""
from PIL import Image
import numpy as np, glob, os

def laplacian_var(im):
    """Variancia do laplaciano: proxy de nitidez. Maior = mais nitido."""
    g = np.asarray(im.convert("L"), dtype=float)
    k = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=float)
    # convolucao manual (sem scipy)
    h, w = g.shape
    out = np.zeros((h - 2, w - 2))
    for dy in range(3):
        for dx in range(3):
            if k[dy, dx]:
                out += k[dy, dx] * g[dy:h - 2 + dy, dx:w - 2 + dx]
    return out.var()

def stats(f):
    im = Image.open(f)
    a = np.asarray(im.convert("RGB"), dtype=float)
    g = np.asarray(im.convert("L"), dtype=float)
    return dict(
        nome=os.path.basename(f), w=im.width, h=im.height,
        kb=os.path.getsize(f) / 1024,
        bpp=os.path.getsize(f) * 8 / (im.width * im.height),   # bits por pixel: <1 = muito comprimido
        brilho=g.mean(), contraste=g.std(),
        p1=np.percentile(g, 1), p99=np.percentile(g, 99),      # faixa tonal usada
        satur=(a.max(axis=2) - a.min(axis=2)).mean(),
        nitidez=laplacian_var(im),
    )

print(f"{'FOTO':<34}{'DIMENSAO':>11}{'KB':>7}{'bpp':>6}{'BRILHO':>8}{'CONTR':>7}"
      f"{'FAIXA':>10}{'SATUR':>7}{'NITIDEZ':>9}")
print("-" * 100)
rows = []
for f in sorted(glob.glob("/projects/sandbox/fotos/*.jpg")):
    if "melhorada" in f or "wix" in f:
        continue
    s = stats(f)
    rows.append(s)
    print(f"{s['nome'][:33]:<34}{s['w']}x{s['h']:<6}{s['kb']:>7.0f}{s['bpp']:>6.2f}"
          f"{s['brilho']:>8.0f}{s['contraste']:>7.0f}"
          f"{int(s['p1'])}-{int(s['p99']):<6}{s['satur']:>7.0f}{s['nitidez']:>9.0f}")

print("\nLeitura:")
print("  bpp < 1.0      -> JPEG muito comprimido, tem artefato de bloco")
print("  faixa longe de 0-255 -> sobra range tonal: auto-levels ganha contraste real")
print("  nitidez < 200  -> imagem macia; nitidez > 800 -> ja bem definida")
print("  brilho < 90    -> subexposta (tipico de foto interna a noite)")
