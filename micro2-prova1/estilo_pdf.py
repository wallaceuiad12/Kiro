"""
Estilos e componentes compartilhados pelos PDFs de estudo de Microeconomia II.

Notação matemática:
  - formula([...])  -> bloco de exibição com LaTeX renderizado (mathtext do matplotlib)
  - P('... <i>x</i>₁ ...') -> texto corrido; subscritos/sobrescritos Unicode viram
    tags <sub>/<super>, e os demais símbolos saem direto na fonte DejaVu Sans.

Usado por gerar_resumo_pdf.py e gerar_lista1_resolvida_pdf.py.
"""
import glob
import hashlib
import os
import re

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, HRFlowable, Image, KeepTogether, PageTemplate,
    Paragraph, Spacer, Table, TableStyle,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
MATH_CACHE = os.path.join(ROOT, '.formulas')
os.makedirs(MATH_CACHE, exist_ok=True)


# --- fontes ----------------------------------------------------------------
# DejaVu Sans cobre os símbolos matemáticos que a Noto Sans não tem
# (⇒ ∀ ≈ ≤ ≥ ∫ □ ∈ ≠ →) e é a mesma família usada nos gráficos.
def _dejavu(nome_arquivo):
    padroes = [
        f'/usr/local/lib*/python3*/site-packages/matplotlib/mpl-data/fonts/ttf/{nome_arquivo}',
        f'/usr/lib*/python3*/site-packages/matplotlib/mpl-data/fonts/ttf/{nome_arquivo}',
        f'/usr/share/fonts/**/{nome_arquivo}',
    ]
    for padrao in padroes:
        achados = glob.glob(padrao, recursive=True)
        if achados:
            return achados[0]
    raise FileNotFoundError(f'Fonte não encontrada: {nome_arquivo}')


BASE = 'DejaVuSans'
pdfmetrics.registerFont(TTFont(BASE, _dejavu('DejaVuSans.ttf')))
pdfmetrics.registerFont(TTFont(BASE + '-Bold', _dejavu('DejaVuSans-Bold.ttf')))
pdfmetrics.registerFont(TTFont(BASE + '-Italic', _dejavu('DejaVuSans-Oblique.ttf')))
pdfmetrics.registerFont(TTFont(BASE + '-BoldItalic', _dejavu('DejaVuSans-BoldOblique.ttf')))
pdfmetrics.registerFontFamily(BASE, normal=BASE, bold=BASE + '-Bold',
                              italic=BASE + '-Italic', boldItalic=BASE + '-BoldItalic')

# --- geometria -------------------------------------------------------------
PAGE_W, PAGE_H = A4
LEFT = RIGHT = 1.65 * cm
TOP = 1.65 * cm
BOTTOM = 1.55 * cm
CONTENT_W = PAGE_W - LEFT - RIGHT

# --- cores -----------------------------------------------------------------
NAVY = colors.HexColor('#17365D')
BLUE = colors.HexColor('#1F4E79')
RED = colors.HexColor('#A61C00')
GREEN = colors.HexColor('#2E7D32')
PURPLE = colors.HexColor('#6A1B9A')
GOLD = colors.HexColor('#FFF2CC')
LIGHT_BLUE = colors.HexColor('#EAF2F8')
LIGHT_GREEN = colors.HexColor('#EAF4EA')
LIGHT_RED = colors.HexColor('#FCE4D6')
LIGHT_PURPLE = colors.HexColor('#F3E5F5')
GRAY = colors.HexColor('#555555')
DARK = colors.HexColor('#202124')
BORDER = colors.HexColor('#AAB7C4')
FORMULA_BG = colors.HexColor('#F5F8FA')
FORMULA_BORDER = colors.HexColor('#B7C9D6')

styles = getSampleStyleSheet()


def _add(name, **kw):
    styles.add(ParagraphStyle(name=name, **kw))


_add('CoverTitle', parent=styles['Title'], fontName=BASE + '-Bold', fontSize=24,
     leading=30, alignment=TA_CENTER, textColor=NAVY, spaceAfter=15)
_add('CoverSub', parent=styles['Normal'], fontName=BASE, fontSize=12.5,
     leading=18, alignment=TA_CENTER, textColor=GRAY, spaceAfter=8)
_add('H1x', parent=styles['Heading1'], fontName=BASE + '-Bold', fontSize=16,
     leading=20, textColor=NAVY, spaceBefore=7, spaceAfter=8, keepWithNext=True)
_add('H2x', parent=styles['Heading2'], fontName=BASE + '-Bold', fontSize=12.5,
     leading=16, textColor=BLUE, spaceBefore=8, spaceAfter=5, keepWithNext=True)
_add('H3x', parent=styles['Heading3'], fontName=BASE + '-Bold', fontSize=11,
     leading=14, textColor=RED, spaceBefore=6, spaceAfter=3, keepWithNext=True)
_add('Bodyx', parent=styles['BodyText'], fontName=BASE, fontSize=9.2,
     leading=13.4, textColor=DARK, spaceAfter=5)
_add('Smallx', parent=styles['BodyText'], fontName=BASE, fontSize=7.9,
     leading=10.6, textColor=GRAY, spaceAfter=3)
_add('BoxTitle', parent=styles['BodyText'], fontName=BASE + '-Bold', fontSize=10,
     leading=13, textColor=NAVY, spaceAfter=3)
_add('Answer', parent=styles['BodyText'], fontName=BASE, fontSize=9.0,
     leading=13.0, leftIndent=8, rightIndent=5, spaceAfter=4)
_add('TOC', parent=styles['BodyText'], fontName=BASE, fontSize=9.8,
     leading=15, leftIndent=8, textColor=DARK, spaceAfter=1)

# Subscritos e sobrescritos Unicode -> tags do ReportLab.
_SUB = {'₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6',
        '₇': '7', '₈': '8', '₉': '9', 'ₘ': 'm', 'ₙ': 'n', 'ₖ': 'k', 'ₐ': 'a',
        'ₑ': 'e', 'ᵢ': 'i', 'ⱼ': 'j', 'ₓ': 'x', 'ᵤ': 'u', 'ᵥ': 'v', 'ₜ': 't',
        'ₒ': 'o', 'ₛ': 's', 'ᵣ': 'r', 'ₗ': 'l', 'ₚ': 'p', 'ₕ': 'h', 'ᵦ': 'β'}
_SUP = {'¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7',
        '⁸': '8', '⁹': '9', '⁰': '0', 'ᴬ': 'A', 'ᴮ': 'B', 'ᶜ': 'C', 'ᴰ': 'D',
        'ᵏ': 'k', 'ᵃ': 'a', 'ᵇ': 'b', 'ᵐ': 'm', 'ⁿ': 'n', 'ᵅ': 'α', 'ᵝ': 'β'}
_SUB_RE = re.compile('([' + ''.join(_SUB) + ']+)')
_SUP_RE = re.compile('([' + ''.join(_SUP) + ']+)')


def clean_text(text):
    """Converte subscritos/sobrescritos Unicode em tags <sub>/<super>."""
    text = _SUB_RE.sub(lambda m: '<sub>' + ''.join(_SUB[c] for c in m.group()) + '</sub>', text)
    text = _SUP_RE.sub(lambda m: '<super>' + ''.join(_SUP[c] for c in m.group()) + '</super>', text)
    return text


def P(text, style='Bodyx'):
    return Paragraph(clean_text(text), styles[style])


# --- LaTeX -----------------------------------------------------------------
MATH_DPI = 350


def _render_latex(latex, fontsize, dpi=MATH_DPI, color='#14213D'):
    """Renderiza uma expressão LaTeX em PNG (com cache em disco) e devolve o caminho."""
    chave = hashlib.sha1(f'{latex}|{fontsize}|{dpi}|{color}'.encode()).hexdigest()[:20]
    caminho = os.path.join(MATH_CACHE, f'{chave}.png')
    if not os.path.exists(caminho):
        fig = plt.figure(figsize=(0.01, 0.01))
        fig.text(0, 0, f'${latex}$', fontsize=fontsize, color=color)
        fig.savefig(caminho, dpi=dpi, bbox_inches='tight', pad_inches=0.012,
                    transparent=True)
        plt.close(fig)
    return caminho


def math(latex, fontsize=10.2, max_width=None):
    """Devolve um Image do ReportLab com a expressão LaTeX no tamanho tipográfico certo."""
    caminho = _render_latex(latex, fontsize)
    px_w, px_h = ImageReader(caminho).getSize()
    # pixels -> pontos, preservando o corpo da fonte
    largura = px_w / MATH_DPI * 72
    altura = px_h / MATH_DPI * 72
    limite = max_width or (CONTENT_W - 1.2 * cm)
    if largura > limite:                      # reduz proporcionalmente se estourar
        altura *= limite / largura
        largura = limite
    im = Image(caminho, width=largura, height=altura)
    im.hAlign = 'LEFT'
    return im


def formula(linhas, fontsize=10.2, juntar=False):
    """
    Bloco de exibição com uma ou mais linhas de LaTeX (sem os '$').
    Ex.: S += formula([r'RMg = CMg', r'P_m = P(Q_m)'])

    Por padrão o bloco PODE quebrar entre páginas (juntar=False). Isso evita os
    vazios enormes que o KeepTogether cria quando o bloco não cabe no resto da
    página. Use juntar=True só em blocos curtos que precisam ficar inteiros.
    """
    if isinstance(linhas, str):
        linhas = [linhas]
    corpo = [[math(l, fontsize)] for l in linhas]
    t = Table(corpo, colWidths=[CONTENT_W], hAlign='LEFT', splitByRow=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), FORMULA_BG),
        ('BOX', (0, 0), (-1, -1), .5, FORMULA_BORDER),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 14),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
    ]))
    bloco = [Spacer(1, 3), t, Spacer(1, 5)]
    # Sempre devolve uma LISTA de flowables: use 'S += formula(...)'.
    return [KeepTogether(bloco)] if juntar and len(linhas) <= 3 else bloco


def bullets(items, style='Bodyx'):
    return [P('• ' + item, style) for item in items]


def note(title, text, bg=GOLD, border=colors.HexColor('#D6B656'), width=None):
    t = Table([[P(title, 'BoxTitle')], [P(text, 'Bodyx')]],
              colWidths=[width or CONTENT_W])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('BOX', (0, 0), (-1, -1), .8, border),
        ('LEFTPADDING', (0, 0), (-1, -1), 9),
        ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 1),
        ('TOPPADDING', (0, 1), (-1, 1), 1),
        ('BOTTOMPADDING', (0, 1), (-1, 1), 6),
    ]))
    return t


def table(data, widths, header=True):
    t = Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign='LEFT')
    cmds = [
        ('GRID', (0, 0), (-1, -1), .35, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
    ]
    if header:
        cmds += [('BACKGROUND', (0, 0), (-1, 0), NAVY),
                 ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                 ('FONTNAME', (0, 0), (-1, 0), BASE + '-Bold')]
        for i in range(1, len(data)):
            if i % 2 == 0:
                cmds.append(('BACKGROUND', (0, i), (-1, i), colors.HexColor('#F3F6F8')))
    t.setStyle(TableStyle(cmds))
    return t


def img(graph_dir, name, width=16.6 * cm):
    path = os.path.join(graph_dir, name)
    if not os.path.exists(path):
        return note('Figura ausente', 'Arquivo não encontrado: ' + name, LIGHT_RED, RED)
    iw, ih = ImageReader(path).getSize()
    im = Image(path, width=width, height=width * ih / iw)
    im.hAlign = 'CENTER'
    return im


def caption(text):
    return P('<b>Figura.</b> ' + text, 'Smallx')


def make_header_footer(left_title, right_title, footer_note):
    def header_footer(canvas, doc):
        canvas.saveState()
        if doc.page > 1:
            canvas.setStrokeColor(colors.HexColor('#D2D9DF'))
            canvas.setLineWidth(.5)
            canvas.line(LEFT, PAGE_H - 1.05 * cm, PAGE_W - RIGHT, PAGE_H - 1.05 * cm)
            canvas.setFont(BASE + '-Bold', 7.6)
            canvas.setFillColor(NAVY)
            canvas.drawString(LEFT, PAGE_H - .78 * cm, left_title)
            canvas.setFont(BASE, 7.6)
            canvas.setFillColor(GRAY)
            canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - .78 * cm, right_title)
        canvas.setStrokeColor(colors.HexColor('#D2D9DF'))
        canvas.setLineWidth(.5)
        canvas.line(LEFT, .95 * cm, PAGE_W - RIGHT, .95 * cm)
        canvas.setFont(BASE, 7.6)
        canvas.setFillColor(GRAY)
        canvas.drawString(LEFT, .63 * cm, footer_note)
        canvas.drawRightString(PAGE_W - RIGHT, .63 * cm, str(doc.page))
        canvas.restoreState()
    return header_footer


def build_pdf(path, story, title, left_title, right_title, footer_note):
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=LEFT, rightMargin=RIGHT,
                          topMargin=TOP, bottomMargin=BOTTOM, title=title, author='Kiro')
    frame = Frame(LEFT, BOTTOM, CONTENT_W, PAGE_H - TOP - BOTTOM, id='normal')
    doc.addPageTemplates([PageTemplate(
        id='main', frames=[frame],
        onPage=make_header_footer(left_title, right_title, footer_note))])
    doc.build(story)
    return path


def cover(title, subtitle, lines, badge=None):
    out = [Spacer(1, 2.2 * cm), P(title, 'CoverTitle'), P(subtitle, 'CoverSub'),
           Spacer(1, 0.9 * cm),
           HRFlowable(width='75%', thickness=2, color=BLUE, hAlign='CENTER'),
           Spacer(1, 0.7 * cm)]
    out += [P(line, 'CoverSub') for line in lines]
    if badge is not None:
        out += [Spacer(1, 1.0 * cm), badge]
    return out
