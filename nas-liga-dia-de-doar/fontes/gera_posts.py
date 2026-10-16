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


def calendario(dr, x, y, lado, dia="29", mes="NOVEMBRO", semana="DOMINGO"):
    """Folha de calendário, cabeçalho laranja e corpo roxo."""
    h_cab = int(lado * 0.24)
    dr.rectangle([x, y, x + lado, y + h_cab], fill=M.LARANJA)
    dr.rectangle([x, y + h_cab, x + lado, y + lado], fill=M.ROXO)

    f_sem = M.fonte("ExtraBold", lado * 0.105)
    tr = lado * 0.012
    w = M.largura_espacada(dr, semana, f_sem, tr)
    bb = f_sem.getbbox(semana)
    M.texto_espacado(dr, (x + (lado - w) / 2, y + (h_cab - (bb[3] - bb[1])) / 2 - bb[1]),
                     semana, f_sem, M.PRETO, tr)

    f_dia = M.fonte("Black", lado * 0.50)
    bb = f_dia.getbbox(dia)
    wd = bb[2] - bb[0]
    corpo = lado - h_cab
    y_dia = y + h_cab + corpo * 0.12 - bb[1]
    dr.text((x + (lado - wd) / 2 - bb[0], y_dia), dia, font=f_dia, fill=M.BRANCO)

    f_mes = M.fonte("ExtraBold", lado * 0.088)
    tr = lado * 0.016
    w = M.largura_espacada(dr, mes, f_mes, tr)
    bbm = f_mes.getbbox(mes)
    y_mes = y + lado - corpo * 0.12 - (bbm[3] - bbm[1]) - bbm[1]
    M.texto_espacado(dr, (x + (lado - w) / 2, y_mes), mes, f_mes, M.BRANCO, tr)


def linha_info(dr, x, y, rotulo_txt, valor, larg_max, cor_marca, tam_val=34, esc=1.0):
    """Linha de informação com marcador, rótulo pequeno e valor em destaque."""
    s = 17 * esc
    dr.rectangle([x, y + 6 * esc, x + s, y + 6 * esc + s], fill=cor_marca)
    f_rot = M.fonte("ExtraBold", 21 * esc)
    M.texto_espacado(dr, (x + s + 14 * esc, y), rotulo_txt, f_rot, (110, 110, 110), 3.2 * esc)

    tam = tam_val
    while tam > 20:
        f_val = M.fonte("Bold", tam)
        if dr.textlength(valor, font=f_val) <= larg_max:
            break
        tam -= 1
    dr.text((x, y + 31 * esc), valor, font=f_val, fill=M.PRETO)


def card_movimento(im, dr, x, y, alt_logo=76, tam_tag=46):
    """Card no estilo da arte original, logo sobre creme e tagline sobre verde."""
    logo = M.logo_dia_de_doar(alt_logo)
    w, h_cab = logo.size
    dr.rectangle([x, y, x + w, y + h_cab], fill=M.CREME)
    im.alpha_composite(logo, (x, y))

    f = M.fonte("ExtraBold", tam_tag)
    pad_x = int(alt_logo * 0.22)
    pad_y = int(tam_tag * 0.42)
    h_corpo = int(tam_tag * 1.26 * 2 + pad_y * 2)
    y2 = y + h_cab
    dr.rectangle([x, y2, x + w, y2 + h_corpo], fill=M.VERDE)
    dr.text((x + pad_x, y2 + pad_y - 4), "Uma andorinha", font=f, fill=M.VERDE_ESC)
    dr.text((x + pad_x, y2 + pad_y - 4 + tam_tag * 1.26), "só não faz verão",
            font=f, fill=M.VERDE_ESC)
    return w, h_cab + h_corpo


# ===================================================================== FEED
def post_feed():
    W = H = 1080
    MG = 80
    im = Image.new("RGBA", (W, H), (255, 255, 255, 255))

    # ---- decoração de canto, mesma diagonal do story
    im.alpha_composite(M.estrela_roxa(360), (836, -124))
    im.alpha_composite(M.estrela_roxa(300), (-150, 936))
    im.alpha_composite(M.andorinha(100, espelhar=True), (730, 196))

    dr = ImageDraw.Draw(im)

    # ---- 1. título
    rotulo(im, dr, MG, 58, "SAVE THE DATE", 24)
    f_med = M.fonte("Black", 46)
    f_big = M.fonte("Black", 72)
    dr.text((MG, 96), "CAMINHADA PELO", font=f_med, fill=M.PRETO)
    y = 160
    _, h = M.faixa_titulo(im, dr, (MG, y), "DIA DE DOAR", f_big)
    y += h + 6
    _, h = M.faixa_titulo(im, dr, (MG, y), "CAMPINAS", f_big)
    y_fim_titulo = y + h

    # ---- 2. calendário e informações lado a lado
    y = int(y_fim_titulo + 30)
    LADO = 234
    calendario(dr, MG, y, LADO)

    x_info = MG + LADO + 36
    larg_info = W - x_info - 60
    passo = LADO / 3
    esc = 0.9
    linha_info(dr, x_info, y + 2, "CONCENTRAÇÃO", "8h no Bosque Jequitibás",
               larg_info, M.LARANJA, tam_val=30, esc=esc)
    linha_info(dr, x_info, y + 2 + passo, "PERCURSO", "1 km até o Centro de Convivência",
               larg_info, M.VERDE, tam_val=30, esc=esc)
    linha_info(dr, x_info, y + 2 + passo * 2, "CAMISETA OFICIAL", "Informações em breve",
               larg_info, M.CIANO, tam_val=30, esc=esc)

    # ---- 3. card do movimento, com sol e andorinha saindo dele
    y_card = int(y + LADO + 30)
    ALT_LOGO = 60
    w_card, h_card = card_movimento(im, dr, MG, y_card, alt_logo=ALT_LOGO, tam_tag=36)
    logo_card = M.logo_dia_de_doar(ALT_LOGO)
    h_cab = logo_card.size[1]
    x_borda = MG + w_card

    ave = M.andorinha(268)
    esc_ave = ave.size[0] / 100
    fundo_ave = ave.getchannel("A").getbbox()[3]
    x_ave = int(x_borda - 58 * ave.size[0] / 356)
    # cabeça na altura da tagline, como no story
    cab_y = y_card + h_cab + 30
    y_ave = int(cab_y - 32 * esc_ave)
    cab_x = x_ave + 28 * esc_ave
    SOL = int(236 * ave.size[0] / 356)
    im.alpha_composite(M.sol(SOL), (int(cab_x - SOL / 2), int(cab_y - SOL / 2)))

    # o sol passa por trás do cabeçalho creme, então o selo Campinas fica limpo
    dr.rectangle([MG, y_card, x_borda, y_card + h_cab], fill=M.CREME)
    im.alpha_composite(logo_card, (MG, y_card))
    im.alpha_composite(ave, (x_ave, y_ave))
    y_fim_ave = y_ave + fundo_ave

    # ---- 4. assinatura
    y_ass = int(max(y_card + h_card + 28, y_fim_ave + 16))
    dr.rectangle([MG, y_ass, W - MG, y_ass + 3], fill=(232, 232, 232))
    assinatura(im, dr, W / 2, y_ass + 22, alt_logo=92, label=False)

    return im.convert("RGB")


# ==================================================================== STORY
def post_story():
    W, H = 1080, 1920
    MG = 92
    im = Image.new("RGBA", (W, H), (255, 255, 255, 255))

    # ---- decoração de canto, fora das zonas de leitura
    im.alpha_composite(M.estrela_roxa(440), (804, -96))
    im.alpha_composite(M.estrela_roxa(560), (-230, 1712))
    im.alpha_composite(M.andorinha(118, espelhar=True), (104, 96))

    dr = ImageDraw.Draw(im)

    # ---- 1. título
    rotulo(im, dr, MG, 236, "SAVE THE DATE", 30)
    f_med = M.fonte("Black", 64)
    f_big = M.fonte("Black", 98)
    dr.text((MG, 290), "CAMINHADA PELO", font=f_med, fill=M.PRETO)
    y = 372
    _, h = M.faixa_titulo(im, dr, (MG, y), "DIA DE DOAR", f_big)
    y += h + 8
    _, h = M.faixa_titulo(im, dr, (MG, y), "CAMPINAS", f_big)
    y_fim_titulo = y + h

    # ---- 2. calendário e informações lado a lado
    y = int(y_fim_titulo + 46)
    LADO = 286
    calendario(dr, MG, y, LADO)

    x_info = MG + LADO + 44
    larg_info = W - x_info - 56
    passo = LADO / 3
    linha_info(dr, x_info, y + 4, "CONCENTRAÇÃO", "8h no Bosque Jequitibás",
               larg_info, M.LARANJA)
    linha_info(dr, x_info, y + 4 + passo, "PERCURSO", "1 km até o Centro de Convivência",
               larg_info, M.VERDE)
    linha_info(dr, x_info, y + 4 + passo * 2, "CAMISETA OFICIAL", "Informações em breve",
               larg_info, M.CIANO)

    # ---- 3. card do movimento, com sol e andorinha saindo dele
    y_card = int(y + LADO + 52)
    w_card, h_card = card_movimento(im, dr, MG, y_card, alt_logo=76, tam_tag=46)
    x_borda = MG + w_card
    ave = M.andorinha(356)
    # cabeça da andorinha, em unidades da caixa de 100, fica perto de (28, 32)
    esc = ave.size[0] / 100
    x_ave = int(x_borda - 58)
    y_ave = int(y_card + h_card - 0.60 * ave.size[1])
    cab_x, cab_y = x_ave + 28 * esc, y_ave + 32 * esc
    SOL = 236
    im.alpha_composite(M.sol(SOL), (int(cab_x - SOL / 2), int(cab_y - SOL / 2)))
    im.alpha_composite(ave, (x_ave, y_ave))
    y_fim_ave = y_ave + ave.getchannel("A").getbbox()[3]

    # ---- 4. assinatura
    y_ass = int(max(y_card + h_card + 72, y_fim_ave + 28))
    dr.rectangle([MG, y_ass, W - MG, y_ass + 3], fill=(232, 232, 232))
    assinatura(im, dr, W / 2, y_ass + 36, alt_logo=132, label=True, escala=1.15)

    return im.convert("RGB")


if __name__ == "__main__":
    f = post_feed()
    f.save(f"{SAIDA}/post-feed-1080x1080.png", optimize=True)
    print("feed:", f.size)
    s = post_story()
    s.save(f"{SAIDA}/post-story-1080x1920.png", optimize=True)
    print("story:", s.size)
