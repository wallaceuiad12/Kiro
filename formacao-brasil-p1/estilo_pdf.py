"""
Estilos e componentes compartilhados pelos PDFs de estudo de Formação do Brasil.

Mesma linguagem visual dos PDFs de Microeconomia II (fontes DejaVu, paleta navy,
cabeçalho/rodapé, capa), mas sem a maquinaria de LaTeX — este é um material de
humanas, com tabelas comparativas e caixas de destaque em vez de fórmulas.

Usado por gerar_resumo_pdf.py.
"""
import glob

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate, Frame, HRFlowable, KeepTogether, PageTemplate,
    Paragraph, Spacer, Table, TableStyle,
)


# --- fontes ----------------------------------------------------------------
# DejaVu Sans cobre os símbolos usados no texto (× → ≈ —) e é a mesma família
# dos outros materiais de estudo do repositório.
def _dejavu(nome_arquivo):
    padroes = [
        f'/usr/local/lib*/python3*/site-packages/matplotlib/mpl-data/fonts/ttf/{nome_arquivo}',
        f'/usr/lib*/python3*/site-packages/matplotlib/mpl-data/fonts/ttf/{nome_arquivo}',
        f'/root/.pyenv/versions/*/lib/python3*/site-packages/matplotlib/mpl-data/fonts/ttf/{nome_arquivo}',
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

styles = getSampleStyleSheet()


def _add(name, **kw):
    styles.add(ParagraphStyle(name=name, **kw))


_add('CoverTitle', parent=styles['Title'], fontName=BASE + '-Bold', fontSize=23,
     leading=29, alignment=TA_CENTER, textColor=NAVY, spaceAfter=15)
_add('CoverSub', parent=styles['Normal'], fontName=BASE, fontSize=12.5,
     leading=18, alignment=TA_CENTER, textColor=GRAY, spaceAfter=8)
_add('H1x', parent=styles['Heading1'], fontName=BASE + '-Bold', fontSize=15.5,
     leading=19.5, textColor=NAVY, spaceBefore=7, spaceAfter=7, keepWithNext=True)
_add('H2x', parent=styles['Heading2'], fontName=BASE + '-Bold', fontSize=12,
     leading=15.5, textColor=BLUE, spaceBefore=8, spaceAfter=4, keepWithNext=True)
_add('H3x', parent=styles['Heading3'], fontName=BASE + '-Bold', fontSize=10.5,
     leading=13.5, textColor=RED, spaceBefore=6, spaceAfter=3, keepWithNext=True)
_add('Bodyx', parent=styles['BodyText'], fontName=BASE, fontSize=9.2,
     leading=13.4, textColor=DARK, spaceAfter=5, alignment=TA_JUSTIFY)
_add('Bulletx', parent=styles['BodyText'], fontName=BASE, fontSize=9.2,
     leading=13.2, textColor=DARK, spaceAfter=3.5, leftIndent=11,
     firstLineIndent=-11, alignment=TA_JUSTIFY)
_add('SubBulletx', parent=styles['BodyText'], fontName=BASE, fontSize=9.0,
     leading=12.8, textColor=DARK, spaceAfter=3, leftIndent=24,
     firstLineIndent=-11, alignment=TA_JUSTIFY)
_add('Smallx', parent=styles['BodyText'], fontName=BASE, fontSize=7.9,
     leading=10.6, textColor=GRAY, spaceAfter=3)
_add('BoxTitle', parent=styles['BodyText'], fontName=BASE + '-Bold', fontSize=10,
     leading=13, textColor=NAVY, spaceAfter=3)
_add('Cell', parent=styles['BodyText'], fontName=BASE, fontSize=8.0,
     leading=11.0, textColor=DARK, spaceAfter=0)
_add('CellHead', parent=styles['BodyText'], fontName=BASE + '-Bold', fontSize=8.2,
     leading=11.0, textColor=colors.white, spaceAfter=0)
_add('TOC', parent=styles['BodyText'], fontName=BASE, fontSize=9.8,
     leading=15.5, leftIndent=8, textColor=DARK, spaceAfter=1)


def P(text, style='Bodyx'):
    return Paragraph(text, styles[style])


def bullets(items, style='Bulletx'):
    """Lista com marcador; itens iniciados por '>' viram sub-itens recuados."""
    out = []
    for item in items:
        if item.startswith('>'):
            out.append(P('–  ' + item[1:].strip(), 'SubBulletx'))
        else:
            out.append(P('•  ' + item, style))
    return out


def note(title, text, bg=GOLD, border=colors.HexColor('#D6B656'), width=None):
    """Caixa de destaque com título e corpo."""
    linhas = text if isinstance(text, list) else [text]
    corpo = [[P(title, 'BoxTitle')]] + [[P(l, 'Bodyx')] for l in linhas]
    t = Table(corpo, colWidths=[width or CONTENT_W], splitByRow=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg),
        ('BOX', (0, 0), (-1, -1), .8, border),
        ('LEFTPADDING', (0, 0), (-1, -1), 9),
        ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 1),
        ('TOPPADDING', (0, 1), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ]))
    return [Spacer(1, 3), t, Spacer(1, 5)]


def table(data, widths, header=True, align='LEFT'):
    """Tabela com cabeçalho navy e linhas zebradas. Células são strings (viram Paragraph)."""
    corpo = []
    for i, linha in enumerate(data):
        estilo = 'CellHead' if (header and i == 0) else 'Cell'
        corpo.append([c if hasattr(c, 'wrap') else P(str(c), estilo) for c in linha])
    t = Table(corpo, colWidths=widths, repeatRows=1 if header else 0,
              hAlign=align, splitByRow=1)
    cmds = [
        ('GRID', (0, 0), (-1, -1), .35, BORDER),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 4.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
    ]
    if header:
        cmds += [('BACKGROUND', (0, 0), (-1, 0), NAVY)]
        for i in range(1, len(data)):
            if i % 2 == 0:
                cmds.append(('BACKGROUND', (0, i), (-1, i), colors.HexColor('#F3F6F8')))
    t.setStyle(TableStyle(cmds))
    return [Spacer(1, 3), t, Spacer(1, 6)]


def rule(width='100%', thickness=.6, color=BORDER, space=6):
    return [Spacer(1, space), HRFlowable(width=width, thickness=thickness,
                                         color=color, hAlign='LEFT'),
            Spacer(1, space)]


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
        out += [Spacer(1, 1.0 * cm)] + (badge if isinstance(badge, list) else [badge])
    return out
