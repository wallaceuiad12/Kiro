#!/usr/bin/env python3
"""
Gera diagramas ESQUEMÁTICOS originais dos painéis do Wix Editor clássico.
NÃO são screenshots do Wix: são ilustrações desenhadas para o relatório,
mostrando a posição relativa dos controles e o caminho de clique.
"""
import os, html

OUT = "/projects/sandbox/audit-ccu/diagrams"
os.makedirs(OUT, exist_ok=True)

# paleta dos diagramas
INK = "#181818"; MUT = "#6B6B6B"; LINE = "#D8D8D8"; BG = "#FFFFFF"
PANEL = "#F7F7F8"; ACC = "#C1272D"; OKG = "#1E7A45"; WARN = "#B8860B"
BLUE = "#1A6FD4"

FONT = "Noto Sans, DejaVu Sans, sans-serif"


def esc(s):
    return html.escape(str(s))


def hdr(w, h, title, subtitle=""):
    s = f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">'
    s += f'<rect width="{w}" height="{h}" fill="{BG}"/>'
    s += (f'<text x="20" y="30" font-family="{FONT}" font-size="17" font-weight="700" '
          f'fill="{INK}">{esc(title)}</text>')
    if subtitle:
        s += (f'<text x="20" y="50" font-family="{FONT}" font-size="12.5" '
              f'fill="{MUT}">{esc(subtitle)}</text>')
    s += (f'<text x="{w-20}" y="30" text-anchor="end" font-family="{FONT}" font-size="10" '
          f'fill="{MUT}">ESQUEMA — não é captura de tela do Wix</text>')
    return s


def panel(x, y, w, h, label="", fill=PANEL):
    s = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="{fill}" '
         f'stroke="{LINE}" stroke-width="1.2"/>')
    if label:
        s += (f'<text x="{x+12}" y="{y+21}" font-family="{FONT}" font-size="12.5" '
              f'font-weight="700" fill="{INK}">{esc(label)}</text>')
    return s


def row(x, y, w, text, note="", icon="", h=27, bold=False, color=None,
        strike=False, box=False):
    col = color or INK
    s = ""
    if box:
        s += (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="#FFFFFF" '
              f'stroke="{LINE}"/>')
    tx = x + (10 if box else 4)
    if icon:
        s += (f'<text x="{tx}" y="{y+h/2+4.5}" font-family="{FONT}" font-size="12.5" '
              f'fill="{MUT}">{esc(icon)}</text>')
        tx += 19
    dec = ' text-decoration="line-through"' if strike else ""
    s += (f'<text x="{tx}" y="{y+h/2+4.5}" font-family="{FONT}" font-size="12.5" '
          f'font-weight="{"700" if bold else "400"}" fill="{col}"{dec}>{esc(text)}</text>')
    if note:
        s += (f'<text x="{x+w-10}" y="{y+h/2+4.5}" text-anchor="end" font-family="{FONT}" '
              f'font-size="10.5" fill="{MUT}">{esc(note)}</text>')
    return s


def btn(x, y, w, h, text, fill=ACC, fg="#FFFFFF", outline=False):
    if outline:
        s = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="none" '
             f'stroke="{fill}" stroke-width="1.6"/>')
        fg = fill
    else:
        s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}"/>'
    s += (f'<text x="{x+w/2}" y="{y+h/2+4.5}" text-anchor="middle" font-family="{FONT}" '
          f'font-size="12" font-weight="700" fill="{fg}">{esc(text)}</text>')
    return s


def step(n, x, y, text, w=300, color=ACC):
    """Bolha numerada + texto do passo."""
    s = f'<circle cx="{x+11}" cy="{y}" r="11" fill="{color}"/>'
    s += (f'<text x="{x+11}" y="{y+4.5}" text-anchor="middle" font-family="{FONT}" '
          f'font-size="12" font-weight="700" fill="#FFFFFF">{n}</text>')
    s += (f'<text x="{x+30}" y="{y+4.5}" font-family="{FONT}" font-size="12.5" '
          f'fill="{INK}">{esc(text)}</text>')
    return s


def arrow(x1, y1, x2, y2, color=ACC, dash=False):
    d = ' stroke-dasharray="5,4"' if dash else ""
    return (f'<defs><marker id="a{abs(hash((x1,y1,x2,y2)))%99999}" markerWidth="9" '
            f'markerHeight="9" refX="7" refY="3" orient="auto">'
            f'<path d="M0,0 L0,6 L8,3 z" fill="{color}"/></marker></defs>'
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" '
            f'stroke-width="2"{d} marker-end="url(#a{abs(hash((x1,y1,x2,y2)))%99999})"/>')


def wrap(text, width):
    """Quebra texto em linhas de no maximo `width` caracteres."""
    out, cur = [], ""
    for w in text.split():
        if len(cur) + len(w) + 1 <= width:
            cur = (cur + " " + w).strip()
        else:
            out.append(cur); cur = w
    if cur: out.append(cur)
    return out


def tick(x, y, color="#1E7A45", size=11):
    return (f'<path d="M{x} {y} l{size*0.33} {size*0.33} l{size*0.62} -{size*0.72}" '
            f'fill="none" stroke="{color}" stroke-width="2.1" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')


def cross(x, y, color="#C1272D", size=10):
    return (f'<path d="M{x} {y} l{size} {size} M{x+size} {y} l-{size} {size}" '
            f'fill="none" stroke="{color}" stroke-width="2.1" stroke-linecap="round"/>')


def callout(x, y, w, text, color=ACC, h=None):
    """Aviso com quebra automatica; ignora \n do chamador e reflui."""
    chars = int((w - 20) / 6.05)
    lines = []
    for para in text.split("\n"):
        lines.extend(wrap(para, chars) or [""])
    h = h or (15 * len(lines) + 16)
    s = (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="#FFF8F8" '
         f'stroke="{color}" stroke-width="1.2"/>')
    for i, l in enumerate(lines):
        s += (f'<text x="{x+10}" y="{y+19+i*15}" font-family="{FONT}" font-size="11" '
              f'fill="{INK}">{esc(l)}</text>')
    return s


def save(name, svg):
    svg += "</svg>"
    p = os.path.join(OUT, name + ".svg")
    open(p, "w", encoding="utf-8").write(svg)
    print("  ", name + ".svg")


# ═══════════════ D1 — Painel de Páginas: ocultar ≠ despublicar ≠ excluir
W, H = 940, 492
s = hdr(W, H, "D1 · Menus e Páginas — ocultar NÃO é excluir",
        "Editor > painel esquerdo > Menus e Páginas. A distinção que gerou 21 páginas órfãs no site do CCU.")
s += panel(20, 66, 330, 330, "Menus e Páginas")
items = [("Início", ""), ("Sobre nós", ""), ("Projetos", "pasta"),
         ("Parceiros", "âncora"), ("Conteúdo", "pasta"), ("Alumni", ""),
         ("Mailing", ""), ("blank-1", "oculta"), ("blank-6", "oculta")]
y = 96
for nm, nt in items:
    hl = nm.startswith("blank")
    s += row(34, y, 300, nm, nt, icon="",
             color=ACC if hl else INK, bold=hl, box=hl)
    y += 30
s += arrow(352, 366, 402, 366)
s += panel(410, 66, 510, 330, "Menu de contexto da página (engrenagem)")
opts = [
    ("Configurações", "", MUT),
    ("SEO básico", "slug, título, descrição", BLUE),
    ("Ocultar do menu", "CONTINUA publicada e indexável", WARN),
    ("Ocultar dos motores de busca", "sai do Google, segue no ar", WARN),
    ("Duplicar", "origem dos slugs blank-N", ACC),
    ("Excluir", "remove de verdade — use com 301", OKG),
]
y = 100
for nm, nt, c in opts:
    s += row(424, y, 480, nm, nt, color=c, bold=c in (OKG, ACC), box=True)
    y += 38
s += callout(20, 406, 900,
             "Regra: “Ocultar do menu” deixa a página publicada, no sitemap e no Google. Foi assim que /blank-1 (“Site em manutenção”) e /blank-6 (Processo Seletivo) continuaram no ar.\n"
             "Quando a página não serve mais: Excluir + criar o redirecionamento 301 (ver D3). Nunca duplicar página para criar a edição seguinte.")
save("d1-paginas", s)

# ═══════════════ D2 — SEO básico da página
W, H = 940, 452
s = hdr(W, H, "D2 · SEO básico da página — slug, título e descrição",
        "Menus e Páginas > engrenagem da página > SEO básico. Corrige os slugs blank-N e as 20 descrições vazias.")
s += panel(20, 66, 560, 300, "SEO básico")
s += row(34, 96, 520, "URL da página (slug)", color=MUT)
s += (f'<rect x="34" y="118" width="520" height="34" rx="5" fill="#FFF" stroke="{ACC}" stroke-width="1.6"/>')
s += (f'<text x="46" y="140" font-family="{FONT}" font-size="12" fill="{MUT}">'
      f'consultoriaunicamp.com/ </text>')
s += (f'<text x="196" y="140" font-family="{FONT}" font-size="12.5" font-weight="700" '
      f'fill="{ACC}">processo-seletivo</text>')
s += (f'<text x="392" y="140" font-family="{FONT}" font-size="10.5" fill="{MUT}">'
      f'era blank-6</text>')
s += row(34, 164, 520, "Título do SEO  (máx. 60 caracteres)", color=MUT)
s += (f'<rect x="34" y="186" width="520" height="34" rx="5" fill="#FFF" stroke="{LINE}"/>')
s += (f'<text x="46" y="208" font-family="{FONT}" font-size="12" fill="{INK}">'
      f'Processo Seletivo do CCU — seja membro | CCU</text>')
s += (f'<text x="520" y="208" font-family="{FONT}" font-size="10" fill="{OKG}">44</text>')
s += row(34, 232, 520, "Descrição do SEO  (máx. 155 caracteres)", color=MUT)
s += (f'<rect x="34" y="254" width="520" height="52" rx="5" fill="#FFF" stroke="{LINE}"/>')
for i, l in enumerate(["Faça parte do Clube de Consultoria Universitário: treinamentos,",
                       "cases semanais, projetos e contato com consultorias."]):
    s += (f'<text x="46" y="{274+i*18}" font-family="{FONT}" font-size="11.5" fill="{INK}">{esc(l)}</text>')
s += (f'<text x="520" y="300" font-family="{FONT}" font-size="10" fill="{OKG}">150</text>')
s += (f'<rect x="34" y="318" width="18" height="18" rx="3" fill="#FFF" stroke="{LINE}"/>')
s += row(58, 318, 300, "Ocultar esta página dos resultados de busca", color=MUT)
s += panel(600, 66, 320, 300, "Prévia no Google")
s += (f'<text x="614" y="104" font-family="{FONT}" font-size="11" fill="{MUT}">'
      f'consultoriaunicamp.com › processo-seletivo</text>')
s += (f'<text x="614" y="128" font-family="{FONT}" font-size="13.5" fill="{BLUE}">'
      f'Processo Seletivo do CCU —</text>')
s += (f'<text x="614" y="146" font-family="{FONT}" font-size="13.5" fill="{BLUE}">'
      f'seja membro | CCU</text>')
for i, l in enumerate(["Faça parte do Clube de Consultoria", "Universitário: treinamentos, cases",
                       "semanais, projetos e contato com", "consultorias."]):
    s += (f'<text x="614" y="{170+i*17}" font-family="{FONT}" font-size="11.5" fill="{MUT}">{esc(l)}</text>')
s += callout(600, 250, 320,
             "Hoje 20 páginas do CCU têm\ndescrição VAZIA — o Google\nrecorta um trecho ao acaso.")
s += callout(20, 378, 900,
             "Atenção: ao mudar o slug, crie o 301 na MESMA sessão (D3). Trocar slug sem redirecionar quebra todo link já compartilhado no WhatsApp, no LinkedIn e nos comentários dos posts.")
save("d2-seo", s)

# ═══════════════ D3 — Redirecionamentos 301
W, H = 940, 416
s = hdr(W, H, "D3 · Gerenciador de Redirecionamentos de URL (301)",
        "Painel do site > SEO > Redirecionamentos de URL. Obrigatório sempre que um slug mudar.")
s += panel(20, 66, 900, 250, "Redirecionamentos de URL")
s += btn(800, 76, 106, 28, "+ Novo")
s += (f'<line x1="34" y1="118" x2="906" y2="118" stroke="{LINE}"/>')
s += row(34, 122, 300, "URL antiga", color=MUT, bold=True)
s += row(420, 122, 300, "Redireciona para", color=MUT, bold=True)
s += row(800, 122, 100, "Tipo", color=MUT, bold=True)
pairs = [("/blank-6", "/processo-seletivo"), ("/blank-2", "/casebooks"),
         ("/blank-7", "/contato"), ("/blank", "/alumni"),
         ("/prep4consulting-2026-2", "/prep4consulting")]
y = 152
for a, b in pairs:
    s += row(34, y, 340, a, color=ACC)
    s += arrow(390, y + 13, 414, y + 13, MUT)
    s += row(420, y, 340, b, color=OKG)
    s += row(800, y, 100, "301", color=MUT)
    y += 30
s += callout(20, 326, 440,
             "31 redirecionamentos a criar no total.\nLista completa na seção 8.1 do relatório.", color=OKG)
s += callout(480, 326, 440,
             "NÃO faça como o PoliCC: lá /sobre-nos e\n/sobre-nós dão 301 para a HOME — o visitante\nperde a página que procurava.")
save("d3-301", s)

# ═══════════════ D4 — Temas de Texto
W, H = 940, 496
s = hdr(W, H, "D4 · Temas de Texto — a correção de maior alcance",
        "Editor > Site > Temas de Texto. Muda a tipografia de TODO o site de uma vez.")
s += panel(20, 66, 430, 340, "Temas de Texto")
themes = [("Título 1", "Brandon Grotesque Light", "88 > 44 px", True),
          ("Título 2", "Brandon Grotesque Light", "72 > 32 px", True),
          ("Título 3", "Brandon Grotesque Light", "28 > 24 px", True),
          ("Parágrafo 1", "Avenir LT 35 Light", "20 px", False),
          ("Parágrafo 2", "Avenir LT 35 Light", "18 px", False),
          ("Legenda", "Avenir LT 35 Light", "14 px", False)]
y = 96
for nm, fam, sz, isT in themes:
    s += (f'<rect x="34" y="{y}" width="400" height="44" rx="5" fill="#FFF" stroke="{LINE}"/>')
    s += (f'<text x="46" y="{y+19}" font-family="{FONT}" font-size="13" font-weight="700" '
          f'fill="{INK}">{esc(nm)}</text>')
    s += (f'<text x="46" y="{y+36}" font-family="{FONT}" font-size="10.5" fill="{MUT}">{esc(fam)}</text>')
    s += (f'<text x="424" y="{y+26}" text-anchor="end" font-family="{FONT}" font-size="11.5" '
          f'font-weight="700" fill="{ACC if " > " in sz else OKG}">{esc(sz)}</text>')
    y += 50
s += arrow(452, 240, 500, 240)
s += panel(510, 66, 410, 200, "Painel de uma caixa de texto")
s += row(524, 100, 380, "Tema", color=MUT)
s += (f'<rect x="524" y="122" width="382" height="32" rx="5" fill="#FFF" stroke="{ACC}" stroke-width="1.6"/>')
s += (f'<text x="536" y="143" font-family="{FONT}" font-size="12.5" font-weight="700" '
      f'fill="{ACC}">Parágrafo 2</text>')
s += (f'<text x="890" y="143" text-anchor="end" font-family="{FONT}" font-size="12" fill="{MUT}">v</text>')
s += callout(510, 172, 410,
             "Selecione TODO o texto da caixa (Ctrl+A)\nantes de escolher o tema — só assim a\nformatação manual antiga é descartada.")
s += callout(510, 282, 410,
             "Hoje: 3.948 formatações manuais\n46 tamanhos de fonte · 34 famílias\nAlvo: 6 temas, 2 famílias, 0 manual", color=OKG)
s += callout(20, 424, 900,
             "Por que isso primeiro: o site JÁ tem os temas certos configurados (Brandon Grotesque para título, Avenir para corpo). O problema é que cada caixa de texto sobrescreve o tema. Arrumar o tema conserta o site inteiro; arrumar caixa por caixa não escala.")
save("d4-temas", s)

# ═══════════════ D5 — Paleta e contraste
W, H = 940, 482
s = hdr(W, H, "D5 · Paleta do site — o que pode e o que não pode virar texto",
        "Editor > Site > Cores do Site. Não mude os valores: mude o uso.")
s += panel(20, 66, 900, 150, "Paleta atual (linha principal + rampa vermelha)")
main = [("#FBFAFA", "color_11", "fundo", True), ("#C2C2C2", "color_7", "decorativo", False),
        ("#898989", "color_8", "decorativo", False), ("#515151", "color_14", "texto 2º", True),
        ("#181818", "color_15", "texto", True)]
ramp = [("#EAACAE", "color_16", "só escuro", False), ("#D68084", "color_17", "só escuro", False),
        ("#C1272D", "color_18", "MARCA", True), ("#811A1E", "color_19", "hover", True),
        ("#400D0F", "color_20", "decorativo", False)]
for i, (hexv, slot, use, ok) in enumerate(main):
    x = 40 + i * 172
    s += f'<rect x="{x}" y="96" width="60" height="44" rx="4" fill="{hexv}" stroke="{LINE}"/>'
    s += (f'<text x="{x+68}" y="110" font-family="{FONT}" font-size="11" font-weight="700" fill="{INK}">{hexv}</text>')
    s += (f'<text x="{x+68}" y="125" font-family="{FONT}" font-size="9.5" fill="{MUT}">{slot}</text>')
    s += (tick(x+68, 134, OKG, 9) if ok else cross(x+68, 130, ACC, 8))
    s += (f'<text x="{x+84}" y="139" font-family="{FONT}" font-size="9.5" '
          f'fill="{OKG if ok else ACC}">{use}</text>')
for i, (hexv, slot, use, ok) in enumerate(ramp):
    x = 40 + i * 172
    s += f'<rect x="{x}" y="152" width="60" height="44" rx="4" fill="{hexv}" stroke="{LINE}"/>'
    s += (f'<text x="{x+68}" y="166" font-family="{FONT}" font-size="11" font-weight="700" fill="{INK}">{hexv}</text>')
    s += (f'<text x="{x+68}" y="181" font-family="{FONT}" font-size="9.5" fill="{MUT}">{slot}</text>')
    s += (tick(x+68, 190, OKG, 9) if ok else cross(x+68, 186, ACC, 8))
    s += (f'<text x="{x+84}" y="195" font-family="{FONT}" font-size="9.5" '
          f'fill="{OKG if ok else ACC}">{use}</text>')
# demonstração de contraste
s += panel(20, 228, 440, 150, "Em fundo CLARO (#FBFAFA) — o site")
s += f'<rect x="34" y="258" width="410" height="106" fill="#FBFAFA" stroke="{LINE}"/>'
demo1 = [("#181818", "Texto principal — 17,0:1", True), ("#515151", "Texto secundário — 7,6:1", True),
         ("#C1272D", "Destaque da marca — 5,6:1", True), ("#898989", "Cinza médio — 3,4:1 FALHA", False),
         ("#D68084", "Rosa do CWC — 2,8:1 FALHA", False)]
for i, (c, t, ok) in enumerate(demo1):
    s += (f'<text x="46" y="{278+i*19}" font-family="{FONT}" font-size="12" fill="{c}">{esc(t)}</text>')
    s += (tick(424, 272+i*19, OKG, 10) if ok else cross(424, 269+i*19, ACC, 9))
s += panel(480, 228, 440, 150, "Em fundo ESCURO (#181818) — as peças do Instagram")
s += f'<rect x="494" y="258" width="410" height="106" fill="#181818"/>'
demo2 = [("#FBFAFA", "Texto claro — 17,0:1", True), ("#C2C2C2", "Cinza claro — 10,0:1", True),
         ("#EAACAE", "Rosa claro CWC — 9,3:1", True), ("#D68084", "Rosa CWC — 6,2:1", True),
         ("#C1272D", "Vermelho da marca — 3,0:1 FALHA", False)]
for i, (c, t, ok) in enumerate(demo2):
    s += (f'<text x="506" y="{278+i*19}" font-family="{FONT}" font-size="12" fill="{c}">{esc(t)}</text>')
    s += (tick(884, 272+i*19, "#7BE0A0", 10) if ok else cross(884, 269+i*19, "#FF8A8A", 9))
s += callout(20, 396, 900,
             "Descoberta: a paleta do CCU foi desenhada para as peças de fundo ESCURO do Instagram/LinkedIn. Os rosas do CWC e os cinzas passam AA em fundo escuro e falham em fundo claro; o vermelho da marca faz o oposto. Se a seção do site tem fundo claro, use #181818/#515151/#C1272D. Se tiver fundo escuro, aí sim os rosas funcionam.")
save("d5-paleta", s)

# ═══════════════ D6 — Editor mobile
W, H = 940, 492
s = hdr(W, H, "D6 · Editor mobile — onde o conteúdo do CCU divergiu",
        "Editor > ícone de celular no topo. No Wix clássico o layout mobile é EDITADO SEPARADAMENTE.")
s += (f'<rect x="20" y="66" width="900" height="40" rx="6" fill="{PANEL}" stroke="{LINE}"/>')
s += btn(34, 74, 120, 24, "Desktop", fill=INK)
s += btn(162, 74, 120, 24, "Mobile", fill=ACC)
s += (f'<text x="300" y="91" font-family="{FONT}" font-size="11.5" fill="{MUT}">'
      f'alternar aqui — toda alteração de layout precisa ser feita nos DOIS</text>')
s += panel(20, 120, 435, 268, "Desktop hoje — /prep4consulting-2026-2")
d = [("Ciclo 1", True), ("Prep 101 · Consulting 101 · Screening", False),
     ("Ciclo 2", True), ("Ciclo 3", True),
     ("Finanças · Framework · Fit · Case · GMAT…", False), ("Ciclo 4", True)]
y = 150
for t, b in d:
    s += row(34, y, 405, t, color=ACC if b else INK, bold=b)
    y += 27
s += callout(34, 322, 405, "PROBLEMA: Ciclo 2 e 3 colados, módulos despejados; falta o módulo Estrutura do PS")
s += panel(485, 120, 435, 268, "Mobile hoje — mesma página")
m = [("Ciclo 1", True), ("Prep 101 · Consulting101 · Screening · Estrutura do PS", False),
     ("Ciclo 2", True), ("GMAT ×4 · Business Case Test", False),
     ("Ciclo 3", True), ("Faça perguntas de clarificação  (texto solto)", False)]
y = 150
for t, b in m:
    isbad = "solto" in t
    s += row(499, y, 405, t, color=ACC if (b or isbad) else INK, bold=b)
    y += 27
s += callout(499, 322, 405, "Ordem dos ciclos correta, mas com 2 textos colados de /entrevista")
s += callout(20, 408, 900,
             "Regra operacional: depois de QUALQUER mudança de layout no desktop, abra o editor mobile e confira a mesma seção antes de publicar. Foi a falta desse passo que fez o desktop perder um módulo do curso e o mobile ganhar dois textos que não pertencem a ele.")
save("d6-mobile", s)

# ═══════════════ D7 — Desinstalar apps
W, H = 940, 420
s = hdr(W, H, "D7 · Desinstalar apps — ocultar a página não resolve",
        "Painel do site > Apps > Gerenciar Apps. Remove a página, o script e o ícone do carrinho.")
s += panel(20, 66, 900, 250, "Gerenciar Apps")
apps = [("Wix Events", "vende o Prep4Consulting", "MANTER", OKG),
        ("Wix Stores", "/shop sem produtos + carrinho no topo de todas as páginas", "DESINSTALAR", ACC),
        ("Wix Forum", "/forum exibe “Widget Didn’t Load”", "DESINSTALAR", ACC),
        ("Wix Loyalty", "/loyalty em inglês, recompensa loja vazia", "DESINSTALAR", ACC),
        ("Wix Bookings", "/book-online travado em “Carregando os dias…”", "DESINSTALAR", ACC),
        ("Members Area", "/members totalmente vazia", "DESINSTALAR", ACC),
        ("Wix Blog", "/blog sem nenhum post", "DESINSTALAR", ACC)]
y = 100
for nm, why, act, c in apps:
    s += (f'<rect x="34" y="{y}" width="872" height="28" rx="5" fill="#FFF" stroke="{LINE}"/>')
    s += (f'<text x="46" y="{y+18}" font-family="{FONT}" font-size="12.5" font-weight="700" '
          f'fill="{INK}">{esc(nm)}</text>')
    s += (f'<text x="190" y="{y+18}" font-family="{FONT}" font-size="11" fill="{MUT}">{esc(why)}</text>')
    s += (f'<text x="896" y="{y+18}" text-anchor="end" font-family="{FONT}" font-size="11" '
          f'font-weight="700" fill="{c}">{esc(act)}</text>')
    y += 30
s += callout(20, 326, 900,
             "O ícone de carrinho com “0” aparece no cabeçalho de TODAS as páginas do site porque o Wix Stores está instalado — inclusive nas páginas de conteúdo gratuito. Desinstalar o app remove o carrinho. Depois de desinstalar, crie os 301 (D3): /shop > /prep4consulting, /forum > /conteudo, /members > /processo-seletivo.")
save("d7-apps", s)

# ═══════════════ D8 — Link de botão
W, H = 940, 376
s = hdr(W, H, "D8 · Corrigir o link de um botão — os 3 CTAs que caem na home",
        "Editor > clicar no botão > ícone de link. Religa 15 casebooks que estão no ar e funcionando.")
s += panel(20, 66, 400, 210, "Selecionar o elemento")
s += btn(60, 110, 150, 34, "Ver mais", fill=ACC)
s += (f'<rect x="52" y="102" width="166" height="50" rx="4" fill="none" stroke="{BLUE}" '
      f'stroke-width="1.5" stroke-dasharray="4,3"/>')
s += (f'<text x="60" y="176" font-family="{FONT}" font-size="11.5" fill="{MUT}">Destino atual:</text>')
s += (f'<text x="60" y="194" font-family="{FONT}" font-size="11.5" font-weight="700" fill="{ACC}">'
      f'consultoriaunicamp.com</text>')
s += (f'<text x="60" y="216" font-family="{FONT}" font-size="11" fill="{MUT}">'
      f'(a raiz do site — link morto)</text>')
s += (f'<text x="60" y="246" font-family="{FONT}" font-size="11.5" fill="{MUT}">clicar no icone de link</text>')
s += arrow(424, 170, 470, 170)
s += panel(480, 66, 440, 210, "Para onde este link vai?")
opts2 = [("Uma página do meu site", True), ("Endereço da web", False),
         ("Âncora nesta página", False), ("Documento", False), ("E-mail", False)]
y = 98
for t, sel in opts2:
    s += (f'<circle cx="502" cy="{y+9}" r="6.5" fill="#FFF" stroke="{ACC if sel else LINE}" stroke-width="1.5"/>')
    if sel:
        s += f'<circle cx="502" cy="{y+9}" r="3.5" fill="{ACC}"/>'
    s += (f'<text x="518" y="{y+13}" font-family="{FONT}" font-size="12.5" '
          f'font-weight="{"700" if sel else "400"}" fill="{INK}">{esc(t)}</text>')
    y += 26
s += (f'<rect x="496" y="{y+6}" width="410" height="32" rx="5" fill="#FFF" stroke="{OKG}" stroke-width="1.6"/>')
s += (f'<text x="508" y="{y+27}" font-family="{FONT}" font-size="12.5" font-weight="700" '
      f'fill="{OKG}">Casebooks  (/casebooks)</text>')
s += callout(20, 288, 900,
             "Os três elementos a corrigir:  /conteudo > card “Cases completos” (Ver mais)  ·  /casebook-ccu > botão “CONFIRA”  ·  /guesstimate > “…confira algumas resoluções de case”.\nTodos apontam hoje para a raiz do site. Nenhum tem âncora — são links mortos.")
save("d8-link", s)

# ═══════════════ D9 — Wix Events
W, H = 940, 424
s = hdr(W, H, "D9 · Wix Events — excluir as 14 edições residuais",
        "Painel do site > Eventos. Duas delas se chamam “teste” e estão indexadas no Google.")
s += panel(20, 66, 900, 250, "Eventos")
evs = [("Prep4Consulting 2026.2", "/event-details/prep4consulting-2026-2", "MANTER", OKG),
       ("Prep4Consulting 2026.1", "/prep4consulting-2025-2-1-1  (slug de 2025.2)", "EXCLUIR", ACC),
       ("teste", "/prep4consulting-2025-2-1", "EXCLUIR", ACC),
       ("teste (1)", "/teste-1", "EXCLUIR", ACC),
       ("Prep4Consulting 2025.1 (old)", "/prep4consulting-2025-1-old", "EXCLUIR", ACC),
       ("Prep4Consulting 2025.2 · 2025.1 · 2024.2 · 2024.1", "4 edições", "EXCLUIR", ACC),
       ("Prep4Consulting 2023.2 · ×4 sem edição · Getting the Job", "5 edições de 2021–2023", "EXCLUIR", ACC)]
y = 100
for nm, sl, act, c in evs:
    s += (f'<rect x="34" y="{y}" width="872" height="28" rx="5" fill="#FFF" stroke="{LINE}"/>')
    s += (f'<text x="46" y="{y+18}" font-family="{FONT}" font-size="12" font-weight="700" fill="{INK}">{esc(nm)}</text>')
    s += (f'<text x="420" y="{y+18}" font-family="{FONT}" font-size="10.5" fill="{MUT}">{esc(sl)}</text>')
    s += (f'<text x="896" y="{y+18}" text-anchor="end" font-family="{FONT}" font-size="11" '
          f'font-weight="700" fill="{c}">{esc(act)}</text>')
    y += 30
s += callout(20, 326, 900,
             "Nunca DUPLIQUE um evento para criar a edição seguinte: é o que produziu os slugs -2, -3, -4 e o absurdo de a edição 2026.1 morar em “prep4consulting-2025-2-1-1”. Crie um evento novo com slug limpo (prep4consulting-2027-1) e escreva uma descrição própria — hoje 13 eventos compartilham quase a mesma meta description.")
save("d9-events", s)

# ═══════════════ D10 — Texto alternativo
W, H = 940, 344
s = hdr(W, H, "D10 · Texto alternativo — hoje o alt é o nome do arquivo",
        "Clicar na imagem > Configurações > Texto alternativo (ou pelo Gerenciador de Mídia).")
s += panel(20, 66, 440, 190, "Como está")
s += f'<rect x="34" y="96" width="120" height="84" rx="4" fill="#E8E8E8" stroke="{LINE}"/>'
s += (f'<text x="94" y="142" text-anchor="middle" font-family="{FONT}" font-size="10.5" fill="{MUT}">cronograma</text>')
s += (f'<text x="168" y="112" font-family="{FONT}" font-size="11" fill="{MUT}">alt =</text>')
for i, l in enumerate(["cronograma-prep4consulting", "-2026-2_5.png"]):
    s += (f'<text x="168" y="{132+i*17}" font-family="{FONT}" font-size="11" fill="{ACC}">{esc(l)}</text>')
s += (f'<text x="168" y="178" font-family="{FONT}" font-size="10.5" fill="{MUT}">'
      f'e as datas do curso só existem</text>')
s += (f'<text x="168" y="192" font-family="{FONT}" font-size="10.5" fill="{MUT}">'
      f'dentro da imagem</text>')
s += arrow(464, 160, 508, 160)
s += panel(520, 66, 400, 190, "Como deve ficar")
s += f'<rect x="534" y="96" width="120" height="84" rx="4" fill="#E8E8E8" stroke="{LINE}"/>'
s += (f'<text x="594" y="142" text-anchor="middle" font-family="{FONT}" font-size="10.5" fill="{MUT}">cronograma</text>')
s += (f'<text x="668" y="112" font-family="{FONT}" font-size="11" fill="{MUT}">alt =</text>')
for i, l in enumerate(["“Cronograma do Prep4Consulting", "2026.2: 11 encontros ao vivo”"]):
    s += (f'<text x="668" y="{132+i*17}" font-family="{FONT}" font-size="11" fill="{OKG}">{esc(l)}</text>')
s += (f'<text x="668" y="178" font-family="{FONT}" font-size="10.5" fill="{MUT}">'
      f'+ as datas repetidas como</text>')
s += (f'<text x="668" y="192" font-family="{FONT}" font-size="10.5" fill="{MUT}">'
      f'TEXTO ou tabela na página</text>')
s += callout(20, 266, 900,
             "Duas imagens da página do curso estão com alt vazio e quatro têm o nome do arquivo como alt (“hq1_edited.png”, “y8-PTBaP90a-removebg-preview.png”…). Imagem decorativa pode ter alt vazio de propósito; imagem que carrega informação, nunca.")
save("d10-alt", s)

print("\nOK — diagramas SVG gerados em", OUT)
