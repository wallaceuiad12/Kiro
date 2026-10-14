#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as peças de save the date da Caminhada pelo Dia de Doar Campinas.

Realização NAS, Núcleo de Ação Social, com a Liga Empreendedora.
Paleta e ilustrações derivadas do material oficial do evento.
"""
import os
from PIL import Image, ImageDraw
import marca_dia_de_doar as M

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
SAIDA = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(SAIDA, exist_ok=True)

LOGO_NAS = Image.open(f"{ASSETS}/nas-logo-30-anos.png").convert("RGBA")
LOGO_LIGA = Image.open(f"{ASSETS}/liga-logo.png").convert("RGBA")


def rotulo(im, dr, x, y, txt, tam=26, cor=M.PRETO, marcador=M.LARANJA, tracking=None):
    """Rótulo pequeno com marcador quadrado à esquerda."""
    f = M.fonte("ExtraBold", tam)
    tracking = tam * 0.22 if tracking is None else tracking
    if marcador:
        s = tam * 0.62
        dr.rectangle([x, y + tam * 0.18, x + s, y + tam * 0.18 + s], fill=marcador)
        x += s + tam * 0.5
    M.texto_espacado(dr, (x, y), txt, f, cor, tracking)


def bloco_info(dr, x, y, linhas, tam=31, lh=1.52, cor=M.PRETO):
    f = M.fonte("SemiBold", tam)
    for i, t in enumerate(linhas):
        dr.text((x, y + i * tam * lh), t, font=f, fill=cor)
    return y + len(linhas) * tam * lh


def caixa_tagline(im, dr, x, y, larg, tam=42):
    """Caixa verde com a assinatura do movimento."""
    f = M.fonte("ExtraBold", tam)
    l1, l2 = "Uma andorinha", "só não faz verão"
    pad = tam * 0.46
    h = int(tam * 2.52 + pad * 1.1)
    dr.rectangle([x, y, x + larg, y + h], fill=M.VERDE)
    dr.text((x + pad, y + pad * 0.72), l1, font=f, fill=M.VERDE_ESC)
    dr.text((x + pad, y + pad * 0.72 + tam * 1.24), l2, font=f, fill=M.VERDE_ESC)
    return y + h


def assinatura(im, dr, cx, y, alt_logo=96, label=True, escala=1.0):
    """Barra de realização com os logos do NAS e da Liga, centralizada em cx."""
    if label:
        f = M.fonte("Bold", 24 * escala)
        txt = "REALIZAÇÃO"
        w = M.largura_espacada(dr, txt, f, 24 * escala * 0.3)
        M.texto_espacado(dr, (cx - w / 2, y), txt, f, (120, 120, 120), 24 * escala * 0.3)
        y += 24 * escala * 2.0

    nas = M.encaixar(LOGO_NAS, alvo_h=alt_logo)
    liga = M.encaixar(LOGO_LIGA, alvo_h=alt_logo * 0.74)
    folga = int(alt_logo * 0.62)
    larg_tot = nas.size[0] + folga * 2 + 3 + liga.size[0]
    x = int(cx - larg_tot / 2)
    im.alpha_composite(nas, (x, int(y)))
    x += nas.size[0] + folga
    dr.rectangle([x, y + alt_logo * 0.12, x + 3, y + alt_logo * 0.88],
                 fill=(214, 214, 214))
    x += 3 + folga
    im.alpha_composite(liga, (x, int(y + (alt_logo - liga.size[1]) / 2)))
    return y + alt_logo


# ===================================================================== FEED
def post_feed():
    W = H = 1080
    MG = 80
    im = Image.new("RGBA", (W, H), (255, 255, 255, 255))

    # ---- decoração: roxo no alto à direita, andorinha e sol embaixo à direita
    im.alpha_composite(M.estrela_roxa(360), (836, -124))
    im.alpha_composite(M.andorinha(96, espelhar=True), (762, 150))
    im.alpha_composite(M.sol(296), (656, 540))
    im.alpha_composite(M.andorinha(380), (698, 520))

    dr = ImageDraw.Draw(im)

    # ---- rótulo
    rotulo(im, dr, MG, 70, "SAVE THE DATE", 27)

    # ---- título
    f_med = M.fonte("Black", 56)
    f_big = M.fonte("Black", 84)
    dr.text((MG, 118), "CAMINHADA PELO", font=f_med, fill=M.PRETO)
    y = 190
    _, h = M.faixa_titulo(im, dr, (MG, y), "DIA DE DOAR", f_big)
    y += h + 6
    M.faixa_titulo(im, dr, (MG, y), "CAMPINAS", f_big)

    # ---- data em faixa roxa
    y = 452
    f_data = M.fonte("ExtraBold", 34)
    txt = "DOMINGO, 29 DE NOVEMBRO"
    w = M.largura_espacada(dr, txt, f_data, 2.2)
    asc, desc = f_data.getmetrics()
    dr.rectangle([MG, y, MG + w + 44, y + asc + desc + 16], fill=M.ROXO)
    M.texto_espacado(dr, (MG + 22, y + 8), txt, f_data, (255, 255, 255), 2.2)

    # ---- informações
    bloco_info(dr, MG, 548, [
        "8h  ·  Bosque Jequitibás",
        "1 km até o Centro de Convivência",
        "Camiseta oficial  ·  em breve",
    ], tam=27, lh=1.52)

    # ---- logo do movimento e tagline
    logo = M.logo_dia_de_doar(66, fundo=M.CREME)
    im.alpha_composite(logo, (MG, 684))
    caixa_tagline(im, dr, MG, 788, 420, tam=34)

    # ---- assinatura
    dr.rectangle([0, 908, W, 911], fill=(234, 234, 234))
    assinatura(im, dr, W / 2, 930, alt_logo=116, label=False)

    return im.convert("RGB")


# ==================================================================== STORY
def post_story():
    W, H = 1080, 1920
    MG = 92
    im = Image.new("RGBA", (W, H), (255, 255, 255, 255))

    # ---- decoração
    im.alpha_composite(M.estrela_roxa(430), (792, 58))
    im.alpha_composite(M.andorinha(112, espelhar=True), (118, 152))
    im.alpha_composite(M.sol(340), (596, 932))
    im.alpha_composite(M.andorinha(436), (636, 880))

    dr = ImageDraw.Draw(im)

    rotulo(im, dr, MG, 292, "SAVE THE DATE", 32)

    f_med = M.fonte("Black", 66)
    f_big = M.fonte("Black", 100)
    dr.text((MG, 352), "CAMINHADA PELO", font=f_med, fill=M.PRETO)
    y = 438
    _, h = M.faixa_titulo(im, dr, (MG, y), "DIA DE DOAR", f_big)
    y += h + 8
    M.faixa_titulo(im, dr, (MG, y), "CAMPINAS", f_big)

    # ---- data
    y = 762
    f_data = M.fonte("ExtraBold", 40)
    txt = "DOMINGO, 29 DE NOVEMBRO"
    w = M.largura_espacada(dr, txt, f_data, 2.4)
    asc, desc = f_data.getmetrics()
    dr.rectangle([MG, y, MG + w + 50, y + asc + desc + 20], fill=M.ROXO)
    M.texto_espacado(dr, (MG + 25, y + 10), txt, f_data, (255, 255, 255), 2.4)

    # ---- informações
    bloco_info(dr, MG, 884, [
        "8h  ·  Bosque Jequitibás",
        "1 km até o Centro",
        "de Convivência",
        "Camiseta oficial  ·  em breve",
    ], tam=33, lh=1.58)

    # ---- logo e tagline
    logo = M.logo_dia_de_doar(78, fundo=M.CREME)
    im.alpha_composite(logo, (MG, 1168))
    caixa_tagline(im, dr, MG, 1298, 492, tam=42)

    # ---- assinatura
    dr.rectangle([0, 1458, W, 1461], fill=(234, 234, 234))
    fim = assinatura(im, dr, W / 2, 1492, alt_logo=146, label=True, escala=1.25)

    f_site = M.fonte("SemiBold", 28)
    site = "nas.org.br   ·   ligaempreendedora.com"
    ws = dr.textlength(site, font=f_site)
    dr.text(((W - ws) / 2, fim + 44), site, font=f_site, fill=(130, 130, 130))

    return im.convert("RGB")


if __name__ == "__main__":
    f = post_feed()
    f.save(f"{SAIDA}/post-feed-1080x1080.png", optimize=True)
    print("feed:", f.size)
    s = post_story()
    s.save(f"{SAIDA}/post-story-1080x1920.png", optimize=True)
    print("story:", s.size)
