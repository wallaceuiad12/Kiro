#!/usr/bin/env python3
"""
Extrai de panfleto6.png os assets reaproveitados na arte de story.

Mantemos a mesma foto, o mesmo selo do Nubank e os mesmos logos do panfleto
oficial para que as pecas da campanha fiquem consistentes entre si. Rode so
quando o panfleto de referencia mudar.

Uso:
    python preparar_assets.py
"""

from pathlib import Path

import numpy as np
from PIL import Image

BASE = Path(__file__).parent
PANFLETO = BASE.parent / "panfleto6.png"
OUT = BASE / "assets"
OUT.mkdir(exist_ok=True)

BG = np.array([245, 241, 236])          # off-white do panfleto

# recortes em coordenadas normalizadas de uma previa de 760 px de largura
CROPS = {
    "photo_bar": (410, 0, 760, 610),
    "logo_decade": (518, 975, 710, 1020),
    "logo_liga": (55, 960, 200, 1035),
}
PAD = 12
PHOTO_BAR_SPLIT = 1956                  # linha onde o retrato termina e o selo comeca


def monocromatico(src, out, cor, escala=2.2):
    """Gera versao monocromatica com alfa, a partir da distancia ao fundo off-white."""
    arr = np.asarray(Image.open(src).convert("RGB")).astype(np.int16)
    dist = np.abs(arr - BG).max(axis=2)
    rgba = np.zeros(arr.shape[:2] + (4,), dtype=np.uint8)
    rgba[..., 0], rgba[..., 1], rgba[..., 2] = cor
    rgba[..., 3] = np.clip(dist * escala, 0, 255).astype(np.uint8)
    img = Image.fromarray(rgba, "RGBA")
    img = img.crop(img.getbbox())
    img.save(out)
    print("ok", out.name, img.size)


def liga_colorida(src, out):
    """Logo da Liga nas cores originais, com fundo transparente."""
    arr = np.asarray(Image.open(src).convert("RGB")).astype(np.int16)
    dist = np.abs(arr - BG).max(axis=2)
    rgba = np.zeros(arr.shape[:2] + (4,), dtype=np.uint8)
    rgba[..., 0:3] = np.clip(arr, 0, 255).astype(np.uint8)
    rgba[..., 3] = np.clip(dist * 2.2, 0, 255).astype(np.uint8)
    img = Image.fromarray(rgba, "RGBA")
    img = img.crop(img.getbbox())
    img.save(out)
    print("ok", out.name, img.size)


def liga_versao_clara(src, out):
    """Versao para fundo escuro, o amarelo fica e a parte escura vira off-white."""
    arr = np.asarray(Image.open(src).convert("RGB")).astype(np.int16)
    dist = np.abs(arr - BG).max(axis=2)
    amarelado = (arr[..., 0] + arr[..., 1]) / 2.0 - arr[..., 2]
    t = np.clip((amarelado - 20) / 120.0, 0, 1)[..., None]
    amarelo = np.array([245, 197, 24], dtype=float)
    claro = np.array([245, 241, 236], dtype=float)
    rgba = np.zeros(arr.shape[:2] + (4,), dtype=np.uint8)
    rgba[..., 0:3] = np.clip(amarelo * t + claro * (1 - t), 0, 255).astype(np.uint8)
    rgba[..., 3] = np.clip(dist * 2.2, 0, 255).astype(np.uint8)
    img = Image.fromarray(rgba, "RGBA")
    img = img.crop(img.getbbox())
    img.save(out)
    print("ok", out.name, img.size)


def main():
    panfleto = Image.open(PANFLETO).convert("RGB")
    s = panfleto.width / 760.0
    recortes = {}
    for nome, (x0, y0, x1, y1) in CROPS.items():
        pad = 0 if nome == "photo_bar" else PAD
        box = (max(0, int(x0 * s - pad)), max(0, int(y0 * s - pad)),
               min(panfleto.width, int(x1 * s + pad)),
               min(panfleto.height, int(y1 * s + pad)))
        recortes[nome] = panfleto.crop(box)

    # retrato limpo e selo do Nubank
    pb = recortes["photo_bar"]
    pb.crop((0, 0, pb.width, PHOTO_BAR_SPLIT)).save(OUT / "photo_clean.png")
    bar = pb.crop((0, PHOTO_BAR_SPLIT, pb.width, pb.height))
    print("ok photo_clean.png", (pb.width, PHOTO_BAR_SPLIT))

    # wordmark "nu" do selo, branco sobre preto, virando mascara de alfa
    g = np.asarray(bar.crop((40, 95, 195, 215)).convert("RGB")).astype(np.int16).mean(axis=2)
    rgba = np.zeros(g.shape + (4,), dtype=np.uint8)
    rgba[..., 0:3] = 255
    rgba[..., 3] = np.clip((g - 30) * 1.6, 0, 255).astype(np.uint8)
    nu = Image.fromarray(rgba, "RGBA")
    nu = nu.crop(nu.getbbox())
    nu.save(OUT / "nu_mark.png")
    print("ok nu_mark.png", nu.size)

    # logos em versao clara e escura
    for nome in ("logo_decade", "logo_liga"):
        recortes[nome].save(OUT / f"{nome}.png")
    monocromatico(OUT / "logo_decade.png", OUT / "decade_black.png", (0, 0, 0))
    monocromatico(OUT / "logo_decade.png", OUT / "decade_offwhite.png", (245, 241, 236))
    monocromatico(OUT / "logo_liga.png", OUT / "liga_black.png", (17, 17, 17))
    monocromatico(OUT / "logo_liga.png", OUT / "liga_offwhite.png", (245, 241, 236))
    liga_colorida(OUT / "logo_liga.png", OUT / "liga_color.png")
    liga_versao_clara(OUT / "logo_liga.png", OUT / "liga_color_dark.png")


if __name__ == "__main__":
    main()
