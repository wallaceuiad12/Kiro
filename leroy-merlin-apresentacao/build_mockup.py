#!/usr/bin/env python3
"""
Monta um mockup novo do produto finalizado, para nao repetir as mesmas fotos
em todos os slides.

Recorta a necessaire e a ecobag das fotos originais e compoe as duas numa cena
de estudio limpa, no cinza claro da identidade da Nunes & Lucato, com sombra
projetada suave.

Saida: mockup-produto-final.png
"""
import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(BASE)
FOTO_NECESSAIRE = os.path.join(REPO, "IMG-20260928-WA0153.jpg")
FOTO_ECOBAG = os.path.join(REPO, "IMG-20260928-WA0154.jpg")
SAIDA = os.path.join(BASE, "mockup-produto-final.png")

LARG, ALT = 1800, 1100
FUNDO_TOPO = (246, 247, 250)
FUNDO_BASE = (226, 229, 238)


def recorta_grabcut(caminho, margem=0.06, iteracoes=6, tira_claros=False):
    """Separa o produto do fundo com GrabCut, partindo de um retangulo amplo."""
    img = cv2.imread(caminho)
    h, w = img.shape[:2]
    rect = (int(w * margem), int(h * margem),
            int(w * (1 - 2 * margem)), int(h * (1 - 2 * margem)))
    mascara = np.zeros((h, w), np.uint8)
    fundo = np.zeros((1, 65), np.float64)
    frente = np.zeros((1, 65), np.float64)
    cv2.grabCut(img, mascara, rect, fundo, frente, iteracoes, cv2.GC_INIT_WITH_RECT)
    binaria = np.where((mascara == cv2.GC_FGD) | (mascara == cv2.GC_PR_FGD), 255, 0)
    binaria = binaria.astype(np.uint8)
    if tira_claros:
        # A necessaire e preta sobre fundo de estudio claro. Cortar so por
        # luminancia deixa farrapos de fundo colados na base, porque a sombra do
        # fundo e escura. Entao a mascara e ancorada no corpo escuro do produto,
        # dilatado o suficiente para reincorporar zíper e brilhos da borda.
        cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        escuro = np.where(cinza < 150, 255, 0).astype(np.uint8)
        nucleo = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
        escuro = cv2.morphologyEx(escuro, cv2.MORPH_CLOSE, nucleo, iterations=3)
        escuro = maior_componente(escuro)
        escuro = cv2.dilate(escuro, cv2.getStructuringElement(
            cv2.MORPH_ELLIPSE, (13, 13)), iterations=1)
        binaria = cv2.bitwise_and(binaria, escuro)
        binaria = cv2.morphologyEx(binaria, cv2.MORPH_CLOSE, nucleo, iterations=2)
    return img, binaria


def recorta_por_luminancia(caminho, limite=205):
    """Para a necessaire, que esta sobre fundo de estudio claro e uniforme."""
    img = cv2.imread(caminho)
    cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mascara = np.where(cinza < limite, 255, 0).astype(np.uint8)
    # fecha buracos e remove respingos
    nucleo = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, nucleo, iterations=3)
    mascara = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, nucleo, iterations=2)
    return img, mascara


def maior_componente(mascara):
    """Mantem apenas a maior area conectada, descarta sujeira do recorte."""
    n, rotulos, estat, _ = cv2.connectedComponentsWithStats(mascara, 8)
    if n <= 1:
        return mascara
    maior = 1 + np.argmax(estat[1:, cv2.CC_STAT_AREA])
    return np.where(rotulos == maior, 255, 0).astype(np.uint8)


def para_rgba(img_bgr, mascara, suavizar=2.0):
    mascara = maior_componente(mascara)
    rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    alfa = Image.fromarray(mascara).filter(ImageFilter.GaussianBlur(suavizar))
    out = Image.fromarray(rgb).convert("RGBA")
    out.putalpha(alfa)
    return out.crop(out.getbbox())


def redimensiona_altura(img, altura):
    prop = altura / img.height
    return img.resize((max(1, int(img.width * prop)), altura), Image.LANCZOS)


def redimensiona_largura(img, largura):
    prop = largura / img.width
    return img.resize((largura, max(1, int(img.height * prop))), Image.LANCZOS)


def fundo_estudio():
    base = Image.new("RGB", (LARG, ALT), FUNDO_TOPO)
    d = ImageDraw.Draw(base)
    for y in range(ALT):
        t = y / ALT
        cor = tuple(int(FUNDO_TOPO[i] + (FUNDO_BASE[i] - FUNDO_TOPO[i]) * t ** 1.6)
                    for i in range(3))
        d.line([(0, y), (LARG, y)], fill=cor)
    return base


def sombra(cena, produto, x, y, forca=150, desfoque=38):
    """Sombra de contato, elipse achatada na base do produto."""
    camada = Image.new("RGBA", cena.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(camada)
    larg = int(produto.width * 0.92)
    alt_s = max(14, int(produto.height * 0.11))
    cx = x + produto.width // 2
    cy = y + produto.height - int(alt_s * 0.35)
    d.ellipse([cx - larg // 2, cy - alt_s // 2, cx + larg // 2, cy + alt_s // 2],
              fill=(26, 28, 46, forca))
    camada = camada.filter(ImageFilter.GaussianBlur(desfoque))
    cena.alpha_composite(camada)


def main():
    # GrabCut resolve os dois casos. Na necessaire o limite por luminancia falhava,
    # porque o fundo de estudio tem gradiente e sombra mais escuros que o limite.
    nec_bgr, nec_mask = recorta_grabcut(FOTO_NECESSAIRE, margem=0.08, tira_claros=True)
    necessaire = para_rgba(nec_bgr, nec_mask, suavizar=1.6)

    eco_bgr, eco_mask = recorta_grabcut(FOTO_ECOBAG)
    ecobag = para_rgba(eco_bgr, eco_mask, suavizar=2.2)

    print("recortes:", "necessaire", necessaire.size, "ecobag", ecobag.size)

    # a ecobag fica atras e mais alta, a necessaire na frente, criando profundidade.
    # a necessaire e dimensionada pela largura, ela e larga e baixa
    ecobag = redimensiona_altura(ecobag, int(ALT * 0.72))
    necessaire = redimensiona_largura(necessaire, int(LARG * 0.235))

    cena = fundo_estudio().convert("RGBA")

    base_y = int(ALT * 0.86)
    eco_x = int(LARG * 0.34) - ecobag.width // 2
    eco_y = base_y - ecobag.height
    nec_x = int(LARG * 0.62) - necessaire.width // 2
    nec_y = base_y - necessaire.height

    sombra(cena, ecobag, eco_x, eco_y, forca=165, desfoque=40)
    cena.alpha_composite(ecobag, (eco_x, eco_y))
    sombra(cena, necessaire, nec_x, nec_y, forca=175, desfoque=24)
    cena.alpha_composite(necessaire, (nec_x, nec_y))

    cena.convert("RGB").save(SAIDA, quality=94)
    print("gerado:", SAIDA)


if __name__ == "__main__":
    main()
