"""
Estilos e componentes compartilhados pelos PDFs de estudo de Microeconomia II.
Usado por gerar_resumo_pdf.py e gerar_lista1_resolvida_pdf.py.
"""
import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, HRFlowable, Image, PageTemplate, Paragraph,
    Spacer, Table, TableStyle,
)

# --- fontes ----------------------------------------------------------------
_FONT_DIR = '/usr/share/fonts/google-noto'
for _name, _file in [('NotoSans', 'NotoSans-Regular.ttf'),
                     ('NotoSans-Bold', 'NotoSans-Bold.ttf'),
                     ('NotoSans-Italic', 'NotoSans-Italic.ttf'),
                     ('NotoSans-BoldItalic', 'NotoSans-BoldItalic.ttf')]:
    pdfmetrics.registerFont(TTFont(_name, os.path.join(_FONT_DIR, _file)))

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

styles = getSampleStyleSheet()


def _add(name, **kw):
    styles.add(ParagraphStyle(name=name, **kw))


_add('CoverTitle', parent=styles['Title'], fontName='NotoSans-Bold', fontSize=25,
     leading=31, alignment=TA_CENTER, textColor=NAVY, spaceAfter=15)
_add('CoverSub', parent=styles['Normal'], fontName='NotoSans', fontSize=13,
     leading=18, alignment=TA_CENTER, textColor=GRAY, spaceAfter=8)
_add('H1x', parent=styles['Heading1'], fontName='NotoSans-Bold', fontSize=17,
     leading=21, textColor=NAVY, spaceBefore=7, spaceAfter=8, keepWithNext=True)
_add('H2x', parent=styles['Heading2'], fontName='NotoSans-Bold', fontSize=13,
     leading=16, textColor=BLUE, spaceBefore=8, spaceAfter=5, keepWithNext=True)
_add('H3x', parent=styles['Heading3'], fontName='NotoSans-Bold', fontSize=11.5,
     leading=14, textColor=RED, spaceBefore=6, spaceAfter=3, keepWithNext=True)
_add('Bodyx', parent=styles['BodyText'], fontName='NotoSans', fontSize=9.4,
     leading=13.2, textColor=DARK, spaceAfter=5)
_add('Smallx', parent=styles['BodyText'], fontName='NotoSans', fontSize=8.1,
     leading=10.5, textColor=GRAY, spaceAfter=3)
_add('Formula', parent=styles['BodyText'], fontName='Helvetica', fontSize=9.4,
     leading=12.8, leftIndent=11, rightIndent=8, borderColor=colors.HexColor('#B7C9D6'),
     borderWidth=.5, borderPadding=6, backColor=colors.HexColor('#F5F8FA'),
     spaceBefore=4, spaceAfter=6)
_add('BoxTitle', parent=styles['BodyText'], fontName='NotoSans-Bold', fontSize=10.2,
     leading=13, textColor=NAVY, spaceAfter=3)
_add('Answer', parent=styles['BodyText'], fontName='NotoSans', fontSize=9.1,
     leading=12.8, leftIndent=8, rightIndent=5, spaceAfter=4)
_add('TOC', parent=styles['BodyText'], fontName='NotoSans', fontSize=10,
     leading=15, leftIndent=8, textColor=DARK, spaceAfter=1)

# Substituicoes que mantem as formulas legiveis em qualquer leitor de PDF.
_REPL = {
    '₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4', '₅': '5', '₆': '6',
    '₇': '7', '₈': '8', '₉': '9', 'ₘ': 'm', 'ₙ': 'n', 'ₖ': 'k', 'ₐ': 'a',
    'ₑ': 'e', 'ᵢ': 'i', 'ᵏ': 'k', 'ᴬ': 'A', 'ᴮ': 'B', 'ᵃ': 'a', 'ᵇ': 'b',
    '¹': '^1', '²': '^2', '³': '^3', '⁴': '^4', '⁵': '^5', '⁶': '^6',
    '⁷': '^7', '⁸': '^8', '⁹': '^9', 'ᵅ': 'alpha', 'ᵝ': 'beta',
    '−': '-', '⇒': '=>', 'Σ': 'SUM', '∑': 'SUM', '½': '1/2', '·': '*',
    '×': '*', '≈': '~', '≤': '<=', '≥': '>=', '□': '[  ]',
}


def clean_text(text):
    for a, b in _REPL.items():
        text = text.replace(a, b)
    return text


def P(text, style='Bodyx'):
    return Paragraph(clean_text(text), styles[style])


def F(text):
    """Bloco de fórmula: preserva quebras de linha e o alinhamento por espaços."""
    linhas = [re.sub(r' {2,}', lambda m: '&nbsp;' * len(m.group()), linha)
              for linha in clean_text(text).split('\n')]
    return Paragraph('<br/>'.join(linhas), styles['Formula'])


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
                 ('FONTNAME', (0, 0), (-1, 0), 'NotoSans-Bold')]
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
            canvas.setFont('NotoSans-Bold', 8)
            canvas.setFillColor(NAVY)
            canvas.drawString(LEFT, PAGE_H - .78 * cm, left_title)
            canvas.setFont('NotoSans', 8)
            canvas.setFillColor(GRAY)
            canvas.drawRightString(PAGE_W - RIGHT, PAGE_H - .78 * cm, right_title)
        canvas.setStrokeColor(colors.HexColor('#D2D9DF'))
        canvas.setLineWidth(.5)
        canvas.line(LEFT, .95 * cm, PAGE_W - RIGHT, .95 * cm)
        canvas.setFont('NotoSans', 8)
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
