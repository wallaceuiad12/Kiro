from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, PageBreak,
    Image, Table, TableStyle, KeepTogether, HRFlowable
)
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.utils import ImageReader
import os

# Noto Sans cobre acentos, subscritos/sobrescritos e símbolos matemáticos usados no material.
pdfmetrics.registerFont(TTFont('NotoSans', '/usr/share/fonts/google-noto/NotoSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('NotoSans-Bold', '/usr/share/fonts/google-noto/NotoSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('NotoSans-Italic', '/usr/share/fonts/google-noto/NotoSans-Italic.ttf'))
pdfmetrics.registerFont(TTFont('NotoSans-BoldItalic', '/usr/share/fonts/google-noto/NotoSans-BoldItalic.ttf'))

ROOT = os.path.dirname(os.path.abspath(__file__))
GRAPH = os.path.join(ROOT, "graficos")
OUT = os.path.join(ROOT, "resumo-micro2-prova1.pdf")

# Built-in Helvetica is sufficient for Portuguese accents in ReportLab's WinAnsi encoding.
PAGE_W, PAGE_H = A4
LEFT = RIGHT = 1.65 * cm
TOP = 1.65 * cm
BOTTOM = 1.55 * cm

NAVY = colors.HexColor('#17365D')
BLUE = colors.HexColor('#1F4E79')
RED = colors.HexColor('#A61C00')
GREEN = colors.HexColor('#2E7D32')
GOLD = colors.HexColor('#FFF2CC')
LIGHT_BLUE = colors.HexColor('#EAF2F8')
LIGHT_GREEN = colors.HexColor('#EAF4EA')
LIGHT_RED = colors.HexColor('#FCE4D6')
GRAY = colors.HexColor('#555555')
DARK = colors.HexColor('#202124')

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CoverTitle', parent=styles['Title'], fontName='NotoSans-Bold', fontSize=25, leading=31, alignment=TA_CENTER, textColor=NAVY, spaceAfter=15))
styles.add(ParagraphStyle(name='CoverSub', parent=styles['Normal'], fontName='NotoSans', fontSize=13, leading=18, alignment=TA_CENTER, textColor=GRAY, spaceAfter=8))
styles.add(ParagraphStyle(name='H1x', parent=styles['Heading1'], fontName='NotoSans-Bold', fontSize=17, leading=21, textColor=NAVY, spaceBefore=7, spaceAfter=8, keepWithNext=True))
styles.add(ParagraphStyle(name='H2x', parent=styles['Heading2'], fontName='NotoSans-Bold', fontSize=13, leading=16, textColor=BLUE, spaceBefore=8, spaceAfter=5, keepWithNext=True))
styles.add(ParagraphStyle(name='H3x', parent=styles['Heading3'], fontName='NotoSans-Bold', fontSize=11.5, leading=14, textColor=RED, spaceBefore=6, spaceAfter=3, keepWithNext=True))
styles.add(ParagraphStyle(name='Bodyx', parent=styles['BodyText'], fontName='NotoSans', fontSize=9.4, leading=13.2, textColor=DARK, spaceAfter=5))
styles.add(ParagraphStyle(name='Smallx', parent=styles['BodyText'], fontName='NotoSans', fontSize=8.1, leading=10.5, textColor=GRAY, spaceAfter=3))
styles.add(ParagraphStyle(name='Formula', parent=styles['BodyText'], fontName='Helvetica', fontSize=9.0, leading=12.2, leftIndent=11, rightIndent=8, borderColor=colors.HexColor('#B7C9D6'), borderWidth=.5, borderPadding=6, backColor=colors.HexColor('#F5F8FA'), spaceBefore=4, spaceAfter=6))
styles.add(ParagraphStyle(name='BoxTitle', parent=styles['BodyText'], fontName='NotoSans-Bold', fontSize=10.2, leading=13, textColor=NAVY, spaceAfter=3))
styles.add(ParagraphStyle(name='Answer', parent=styles['BodyText'], fontName='NotoSans', fontSize=9.1, leading=12.8, leftIndent=8, rightIndent=5, spaceAfter=4))
styles.add(ParagraphStyle(name='TOC', parent=styles['BodyText'], fontName='NotoSans', fontSize=10, leading=15, leftIndent=8, textColor=DARK, spaceAfter=1))


def clean_text(text):
    # Keep formulas legible even in PDF viewers whose default fonts lack Unicode math glyphs.
    repl = {
        '₀':'0','₁':'1','₂':'2','₃':'3','₄':'4','₅':'5','₆':'6','₇':'7','₈':'8','₉':'9',
        'ₘ':'m','ₙ':'n','ₖ':'k','ₐ':'a','ₑ':'e','ᵢ':'i','ᵏ':'k','ᴬ':'A','ᴮ':'B','ᵃ':'a','ᵇ':'b',
        '¹':'^1','²':'^2','³':'^3','⁴':'^4','⁵':'^5','⁶':'^6','⁷':'^7','⁸':'^8','⁹':'^9',
        '−':'-','⇒':'=>','Σ':'SUM','∑':'SUM','½':'1/2','·':'*','×':'*','≈':'~','≤':'<=','≥':'>=',
        '□':'[ ]','ᵅ':'alpha','ᵝ':'beta'
    }
    for a,b in repl.items(): text=text.replace(a,b)
    return text

def P(text, style='Bodyx'):
    return Paragraph(clean_text(text), styles[style])

def F(text):
    return P(text, 'Formula')

def bullets(items, style='Bodyx'):
    out=[]
    for item in items:
        out.append(P('• ' + item, style))
    return out

def note(title, text, bg=GOLD, border=colors.HexColor('#D6B656')):
    t=Table([[P(title,'BoxTitle')],[P(text,'Bodyx')]], colWidths=[PAGE_W-LEFT-RIGHT])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),bg), ('BOX',(0,0),(-1,-1),.8,border),
        ('LEFTPADDING',(0,0),(-1,-1),9), ('RIGHTPADDING',(0,0),(-1,-1),9),
        ('TOPPADDING',(0,0),(-1,0),6), ('BOTTOMPADDING',(0,0),(-1,0),1),
        ('TOPPADDING',(0,1),(-1,1),1), ('BOTTOMPADDING',(0,1),(-1,1),6),
    ]))
    return t

def table(data, widths, header=True, font=8.2):
    t=Table(data, colWidths=widths, repeatRows=1 if header else 0, hAlign='LEFT')
    cmds=[('GRID',(0,0),(-1,-1),.35,colors.HexColor('#AAB7C4')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]
    if header:
        cmds += [('BACKGROUND',(0,0),(-1,0),NAVY),('TEXTCOLOR',(0,0),(-1,0),colors.white),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold')]
        for i in range(1,len(data)):
            if i%2==0: cmds.append(('BACKGROUND',(0,i),(-1,i),colors.HexColor('#F3F6F8')))
    t.setStyle(TableStyle(cmds))
    return t

def img(name, width=16.8*cm):
    path=os.path.join(GRAPH,name)
    if not os.path.exists(path):
        return note('Figura ausente', 'O arquivo de imagem não foi encontrado: '+name, LIGHT_RED, RED)
    iw, ih = ImageReader(path).getSize()
    height=width*ih/iw
    im=Image(path, width=width, height=height)
    im.hAlign='CENTER'
    return im

def caption(text):
    return P('<b>Figura.</b> '+text, 'Smallx')

class NumberedCanvas:
    pass

def header_footer(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(colors.HexColor('#D2D9DF'))
        canvas.setLineWidth(.5)
        canvas.line(LEFT, PAGE_H-1.05*cm, PAGE_W-RIGHT, PAGE_H-1.05*cm)
        canvas.setFont('Helvetica-Bold', 8)
        canvas.setFillColor(NAVY)
        canvas.drawString(LEFT, PAGE_H-.78*cm, 'MICROECONOMIA II — RESUMO DA PROVA 1')
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(GRAY)
        canvas.drawRightString(PAGE_W-RIGHT, PAGE_H-.78*cm, 'CE-362D | Unicamp | 2º semestre de 2026')
    canvas.setStrokeColor(colors.HexColor('#D2D9DF'))
    canvas.setLineWidth(.5)
    canvas.line(LEFT, .95*cm, PAGE_W-RIGHT, .95*cm)
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(GRAY)
    canvas.drawString(LEFT, .63*cm, 'Material de estudo — conferir sempre a notação usada em aula')
    canvas.drawRightString(PAGE_W-RIGHT, .63*cm, f'{doc.page}')
    canvas.restoreState()


def build_story():
    S=[]
    # Cover
    S += [Spacer(1,2.2*cm), P('MICROECONOMIA II','CoverTitle'), P('Resumo completo para a Prova 1','CoverSub'), Spacer(1,.25*cm), P('Equilíbrio Geral • Caixa de Edgeworth • Lei de Walras • Monopólio • Bem-estar • Discriminação de preços','CoverSub'), Spacer(1,1.0*cm)]
    S.append(HRFlowable(width='75%', thickness=2, color=BLUE, hAlign='CENTER'))
    S += [Spacer(1,.7*cm), P('<b>Disciplina:</b> CE-362D — Microeconomia II', 'CoverSub'), P('<b>Universidade:</b> Instituto de Economia — Unicamp', 'CoverSub'), P('<b>Prova 1:</b> 23 de setembro de 2026 (data indicada no programa)', 'CoverSub'), Spacer(1,1.1*cm)]
    S.append(note('Como usar este resumo', 'Leia a intuição antes da álgebra; depois refaça os exercícios sem consultar o gabarito. Os gráficos foram reconstruídos a partir dos números dos slides de revisão, da Lista 1 e do material de excedente. Quando a fonte não fornece uma informação necessária, isso é indicado explicitamente.', LIGHT_BLUE, BLUE))
    S += [Spacer(1,.8*cm), P('<b>Base documental utilizada:</b> Revisao_EGeMONO.pdf; lista1.pdf; excedente.pdf; _Programa_Micro II_2S_2025.pdf. O programa geral também contém Teoria dos Jogos e Incerteza, mas o material específico de revisão e a Lista 1 delimitam a P1 em Equilíbrio Geral e Monopólio.', 'Smallx'), PageBreak()]

    S += [P('Sumário','H1x')]
    toc=[
        '1. Escopo provável da P1 e mapa do material',
        '2. Equilíbrio geral em uma economia de trocas',
        '3. Caixa de Edgeworth, eficiência e curva de contrato',
        '4. Álgebra do equilíbrio e Lei de Walras',
        '5. Monopólio: decisão, receita marginal e elasticidade',
        '6. Bem-estar: concorrência versus monopólio',
        '7. Discriminação de preços',
        '8. Método de resolução e pegadinhas',
        '9. Exercícios para resolver',
        '10. Gabaritos comentados',
        '11. Formulário e checklist final',
    ]
    S += [P(x,'TOC') for x in toc]
    S += [Spacer(1,.35*cm), note('Resultado mais importante para memorizar', '<b>Equilíbrio Geral:</b> os preços relativos coordenam as decisões individuais e zeram a demanda excedente. <b>Monopólio:</b> a firma escolhe Q onde RMg = CMg e depois lê P na demanda; por isso, em geral, P > CMg e Q é menor que na concorrência perfeita.', LIGHT_GREEN, GREEN), PageBreak()]

    # 1 scope
    S += [P('1. Escopo provável da P1 e mapa do material','H1x')]
    S += [P('O programa de Microeconomia II enumera quatro blocos: Equilíbrio Geral; Estruturas de Mercado e Estratégia Competitiva; Teoria dos Jogos; e Incerteza. Entretanto, a aula de revisão fornecida é explicitamente “Equilíbrio Geral e Monopólio”, e a Lista 1 cobra equilíbrio geral, monopólio, custos multiproduto e discriminação de preços. Portanto, este PDF prioriza esse recorte, sem afirmar que os demais blocos estejam fora da disciplina inteira.', 'Bodyx')]
    S.append(table([
        [P('Fonte','Smallx'),P('Conteúdo identificado','Smallx'),P('Uso neste resumo','Smallx')],
        [P('<b>Revisao_EGeMONO.pdf</b>','Smallx'),P('Leiloeiro walrasiano; equilíbrio parcial/geral; Pareto; caixa de Edgeworth; álgebra; Lei de Walras; monopólio; elasticidade; markup; bem-estar; discriminação 1º–3º graus.','Smallx'),P('Fonte principal da teoria e dos exemplos numéricos.','Smallx')],
        [P('<b>lista1.pdf</b>','Smallx'),P('Questões de troca pura, demandas Cobb–Douglas/Leontief, curva de contrato, monopólio, duas fábricas e discriminação.','Smallx'),P('Modelo de exercícios e notação da prova.','Smallx')],
        [P('<b>excedente.pdf</b>','Smallx'),P('Comparação competitiva/monopólio: P = 100 − 2Q e CMg = 10 + 3Q; EC, EP, ET e PPM.','Smallx'),P('Cálculos de bem-estar e gráfico de áreas.','Smallx')],
        [P('<b>Programa</b>','Smallx'),P('Objetivos, ementa, organização e datas.','Smallx'),P('Contextualização; não especifica isoladamente o conteúdo da P1.','Smallx')],
    ], [3.0*cm, 8.7*cm, 5.0*cm]))
    S += [Spacer(1,.25*cm), note('Atenção sobre o recorte', 'O programa geral menciona concorrência perfeita, concorrência monopolística, oligopólios e teoria dos jogos. Eles aparecem na ementa anual, mas não são desenvolvidos no material específico de revisão anexado. Por isso, não são tratados aqui como conteúdo confirmado da P1.','',)]
    # fix note bg accidental string? no, note accepts bg string invalid. We'll replace below at generation? 
    return S

# Remove accidental unfinished section by rebuilding tail below; build_story is completed by _build_rest.

def _build_rest(S):
    # 2 Equilibrio geral
    S += [P('2. Equilíbrio geral em uma economia de trocas','H1x'), P('Equilíbrio parcial estuda um mercado isoladamente, mantendo os demais constantes. Equilíbrio geral reconhece que preços e quantidades de todos os mercados são determinados simultaneamente: uma mudança em um mercado altera a renda, a demanda e os preços relativos nos outros.', 'Bodyx')]
    S += [P('2.1 Modelo básico','H2x')] + bullets(['Dois ou mais consumidores, dois ou mais bens e dotações iniciais.','Cada consumidor escolhe a cesta que maximiza sua utilidade dentro da restrição orçamentária.','A oferta total de cada bem é a soma das dotações iniciais, no modelo de trocas puras.','Um equilíbrio walrasiano é um vetor de preços e uma alocação em que cada agente otimiza e todos os mercados são factíveis/limpos.'])
    S += [P('O leiloeiro walrasiano anuncia um vetor de preços. Se a demanda excedente de um bem for positiva, o preço sobe; se for negativa, o preço cai. O processo de ajuste, ou <i>tâtonnement</i>, continua até que a demanda agregada coincida com a oferta em todos os mercados. As transações ocorrem apenas no equilíbrio.', 'Bodyx'), img('06-lei-de-walras.png', 16.6*cm), caption('Demanda excedente e ajuste de preços no exemplo numérico dos slides. O preço absoluto é normalizado; o que importa é o preço relativo.')]
    S += [P('2.2 Factibilidade, dotações e demanda líquida','H2x'), F('Factibilidade:  Σᵢ x¹ᵢ = Σᵢ w¹ᵢ  e  Σᵢ x²ᵢ = Σᵢ w²ᵢ'), F('Demanda líquida do agente i no bem k:  eᵏᵢ = xᵏᵢ − wᵏᵢ'), F('Demanda excedente agregada:  zᵏ(p) = Σᵢ eᵏᵢ(p) = Σᵢ xᵏᵢ(p) − Σᵢ wᵏᵢ')]
    S += [P('Interpretação: eᵏᵢ > 0 significa que o agente é demandante líquido do bem k; eᵏᵢ < 0 significa que ele oferece parte de sua dotação. No equilíbrio, a soma das demandas líquidas é zero para cada bem.', 'Bodyx')]

    # 3 Edgeworth
    S += [P('3. Caixa de Edgeworth, eficiência e curva de contrato','H1x'), P('A caixa de Edgeworth representa todas as alocações factíveis entre dois agentes e dois bens. A origem do agente A fica no canto inferior esquerdo; a origem do agente B fica no canto superior direito. Um ponto dentro da caixa informa simultaneamente a cesta de A e, por complementaridade, a cesta de B.', 'Bodyx')]
    S += [P('3.1 Dotação inicial e trocas mutuamente benéficas','H2x')] + bullets(['A dotação inicial é o ponto de partida, não necessariamente eficiente.','Se as TMS dos agentes forem diferentes, existe espaço para uma troca que pode melhorar ambos.','A troca termina quando as TMS se igualam, ou quando se chega a uma solução de canto/kink que já não permite melhoria conjunta.'])
    S += [P('A Taxa Marginal de Substituição (TMS) mede quanto de um bem o consumidor aceita abrir mão para obter uma unidade adicional do outro, mantendo a utilidade constante. Em uma solução interior:', 'Bodyx'), F('TMSᵢ = UMg¹ᵢ / UMg²ᵢ = p₁ / p₂')]
    S += [img('01-caixa-edgeworth.png', 16.6*cm), caption('Caixa de Edgeworth construída para a Questão 1 da Lista 1: totais (5,5), A com (4,2), B com (1,3), Uᵢ = x₁x₂. O equilíbrio é A=(3,3), B=(2,2).')]
    S += [P('3.2 Curva de contrato e Pareto','H2x'), P('A curva de contrato é o conjunto das alocações Pareto-eficientes: pontos em que não é possível aumentar a utilidade de um agente sem reduzir a do outro. Ela não significa “justiça”. Uma alocação pode ser eficiente e extremamente desigual, como um canto da caixa em que um agente possui todos os bens.', 'Bodyx'), F('Para soluções interiores:  TMS_A = TMS_B'), P('Em uma economia com produção, a condição de eficiência também relaciona as TMS dos consumidores à taxa marginal de transformação. Isso não é necessário para os exercícios de troca pura da Lista 1.', 'Bodyx')]
    S += [P('3.3 Exemplo Cobb–Douglas da Lista 1','H2x'), P('Na Questão 1, U_A = x₁ᴬx₂ᴬ e U_B = x₁ᴮx₂ᴮ, com w_A=(4,2) e w_B=(1,3). A oferta total é (5,5). Na dotação inicial, TMS_A = 2 e TMS_B = 1/3. Como são diferentes, há ganhos de troca.', 'Bodyx'), F('Para U=x₁x₂:  x₁* = ½·m/p₁  e  x₂* = ½·m/p₂'), P('Com p₁/p₂=1, as rendas são m_A=6 e m_B=4. Logo A demanda (3,3), B demanda (2,2), e os mercados fecham. No equilíbrio, TMS_A=TMS_B=1.', 'Bodyx')]
    S += [note('Leitura econômica do gráfico', 'A dotação W está dentro da lente de ganhos mútuos: ambos podem melhorar trocando. O ponto E está na curva de contrato e também no núcleo compatível com a dotação inicial. A reta orçamentária indica as cestas que têm o mesmo valor aos preços de equilíbrio.', LIGHT_GREEN, GREEN)]

    # 4 Algebra/Walras
    S += [P('4. Álgebra do equilíbrio e Lei de Walras','H1x'), P('O procedimento algébrico da prova é quase sempre o mesmo. A maior fonte de erro é usar a renda como se fosse um número fixo quando, na economia de trocas, a renda é o valor da dotação aos preços vigentes.', 'Bodyx')]
    S += [P('4.1 Roteiro mecânico','H2x')]
    S += [table([[P('Passo','Smallx'),P('O que fazer','Smallx')],[P('1','Smallx'),P('Escrever a renda de cada agente: mᵢ = p₁w¹ᵢ + p₂w²ᵢ.','Smallx')],[P('2','Smallx'),P('Resolver a escolha ótima: TMSᵢ = p₁/p₂ e substituir na restrição orçamentária.','Smallx')],[P('3','Smallx'),P('Obter as demandas xᵢ*(p) e somá-las.','Smallx')],[P('4','Smallx'),P('Impor market clearing em um mercado e normalizar um preço, por exemplo p₁=1.','Smallx')],[P('5','Smallx'),P('Usar a Lei de Walras para conferir o outro mercado.','Smallx')]], [1.2*cm,15.5*cm])]
    S += [P('4.2 Regra Cobb–Douglas','H2x'), F('U(x₁,x₂)=x₁ᵅx₂ᵝ  ⇒  x₁* = [α/(α+β)]·m/p₁;  x₂* = [β/(α+β)]·m/p₂'), P('Cada agente gasta a fração α/(α+β) da renda no bem 1 e β/(α+β) no bem 2. Essa regra é muito útil na Lista 1.', 'Bodyx')]
    S += [P('4.3 Exemplo numérico dos slides','H2x'), P('Dados: U_A=x₁ᴬ(x₂ᴬ)², w_A=(10,10); U_B=(x₁ᴮ)²x₂ᴮ, w_B=(20,20). Normalize p₁=1 e encontre p₂.', 'Bodyx'), F('A: TMS_A = x₂/(2x₁) = 1/p₂  ⇒  x₂ᴬ = 2x₁ᴬ/p₂'), F('m_A=10+10p₂  ⇒  x₁ᴬ=10(1+p₂)/3;  x₂ᴬ=20(1+p₂)/(3p₂)'), F('B: x₁ᴮ=40(1+p₂)/3;  x₂ᴮ=20(1+p₂)/(3p₂)'), F('Mercado 1: 10(1+p₂)/3 + 40(1+p₂)/3 = 30  ⇒  p₂ = 0,8'), P('Com p₂=0,8: A consome (6,15), B consome (24,15). A é ofertante líquido do bem 1 e demandante líquida do bem 2; B faz o oposto. A soma das demandas é (30,30), igual à soma das dotações.', 'Bodyx'), img('06-lei-de-walras.png', 16.6*cm), caption('No ponto p₂*=0,8, as duas demandas excedentes se anulam no exemplo dos slides.')]
    S += [P('4.4 Lei de Walras','H2x'), F('Σₖ pₖ zₖ(p) = 0  para todo vetor de preços p'), P('Se existem dois mercados e um está em equilíbrio, a Lei de Walras garante que o outro também está, desde que as restrições orçamentárias sejam respeitadas. Por isso, em dois bens, basta limpar um mercado. O preço absoluto não é determinado: multiplicar todos os preços pelo mesmo número não altera escolhas. Normaliza-se um preço como numerário.', 'Bodyx')]
    S += [note('Não confunda', '<b>Lei de Walras</b> não diz que cada mercado está em equilíbrio para qualquer preço. Ela diz que o valor do excesso de demanda agregado é zero para qualquer preço; se n−1 mercados estão limpos, o último também estará.', LIGHT_RED, RED)]

    # 5 monopoly
    S += [P('5. Monopólio: decisão, receita marginal e elasticidade','H1x'), P('O monopolista é price maker: enfrenta a demanda de mercado e escolhe a quantidade que maximiza π(Q)=RT(Q)−CT(Q). Ele não escolhe simultaneamente preço e quantidade de forma independente; a demanda liga os dois.', 'Bodyx')]
    S += [P('5.1 Receita marginal','H2x'), F('RT(Q)=P(Q)·Q'), F('RMg(Q)=dRT/dQ=P(Q)+P′(Q)·Q'), P('O segundo termo é o efeito-preço: para vender mais, a firma reduz o preço de todas as unidades. É por isso que RMg fica abaixo da demanda quando a demanda é descendente.', 'Bodyx'), img('02-demanda-rmg.png', 16.6*cm), caption('Para demanda linear P=a−bQ, RMg=a−2bQ: mesmo intercepto vertical e inclinação duas vezes maior.')]
    S += [P('5.2 Condição de ótimo e curva de oferta','H2x'), F('Condição de primeira ordem:  RMg(Qₘ)=CMg(Qₘ)'), F('Preço:  Pₘ=P(Qₘ)  (leia na curva de demanda, não na RMg)'), F('Lucro:  πₘ=[Pₘ−CMe(Qₘ)]·Qₘ'), P('A curva de oferta da concorrência perfeita é derivada do CMg acima do mínimo do CMe. Um monopolista não possui uma curva de oferta independente: a quantidade ótima depende da demanda e do custo.', 'Bodyx'), img('03-monopolio-equilibrio.png', 16.6*cm), caption('Exemplo dos slides: P=100−y, C=y²/2+10. O monopólio produz yₘ=100/3 e cobra pₘ=200/3; a referência competitiva é y_c=50, p_c=50.')]
    S += [P('5.3 Elasticidade e markup','H2x'), F('RMg=P·(1+1/ε)=P·(1−1/|ε|),  com ε<0'), F('RMg=CMg  ⇒  P/CMg = 1/[1−1/|ε|]'), P('O markup aumenta quando a demanda fica menos elástica. O monopolista sempre opera na região elástica: se |ε|<1, RMg<0; reduzir Q aumenta a receita e reduz o custo.', 'Bodyx')]
    S += [P('Exemplo linear rápido','H2x'), F('P=100−Q;  C(Q)=Q²/2+10  ⇒  RMg=100−2Q; CMg=Q'), F('100−2Q=Q  ⇒  Qₘ=100/3≈33,33;  Pₘ=100−100/3=200/3≈66,67'), P('A margem é P−CMg=200/3−100/3=100/3. O lucro é positivo porque o preço está acima do custo médio no Q escolhido.', 'Bodyx')]

    # 6 welfare
    S += [P('6. Bem-estar: concorrência versus monopólio','H1x'), P('O material de excedente usa P=100−2Q e CMg=10+3Q. Na concorrência, a disposição a pagar da última unidade se iguala ao custo marginal. No monopólio, a firma restringe Q porque considera o efeito da redução de preço sobre todas as unidades.', 'Bodyx')]
    S += [P('6.1 Cálculo completo do exemplo','H2x'), F('Concorrência: 100−2Q=10+3Q  ⇒  Q_c=18, P_c=64'), F('Monopólio: RMg=100−4Q;  100−4Q=10+3Q  ⇒  Q_m=90/7≈12,86; P_m=520/7≈74,29'), S[-1] if False else Spacer(1,0)]
    # Remove weird placeholder effect harmless; add rest
    S += [table([[P('Indicador','Smallx'),P('Concorrência','Smallx'),P('Monopólio','Smallx'),P('Efeito','Smallx')],[P('Quantidade','Smallx'),P('18','Smallx'),P('12,86','Smallx'),P('reduz','Smallx')],[P('Preço','Smallx'),P('64','Smallx'),P('74,29','Smallx'),P('aumenta','Smallx')],[P('EC','Smallx'),P('324','Smallx'),P('165,31','Smallx'),P('cai','Smallx')],[P('EP','Smallx'),P('486','Smallx'),P('578,57','Smallx'),P('aumenta','Smallx')],[P('ET','Smallx'),P('810','Smallx'),P('743,88','Smallx'),P('cai','Smallx')],[P('PPM','Smallx'),P('0','Smallx'),P('66,12','Smallx'),P('perda líquida','Smallx')]], [4.0*cm,3.0*cm,3.0*cm,6.7*cm]), img('04-onus-monopolio.png', 16.6*cm), caption('Áreas de EC, EP, transferência de excedente e perda de peso morto no exemplo do material.'), P('A redução do EC não é toda uma perda social: parte é transferência para o produtor (área retangular). A perda de peso morto é o triângulo associado às unidades entre Qₘ e Q_c que deixaram de ser produzidas mesmo tendo benefício social maior que o custo.', 'Bodyx')]
    S += [P('6.2 Excedentes com curvas lineares','H2x'), F('EC = ½·Q·(preço máximo−preço de mercado)'), F('EP competitivo = ½·Q·(preço de mercado−CMg em Q=0)'), F('PPM = ET competitivo − ET monopólio'), P('Em monopólio, o EP pode ser calculado como retângulo de margem mais a área entre a curva de CMg e a linha de preço. Não use automaticamente a fórmula triangular do EP competitivo se o custo marginal for crescente.', 'Bodyx')]

    # 7 discrimination
    S += [P('7. Discriminação de preços','H1x'), P('Discriminar é cobrar preços diferentes por unidades ou consumidores com base na disposição a pagar, impedindo que a arbitragem/revenda elimine a diferença.', 'Bodyx')]
    S += [table([[P('Grau','Smallx'),P('Como funciona','Smallx'),P('Resultado típico','Smallx')],[P('1º','Smallx'),P('Preço personalizado, igual à disposição a pagar de cada consumidor.','Smallx'),P('Captura todo o EC; produz até P=CMg; PPM=0.','Smallx')],[P('2º','Smallx'),P('Menu de quantidades, pacotes ou versões. O consumidor se auto-seleciona.','Smallx'),P('Extrai excedente sem observar diretamente o tipo.','Smallx')],[P('3º','Smallx'),P('Preços diferentes em grupos/mercados observáveis.','Smallx'),P('RMg₁=RMg₂=CMg; preço maior no mercado menos elástico.','Smallx')]], [1.5*cm,8.5*cm,7.0*cm]), img('05-discriminacao-precos.png', 16.8*cm), caption('Os três graus de discriminação, incluindo o exemplo da Lista 1 com ε₁=−2 e ε₂=−4.')]
    S += [P('7.1 Terceiro grau: condição central','H2x'), F('RMg₁=RMg₂=CMg'), F('P₁(1−1/|ε₁|)=P₂(1−1/|ε₂|)=CMg'), P('Como |ε₁|=2 e |ε₂|=4:', 'Bodyx'), F('RMg₁=0,5P₁;  RMg₂=0,75P₂  ⇒  0,5P₁=0,75P₂  ⇒  P₁/P₂=1,5'), P('Se a firma cobra P₁=2,5P₂, não está maximizando: RMg₁=1,25P₂, enquanto RMg₂=0,75P₂. A receita marginal do mercado 1 é maior; a firma deve deslocar vendas para o mercado 1, reduzindo P₁ e/ou aumentando P₂, até igualar as receitas marginais.', 'Bodyx')]
    S += [P('7.2 Segundo grau: exemplo dos slides','H2x'), P('Tipo A aceita 30, 20 e 10 pelas três primeiras unidades; Tipo B aceita 20 e 10 pelas duas primeiras. O menu dos slides ilustra pacote de 2 unidades por R$30 e pacote de 3 por R$60. Os pacotes permitem auto-seleção: B escolhe o menor pacote; A escolhe o maior.', 'Bodyx')]
    S += [note('Condições para discriminar', 'A firma precisa conseguir identificar ou induzir tipos diferentes, limitar a revenda e ter poder de mercado. Sem essas condições, consumidores que compram barato podem revender para os que pagariam caro.', LIGHT_BLUE, BLUE)]

    # 8 method traps
    S += [P('8. Método de resolução e pegadinhas','H1x'), P('8.1 Checklist algébrico de equilíbrio geral','H2x')]
    S += bullets(['Liste dotações e some os totais de cada bem.','Calcule a renda pelo valor da dotação, não apenas pela quantidade consumida.','Derive a demanda individual antes de somar agentes.','Normalize um preço: p₁=1 ou p₂=1.','Limpe um mercado e confira o segundo pela factibilidade/Lei de Walras.','Verifique se as cestas finais somam as dotações totais.'])
    S += [P('8.2 Checklist algébrico de monopólio','H2x')]
    S += bullets(['Converta a demanda para a forma inversa P(Q), se necessário.','Calcule RT=P(Q)Q e depois RMg=dRT/dQ.','Calcule CMg=dC/dQ.','Resolva RMg=CMg para Qₘ.','Substitua Qₘ na demanda para obter Pₘ.','Compare Pₘ com CMe para obter lucro; compare Qₘ e Q_c para bem-estar.'])
    S += [P('Pegadinhas frequentes','H2x'), table([[P('Erro','Smallx'),P('Correção','Smallx')],[P('Usar P=CMg no monopólio.','Smallx'),P('P=CMg é a condição competitiva; monopólio usa RMg=CMg e depois lê P na demanda.','Smallx')],[P('Confundir RMg com demanda.','Smallx'),P('Para demanda descendente, RMg fica abaixo de P porque vender mais reduz o preço das unidades anteriores.','Smallx')],[P('Achar que Pareto eficiente é justo.','Smallx'),P('Pareto é eficiência; justiça/equidade é outro critério.','Smallx')],[P('Resolver todos os mercados sem normalizar preço.','Smallx'),P('Só preços relativos importam; fixe um numerário.','Smallx')],[P('Dizer que PPM é toda a perda do EC.','Smallx'),P('Parte da perda do EC é transferência para EP; PPM é a perda líquida de ET.','Smallx')],[P('No 3º grau, cobrar mais no mercado mais elástico.','Smallx'),P('A regra é o contrário: preço maior onde a demanda é menos elástica.','Smallx')]], [5.2*cm,13.0*cm])]

    # exercises
    S += [PageBreak(), P('9. Exercícios para resolver','H1x'), P('Tente resolver todos antes de abrir a seção 10. Os quatro primeiros reproduzem ou adaptam diretamente questões da Lista 1; os demais consolidam os exemplos dos slides e do material de excedente.', 'Bodyx')]
    exs=[
        ('Exercício 1 — Lista 1, Q1 (troca pura)', 'Dois agentes A e B têm Uᵢ(x₁,x₂)=x₁x₂. As dotações são w_A=(4,2) e w_B=(1,3). (a) Verifique se há incentivo à troca na dotação inicial. (b) Encontre as demandas Marshallianas. (c) Determine p₁/p₂ e as cestas de equilíbrio. (d) Calcule as demandas líquidas e interprete a eficiência de Pareto.'),
        ('Exercício 2 — Lista 1, Q2 (Cobb–Douglas)', 'U=x⁴y⁶ para o agente 1 e V=x⁶y⁴ para o agente 2. As dotações são (4,2) e (2,4). Julgue: (a) o agente 1 gasta 40% da renda em x; (b) p_x/p_y=2; (c) o agente 1 consome 2,4 unidades de x; (d) a TMS do agente 1 no equilíbrio é 1.'),
        ('Exercício 3 — Lista 1, Q3 (curva de contrato)', 'UA=x₁ᴬ^(1/3)x₂ᴬ^(2/3), UB=min{x₁ᴮ,x₂ᴮ}, w_A=(10,20), w_B=(20,5). (a) Obtenha a curva de contrato. (b) Avalie se (x_A=(10,5), x_B=(20,20)) é Pareto-eficiente. (c) Com p₁=p₂=1, calcule o excesso de demanda agregado.'),
        ('Exercício 4 — Lista 1, Q4 (monopólio)', 'A demanda é P=18−Q e o custo total é CT(Q)=27+2Q². Encontre RMg, CMg, quantidade e preço de monopólio. Calcule o lucro.'),
        ('Exercício 5 — exemplo dos slides (equilíbrio geral)', 'UA=x₁ᴬ(x₂ᴬ)², UB=(x₁ᴮ)²x₂ᴮ, w_A=(10,10), w_B=(20,20). Normalize p₁=1. Encontre p₂, as cestas de equilíbrio e as demandas líquidas.'),
        ('Exercício 6 — Lista 1, Q6 (3º grau)', 'Um monopolista vende em dois mercados com ε₁=−2 e ε₂=−4. Mostre se a relação P₁=2,5P₂ maximiza o lucro. Encontre a relação correta entre os preços.'),
        ('Exercício 7 — excedente e PPM', 'Com P=100−2Q e CMg=10+3Q, calcule os equilíbrios competitivo e monopolista, EC, EP, ET e a perda de peso morto.'),
        ('Exercício 8 — comparação conceitual', 'Explique por que o monopolista nunca escolhe uma quantidade na região inelástica da demanda e por que a discriminação perfeita elimina a PPM, embora possa ser distributivamente controversa.'),
    ]
    for title, text in exs:
        S += [P(title,'H2x'), note('Para resolver', text, colors.white, colors.HexColor('#AAB7C4')), Spacer(1,.08*cm)]

    # gabaritos
    S += [P('10. Gabaritos comentados','H1x'), P('As soluções abaixo mostram o caminho algébrico e a interpretação econômica. Valores aproximados usam vírgula decimal.', 'Bodyx')]
    S += [P('Gabarito 1 — troca pura','H2x'), P('(a) Na dotação, TMS_A = x₂/x₁ = 2/4 = 0,5 e TMS_B = x₂ᴮ/x₁ᴮ = 3/1 = 3. Como são diferentes, há trocas mutuamente benéficas. (b) Para U=x₁x₂, a condição TMS=p₁/p₂ e a restrição dão:', 'Answer'), F('x₁ᵢ* = mᵢ/(2p₁);  x₂ᵢ* = mᵢ/(2p₂)'), P('(c) Normalize p₁=p₂=1. Então m_A=4+2=6 e m_B=1+3=4. Logo A=(3,3) e B=(2,2). A soma é (5,5), exatamente a dotação total; portanto p₁/p₂=1. (d) A demanda líquida de A é (3−4,3−2)=(−1,+1); a de B é (2−1,2−3)=(+1,−1). A troca é uma realocação sem desperdício e o equilíbrio está na curva de contrato, portanto é Pareto-eficiente.', 'Answer'), note('Resposta final', '<b>Há incentivo à troca; p₁/p₂=1; A=(3,3); B=(2,2).</b> A vende 1 unidade do bem 1 e compra 1 unidade do bem 2; B faz o oposto.', LIGHT_GREEN, GREEN)]
    S += [P('Gabarito 2 — Cobb–Douglas','H2x'), P('Para U=x⁴y⁶, as frações de gasto são 4/10=40% em x e 6/10=60% em y. Para V=x⁶y⁴, são 60% e 40%. Portanto (a) é verdadeira.', 'Answer'), F('Fixe p_y=1 e r=p_x/p_y=p_x.  m₁=4r+2;  m₂=2r+4'), F('Demanda total de x = 0,4(4r+2)/r + 0,6(2r+4)/r = 2,8 + 3,2/r'), P('A oferta total de x é 6. Igualando: 2,8+3,2/r=6, então 3,2/r=3,2 e <b>r=1</b>. Logo (b) é falsa. A demanda de x do agente 1 é 0,4·6/1=<b>2,4</b>, então (c) é verdadeira. Sua demanda de y é 0,6·6=3,6; TMS=MU_x/MU_y=(4y)/(6x)=2y/(3x)=2·3,6/(3·2,4)=<b>1</b>. (d) é verdadeira.', 'Answer'), note('Resposta final', '<b>Verdadeiras: (a), (c), (d). Falsa: (b).</b> O preço relativo correto é p_x/p_y=1.', LIGHT_GREEN, GREEN)]
    S += [P('Gabarito 3 — curva de contrato','H2x'), P('(a) Para B, UB=min{x₁ᴮ,x₂ᴮ}; suas alocações eficientes têm x₁ᴮ=x₂ᴮ. Pela factibilidade:', 'Answer'), F('x₁ᴬ+x₁ᴮ=30;  x₂ᴬ+x₂ᴮ=25;  x₁ᴮ=x₂ᴮ'), F('x₂ᴬ = 25−x₂ᴮ = 25−x₁ᴮ = 25−(30−x₁ᴬ) = x₁ᴬ−5'), P('Logo a curva de contrato é x₂ᴬ=x₁ᴬ−5, respeitando os limites da caixa. (b) A alocação A=(10,5), B=(20,20) satisfaz x₁ᴮ=x₂ᴮ e está na curva de contrato; é Pareto-eficiente. (c) Com p₁=p₂=1: m_A=30. A demanda Cobb–Douglas é (10,20). B tem m_B=25 e, pela preferência Leontief, demanda (12,5;12,5). A demanda agregada é (22,5;32,5). Menos a oferta total (30,25), o excesso é <b>(−7,5,+7,5)</b>.', 'Answer'), note('Resposta final', '<b>Curva de contrato: x₂ᴬ=x₁ᴬ−5; excesso de demanda: (−7,5; +7,5).</b> O primeiro bem tem excesso de oferta e o segundo, excesso de demanda.', LIGHT_GREEN, GREEN)]
    S += [P('Gabarito 4 — monopólio com custo quadrático','H2x'), F('P=18−Q  ⇒  RT=(18−Q)Q=18Q−Q²  ⇒  RMg=18−2Q'), F('CT=27+2Q²  ⇒  CMg=4Q'), F('RMg=CMg  ⇒  18−2Q=4Q  ⇒  Qₘ=3'), F('Pₘ=18−3=<b>15</b>'), F('π=RT−CT = 15·3 − [27+2(3²)] = 45−45 = <b>0</b>'), P('O custo fixo de 27 é exatamente coberto no ponto ótimo. A firma produz três unidades e cobra quinze; produzir zero daria prejuízo de 27.', 'Answer')]
    S += [P('Gabarito 5 — exemplo dos slides','H2x'), P('As demandas dos slides são:', 'Answer'), F('x₁ᴬ=10(1+p₂)/3;  x₂ᴬ=20(1+p₂)/(3p₂)'), F('x₁ᴮ=40(1+p₂)/3;  x₂ᴮ=20(1+p₂)/(3p₂)'), P('No mercado 1, a demanda total deve ser 30:', 'Answer'), F('50(1+p₂)/3=30  ⇒  1+p₂=1,8  ⇒  <b>p₂=0,8</b>'), P('Substituindo: A=(6,15), B=(24,15). As demandas líquidas são A=(−4,+5) e B=(+4,−5). A soma é (30,30), igual à oferta total; a Lei de Walras confirma o segundo mercado.', 'Answer')]
    S += [P('Gabarito 6 — discriminação de 3º grau','H2x'), F('RMg₁=P₁(1−1/2)=0,5P₁;  RMg₂=P₂(1−1/4)=0,75P₂'), P('O ótimo exige 0,5P₁=0,75P₂, então:', 'Answer'), F('<b>P₁/P₂=0,75/0,5=1,5</b>'), P('Se P₁=2,5P₂, então RMg₁=1,25P₂ e RMg₂=0,75P₂. Como RMg₁>RMg₂, uma unidade adicional no mercado 1 gera mais receita; a alocação atual não é ótima. O mercado 1 é menos elástico e deve ter o preço maior, mas na proporção 1,5, não 2,5.', 'Answer')]
    S += [P('Gabarito 7 — excedente e PPM','H2x'), F('Competição: 100−2Q=10+3Q  ⇒  <b>Q_c=18, P_c=64</b>'), F('Monopólio: RMg=100−4Q; 100−4Q=10+3Q  ⇒  <b>Q_m=90/7≈12,86; P_m=520/7≈74,29</b>'), F('EC_c=½·18·(100−64)=<b>324</b>; EP_c=½·18·(64−10)=<b>486</b>; ET_c=<b>810</b>'), F('EC_m≈<b>165,31</b>; EP_m≈<b>578,57</b>; ET_m≈<b>743,88</b>'), F('PPM=810−743,88=<b>66,12</b>'), P('O monopólio reduz a quantidade e aumenta o preço. O produtor ganha excedente, mas o ganho não compensa a queda do consumidor: a diferença é a perda líquida de bem-estar.', 'Answer')]
    S += [P('Gabarito 8 — comparação conceitual','H2x'), P('O monopolista não opera na região inelástica porque, nessa região, |ε|<1 e RMg=P(1−1/|ε|)<0. Reduzir a quantidade aumenta a receita total e reduz o custo, portanto uma escolha nessa região não pode ser ótima.', 'Answer'), P('Na discriminação perfeita, cada unidade é vendida ao preço máximo que aquele consumidor aceita pagar. A firma continua expandindo a produção enquanto a disposição a pagar for pelo menos o CMg; assim, a quantidade coincide com a eficiente e a PPM desaparece. Isso não significa igualdade distributiva: o EC é capturado pela firma.', 'Answer')]

    # formula/checklist
    S += [PageBreak(), P('11. Formulário e checklist final','H1x'), P('11.1 Formulário de uma página','H2x'), F('Renda:  mᵢ=p₁w¹ᵢ+p₂w²ᵢ'), F('TMS:  UMg₁/UMg₂=p₁/p₂'), F('Cobb–Douglas: U=x₁ᵅx₂ᵝ  ⇒  x₁=α/(α+β)·m/p₁;  x₂=β/(α+β)·m/p₂'), F('Factibilidade: Σxᵢᵏ=Σwᵢᵏ;  excesso: zᵏ=Σxᵢᵏ−Σwᵢᵏ'), F('Pareto interior: TMS_A=TMS_B'), F('Lei de Walras: Σₖ pₖzₖ(p)=0; se n−1 mercados fecham, o n-ésimo fecha'), F('Monopólio: RT=P(Q)Q; RMg=P+P′Q; RMg=CMg; P=P(Qₘ)'), F('Elasticidade: RMg=P(1−1/|ε|); markup P/CMg=1/[1−1/|ε|]'), F('Concorrência: P=CMg; monopólio: P>CMg em geral'), F('Discriminação 3º grau: RMg₁=RMg₂=CMg; preço maior onde |ε| é menor'), F('Excedentes lineares: EC=½·base·altura; PPM=ET_c−ET_m'), P('11.2 Checklist “eu sei fazer?”','H2x')]
    checklist=['Desenhar e interpretar uma caixa de Edgeworth, identificando as duas origens.','Calcular a TMS e explicar por que TMS diferentes geram ganhos de troca.','Derivar a curva de contrato em uma economia com Leontief e Cobb–Douglas.','Escrever a renda de cada consumidor como valor da dotação.','Obter demandas Cobb–Douglas e fechar um mercado.','Usar a Lei de Walras e explicar o que é preço relativo/numerário.','Calcular RT, RMg, CMg, Qₘ, Pₘ e lucro.','Explicar por que o monopolista opera na região elástica.','Calcular EC, EP, ET e PPM em um gráfico linear.','Distinguir transferência de excedente de perda de peso morto.','Aplicar RMg₁=RMg₂ no terceiro grau de discriminação.','Explicar os graus 1, 2 e 3 e as condições de arbitragem.']
    S += [P('Marque cada item após resolvê-lo sem consultar o texto:', 'Bodyx')]
    for x in checklist: S.append(P('□ '+x,'Bodyx'))
    S += [note('Prioridade para a véspera', '<b>1º:</b> refaça os Exercícios 1, 3, 4, 6 e 7. <b>2º:</b> memorize o roteiro RMg=CMg e a regra de terceiro grau. <b>3º:</b> desenhe de memória a caixa de Edgeworth e o gráfico de PPM. <b>4º:</b> confira os sinais das demandas líquidas e os preços relativos.', LIGHT_GREEN, GREEN),
      Spacer(1,.35*cm),
      note('Continuação deste material',
           'A <b>Lista 1 completa e resolvida</b> (as seis questões, item por item, incluindo a Questão 5 '
           'das duas fábricas) e um <b>banco de 23 exercícios novos</b> com gabaritos estão no arquivo '
           '<b>lista1-resolvida-e-exercicios-extra.pdf</b>, na mesma pasta.', LIGHT_BLUE, BLUE),
      Spacer(1,.35*cm),
      P('<b>Nota de transparência:</b> este resumo foi produzido com base nos arquivos da disciplina disponíveis no diretório prints do repositório. As equações de custo da Questão 5 da Lista 1 estavam embutidas como imagem no PDF original e foram recuperadas por renderização: C₁(Q₁)=10Q₁² e C₂(Q₂)=20Q₂². Todos os resultados numéricos são recalculados por verificar_contas.py (114 checagens simbólicas). A teoria está coberta, mas a notação específica usada em aula deve prevalecer.', 'Smallx')]
    return S

# Fix the one note call with invalid background in build_story by constructing only before it and overriding.
def make_story():
    # We cannot use the accidental call in build_story; it is corrected in source by editing it at runtime logically.
    S=[]
    # execute build_story after monkey-free correction: build_story's last note has bg='' and would fail in TableStyle.
    # Replicate by temporarily not relying on its last element: correct function text before invocation is handled below through local wrapper.
    return _build_rest(S)

# Build a clean story by using the same content function but with a corrected minimal preamble inserted explicitly.
def full_story():
    S=[]
    S += [Spacer(1,2.2*cm), P('MICROECONOMIA II','CoverTitle'), P('Resumo completo para a Prova 1','CoverSub'), Spacer(1,.25*cm), P('Equilíbrio Geral • Caixa de Edgeworth • Lei de Walras • Monopólio • Bem-estar • Discriminação de preços','CoverSub'), Spacer(1,1.0*cm)]
    S.append(HRFlowable(width='75%', thickness=2, color=BLUE, hAlign='CENTER'))
    S += [Spacer(1,.7*cm), P('<b>Disciplina:</b> CE-362D — Microeconomia II', 'CoverSub'), P('<b>Universidade:</b> Instituto de Economia — Unicamp', 'CoverSub'), P('<b>Prova 1:</b> 23 de setembro de 2026 (data indicada no programa)', 'CoverSub'), Spacer(1,1.1*cm)]
    S.append(note('Como usar este resumo', 'Leia a intuição antes da álgebra; depois refaça os exercícios sem consultar o gabarito. Os gráficos foram reconstruídos a partir dos números dos slides de revisão, da Lista 1 e do material de excedente. Quando a fonte não fornece uma informação necessária, isso é indicado explicitamente.', LIGHT_BLUE, BLUE))
    S += [Spacer(1,.8*cm), P('<b>Base documental utilizada:</b> Revisao_EGeMONO.pdf; lista1.pdf; excedente.pdf; _Programa_Micro II_2S_2025.pdf. O programa geral também contém Teoria dos Jogos e Incerteza, mas o material específico de revisão e a Lista 1 delimitam a P1 em Equilíbrio Geral e Monopólio.', 'Smallx'), PageBreak(), P('Sumário','H1x')]
    toc=['1. Escopo provável da P1 e mapa do material','2. Equilíbrio geral em uma economia de trocas','3. Caixa de Edgeworth, eficiência e curva de contrato','4. Álgebra do equilíbrio e Lei de Walras','5. Monopólio: decisão, receita marginal e elasticidade','6. Bem-estar: concorrência versus monopólio','7. Discriminação de preços','8. Método de resolução e pegadinhas','9. Exercícios para resolver','10. Gabaritos comentados','11. Formulário e checklist final']
    S += [P(x,'TOC') for x in toc] + [Spacer(1,.35*cm), note('Resultado mais importante para memorizar', '<b>Equilíbrio Geral:</b> os preços relativos coordenam as decisões individuais e zeram a demanda excedente. <b>Monopólio:</b> a firma escolhe Q onde RMg = CMg e depois lê P na demanda; por isso, em geral, P > CMg e Q é menor que na concorrência perfeita.', LIGHT_GREEN, GREEN), PageBreak()]
    S += [P('1. Escopo provável da P1 e mapa do material','H1x'), P('O programa de Microeconomia II enumera quatro blocos: Equilíbrio Geral; Estruturas de Mercado e Estratégia Competitiva; Teoria dos Jogos; e Incerteza. Entretanto, a aula de revisão fornecida é explicitamente “Equilíbrio Geral e Monopólio”, e a Lista 1 cobra equilíbrio geral, monopólio, custos multiproduto e discriminação de preços. Portanto, este PDF prioriza esse recorte, sem afirmar que os demais blocos estejam fora da disciplina inteira.', 'Bodyx')]
    S.append(table([[P('Fonte','Smallx'),P('Conteúdo identificado','Smallx'),P('Uso neste resumo','Smallx')],[P('<b>Revisao_EGeMONO.pdf</b>','Smallx'),P('Leiloeiro walrasiano; equilíbrio parcial/geral; Pareto; caixa de Edgeworth; álgebra; Lei de Walras; monopólio; elasticidade; markup; bem-estar; discriminação 1º–3º graus.','Smallx'),P('Fonte principal da teoria e dos exemplos numéricos.','Smallx')],[P('<b>lista1.pdf</b>','Smallx'),P('Questões de troca pura, demandas Cobb–Douglas/Leontief, curva de contrato, monopólio, duas fábricas e discriminação.','Smallx'),P('Modelo de exercícios e notação da prova.','Smallx')],[P('<b>excedente.pdf</b>','Smallx'),P('Comparação competitiva/monopólio: P = 100 − 2Q e CMg = 10 + 3Q; EC, EP, ET e PPM.','Smallx'),P('Cálculos de bem-estar e gráfico de áreas.','Smallx')],[P('<b>Programa</b>','Smallx'),P('Objetivos, ementa, organização e datas.','Smallx'),P('Contextualização; não especifica isoladamente o conteúdo da P1.','Smallx')]], [3.0*cm, 8.7*cm, 5.0*cm]))
    S += [Spacer(1,.25*cm), note('Atenção sobre o recorte', 'O programa geral menciona concorrência perfeita, concorrência monopolística, oligopólios e teoria dos jogos. Eles aparecem na ementa anual, mas não são desenvolvidos no material específico de revisão anexado. Por isso, não são tratados aqui como conteúdo confirmado da P1.', LIGHT_BLUE, BLUE), PageBreak()]
    return _build_rest(S)

if __name__ == '__main__':
    doc=BaseDocTemplate(OUT, pagesize=A4, leftMargin=LEFT, rightMargin=RIGHT, topMargin=TOP, bottomMargin=BOTTOM, title='Resumo Microeconomia II — Prova 1', author='Kiro')
    frame=Frame(LEFT, BOTTOM, PAGE_W-LEFT-RIGHT, PAGE_H-TOP-BOTTOM, id='normal')
    doc.addPageTemplates([PageTemplate(id='main', frames=[frame], onPage=header_footer)])
    doc.build(full_story())
    print(OUT)
    print(os.path.getsize(OUT))
