#!/usr/bin/env python3
"""Monta o Guia de Execução no Wix em PDF (WeasyPrint)."""
import os
from weasyprint import HTML

BASE = "/projects/sandbox/audit-ccu"
OUT = os.path.join(BASE, "Guia-Execucao-Wix-CCU.pdf")

CSS = """
@page { size: A4; margin: 15mm 13mm 17mm 13mm;
  @bottom-center { content: "Guia de Execução no Wix — CCU · pág. " counter(page) " de " counter(pages);
    font-family: 'Noto Sans'; font-size: 7.6pt; color: #8A8A8A; } }
@page :first { margin: 0; @bottom-center { content: ""; } }
* { box-sizing: border-box; }
body { font-family: 'Noto Sans', sans-serif; font-size: 9.1pt; color: #181818; line-height: 1.5; margin: 0; }
h1 { font-size: 19pt; margin: 0 0 3mm; color: #181818; line-height: 1.15; }
h2 { font-size: 13.2pt; margin: 9mm 0 3mm; padding-bottom: 1.6mm; border-bottom: 2.2px solid #C1272D;
     color: #181818; page-break-after: avoid; }
h3 { font-size: 10.6pt; margin: 6mm 0 2mm; color: #C1272D; page-break-after: avoid; }
h4 { font-size: 9.4pt; margin: 4mm 0 1.5mm; color: #181818; page-break-after: avoid; }
p { margin: 0 0 2.4mm; }
ul, ol { margin: 0 0 2.8mm; padding-left: 5.2mm; }
li { margin-bottom: 1.3mm; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.1pt; background: #F2F2F3;
       padding: 0.4mm 1mm; border-radius: 2px; }
table { width: 100%; border-collapse: collapse; margin: 0 0 3.4mm; font-size: 8.2pt; }
th { background: #181818; color: #fff; text-align: left; padding: 1.7mm 2mm; font-weight: 700; font-size: 8pt; }
td { padding: 1.6mm 2mm; border-bottom: 1px solid #E3E3E3; vertical-align: top; }
tr:nth-child(even) td { background: #FAFAFA; }
.cover { background: #181818; color: #fff; height: 297mm; padding: 34mm 24mm 0; }
.cover .kicker { color: #E9989B; font-size: 9.4pt; letter-spacing: 2.4px; text-transform: uppercase; margin-bottom: 7mm; }
.cover h1 { color: #fff; font-size: 33pt; line-height: 1.1; margin-bottom: 5mm; }
.cover .sub { color: #C9C9C9; font-size: 12pt; line-height: 1.55; max-width: 130mm; }
.cover .rule { width: 46mm; height: 4.5px; background: #C1272D; margin: 9mm 0; }
.cover .meta { margin-top: 26mm; font-size: 8.9pt; color: #9A9A9A; line-height: 1.85; }
.cover .box { margin-top: 12mm; border-left: 3.4px solid #C1272D; padding: 4mm 0 4mm 6mm;
              color: #E4E4E4; font-size: 9.6pt; max-width: 132mm; }
figure { margin: 0 0 4.5mm; page-break-inside: avoid; }
.grid2 { page-break-inside: avoid; }
figure img { width: 100%; border: 1px solid #DDD; display: block; }
figcaption { font-size: 7.6pt; color: #6E6E6E; margin-top: 1.3mm; line-height: 1.4; }
.shot img { border: 1px solid #CFCFCF; }
.alert { background: #FDF4F4; border-left: 3.4px solid #C1272D; padding: 2.8mm 3.4mm; margin: 0 0 3.4mm; font-size: 8.6pt; }
.ok { background: #F1F8F3; border-left: 3.4px solid #1E7A45; padding: 2.8mm 3.4mm; margin: 0 0 3.4mm; font-size: 8.6pt; }
.warn { background: #FFFBEF; border-left: 3.4px solid #B8860B; padding: 2.8mm 3.4mm; margin: 0 0 3.4mm; font-size: 8.6pt; }
.task { border: 1px solid #DEDEDE; border-radius: 4px; padding: 3.4mm 4mm; margin: 0 0 4.5mm; page-break-inside: avoid; }
.task h3 { margin-top: 0; }
.tags { font-size: 7.5pt; color: #6E6E6E; margin-bottom: 2.4mm; }
.tag { background: #EFEFEF; border-radius: 9px; padding: 0.7mm 2.2mm; margin-right: 1.6mm; }
.tag.p { background: #E4F3E9; color: #1E7A45; } .tag.m { background: #FFF4DC; color: #8A6400; }
.tag.g { background: #FBE7E8; color: #A81F25; }
.grid2 { display: flex; gap: 3.4mm; margin-bottom: 4mm; }
.grid2 > div { flex: 1; }
.grid2 figure img { max-height: 86mm; width: auto; max-width: 100%; }
.imgrow figure img { max-height: 62mm; width: auto; max-width: 100%; }
.imgrow { display: flex; gap: 2.4mm; margin-bottom: 1.6mm; }
.imgrow > figure { flex: 1; margin-bottom: 0; }
.imgrow img { border: 1px solid #DDD; }
.pill { display:inline-block; background:#C1272D; color:#fff; font-size:7.4pt; font-weight:700;
        padding:0.7mm 2.2mm; border-radius:2px; margin-right:1.6mm; }
.newpage { page-break-before: always; }
.small { font-size: 7.9pt; color: #5E5E5E; }
.chk { font-family: 'DejaVu Sans', sans-serif; }
"""


def img(path, cap, cls="", w=None):
    style = f' style="width:{w}"' if w else ""
    return (f'<figure class="{cls}"><img src="{path}"{style}/>'
            f'<figcaption>{cap}</figcaption></figure>')


P = []  # pedaços de HTML

# ───────────────────────── CAPA
P.append("""
<div class="cover">
  <div class="kicker">Clube de Consultoria Universitário</div>
  <h1>Guia de execução<br/>no Wix</h1>
  <div class="rule"></div>
  <div class="sub">Passo a passo ilustrado para deixar o site mais enxuto e atualizado —
  com as evidências capturadas do site no ar e o banco de imagens do LinkedIn do clube
  mapeado para cada página.</div>
  <div class="box">O site está no ar hoje sem nenhum caminho de inscrição funcionando,
  enquanto o Consulting Women&rsquo;s Community acontece com Kearney, Roland Berger,
  Bain, Peers e BCG — e a página do CWC não menciona nada disso.</div>
  <div class="meta">
    Documento complementar ao relatório de auditoria<br/>
    Plataforma: Wix Editor clássico (não Studio)<br/>
    Coleta: 16 de setembro de 2026<br/>
    44 URLs verificadas · 11 telas capturadas · 17 imagens recuperadas do LinkedIn
  </div>
</div>
""")

# ───────────────────────── COMO USAR
P.append("""
<h2>Como usar este guia</h2>
<p>Este documento é a parte operacional da auditoria. Cada tarefa traz: o que está errado,
a evidência, o caminho de clique no Wix e o critério para saber que ficou pronto.
A ordem é a das ondas do backlog — comece pela Parte C, tarefa T1.</p>

<div class="warn">
<b>Sobre as imagens deste guia — leia antes de continuar.</b> Há três tipos, e eles não se confundem:
<ul>
<li><b>Capturas reais do site do CCU</b> (moldura cinza). Foram tiradas do site público em 16/09/2026,
com o navegador em 1440&times;1000. São a evidência de cada problema.</li>
<li><b>Diagramas esquemáticos dos painéis do Wix</b> (marcados <i>&ldquo;ESQUEMA — não é captura de tela do Wix&rdquo;</i>).
São ilustrações desenhadas para este guia, mostrando a posição relativa dos controles e o caminho de clique.
<b>Não consigo gerar capturas reais do editor Wix do CCU</b>, porque isso exigiria acesso logado à conta do clube.
Os nomes dos comandos seguem a interface em português do Wix Editor; se a conta estiver em inglês,
os equivalentes estão indicados entre parênteses.</li>
<li><b>Peças gráficas do próprio clube</b>, recuperadas do LinkedIn público do CCU. São material do CCU,
reaproveitável no site.</li>
</ul>
</div>

<div class="alert">
<b>Uma ressalva de método.</b> Não tenho acesso ao painel Wix do clube. Os caminhos de clique descritos
seguem a estrutura do Wix Editor clássico, confirmada pelo código do site
(<code>"isResponsive":false</code>, <code>id="wixDesktopViewport"</code>). Rótulos de menu podem variar
conforme a versão da conta. Onde a ação depende de uma informação que só a diretoria tem
(datas da próxima edição, números da última turma), isso está sinalizado.
</div>
""")

# ───────────────────────── PARTE A
P.append("""
<div class="newpage"></div>
<h2>Parte A · O que o LinkedIn revelou</h2>
<p>Você pediu para procurar imagens no LinkedIn e no Instagram do clube. O Instagram
(<code>@ccuclubedeconsultoria</code>) exige login e bloqueou o acesso — redirecionou para
<code>/accounts/login</code>, então <b>não consegui verificar nada de lá</b>. O LinkedIn
(<code>/company/clube-de-consultoria-universitario</code>) está público e rendeu 17 imagens e,
mais importante, <b>informação que contradiz o site</b>.</p>

<h3>A.1 O CWC está acontecendo agora — e o site não sabe</h3>
<p>O post de 4 semanas atrás anuncia: <i>&ldquo;O Consulting Women&rsquo;s Community 2026 já começou!&rdquo;</i>,
citando <b>McKinsey &amp; Company, Accenture, Kearney, Roland Berger, Bain &amp; Company,
Peers Consulting e BCG</b>. O cronograma publicado detalha setembro:</p>
<table>
<tr><th style="width:15%">Data</th><th style="width:9%">Hora</th><th style="width:24%">Consultoria</th><th>Tema</th></tr>
<tr><td>19/08 (qua)</td><td>19h30</td><td>McKinsey &amp; Company</td><td>&ldquo;The Broken Rung&rdquo; — Como atingir seu maior potencial</td></tr>
<tr><td>26/08 (qua)</td><td>19h30</td><td>Accenture</td><td>Trilha de Vida e Carreira (bate-papo)</td></tr>
<tr><td>02/09 (qua)</td><td>19h30</td><td>Kearney</td><td>Problem Solving em Ambientes Competitivos</td></tr>
<tr><td>09/09 (qua)</td><td>19h30</td><td>Roland Berger</td><td>Visão Estratégica &amp; Atualidades de Mercado</td></tr>
<tr><td><b>16/09 (qua)</b></td><td>19h30</td><td>Bain &amp; Company</td><td>Crescimento de Alta Performance e Liderança Feminina</td></tr>
<tr><td>23/09 (qua)</td><td>19h30</td><td>Peers</td><td>Tech, IA e Consultoria Estratégica</td></tr>
<tr><td>24/09 (qui)</td><td>19h00</td><td>BCG</td><td>Roda de Conversa e Encerramento (presencial)</td></tr>
</table>
<p class="small">As sete sessões e as sete consultorias conferem com o post do clube. Transcrito das peças
<code>cwc-2026-b.jpg</code> (agosto) e <code>cwc-2026-c.jpg</code> (setembro).</p>
<div class="alert"><b>A sessão de 16/09 é hoje.</b> O programa encerra em 24/09/2026. É a
<b>3ª edição</b> do CWC (post de 1 mês: <i>&ldquo;As inscrições para a 3ª edição&hellip; estão abertas&rdquo;</i>,
inscrições de 19 de agosto a 23). Enquanto isso, a página <code>/consulting-women-consulting</code>
tem 236 palavras de adjetivos, <b>zero data, zero nome de consultoria, zero botão de inscrição</b> e
nenhum título (<code>&lt;h1&gt;</code> ou <code>&lt;h2&gt;</code>). É a maior distância entre o que o
clube faz e o que o site conta.</div>
""")

P.append('<div class="grid2">'
         + '<div>' + img("../social/img/cwc-2026-c.jpg",
                        "Peça do CCU no LinkedIn: cronograma de setembro do CWC, com consultoria e tema por encontro. "
                        "Toda essa informação deveria estar como <b>texto</b> na página do CWC.") + '</div>'
         + '<div>' + img("../shots/cwc-fraca.png",
                         "Captura real de <code>/consulting-women-consulting</code> em 16/09/2026: três parágrafos "
                         "genéricos, sem datas, sem parceiros e sem nenhuma forma de participar.", "shot") + '</div>'
         + '</div>')

P.append("""
<h3>A.2 O Processo Seletivo 2026.2 rodou inteiro fora do site</h3>
<p>Post de 2 semanas atrás: <i>&ldquo;O Clube de Consultoria Universitário está com o Processo Seletivo
2026.2 aberto!&rdquo;</i> — <b>&ldquo;Inscrições: 17 de agosto a 07 de setembro&rdquo;</b>, com
<i>&ldquo;Inscreva-se pelo link nos comentários&rdquo;</i>.</p>
<p>Três consequências, todas verificadas:</p>
<ol>
<li>O clube conduziu sua principal captação de membros <b>sem usar o site</b>: o link ia nos comentários do post.</li>
<li>A página do PS no site (<code>/blank-6</code>) não recebe <b>nenhum link interno</b> — nem do menu, nem do rodapé,
nem de outra página. Ficou invisível durante toda a campanha.</li>
<li>O botão &ldquo;Inscreva-se já!&rdquo; dessa página aponta para um formulário que não é o de 2026.2:
é o <b>&ldquo;Formulário de Inscrição PS Interno CCU 2022.1&rdquo;</b>, e está fechado.</li>
</ol>
""")

P.append('<div class="grid2">'
         + '<div>' + img("../shots/ps-orfa.png",
                        "Captura real de <code>/blank-6</code>: &ldquo;Não perca tempo! Garanta sua vaga no PS!&rdquo; — "
                        "o hype que a própria política do clube proíbe. Página órfã.", "shot") + '</div>'
         + '<div>' + img("../shots/form-fechado.png",
                         "Destino do botão: o formulário do <b>PS 2022.1</b>, encerrado. O banner traz a tagline "
                         "&ldquo;da Unicamp para o Mundo&rdquo;, que não existe no site.", "shot") + '</div>'
         + '</div>')

P.append("""
<h3>A.3 O cronograma do curso existe pronto — com a consultoria de cada módulo</h3>
<p>A recomendação do relatório era adotar do Poli Consulting Club o padrão de <i>nomear qual parceiro
ensina cada módulo</i>. <b>O CCU já faz isso</b> — só não no site. A peça do cronograma do
Prep4Consulting 2026.2 traz dia, hora, módulo e a consultoria responsável:</p>
<table>
<tr><th>Data</th><th>18h00</th><th>20h00</th><th>Parceiro</th></tr>
<tr><td>20/07 seg</td><td>Prep 101 + Consulting 101</td><td>Fit + Screening</td><td>McKinsey &amp; Company</td></tr>
<tr><td>21/07 ter</td><td>Screening</td><td>GMAT: Estrutura de prova</td><td>—</td></tr>
<tr><td>22/07 qua</td><td>GMAT: Problem Solving</td><td>GMAT: Data Sufficiency</td><td>—</td></tr>
<tr><td>23/07 qui</td><td>GMAT: Critical Reasoning</td><td>Fit + Screening</td><td>—</td></tr>
<tr><td>24/07 sex</td><td>GMAT</td><td>Framework</td><td>BCG</td></tr>
<tr><td>25/07 sáb</td><td>10h Finanças</td><td>13h Dinâmica em Grupo + Fit</td><td>—</td></tr>
<tr><td>27/07 seg</td><td>Dinâmica em grupo</td><td>Case Interview</td><td>EloGroup</td></tr>
<tr><td>28/07 ter</td><td>Case Interview</td><td>Guesstimate</td><td>Kearney</td></tr>
<tr><td>29/07 qua</td><td>Estratégia</td><td>Crack the case Harvard</td><td>Visagio</td></tr>
<tr><td>30/07 qui</td><td>Crack the case GBP</td><td>—</td><td>btc</td></tr>
<tr><td>31/07 sex</td><td>Crack the case</td><td>—</td><td>Bain &amp; Company</td></tr>
</table>
<div class="ok"><b>Isso resolve dois achados de uma vez.</b> É o conteúdo do cronograma que hoje só existe
dentro de um PNG na página do curso (alt = <code>cronograma-prep4consulting-2026-2_5.png</code>), e é a
prova de parceria que a home não tem. Transcrever esta tabela para texto na página do curso mata os dois.</div>
""")

P.append('<div class="grid2">'
         + '<div>' + img("../social/img/p4c-cronograma.jpg",
                        "Peça do CCU: cronograma completo do Prep4Consulting 2026.2 (20 a 31 de julho), "
                        "com o logo da consultoria em cada módulo.") + '</div>'
         + '<div>' + img("../social/img/p4c-parceiros-1.jpg",
                         "Peça do CCU: &ldquo;Empresas Parceiras — Parte I&rdquo; (EloGroup, McKinsey, Kearney, Visagio). "
                         "Há 6 peças dessas, úteis para a futura página <code>/parceiros</code>.") + '</div>'
         + '</div>')

P.append("""
<h3>A.4 Quatro informações que o clube publica e o site omite</h3>
<table>
<tr><th style="width:26%">Informação</th><th style="width:37%">O que o LinkedIn diz</th><th>O que o site diz</th></tr>
<tr><td><b>Desconto de grupo</b></td>
<td>&ldquo;4 a 7 pessoas: 40% OFF · 8 a 12 pessoas: 50% OFF · 13 ou mais: 60% OFF&rdquo;, via cupom
pedido por e-mail</td>
<td><b>Nada.</b> A seção de preços mostra apenas R$ 189,99 e R$ 239,99. Um desconto de até 60% não é anunciado.</td></tr>
<tr><td><b>Tagline</b></td><td>&ldquo;CCU — da Unicamp para o Mundo&rdquo; (também no banner do formulário)</td>
<td>Não aparece. A home abre com &ldquo;BEM-VINDO AO CLUBE DE CONSULTORIA UNIVERSITÁRIO&rdquo;.</td></tr>
<tr><td><b>Fundação</b></td><td>&ldquo;Criado em 2011 por alunos de graduação da Unicamp&rdquo; · 15 anos de história</td>
<td>Nenhuma menção ao ano de fundação em <code>/sobre-nos</code>.</td></tr>
<tr><td><b>Prazo de inscrição do curso</b></td><td>&ldquo;Inscrições até <b>19/07</b>&rdquo; (dois posts)</td>
<td>&ldquo;Inscrições até <b>17/07/2026</b>&rdquo; em <code>/eventos</code> e na página do evento —
<b>dois prazos diferentes publicados</b>.</td></tr>
</table>
<p class="small">Outros dados públicos verificáveis no LinkedIn, hoje ausentes do site:
<b>1.854 seguidores</b>, sede em Campinas-SP, e dois ativos de conteúdo já produzidos
(um glossário de termos de consultoria em 3 cartões e um post &ldquo;6 diferenciais&rdquo; do curso)
que servem para alimentar <code>/conteudo</code> e o FAQ.</p>
""")

# ───────────────────────── PARTE B
P.append("""
<div class="newpage"></div>
<h2>Parte B · Banco de imagens: o que usar em cada página</h2>
<p>As 17 imagens foram baixadas do LinkedIn público do CCU e estão na pasta
<code>audit-ccu/social/img/</code>. São peças do próprio clube — reaproveitá-las no site é legítimo.</p>

<div class="warn"><b>Duas regras técnicas antes de usar.</b>
<ol>
<li><b>Não use o link do LinkedIn direto no Wix.</b> As URLs <code>media.licdn.com</code> têm assinatura
de expiração (<code>?v=beta&amp;t=&hellip;</code>) e vão quebrar. Baixe e envie o arquivo para o
<b>Gerenciador de Mídia</b> do Wix.</li>
<li><b>Recorte para o formato da web.</b> Todas as peças são verticais de Instagram (1080&times;1350 ou
1080&times;1440). Cartões de evento e faixas de site pedem formato horizontal ou quadrado —
recorte o miolo, ou use a peça vertical só em coluna estreita no mobile.</li>
</ol></div>

<h3>B.1 Mapa de uso</h3>
<table>
<tr><th style="width:22%">Arquivo</th><th style="width:26%">Onde usar</th><th style="width:30%">Texto alternativo sugerido</th><th>Observação</th></tr>
<tr><td><code>p4c-cronograma.jpg</code></td><td><code>/prep4consulting</code> — apoio visual ao lado da tabela de texto</td>
<td>&ldquo;Cronograma do Prep4Consulting 2026.2: 11 encontros de 20 a 31 de julho&rdquo;</td>
<td>Prioridade: transcreva para <b>texto</b>; a imagem é reforço, não a fonte.</td></tr>
<tr><td><code>cwc-2026-c.jpg</code></td><td><code>/consulting-womens-community</code></td>
<td>&ldquo;Cronograma de setembro do CWC 2026 com Kearney, Roland Berger, Bain, Peers e BCG&rdquo;</td>
<td>Transcreva as 5 sessões como texto também.</td></tr>
<tr><td><code>cwc-2026-a/b/d.jpg</code></td><td><code>/consulting-womens-community</code> — galeria</td>
<td>&ldquo;Peça de divulgação da 3ª edição do Consulting Women&rsquo;s Community&rdquo;</td>
<td>Identidade mauve do CWC; combina com fundo escuro (ver D5).</td></tr>
<tr><td><code>p4c-parceiros-1..6.jpg</code></td><td>nova página <code>/parceiros</code></td>
<td>&ldquo;Consultorias parceiras do Prep4Consulting 2026.2&rdquo;</td>
<td>Melhor: extrair os logos e montar grade padronizada (ver T11).</td></tr>
<tr><td><code>glossario-1..3.jpg</code></td><td><code>/conteudo</code> ou <code>/faq</code></td>
<td>&ldquo;Glossário de termos usados em consultoria estratégica&rdquo;</td>
<td>Vira conteúdo de texto indexável — hoje só existe como imagem no LinkedIn.</td></tr>
<tr><td><code>p4c-reta-final.jpg</code></td><td>usar só <b>durante</b> janela de inscrição aberta</td>
<td>&ldquo;Inscrições abertas para o Prep4Consulting&rdquo;</td>
<td>Peça datada: retire quando a inscrição fechar.</td></tr>
<tr><td><code>logo-ccu.png</code> / <code>capa-ccu.png</code></td><td>favicon, Open Graph, cabeçalho</td>
<td>&ldquo;Clube de Consultoria Universitário&rdquo;</td>
<td>Capa 2100&times;637 serve de imagem de compartilhamento.</td></tr>
</table>

<div class="ok"><b>Ganho colateral de performance.</b> As 17 peças do LinkedIn pesam entre
<b>79 KB e 167 KB</b>. As imagens que hoje estão no site chegam a <b>6.839 KB</b> (em
<code>/loyalty</code>), <b>5.189 KB</b> (<code>/blank-2</code>) e <b>3.082 KB</b> (<code>/blank-6</code>).
Ou seja: o material gráfico do próprio clube é cerca de <b>40&times; mais leve</b> do que o que está
publicado. Trocar já melhora o site no celular.</div>
""")

P.append('<h3>B.2 As peças recuperadas</h3>')
rows = [["cwc-2026-a.jpg", "cwc-2026-b.jpg", "cwc-2026-c.jpg", "cwc-2026-d.jpg"],
        ["p4c-cronograma.jpg", "p4c-reta-final.jpg", "p4c-parceiros-1.jpg", "p4c-parceiros-2.jpg"],
        ["p4c-parceiros-3.jpg", "p4c-parceiros-4.jpg", "glossario-1.jpg", "glossario-2.jpg"]]
for r in rows:
    P.append('<div class="imgrow">' + "".join(
        f'<figure><img src="../social/img/{f}"/><figcaption>{f}</figcaption></figure>' for f in r
    ) + '</div>')
P.append('<p class="small">Fonte: LinkedIn público do Clube de Consultoria Universitário, '
         'coletado em 16/09/2026. Material de autoria do próprio CCU.</p>')

# ───────────────────────── PARTE C
P.append("""
<div class="newpage"></div>
<h2>Parte C · Passo a passo no Wix</h2>
<p>14 tarefas, na ordem de execução. Cada uma tem esforço estimado
(<span class="tag p">P</span> até 30 min · <span class="tag m">M</span> 1 a 4 h ·
<span class="tag g">G</span> mais de 4 h) e um critério de aceite objetivo.</p>

<div class="alert"><b>Antes da primeira tarefa.</b> No Wix não há histórico de versões ilimitado:
vá em <b>Site &gt; Salvar</b> e depois em <b>Histórico do site</b> (<i>Site History</i>) e
<b>nomeie a versão atual</b> como &ldquo;antes da limpeza — set/2026&rdquo;. É o seu ponto de retorno.</div>

<h3>Conceito que explica 21 das 44 URLs do site</h3>
""")
P.append(img("../diagrams/d1-paginas.png",
             "<b>D1</b> — No Wix, “Ocultar do menu” deixa a página publicada, no sitemap e no Google. "
             "Só “Excluir” remove. Essa confusão é a origem das páginas órfãs."))

# Tarefas
def task(tid, titulo, esforco, corpo, aceite, diagrama=None, dcap=None, shot=None, scap=None):
    cls = {"P": "p", "M": "m", "G": "g"}[esforco]
    h = f'<div class="task"><h3>{tid} · {titulo}</h3>'
    h += (f'<div class="tags"><span class="tag {cls}">{esforco}</span>'
          f'<span class="tag">Wix Editor clássico</span></div>')
    h += corpo
    if shot:
        h += img(shot, scap, "shot")
    if diagrama:
        h += img(diagrama, dcap)
    h += f'<div class="ok"><b>Pronto quando:</b> {aceite}</div></div>'
    return h


P.append(task("T1", "Parar de convidar para um formulário fechado", "P", """
<p><b>Problema.</b> <code>/blank-6</code> diz &ldquo;Não perca tempo! Garanta sua vaga no PS!&rdquo; e o botão
&ldquo;Inscreva-se já!&rdquo; leva ao formulário do <b>PS 2022.1</b>, encerrado. A mesma página oferece um
e-book &ldquo;PS 2022.1&rdquo;. A página não é tocada desde 2022 e está órfã.</p>
<p><b>Passos.</b></p>
<ol>
<li>Editor &gt; painel esquerdo &gt; <b>Menus e Páginas</b> &gt; abrir a página <code>blank-6</code>.</li>
<li>Clicar no botão &ldquo;Inscreva-se já!&rdquo; &gt; ícone de <b>link</b> &gt; <b>Uma página do meu site</b>
&gt; escolher <b>Mailing</b>.</li>
<li>Trocar o rótulo do botão para <b>&ldquo;Quero ser avisado do próximo PS&rdquo;</b>.</li>
<li>Editar o texto acima: <i>&ldquo;As inscrições para o Processo Seletivo 2026.2 foram encerradas em
07/09/2026. As do próximo semestre abrem em [mês/ano].&rdquo;</i> — com <b>dia/mês/ano completos</b>.</li>
<li>Remover o bloco do e-book 2022.1 (ou substituir pelo material vigente).</li>
<li>Trocar o título para &ldquo;O Clube está em busca de novos membros&rdquo;, sem exclamação dupla.</li>
<li>Alternar para o <b>editor mobile</b> e repetir. <b>Publicar</b>.</li>
</ol>
""", "a página não contém mais nenhum link para <code>forms.gle/gWXZmxHAxWAhH1VW8</code> e a frase "
     "&ldquo;Não perca tempo! Garanta sua vaga no PS!&rdquo; não existe mais no HTML."))

P.append(task("T2", "Tirar o Processo Seletivo da invisibilidade", "P", """
<p><b>Problema.</b> A página do PS não recebe nenhum link em todo o site. O menu é
Início · Sobre nós · Projetos · Parceiros · Conteúdo · Alumni · Mailing · Mais — sem PS.</p>
<p><b>Passos.</b></p>
<ol>
<li><b>Menus e Páginas</b> &gt; engrenagem de <code>blank-6</code> &gt; <b>SEO básico</b> &gt;
trocar a URL para <code>processo-seletivo</code>.</li>
<li>Preencher <b>Título do SEO</b>: <code>Processo Seletivo do CCU — seja membro | CCU</code> (44 caracteres).</li>
<li>Preencher <b>Descrição do SEO</b> (hoje vazia) com até 155 caracteres.</li>
<li>Arrastar a página para o <b>topo</b> da lista do menu; renomear o item para <b>Processo Seletivo</b>.</li>
<li><b>Imediatamente</b>: Painel &gt; <b>SEO &gt; Redirecionamentos de URL</b> &gt; criar 301
<code>/blank-6</code> &rarr; <code>/processo-seletivo</code>.</li>
</ol>
""", "<code>/processo-seletivo</code> responde 200, aparece no menu de todas as páginas, e "
     "<code>/blank-6</code> responde 301.",
     "../diagrams/d2-seo.png",
     "<b>D2</b> — Painel de SEO da página: onde se corrige o slug, o título e a descrição. "
     "A prévia mostra como o resultado aparece no Google."))

P.append(task("T3", "Criar os 31 redirecionamentos 301", "M", """
<p><b>Problema.</b> Sete páginas centrais moram em slugs de template (<code>/blank</code> a
<code>/blank-7</code>) e 14 páginas de evento vão ser excluídas. Sem 301, todo link já compartilhado quebra.</p>
<p><b>Passos.</b> Painel do site &gt; <b>SEO</b> &gt; <b>Redirecionamentos de URL</b>
(<i>URL Redirect Manager</i>) &gt; <b>+ Novo redirecionamento</b>, tipo <b>301</b>. Principais:</p>
<table>
<tr><th>De</th><th>Para</th><th>De</th><th>Para</th></tr>
<tr><td><code>/blank</code></td><td><code>/alumni</code></td><td><code>/blank-7</code></td><td><code>/contato</code></td></tr>
<tr><td><code>/blank-2</code></td><td><code>/casebooks</code></td><td><code>/shop</code></td><td><code>/prep4consulting</code></td></tr>
<tr><td><code>/blank-3</code></td><td><code>/casebook-ccu</code></td><td><code>/forum</code></td><td><code>/conteudo</code></td></tr>
<tr><td><code>/blank-4</code></td><td><code>/banco-de-casebooks</code></td><td><code>/members</code></td><td><code>/processo-seletivo</code></td></tr>
<tr><td><code>/blank-5</code></td><td><code>/conteudo</code></td><td><code>/blog</code></td><td><code>/conteudo</code></td></tr>
<tr><td><code>/blank-6</code></td><td><code>/processo-seletivo</code></td><td><code>/loyalty</code></td><td><code>/prep4consulting</code></td></tr>
<tr><td><code>/blank-1</code></td><td><code>/</code></td><td><code>/book-online</code></td><td><code>/contato</code></td></tr>
<tr><td><code>/prep4consulting-2026-2</code></td><td><code>/prep4consulting</code></td>
<td><code>/service-page/processo-seletivo</code></td><td><code>/processo-seletivo</code></td></tr>
<tr><td colspan="2"><code>/consulting-women-consulting</code></td><td colspan="2"><code>/consulting-womens-community</code></td></tr>
<tr><td colspan="2">13 &times; <code>/event-details/&hellip;</code> antigas</td><td colspan="2"><code>/eventos</code></td></tr>
</table>
""", "cada slug antigo devolve <b>301</b> (não 404 e não 200) e aterra no equivalente semântico.",
     "../diagrams/d3-301.png",
     "<b>D3</b> — Gerenciador de Redirecionamentos. Note o aviso: não repita o erro do PoliCC, "
     "onde <code>/sobre-nos</code> redireciona para a home em vez da página certa."))

P.append(task("T4", "Religar os casebooks — 3 links, 15 PDFs de volta", "P", """
<p><b>Problema.</b> Três CTAs que deveriam levar aos casebooks apontam para a raiz do site.
Isso deixa <code>/blank-2</code> órfã e, como <code>/blank-3</code> e <code>/blank-4</code> só recebem
link dela, derruba a vertical inteira — <b>15 casebooks que respondem HTTP 200</b> (MIT, Harvard,
Wharton &times;2, Kellogg, Ross &times;3, Darden &times;2, ESADE &times;2, NYU, Illinois, Kearney).</p>
<p><b>Os três elementos a corrigir:</b></p>
<ul>
<li><code>/conteudo</code> — card <b>&ldquo;Cases completos&rdquo;</b>, botão &ldquo;Ver mais&rdquo;</li>
<li><code>/casebook-ccu</code> (era <code>/blank-3</code>) — botão <b>&ldquo;CONFIRA&rdquo;</b></li>
<li><code>/guesstimate</code> — <i>&ldquo;&hellip;clique aqui e confira algumas resoluções de case&rdquo;</i></li>
</ul>
<p><b>Passos.</b> Para cada um: clicar no elemento &gt; ícone de <b>link</b> &gt;
<b>Uma página do meu site</b> &gt; <b>Casebooks</b> &gt; Concluído. Conferir no editor mobile. Publicar.</p>
""", "nenhum dos três elementos tem <code>href</code> igual à raiz do site, e <code>/casebooks</code> "
     "passa a receber 3 links internos.",
     "../diagrams/d8-link.png",
     "<b>D8</b> — Como trocar o destino de um botão. O erro atual é o link apontar para a raiz do site, "
     "sem âncora: um link morto."))

P.append(task("T5", "Encerrar o funil de venda com honestidade", "P", """
<p><b>Problema.</b> <code>/prep4consulting-2026-2</code> mostra &ldquo;POR R$189,99&rdquo;,
&ldquo;POR R$239,99&rdquo; e dois botões <b>&ldquo;Compre agora&rdquo;</b> — ambos levando a uma
página que responde <b>&ldquo;O registro está fechado / Vendas encerradas&rdquo;</b>.</p>
<p><b>Passos.</b></p>
<ol>
<li>Selecionar os dois botões &ldquo;Compre agora&rdquo; &gt; <b>Configurações &gt; Ocultar</b>
(não excluir — serão reusados na próxima edição).</li>
<li>Inserir caixa de texto: <i>&ldquo;As inscrições da edição 2026.2 foram encerradas. A próxima
edição abre em [mês/ano].&rdquo;</i></li>
<li>Adicionar <b>um</b> botão secundário &rarr; <code>/mailing</code>, rótulo
&ldquo;Avise-me quando abrir&rdquo;.</li>
<li>Aproveitar para incluir o <b>desconto de grupo</b> (40/50/60%), hoje só no LinkedIn — ver Parte A.4.</li>
<li>Editor mobile. Publicar.</li>
</ol>
""", "a página não contém mais &ldquo;Compre agora&rdquo; e tem exatamente 1 link para <code>/mailing</code>.",
     None, None,
     "../shots/evento-vendas-encerradas.png",
     "Captura real do destino dos botões: &ldquo;O registro está fechado&rdquo; e &ldquo;Vendas encerradas&rdquo;. "
     "Note também a taxa de <b>+ R$ 4,75</b>, que a página de preço não informa."))

P.append(task("T6", "Corrigir o rodapé — aparece nas 44 páginas", "P", """
<p><b>Problema.</b> Duas falhas repetidas em todo o site: <b>&ldquo;©2023 Clube de Consultoria
Universitário&rdquo;</b> e a frase quebrada <b>&ldquo;Todos os seus são direitos reservados&rdquo;</b>.
No mobile, o <b>CNPJ desaparece</b> do rodapé.</p>
<p><b>Passos.</b></p>
<ol>
<li>Editor &gt; clicar no rodapé (é global: editar uma vez vale para todas as páginas).</li>
<li>Trocar por <b>&ldquo;© 2026 Clube de Consultoria Universitário&rdquo;</b> e
<b>&ldquo;Todos os direitos reservados.&rdquo;</b></li>
<li>Adicionar link para <b>Política de Privacidade</b> (criada em T12) ao lado da Política de Troca.</li>
<li><b>Editor mobile</b>: conferir que endereço e <b>CNPJ 45.692.698/0001-91</b> aparecem —
hoje o CNPJ não é exibido no celular.</li>
</ol>
""", "busca por &ldquo;©2023&rdquo; e por &ldquo;Todos os seus&rdquo; retorna zero no site, e o CNPJ "
     "aparece no rodapé também no mobile."))

P.append(task("T7", "Apagar a página “Site em manutenção”", "P", """
<p><b>Problema.</b> <code>/blank-1</code> tem <code>&lt;h1&gt;Site em manutenção&lt;/h1&gt;</code>,
está publicada, indexável, no sitemap — e o <b>título SEO é idêntico ao da home</b>
(&ldquo;Início | Clube de Consultoria Universitário&rdquo;). Uma terceira página,
<code>/getting-the-job</code>, usa o mesmo título. Três URLs disputando o mesmo termo.</p>
<p><b>Passos.</b></p>
<ol>
<li><b>Menus e Páginas</b> &gt; <code>blank-1</code> &gt; <b>Excluir</b>.</li>
<li>301 <code>/blank-1</code> &rarr; <code>/</code>.</li>
<li>Página <b>Getting The Job</b> &gt; engrenagem &gt; <b>SEO básico</b> &gt; Título do SEO:
<code>Getting the Job: simulação de PS | CCU</code>.</li>
</ol>
""", "apenas <b>uma</b> página do site tem título começando com &ldquo;Início&rdquo;.",
     None, None, "../shots/blank-1-manutencao.png",
     "Captura real de <code>/blank-1</code>: página de manutenção pública, indexável e com o título da home."))

P.append(task("T8", "Desinstalar os seis apps que não são usados", "P", """
<p><b>Problema.</b> Sete URLs de app estão no ar, vazias ou quebradas. E o <b>ícone de carrinho com
&ldquo;0&rdquo;</b> aparece no cabeçalho de <b>todas</b> as páginas porque o Wix Stores está instalado —
inclusive nas páginas de conteúdo gratuito.</p>
<p><b>Passos.</b> Painel do site &gt; <b>Apps &gt; Gerenciar Apps</b> &gt; em cada app: <b>&hellip;</b>
&gt; <b>Excluir</b>. Desinstalar: Wix Stores, Wix Forum, Wix Loyalty, Wix Bookings, Members Area, Wix Blog.
<b>Manter o Wix Events</b> — é o que vende o curso. Depois, criar os 301 (T3).</p>
<div class="alert"><b>Confirme com a diretoria antes.</b> Se há intenção de abrir loja ou área de
membros neste semestre, mantenha o app mas <b>oculte a página da busca</b>
(SEO básico &gt; &ldquo;Ocultar esta página dos resultados de busca&rdquo;) até ter conteúdo real.</div>
""", "as sete URLs respondem 301, o <code>pages-sitemap.xml</code> cai de 28 para ~21 entradas, "
     "e o carrinho desaparece do cabeçalho.",
     "../diagrams/d7-apps.png",
     "<b>D7</b> — Quais apps remover e por quê. Ocultar a página não basta: ela continua publicada e indexável."))

P.append('<div class="imgrow">'
         + f'<figure><img src="../shots/forum-erro.png"/><figcaption>'
           f'<code>/forum</code>: &ldquo;Widget Didn&rsquo;t Load&rdquo; — erro em inglês, indexável.</figcaption></figure>'
         + f'<figure><img src="../shots/shop-vazia.png"/><figcaption>'
           f'<code>/shop</code>: sem produtos, mas a descrição no Google anuncia &ldquo;inscrições abertas&rdquo;.</figcaption></figure>'
         + '</div>')
P.append('<div class="imgrow">'
         + f'<figure><img src="../shots/loyalty-ingles.png"/><figcaption>'
           f'<code>/loyalty</code>: &ldquo;Sign up to the site&rdquo; não traduzido e recompensas para uma loja vazia.</figcaption></figure>'
         + f'<figure><img src="../shots/blank-7-contato-vazia.png"/><figcaption>'
           f'<code>/blank-7</code> &ldquo;Fale Conosco&rdquo;: só cabeçalho e rodapé. A página de contato está vazia.</figcaption></figure>'
         + '</div>')

P.append(task("T9", "Limpar as 14 edições de evento residuais", "M", """
<p><b>Problema.</b> 15 páginas de evento indexáveis. Duas se chamam <b>&ldquo;teste&rdquo;</b> e
<b>&ldquo;teste (1)&rdquo;</b>; uma é &ldquo;2025.1 <b>(old)</b>&rdquo;; e a edição <b>2026.1</b> mora no
slug <code>prep4consulting-2025-2-1-1</code>. Além disso <b>13 delas têm quase a mesma meta description</b>
(293 a 299 caracteres), o que é canibalização.</p>
<p><b>Passos.</b> Painel &gt; <b>Eventos</b> &gt; para cada evento encerrado: <b>&hellip; &gt; Excluir</b>.
Manter a edição corrente e, no máximo, a anterior. Criar 301 para <code>/eventos</code> (T3).
Se a diretoria quiser preservar histórico, em vez de excluir: abrir o evento &gt; <b>SEO</b> &gt;
marcar <b>&ldquo;Ocultar dos motores de busca&rdquo;</b> e reescrever a descrição para ser única.</p>
<div class="warn"><b>Nunca duplique um evento</b> para criar a edição seguinte — é o que gerou os
sufixos <code>-2</code>, <code>-3</code>, <code>-4</code> e <code>-2025-2-1-1</code>.
Crie evento novo com slug limpo: <code>prep4consulting-2027-1</code>.</div>
""", "<code>event-pages-sitemap.xml</code> lista no máximo 2 URLs e nenhuma contém "
     "&ldquo;teste&rdquo; ou &ldquo;old&rdquo;.",
     "../diagrams/d9-events.png",
     "<b>D9</b> — As 15 páginas de evento e o veredito de cada uma."))

P.append(task("T10", "Consertar a vitrine de eventos", "P", """
<p><b>Problema.</b> <code>/eventos</code> exibe <b>&ldquo;0 DIAS PARA O EVENTO&rdquo;</b>,
&ldquo;Inscrições até 17/07/2026!&rdquo;, &ldquo;Início: 20/07/2026!&rdquo; e ainda pergunta
<b>&ldquo;Você pode comparecer?&rdquo;</b> — para um curso que terminou em julho. A página é órfã
(não está no menu), mas está indexada.</p>
<p><b>Passos.</b></p>
<ol>
<li><b>Menus e Páginas</b> &gt; engrenagem de <b>Eventos</b> &gt; <b>Ocultar do menu</b>
<i>e também</i> <b>SEO básico &gt; Ocultar esta página dos resultados de busca</b> — as duas coisas,
enquanto não houver edição aberta.</li>
<li>Quando abrir a próxima edição, reverter as duas e pôr &ldquo;Eventos&rdquo; no menu.</li>
<li>Remover de <code>/prep4consulting</code> o link obsoleto para
<code>/event-details/prep4consulting-2023-2</code>.</li>
</ol>
""", "<code>/eventos</code> não aparece no sitemap, ou não exibe mais &ldquo;0 DIAS PARA O EVENTO&rdquo;; "
     "e a página do curso tem zero links para o evento de 2023.",
     None, None, "../shots/eventos.png",
     "Captura real de <code>/eventos</code> em 16/09/2026: contador zerado, datas de julho e convite de "
     "presença para evento encerrado. No alto à direita, o carrinho do Wix Stores."))

P.append(task("T11", "Aplicar os Temas de Texto e a paleta", "G", """
<p><b>Problema.</b> O site <b>já tem</b> um sistema tipográfico coerente configurado — Brandon Grotesque
Light para títulos, Avenir LT 35 Light para corpo, uma única cor de texto. E o sobrescreve
<b>3.948 vezes</b>: são <b>46 tamanhos de fonte</b> e <b>34 famílias</b> declaradas caixa por caixa,
incluindo fontes japonesas herdadas do template. São 141 sobrescritas por página, contra 28 do PoliCC
e <b>zero</b> nos clubes de USC e Rice.</p>
<p><b>Passos.</b></p>
<ol>
<li>Editor &gt; <b>Site &gt; Temas de Texto</b> &gt; ajustar os 6 temas conforme D4. É global e instantâneo.</li>
<li>Por página, na ordem: home, <code>/prep4consulting</code>, <code>/sobre-nos</code>,
<code>/processo-seletivo</code>, <code>/conteudo</code>. Em cada caixa de texto: <b>Ctrl+A</b> para
selecionar tudo, depois escolher o <b>Tema</b> — só assim a formatação manual é descartada.</li>
<li>Corrigir a hierarquia: <b>um</b> <code>&lt;h1&gt;</code> por página. Hoje a home tem <b>zero</b>,
<code>/alumni</code> tem <b>44</b>, <code>/sobre-nos</code> tem <b>18</b>, e nenhuma página do site
usa H3, H4 ou H5. Preço e nota de rodapé <b>nunca</b> são título — em
<code>/prep4consulting</code>, &ldquo;*Desconto válido&hellip;&rdquo; e &ldquo;de R$ 209,99&rdquo;
estão marcados como <code>&lt;h1&gt;</code>.</li>
<li>Cores: seguir D5. Texto secundário passa de <code>#898989</code> (reprova WCAG AA em fundo claro,
3,36:1) para <code>#515151</code> (7,62:1).</li>
</ol>
""", "as sobrescritas de fonte caem de 141 para menos de 20 por página nas 5 páginas principais, "
     "e cada página tem exatamente um <code>&lt;h1&gt;</code>.",
     "../diagrams/d4-temas.png",
     "<b>D4</b> — Temas de Texto: a correção de maior alcance. Arrumar o tema conserta o site inteiro."))

P.append(img("../diagrams/d5-paleta.png",
             "<b>D5</b> — A descoberta sobre a paleta: ela foi desenhada para as peças de fundo escuro do "
             "Instagram. Os rosas do CWC e os cinzas passam contraste AA em fundo escuro e reprovam em fundo "
             "claro; o vermelho da marca faz o oposto. Escolha a cor conforme o fundo da seção."))

P.append(task("T12", "Criar a Política de Privacidade e ajustar o mailing", "M", """
<p><b>Problema.</b> Não existe política de privacidade em nenhuma URL do site — o rodapé só linka a
Política de Troca. E o formulário de <code>/mailing</code> coleta <b>data de nascimento</b> e
<b>gênero como campo obrigatório</b> (Homem · Mulher · Trans · Outro · Prefiro não informar), sem
finalidade declarada, sem base legal e sem caixa de consentimento. O CCU tem CNPJ e trata dados de terceiros.</p>
<p><b>Passos.</b></p>
<ol>
<li><b>Menus e Páginas &gt; + Adicionar Página</b> &gt; nome &ldquo;Política de Privacidade&rdquo;,
slug <code>politica-privacidade</code> &gt; <b>Ocultar do menu</b> (mas deixar indexável).</li>
<li>Conteúdo mínimo: controlador (razão social + CNPJ), dados coletados, finalidade de cada um,
base legal (consentimento), prazo de retenção, com quem é compartilhado, e como pedir exclusão.</li>
<li>Rodapé &gt; adicionar o link (T6).</li>
<li>Formulário: clicar no campo de gênero &gt; desmarcar <b>Obrigatório</b>; declarar a finalidade ao lado
(ex.: &ldquo;usamos para medir a diversidade do público e desenhar o CWC&rdquo;).</li>
<li><b>Adicionar campo &gt; Caixa de seleção</b> para consentimento antes do botão &ldquo;Participar&rdquo;.</li>
<li>Remover <b>data de nascimento</b> se não houver uso definido — minimização de dados.</li>
<li>Corrigir o erro &ldquo;treinamentos e <b>processo seletivos</b>&rdquo; &rarr; &ldquo;processos seletivos&rdquo;.</li>
</ol>
""", "<code>/politica-privacidade</code> responde 200 e é linkada de todas as páginas; o campo de gênero "
     "não é mais obrigatório; existe caixa de consentimento."))

P.append(task("T13", "Dar prova e porta de entrada ao CWC", "M", """
<p><b>Problema.</b> É o projeto mais ativo do clube — 3ª edição, acontecendo agora, com 7 consultorias —
e a página mais fraca do site: 236 palavras de adjetivos, nenhum título, nenhum dado, <b>nenhuma
forma de participar</b>. Toda a informação real está no LinkedIn (Parte A.1).</p>
<p><b>Passos.</b></p>
<ol>
<li>Renomear o slug para <code>consulting-womens-community</code> (hoje
<code>consulting-women-consulting</code>, que não é o nome do projeto) + 301.</li>
<li>Padronizar o nome nos três lugares: título SEO, texto e slug &mdash; <b>Consulting Women&rsquo;s
Community (CWC)</b>.</li>
<li>Inserir um <code>&lt;h1&gt;</code> e a tabela de sessões <b>como texto</b> (data · consultoria · tema).</li>
<li>Adicionar a faixa de números: <b>3ª edição</b> · <b>7 consultorias parceiras</b> · nº de participantes
(pedir à diretoria).</li>
<li>Adicionar <b>um</b> botão primário: inscrição quando aberta, ou <code>/mailing</code> quando fechada.</li>
<li>Subir as peças <code>cwc-2026-*.jpg</code> pelo <b>Gerenciador de Mídia</b>, com alt descritivo.</li>
</ol>
""", "a página tem 1 <code>&lt;h1&gt;</code>, cita ao menos 5 consultorias pelo nome, mostra as datas "
     "como texto e tem exatamente 1 botão primário."))

P.append(task("T14", "Transformar o cronograma do curso em texto", "M", """
<p><b>Problema.</b> As datas do curso só existem dentro de um PNG
(<code>cronograma-prep4consulting-2026-2_5.png</code>, cujo <code>alt</code> é o próprio nome do arquivo).
Consequências: invisível para o Google, inacessível a leitor de tela, e cada edição exige reexportar
a imagem — o sufixo <code>_5</code> indica que já houve 5 versões. Duas imagens da página têm
<code>alt</code> vazio.</p>
<p><b>Passos.</b></p>
<ol>
<li>Inserir <b>Adicionar &gt; Tabela</b> (ou lista) com a grade da Parte A.3: data, horário, módulo, parceiro.</li>
<li>Manter a imagem como reforço visual, com alt descritivo.</li>
<li>Revisar o <code>alt</code> das imagens-chave (ver D10).</li>
<li>Reconstruir a ementa em <b>4 blocos, um por ciclo</b> — hoje o desktop mostra &ldquo;Ciclo 2&rdquo; e
&ldquo;Ciclo 3&rdquo; colados e <b>perdeu o módulo &ldquo;Estrutura do PS&rdquo;</b>, que só aparece no
mobile; e o mobile carrega dois textos soltos vindos de <code>/entrevista</code>.</li>
<li>Eliminar o rótulo <b>&ldquo;Âncora 1&rdquo;</b>, hoje visível no desktop e no mobile.</li>
<li>Padronizar &ldquo;Consulting 101&rdquo;, &ldquo;Fit Interview&rdquo;, &ldquo;Case Interview&rdquo; —
hoje a grafia difere entre desktop e mobile.</li>
</ol>
""", "as datas aparecem como texto no HTML da página; &ldquo;Estrutura do PS&rdquo; aparece no desktop "
     "<i>e</i> no mobile; e &ldquo;Âncora 1&rdquo; não aparece em nenhum dos dois.",
     "../diagrams/d6-mobile.png",
     "<b>D6</b> — A divergência entre os dois layouts. No Wix clássico o mobile é editado à parte: "
     "toda alteração precisa ser refeita lá."))

P.append(img("../diagrams/d10-alt.png",
             "<b>D10</b> — Texto alternativo: como está e como deve ficar. Imagem decorativa pode ter alt "
             "vazio de propósito; imagem que carrega informação, nunca."))

# ───────────────────────── PARTE D
P.append("""
<div class="newpage"></div>
<h2>Parte D · Checklist para imprimir</h2>
<h3>Onda 1 — higiene (dias, risco quase zero)</h3>
<table>
<tr><th style="width:6%">Feito</th><th style="width:8%">Tarefa</th><th>Ação</th><th style="width:16%">Responsável</th></tr>
<tr><td class="chk">☐</td><td>T1</td><td>CTA do PS deixa de apontar para o formulário de 2022.1</td><td>Marketing</td></tr>
<tr><td class="chk">☐</td><td>T5</td><td>Ocultar &ldquo;Compre agora&rdquo; e anunciar a próxima edição</td><td>Marketing</td></tr>
<tr><td class="chk">☐</td><td>T4</td><td>Religar os 3 CTAs dos casebooks</td><td>Marketing</td></tr>
<tr><td class="chk">☐</td><td>T6</td><td>Rodapé: &ldquo;© 2026&rdquo; e &ldquo;Todos os direitos reservados.&rdquo;</td><td>Marketing</td></tr>
<tr><td class="chk">☐</td><td>T7</td><td>Excluir <code>/blank-1</code> + 301; corrigir título de Getting the Job</td><td>Marketing</td></tr>
<tr><td class="chk">☐</td><td>T10</td><td>Ocultar <code>/eventos</code> do menu <i>e</i> da busca</td><td>Marketing</td></tr>
<tr><td class="chk">☐</td><td>T8</td><td>Desinstalar os 6 apps sem uso (confirmar com a diretoria)</td><td>Diretoria + Marketing</td></tr>
<tr><td class="chk">☐</td><td>T9</td><td>Excluir as 14 edições de evento residuais</td><td>Marketing</td></tr>
<tr><td class="chk">☐</td><td>—</td><td>Revisão ortográfica: &ldquo;tem têm&rdquo;, &ldquo;prepararam&rdquo;, &ldquo;Prepara-se&rdquo;, &ldquo;processo seletivos&rdquo;, &ldquo;os tema&rdquo;, &ldquo;Essas essas&rdquo;, &ldquo;Mastecard&rdquo;, &ldquo;Enterpreneurship&rdquo;, &ldquo;Engenhria&rdquo;</td><td>Marketing</td></tr>
<tr><td class="chk">☐</td><td>—</td><td>Corrigir &ldquo;4 opções&rdquo; na política e divulgar a taxa de 2,5% na página de preço</td><td>Diretoria</td></tr>
<tr><td class="chk">☐</td><td>—</td><td>Trocar &ldquo;14/jul&rdquo; por regra relativa e datar a política</td><td>Diretoria</td></tr>
<tr><td class="chk">☐</td><td>—</td><td>Publicar o desconto de grupo (40/50/60%) na página do curso</td><td>Marketing</td></tr>
</table>

<h3>Onda 2 — estrutura (semanas)</h3>
<table>
<tr><th style="width:6%">Feito</th><th style="width:8%">Tarefa</th><th>Ação</th><th style="width:16%">Responsável</th></tr>
<tr><td class="chk">☐</td><td>T2</td><td>Processo Seletivo no 1º nível do menu, slug semântico</td><td>Diretoria + Design</td></tr>
<tr><td class="chk">☐</td><td>T3</td><td>Renomear os 7 slugs <code>blank-*</code> + criar os 31 redirects</td><td>Marketing</td></tr>
<tr><td class="chk">☐</td><td>T13</td><td>Reescrever a página do CWC com datas, parceiros e CTA</td><td>Marketing</td></tr>
<tr><td class="chk">☐</td><td>T14</td><td>Cronograma como texto + ementa em 4 blocos + alt text</td><td>Design</td></tr>
<tr><td class="chk">☐</td><td>T11</td><td>Temas de Texto nas 5 páginas principais + 1 H1 por página</td><td>Design</td></tr>
<tr><td class="chk">☐</td><td>T12</td><td>Política de Privacidade + consentimento no mailing</td><td>Diretoria</td></tr>
<tr><td class="chk">☐</td><td>—</td><td>Reestruturar a home: H1, números (82 · 9,7 · 86 · 19), funil duplo</td><td>Design + Marketing</td></tr>
<tr><td class="chk">☐</td><td>—</td><td>Criar <code>/faq</code>, <code>/contato</code>, <code>/equipe</code>, <code>/parceiros</code></td><td>Marketing</td></tr>
<tr><td class="chk">☐</td><td>—</td><td>Preencher as 20 meta descriptions vazias</td><td>Marketing</td></tr>
<tr><td class="chk">☐</td><td>—</td><td>Recomprimir imagens &gt; 1 MB e PDFs do X-Ray (um tem 54,6 MB)</td><td>Design</td></tr>
<tr><td class="chk">☐</td><td>—</td><td>Conferir nome e cargo de cada pessoa em <code>/equipe</code></td><td>Diretoria</td></tr>
</table>

<h3>A cada edição do Prep4Consulting</h3>
<table>
<tr><th style="width:6%">Feito</th><th>Verificação</th></tr>
<tr><td class="chk">☐</td><td>Criar evento <b>novo</b> com slug limpo (<code>prep4consulting-2027-1</code>) — nunca duplicar</td></tr>
<tr><td class="chk">☐</td><td>Meta description <b>única</b>, até 155 caracteres</td></tr>
<tr><td class="chk">☐</td><td>Cronograma atualizado <b>como texto</b>, não como imagem nova</td></tr>
<tr><td class="chk">☐</td><td>Datas com <b>dia/mês/ano</b> completos, iguais no site e no LinkedIn</td></tr>
<tr><td class="chk">☐</td><td>Atualizar os 4 números da última edição (alunos · nota · NPS · cursos)</td></tr>
<tr><td class="chk">☐</td><td>Três cards de preço com o mesmo peso, incluindo <b>bolsista R$ 70,00</b></td></tr>
<tr><td class="chk">☐</td><td>Informar a taxa de serviço de 2,5% na página de preço</td></tr>
<tr><td class="chk">☐</td><td>Reexibir os botões de compra e conferir que apontam para o evento <b>novo</b></td></tr>
<tr><td class="chk">☐</td><td>Publicar &ldquo;Eventos&rdquo; no menu e reverter a ocultação da busca</td></tr>
<tr><td class="chk">☐</td><td>Conferir tudo no <b>editor mobile</b> antes de publicar</td></tr>
<tr><td class="chk">☐</td><td><b>No dia do fechamento:</b> ocultar botões, ocultar <code>/eventos</code>, trocar CTA por mailing</td></tr>
</table>

<h3>A cada troca de diretoria</h3>
<table>
<tr><th style="width:6%">Feito</th><th>Verificação</th></tr>
<tr><td class="chk">☐</td><td>Atualizar <code>/equipe</code>: nome, curso e cargo — <b>conferir um por um</b></td></tr>
<tr><td class="chk">☐</td><td>Mover quem saiu para <code>/alumni</code>, com empresa e cargo atuais</td></tr>
<tr><td class="chk">☐</td><td>Atualizar o ano do rodapé</td></tr>
<tr><td class="chk">☐</td><td>Criar o formulário do PS <b>do semestre</b> e conferir que não está em <code>closedform</code></td></tr>
<tr><td class="chk">☐</td><td>Substituir o e-book do PS pela edição vigente (o atual é de 2022.1)</td></tr>
<tr><td class="chk">☐</td><td>Repassar acessos: Wix, Drive dos materiais, e-mail institucional</td></tr>
<tr><td class="chk">☐</td><td>Registrar quem responde pelo site no semestre</td></tr>
</table>

<h3>Auditoria trimestral — 30 minutos</h3>
<table>
<tr><th style="width:6%">Feito</th><th>Verificação</th></tr>
<tr><td class="chk">☐</td><td>Abrir <code>/pages-sitemap.xml</code> e <code>/event-pages-sitemap.xml</code>: toda URL precisa ter dono e propósito. Se aparecer <code>blank-*</code>, <code>teste</code>, <code>old</code>, <code>cópia-*</code> ou <code>copy-of-*</code> &rarr; excluir + 301</td></tr>
<tr><td class="chk">☐</td><td>Nenhuma página publicada sem link de entrada (menu, rodapé ou outra página)</td></tr>
<tr><td class="chk">☐</td><td><b>Clicar em todos os CTAs.</b> Qualquer um que caia na home é link quebrado</td></tr>
<tr><td class="chk">☐</td><td>Nenhuma data passada apresentada como futura; nenhum contador em &ldquo;0 dias&rdquo;</td></tr>
<tr><td class="chk">☐</td><td>Abrir home, <code>/prep4consulting</code> e <code>/processo-seletivo</code> <b>no celular</b> e comparar com o desktop</td></tr>
<tr><td class="chk">☐</td><td>Testar links externos: Google Forms (não deve estar em <code>closedform</code>), Drive, PDFs</td></tr>
<tr><td class="chk">☐</td><td>Rodar o <b>Assistente de configuração de SEO</b> do Wix e zerar pendências</td></tr>
<tr><td class="chk">☐</td><td>Conferir se algum texto novo foi formatado à mão em vez de usar Temas de Texto</td></tr>
<tr><td class="chk">☐</td><td>Comparar o site com os últimos posts do LinkedIn: o que foi anunciado lá está no site?</td></tr>
</table>

<div class="alert" style="margin-top:6mm"><b>A regra que evita a recaída.</b> No Wix,
&ldquo;ocultar do menu&rdquo; &ne; &ldquo;ocultar da busca&rdquo; &ne; &ldquo;despublicar&rdquo; &ne;
&ldquo;excluir&rdquo;. Uma página oculta do menu continua publicada, no sitemap e no Google — foi assim
que o CCU acumulou 21 páginas órfãs. Quando a página deixa de servir: <b>exclua e crie o 301</b>.
E nunca duplique uma página ou um evento para criar a edição seguinte.</div>

<p class="small" style="margin-top:8mm">
<b>Procedência das informações.</b> Dados do site coletados por requisição HTTP direta às 44 URLs
indexáveis em 16/09/2026, com user-agent de desktop e de iPhone. Capturas de tela feitas com navegador
headless em 1440&times;1000. Contraste calculado pela fórmula de luminância relativa da WCAG 2.1 sobre os
valores da paleta do próprio site. Dados e imagens do LinkedIn recuperados da página pública da empresa.
Instagram não verificado — exige autenticação. Os diagramas D1 a D10 são ilustrações originais dos painéis
do Wix, não capturas do editor.</p>
""")

html = ("<!DOCTYPE html><html lang='pt-BR'><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>" + "".join(P) + "</body></html>")

hp = os.path.join(BASE, "pdf", "guia.html")
open(hp, "w", encoding="utf-8").write(html)
HTML(filename=hp, base_url=os.path.join(BASE, "pdf")).write_pdf(OUT)
print("PDF:", OUT, os.path.getsize(OUT) // 1024, "KB")
