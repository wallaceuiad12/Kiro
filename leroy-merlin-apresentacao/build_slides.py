#!/usr/bin/env python3
"""
Gera os 2 slides do Projeto Leroy Merlin na identidade visual da apresentacao
institucional da Nunes & Lucato (Bioma Textil, Ecoponto Belezinho).

Toda a geometria, paleta e tipografia foi extraida do proprio arquivo modelo
Nunes_Lucato_Bioma_Textil_Ecoponto_Belezinho.pptx.pdf, slides 2 e 8.

Saida: slides-projeto-leroy-merlin.pdf (1440 x 810 pt, 2 paginas)
"""
import io
import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(BASE)
OUT = os.path.join(BASE, "slides-projeto-leroy-merlin.pdf")

# ---------------------------------------------------------------- identidade
W, H = 1440.0, 810.0
MARGIN = 91.5
RIGHT = 1348.5

AZUL = (0.2039, 0.1961, 0.7882)        # #3432C9 destaque
NAVY = (0.0784, 0.0784, 0.1804)        # #14142E titulos
CINZA = (0.4314, 0.4471, 0.5333)       # #6E7288 corpo
CINZA_MED = (0.2275, 0.2353, 0.3333)   # #3A3C55 rotulos
CINZA_CLARO = (0.6039, 0.6157, 0.6902) # #9A9DB0 legendas
LINHA = (0.8745, 0.8863, 0.9412)       # #DFE2F0 divisorias
VERDE = (0.0706, 0.6588, 0.4824)       # #12A87B upcycle
BANDA = (0.9647, 0.9686, 0.9843)       # fundo da linha de total

SZ_KICKER, SZ_TITULO, SZ_CORPO = 13.5, 38.3, 16.2
SZ_SECAO, SZ_NUM, SZ_CARD_T = 20.3, 30.0, 15.9
SZ_CARD_D, SZ_RODAPE, SZ_LEGENDA, SZ_ROTULO = 13.0, 11.3, 11.7, 14.7

FONTES = {
    "light": "Montserrat-Light",
    "regular": "Montserrat-Regular",
    "medium": "Montserrat-Medium",
    "semibold": "Montserrat-SemiBold",
}
for chave, arq in FONTES.items():
    pdfmetrics.registerFont(TTFont(arq, os.path.join(BASE, "fontes", arq + ".ttf")))

LOGO = os.path.join(BASE, "logo-nunes-lucato.png")
FOTO_NECESSAIRE = os.path.join(REPO, "IMG-20260928-WA0153.jpg")
FOTO_ECOBAG = os.path.join(REPO, "IMG-20260928-WA0154.jpg")

RODAPE_TXT = "Projeto Leroy Merlin  \u00b7  Upcycle de Uniformes"


# ------------------------------------------------------------------ ajudantes
def Y(y):
    """Converte coordenada medida do topo para o sistema do reportlab."""
    return H - y


def base(y_topo, tamanho):
    """Baseline a partir do topo da caixa de texto, proporcao do modelo."""
    return y_topo + 0.78 * tamanho


def texto(c, x, y_base, s, fonte="regular", tam=SZ_CORPO, cor=CINZA, espaco=0):
    c.setFillColorRGB(*cor)
    if espaco:
        t = c.beginText(x, Y(y_base))
        t.setFont(FONTES[fonte], tam)
        t.setFillColorRGB(*cor)
        t.setCharSpace(espaco)
        t.textOut(s)
        t.setCharSpace(0)  # Tc faz parte do estado de texto e vazaria no resto do PDF
        c.drawText(t)
    else:
        c.setFont(FONTES[fonte], tam)
        c.drawString(x, Y(y_base), s)
    return x + pdfmetrics.stringWidth(s, FONTES[fonte], tam) + espaco * len(s)


def texto_dir(c, x_dir, y_base, s, fonte="regular", tam=SZ_CORPO, cor=CINZA):
    c.setFont(FONTES[fonte], tam)
    c.setFillColorRGB(*cor)
    c.drawRightString(x_dir, Y(y_base), s)


def linha(c, x0, y, x1, cor=LINHA, w=0.75):
    c.setStrokeColorRGB(*cor)
    c.setLineWidth(w)
    c.line(x0, Y(y), x1, Y(y))


def kicker(c, s):
    linha(c, 91.4, 79.1, 124.7, AZUL, 1.5)
    texto(c, 141.6, base(67.6, SZ_KICKER), s, "regular", SZ_KICKER, AZUL, espaco=3.4)


def titulo(c, leve, forte):
    x = texto(c, MARGIN, base(107.1, SZ_TITULO), leve, "light", SZ_TITULO, NAVY)
    # o modelo usa Light no inicio e Regular no trecho de enfase, slide 2
    texto(c, x, base(107.1, SZ_TITULO), forte, "regular", SZ_TITULO, NAVY)


def rodape(c, numero):
    linha(c, 91.7, 732.8, 1349.4)
    c.drawImage(LOGO, 91.9, Y(777.7), width=133.9, height=27.6, mask=None)
    texto_dir(c, 1349.4, base(755.5, SZ_RODAPE),
              f"{RODAPE_TXT}    |    {numero}", "regular", SZ_RODAPE, CINZA_CLARO)


def secao(c, x, y_linha, x_fim, rotulo, complemento):
    """Rotulo de secao no padrao do slide 2, divisoria acima e texto abaixo."""
    linha(c, x, y_linha, x_fim)
    xf = texto(c, x, base(y_linha + 23.7, SZ_SECAO), rotulo, "regular", SZ_SECAO, AZUL)
    texto(c, xf, base(y_linha + 23.7, SZ_SECAO), complemento, "light", SZ_SECAO, NAVY)


def card(c, x, y, w, h, cor_barra):
    c.setFillColorRGB(1, 1, 1)
    c.rect(x, Y(y + h), w, h, stroke=0, fill=1)
    c.setStrokeColorRGB(*LINHA)
    c.setLineWidth(1.5)
    c.rect(x, Y(y + h), w, h, stroke=1, fill=0)
    c.setFillColorRGB(*cor_barra)
    c.rect(x + 0.8, Y(y + 6.8), w - 1.6, 6.0, stroke=0, fill=1)


def numero_grande(c, x, y_topo, num, unidade, cor_num=AZUL, tam=SZ_NUM):
    xf = texto(c, x, base(y_topo, tam), num, "light", tam, cor_num)
    texto(c, xf, base(y_topo, tam), "  " + unidade, "light", tam, CINZA)


def foto_recortada(c, caminho, x, y, w, h, moldura=True):
    """Recorta a foto no centro para preencher a area sem distorcer."""
    img = Image.open(caminho).convert("RGB")
    alvo = w / h
    atual = img.width / img.height
    if atual > alvo:
        nova_l = int(img.height * alvo)
        esq = (img.width - nova_l) // 2
        img = img.crop((esq, 0, esq + nova_l, img.height))
    else:
        nova_a = int(img.width / alvo)
        topo = int((img.height - nova_a) * 0.5)
        img = img.crop((0, topo, img.width, topo + nova_a))
    # reamostra para cerca de 2x o tamanho de exibicao e grava em JPEG,
    # senao o reportlab embute a foto sem compressao e o PDF fica pesado
    alvo_px = (int(w * 2), int(h * 2))
    if img.width > alvo_px[0]:
        img = img.resize(alvo_px, Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=88, optimize=True)
    buf.seek(0)
    c.drawImage(ImageReader(buf), x, Y(y + h), width=w, height=h, mask=None)
    if moldura:
        c.setStrokeColorRGB(*LINHA)
        c.setLineWidth(1.2)
        c.rect(x, Y(y + h), w, h, stroke=1, fill=0)


def icone_cabide(c, x, y, s):
    c.setStrokeColorRGB(*AZUL)
    c.setLineWidth(2.6)
    c.setLineCap(1)
    c.setLineJoin(1)
    p = c.beginPath()
    p.moveTo(x + s * 0.5, Y(y + s * 0.30))
    p.curveTo(x + s * 0.5, Y(y + s * 0.10), x + s * 0.32, Y(y + s * 0.02),
              x + s * 0.32, Y(y + s * 0.20))
    c.drawPath(p, stroke=1, fill=0)
    p = c.beginPath()
    p.moveTo(x + s * 0.03, Y(y + s * 0.80))
    p.lineTo(x + s * 0.5, Y(y + s * 0.34))
    p.lineTo(x + s * 0.97, Y(y + s * 0.80))
    p.lineTo(x + s * 0.03, Y(y + s * 0.80))
    c.drawPath(p, stroke=1, fill=0)


def icone_moletom(c, x, y, s):
    c.setStrokeColorRGB(*AZUL)
    c.setLineWidth(2.6)
    c.setLineCap(1)
    c.setLineJoin(1)
    p = c.beginPath()
    p.moveTo(x + s * 0.26, Y(y + s * 0.18))
    p.lineTo(x + s * 0.03, Y(y + s * 0.46))
    p.lineTo(x + s * 0.20, Y(y + s * 0.60))
    c.drawPath(p, stroke=1, fill=0)
    p = c.beginPath()
    p.moveTo(x + s * 0.74, Y(y + s * 0.18))
    p.lineTo(x + s * 0.97, Y(y + s * 0.46))
    p.lineTo(x + s * 0.80, Y(y + s * 0.60))
    c.drawPath(p, stroke=1, fill=0)
    p = c.beginPath()
    p.moveTo(x + s * 0.26, Y(y + s * 0.18))
    p.lineTo(x + s * 0.26, Y(y + s * 0.96))
    p.lineTo(x + s * 0.74, Y(y + s * 0.96))
    p.lineTo(x + s * 0.74, Y(y + s * 0.18))
    c.drawPath(p, stroke=1, fill=0)
    p = c.beginPath()
    p.moveTo(x + s * 0.38, Y(y + s * 0.18))
    p.curveTo(x + s * 0.44, Y(y + s * 0.30), x + s * 0.56, Y(y + s * 0.30),
              x + s * 0.62, Y(y + s * 0.18))
    c.drawPath(p, stroke=1, fill=0)


def fundo(c):
    c.setFillColorRGB(1, 1, 1)
    c.rect(0, 0, W, H, stroke=0, fill=1)


# ------------------------------------------------------- slide 12, o projeto
def slide_projeto(c):
    fundo(c)
    kicker(c, "Projeto Leroy Merlin")
    titulo(c, "Upcycle de uniformes ", "inserv\u00edveis")
    texto(c, MARGIN, base(186.0, SZ_CORPO),
          "A Leroy Merlin envia os uniformes antigos inserv\u00edveis e a Nunes & Lucato "
          "devolve produtos acabados de maior valor agregado.",
          "regular", SZ_CORPO, CINZA)

    COL_L_X, COL_L_W = MARGIN, 595.0
    COL_R_X, COL_R_W = 753.5, 595.0
    Y_SEC = 228.0

    # ------------------------------------------------ coluna 1, recebidas
    secao(c, COL_L_X, Y_SEC, COL_L_X + COL_L_W, "Pe\u00e7as recebidas",
          "  \u00b7  uniformes inserv\u00edveis")

    itens = [
        (icone_cabide, "Jaqueta verde musgo", "626", "pe\u00e7as em estoque",
         "618 femininas e 8 masculinas", "495 metros de tecido"),
        (icone_moletom, "Moletom verde Leroy", "297", "pe\u00e7as em estoque",
         "37 femininos e 260 masculinos", "237 metros de tecido"),
    ]
    y = 292.0
    ALT = 150.0
    for icone, nome, num, uni, l1, l2 in itens:
        card(c, COL_L_X, y, COL_L_W, ALT, AZUL)
        icone(c, COL_L_X + 30, y + 54, 34)
        texto(c, COL_L_X + 92, base(y + 36, SZ_CARD_T), nome, "medium", SZ_CARD_T, NAVY)
        xf = texto(c, COL_L_X + 92, base(y + 66, 17.0), num, "medium", 17.0, AZUL)
        texto(c, xf, base(y + 66, 17.0), "  " + uni, "regular", SZ_CARD_D, CINZA)
        texto(c, COL_L_X + 92, base(y + 94, SZ_CARD_D), l1, "regular", SZ_CARD_D, CINZA)
        texto(c, COL_L_X + 92, base(y + 114, SZ_CARD_D), l2, "regular", SZ_CARD_D, CINZA)
        y += ALT + 22

    linha(c, COL_L_X, 636.0, COL_L_X + COL_L_W)
    numero_grande(c, COL_L_X, 658.0, "923", "uniformes", tam=26.0)
    numero_grande(c, COL_L_X + 290, 658.0, "732", "metros de tecido", tam=26.0)

    # -------------------------------------------------- coluna 2, criadas
    secao(c, COL_R_X, Y_SEC, COL_R_X + COL_R_W, "Pe\u00e7as criadas",
          "  \u00b7  produto acabado")

    produtos = [
        (FOTO_NECESSAIRE, "Necessaire", "1.250 pe\u00e7as"),
        (FOTO_ECOBAG, "Ecobag", "1.250 pe\u00e7as"),
    ]
    LARG = 287.0
    for i, (foto, nome, qtd) in enumerate(produtos):
        x = COL_R_X + i * (LARG + 21)
        card(c, x, 292.0, LARG, 402.0, VERDE)
        foto_recortada(c, foto, x + 0.8, 298.8, LARG - 1.6, 320.0, moldura=False)
        texto(c, x + 26, base(638.0, SZ_CARD_T), nome, "medium", SZ_CARD_T, NAVY)
        texto(c, x + 26, base(663.0, SZ_CARD_D), qtd, "regular", SZ_CARD_D, CINZA)

    rodape(c, 12)
    c.showPage()


# --------------------------------------------------- slide 13, volume e valores
def slide_valores(c):
    fundo(c)
    kicker(c, "Volume e valores")
    titulo(c, "Produ\u00e7\u00e3o e ", "investimento do projeto")
    texto(c, MARGIN, base(186.0, SZ_CORPO),
          "Produ\u00e7\u00e3o de 2.500 acess\u00f3rios, 1.250 de cada item, "
          "integralmente a partir dos uniformes recebidos.",
          "regular", SZ_CORPO, CINZA)

    TAB_X, TAB_FIM = MARGIN, 900.0
    C_QTD, C_UNIT, C_TOT = 505.0, 700.0, 900.0

    secao(c, TAB_X, 228.0, TAB_FIM, "Valores por item", "  \u00b7  pre\u00e7o unit\u00e1rio")

    # cabecalho
    texto(c, TAB_X, base(292.0, SZ_ROTULO), "Item", "medium", SZ_ROTULO, NAVY)
    for x, rot in ((C_QTD, "Quantidade"), (C_UNIT, "Valor unit\u00e1rio"),
                   (C_TOT, "Valor total")):
        texto_dir(c, x, base(292.0, SZ_ROTULO), rot, "medium", SZ_ROTULO, NAVY)
    linha(c, TAB_X, 322.0, TAB_FIM)

    linhas = [
        ("Necessaire", "1.250", "R$ 25,00", "R$ 31.250,00"),
        ("Ecobag", "1.250", "R$ 20,00", "R$ 25.000,00"),
    ]
    y = 352.0
    for nome, qtd, unit, tot in linhas:
        texto(c, TAB_X, base(y, 17.0), nome, "regular", 17.0, CINZA_MED)
        for x, val in ((C_QTD, qtd), (C_UNIT, unit), (C_TOT, tot)):
            texto_dir(c, x, base(y, 17.0), val, "regular", 17.0, CINZA_MED)
        y += 26.0
        linha(c, TAB_X, y + 10, TAB_FIM)
        y += 34.0

    # linha de total
    c.setFillColorRGB(*BANDA)
    c.rect(TAB_X, Y(y + 54), TAB_FIM - TAB_X, 54, stroke=0, fill=1)
    texto(c, TAB_X + 14, base(y + 17, 17.0), "Total", "medium", 17.0, NAVY)
    for x, val in ((C_QTD, "2.500"), (C_TOT, "R$ 56.250,00")):
        texto_dir(c, x, base(y + 17, 17.0), val, "medium", 17.0, NAVY)

    linha(c, TAB_X, 540.0, TAB_FIM)
    numero_grande(c, TAB_X, 561.0, "2.500", "acess\u00f3rios produzidos", tam=26.0)
    numero_grande(c, TAB_X, 604.0, "923", "uniformes reaproveitados", tam=26.0)

    texto(c, TAB_X, base(660.0, SZ_ROTULO),
          "Volume originado integralmente do reaproveitamento dos uniformes, "
          "sem consumo de mat\u00e9ria-prima nova.",
          "regular", SZ_ROTULO, CINZA_CLARO)

    # foto de apoio
    foto_recortada(c, FOTO_ECOBAG, 960.0, 244.0, 388.5, 416.0)
    texto(c, 960.0, base(670.0, SZ_LEGENDA),
          "Ecobag produzida a partir do moletom verde Leroy",
          "regular", SZ_LEGENDA, CINZA_CLARO)

    rodape(c, 13)
    c.showPage()


def main():
    c = canvas.Canvas(OUT, pagesize=(W, H))
    c.setTitle("Projeto Leroy Merlin, Nunes & Lucato")
    slide_projeto(c)
    slide_valores(c)
    c.save()
    print("gerado:", OUT)


if __name__ == "__main__":
    main()
