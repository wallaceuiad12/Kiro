"""
Gera o motivo de fundo a partir do SIMBOLO da Decade.

A analise de encaixe mostrou que o motivo de barras do fundo do Post1 e o proprio
simbolo ampliado (IoU 0.914 com escala 1480x1370 e offset -100,110 no canvas 1280x1600).
Usar o simbolo como fonte elimina os artefatos da extracao tonal e garante fidelidade.

Tons medidos nas pecas originais:
  claro -> #E9E5E0 sobre o off-white #F5F1EC
  escuro -> #1A1917 sobre o preto #0C0B09
"""
from PIL import Image
import numpy as np

alpha = Image.open("assets/symbol_black.png").split()[3]

TINTS = {
    "light": (233, 229, 224),   # #E9E5E0
    "dark":  (26, 25, 23),      # #1A1917
}

# renderiza em alta resolucao para nao serrilhar ao escalar no navegador
W, H = 2496, 2310   # 2x o tamanho de uso (1248x1155)
big = alpha.resize((W, H), Image.LANCZOS)
a8 = np.asarray(big)

for name, rgb in TINTS.items():
    canvas = np.zeros((H, W, 4), dtype=np.uint8)
    canvas[:, :, 0], canvas[:, :, 1], canvas[:, :, 2] = rgb
    canvas[:, :, 3] = a8
    path = f"assets/motif_tint_{name}.png"
    Image.fromarray(canvas).save(path)
    print(f"{path}  {W}x{H}  tom=#{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}")
