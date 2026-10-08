#!/usr/bin/env python3
"""
Gera um mockup de anúncio da OLX usando a foto da cuia Sadhu.
Brincadeira, não é material oficial nem afiliado à OLX.

A altura final é calculada a partir do conteúdo, então a barra de
botões nunca cobre a descrição ou o card do vendedor.
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------- caminhos
AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
FOTO = RAIZ / "WhatsApp Image 2026-10-08 at 10.50.34.jpeg"
SAIDA = AQUI / "anuncio-olx-cuia.png"
FONTES = Path("/usr/share/fonts/google-noto")


def fonte(nome, tamanho):
    return ImageFont.truetype(str(FONTES / f"NotoSans-{nome}.ttf"), tamanho)


# ---------------------------------------------------------------- paleta
ROXO = (110, 10, 214)
ROXO_CLARO = (243, 234, 253)
BRANCO = (255, 255, 255)
PRETO_TEXTO = (30, 30, 30)
CINZA_TEXTO = (60, 60, 60)
CINZA = (118, 118, 118)
CINZA_LINHA = (228, 228, 228)
FUNDO_FOTO = (18, 18, 18)
VERDE_BG = (226, 247, 231)
VERDE_TXT = (21, 128, 61)

L = 1080
MARGEM = 48
ALTURA_BARRA = 176
CANVAS = 3200  # rascunho generoso, cortado no final

# ---------------------------------------------------------------- conteúdo
PRECO = "R$ 1,50"
SELO = "Preço bom, 97% abaixo da média"
TITULO = "Cuia Sadhu de silicone inquebrável, tamanho pequeno"
LOCAL = "Barão Geraldo, Campinas, SP"
DATA = "Publicado hoje às 10:51"
VENDEDOR = "Matteo"
VENDEDOR_SUB = "Na OLX desde outubro de 2026"
DESCRICAO = (
    "Cuia de silicone Sadhu, azul e amarela. Não quebra de jeito nenhum. "
    "Já caiu da mesa, da cadeira e até da escada, continua inteirinha.\n"
    "\n"
    "Estado: usada, mas lavada. Juro.\n"
    "Motivo da venda: comprei duas achando que vinha par.\n"
    "Aceito PIX ou R$ 1,50 em moedinha.\n"
    "\n"
    "Não entrego e não envio. Vem buscar que a gente roda um mate."
)

# ---------------------------------------------------------------- fontes
f_status = fonte("SemiBold", 30)
f_logo = fonte("Black", 54)
f_preco = fonte("Black", 86)
f_badge = fonte("Bold", 30)
f_titulo = fonte("SemiBold", 44)
f_meta = fonte("Regular", 30)
f_sec = fonte("Bold", 34)
f_desc = fonte("Regular", 32)
f_vend = fonte("SemiBold", 34)
f_vend_sub = fonte("Regular", 28)
f_botao = fonte("Bold", 38)
f_contador = fonte("SemiBold", 28)

img = Image.new("RGB", (L, CANVAS), BRANCO)
d = ImageDraw.Draw(img)


def largura(texto, f):
    x0, _, x1, _ = d.textbbox((0, 0), texto, font=f)
    return x1 - x0


def centro(texto, f, x_ini, x_fim, y, cor, desenho=None):
    (desenho or d).text(
        ((x_ini + x_fim) / 2 - largura(texto, f) / 2, y), texto, font=f, fill=cor
    )


def quebra(texto, f, max_larg):
    """Quebra o texto respeitando parágrafos (linha vazia vira espaço)."""
    linhas = []
    for paragrafo in texto.split("\n"):
        if not paragrafo.strip():
            linhas.append("")
            continue
        atual = ""
        for palavra in paragrafo.split():
            teste = f"{atual} {palavra}".strip()
            if largura(teste, f) <= max_larg:
                atual = teste
            else:
                linhas.append(atual)
                atual = palavra
        if atual:
            linhas.append(atual)
    return linhas


# ================================================= 1. barra de status
d.text((MARGEM - 8, 12), "10:51", font=f_status, fill=PRETO_TEXTO)

bx = L - 230
for i, h in enumerate((12, 18, 24)):
    d.rectangle([bx + i * 16, 38 - h, bx + i * 16 + 10, 38], fill=PRETO_TEXTO)

wx = L - 138
for r in (22, 15, 8):
    d.arc([wx - r, 34 - r, wx + r, 34 + r], 210, 330, fill=PRETO_TEXTO, width=5)
d.ellipse([wx - 3, 31, wx + 3, 37], fill=PRETO_TEXTO)

d.rounded_rectangle([L - 108, 14, L - 52, 40], radius=6, outline=PRETO_TEXTO, width=4)
d.rectangle([L - 50, 22, L - 44, 32], fill=PRETO_TEXTO)
d.rounded_rectangle([L - 103, 19, L - 72, 35], radius=3, fill=PRETO_TEXTO)

# ================================================= 2. header
HEADER_BASE = 172
cy = (56 + HEADER_BASE) // 2

d.line([(52, cy), (104, cy)], fill=PRETO_TEXTO, width=6)
d.line([(52, cy), (74, cy - 22)], fill=PRETO_TEXTO, width=6)
d.line([(52, cy), (74, cy + 22)], fill=PRETO_TEXTO, width=6)

centro("OLX", f_logo, 0, L, cy - 36, ROXO)

sx, sy = L - 190, cy
d.line([(sx - 18, sy + 6), (sx + 18, sy - 14)], fill=PRETO_TEXTO, width=5)
d.line([(sx - 18, sy - 2), (sx + 18, sy + 18)], fill=PRETO_TEXTO, width=5)
for px, py in ((sx - 22, sy + 2), (sx + 22, sy - 18), (sx + 22, sy + 22)):
    d.ellipse([px - 10, py - 10, px + 10, py + 10], fill=BRANCO, outline=PRETO_TEXTO, width=5)

hx, hy = L - 78, cy - 6
d.ellipse([hx - 24, hy - 16, hx - 2, hy + 6], outline=PRETO_TEXTO, width=5)
d.ellipse([hx + 2, hy - 16, hx + 24, hy + 6], outline=PRETO_TEXTO, width=5)
d.polygon([(hx - 21, hy + 2), (hx + 21, hy + 2), (hx, hy + 28)], fill=BRANCO)
d.line([(hx - 21, hy + 1), (hx, hy + 28)], fill=PRETO_TEXTO, width=5)
d.line([(hx + 21, hy + 1), (hx, hy + 28)], fill=PRETO_TEXTO, width=5)

# ================================================= 3. foto
FOTO_ALTURA = 900
FOTO_BASE = HEADER_BASE + FOTO_ALTURA
d.rectangle([0, HEADER_BASE, L, FOTO_BASE], fill=FUNDO_FOTO)

original = Image.open(FOTO).convert("RGB")
escala = FOTO_ALTURA / original.height
nova = original.resize((round(original.width * escala), FOTO_ALTURA), Image.LANCZOS)
img.paste(nova, ((L - nova.width) // 2, HEADER_BASE))

cont = "1 / 1"
cw = largura(cont, f_contador)
d.rounded_rectangle(
    [L - 60 - cw - 48, FOTO_BASE - 86, L - 60, FOTO_BASE - 28], radius=29, fill=(0, 0, 0)
)
d.text((L - 60 - cw - 24, FOTO_BASE - 74), cont, font=f_contador, fill=BRANCO)

# ================================================= 4. preço e selo
y = FOTO_BASE + 44
d.text((MARGEM, y), PRECO, font=f_preco, fill=PRETO_TEXTO)
y += 118

sw = largura(SELO, f_badge)
d.rounded_rectangle([MARGEM, y, MARGEM + sw + 76, y + 58], radius=29, fill=VERDE_BG)
ax, ay = MARGEM + 30, y + 29
d.line([(ax, ay - 14), (ax, ay + 6)], fill=VERDE_TXT, width=5)
d.polygon([(ax - 10, ay + 2), (ax + 10, ay + 2), (ax, ay + 18)], fill=VERDE_TXT)
d.text((MARGEM + 52, y + 12), SELO, font=f_badge, fill=VERDE_TXT)
y += 96

# ================================================= 5. título e meta
for linha in quebra(TITULO, f_titulo, L - 2 * MARGEM):
    d.text((MARGEM, y), linha, font=f_titulo, fill=PRETO_TEXTO)
    y += 56
y += 10

d.text((MARGEM, y), LOCAL, font=f_meta, fill=CINZA)
y += 42
d.text((MARGEM, y), DATA, font=f_meta, fill=CINZA)
y += 62

d.line([(MARGEM, y), (L - MARGEM, y)], fill=CINZA_LINHA, width=3)
y += 40

# ================================================= 6. descrição
d.text((MARGEM, y), "Descrição", font=f_sec, fill=PRETO_TEXTO)
y += 58

for linha in quebra(DESCRICAO, f_desc, L - 2 * MARGEM):
    if linha:
        d.text((MARGEM, y), linha, font=f_desc, fill=CINZA_TEXTO)
    y += 46
y += 20

d.line([(MARGEM, y), (L - MARGEM, y)], fill=CINZA_LINHA, width=3)
y += 40

# ================================================= 7. vendedor
d.ellipse([MARGEM, y, MARGEM + 88, y + 88], fill=ROXO_CLARO)
centro(VENDEDOR[0], f_vend, MARGEM, MARGEM + 88, y + 22, ROXO)
d.text((MARGEM + 116, y + 12), VENDEDOR, font=f_vend, fill=PRETO_TEXTO)
d.text((MARGEM + 116, y + 54), VENDEDOR_SUB, font=f_vend_sub, fill=CINZA)
y += 88 + 44

# ================================================= 8. corta e fecha
A = y + ALTURA_BARRA
if A > CANVAS:
    raise SystemExit(f"conteúdo passou do canvas ({A} > {CANVAS})")
img = img.crop((0, 0, L, A))
d = ImageDraw.Draw(img)

BARRA = A - ALTURA_BARRA
d.rectangle([0, BARRA, L, A], fill=BRANCO)
d.line([(0, BARRA), (L, BARRA)], fill=CINZA_LINHA, width=3)

by0, by1 = BARRA + 36, A - 48
meio = L // 2
raio = (by1 - by0) // 2

d.rounded_rectangle([MARGEM, by0, meio - 14, by1], radius=raio, outline=ROXO, width=5)
centro("Ligar", f_botao, MARGEM, meio - 14, by0 + 22, ROXO)

d.rounded_rectangle([meio + 14, by0, L - MARGEM, by1], radius=raio, fill=ROXO)
centro("Chat", f_botao, meio + 14, L - MARGEM, by0 + 22, BRANCO)

img.save(SAIDA, "PNG", optimize=True)
print(f"gerado: {SAIDA.name} ({img.width}x{img.height})")
