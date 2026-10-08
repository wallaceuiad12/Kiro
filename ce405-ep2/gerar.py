# -*- coding: utf-8 -*-
"""
Insere as respostas dissertativas da lista de Economia Política II dentro do
próprio .docx das questões, logo abaixo de cada enunciado, e gera também uma
versão em Markdown.

Uso:
    python3 ce405-ep2/gerar.py

Entrada : ce405-ep2/ce_405_c_lista_1_exercicios-original.docx  (cópia limpa)
Saídas  : ce_405_c_lista_1_exercicios.docx  (questões com as respostas)
          ce405-ep2/lista1-resolvida.md     (mesmo conteúdo em Markdown)

As respostas são parágrafos de prosa corrida, sem tópicos, subtítulos ou tabelas,
porque o destino é a reprodução à mão em prova. O script sempre reconstrói o
resultado a partir da cópia limpa, de modo que reexecutá-lo é idempotente.
"""
import os
import re
import shutil
import sys

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from respostas import RESPOSTAS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AQUI = os.path.dirname(os.path.abspath(__file__))
DOCX = os.path.join(ROOT, 'ce_405_c_lista_1_exercicios.docx')
ORIGINAL = os.path.join(AQUI, 'ce_405_c_lista_1_exercicios-original.docx')
MD = os.path.join(AQUI, 'lista1-resolvida.md')

FONTE = 'Times New Roman'
CORPO = 11.5          # pt, mesmo corpo dos enunciados
AZUL = RGBColor(0x1F, 0x38, 0x64)
CINZA = RGBColor(0x40, 0x40, 0x40)

TOKEN = re.compile(r'(\*\*[^*]+\*\*|\*[^*]+\*)')

# O esquema do OOXML exige ordem fixa dos filhos de pPr. Anexar no fim gera
# arquivo que o Word acusa como corrompido, por isso w:pBdr é inserido antes dos
# seus sucessores legítimos (lista extraída de CT_PPr do python-docx).
_SUC_PBDR = ('w:shd', 'w:tabs', 'w:suppressAutoHyphens', 'w:kinsoku', 'w:wordWrap',
             'w:overflowPunct', 'w:topLinePunct', 'w:autoSpaceDE', 'w:autoSpaceDN',
             'w:bidi', 'w:adjustRightInd', 'w:snapToGrid', 'w:spacing', 'w:ind',
             'w:contextualSpacing', 'w:mirrorIndents', 'w:suppressOverlap', 'w:jc',
             'w:textDirection', 'w:textAlignment', 'w:textboxTightWrap', 'w:outlineLvl',
             'w:divId', 'w:cnfStyle', 'w:rPr', 'w:sectPr', 'w:pPrChange')


# --------------------------------------------------------------------- helpers
def _xml(tag, **attrs):
    from docx.oxml import OxmlElement
    el = OxmlElement(tag)
    for chave, valor in attrs.items():
        el.set(qn('w:' + chave), valor)
    return el


def _borda_superior(par, cor='BFBFBF'):
    pPr = par._p.get_or_add_pPr()
    bordas = _xml('w:pBdr')
    bordas.append(_xml('w:top', val='single', sz='8', space='6', color=cor))
    pPr.insert_element_before(bordas, *_SUC_PBDR)


def _runs(par, texto, tamanho=CORPO, cor=None, negrito_tudo=False, italico_tudo=False):
    """Escreve `texto` no parágrafo, interpretando **negrito** e *itálico*."""
    for pedaco in TOKEN.split(texto):
        if not pedaco:
            continue
        negrito, italico = negrito_tudo, italico_tudo
        if pedaco.startswith('**') and pedaco.endswith('**'):
            pedaco, negrito = pedaco[2:-2], True
        elif pedaco.startswith('*') and pedaco.endswith('*'):
            pedaco, italico = pedaco[1:-1], True
        run = par.add_run(pedaco)
        run.font.name = FONTE
        run.font.size = Pt(tamanho)
        run.font.bold = negrito
        run.font.italic = italico
        if cor is not None:
            run.font.color.rgb = cor
    return par


def _novo_par(doc, esquerda=0.5, primeira_linha=0.0, antes=0, depois=6,
              alinhamento=WD_ALIGN_PARAGRAPH.JUSTIFY):
    par = doc.add_paragraph()
    par.style = doc.styles['Normal']
    pf = par.paragraph_format
    pf.left_indent = Cm(esquerda)
    pf.first_line_indent = Cm(primeira_linha)
    pf.space_before = Pt(antes)
    pf.space_after = Pt(depois)
    pf.alignment = alinhamento
    pf.line_spacing = 1.15
    # impede que o parágrafo herde a numeração automática da lista do documento
    pPr = par._p.get_or_add_pPr()
    for numPr in pPr.findall(qn('w:numPr')):
        pPr.remove(numPr)
    return par


# ------------------------------------------------------------------ renderizador
def construir_blocos(doc, resposta):
    """Cria os elementos XML de uma resposta e devolve-os na ordem de leitura."""
    elementos = []

    cab = _novo_par(doc, esquerda=0.5, antes=12, depois=4,
                    alinhamento=WD_ALIGN_PARAGRAPH.LEFT)
    _borda_superior(cab)
    _runs(cab, resposta['rotulo'], cor=AZUL, negrito_tudo=True)
    elementos.append(cab._p)

    for texto in resposta['paragrafos']:
        par = _novo_par(doc, esquerda=0.5, primeira_linha=0.75, depois=6)
        _runs(par, texto)
        elementos.append(par._p)

    return elementos


def nota_de_cabecalho(doc):
    par = _novo_par(doc, esquerda=0, antes=2, depois=10,
                    alinhamento=WD_ALIGN_PARAGRAPH.CENTER)
    _runs(par, 'Respostas dissertativas inseridas abaixo de cada questão. '
               'Referência: MARX, K. O Capital, Livro I (ed. Boitempo).',
          tamanho=10, cor=CINZA, italico_tudo=True)
    return par._p


# ------------------------------------------------------------------------ main
def escrever_docx():
    if not os.path.exists(ORIGINAL):
        shutil.copy2(DOCX, ORIGINAL)   # guarda uma cópia limpa das questões
    doc = docx.Document(ORIGINAL)      # parte sempre do original, idempotente
    paragrafos = list(doc.paragraphs)

    for resposta in RESPOSTAS:
        ancora = paragrafos[resposta['depois']]._p
        for elemento in reversed(construir_blocos(doc, resposta)):
            ancora.addnext(elemento)

    paragrafos[0]._p.addnext(nota_de_cabecalho(doc))
    doc.save(DOCX)
    return DOCX


def escrever_markdown():
    doc = docx.Document(ORIGINAL)
    paragrafos = [p.text.strip() for p in doc.paragraphs]
    por_indice = {r['depois']: r for r in RESPOSTAS}

    saida = ['# Lista de Questões I de Economia Política II (CE405, turma C, 2025)',
             '',
             'Questões transcritas do enunciado original, com as respostas dissertativas '
             'logo abaixo de cada uma. Referência: MARX, Karl. *O Capital*, Livro I '
             '(ed. Boitempo).',
             '']

    for i, texto in enumerate(paragrafos):
        if texto and i > 0:
            if texto.lower().startswith('capítulo'):
                saida += ['', '## ' + texto, '']
            else:
                saida += ['> ' + texto, '']
        if i in por_indice:
            resposta = por_indice[i]
            saida += ['**' + resposta['rotulo'] + '**', '']
            for par in resposta['paragrafos']:
                saida += [par, '']

    with open(MD, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(saida).replace('\n\n\n', '\n\n') + '\n')
    return MD


def contar_palavras():
    return [(r['rotulo'], sum(len(p.split()) for p in r['paragrafos']),
             len(r['paragrafos'])) for r in RESPOSTAS]


if __name__ == '__main__':
    print('respostas carregadas:', len(RESPOSTAS))
    print('docx     ->', escrever_docx())
    print('markdown ->', escrever_markdown())
    print()
    print('%-22s %8s %11s' % ('resposta', 'palavras', 'parágrafos'))
    total = 0
    for rotulo, palavras, pars in contar_palavras():
        total += palavras
        print('%-22s %8d %11d' % (rotulo, palavras, pars))
    print('%-22s %8d' % ('TOTAL', total))
