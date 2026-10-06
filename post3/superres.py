"""
Melhora a nitidez dos ativos de marca, com a menor mudanca possivel.

O que estava errado: os ativos eram recortados em tamanho nativo (o da Liga em 189x78)
e o navegador os AMPLIAVA no render @2x, o que produzia o aspecto pixelado.

Duas tentativas foram feitas e descartadas, registradas aqui para nao repetir:

  1. Vetorizar com potrace. Tracar um JPEG de 189 px faz o potrace seguir fielmente o
     ruido de compressao: a borda sai bamba e o globo sobre o "i" do logo da Liga se
     desfaz. O bitmap, mesmo suave, e mais fiel.

  2. Media das duas pecas. O alinhamento por translacao inteira so chega a IoU ~0.85,
     e misturar mascaras desalinhadas gera franja cinza, ou seja, mais borrao.

  3. Trocar TODOS os ativos para a peca escura. O simbolo e o lockup da Decade ficaram
     mais pesados e com serifa borrada: off-white sobre preto sofre mais com JPEG do
     que tinta escura sobre fundo claro. Revertido.

O que ficou:

  - Pre-ampliar 4x com LANCZOS. Nao cria informacao, mas faz o navegador REDUZIR em vez
    de ampliar, e era a ampliacao no navegador que causava a pixelacao.

  - Trocar a fonte APENAS do logo da Liga para a peca escura, onde ele esta em 195x80 e,
    mais importante, onde o globo sobre o "i" e as letras de EMPREENDEDORA aparecem com
    definicao. O peso da tinta e calibrado por busca para bater com o do Post1, senao a
    marca do parceiro sairia mais gorda que a original.

  - Simbolo e lockup da Decade seguem vindo do Post1, com os mesmos parametros de
    extracao que foram validados contra o original dentro de +/-1 px.
"""
from PIL import Image, ImageFilter
import numpy as np

CLARO = "../Post1 - Inicio.jpeg"
ESCURO = "../SaveClip.App_838195465_18444907306131074_592259580098203467_n.jpg"

BG = {
    "claro": [np.array([245, 241, 236]), np.array([233, 229, 224])],
    "escuro": [np.array([12, 11, 9]), np.array([26, 25, 23])],
}
IMG = {
    "claro": np.asarray(Image.open(CLARO).convert("RGB")).astype(float),
    "escuro": np.asarray(Image.open(ESCURO).convert("RGB")).astype(float),
}

CORTE_PADRAO = 25.0     # o valor validado contra o Post1
ESCALA = 4
VARIANTS = {"black": (0, 0, 0), "offwhite": (245, 241, 236)}
MOTIF_TINTS = {"motif_light": (233, 229, 224), "motif_dark": (26, 25, 23)}

# bbox de tinta por peca, tamanho de uso em 1080x1350, e de onde vem cada ativo
ATIVOS = {
    "symbol": {
        "fonte": "claro", "box": (599, 420, 681, 497),
        "uso": (69.19, 64.97), "calibrar": False, "nitidez": 0,
    },
    "decade_lockup": {
        "fonte": "claro", "box": (362, 1453, 623, 1505),
        "uso": (220.22, 43.88), "calibrar": False, "nitidez": 0,
    },
    "liga_lockup": {
        "fonte": "escuro", "box": (764, 1502, 959, 1582),
        "uso": (159.47, 65.81), "calibrar": True, "nitidez": 35,
        "ref": (728, 1427, 917, 1505),   # a mesma marca no Post1, para medir o peso alvo
    },
}


def alfa(fonte, box, corte):
    x0, y0, x1, y1 = box
    sub = IMG[fonte][y0:y1, x0:x1]
    dist = np.minimum.reduce([np.sqrt(((sub - f) ** 2).sum(axis=2)) for f in BG[fonte]])
    a = np.clip((dist - corte) / 85.0, 0.0, 1.0)
    a[a < 0.10] = 0.0
    a[a > 0.90] = 1.0
    return a


def peso(a, uso):
    """Peso de tinta da forma no tamanho final de uso."""
    w, h = int(round(uso[0])), int(round(uso[1]))
    img = Image.fromarray((a * 255).astype(np.uint8)).resize((w, h), Image.LANCZOS)
    return np.asarray(img).astype(float).mean() / 255.0


print("ativo            fonte    limiar  peso alvo  peso final  tamanho final")
print("-" * 72)

for nome, cfg in ATIVOS.items():
    if cfg["calibrar"]:
        alvo = peso(alfa("claro", cfg["ref"], CORTE_PADRAO), cfg["uso"])
        melhor = None
        for corte in range(10, 141, 2):
            a = alfa(cfg["fonte"], cfg["box"], float(corte))
            erro = abs(peso(a, cfg["uso"]) - alvo)
            if melhor is None or erro < melhor[0]:
                melhor = (erro, corte, a)
        _, corte, a = melhor
    else:
        corte = int(CORTE_PADRAO)
        a = alfa(cfg["fonte"], cfg["box"], CORTE_PADRAO)
        alvo = peso(a, cfg["uso"])

    h, w = a.shape
    W, H = w * ESCALA, h * ESCALA
    big = Image.fromarray((a * 255).astype(np.uint8)).resize((W, H), Image.LANCZOS)
    if cfg["nitidez"]:
        big = big.filter(ImageFilter.UnsharpMask(2.0, cfg["nitidez"], 2))
    a8 = np.asarray(big)

    fills = dict(VARIANTS)
    if nome == "symbol":
        fills.update(MOTIF_TINTS)
    for variante, rgb in fills.items():
        canvas = np.zeros((H, W, 4), dtype=np.uint8)
        canvas[:, :, 0], canvas[:, :, 1], canvas[:, :, 2] = rgb
        canvas[:, :, 3] = a8
        saida = variante if variante.startswith("motif") else f"{nome}_{variante}"
        Image.fromarray(canvas).save(f"assets/{saida}.png")

    final = peso(a8.astype(float) / 255.0, cfg["uso"])
    print(f"{nome:16s} {cfg['fonte']:8s} {corte:6d}  {alvo:9.4f}  {final:10.4f}  {W}x{H}")

print("\nativos regravados em assets/")
