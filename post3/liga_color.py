"""
Gera o logo da Liga em cor padrao, preto e amarelo, nas duas variantes oficiais.

DECISAO DE PROJETO, tomada pelo time de marketing e que contraria o manual de marca.
O manual proibe o amarelo da Liga na arte oficial do evento em tres pontos (p.2, p.5 e
p.7) e manda os dois logos monocromaticos. O time decidiu que a marca do parceiro deve
aparecer na forma padrao, igual a do site e das outras publicacoes, e essa decisao vale
sobre o manual. Nao reverter sem combinar.

Consequencia direta: as pecas deixam de ser preto e branco estrito. A cor fica confinada
ao logo da Liga, e todo o resto segue monocromatico na paleta da Decade.

Fonte: a peca escura, onde o logo esta em 195x80 px e o globo sobre o "i" tem definicao.
Dela saem as duas variantes, porque o unico elemento que muda entre elas e o texto
"LIGA", preto sobre fundo claro e off-white sobre fundo escuro. O amarelo e o mesmo nas
duas. As cores finais vem da paleta oficial da Liga (manual p.3) em vez da amostra do
JPEG, que esta degradada pela compressao.
"""
from PIL import Image, ImageFilter
import numpy as np

FONTE = "../SaveClip.App_838195465_18444907306131074_592259580098203467_n.jpg"
BOX = (764, 1502, 959, 1582)
FUNDOS = [np.array([12, 11, 9]), np.array([26, 25, 23])]
CORTE = 72.0        # o mesmo valor calibrado para o peso bater com o do Post1
ESCALA = 4

# paleta oficial da Liga, manual p.3
AMARELO = np.array([245, 197, 24])      # #F5C518
PRETO = np.array([33, 24, 21])          # #211815
OFFWHITE = np.array([255, 254, 251])    # #FFFEFB

VARIANTES = {
    "liga_color_light": PRETO,      # sobre fundo off-white
    "liga_color_dark": OFFWHITE,    # sobre fundo preto
}

arr = np.asarray(Image.open(FONTE).convert("RGB")).astype(float)
x0, y0, x1, y1 = BOX
sub = arr[y0:y1, x0:x1]

# alfa pela distancia ao fundo mais proximo
dists = np.stack([np.sqrt(((sub - f) ** 2).sum(axis=2)) for f in FUNDOS])
dist = dists.min(axis=0)
alfa = np.clip((dist - CORTE) / 85.0, 0.0, 1.0)
alfa[alfa < 0.10] = 0.0
alfa[alfa > 0.90] = 1.0

# desfaz a composicao para estimar a cor real do tracco: C_obs = a*C_fg + (1-a)*C_bg
fundo_proximo = np.take_along_axis(
    np.stack([np.broadcast_to(f, sub.shape) for f in FUNDOS]),
    dists.argmin(axis=0)[None, :, :, None].repeat(3, axis=3), axis=0)[0]
a3 = alfa[:, :, None]
with np.errstate(divide="ignore", invalid="ignore"):
    fg = np.where(a3 > 0.12, (sub - (1 - a3) * fundo_proximo) / np.maximum(a3, 1e-6), 0.0)
fg = np.clip(fg, 0, 255)

# amarelo tem r muito acima de b; off-white e preto tem r proximo de b
amarelidao = np.clip((fg[:, :, 0] - fg[:, :, 2]) / 120.0, 0.0, 1.0)
amarelidao[alfa < 0.12] = 0.0

h, w = alfa.shape
W, H = w * ESCALA, h * ESCALA

alfa_g = np.asarray(Image.fromarray((alfa * 255).astype(np.uint8)).resize((W, H), Image.LANCZOS)).astype(float) / 255.0
alfa_g = np.asarray(Image.fromarray((alfa_g * 255).astype(np.uint8)).filter(
    ImageFilter.UnsharpMask(2.0, 35, 2))).astype(float) / 255.0

# suaviza a classificacao antes de ampliar, para a fronteira entre amarelo e
# neutro nao serrilhar. As duas regioes sao separadas no desenho, entao o blur
# nao mistura elementos distintos
am_img = Image.fromarray((amarelidao * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
am_g = np.asarray(am_img.resize((W, H), Image.LANCZOS)).astype(float) / 255.0
am_g = np.clip((am_g - 0.35) / 0.30, 0.0, 1.0)      # endurece a decisao

print("variante              tamanho    amarelo  neutro")
print("-" * 52)
for nome, neutro in VARIANTES.items():
    cor = am_g[:, :, None] * AMARELO + (1 - am_g[:, :, None]) * neutro
    canvas = np.zeros((H, W, 4), dtype=np.uint8)
    canvas[:, :, :3] = np.clip(cor, 0, 255).astype(np.uint8)
    canvas[:, :, 3] = np.clip(alfa_g * 255, 0, 255).astype(np.uint8)
    Image.fromarray(canvas).save(f"assets/{nome}.png")

    vis = alfa_g > 0.5
    pa = (am_g[vis] > 0.5).mean() * 100
    print(f"{nome:21s} {W}x{H}   {pa:5.1f}%  {100-pa:5.1f}%")

print("\nassets/liga_color_light.png e assets/liga_color_dark.png gerados")
print("amarelo #F5C518, preto #211815, off-white #FFFEFB, todos da paleta oficial")
