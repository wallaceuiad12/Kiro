# Prompt completo para o Wix Harmony / Aria — site do CCU

Gera o site do Clube de Consultoria Universitário do zero, já com todas as melhorias da auditoria
aplicadas e com as fotos reais de eventos do clube.

---

## 0. Leia antes de colar (30 segundos que evitam retrabalho)

### O que o Harmony resolve e o que não resolve

`[FATO]` O Wix Harmony é o construtor de IA do Wix (sucessor do Wix ADI), e o **Aria** é o agente
dentro do editor. Segundo a documentação do Wix, o Aria cria site inteiro, gera página nova, redesenha
seção, escreve conteúdo, insere imagens e adiciona botões com link — e depois você ajusta à mão.

| O Harmony/Aria faz | O Harmony/Aria **não** faz — fica com você |
|---|---|
| Gerar as 25 páginas com estrutura, textos e seções | **Converter o site atual.** O site do CCU hoje é Wix Editor **clássico**; Harmony é outra arquitetura. Não existe conversão: é site novo. |
| Aplicar paleta, tipografia e estilos de botão | **Criar os 31 redirecionamentos 301.** Feito no painel do site que ficar com o domínio. |
| Escrever títulos e descrições de SEO | **Desinstalar os apps do site antigo** (Stores, Forum, Loyalty, Bookings, Members, Blog) |
| Inserir as fotos e escrever alt text | **Excluir as 14 páginas de evento residuais** no app Wix Events |
| Montar formulários | **Apontar o domínio** `consultoriaunicamp.com` para o site novo |
| — | **Saber os dados reais do clube.** Por isso eles estão escritos no prompt. |

> **Decisão que você precisa tomar antes:** este prompt cria um site **novo**. Se a escolha for
> consertar o site atual em vez de reconstruir, o documento certo é o
> `Guia-Execucao-Wix-CCU.pdf` — ele tem o caminho de clique no Editor clássico, tarefa por tarefa.
> Os dois caminhos levam ao mesmo destino; este é o mais rápido, e custa refazer o que já existe.

### Onde colar

Qualquer um dos três funciona:
1. **Wix Harmony** — criar site novo e colar o Prompt A no campo de descrição.
2. **ChatGPT com o app do Wix** — marcar `@wix` e colar o Prompt A.
3. **Aria, dentro do editor Harmony** — colar o Prompt A e depois os prompts da Parte B.

---

## 1. Preparação obrigatória: subir as fotos antes

O Aria insere imagens que estão no **Gerenciador de Mídia** do Wix. Ele não busca arquivo em URL do
GitHub. Então faça isto primeiro, senão ele preenche com banco de imagens genérico.

### 1.1 Baixe as 6 fotos utilizáveis

Estão no seu repositório, pasta `prints`. Links diretos:

```
https://raw.githubusercontent.com/wallaceuiad12/Kiro/add-prints-folder/prints/1760991748668.jpg
https://raw.githubusercontent.com/wallaceuiad12/Kiro/add-prints-folder/prints/1760991748872.jpg
https://raw.githubusercontent.com/wallaceuiad12/Kiro/add-prints-folder/prints/1761779524625.jpg
https://raw.githubusercontent.com/wallaceuiad12/Kiro/add-prints-folder/prints/1771088123226.jpg
https://raw.githubusercontent.com/wallaceuiad12/Kiro/add-prints-folder/prints/1771088123415.jpg
https://raw.githubusercontent.com/wallaceuiad12/Kiro/add-prints-folder/prints/1787747977006.jpg
```

### 1.2 Renomeie e suba com estes nomes e alt text

No **Gerenciador de Mídia**, crie a pasta `eventos-ccu` e suba com o nome novo. O nome importa: é
assim que você vai pedir a foto ao Aria.

| Nome original | Renomear para | O que a foto mostra | Alt text | Onde usar |
|---|---|---|---|---|
| `1771088123415.jpg` | `ccu-evento-bain-turma.jpg` | ~35 pessoas, tela "Be More at Bain" | Membros do CCU em evento na Bain & Company | **Hero da home** e `/parceiros` |
| `1787747977006.jpg` | `ccu-bain-logo.jpg` | 8 pessoas com o logo 3D Bain & Company, à noite | Membros do CCU no escritório da Bain & Company | `/parceiros`, prova de parceria |
| `1760991748668.jpg` | `cwc-mckinsey-broken-rung.jpg` | ~25 mulheres, telas "THE BROKEN RUNG / Construindo sua carreira com propósito" | Participantes do Consulting Women's Community na sessão sobre The Broken Rung | **Hero do `/consulting-womens-community`** |
| `1761779524625.jpg` | `cwc-do-campus-a-consultoria.jpg` | ~22 mulheres, tela "Do Campus à Consultoria" | Participantes do CWC em sessão com consultoria parceira | `/consulting-womens-community` |
| `1760991748872.jpg` | `cwc-networking.jpg` | 8 mulheres, escritório à noite, vista da cidade | Participantes do CWC em momento de networking | `/consulting-womens-community`, galeria |
| `1771088123226.jpg` | `ccu-evento-bain-retrato.jpg` | 10 pessoas, "Be More at Bain" (vertical) | Membros do CCU em evento na Bain & Company | Cartão de projeto, versão mobile |

**Não use** `CP20_PRO_20260911_220549.jpg` — é foto de uma lousa de microeconomia ("Ônus do
monopólio"), material de aula, não de evento.

### 1.3 Três ressalvas honestas sobre essas fotos

- `[FATO]` **Resolução baixa para hero.** As seis têm 800 px de largura. Em faixa de largura total
  ficam borradas. Peça os **originais** a quem fotografou — a única imagem em alta que você subiu
  (3264×2448) é a da lousa. Enquanto não tiver os originais, use as fotos em **cartões e galeria**,
  não em banner de largura total.
- `[HIPÓTESE]` **A edição do CWC não é certa.** As fotos não têm EXIF; datei pelo nome do arquivo
  (carimbo de WhatsApp), o que dá out/2025 para as do CWC e fev/2026 e ago/2026 para as da Bain. O
  post do clube coloca a sessão "The Broken Rung" com a McKinsey em 19/08/2026. **Confirme a edição
  com a diretoria antes de escrever legenda com ano** — legenda errada é o tipo de erro que a
  auditoria já apontou.
- **Direito de imagem e LGPD.** São pessoas identificáveis. Publicar exige consentimento de cada
  uma. E as fotos exibem marca de parceiros (Bain, McKinsey): usar isso no site sugere endosso —
  vale um aval do parceiro. Isso não é excesso de zelo: é o mesmo tema do achado de LGPD da auditoria.

---

## 2. PROMPT A — gerar o site do zero

> Copie tudo dentro do bloco. É autocontido: tem os dados reais, as regras de tom, a estrutura e as
> proibições. Se o campo do Harmony truncar, use a versão curta da Parte 4 e depois aplique a Parte B.

```
Crie o site institucional do Clube de Consultoria Universitário (CCU), organização estudantil da
Unicamp. Idioma: português do Brasil. Público: universitários e recém-formados que querem carreira em
consultoria estratégica.

=== IDENTIDADE ===
Nome: Clube de Consultoria Universitário (CCU)
Tagline oficial: "Da Unicamp para o Mundo"
Fundação: 2011 — 15 anos de atuação
Vínculo: organização gerida por alunos de graduação da Unicamp. IMPORTANTE: o CCU NÃO é órgão
oficial da universidade. Nunca escreva nada que sugira representação institucional da Unicamp.
CNPJ: 45.692.698/0001-91
Endereço: Cidade Universitária "Zeferino Vaz", Campinas - SP
E-mail: equipeccu@gmail.com
Redes: instagram.com/ccuclubedeconsultoria · linkedin.com/company/clube-de-consultoria-universitario

Missão: promover a carreira de consultoria no ambiente universitário; aproximar alunos da Unicamp de
grandes consultorias; preparar alunos para o ingresso na carreira.
Visão: ser o clube que mais aprova em consultorias estratégicas; potencializar a entrada de
universitários no mercado; atuar com excelência, adequando-se ao mercado.
Valores (cinco, sempre no plural): Capacidade Analítica, Criatividade, Determinação, Poder de
Comunicação, Trabalho em Equipe.

=== REGRAS DE ESCRITA (obrigatórias) ===
1. Resposta primeiro. Cada seção abre com a conclusão, depois o detalhe. É um clube que ensina
   comunicação estruturada: o site precisa demonstrar isso.
2. Uma ideia por bloco. Blocos MECE, sem sobreposição. Máximo 3 linhas por parágrafo.
3. Prova acima de adjetivo. Use os números desta lista. Não invente nenhum número que não esteja aqui.
4. Tom institucional sóbrio. PROIBIDO: "garanta sua vaga", "não perca tempo", "última chance",
   emoji em título, exclamação dupla, qualquer promessa de aprovação.
5. Datas sempre em dia/mês/ano completos. Nunca "14/jul" sem ano.
6. Português revisado. Concordância e pontuação corretas.
7. Uma frase = um bloco de texto. Nunca quebre frase ou palavra entre caixas.

=== DADOS REAIS (use estes; não invente outros) ===
Prep4Consulting, última edição encerrada (2026.1): 82 alunos · nota média 9,7 · NPS 86 ·
19 cursos de graduação distintos, com pelo menos um representante em exatas, humanas, biológicas e
sociais.
Rede alumni: 44 ex-membros, em BCG, Bain & Company, McKinsey & Company, Kearney, Oliver Wyman,
Accenture, Mubadala Capital, Peers, Pragmatis, Kea & Partners, Altman Solon, EloGroup, Advisia,
Google, Walmart, Shopee, Mercado Livre, XP, Itaú, Bradesco, BTG Pactual, P&G, AstraZeneca, Cielo,
Mastercard.
Consulting Women's Community: 3ª edição, 7 encontros, 7 consultorias parceiras.
Getting the Job: mais de 700 inscritos na 1ª edição.
X-Ray: 6 relatórios publicados, de 2014 a 2024.
Material gratuito: casebook próprio + banco com 15 casebooks de MIT, Harvard, Wharton, Kellogg,
Ross, Darden, ESADE, Illinois, NYU e Kearney.
LinkedIn: 1.854 seguidores.

=== ESTRUTURA: 8 itens de menu, nesta ordem ===
Os dois funis (virar membro × virar aluno do curso) têm de estar visíveis na entrada. Hoje o maior
defeito do site é esconder o Processo Seletivo.

1. Processo Seletivo   -> /processo-seletivo
2. Prep4Consulting     -> /prep4consulting
3. Sobre nós           -> /sobre-nos   [submenu: Equipe /equipe · Alumni /alumni · Parceiros /parceiros]
4. Projetos            -> /projetos    [submenu: X-Ray /x-ray · Consulting Women's Community
                          /consulting-womens-community · Getting the Job /getting-the-job]
5. Conteúdo            -> /conteudo     [submenu: Entrevista /entrevista · Revisão das Indústrias
                          /revisao-industrias · Framework /framework · Guesstimate /guesstimate ·
                          Casebooks /casebooks]
6. FAQ                 -> /faq
7. Contato             -> /contato
8. Mailing             -> /mailing

Fora do menu, linkadas no rodapé: /politica-troca e /politica-privacidade.
Slugs sempre em ASCII minúsculo com hífen. Nunca use slug genérico tipo "blank-1", "pagina-2" ou
"copia-de-home".

=== HOME: 6 seções, nesta ordem ===
S1 HERO — um único H1: "Preparamos universitários para os processos seletivos das principais
consultorias estratégicas". Subtítulo com a tagline "Da Unicamp para o Mundo. Desde 2011."
Imagem de fundo: ccu-evento-bain-turma.jpg (alt: "Membros do CCU em evento na Bain & Company").
Dois botões lado a lado, mesmo peso: primário "Quero entrar no Clube" -> /processo-seletivo;
secundário "Quero fazer o curso" -> /prep4consulting.

S2 NÚMEROS — faixa com 4 cartões, número grande + rótulo curto:
82 Alunos na última edição · 9,7 Nota média · 86 NPS · 19 Cursos de graduação.
Legenda abaixo: "Prep4Consulting, edição 2026.1."

S3 FUNIL DUPLO — dois cartões irmãos, mesmo tamanho:
Cartão A "Seja membro do CCU": treinamentos e cases semanais, projetos, contato com consultorias.
Status do Processo Seletivo e prazo em dia/mês/ano. Botão -> /processo-seletivo.
Cartão B "Faça o Prep4Consulting": curso preparatório intensivo, módulos com consultorias parceiras.
Status das inscrições e prazo em dia/mês/ano. Botão -> /prep4consulting.

S4 PROVA SOCIAL — "Onde estão nossos alumni": 6 logos (BCG, Bain, McKinsey, Kearney, Oliver Wyman,
Accenture) + frase "44 ex-membros do CCU atuam em consultorias estratégicas e grandes empresas."
Botão secundário -> /alumni.

S5 CONTEÚDO GRATUITO — 3 cartões: "Trilha de preparação" -> /conteudo; "15 casebooks" -> /casebooks;
"Relatório X-Ray" -> /x-ray. Nenhum exige cadastro.

S6 PARCEIROS — grade de logos em altura uniforme + uma frase sobre o que a parceria envolve.
Botão secundário -> /parceiros.

Regra: exatamente UM botão primário por seção. Não repita o mesmo CTA duas vezes na mesma seção.

=== DESIGN ===
Tipografia — só duas famílias, definidas nos temas de texto (nunca formatação por caixa):
  Títulos: Brandon Grotesque Light (alternativa: Montserrat Light)
  Corpo: Avenir LT 35 Light (alternativa: Inter Light)
  Seis estilos apenas: Título 1 44px · Título 2 32px · Título 3 24px · Corpo 18px ·
  Corpo destaque 20px · Legenda 14px.

Paleta — exatamente 6 cores:
  Marca:          #C1272D (vermelho)
  Marca escura:   #811A1E (hover, estados ativos)
  Fundo claro:    #FBFAFA
  Texto:          #181818
  Texto 2º:       #515151
  Branco:         #FFFFFF

REGRA DE CONTRASTE (não negocie): a cor depende do fundo da seção.
  Fundo claro #FBFAFA -> texto #181818 (17,0:1) ou #515151 (7,6:1); destaque #C1272D (5,6:1).
  Fundo escuro #181818 -> texto #FBFAFA. NUNCA #C1272D sobre #181818 (3,0:1, reprova WCAG AA).
  Botão primário: fundo #C1272D com texto #FFFFFF (5,8:1). Hover: #811A1E.
  NUNCA use cinza claro (#C2C2C2, #898989) nem rosa (#EAACAE, #D68084) como texto em fundo claro.

Botões: dois estilos só. Primário = preenchido #C1272D, texto branco, canto 4px.
Secundário = contorno #C1272D, fundo transparente.

Layout: fundo claro, muito espaço em branco, ritmo vertical constante, seções separadas por respiro
generoso. Visual sóbrio e analítico, sem gradiente chamativo, sem animação decorativa.

=== SEO E ACESSIBILIDADE (aplicar em toda página) ===
- Exatamente um H1 por página, igual ao assunto da página. H2 para seções, H3 para subitens.
  NUNCA use heading em preço, rótulo, nota de rodapé ou asterisco.
- Título de SEO com até 60 caracteres, sufixo padrão " | CCU" em todas as páginas.
- Meta description com até 155 caracteres, única por página, nenhuma vazia.
- Toda imagem com alt descritivo. Nunca use o nome do arquivo como alt.
- Nenhum texto dentro de imagem: data, preço e cronograma sempre como texto real.

=== RODAPÉ (global) ===
Cidade Universitária "Zeferino Vaz", Campinas - SP · CNPJ: 45.692.698/0001-91 ·
equipeccu@gmail.com · links para Política de Troca e Política de Privacidade ·
"© 2026 Clube de Consultoria Universitário. Todos os direitos reservados."
O CNPJ e o endereço devem aparecer também no mobile.

=== NÃO FAÇA ===
- Não crie página de loja, fórum, programa de fidelidade, agendamento, área de membros nem blog.
  Se não houver conteúdo real, a página não existe.
- Não crie página de "manutenção", "em breve", rascunho ou cópia.
- Não deixe nenhuma página sem link de entrada a partir do menu, do rodapé ou de outra página.
- Não repita o mesmo título de SEO em duas páginas.
- Não escreva "0 dias para o evento", contador, ou data passada como se fosse futura.
- Não prometa aprovação em processo seletivo.
- Não coloque preço ou data dentro de imagem.
```

---

## 3. PROMPTS B — refinar com o Aria, página por página

Depois que o site nascer, cole um por vez no chat do Aria. Ordem importa: a home primeiro.

### B1 · Processo Seletivo — o funil que hoje está invisível

```
Na página /processo-seletivo, monte estas seções:
H1: "Seja membro do Clube de Consultoria Universitário"
Abertura em uma frase: o que o membro faz e o que recebe.
Seção "Por que fazer parte", 4 cartões: Capacitação (treinamentos e cases semanais);
Projetos em diferentes áreas; Exposição a desafios (liderar projeto desde os primeiros meses);
Networking (contato com consultorias e outras organizações estudantis).
Seção "Etapas do processo", como lista numerada, cada etapa com uma linha de descrição.
Seção "Prazos": inscrições de [DIA/MÊS/ANO] a [DIA/MÊS/ANO]. Deixe os campos marcados para eu
preencher — não invente datas.
Um único botão primário. Se as inscrições estiverem abertas: "Inscrever-se", apontando para o
formulário. Se estiverem fechadas: "Avise-me quando abrir", apontando para /mailing, com a frase
"As inscrições da edição atual foram encerradas em [DATA]. As próximas abrem em [MÊS/ANO]."
Tom institucional. Não use "garanta sua vaga" nem "não perca tempo".
```

### B2 · Prep4Consulting — com o cronograma como texto

```
Na página /prep4consulting, crie a seção "Cronograma" como TABELA DE TEXTO, não como imagem.
Use exatamente estes dados da edição 2026.2, com a consultoria responsável por módulo:

20/07 seg — 18h Prep 101 + Consulting 101 · 20h Fit + Screening — McKinsey & Company
21/07 ter — 18h Screening · 20h GMAT: Estrutura da prova
22/07 qua — 18h GMAT: Problem Solving · 20h GMAT: Data Sufficiency
23/07 qui — 18h GMAT: Critical Reasoning · 20h Fit + Screening
24/07 sex — 18h GMAT · 20h Framework — BCG
25/07 sáb — 10h Finanças · 13h Dinâmica em Grupo + Fit
27/07 seg — 18h Dinâmica em grupo · 20h Case Interview — EloGroup
28/07 ter — 18h Case Interview · 20h Guesstimate — Kearney
29/07 qua — 18h Estratégia · 20h Crack the case Harvard — Visagio
30/07 qui — 18h Crack the case GBP — BTC
31/07 sex — 18h Crack the case — Bain & Company

Acrescente a seção "Ementa" com quatro blocos, um por ciclo, cada um em um único elemento de texto:
Ciclo 1: Prep 101, Consulting 101, Screening, Estrutura do PS
Ciclo 2: GMAT (Estrutura da prova, Problem Solving, Data Sufficiency, Critical Reasoning),
         Business Case Test
Ciclo 3: Finanças, Framework, Fit Interview, Case Interview, Guesstimate, Estratégia para Cases
Ciclo 4: Wrap up
Grafia padronizada: "Consulting 101", "Fit Interview", "Case Interview".

Seção "Investimento" com TRÊS cartões de mesmo tamanho e mesmo peso visual:
  Bolsista — R$ 70,00 — "Mediante comprovação de auxílio vigente, enviada para equipeccu@gmail.com"
  Estudante — R$ 189,99 — "Matriculados em instituição de ensino"
  Formado — R$ 239,99 — "Já formados em instituição de ensino"
Em legenda, abaixo dos três: "Acrescem 2,5% de taxa de serviço no ato da inscrição."
O cartão de bolsista tem o MESMO destaque dos outros dois. Não o coloque como nota de rodapé.

Seção "Desconto para grupos", lista: 4 a 7 pessoas 40% · 8 a 12 pessoas 50% · 13 ou mais 60%.
Como funciona, em 4 passos: montar o grupo; um integrante envia nomes e e-mails para
equipeccu@gmail.com; a equipe envia um cupom; usar o cupom na inscrição.

Seção "Resultados da última edição (2026.1)": 82 alunos · nota média 9,7 · NPS 86 ·
19 cursos de graduação.

Seção "Como funciona": aulas ao vivo por Zoom, gravadas e disponibilizadas, exceto os módulos com
consultoria parceira; acesso a turma no Google Classroom com material extra e simulados; grupo de
WhatsApp com avisos de processos seletivos.

Um único botão primário. Se as inscrições estiverem fechadas, ele aponta para /mailing com o texto
"Avise-me da próxima edição" — nunca deixe botão de compra ativo fora do período de inscrição.
```

### B3 · Consulting Women's Community — a página mais fraca vira uma das melhores

```
Na página /consulting-womens-community:
H1: "Consulting Women's Community (CWC)"
Use este nome exato em todo o site — título, texto e slug. Não escreva "Consulting Women's
Consulting".
Abertura em uma frase: comunidade do CCU para mulheres que querem carreira em consultoria, com
capacitação, mentoria e rede.
Faixa de números: 3ª edição · 7 encontros · 7 consultorias parceiras.
Imagem principal: cwc-mckinsey-broken-rung.jpg
(alt: "Participantes do Consulting Women's Community na sessão sobre The Broken Rung").
Galeria com cwc-do-campus-a-consultoria.jpg e cwc-networking.jpg.

Seção "Programação da 3ª edição" como TABELA DE TEXTO (data · horário · consultoria · tema):
19/08 qua 19h30 — McKinsey & Company — "The Broken Rung": como atingir seu maior potencial
26/08 qua 19h30 — Accenture — Trilha de vida e carreira
02/09 qua 19h30 — Kearney — Problem Solving em ambientes competitivos
09/09 qua 19h30 — Roland Berger — Visão estratégica e atualidades de mercado
16/09 qua 19h30 — Bain & Company — Crescimento de alta performance e liderança feminina
23/09 qua 19h30 — Peers — Tech, IA e consultoria estratégica
24/09 qui 19h00 — BCG — Roda de conversa e encerramento (presencial)
Confirme o ano da edição comigo antes de publicar.

Um botão primário: inscrição quando aberta, ou /mailing quando fechada.
A página precisa ter uma porta de entrada. Hoje ela não tem nenhuma.
```

### B4 · FAQ — a lacuna estrutural

```
Crie /faq com acordeão, perguntas numeradas, agrupadas em três categorias:
"A carreira de consultoria" — o que é consultoria estratégica; como perfis de diferentes cursos se
encaixam; como são os processos seletivos; plano de carreira; rotina de trabalho; remuneração e
benefícios.
"O Clube" — o que é o CCU e desde quando existe; quem pode participar; qual o compromisso de tempo;
o que o membro faz na prática; como funcionam os projetos.
"Processo Seletivo e Prep4Consulting" — quando abrem as inscrições; quais as etapas; o curso é só
para alunos da Unicamp (não: é aberto ao público); como funciona o desconto para bolsista; como
funciona o desconto de grupo; qual a política de reembolso.
Respostas de 2 a 4 linhas, diretas, sem hype. Um H1 só na página; as perguntas são H3.
```

### B5 · Equipe, Alumni e Parceiros

```
Crie /equipe com uma grade de cartões idênticos, um por pessoa, cada cartão com exatamente quatro
campos na mesma ordem: foto, nome, curso de graduação, cargo. Use um componente repetido para que
todos fiquem iguais. Deixe os campos vazios para eu preencher — não invente nomes.
Regra: um nome, um curso e um cargo por pessoa, sem duplicar e sem cargo solto entre dois nomes.

Crie /alumni com os 44 ex-membros agrupados em categorias mutuamente exclusivas:
Ex-presidentes · Ex-vice-presidentes · Ex-diretores · Ex-membros.
Não crie "Presidentes anteriores" e "Ex-presidentes" como categorias separadas: é a mesma coisa.
Cada pessoa: nome, empresa atual, cargo atual. Grafia correta: Mastercard, AstraZeneca,
Entrepreneurship. Os nomes não são títulos: use texto normal, não H1.

Crie /parceiros com: uma frase sobre o que a parceria envolve; grade de logos com a MESMA altura e
fundo transparente, cada um com alt igual ao nome da empresa; seção "O que oferecemos ao parceiro"
(módulo no Prep4Consulting, presença no CWC, acesso ao relatório X-Ray, divulgação de processos
seletivos); e um contato para novas parcerias.
Imagens: ccu-bain-logo.jpg e ccu-evento-bain-turma.jpg.
```

### B6 · Conteúdo — religar a trilha que hoje quebra no fim

```
Em /conteudo, monte a trilha de preparação como 5 passos numerados, em ordem, cada um com link:
1. Entrevista (fit e case) -> /entrevista
2. Revisão das Indústrias -> /revisao-industrias
3. Frameworks -> /framework
4. Guesstimates -> /guesstimate
5. Casebooks e cases completos -> /casebooks
Todo cartão precisa apontar para a página correspondente. Nenhum "Ver mais" pode apontar para a home.
Ao fim de cada uma dessas páginas, coloque um link para o passo seguinte da trilha; na página
/guesstimate o próximo passo é /casebooks.

Crie /casebooks com dois cartões: "Casebook do CCU" -> /casebook-ccu e "Banco de casebooks"
-> /banco-de-casebooks.
Em /banco-de-casebooks, liste os 15 casebooks por instituição e ano: MIT 2015; Darden 2012; Darden
2019; ESADE 2011; ESADE 2014; Harvard 2011; Illinois 2016; Kearney; Kellogg 2012; NYU 2015;
Ross 2008; Ross 2011; Ross 2016; Wharton 2008; Wharton 2017.
Avise em legenda quando o arquivo passar de 10 MB.
Todo o conteúdo é gratuito e sem cadastro.
```

### B7 · Contato, Mailing e Privacidade (LGPD)

```
Crie /contato com: e-mail equipeccu@gmail.com, prazo de resposta ("respondemos em até 3 dias
úteis"), links de Instagram e LinkedIn, e um formulário curto (nome, e-mail, assunto, mensagem) com
a finalidade declarada acima dele. A página precisa estar no menu.

Em /mailing, o formulário deve ter: nome, e-mail e interesse. Regras:
- Campo de gênero é OPCIONAL, com a finalidade escrita ao lado ("usamos para medir a diversidade do
  público e desenhar o CWC").
- Não peça data de nascimento.
- Inclua caixa de consentimento obrigatória antes do botão, com link para a Política de Privacidade.
- Texto sem erro: "programas, treinamentos e processos seletivos".

Crie /politica-privacidade cobrindo: controlador (Clube de Consultoria Universitário, CNPJ
45.692.698/0001-91), quais dados são coletados, finalidade de cada um, base legal (consentimento),
prazo de retenção, com quem são compartilhados, e como pedir acesso ou exclusão (e-mail).
Linke no rodapé de todas as páginas.

Crie /politica-troca com prazo RELATIVO, não data fixa: "o cancelamento pode ser solicitado até 3
dias antes do início das aulas da edição contratada, cuja data consta na página da edição".
Informe que a taxa de serviço de 2,5% não é reembolsada, e o número correto de opções de inscrição.
Acrescente "Versão vigente desde 09/2026".
```

### B8 · Revisão final — peça ao Aria para auditar o que ele criou

```
Faça uma revisão do site inteiro e me liste o que encontrar:
1. Páginas com mais de um H1, ou sem nenhum H1.
2. Páginas sem meta description, ou com mais de 155 caracteres.
3. Títulos de SEO repetidos entre páginas, ou com mais de 60 caracteres.
4. Imagens sem alt, ou com o nome do arquivo como alt.
5. Páginas sem nenhum link de entrada a partir do menu, do rodapé ou de outra página.
6. Botões e links cujo destino seja a home quando deveriam apontar para uma página específica.
7. Textos com data sem ano, ou data passada apresentada como futura.
8. Pares de cor que reprovem contraste WCAG AA (4,5:1 para texto).
9. Seções com mais de um botão primário.
10. Qualquer preço, prazo ou cronograma que esteja dentro de imagem em vez de texto.
Depois confira se tudo aparece corretamente também no mobile.
```

---

## 4. Versão curta do Prompt A (se o campo truncar)

```
Crie o site do Clube de Consultoria Universitário (CCU), organização estudantil da Unicamp fundada
em 2011, tagline "Da Unicamp para o Mundo". Português do Brasil. Tom institucional sóbrio, sem hype,
sem promessa de aprovação, datas sempre com dia/mês/ano.

8 páginas no menu, nesta ordem: Processo Seletivo (/processo-seletivo), Prep4Consulting
(/prep4consulting), Sobre nós (/sobre-nos, com Equipe, Alumni e Parceiros), Projetos (/projetos, com
X-Ray, Consulting Women's Community e Getting the Job), Conteúdo (/conteudo, com Entrevista, Revisão
das Indústrias, Framework, Guesstimate e Casebooks), FAQ (/faq), Contato (/contato), Mailing
(/mailing). No rodapé: Política de Troca e Política de Privacidade.

Home com 6 seções: (1) hero com um H1 "Preparamos universitários para os processos seletivos das
principais consultorias estratégicas" e dois botões de mesmo peso, "Quero entrar no Clube" e "Quero
fazer o curso"; (2) faixa com 4 números: 82 alunos, nota 9,7, NPS 86, 19 cursos de graduação;
(3) dois cartões irmãos, um por funil, cada um com prazo; (4) alumni com 6 logos e a frase "44
ex-membros em consultorias estratégicas"; (5) três cartões de conteúdo gratuito; (6) grade de
parceiros.

Design: duas fontes só (Brandon Grotesque Light em títulos, Avenir LT 35 Light no corpo), seis
estilos de texto (44/32/24/20/18/14px). Paleta de seis cores: #C1272D marca, #811A1E hover, #FBFAFA
fundo, #181818 texto, #515151 texto secundário, #FFFFFF. Em fundo claro nunca use #C1272D como
texto pequeno nem cinza claro; em fundo escuro nunca use #C1272D. Dois estilos de botão apenas.
Fundo claro, muito espaço em branco, visual sóbrio.

Um H1 por página, título de SEO até 60 caracteres com sufixo " | CCU", meta description até 155,
alt descritivo em toda imagem. Nenhuma data, preço ou cronograma dentro de imagem.

Não crie loja, fórum, fidelidade, agendamento, área de membros nem blog. Não crie página de
manutenção, rascunho ou cópia. Nenhuma página sem link de entrada.

Rodapé: Cidade Universitária "Zeferino Vaz", Campinas - SP; CNPJ 45.692.698/0001-91;
equipeccu@gmail.com; "© 2026 Clube de Consultoria Universitário. Todos os direitos reservados."
```

---

## 5. O que fazer à mão — o Aria não faz

| # | Tarefa | Onde | Por quê |
|---|---|---|---|
| 1 | Criar os **31 redirecionamentos 301** | Painel → SEO → Redirecionamentos de URL | Ao trocar de site, todo link já compartilhado (`/blank-6`, `/prep4consulting-2026-2`, as 14 páginas de evento) quebra. A lista completa está na seção 8.1 do `RELATORIO-CCU.md`. |
| 2 | **Apontar o domínio** `consultoriaunicamp.com` para o site novo | Painel → Domínios | Sem isso o site novo nasce em endereço `wixsite.com` e o antigo continua no ar. |
| 3 | **Desinstalar os apps** do site antigo: Stores, Forum, Loyalty, Bookings, Members, Blog | Painel do site antigo → Apps | Ocultar página não basta: ela continua publicada e indexável. |
| 4 | **Excluir as 14 páginas de evento** residuais, incluindo as chamadas "teste" | Painel → Eventos | Duas estão indexadas no Google com o título "teste". |
| 5 | **Recriar o evento de venda** do curso no Wix Events, com slug limpo | Painel → Eventos | Nunca duplique evento antigo: foi assim que a edição 2026.1 foi morar no slug `prep4consulting-2025-2-1-1`. |
| 6 | **Substituir o formulário do PS** | Google Forms | O link atual aponta para o "Formulário de Inscrição PS Interno CCU 2022.1", que está fechado. |
| 7 | **Subir o casebook do CCU** e conferir que o botão entrega arquivo | Gerenciador de Mídia | Hoje o CTA "CONFIRA" não entrega nada. |
| 8 | **Conseguir os originais das fotos** em alta resolução | com quem fotografou | As seis disponíveis têm 800 px: insuficiente para banner. |
| 9 | **Consentimento de imagem** das pessoas fotografadas e aval dos parceiros | diretoria | Pessoas identificáveis e marcas de terceiros. |
| 10 | **Conferir nome, curso e cargo** de cada pessoa em `/equipe` | diretoria | Foi o erro mais sensível da auditoria: cargos atribuídos à pessoa errada. |

---

## 6. Verificação: como saber que ficou pronto

Rode isto depois de publicar. Se algum item falhar, o site repetiu um defeito do anterior.

| Verificação | Como conferir | Esperado |
|---|---|---|
| Nenhuma página órfã | Clicar em tudo a partir do menu e do rodapé | Toda página alcançável |
| Nenhum CTA caindo na home | Clicar em todos os botões | Nenhum volta para `/` |
| Um H1 por página | Abrir `/sitemap.xml` e checar página por página | Exatamente 1 |
| Nenhum slug genérico | Abrir `/pages-sitemap.xml` | Zero `blank-*`, `copia-*`, `teste`, `old` |
| Nenhum título repetido | Comparar os títulos de SEO | Todos únicos |
| Descrições preenchidas | Página por página | Nenhuma vazia, nenhuma acima de 155 |
| Dois funis visíveis na home | Abrir a home | Botão de PS e botão de curso, mesmo peso |
| Números na home | Abrir a home | 82, 9,7, 86 e 19 visíveis |
| Datas completas | Buscar por "/" em datas | Sempre com ano |
| Cronograma em texto | Selecionar o texto do cronograma com o cursor | Selecionável, não é imagem |
| Bolsista com mesmo destaque | Abrir `/prep4consulting` | Três cartões de tamanho igual |
| Rodapé correto | Qualquer página, desktop e mobile | "© 2026", "Todos os direitos reservados.", CNPJ visível nos dois |
| Privacidade acessível | Rodapé | Link presente em todas as páginas |
| Contraste | Verificador de contraste WCAG | Todo texto ≥ 4,5:1 |
| Mobile igual ao desktop | Abrir as 3 páginas principais no celular | Mesmo conteúdo, mesma ordem |

---

## 7. Procedência

`[FATO]` Dados do clube extraídos do site (44 URLs, coleta de 16/09/2026) e do LinkedIn público do
CCU. Cronograma do Prep4Consulting e programação do CWC transcritos das peças publicadas pelo próprio
clube. Números 82 / 9,7 / 86 / 19 constam da página do curso. Contrastes calculados pela fórmula de
luminância relativa da WCAG 2.1.
`[FATO]` Capacidades do Harmony e do Aria conforme a documentação e o blog oficiais do Wix.
`[HIPÓTESE]` A edição do CWC a que cada foto pertence — as fotos não têm EXIF e foram datadas pelo
carimbo do nome do arquivo. Confirmar com a diretoria.
**Não verificado:** Instagram do clube (exige autenticação); comportamento do Harmony com o volume
deste prompt específico; se o campo de entrada tem limite de caracteres.
