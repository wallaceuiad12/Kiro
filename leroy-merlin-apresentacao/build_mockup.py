#!/usr/bin/env python3
"""
Monta o mockup do produto finalizado, para nao repetir as mesmas fotos em todos
os slides.

Recorta a necessaire e a ecobag das fotos originais e compoe as duas sobre o
branco da identidade da Nunes & Lucato.

Tres decisoes para nao parecer montagem:

1. A sombra sai da propria silhueta do produto, achatada e inclinada conforme a
   direcao da luz. Elipse generica embaixo do objeto e o que mais denuncia recorte.
2. Sombra em duas camadas, uma de contato curta e escura na base e uma projetada
   longa e difusa, que e como sombra real se comporta.
3. Fundo branco puro, sem cenario de estudio nem linha de apoio, para a imagem
   se integrar ao card branco do slide em vez de parecer uma foto colada.

Saida: mockup-produto-final.png
"""
import os
import cv2
import numpy as np
from PIL import Image, ImageFilter

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(BASE)
FOTO_NECESSAIRE = os.path.join(REPO, "IMG-20260928-WA0153.jpg")
FOTO_ECOBAG = os.path.join(REPO, "IMG-20260928-WA0154.jpg")
SAIDA = os.path.join(BASE, "mockup-produto-final.png")

LARG, ALT = 1800, 1100
BASE_Y = int(ALT * 0.90)
BRANCO = (255, 255, 255)


# ------------------------------------------------------------------- recortes
def maior_componente(mascara):
    n, rotulos, estat, _ = cv2.connectedComponentsWithStats(mascara, 8)
    if n <= 1:
        return mascara
    maior = 1 + np.argmax(estat[1:, cv2.CC_STAT_AREA])
    return np.where(rotulos == maior, 255, 0).astype(np.uint8)


def recorta(caminho, margem=0.06, iteracoes=6, ancora_escura=False):
    """GrabCut partindo de um retangulo amplo."""
    img = cv2.imread(caminho)
    h, w = img.shape[:2]
    rect = (int(w * margem), int(h * margem),
            int(w * (1 - 2 * margem)), int(h * (1 - 2 * margem)))
    mascara = np.zeros((h, w), np.uint8)
    cv2.grabCut(img, mascara, rect, np.zeros((1, 65), np.float64),
                np.zeros((1, 65), np.float64), iteracoes, cv2.GC_INIT_WITH_RECT)
    binaria = np.where((mascara == cv2.GC_FGD) | (mascara == cv2.GC_PR_FGD),
                       255, 0).astype(np.uint8)
    if ancora_escura:
        # A necessaire e preta sobre fundo claro. Cortar so por luminancia deixa
        # farrapos de fundo colados na base, porque a sombra do fundo e escura.
        # Entao a mascara e ancorada no corpo escuro e dilatada depois, para o
        # ziper e os brilhos da borda voltarem.
        cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        escuro = np.where(cinza < 150, 255, 0).astype(np.uint8)
        nucleo = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
        escuro = cv2.morphologyEx(escuro, cv2.MORPH_CLOSE, nucleo, iterations=3)
        escuro = maior_componente(escuro)
        escuro = cv2.dilate(escuro, cv2.getStructuringElement(
            cv2.MORPH_ELLIPSE, (13, 13)))
        binaria = cv2.bitwise_and(binaria, escuro)
        binaria = cv2.morphologyEx(binaria, cv2.MORPH_CLOSE, nucleo, iterations=2)
    return img, maior_componente(binaria)


def para_rgba(img_bgr, mascara):
    """Encolhe a mascara 1 px antes de suavizar, senao sobra halo do fundo."""
    mascara = cv2.erode(mascara, cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE, (3, 3)))
    rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    alfa = Image.fromarray(mascara).filter(ImageFilter.GaussianBlur(1.1))
    out = Image.fromarray(rgb).convert("RGBA")
    out.putalpha(alfa)
    return out.crop(out.getbbox())


def redimensiona(img, largura=None, altura=None):
    if largura:
        k = largura / img.width
    else:
        k = altura / img.height
    return img.resize((max(1, int(img.width * k)), max(1, int(img.height * k))),
                      Image.LANCZOS)


# -------------------------------------------------------------------- sombras
def sombra_silhueta(cena, produto, x, y, inclinacao=0.42, achatamento=0.17,
                    desfoque=26, opacidade=58):
    """Sombra projetada, a propria silhueta achatada e inclinada."""
    alfa = produto.split()[3]
    w, h = alfa.size
    alt = max(8, int(h * achatamento))
    sh = alfa.resize((w, alt), Image.LANCZOS)
    desloc = int(h * achatamento * inclinacao * 3.2)
    tela = Image.new("L", (w + abs(desloc) * 2, alt), 0)
    tela.paste(sh, (abs(desloc), 0))
    sh = tela.transform(tela.size, Image.AFFINE,
                        (1, inclinacao, -inclinacao * alt, 0, 1, 0),
                        resample=Image.BICUBIC)
    sh = sh.filter(ImageFilter.GaussianBlur(desfoque))
    camada = Image.new("RGBA", cena.size, (0, 0, 0, 0))
    tinta = Image.new("RGBA", sh.size, (22, 24, 42, 255))
    tinta.putalpha(sh.point(lambda v: int(v * opacidade / 255)))
    camada.alpha_composite(tinta, (x - abs(desloc), y + h - alt // 2))
    cena.alpha_composite(camada)


def sombra_contato(cena, produto, x, y, desfoque=9, opacidade=165):
    """Sombra curta e escura na linha de apoio, o que ancora o objeto."""
    alfa = produto.split()[3]
    w, h = alfa.size
    faixa = alfa.crop((0, int(h * 0.93), w, h)).resize((w, max(6, int(h * 0.05))),
                                                       Image.LANCZOS)
    faixa = faixa.filter(ImageFilter.GaussianBlur(desfoque))
    tinta = Image.new("RGBA", faixa.size, (18, 20, 36, 255))
    tinta.putalpha(faixa.point(lambda v: int(v * opacidade / 255)))
    cena.alpha_composite(tinta, (x, y + h - faixa.height // 2))


# ----------------------------------------------------------------------- cena
def fundo():
    """Branco puro, o mesmo fundo dos slides, sem cenario e sem linha de apoio.

    Gradiente de estudio e linha de horizonte sao o que mais faz a composicao
    parecer montagem, e o branco faz a imagem se integrar ao card do slide.
    """
    return Image.new("RGBA", (LARG, ALT), BRANCO + (255,))


def main():
    nec = para_rgba(*recorta(FOTO_NECESSAIRE, margem=0.08, ancora_escura=True))
    eco = para_rgba(*recorta(FOTO_ECOBAG))

    eco = redimensiona(eco, altura=int(ALT * 0.76))
    nec = redimensiona(nec, largura=int(LARG * 0.25))
    print("pecas:", "ecobag", eco.size, "necessaire", nec.size)

    cena = fundo()

    eco_x = int(LARG * 0.36) - eco.width // 2
    eco_y = BASE_Y - eco.height
    nec_x = int(LARG * 0.67) - nec.width // 2
    nec_y = BASE_Y - nec.height

    # luz vem de cima a esquerda, as duas sombras caem para a direita
    sombra_silhueta(cena, eco, eco_x, eco_y, desfoque=24, opacidade=74)
    sombra_silhueta(cena, nec, nec_x, nec_y, desfoque=16, opacidade=78)
    sombra_contato(cena, eco, eco_x, eco_y)
    sombra_contato(cena, nec, nec_x, nec_y)

    cena.alpha_composite(eco, (eco_x, eco_y))
    cena.alpha_composite(nec, (nec_x, nec_y))

    cena.convert("RGB").save(SAIDA, quality=95)
    print("gerado:", SAIDA)


if __name__ == "__main__":
    main()
