"""
Gera `gabarito-econopol2-prova1.pdf` a partir de `GABARITO.md`.

O Markdown é a ÚNICA fonte do conteúdo: edite `GABARITO.md` e rode este script
para regerar o PDF. Nada de texto duplicado entre os dois arquivos.

Reaproveita o módulo de estilo já existente no repositório
(`micro2-prova1/estilo_pdf.py`), inclusive a renderização de LaTeX via mathtext.

Subconjunto de Markdown suportado:
  #  ##  ###  ####     títulos (o primeiro `#` vira a capa)
  ---                  linha horizontal
  >                    citação (bloco destacado)
  -  /  2 espaços + -  listas com dois níveis
  1.                   listas numeradas
  | a | b |            tabelas com linha separadora `| --- |`
  $$ ... $$            fórmula em bloco (LaTeX renderizado)
  **negrito**  *itálico*  `código`  $inline$

Uso:  python3 gerar_gabarito_pdf.py
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
# O módulo de estilo vive na pasta de Microeconomia II; reaproveitamos em vez de
# duplicar ~300 linhas de configuração de fontes, cores e componentes.
sys.path.insert(0, os.path.join(os.path.dirname(ROOT), 'micro2-prova1'))

from reportlab.lib import colors                                  # noqa: E402
from reportlab.lib.styles import ParagraphStyle                   # noqa: E402
from reportlab.lib.units import cm                                # noqa: E402
from reportlab.platypus import (                                  # noqa: E402
    HRFlowable, PageBreak, Paragraph, Spacer, Table, TableStyle,
)

import estilo_pdf as E                                            # noqa: E402

MD = os.path.join(ROOT, 'GABARITO.md')
OUT = os.path.join(ROOT, 'gabarito-econopol2-prova1.pdf')

# --- estilos próprios deste documento --------------------------------------
E.styles.add(ParagraphStyle(
    name='Bullet0', parent=E.styles['Bodyx'], leftIndent=14, bulletIndent=4,
    spaceAfter=3))
E.styles.add(ParagraphStyle(
    name='Bullet1', parent=E.styles['Bodyx'], leftIndent=29, bulletIndent=19,
    spaceAfter=2.5))
E.styles.add(ParagraphStyle(
    name='Quote', parent=E.styles['Bodyx'], fontName=E.BASE + '-Italic',
    fontSize=8.9, leading=13, textColor=E.BLUE, spaceAfter=0))
E.styles.add(ParagraphStyle(
    name='Cell', parent=E.styles['Bodyx'], fontSize=8.3, leading=11.4,
    spaceAfter=0))
E.styles.add(ParagraphStyle(
    name='CellHead', parent=E.styles['Cell'], fontName=E.BASE + '-Bold',
    textColor=colors.white))

# --- conversão de LaTeX inline para Unicode --------------------------------
_SIMBOLOS = [
    (r'\Delta', 'Δ'), (r'\cdot', '·'), (r'\times', '×'), (r'\Rightarrow', '⇒'),
    (r'\rightarrow', '→'), (r'\uparrow', '↑'), (r'\downarrow', '↓'),
    (r'\leq', '≤'), (r'\geq', '≥'), (r'\neq', '≠'), (r'\approx', '≈'),
    (r'\quad', ' '), (r'\qquad', '  '), (r'\,', ' '),
]


def _inline_math(latex):
    """`$...$` -> texto corrido com símbolos Unicode (sem imagem)."""
    s = latex
    for cmd, uni in _SIMBOLOS:
        s = s.replace(cmd, uni)
    s = re.sub(r'\\(?:text|mathrm|mathit)\{([^}]*)\}', r'\1', s)
    s = re.sub(r'\\frac\{([^}]*)\}\{([^}]*)\}', r'\1/\2', s)
    s = s.replace("'", '′').replace('{', '').replace('}', '')
    return re.sub(r'\s+', ' ', s).strip()


# --- conversão de Markdown inline para marcação do ReportLab ---------------
def _enfase(texto):
    """
    Converte *itálico*, **negrito** e ***ambos*** usando uma pilha, de modo que
    aninhamentos como `**Livro I de *O Capital***` gerem tags bem formadas
    (`<b>Livro I de <i>O Capital</i></b>`) em vez de tags cruzadas.
    """
    saida, pilha = [], []
    for seg in re.split(r'(\*{1,3})', texto):
        if not re.fullmatch(r'\*{1,3}', seg):
            saida.append(seg)
            continue
        quer = {1: ['i'], 2: ['b'], 3: ['b', 'i']}[len(seg)]
        if all(t in pilha for t in quer):          # fecha, em ordem LIFO
            while pilha and pilha[-1] in quer:
                saida.append(f'</{pilha.pop()}>')
        else:                                      # abre
            for t in quer:
                pilha.append(t)
                saida.append(f'<{t}>')
    while pilha:                                   # delimitador órfão
        saida.append(f'</{pilha.pop()}>')
    return ''.join(saida)


def inline(texto):
    """**negrito**, *itálico*, `código`, $matemática$ -> tags do ReportLab."""
    # 1. protege a matemática inline antes de qualquer escape
    guardados = []

    def _guarda(m):
        guardados.append(_inline_math(m.group(1)))
        return f'\x00{len(guardados) - 1}\x00'

    texto = re.sub(r'\$([^$\n]+)\$', _guarda, texto)

    # 2. escapa o que o ReportLab interpretaria como marcação
    texto = (texto.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))

    # 3. marcação Markdown -> tags
    texto = _enfase(texto)
    texto = re.sub(r'`([^`]+)`', r'<font face="Courier" size="8.2">\1</font>', texto)

    # 4. devolve a matemática
    def _solta(m):
        return '<i>' + guardados[int(m.group(1))] + '</i>'

    return re.sub(r'\x00(\d+)\x00', _solta, texto)


def par(texto, estilo='Bodyx', **kw):
    return Paragraph(E.clean_text(inline(texto)), E.styles[estilo], **kw)


# --- blocos ----------------------------------------------------------------
def bloco_citacao(linhas):
    """Citação destacada, com barra azul à esquerda."""
    corpo = [[par(' '.join(linhas), 'Quote')]]
    t = Table(corpo, colWidths=[E.CONTENT_W], hAlign='LEFT')
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), E.LIGHT_BLUE),
        ('LINEBEFORE', (0, 0), (0, -1), 2.2, E.BLUE),
        ('LEFTPADDING', (0, 0), (-1, -1), 11),
        ('RIGHTPADDING', (0, 0), (-1, -1), 9),
        ('TOPPADDING', (0, 0), (-1, -1), 7),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
    ]))
    return [Spacer(1, 3), t, Spacer(1, 6)]


def bloco_tabela(linhas):
    """Tabela Markdown -> tabela do ReportLab, com larguras proporcionais."""
    def celulas(linha):
        return [c.strip() for c in linha.strip().strip('|').split('|')]

    linhas = [l for l in linhas if not re.fullmatch(r'\|[\s:|-]+\|', l.strip())]
    dados = [celulas(l) for l in linhas]
    n = max(len(r) for r in dados)
    dados = [r + [''] * (n - len(r)) for r in dados]

    # Largura proporcional ao maior conteúdo da coluna, com piso de 8%. O peso
    # considera também a palavra mais longa (x1.8), para que cabeçalhos curtos
    # como "Resultado" não sejam quebrados no meio.
    pesos = []
    for j in range(n):
        limpos = [re.sub(r'[*`$\\]', '', r[j]) for r in dados]
        maior = max(len(c) for c in limpos)
        palavra = max((len(p) for c in limpos for p in c.split()), default=1)
        pesos.append(max(maior, palavra * 1.8, 6))
    total = sum(pesos)
    larguras = [max(0.08, p / total) * E.CONTENT_W for p in pesos]
    fator = E.CONTENT_W / sum(larguras)
    larguras = [w * fator for w in larguras]

    corpo = [[par(c, 'CellHead') for c in dados[0]]]
    corpo += [[par(c, 'Cell') for c in r] for r in dados[1:]]
    return [Spacer(1, 3), E.table(corpo, larguras, header=True), Spacer(1, 7)]


def renderizar(md):
    story = []
    linhas = md.split('\n')
    i = 0
    capa_feita = False

    while i < len(linhas):
        linha = linhas[i]
        crua = linha.rstrip()
        texto = crua.strip()

        # linha em branco
        if not texto:
            i += 1
            continue

        # fórmula em bloco: $$ ... $$
        if texto.startswith('$$'):
            buf = []
            if texto.endswith('$$') and len(texto) > 4:
                buf.append(texto[2:-2].strip())
                i += 1
            else:
                buf.append(texto[2:].strip())
                i += 1
                while i < len(linhas) and not linhas[i].strip().endswith('$$'):
                    buf.append(linhas[i].strip())
                    i += 1
                if i < len(linhas):
                    buf.append(linhas[i].strip().rstrip('$'))
                    i += 1
            latex = ' '.join(b for b in buf if b)
            story += E.formula([latex], fontsize=9.6)
            continue

        # títulos
        m = re.match(r'^(#{1,4})\s+(.*)$', texto)
        if m:
            nivel, titulo = len(m.group(1)), m.group(2)
            if nivel == 1 and not capa_feita:
                story += E.cover(
                    inline(titulo),
                    'Gabarito detalhado e comentado das duas listas de questões',
                    ['Livro I de <i>O Capital</i>, de Karl Marx',
                     'Lista de Questões I (2025) &amp; Prova 1 (26/09/2024)',
                     'Capítulos 4, 5, 6, 7, 9, 10, 13, 21, 22, 23 e 24'])
                story.append(PageBreak())
                capa_feita = True
            else:
                estilo = {1: 'H1x', 2: 'H1x', 3: 'H2x', 4: 'H3x'}[nivel]
                if nivel <= 2:
                    story.append(Spacer(1, 6))
                story.append(par(titulo, estilo))
            i += 1
            continue

        # linha horizontal
        if re.fullmatch(r'-{3,}', texto):
            story += [Spacer(1, 5),
                      HRFlowable(width='100%', thickness=0.7, color=E.BORDER),
                      Spacer(1, 5)]
            i += 1
            continue

        # citação
        if texto.startswith('>'):
            buf = []
            while i < len(linhas) and linhas[i].strip().startswith('>'):
                buf.append(linhas[i].strip().lstrip('>').strip())
                i += 1
            story += bloco_citacao([b for b in buf if b])
            continue

        # tabela
        if texto.startswith('|'):
            buf = []
            while i < len(linhas) and linhas[i].strip().startswith('|'):
                buf.append(linhas[i])
                i += 1
            story += bloco_tabela(buf)
            continue

        # item de lista (com ou sem recuo), possivelmente em várias linhas
        m = re.match(r'^(\s*)(?:([-*])|(\d+)\.)\s+(.*)$', crua)
        if m:
            recuo = len(m.group(1))
            marcador = '•' if m.group(2) else f'{m.group(3)}.'
            buf = [m.group(4)]
            i += 1
            # continuações: linhas mais indentadas que não iniciem novo item
            while i < len(linhas):
                seg = linhas[i]
                if not seg.strip():
                    break
                if re.match(r'^(\s*)(?:[-*]|\d+\.)\s+', seg):
                    break
                if seg.strip().startswith(('|', '>', '#', '$$', '---')):
                    break
                if len(seg) - len(seg.lstrip()) <= recuo and recuo == 0:
                    break
                buf.append(seg.strip())
                i += 1
            estilo = 'Bullet1' if recuo >= 2 else 'Bullet0'
            story.append(par(' '.join(buf), estilo, bulletText=marcador))
            continue

        # parágrafo comum (junta linhas até a próxima em branco / bloco novo)
        buf = [texto]
        i += 1
        while i < len(linhas):
            seg = linhas[i].strip()
            if not seg or seg.startswith(('|', '>', '#', '$$', '---')):
                break
            if re.match(r'^(\s*)(?:[-*]|\d+\.)\s+', linhas[i]):
                break
            buf.append(seg)
            i += 1
        story.append(par(' '.join(buf)))

    return story


def main():
    with open(MD, encoding='utf-8') as f:
        md = f.read()

    story = renderizar(md)
    E.build_pdf(
        OUT, story,
        title='Gabarito comentado — Economia Política II',
        left_title='Economia Política II — gabarito comentado',
        right_title="Livro I d'O Capital",
        footer_note='Lista de Questões I (2025) e Prova 1 (26/09/2024)')
    print(f'PDF gerado: {OUT}')
    print(f'Flowables:  {len(story)}')


if __name__ == '__main__':
    main()
