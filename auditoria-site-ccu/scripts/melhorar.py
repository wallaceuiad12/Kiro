#!/usr/bin/env python3
"""
Melhora as 6 fotos de evento do CCU e gera os recortes que o Wix precisa.

O que faz (e por que):
  1. Auto-levels por canal, com corte suave -> recupera faixa tonal e tira dominante de cor
  2. Lift de exposicao adaptativo -> so nas subexpostas (brilho < 100)
  3. Saturacao leve -> fotos internas ficam lavadas
  4. Upscale LANCZOS -> melhor reamostragem disponivel sem IA
  5. Unsharp mask DEPOIS do upscale -> ordem correta do fluxo profissional
  6. Exporta JPEG q92 + WebP q88

O que NAO faz: inventar detalhe. Upscale nao recupera informacao que nao foi capturada.
"""
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import os, json

SRC = "/projects/sandbox/fotos"
OUT = "/projects/sandbox/fotos/wix"
os.makedirs(OUT, exist_ok=True)

FOTOS = {
    "1771088123415.jpg": ("ccu-evento-bain-turma", "Hero da home / Parceiros",
                          [("hero", 1600, 667), ("card", 800, 600), ("quadrado", 1080, 1080)]),
    "1787747977006.jpg": ("ccu-bain-logo", "Parceiros / prova de parceria",
                          [("card", 800, 600), ("quadrado", 1080, 1080)]),
    "1760991748668.jpg": ("cwc-mckinsey-broken-rung", "Hero do CWC",
                          [("hero", 1600, 667), ("card", 800, 600)]),
    "1761779524625.jpg": ("cwc-do-campus-a-consultoria", "CWC",
                          [("card", 800, 600), ("quadrado", 1080, 1080)]),
    "1760991748872.jpg": ("cwc-networking", "CWC / galeria",
                          [("card", 800, 600)]),
    "1771088123226.jpg": ("ccu-evento-bain-retrato", "Cartao de projeto / mobile",
                          [("retrato", 1080, 1350), ("card", 800, 600)]),
}


def lap_var(im):
    g = np.asarray(im.convert("L"), dtype=float)
    k = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=float)
    h, w = g.shape
    o = np.zeros((h - 2, w - 2))
    for dy in range(3):
        for dx in range(3):
            if k[dy, dx]:
                o += k[dy, dx] * g[dy:h - 2 + dy, dx:w - 2 + dx]
    return o.var()


def auto_levels(im, corte=0.4, forca=0.7):
    """Estica cada canal entre percentis. forca<1 preserva tom de pele natural."""
    a = np.asarray(im, dtype=float)
    out = np.empty_like(a)
    for c in range(3):
        ch = a[:, :, c]
        lo, hi = np.percentile(ch, corte), np.percentile(ch, 100 - corte)
        out[:, :, c] = ch if hi - lo < 1 else np.clip((ch - lo) * 255.0 / (hi - lo), 0, 255)
    mix = out * forca + a * (1 - forca)
    return Image.fromarray(mix.astype(np.uint8))


def lift_exposicao(im, alvo=112):
    """Clareia so o necessario, via gama. Nao estoura as altas luzes."""
    g = np.asarray(im.convert("L"), dtype=float)
    atual = g.mean()
    if atual >= alvo:
        return im, 1.0
    gama = max(0.68, min(1.0, np.log(alvo / 255.0) / np.log(max(atual, 1) / 255.0)))
    a = np.asarray(im, dtype=float) / 255.0
    a = np.power(a, gama) * 255.0
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)), gama


def recorta(im, lw, lh):
    """Recorte central no aspecto desejado, sem distorcer."""
    ar_alvo, ar = lw / lh, im.width / im.height
    if ar > ar_alvo:
        nw = int(im.height * ar_alvo)
        box = ((im.width - nw) // 2, 0, (im.width - nw) // 2 + nw, im.height)
    else:
        nh = int(im.width / ar_alvo)
        # recorte deslocado para cima: em foto de grupo o interesse esta no terco superior
        top = int((im.height - nh) * 0.35)
        box = (0, top, im.width, top + nh)
    return im.crop(box)


def processa(caminho):
    orig = Image.open(caminho).convert("RGB")
    im = auto_levels(orig)
    im, gama = lift_exposicao(im)
    im = ImageEnhance.Color(im).enhance(1.18)
    im = ImageEnhance.Contrast(im).enhance(1.06)
    return orig, im, gama


relatorio = []
print(f"{'ARQUIVO FINAL':<34}{'RECORTE':<10}{'SAIDA':>12}{'ESCALA':>8}"
      f"{'NITIDEZ':>9}{'JPEG':>8}{'WEBP':>8}")
print("-" * 92)

for src, (nome, uso, recortes) in FOTOS.items():
    p = os.path.join(SRC, src)
    orig, base, gama = processa(p)
    n0 = lap_var(orig)
    b0 = np.asarray(orig.convert("L"), dtype=float).mean()
    b1 = np.asarray(base.convert("L"), dtype=float).mean()

    for tag, lw, lh in recortes:
        c = recorta(base, lw, lh)
        escala = lw / c.width
        im = c.resize((lw, lh), Image.LANCZOS)
        # unsharp proporcional ao quanto foi ampliado
        raio = 1.1 if escala <= 1.05 else 1.7
        pct = 95 if escala <= 1.05 else 135
        im = im.filter(ImageFilter.UnsharpMask(radius=raio, percent=pct, threshold=3))

        fj = f"{nome}--{tag}.jpg"
        fw = f"{nome}--{tag}.webp"
        im.save(os.path.join(OUT, fj), "JPEG", quality=92, optimize=True, progressive=True)
        im.save(os.path.join(OUT, fw), "WEBP", quality=88, method=6)
        kj = os.path.getsize(os.path.join(OUT, fj)) / 1024
        kw = os.path.getsize(os.path.join(OUT, fw)) / 1024
        n1 = lap_var(im)
        print(f"{nome[:33]:<34}{tag:<10}{lw}x{lh:<7}{escala:>7.2f}x"
              f"{n1:>9.0f}{kj:>7.0f}K{kw:>7.0f}K")
        relatorio.append(dict(origem=src, nome=nome, uso=uso, recorte=tag,
                              saida=f"{lw}x{lh}", escala=round(escala, 2),
                              nitidez_orig=round(n0), nitidez_final=round(n1),
                              brilho_orig=round(b0), brilho_final=round(b1),
                              gama=round(gama, 3), jpeg_kb=round(kj), webp_kb=round(kw)))

json.dump(relatorio, open(os.path.join(OUT, "_relatorio.json"), "w"),
          ensure_ascii=False, indent=1)

print("\n=== ganho de exposicao por foto ===")
vistos = set()
for r in relatorio:
    if r["nome"] in vistos:
        continue
    vistos.add(r["nome"])
    d = r["brilho_final"] - r["brilho_orig"]
    print(f"  {r['nome']:<34} brilho {r['brilho_orig']:>3} -> {r['brilho_final']:>3} "
          f"({d:+d})  gama {r['gama']}")
print(f"\n{len(relatorio)} arquivos JPEG + {len(relatorio)} WebP em {OUT}")
