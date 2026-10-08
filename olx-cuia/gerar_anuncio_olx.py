#!/usr/bin/env python3
"""
Gera um mockup de anúncio da OLX usando a foto da cuia Sadhu.
Brincadeira, não é material oficial nem afiliado à OLX.

A interface imita um Android atual (Material 3), com barra de status do
Android, top app bar achatada, botões em formato pill e a barra de gestos
no rodapé. A altura final é calculada a partir do conteúdo, então a barra
de ações nunca cobre a descrição ou o card do vendedor.
"""

from pathlib import Path
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageFont

# ---------------------------------------------------------------- caminhos
AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
FOTO = RAIZ / "WhatsApp Image 2026-10-08 at 10.50.34.jpeg"
SAIDA = AQUI / "anuncio-olx-cuia.png"
FONTES = Path("/usr/share/fonts/google-noto")


def fonte(nome, tamanho):
    return ImageFont.truetype(str(FONTES / f"NotoSans-{nome}.ttf"), tamanho)


# ------------------------------------------------- paleta (Material 3)
ROXO = (110, 10, 214)
ROXO_CLARO = (237, 224, 251)
BRANCO = (255, 255, 255)
ON_SURFACE = (28, 27, 31)
ON_SURFACE_VAR = (73, 69, 79)
OUTLINE = (121, 116, 126)
OUTLINE_VAR = (228, 225, 230)
FUNDO_FOTO = (18, 18, 18)
VERDE_BG = (214, 245, 222)
VERDE_TXT = (16, 109, 52)
NAV_PILL = (28, 27, 31)

L = 1080
MARGEM = 48
H_STATUS = 72
H_APPBAR = 168
H_ACOES = 176
H_NAV = 72
CANVAS = 3400  # rascunho generoso, cortado no final

# ---------------------------------------------------------------- conteúdo
HORA = "10:51"
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
    "Motivo da venda: usei ela de copo de café uma única vez e agora todo "
    "mate que eu tomo tem gosto de café. Já lavei sete vezes, já deixei de "
    "molho, já pedi desculpa pra ela. Não tem volta.\n"
    "Aceito PIX ou R$ 1,50 em moedinha.\n"
    "\n"
    "Não entrego e não envio. Vem buscar que a gente roda um mate."
)

# ---------------------------------------------------------------- fontes
f_status = fonte("Medium", 32)
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


# ---------------------------------------------------------------- helpers
def largura(texto, f):
    x0, _, x1, _ = d.textbbox((0, 0), texto, font=f)
    return x1 - x0


def centro(texto, f, x_ini, x_fim, y, cor):
    d.text(((x_ini + x_fim) / 2 - largura(texto, f) / 2, y), texto, font=f, fill=cor)


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


def _mascara_coracao(lado, w):
    """Silhueta cheia de coração, centrada num quadrado de lado `lado`."""
    m = Image.new("L", (lado, lado), 0)
    dm = ImageDraw.Draw(m)
    cx = cy = lado / 2
    r = w * 0.28
    topo = cy - w * 0.18
    for dx in (-w * 0.22, w * 0.22):
        dm.ellipse([cx + dx - r, topo - r, cx + dx + r, topo + r], fill=255)
    dm.polygon(
        [(cx - w * 0.5, topo), (cx + w * 0.5, topo), (cx, cy + w * 0.52)], fill=255
    )
    return m


def coracao(base, cx, cy, w, cor, espessura=None):
    """
    Desenha um coração em (cx, cy). Sem `espessura` sai cheio; com
    `espessura` sai vazado, usando erosão da máscara para o contorno
    ficar com a mesma grossura em toda a volta.
    """
    S = 4  # supersample, suaviza as bordas
    lado = int(w * S * 1.7)
    m = _mascara_coracao(lado, w * S)
    if espessura:
        k = 2 * int(espessura * S) + 1
        m = ImageChops.subtract(m, m.filter(ImageFilter.MinFilter(k)))
    m = m.resize((lado // S, lado // S), Image.LANCZOS)
    base.paste(Image.new("RGB", m.size, cor), (int(cx - m.width / 2), int(cy - m.height / 2)), m)


# ======================================= 1. barra de status do Android
cy = H_STATUS // 2
d.text((MARGEM, cy - 21), HORA, font=f_status, fill=ON_SURFACE)

# ícones de notificação à esquerda, bem típico do Android
nx = MARGEM + largura(HORA, f_status) + 34
d.rounded_rectangle([nx, cy - 14, nx + 30, cy + 8], radius=8, fill=ON_SURFACE)
d.polygon([(nx + 6, cy + 7), (nx + 18, cy + 7), (nx + 6, cy + 18)], fill=ON_SURFACE)
nx += 50
d.line([(nx + 14, cy - 15), (nx + 14, cy + 6)], fill=ON_SURFACE, width=5)
d.polygon([(nx + 4, cy + 1), (nx + 24, cy + 1), (nx + 14, cy + 15)], fill=ON_SURFACE)
d.rectangle([nx, cy + 17, nx + 28, cy + 22], fill=ON_SURFACE)

# sinal de celular (triângulo cheio, signal_cellular_4_bar)
sx = L - 232
d.polygon([(sx, cy + 17), (sx + 36, cy + 17), (sx + 36, cy - 19)], fill=ON_SURFACE)

# wifi (leque sólido apontando para cima)
wx, wr = L - 158, 25
d.pieslice([wx - wr, cy - wr + 8, wx + wr, cy + wr + 8], 228, 312, fill=ON_SURFACE)

# bateria vertical com nível, como no Android
bx = L - 88
d.rounded_rectangle([bx + 9, cy - 24, bx + 25, cy - 18], radius=3, fill=ON_SURFACE)
d.rounded_rectangle(
    [bx, cy - 20, bx + 34, cy + 22], radius=10, outline=ON_SURFACE, width=4
)
d.rounded_rectangle([bx + 6, cy - 12, bx + 28, cy + 16], radius=6, fill=ON_SURFACE)

# ======================================= 2. top app bar (Material 3)
APPBAR_BASE = H_STATUS + H_APPBAR
cy = H_STATUS + H_APPBAR // 2

# arrow_back
d.line([(52, cy), (106, cy)], fill=ON_SURFACE, width=6)
d.line([(52, cy), (76, cy - 24)], fill=ON_SURFACE, width=6)
d.line([(52, cy), (76, cy + 24)], fill=ON_SURFACE, width=6)

centro("OLX", f_logo, 0, L, cy - 36, ROXO)

# share (três nós ligados por duas hastes)
sx = L - 192
d.line([(sx - 16, cy + 8), (sx + 18, cy - 14)], fill=ON_SURFACE, width=5)
d.line([(sx - 16, cy - 4), (sx + 18, cy + 20)], fill=ON_SURFACE, width=5)
for px, py in ((sx - 20, cy + 2), (sx + 22, cy - 18), (sx + 22, cy + 24)):
    d.ellipse([px - 11, py - 11, px + 11, py + 11], fill=BRANCO, outline=ON_SURFACE, width=5)

# favorite_border (coração vazado, feito por duas camadas)
coracao(img, L - 78, cy, 54, ON_SURFACE, espessura=5)

# ======================================= 3. foto
FOTO_ALTURA = 900
FOTO_BASE = APPBAR_BASE + FOTO_ALTURA
d.rectangle([0, APPBAR_BASE, L, FOTO_BASE], fill=FUNDO_FOTO)

original = Image.open(FOTO).convert("RGB")
escala = FOTO_ALTURA / original.height
nova = original.resize((round(original.width * escala), FOTO_ALTURA), Image.LANCZOS)
img.paste(nova, ((L - nova.width) // 2, APPBAR_BASE))

cont = "1 / 1"
cw = largura(cont, f_contador)
d.rounded_rectangle(
    [L - 60 - cw - 48, FOTO_BASE - 86, L - 60, FOTO_BASE - 28], radius=29, fill=(0, 0, 0)
)
d.text((L - 60 - cw - 24, FOTO_BASE - 74), cont, font=f_contador, fill=BRANCO)

# ======================================= 4. preço e selo
y = FOTO_BASE + 44
d.text((MARGEM, y), PRECO, font=f_preco, fill=ON_SURFACE)
y += 118

sw = largura(SELO, f_badge)
d.rounded_rectangle([MARGEM, y, MARGEM + sw + 76, y + 58], radius=16, fill=VERDE_BG)
ax, ay = MARGEM + 30, y + 29
d.line([(ax, ay - 14), (ax, ay + 6)], fill=VERDE_TXT, width=5)
d.polygon([(ax - 10, ay + 2), (ax + 10, ay + 2), (ax, ay + 18)], fill=VERDE_TXT)
d.text((MARGEM + 52, y + 12), SELO, font=f_badge, fill=VERDE_TXT)
y += 96

# ======================================= 5. título e meta
for linha in quebra(TITULO, f_titulo, L - 2 * MARGEM):
    d.text((MARGEM, y), linha, font=f_titulo, fill=ON_SURFACE)
    y += 56
y += 10

d.text((MARGEM, y), LOCAL, font=f_meta, fill=OUTLINE)
y += 42
d.text((MARGEM, y), DATA, font=f_meta, fill=OUTLINE)
y += 62

d.line([(MARGEM, y), (L - MARGEM, y)], fill=OUTLINE_VAR, width=3)
y += 40

# ======================================= 6. descrição
d.text((MARGEM, y), "Descrição", font=f_sec, fill=ON_SURFACE)
y += 58

for linha in quebra(DESCRICAO, f_desc, L - 2 * MARGEM):
    if linha:
        d.text((MARGEM, y), linha, font=f_desc, fill=ON_SURFACE_VAR)
    y += 46
y += 20

d.line([(MARGEM, y), (L - MARGEM, y)], fill=OUTLINE_VAR, width=3)
y += 40

# ======================================= 7. vendedor
d.ellipse([MARGEM, y, MARGEM + 88, y + 88], fill=ROXO_CLARO)
centro(VENDEDOR[0], f_vend, MARGEM, MARGEM + 88, y + 22, ROXO)
d.text((MARGEM + 116, y + 12), VENDEDOR, font=f_vend, fill=ON_SURFACE)
d.text((MARGEM + 116, y + 54), VENDEDOR_SUB, font=f_vend_sub, fill=OUTLINE)
y += 88 + 44

# ======================================= 8. corta e fecha
A = y + H_ACOES + H_NAV
if A > CANVAS:
    raise SystemExit(f"conteúdo passou do canvas ({A} > {CANVAS})")
img = img.crop((0, 0, L, A))
d = ImageDraw.Draw(img)

# barra de ações
ACOES = A - H_ACOES - H_NAV
d.rectangle([0, ACOES, L, A], fill=BRANCO)
d.line([(0, ACOES), (L, ACOES)], fill=OUTLINE_VAR, width=3)

by0, by1 = ACOES + 32, ACOES + H_ACOES - 36
meio = L // 2
raio = (by1 - by0) // 2

# outlined button
d.rounded_rectangle([MARGEM, by0, meio - 14, by1], radius=raio, outline=ROXO, width=5)
centro("Ligar", f_botao, MARGEM, meio - 14, by0 + 22, ROXO)

# filled button
d.rounded_rectangle([meio + 14, by0, L - MARGEM, by1], radius=raio, fill=ROXO)
centro("Chat", f_botao, meio + 14, L - MARGEM, by0 + 22, BRANCO)

# barra de gestos do Android
d.rounded_rectangle(
    [meio - 162, A - H_NAV // 2 - 6, meio + 162, A - H_NAV // 2 + 6],
    radius=6,
    fill=NAV_PILL,
)

img.save(SAIDA, "PNG", optimize=True)
print(f"gerado: {SAIDA.name} ({img.width}x{img.height})")
