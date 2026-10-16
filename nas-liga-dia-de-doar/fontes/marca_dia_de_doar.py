#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biblioteca de elementos visuais do Dia de Doar Campinas, recriados em alta resolucao.

Paleta extraida do material oficial do evento (6abfdf9462829-lg.jpg) por analise de matiz.
"""
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ----------------------------------------------------------------- PALETA
LARANJA   = (254, 165,   1)   # #FEA501  faixa de destaque do titulo
ROXO      = (136,   0, 194)   # #8800C2  forma geometrica
VERDE     = ( 85, 215,  44)   # #55D72C  caixa da tagline e selo Campinas
VERDE_ESC = (  2,  76,   0)   # #024C00  texto sobre verde
CIANO     = (  7, 201, 254)   # #07C9FE  andorinhas
AMARELO   = (248, 210,   5)   # #F8D205  sol
CREME     = (249, 240, 225)   # #F9F0E1  caixa do logo
PRETO     = ( 15,   2,  16)   # #0F0210  titulo
NAVY      = ( 10,  42,  94)   # detalhe de pena e olho
BRANCO    = (255, 255, 255)
GRAFITE   = ( 33,  33,  33)   # #212121  Liga Empreendedora
AMARELO_L = (253, 200,  21)   # #FDC815  Liga Empreendedora
VERMELHO_NAS = (214, 50, 44)  # #D6322C  NAS
VERDE_LOGO = ( 90, 190,  70)  # verde das tiras do coracao
OURO_LOGO  = (240, 190,  40)  # ouro das tiras do coracao

FONTDIR = "/inner_container/usr/share/fonts/google-noto"


def fonte(peso, tam):
    return ImageFont.truetype(f"{FONTDIR}/NotoSans-{peso}.ttf", int(tam))


# ------------------------------------------------------------- UTILITARIOS
def bezier(p0, p1, p2, n=28):
    """Amostra uma curva quadratica."""
    pts = []
    for i in range(n + 1):
        t = i / n
        u = 1 - t
        pts.append((u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0],
                    u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]))
    return pts


def texto_espacado(dr, xy, txt, font, fill, tracking=0):
    """Desenha texto com entreletra manual e devolve a largura total."""
    x, y = xy
    for ch in txt:
        dr.text((x, y), ch, font=font, fill=fill)
        x += dr.textlength(ch, font=font) + tracking
    return x - xy[0] - tracking


def largura_espacada(dr, txt, font, tracking=0):
    w = sum(dr.textlength(c, font=font) for c in txt)
    return w + tracking * max(0, len(txt) - 1)


# --------------------------------------------- CORACAO TRANCADO DIA DE DOAR
def coracao_trancado(lado, periodo_rel=0.165):
    """Recria o coracao de tiras trancadas do Dia de Doar.

    Duas familias de tiras diagonais, verde no sentido '/' e ouro no sentido '\\',
    alternando quem passa por cima a cada cruzamento, recortadas pela silhueta
    de um coracao.
    """
    S = 4                      # supersampling
    N = lado * S
    yy, xx = np.mgrid[0:N, 0:N]
    # coordenadas normalizadas, coracao centrado
    u = (xx / N) * 2 - 1.0
    v = 1.0 - (yy / N) * 2
    u *= 1.18
    v = v * 1.18 - 0.08
    # silhueta de coracao
    dentro = (u * u + v * v - 0.62) ** 3 - u * u * (v ** 3) * 1.08 <= 0

    p = periodo_rel * N * S / S * S      # periodo em pixels do grid
    p = periodo_rel * N
    larg = p * 0.52
    d1 = (xx + yy) / math.sqrt(2.0)      # sentido '/'
    d2 = (xx - yy) / math.sqrt(2.0)      # sentido '\'
    i1 = np.floor(d1 / p)
    i2 = np.floor(d2 / p)
    t1 = (d1 % p) < larg
    t2 = (d2 % p) < larg
    verde_em_cima = ((i1 + i2) % 2) == 0

    rgba = np.zeros((N, N, 4), dtype=np.uint8)
    so_verde = t1 & ~t2
    so_ouro = t2 & ~t1
    ambos = t1 & t2
    pinta_verde = (so_verde | (ambos & verde_em_cima)) & dentro
    pinta_ouro = (so_ouro | (ambos & ~verde_em_cima)) & dentro
    for canal, cor in ((pinta_verde, VERDE_LOGO), (pinta_ouro, OURO_LOGO)):
        for k in range(3):
            rgba[..., k] = np.where(canal, cor[k], rgba[..., k])
    rgba[..., 3] = np.where(pinta_verde | pinta_ouro, 255, 0)

    im = Image.fromarray(rgba, "RGBA")
    return im.resize((lado, lado), Image.LANCZOS)


def logo_dia_de_doar(altura=120, com_selo=True, fundo=None):
    """Lockup 'coracao + Dia de Doar + selo Campinas'. Devolve RGBA."""
    h = int(altura)
    pad = int(h * 0.22)
    f_nome = fonte("Bold", h * 0.62)
    f_selo = fonte("Bold", h * 0.34)

    tmp = Image.new("RGBA", (10, 10))
    dr = ImageDraw.Draw(tmp)
    w_nome = dr.textlength("Dia de Doar", font=f_nome)
    w_selo_txt = dr.textlength("Campinas", font=f_selo)
    h_selo = int(h * 0.52)
    w_selo = int(w_selo_txt + h * 0.34)
    lado_cor = int(h * 0.92)

    larg = pad + lado_cor + int(h * 0.26) + int(w_nome)
    if com_selo:
        larg += int(h * 0.24) + w_selo
    larg += pad
    alt = h + pad * 2

    im = Image.new("RGBA", (int(larg), int(alt)), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if fundo is not None:
        d.rounded_rectangle([0, 0, larg - 1, alt - 1], radius=int(h * 0.16), fill=fundo)

    cor = coracao_trancado(lado_cor)
    cy = (alt - lado_cor) // 2
    im.alpha_composite(cor, (pad, cy))

    x = pad + lado_cor + int(h * 0.26)
    bb = f_nome.getbbox("Dia de Doar")
    d.text((x, (alt - (bb[3] - bb[1])) // 2 - bb[1]), "Dia de Doar",
           font=f_nome, fill=(51, 51, 51))
    x += w_nome + int(h * 0.24)

    if com_selo:
        y0 = (alt - h_selo) // 2
        d.rounded_rectangle([x, y0, x + w_selo, y0 + h_selo],
                            radius=int(h_selo * 0.26), fill=VERDE)
        bbs = f_selo.getbbox("Campinas")
        d.text((x + (w_selo - w_selo_txt) / 2,
                y0 + (h_selo - (bbs[3] - bbs[1])) / 2 - bbs[1]),
               "Campinas", font=f_selo, fill=VERDE_ESC)
    return im


# ------------------------------------------------------------------- SOL
def sol(tam, raios=16, cor=AMARELO):
    """Sol espetado, no estilo da ilustracao original."""
    S = 3
    N = tam * S
    im = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = N / 2
    r_in = N * 0.235
    pts = []
    for i in range(raios * 2):
        ang = math.pi * i / raios - math.pi / 2
        r = N * 0.5 if i % 2 == 0 else r_in
        pts.append((c + r * math.cos(ang), c + r * math.sin(ang)))
    d.polygon(pts, fill=cor)
    d.ellipse([c - r_in * 1.02, c - r_in * 1.02, c + r_in * 1.02, c + r_in * 1.02], fill=cor)
    return im.resize((tam, tam), Image.LANCZOS)


# -------------------------------------------------------------- ANDORINHA
def andorinha(larg, espelhar=False):
    """Andorinha em voo, ciano com barriga branca, bico dourado e penas navy.

    Geometria derivada do material oficial do evento. Caixa de 100 x 80 unidades.
    """
    S = 3
    U = larg * S / 100.0
    W, H = int(100 * U), int(82 * U)
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    def P(pts):
        return [(x * U, y * U) for x, y in pts]

    # ---- 1. cauda bifurcada, atras do corpo
    cauda = P([(60, 50), (96, 43), (83, 56), (96, 73), (71, 64), (61, 57)])
    d.polygon(cauda, fill=CIANO)

    # ---- 2. corpo e cabeca em contorno unico, sem emenda
    corpo = (bezier((12, 33), (13, 17), (27, 11), 22)      # testa
             + bezier((27, 11), (45, 13), (56, 30), 22)    # nuca
             + bezier((56, 30), (70, 42), (68, 54), 18)    # dorso
             + bezier((68, 54), (66, 69), (48, 72), 20)    # garupa
             + bezier((48, 72), (28, 70), (17, 52), 22)    # ventre
             + bezier((17, 52), (9, 44), (12, 33), 16))    # papo
    d.polygon(P(corpo), fill=CIANO)

    # ---- 3. barriga branca, acompanhando o contorno inferior
    barriga = (bezier((17, 52), (28, 70), (48, 72), 22)
               + bezier((48, 72), (58, 67), (60, 55), 18)
               + bezier((60, 55), (38, 48), (17, 52), 22))
    d.polygon(P(barriga), fill=BRANCO)

    # contorno do corpo e da barriga, para a barriga ler sobre fundo claro
    ciano_esc = (0, 150, 205)
    cw = max(1, int(1.0 * U))
    d.line(P(corpo + [corpo[0]]), fill=ciano_esc, width=cw, joint="curve")
    d.line(P(bezier((60, 55), (38, 48), (17, 52), 22)), fill=ciano_esc,
           width=cw, joint="curve")

    # ---- 4. asa erguida, lamina sobre o corpo
    asa = (bezier((40, 38), (58, 6), (90, 4), 28)
           + bezier((90, 4), (70, 20), (55, 41), 24)
           + bezier((55, 41), (46, 41), (40, 38), 14))
    d.polygon(P(asa), fill=CIANO)

    # ---- 5. bico dourado, protuberante a esquerda
    bico = P([(0, 34), (14, 29), (14, 39)])
    d.polygon(bico, fill=(247, 196, 36))
    d.line(bico + [bico[0]], fill=VERDE_ESC, width=max(1, int(0.85 * U)), joint="curve")

    # ---- 6. olho
    d.ellipse([(20.0) * U, (22.0) * U, (24.4) * U, (26.4) * U], fill=NAVY)

    # ---- 7. linhas de pena na asa
    lw = max(1, int(1.1 * U))
    for p0, p1, p2 in (((58, 30), (68, 22), (80, 17)),
                       ((56, 36), (66, 29), (78, 25)),
                       ((52, 42), (62, 37), (72, 34)),
                       ((47, 33), (51, 30), (56, 28))):
        d.line(P(bezier(p0, p1, p2, 16)), fill=NAVY, width=lw, joint="curve")

    im = im.resize((int(100 * larg / 100), int(82 * larg / 100)), Image.LANCZOS)
    if espelhar:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    return im


# ------------------------------------------------------- FORMA ROXA ANGULAR
def estrela_roxa(tam, cor=ROXO):
    """Forma angular pontiaguda, como a do material original."""
    S = 3
    N = tam * S
    im = Image.new("RGBA", (N, N), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    c = N / 2
    pontas = [(0.50, 0.00), (0.62, 0.30), (0.95, 0.18), (0.78, 0.48),
              (1.00, 0.68), (0.66, 0.70), (0.72, 1.00), (0.48, 0.78),
              (0.22, 0.98), (0.26, 0.66), (0.00, 0.60), (0.24, 0.40),
              (0.08, 0.14), (0.38, 0.26)]
    d.polygon([(x * N, y * N) for x, y in pontas], fill=cor)
    return im.resize((tam, tam), Image.LANCZOS)


# ------------------------------------------------------- FAIXA DE DESTAQUE
def faixa_titulo(im, dr, xy, txt, font, cor_faixa=LARANJA, cor_txt=PRETO,
                 folga_x=0.14, folga_y=0.10, tracking=0):
    """Escreve o texto sobre uma faixa solida, como no material oficial."""
    x, y = xy
    w = largura_espacada(dr, txt, font, tracking)
    asc, desc = font.getmetrics()
    h = asc + desc
    fx = h * folga_x
    fy = h * folga_y
    dr.rectangle([x - fx * 0.55, y - fy, x + w + fx * 0.55, y + h + fy * 0.3],
                 fill=cor_faixa)
    texto_espacado(dr, (x, y), txt, font, cor_txt, tracking)
    return w, h + fy * 1.3


def encaixar(logo, alvo_h=None, alvo_w=None):
    """Redimensiona um PNG de logo preservando proporcao."""
    w, h = logo.size
    if alvo_h:
        nw = int(w * alvo_h / h)
        return logo.resize((nw, int(alvo_h)), Image.LANCZOS)
    nh = int(h * alvo_w / w)
    return logo.resize((int(alvo_w), nh), Image.LANCZOS)
