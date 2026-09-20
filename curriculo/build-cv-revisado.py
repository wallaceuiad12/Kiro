# -*- coding: utf-8 -*-
"""Gera o CV revisado de Matteo Lucato replicando o layout do PDF original.

Regras de conteudo:
  - Sem travessao (em dash U+2014) em qualquer texto corrido.
  - Datas usam en dash (U+2013), que e a convencao tipografica correta.
  - Nenhum fato novo: o texto so reformula/expande o que ja existia no original.
"""
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

W, H = 595.92, 842.40
LEFT, RIGHT = 28.3, 566.0
RULE0, RULE1 = 26.9, 568.6
BULLET_X, TEXT_X = 48.0, 62.5
F, FB, FI = "Times-Roman", "Times-Bold", "Times-Italic"
SZ_NAME, SZ_CONTACT, SZ_SEC, SZ_BODY = 13.0, 10.6, 10.6, 10.1
BOTTOM_LIMIT = 823.0          # pagina cheia, ~20pt de margem inferior

NAME = "MATTEO LUCATO"
CONTACT = "São Paulo, SP  |  (11) 94591-1942  |  m246226@dac.unicamp.br  |  linkedin.com/in/matteo-lucato"

DATA = [
 ("FORMAÇÃO ACADÊMICA", [
   ("UNICAMP", "Campinas, SP",
    "Bacharelado em Economia (Instituto de Economia)", "Fevereiro 2023 – Dezembro 2027", [
     "**Disciplinas relevantes:** Finanças Corporativas, Contabilidade e Análise de Balanços, Econometria, Estatística, Derivativos e Gestão de Portfólio, Matemática Financeira, Mercado de Capitais e Métodos Computacionais.",
    ]),
   ("Agostiniano Mendel / Calvert Academy", "São Paulo, SP",
    "Ensino Médio com currículo internacional norte-americano (AP Economics e AP Statistics), com ênfase em Economia, Tecnologia, Finanças e Matemática", "", []),
 ]),
 ("EXPERIÊNCIA PROFISSIONAL", [
   ("V4 Company", "Campinas, SP", "Analista Financeiro Júnior", "Janeiro 2026 – Setembro 2026", [
     "Conduzi as análises mensais de DRE, a modelagem financeira e as projeções de fluxo de caixa da empresa, acompanhando receitas, custos e margens de cada período e consolidando os resultados em relatórios gerenciais que a diretoria utilizava como base para decidir a alocação de um orçamento anual superior a R$ 5M.",
     "Administrei o fluxo de caixa, a conciliação bancária e as rotinas de contas a pagar e a receber, com volume superior a 400 transações mensais, e implantei um controle diário de vencimentos que antecipou a cobrança dos recebíveis e reduziu a inadimplência da carteira.",
     "Reestruturei as rotinas de fechamento mensal e a documentação dos controles internos, reduzindo a exposição a riscos operacionais e deixando cada lançamento rastreável até o comprovante de origem, formando a base documental que sustentou as auditorias e os processos de Due Diligence da empresa.",
   ]),
   ("Nunes&Lucato", "São Paulo, SP", "Gestor de Projetos", "Fevereiro 2023 – Dezembro 2025", [
     "Conduzi a prospecção e a negociação das parcerias de coleta com a NK Store e a Track&Field, garantindo a destinação integral do resíduo têxtil recebido e assegurando fluxo contínuo de matéria-prima ao longo de 2023 e 2024, período em que a receita e o volume do negócio cresceram de forma sustentada.",
     "Gerenciei projetos de upcycling para a Midea, a Carrier e a Santista S.A., administrando um orçamento de R$ 150 mil, coordenando a produção e a entrega de mais de 2.500 itens às marcas como parte de suas iniciativas de sustentabilidade.",
     "Supervisionei o projeto Bom Retiro Recicla, acompanhando o volume de resíduo têxtil recebido e realocando mais de 40 toneladas por mês para a reciclagem, o que evitou que esse material fosse encaminhado a descarte inadequado.",
   ]),
 ]),
 ("ATIVIDADES EXTRACURRICULARES E LIDERANÇA", [
   ("Clube de Consultoria da Unicamp", "Campinas, SP", "Diretor de Gestão de Pessoas", "Agosto 2025 – Setembro 2026", [
     "Atuei como instrutor do programa Prep4Consulting, ministrando aulas de Finanças e de resolução de cases para mais de 100 alunos e capacitando os participantes na estruturação e na resolução dos problemas exigidos nos processos seletivos de consultoria.",
     "Conduzi as sessões de preparação do programa Getting the Job, rodando simulações de entrevista com devolutiva de desempenho e revisões estratégicas de currículo com os candidatos que disputavam vagas nas principais consultorias do mercado.",
     "Colaborei na divulgação do XRAY 2025, censo da Unicamp voltado a mapear o interesse dos alunos pelo mercado de consultoria, levantamento que alcançou o recorde de 626 respostas em apenas duas semanas.",
   ]),
   ("IME Jr", "São Paulo, SP", "Analista Financeiro, Departamento Jurídico-Financeiro", "Agosto 2024 – Dezembro 2025", [
     "Estruturei modelos preditivos em Python e rotinas de extração de dados em SQL para projetos nos setores de Saúde e Transporte, tratando e analisando bases com mais de 1,2 milhão de registros.",
     "Conduzi a análise SWOT da empresa júnior, identificando a captação de recursos como principal ponto forte, e analisei as despesas operacionais em Excel para apontar as linhas de custo com maior potencial de redução, o que gerou economia mensal recorrente.",
     "Padronizei o arquivo financeiro e jurídico do departamento, reunindo fluxo de caixa, orçamentos, contratos e notas fiscais em uma estrutura única de pastas, com convenção de nomes que tornou cada documento localizável por período e por contraparte.",
   ]),
 ]),
]

SKILLS = [
 "**Certificações:** CPA-20 (ANBIMA), candidato ao Nível I do CFA, Financial & Valuation Modeling (WSP), Excel Avançado (Fundação Bradesco), Derivativos e Gestão de Portfólio (GMF) e Análise de Demonstrações Financeiras (GMF).",
 "**Habilidades Técnicas:** Pacote Office (avançado), Excel e VBA, Python, SQL e Power BI.",
 "**Competições:** Semifinalista do Challenge Ágora.",
 "**Línguas:** Português (nativo), Inglês (avançado) e Espanhol (intermediário).",
 "**Interesses:** Tênis, xadrez e leitura de livros de não-ficção.",
]


def runs(text):
    out, bold = [], False
    for part in text.split("**"):
        if part:
            out.append((part, bold))
        bold = not bold
    return out


def words(text):
    ws = []
    for chunk, b in runs(text):
        for w in chunk.split(" "):
            if w:
                ws.append((w, b))
    return ws


def wrap(ws, width, size):
    lines, cur, curw = [], [], 0.0
    sp = stringWidth(" ", F, size)
    for w, b in ws:
        wd = stringWidth(w, FB if b else F, size)
        add = wd if not cur else wd + sp
        if cur and curw + add > width:
            lines.append(cur)
            cur, curw = [(w, b)], wd
        else:
            cur.append((w, b))
            curw += add
    if cur:
        lines.append(cur)
    return lines


def render(c, LEAD, GAP_SEC, GAP_ENTRY, dry=False):
    """y e medido do TOPO para baixo; a conversao para o sistema do reportlab
    (origem no canto inferior esquerdo) acontece em ds/drs/ln."""
    def ds(x, y, t):
        if not dry:
            c.drawString(x, H - y, t)

    def drs(x, y, t):
        if not dry:
            c.drawRightString(x, H - y, t)

    def ln(y):
        if not dry:
            c.setLineWidth(1.0)
            c.line(RULE0, H - y, RULE1, H - y)

    def font(name, size):
        if not dry:
            c.setFont(name, size)

    y = 38.0
    font(FB, SZ_NAME); ds(LEFT, y, NAME)
    y += 15.0
    font(F, SZ_CONTACT); ds(LEFT, y, CONTACT)
    y += GAP_SEC + 4

    def draw_lines(lines, x, size, lead):
        nonlocal y
        for line in lines:
            if not dry:
                cx = x
                for i, (w, b) in enumerate(line):
                    c.setFont(FB if b else F, size)
                    if i:
                        cx += stringWidth(" ", F, size)
                    c.drawString(cx, H - y, w)
                    cx += stringWidth(w, FB if b else F, size)
            y += lead

    for title, entries in DATA:
        font(FB, SZ_SEC); ds(LEFT, y, title)
        y += 3.2
        ln(y)
        y += LEAD - 1.5
        for comp, city, role, dates, bullets in entries:
            font(FB, SZ_BODY); ds(LEFT, y, comp); drs(RIGHT, y, city)
            y += LEAD - 0.6
            font(FI, SZ_BODY)
            for i, line in enumerate(wrap(words(role), RIGHT - LEFT - 150, SZ_BODY)):
                if not dry:
                    c.setFont(FI, SZ_BODY)
                    c.drawString(LEFT, H - y, " ".join(w for w, _ in line))
                if i == 0 and dates:
                    drs(RIGHT, y, dates)
                y += LEAD - 0.6
            for b in bullets:
                font(F, SZ_BODY); ds(BULLET_X, y, "\u2022")
                draw_lines(wrap(words(b), RIGHT - TEXT_X, SZ_BODY), TEXT_X, SZ_BODY, LEAD - 0.6)
            y += GAP_ENTRY
        y += GAP_SEC - GAP_ENTRY

    font(FB, SZ_SEC); ds(LEFT, y, "HABILIDADES, CERTIFICAÇÕES E INTERESSES")
    y += 3.2
    ln(y)
    y += LEAD - 1.5
    for s in SKILLS:
        draw_lines(wrap(words(s), RIGHT - LEFT, SZ_BODY), LEFT, SZ_BODY, LEAD - 0.6)
    return y


def main():
    best = None
    for LEAD in [13.2, 12.9]:
        for GAP_SEC in [11.0, 10.0, 9.0]:
            for GAP_ENTRY in [6.0, 5.0, 4.0]:
                c = canvas.Canvas("/dev/null", pagesize=(W, H))
                end = render(c, LEAD, GAP_SEC, GAP_ENTRY, dry=True)
                if end <= BOTTOM_LIMIT:
                    best = (LEAD, GAP_SEC, GAP_ENTRY, end)
                    break
            if best:
                break
        if best:
            break

    LEAD, GAP_SEC, GAP_ENTRY, end = best
    print("LAYOUT: leading=%.1f gap_secao=%.1f gap_entrada=%.1f fim_y=%.1f margem_inferior=%.1fpt"
          % (LEAD, GAP_SEC, GAP_ENTRY, end, H - end))
    out = "CV - Matteo Lucato (revisado).pdf"
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle("Curriculo - Matteo Lucato")
    c.setAuthor("Matteo Lucato")
    render(c, LEAD, GAP_SEC, GAP_ENTRY)
    c.showPage()
    c.save()
    print("GERADO:", out)


if __name__ == "__main__":
    main()
