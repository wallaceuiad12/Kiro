#!/usr/bin/env python3
"""
Gera a apresentacao do Projeto Leroy Merlin na identidade visual da Nunes & Lucato.

4 slides, capa, introducao, o projeto detalhado e volume e valores.

Toda a geometria, paleta e tipografia foi extraida do proprio arquivo modelo
Nunes_Lucato_Bioma_Textil_Ecoponto_Belezinho.pptx.pdf, capa e slides 2 e 8.

Saida: slides-projeto-leroy-merlin.pdf (1440 x 810 pt, 4 paginas)
"""
import io
import os
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
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
BRANCO = (1, 1, 1)

# gradiente da capa, amostrado do arquivo modelo
CAPA_INICIO = (9, 8, 23)
CAPA_FIM = (46, 44, 212)
CAPA_EXPOENTE = 1.9

SZ_KICKER, SZ_TITULO, SZ_CORPO = 13.5, 38.3, 16.2
SZ_CAPA_TIT, SZ_CAPA_SUB = 49.5, 21.0
SZ_SECAO, SZ_NUM, SZ_CARD_T = 20.3, 30.0, 15.9
SZ_CARD_D, SZ_RODAPE, SZ_LEGENDA, SZ_ROTULO = 13.0, 11.3, 11.7, 14.7
SZ_GRADE = 11.7

FONTES = {
    "light": "Montserrat-Light",
    "regular": "Montserrat-Regular",
    "medium": "Montserrat-Medium",
    "semibold": "Montserrat-SemiBold",
}
for chave, arq in FONTES.items():
    pdfmetrics.registerFont(TTFont(arq, os.path.join(BASE, "fontes", arq + ".ttf")))

LOGO_ESCURO = os.path.join(BASE, "logo-nunes-escuro.png")
LOGO_BRANCO = os.path.join(BASE, "logo-nunes-branco.png")
LOGO_LEROY = os.path.join(BASE, "leroy-merlin-logo.svg")
FOTO_NECESSAIRE = os.path.join(REPO, "IMG-20260928-WA0153.jpg")
FOTO_ECOBAG = os.path.join(REPO, "IMG-20260928-WA0154.jpg")
MOCKUP = os.path.join(BASE, "mockup-produto-final.png")

RODAPE_TXT = "Projeto Leroy Merlin  \u00b7  Upcycle de Uniformes"

# posicao fixa do logotipo do cliente, igual em todos os slides depois da capa
LEROY_X, LEROY_Y, LEROY_W = 1248.5, 100.0, 100.0


# ------------------------------------------------------------------ ajudantes
def Y(y):
    return H - y


def base(y_topo, tamanho):
    """Baseline a partir do topo da caixa de texto, proporcao medida no modelo."""
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


def paragrafo(c, x, y_base, largura, s, fonte="regular", tam=SZ_CORPO,
              cor=CINZA, entrelinha=None):
    """Quebra o texto na largura disponivel, evita invadir a coluna da foto."""
    entrelinha = entrelinha or tam * 1.66
    palavras = s.split()
    linhas, atual = [], ""
    for pal in palavras:
        teste = (atual + " " + pal).strip()
        if pdfmetrics.stringWidth(teste, FONTES[fonte], tam) <= largura:
            atual = teste
        else:
            linhas.append(atual)
            atual = pal
    if atual:
        linhas.append(atual)
    for i, l in enumerate(linhas):
        texto(c, x, y_base + i * entrelinha, l, fonte, tam, cor)
    return y_base + (len(linhas) - 1) * entrelinha


def texto_dir(c, x_dir, y_base, s, fonte="regular", tam=SZ_CORPO, cor=CINZA):
    c.setFont(FONTES[fonte], tam)
    c.setFillColorRGB(*cor)
    c.drawRightString(x_dir, Y(y_base), s)


def linha(c, x0, y, x1, cor=LINHA, w=0.75):
    c.setStrokeColorRGB(*cor)
    c.setLineWidth(w)
    c.line(x0, Y(y), x1, Y(y))


def kicker(c, s, cor=AZUL, y=67.6, tam=SZ_KICKER):
    linha(c, 91.4, y + 11.5, 124.7, cor, 1.5)
    texto(c, 141.6, base(y, tam), s, "regular", tam, cor, espaco=3.4)


def titulo(c, leve, forte, y=107.1, tam=SZ_TITULO, cor=NAVY):
    """Light no inicio e Regular no trecho de enfase, como no slide 2 do modelo."""
    x = texto(c, MARGIN, base(y, tam), leve, "light", tam, cor)
    texto(c, x, base(y, tam), forte, "regular", tam, cor)


def rodape(c, numero):
    linha(c, 91.7, 732.8, 1349.4)
    c.drawImage(LOGO_ESCURO, 91.9, Y(777.7), width=133.9, height=27.6, mask="auto")
    texto_dir(c, 1349.4, base(755.5, SZ_RODAPE),
              f"{RODAPE_TXT}    |    {numero:02d}", "regular", SZ_RODAPE, CINZA_CLARO)


def secao(c, x, y_linha, x_fim, rotulo, complemento):
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


def _preenche(img, w, h, ancora=0.5):
    """Recorta no centro para preencher a area sem distorcer."""
    alvo = w / h
    atual = img.width / img.height
    if atual > alvo:
        nova_l = int(img.height * alvo)
        esq = int((img.width - nova_l) * 0.5)
        img = img.crop((esq, 0, esq + nova_l, img.height))
    elif atual < alvo:
        nova_a = int(img.width / alvo)
        topo = int((img.height - nova_a) * ancora)
        img = img.crop((0, topo, img.width, topo + nova_a))
    alvo_px = (max(1, int(w * 2)), max(1, int(h * 2)))
    if img.width > alvo_px[0]:
        img = img.resize(alvo_px, Image.LANCZOS)
    return img


def _desenha_jpeg(c, img, x, y, w, h):
    buf = io.BytesIO()
    img.convert("RGB").save(buf, format="JPEG", quality=88, optimize=True)
    buf.seek(0)
    c.drawImage(ImageReader(buf), x, Y(y + h), width=w, height=h, mask=None)


def foto(c, caminho, x, y, w, h, moldura=True, ancora=0.5):
    img = _preenche(Image.open(caminho).convert("RGB"), w, h, ancora)
    _desenha_jpeg(c, img, x, y, w, h)
    if moldura:
        c.setStrokeColorRGB(*LINHA)
        c.setLineWidth(1.2)
        c.rect(x, Y(y + h), w, h, stroke=1, fill=0)


def logo_cliente(c):
    """Logotipo da Leroy Merlin no topo direito, co-marca da proposta."""
    logo_leroy(c, LEROY_X, LEROY_Y, LEROY_W)


def logo_leroy(c, x, y, largura):
    """Logo oficial em vetor, dominio publico (Wikimedia Commons)."""
    d = svg2rlg(LOGO_LEROY)
    k = largura / d.width
    d.width *= k
    d.height *= k
    d.scale(k, k)
    renderPDF.draw(d, c, x, Y(y + d.height))
    return d.height


def icone_cabide(c, x, y, s, cor=AZUL):
    c.setStrokeColorRGB(*cor)
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


def icone_moletom(c, x, y, s, cor=AZUL):
    c.setStrokeColorRGB(*cor)
    c.setLineWidth(2.6)
    c.setLineCap(1)
    c.setLineJoin(1)
    for pontos in (
        [(0.26, 0.18), (0.03, 0.46), (0.20, 0.60)],
        [(0.74, 0.18), (0.97, 0.46), (0.80, 0.60)],
        [(0.26, 0.18), (0.26, 0.96), (0.74, 0.96), (0.74, 0.18)],
    ):
        p = c.beginPath()
        p.moveTo(x + s * pontos[0][0], Y(y + s * pontos[0][1]))
        for px, py in pontos[1:]:
            p.lineTo(x + s * px, Y(y + s * py))
        c.drawPath(p, stroke=1, fill=0)
    p = c.beginPath()
    p.moveTo(x + s * 0.38, Y(y + s * 0.18))
    p.curveTo(x + s * 0.44, Y(y + s * 0.30), x + s * 0.56, Y(y + s * 0.30),
              x + s * 0.62, Y(y + s * 0.18))
    c.drawPath(p, stroke=1, fill=0)


def icone_caminhao(c, x, y, s, cor=AZUL):
    c.setStrokeColorRGB(*cor)
    c.setLineWidth(2.6)
    c.setLineCap(1)
    c.setLineJoin(1)
    c.rect(x, Y(y + s * 0.72), s * 0.56, s * 0.46, stroke=1, fill=0)
    p = c.beginPath()
    p.moveTo(x + s * 0.58, Y(y + s * 0.72))
    p.lineTo(x + s * 0.76, Y(y + s * 0.72))
    p.lineTo(x + s, Y(y + s * 0.50))
    p.lineTo(x + s, Y(y + s * 0.26))
    p.lineTo(x + s * 0.58, Y(y + s * 0.26))
    c.drawPath(p, stroke=1, fill=0)
    for cx in (0.20, 0.78):
        c.circle(x + s * cx, Y(y + s * 0.85), s * 0.10, stroke=1, fill=0)


def icone_tesoura(c, x, y, s, cor=AZUL):
    c.setStrokeColorRGB(*cor)
    c.setLineWidth(2.6)
    c.setLineCap(1)
    p = c.beginPath()
    p.moveTo(x + s * 0.12, Y(y + s * 0.05))
    p.lineTo(x + s * 0.80, Y(y + s * 0.72))
    c.drawPath(p, stroke=1, fill=0)
    p = c.beginPath()
    p.moveTo(x + s * 0.80, Y(y + s * 0.05))
    p.lineTo(x + s * 0.12, Y(y + s * 0.72))
    c.drawPath(p, stroke=1, fill=0)
    c.circle(x + s * 0.20, Y(y + s * 0.88), s * 0.14, stroke=1, fill=0)
    c.circle(x + s * 0.74, Y(y + s * 0.88), s * 0.14, stroke=1, fill=0)


def icone_etiqueta(c, x, y, s, cor=AZUL):
    c.setStrokeColorRGB(*cor)
    c.setLineWidth(2.6)
    c.setLineJoin(1)
    p = c.beginPath()
    p.moveTo(x + s * 0.05, Y(y + s * 0.42))
    p.lineTo(x + s * 0.48, Y(y + s * 0.02))
    p.lineTo(x + s * 0.98, Y(y + s * 0.52))
    p.lineTo(x + s * 0.55, Y(y + s * 0.95))
    p.lineTo(x + s * 0.05, Y(y + s * 0.42))
    c.drawPath(p, stroke=1, fill=0)
    c.circle(x + s * 0.34, Y(y + s * 0.40), s * 0.09, stroke=1, fill=0)


def icone_sacola(c, x, y, s, cor=VERDE):
    """Sacola de produto acabado, mais legivel que um simbolo abstrato."""
    c.setStrokeColorRGB(*cor)
    c.setLineWidth(2.6)
    c.setLineCap(1)
    c.setLineJoin(1)
    c.rect(x + s * 0.10, Y(y + s * 0.96), s * 0.80, s * 0.62, stroke=1, fill=0)
    p = c.beginPath()
    p.moveTo(x + s * 0.32, Y(y + s * 0.34))
    p.curveTo(x + s * 0.32, Y(y + s * 0.02), x + s * 0.68, Y(y + s * 0.02),
              x + s * 0.68, Y(y + s * 0.34))
    c.drawPath(p, stroke=1, fill=0)


def fundo_branco(c):
    c.setFillColorRGB(1, 1, 1)
    c.rect(0, 0, W, H, stroke=0, fill=1)


# ------------------------------------------------------------------- slide 1
def fundo_capa(c):
    """Gradiente horizontal e textura diagonal, como na capa do modelo."""
    larg = 360
    grad = Image.new("RGB", (larg, 2))
    for i in range(larg):
        t = (i / (larg - 1)) ** CAPA_EXPOENTE
        cor = tuple(int(CAPA_INICIO[k] + (CAPA_FIM[k] - CAPA_INICIO[k]) * t)
                    for k in range(3))
        grad.putpixel((i, 0), cor)
        grad.putpixel((i, 1), cor)
    c.drawImage(ImageReader(grad), 0, 0, width=W, height=H, mask=None)

    c.saveState()
    c.setStrokeColorRGB(1, 1, 1)
    c.setStrokeAlpha(0.05)
    c.setLineWidth(1.0)
    passo = 49.7
    x = -H
    while x < W + H:
        c.line(x, 0, x + H, H)
        x += passo
    c.restoreState()


def duotone(caminho, w, h, escuro=(8, 7, 24), claro=(108, 106, 226), ancora=0.42):
    """Foto em monocromia azul, no tratamento da capa do modelo."""
    img = _preenche(Image.open(caminho).convert("RGB"), w, h, ancora).convert("L")
    lut = []
    for canal in range(3):
        lut += [int(escuro[canal] + (claro[canal] - escuro[canal]) * (i / 255))
                for i in range(256)]
    return img.convert("RGB").point(lut)


def slide_capa(c):
    fundo_capa(c)

    # painel de foto na direita, em monocromia azul como na capa do modelo
    px, pw = 870.0, W - 870.0
    _desenha_jpeg(c, duotone(FOTO_ECOBAG, pw, H), px, 0, pw, H)

    kicker(c, "Proposta comercial  \u00b7  Leroy Merlin", BRANCO, y=149.5, tam=12.9)

    texto(c, MARGIN, base(193.4, SZ_CAPA_TIT), "Projeto", "light",
          SZ_CAPA_TIT, BRANCO)
    texto(c, MARGIN, base(260.9, SZ_CAPA_TIT), "Leroy Merlin", "regular",
          SZ_CAPA_TIT, BRANCO)

    linha(c, MARGIN, 410.0, MARGIN + 110, BRANCO, 1.0)
    texto(c, MARGIN, base(452.0, SZ_CAPA_SUB),
          "Upcycle de uniformes inserv\u00edveis em acess\u00f3rios",
          "light", SZ_CAPA_SUB, BRANCO)
    texto(c, MARGIN, base(485.8, SZ_CAPA_SUB),
          "de maior valor agregado", "light", SZ_CAPA_SUB, BRANCO)

    texto(c, MARGIN, base(645.4, 12.3), "Proposta apresentada pela", "regular",
          12.3, BRANCO, espaco=3.2)
    c.drawImage(LOGO_BRANCO, 91.9, Y(724.2), width=210.2, height=43.3, mask="auto")
    c.showPage()


# ------------------------------------------------------------------- slide 2
def slide_introducao(c):
    fundo_branco(c)
    kicker(c, "Introdu\u00e7\u00e3o")
    titulo(c, "Quem somos e ", "o que propomos")
    logo_cliente(c)

    paragrafo(c, MARGIN, base(213.0, SZ_CORPO), 700.0,
              "A Nunes & Lucato atua na cadeia de res\u00edduos t\u00eaxteis com "
              "estrutura pr\u00f3pria de transforma\u00e7\u00e3o, equipe treinada e "
              "rastreabilidade documental completa, da coleta \u00e0 "
              "destina\u00e7\u00e3o final ambientalmente adequada.",
              "regular", SZ_CORPO, CINZA, entrelinha=27.0)

    linha(c, MARGIN, 330.0, 790.0)
    xf = texto(c, MARGIN, base(353.7, SZ_SECAO), "Do uniforme ao produto acabado",
               "regular", SZ_SECAO, AZUL)
    texto(c, xf, base(353.7, SZ_SECAO), "  \u00b7  com respaldo documental",
          "light", SZ_SECAO, NAVY)

    paragrafo(c, MARGIN, base(410.0, SZ_ROTULO), 700.0,
              "A Leroy Merlin envia os uniformes antigos inserv\u00edveis. A Nunes & "
              "Lucato descaracteriza, transforma e devolve produtos acabados, com "
              "atestado de descaracteriza\u00e7\u00e3o e documenta\u00e7\u00e3o "
              "ambiental de todo o processo.",
              "regular", SZ_ROTULO, CINZA, entrelinha=22.0)

    foto(c, FOTO_NECESSAIRE, 880.0, 200.0, 468.5, 272.0, ancora=0.46)
    texto(c, 880.0, base(482.0, SZ_LEGENDA),
          "Necessaire produzida a partir da jaqueta verde musgo",
          "regular", SZ_LEGENDA, CINZA_CLARO)

    etapas = [
        (icone_caminhao, "Coleta e transporte",
         ["Recebimento dos uniformes", "com emiss\u00e3o de MTR."], AZUL),
        (icone_etiqueta, "Descaracteriza\u00e7\u00e3o",
         ["Remo\u00e7\u00e3o de logos e etiquetas,", "pe\u00e7a por pe\u00e7a."], AZUL),
        (icone_tesoura, "Corte e costura",
         ["Produ\u00e7\u00e3o por artes\u00e3s", "capacitadas pela equipe."], AZUL),
        (icone_sacola, "Produto acabado",
         ["Necessaire e ecobag", "prontas para uso."], VERDE),
    ]
    LARG, PASSO, TOPO, ALT = 295.2, 320.5, 528.0, 172.0
    for i, (icone, nome, linhas, cor) in enumerate(etapas):
        x = 91.1 + i * PASSO
        card(c, x, TOPO, LARG, ALT, cor)
        icone(c, x + 26.7, TOPO + 36, 26, cor)
        texto(c, x + 26.7, base(TOPO + 82, SZ_CARD_T), nome, "regular",
              SZ_CARD_T, NAVY)
        for j, l in enumerate(linhas):
            texto(c, x + 26.7, base(TOPO + 114 + j * 19.5, SZ_CARD_D), l,
                  "regular", SZ_CARD_D, CINZA)

    rodape(c, 2)
    c.showPage()


# ------------------------------------------------------------------- slide 3
def slide_projeto(c):
    fundo_branco(c)
    kicker(c, "Projeto Leroy Merlin")
    titulo(c, "Upcycle de uniformes ", "inserv\u00edveis")
    logo_cliente(c)

    texto(c, MARGIN, base(186.0, SZ_CORPO),
          "Estoque dispon\u00edvel de uniformes inserv\u00edveis, grade completa e "
          "mat\u00e9ria-prima apurada peça por peça.",
          "regular", SZ_CORPO, CINZA)

    COL_X, COL_W = MARGIN, 760.0
    DIR_X, DIR_W = 881.0, 467.5

    secao(c, COL_X, 228.0, COL_X + COL_W, "Pe\u00e7as recebidas",
          "  \u00b7  uniformes inserv\u00edveis")

    itens = [
        (icone_cabide, "Jaqueta verde musgo", "626",
         ("Feminina  618", "PP 47 \u00b7 P 141 \u00b7 M 205 \u00b7 G 141 \u00b7 GG 40 \u00b7 XG 44"),
         ("Masculina  8", "P 7 \u00b7 XGG 1"),
         "495 metros de tecido, cerca de 300 pe\u00e7as de produ\u00e7\u00e3o"),
        (icone_moletom, "Moletom verde Leroy", "297",
         ("Feminino  37", "XG 14 \u00b7 EG 13 \u00b7 EXG 10"),
         ("Masculino  260",
          "P 46 \u00b7 M 54 \u00b7 G 67 \u00b7 GG 13 \u00b7 XG 27 \u00b7 EG 4 \u00b7 EXG 27 \u00b7 EGG 22"),
         "237 metros de tecido, cerca de 415 pe\u00e7as de produ\u00e7\u00e3o"),
    ]
    y = 292.0
    ALT = 172.0
    for icone, nome, qtd, fem, masc, materia in itens:
        card(c, COL_X, y, COL_W, ALT, AZUL)
        icone(c, COL_X + 28, y + 52, 32)
        texto(c, COL_X + 92, base(y + 32, SZ_CARD_T), nome, "medium",
              SZ_CARD_T, NAVY)
        xf = texto(c, COL_X + 92, base(y + 58, 17.0), qtd, "medium", 17.0, AZUL)
        texto(c, xf, base(y + 58, 17.0), "  pe\u00e7as em estoque", "regular",
              SZ_CARD_D, CINZA)
        for j, (rot, grade) in enumerate((fem, masc)):
            yy = y + 88 + j * 20
            texto(c, COL_X + 92, base(yy, SZ_GRADE), rot, "medium",
                  SZ_GRADE, CINZA_MED)
            texto(c, COL_X + 200, base(yy, SZ_GRADE), grade, "regular",
                  SZ_GRADE, CINZA)
        linha(c, COL_X + 92, y + 136, COL_X + COL_W - 26)
        texto(c, COL_X + 92, base(y + 146, SZ_GRADE), "Mat\u00e9ria-prima",
              "medium", SZ_GRADE, CINZA_MED)
        texto(c, COL_X + 200, base(y + 146, SZ_GRADE), materia, "regular",
              SZ_GRADE, CINZA)
        y += ALT + 20

    linha(c, COL_X, 672.0, COL_X + COL_W)
    numero_grande(c, COL_X, 692.0, "923", "uniformes", tam=24.0)
    numero_grande(c, COL_X + 290, 692.0, "732", "metros de tecido", tam=24.0)

    # ------------------------------------------------------- pecas criadas
    secao(c, DIR_X, 228.0, DIR_X + DIR_W, "Pe\u00e7as criadas",
          "  \u00b7  produto acabado")

    card(c, DIR_X, 292.0, DIR_W, 392.0, VERDE)
    img = Image.open(MOCKUP).convert("RGB")
    _desenha_jpeg(c, _preenche(img, DIR_W - 1.6, 286.0), DIR_X + 0.8, 298.8,
                  DIR_W - 1.6, 286.0)

    for i, (nome, qtd) in enumerate((("Necessaire", "1.250 pe\u00e7as"),
                                     ("Ecobag", "1.250 pe\u00e7as"))):
        yy = 614.0 + i * 30
        c.setFillColorRGB(*VERDE)
        c.rect(DIR_X + 26, Y(yy + 2), 7, 7, stroke=0, fill=1)
        texto(c, DIR_X + 44, base(yy - 4, SZ_CARD_T), nome, "medium",
              SZ_CARD_T, NAVY)
        texto_dir(c, DIR_X + DIR_W - 26, base(yy - 4, SZ_CARD_D), qtd,
                  "regular", SZ_CARD_D, CINZA)

    rodape(c, 3)
    c.showPage()


# ------------------------------------------------------------------- slide 4
def slide_valores(c):
    fundo_branco(c)
    kicker(c, "Volume e valores")
    titulo(c, "Produ\u00e7\u00e3o e ", "investimento do projeto")
    logo_cliente(c)
    texto(c, MARGIN, base(186.0, SZ_CORPO),
          "Produ\u00e7\u00e3o de 2.500 acess\u00f3rios, 1.250 de cada item, "
          "integralmente a partir dos uniformes recebidos.",
          "regular", SZ_CORPO, CINZA)

    C_QTD, C_UNIT, C_TOT = 760.0, 1050.0, RIGHT

    secao(c, MARGIN, 228.0, RIGHT, "Valores por item", "  \u00b7  pre\u00e7o unit\u00e1rio")

    texto(c, MARGIN, base(300.0, SZ_ROTULO), "Item", "medium", SZ_ROTULO, NAVY)
    for x, rot in ((C_QTD, "Quantidade"), (C_UNIT, "Valor unit\u00e1rio"),
                   (C_TOT, "Valor total")):
        texto_dir(c, x, base(300.0, SZ_ROTULO), rot, "medium", SZ_ROTULO, NAVY)
    linha(c, MARGIN, 330.0, RIGHT)

    linhas = [
        ("Necessaire", "1.250", "R$ 25,00", "R$ 31.250,00"),
        ("Ecobag", "1.250", "R$ 20,00", "R$ 25.000,00"),
    ]
    y = 364.0
    for nome, qtd, unit, tot in linhas:
        texto(c, MARGIN, base(y, 17.0), nome, "regular", 17.0, CINZA_MED)
        for x, val in ((C_QTD, qtd), (C_UNIT, unit), (C_TOT, tot)):
            texto_dir(c, x, base(y, 17.0), val, "regular", 17.0, CINZA_MED)
        y += 26.0
        linha(c, MARGIN, y + 12, RIGHT)
        y += 36.0

    c.setFillColorRGB(*BANDA)
    c.rect(MARGIN, Y(y + 56), RIGHT - MARGIN, 56, stroke=0, fill=1)
    texto(c, MARGIN + 16, base(y + 18, 17.0), "Total", "medium", 17.0, NAVY)
    for x, val in ((C_QTD, "2.500"), (C_TOT, "R$ 56.250,00")):
        texto_dir(c, x - 16 if x == C_TOT else x, base(y + 18, 17.0), val,
                  "medium", 17.0, NAVY)

    linha(c, MARGIN, 568.0, RIGHT)
    metricas = [
        (MARGIN, "2.500", "acess\u00f3rios produzidos"),
        (MARGIN + 450, "923", "uniformes reaproveitados"),
        (MARGIN + 900, "732", "metros de tecido"),
    ]
    for x, num, uni in metricas:
        numero_grande(c, x, 590.0, num, uni, tam=24.0)

    texto(c, MARGIN, base(672.0, SZ_ROTULO),
          "Volume originado integralmente do reaproveitamento dos uniformes, "
          "sem consumo de mat\u00e9ria-prima nova.",
          "regular", SZ_ROTULO, CINZA_CLARO)

    rodape(c, 4)
    c.showPage()


def main():
    c = canvas.Canvas(OUT, pagesize=(W, H))
    c.setTitle("Projeto Leroy Merlin, Nunes & Lucato")
    slide_capa(c)
    slide_introducao(c)
    slide_projeto(c)
    slide_valores(c)
    c.save()
    print("gerado:", OUT)


if __name__ == "__main__":
    main()
