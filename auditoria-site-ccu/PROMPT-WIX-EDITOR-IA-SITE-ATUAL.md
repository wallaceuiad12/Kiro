# Prompts para a IA do Wix Editor — corrigir o site atual do CCU

Para usar **no site que já existe** (`consultoriaunicamp.com`), sem reconstruir nada.
Complementa o `Guia-Execucao-Wix-CCU.pdf`, que tem a parte manual.

---

## 0. A limitação que define tudo aqui

`[FATO]` Segundo a documentação do Wix, no **Editor clássico** — que é o caso do CCU — você desenha
manualmente e usa **AI Tools para fins específicos**, como gerar ou editar texto e imagem. A IA do
Editor clássico **não conduz a edição** como o Aria faz no Harmony.

Traduzindo para este projeto:

| A IA do Editor faz | A IA do Editor **não** faz |
|---|---|
| Reescrever o texto de uma caixa (tom, tamanho) | Criar, excluir ou renomear página |
| Gerar título e descrição de SEO por página | Mudar slug (`/blank-6` → `/processo-seletivo`) |
| Sugerir texto alternativo de imagem | Criar os 31 redirecionamentos 301 |
| Melhorar, recortar e limpar imagem | Reorganizar o menu |
| Gerar texto novo para uma seção | Trocar o destino de um botão |
| — | Desinstalar app · excluir evento antigo |
| — | Consertar a divergência desktop/mobile |

> **Portanto:** os prompts abaixo cobrem **texto, SEO e imagem** — que é a maior parte do volume de
> trabalho da auditoria. As tarefas estruturais estão na seção 6, e o caminho de clique de cada uma
> está no PDF. Nenhum prompt vai resolver o 301; isso é botão, não conversa.

### Onde ficam as ferramentas

| Ferramenta | Caminho |
|---|---|
| **IA de texto** | Clicar na caixa de texto → **Editar texto** → ícone de IA / **Criar texto com IA** |
| **IA de SEO** | **Menus e Páginas** → engrenagem da página → **SEO básico** → **Criar com IA** |
| **Texto alternativo** | Clicar na imagem → **Configurações** → **Texto alternativo** |
| **Melhorar imagem** | Clicar na imagem → **Configurações de imagem** → **Ajustar / Aperfeiçoar** |

### Como usar cada bloco

Cada item traz **o prompt** (para a IA gerar) e **o texto final** (para colar direto). Se a IA
inventar número, mudar o tom ou encher de adjetivo, ignore e cole o texto final — ele já está
conforme as regras do clube. É mais rápido e não erra dado.

---

## 1. Prompt de contexto — cole isto primeiro, em toda sessão de IA

A IA do Editor não guarda contexto entre caixas. Cole este bloco antes de cada pedido, ou mantenha-o
aberto para copiar junto.

```
Contexto: escrevo para o site do Clube de Consultoria Universitário (CCU), organização estudantil
da Unicamp fundada em 2011, que promove a carreira de consultoria estratégica e prepara alunos para
processos seletivos. Tagline: "Da Unicamp para o Mundo".

Regras de escrita, obrigatórias:
- Resposta primeiro: a conclusão abre o texto, o detalhe vem depois.
- Uma ideia por bloco. Parágrafo com no máximo 3 linhas.
- Tom institucional sóbrio. PROIBIDO: "garanta sua vaga", "não perca tempo", "última chance",
  "imperdível", emoji, exclamação dupla, e qualquer promessa de aprovação.
- Datas sempre com dia, mês e ano. Nunca "14/jul".
- Não invente número, data, nome de empresa nem depoimento. Use só o que eu fornecer.
- Português do Brasil revisado, concordância e pontuação corretas.
- O CCU não é órgão oficial da Unicamp: nunca escreva nada que sugira representação institucional.
```

---

## 2. Correções de texto, bloco por bloco

### 2.1 Rodapé global — aparece nas 44 páginas

Duas falhas repetidas no site inteiro: `©2023` e a frase quebrada
*"Todos os seus são direitos reservados"*.

```
Reescreva este rodapé corrigindo a gramática e o ano, mantendo todos os dados cadastrais:
"Cidade Universitária "Zeferino Vaz", Campinas - SP · CNPJ: 45.692.698/0001-91 · ©2023 Clube de
Consultoria Universitário · Todos os seus são direitos reservados · Contato: equipeccu@gmail.com"
Mantenha endereço, CNPJ e e-mail exatamente como estão. Corrija só o ano para 2026 e a frase final.
```

**Texto final:**
> Cidade Universitária "Zeferino Vaz", Campinas – SP · CNPJ: 45.692.698/0001-91
> Contato: equipeccu@gmail.com
> Política de Troca, Devolução e Reembolso · Política de Privacidade
> © 2026 Clube de Consultoria Universitário. Todos os direitos reservados.

*Depois de editar, abra o **editor mobile**: hoje o CNPJ não aparece no celular.*

---

### 2.2 Home — o título que não existe

A home hoje tem **zero `<h1>`** e abre com uma saudação. Precisa abrir com o que o clube faz.

```
Escreva o título principal da home de um clube universitário de consultoria. Uma frase, no máximo
90 caracteres, dizendo o que o clube faz pelo visitante — não uma saudação. Depois, um subtítulo de
uma linha com a tagline e o ano de fundação (2011). Tom institucional, sem exclamação.
```

**Texto final:**
> **H1:** Preparamos universitários para os processos seletivos das principais consultorias estratégicas
> **Subtítulo:** Da Unicamp para o Mundo. Desde 2011.

*Marque o H1 como **Título 1** pelos Temas de Texto — não aumente a fonte à mão.*

---

### 2.3 Home — os três parágrafos corridos

O texto atual tem 408 palavras em parágrafos densos, com dois erros: *"os projetos **tem têm** como
objetivo"* e *"os projetos externos, **prepararam** pessoas externas"*.

```
Reescreva o texto abaixo em no máximo 90 palavras, em 3 blocos curtos com subtítulo próprio.
Corrija os erros de português. Cada bloco com uma ideia só. Sem adjetivo desnecessário.

"O Clube de Consultoria Universitário (CCU) é uma organização voltada para o desenvolvimento de
indivíduos interessados na área de consultoria, principalmente no ambiente universitário. Assim, os
projetos tem têm como objetivo principal fornecer treinamento e capacitação intensiva para os
estudantes engajados em ingressar nessa área. A partir dos projetos internos, os membros são
capacitados no que diz respeito à carreira de consultoria. Por outro lado, os projetos externos,
prepararam pessoas externas à organização."
```

**Texto final:**
> **O que fazemos**
> Formamos universitários interessados em consultoria estratégica, com treinamento intensivo e
> contato direto com as consultorias do setor.
>
> **Projetos internos**
> Capacitam os membros do Clube em cada etapa do processo seletivo de consultoria.
>
> **Projetos externos**
> Preparam candidatos de fora do Clube: Prep4Consulting, X-Ray, Consulting Women's Community e
> Getting the Job.

---

### 2.4 Home — a faixa de números que não existe

O clube tem os dados e não os usa. Esta seção é nova: crie 4 caixas de texto.

**Texto final** (não precisa de IA, é dado):
> **82** Alunos na última edição · **9,7** Nota média · **86** NPS · **19** Cursos de graduação
> *Legenda:* Prep4Consulting, edição 2026.1.

---

### 2.5 Página do Processo Seletivo (`/blank-6`) — o pior texto do site

Hoje diz *"Não perca tempo! Garanta sua vaga no PS!"* — exatamente o hype que a política do clube
proíbe. E o botão aponta para o formulário do **PS 2022.1**, fechado.

```
Reescreva a chamada de uma página de processo seletivo de clube universitário. O texto atual é
"O Clube está em busca de Novos Membros — Não perca tempo! Garanta sua vaga no PS!".
Remova todo o tom de urgência e de venda. Escreva em tom institucional, dizendo o que o candidato
encontra no Clube. Máximo 40 palavras. Depois escreva um aviso de inscrições encerradas, com espaço
para eu inserir as datas.
```

**Texto final:**
> **H1:** Seja membro do Clube de Consultoria Universitário
>
> No CCU você participa de treinamentos e cases semanais, conduz projetos e tem contato direto com
> consultorias estratégicas.
>
> **Status:** As inscrições do Processo Seletivo 2026.2 foram encerradas em 07/09/2026.
> As próximas abrem em [MÊS/ANO].
>
> **Botão:** Avise-me quando abrir → `/mailing`

*O botão precisa ser reapontado à mão — a IA não troca link.*

---

### 2.6 Página do curso — preços com o bolsista em pé de igualdade

Hoje o desconto de bolsista está num parágrafo no fim da seção; a taxa de serviço não é informada;
e o desconto de grupo (até 60%) não existe no site, só no LinkedIn.

```
Escreva a seção de investimento de um curso preparatório, com três opções de mesmo peso visual,
cada uma com valor, uma linha de quem se aplica, e nada mais. Depois uma legenda única sobre taxa
de serviço. Sem urgência, sem "aproveite". Dados:
Bolsista R$ 70,00 (mediante comprovação de auxílio vigente por e-mail); Estudante R$ 189,99
(matriculados em instituição de ensino); Formado R$ 239,99 (já formados). Taxa de serviço de 2,5%
cobrada na inscrição.
```

**Texto final:**
> **Bolsista — R$ 70,00**
> Mediante comprovação de auxílio vigente, enviada para equipeccu@gmail.com
>
> **Estudante — R$ 189,99**
> Matriculados em instituição de ensino
>
> **Formado — R$ 239,99**
> Já formados em instituição de ensino
>
> *Acrescem 2,5% de taxa de serviço no ato da inscrição.*
>
> **Desconto para grupos:** 4 a 7 pessoas 40% · 8 a 12 pessoas 50% · 13 ou mais 60%.
> Como funciona: monte o grupo → um integrante envia nomes e e-mails para equipeccu@gmail.com →
> a equipe envia um cupom → use o cupom na inscrição.

*Os três cartões precisam ter o mesmo tamanho. Isso é layout, feito à mão.*

---

### 2.7 Página do curso — o cronograma que hoje é imagem

As datas só existem dentro de um PNG. Use a IA para formatar, não para inventar: os dados abaixo
saíram da peça publicada pelo próprio clube.

```
Formate esta grade como texto corrido legível, uma linha por dia, no formato
"data — horário módulo · horário módulo — consultoria responsável".
Não altere nenhum dado. Não acrescente comentário.

20/07 seg 18h Prep 101 + Consulting 101 / 20h Fit + Screening / McKinsey & Company
21/07 ter 18h Screening / 20h GMAT: Estrutura da prova
22/07 qua 18h GMAT: Problem Solving / 20h GMAT: Data Sufficiency
23/07 qui 18h GMAT: Critical Reasoning / 20h Fit + Screening
24/07 sex 18h GMAT / 20h Framework / BCG
25/07 sáb 10h Finanças / 13h Dinâmica em Grupo + Fit
27/07 seg 18h Dinâmica em grupo / 20h Case Interview / EloGroup
28/07 ter 18h Case Interview / 20h Guesstimate / Kearney
29/07 qua 18h Estratégia / 20h Crack the case Harvard / Visagio
30/07 qui 18h Crack the case GBP / BTC
31/07 sex 18h Crack the case / Bain & Company
```

Também padronize a ementa em quatro blocos, um por ciclo — hoje o desktop mostra "Ciclo 2" e
"Ciclo 3" colados e **perdeu o módulo "Estrutura do PS"**, que só aparece no mobile:

> **Ciclo 1** — Prep 101 · Consulting 101 · Screening · Estrutura do PS
> **Ciclo 2** — GMAT (Estrutura da prova, Problem Solving, Data Sufficiency, Critical Reasoning) · Business Case Test
> **Ciclo 3** — Finanças · Framework · Fit Interview · Case Interview · Guesstimate · Estratégia para Cases
> **Ciclo 4** — Wrap up

*Grafia padronizada: "Consulting 101", "Fit Interview", "Case Interview" — hoje varia entre desktop
e mobile.*

---

### 2.8 Consulting Women's Community — de página mais fraca a uma das melhores

236 palavras de adjetivos, zero data, zero parceiro, zero botão. E o projeto teve 7 encontros com
7 consultorias.

```
Reescreva a descrição de um programa de capacitação em consultoria voltado a mulheres
universitárias. Máximo 70 palavras. Abra dizendo o que a participante faz e recebe, não o que o
programa "representa". Remova todo adjetivo vago como "espaço de união", "ambiente propício",
"jornada enriquecedora". Tom institucional.
```

**Texto final:**
> **H1:** Consulting Women's Community (CWC)
>
> Comunidade do CCU para mulheres que querem carreira em consultoria. Ao longo de sete encontros,
> as participantes trabalham problem solving, visão de mercado, liderança e preparação para
> processos seletivos, com consultoras de sete consultorias parceiras.
>
> **3ª edição · 7 encontros · 7 consultorias parceiras**
>
> | Data | Horário | Consultoria | Tema |
> |---|---|---|---|
> | 19/08 | 19h30 | McKinsey & Company | "The Broken Rung": como atingir seu maior potencial |
> | 26/08 | 19h30 | Accenture | Trilha de vida e carreira |
> | 02/09 | 19h30 | Kearney | Problem Solving em ambientes competitivos |
> | 09/09 | 19h30 | Roland Berger | Visão estratégica e atualidades de mercado |
> | 16/09 | 19h30 | Bain & Company | Crescimento de alta performance e liderança feminina |
> | 23/09 | 19h30 | Peers | Tech, IA e consultoria estratégica |
> | 24/09 | 19h00 | BCG | Roda de conversa e encerramento (presencial) |

*Confirme o ano da edição com a diretoria antes de publicar. E use o nome
**Consulting Women's Community (CWC)** nos três lugares — hoje o título da página diz
"Consulting Women's Consulting".*

---

### 2.9 Política de troca — tirar a data presa a uma edição

Hoje: *"até o dia 14/jul"* sem ano (duas vezes), sem ponto entre frases, e cita *"as 4 opções
disponíveis"* quando a página de vendas mostra 2.

```
Reescreva esta cláusula trocando a data fixa por uma regra relativa, para que não vença a cada
edição. Corrija a pontuação. Não cite número de opções de inscrição.

"Em caso de escolha da opção errada no ato da inscrição (dentre as 4 opções disponíveis), entre em
contato conosco via e-mail por equipeccu@gmail.com para solicitar a troca até o dia 14/jul Devido à
disponibilização do cronograma e da ementa antecipadamente, o cancelamento da inscrição pode ser
solicitado até o dia 14/jul."
```

**Texto final:**
> Em caso de escolha equivocada da modalidade no ato da inscrição, entre em contato pelo e-mail
> equipeccu@gmail.com para solicitar a troca até 3 dias antes do início das aulas da edição
> contratada, cuja data consta na página da edição.
>
> Pelo mesmo prazo pode ser solicitado o cancelamento, já que o cronograma e a ementa são
> disponibilizados antecipadamente e, com o início das aulas, o aluno recebe acesso à plataforma
> Classroom com materiais de apoio, simulados e gravações.
>
> A taxa de serviço de 2,5%, cobrada no ato da inscrição, não é reembolsada.
>
> *Versão vigente desde 09/2026.*

---

### 2.10 Página de contato (`/blank-7`) — hoje totalmente vazia

```
Escreva o conteúdo de uma página de contato de uma organização estudantil. Precisa ter: uma frase
de abertura, o e-mail, o prazo de resposta, e uma linha convidando para as redes. Máximo 50
palavras, tom institucional. E-mail: equipeccu@gmail.com. Prazo: até 3 dias úteis.
```

**Texto final:**
> **H1:** Fale com o CCU
>
> Dúvidas sobre o Processo Seletivo, o Prep4Consulting ou propostas de parceria: escreva para
> **equipeccu@gmail.com**. Respondemos em até 3 dias úteis.
>
> Também estamos no Instagram (@ccuclubedeconsultoria) e no LinkedIn.

---

### 2.11 FAQ — conteúdo que não existe no site

Página nova (criar à mão), mas o conteúdo pode vir da IA.

```
Escreva 12 perguntas frequentes para o site de um clube universitário de consultoria, divididas em
três grupos de 4: "A carreira de consultoria", "O Clube" e "Processo Seletivo e Prep4Consulting".
Cada resposta com 2 a 4 linhas, direta, sem hype. Contexto: clube fundado em 2011 na Unicamp; o
curso Prep4Consulting é aberto ao público, não só a alunos da Unicamp; há desconto para bolsista e
desconto progressivo para grupo. Não invente datas nem valores: escreva [DATA] e [VALOR] onde eu
devo preencher.
```

---

### 2.12 Lista de correções ortográficas — faça em lote

Não vale prompt: é busca e substituição. Estão espalhadas pelo site.

| Onde | Está | Deve ser |
|---|---|---|
| rodapé | Todos os seus são direitos reservados | Todos os direitos reservados. |
| home | os projetos tem têm | os projetos têm |
| home | os projetos externos, prepararam | os projetos externos preparam |
| home | missão, visão e valor | missão, visão e valores |
| `/sobre-nos` | VALOR (sobre 5 itens) | VALORES |
| `/sobre-nos` | Engenhria Mecânica | Engenharia Mecânica |
| `/sobre-nos` | "Nossos pilares" 3× | manter 1 |
| `/conteudo` | Prepara-se com esses materiais | Prepare-se com esses materiais |
| `/conteudo` | Guesstimate exclusivos | Guesstimates exclusivos |
| `/mailing` | treinamentos e processo seletivos | treinamentos e processos seletivos |
| `/revisao-industrias` | para os tema mais recorrentes | para os temas mais recorrentes |
| `/x-ray` | através de um formulário e partir desses dados | e, a partir desses dados |
| `/getting-the-job` | Essas essas empresas contribuíram | Essas empresas contribuíram |
| `/blank` (Alumni) | Mastecard | Mastercard |
| `/blank` (Alumni) | Enterpreneurship Analyst | Entrepreneurship Analyst |
| `/blank` (Alumni) | Presidentes anterior + es (2 caixas) | Presidentes anteriores (1 caixa) |
| `/prep4consulting-2026-2` | + módulos d / e consultorias (3 caixas) | + módulos de consultorias parceiras |
| `/prep4consulting-2026-2` | Âncora 1 (visível) | remover o rótulo |

---

## 3. Prompts de SEO — um por página

Use o **Criar com IA** do painel **SEO básico**. Título até 60 caracteres, descrição até 155.
Hoje **20 páginas do site estão com a descrição vazia**.

```
Gere o título e a meta descrição desta página. Regras: título com no máximo 60 caracteres,
terminando em " | CCU". Descrição com no máximo 155 caracteres, em português do Brasil, incluindo um
dado concreto quando eu fornecer. Sem emoji, sem exclamação, sem "clique aqui". A descrição precisa
ser única, diferente das outras páginas do site.

Página: [NOME]
Assunto: [o que a página trata]
Dado que pode entrar: [número ou fato]
```

Preenchido, página por página:

| Página | Título (≤60) | Descrição (≤155) |
|---|---|---|
| Home | `Clube de Consultoria Universitário — Unicamp` | Preparamos alunos da Unicamp e de todo o Brasil para os processos seletivos das principais consultorias estratégicas. Curso, conteúdo e alumni. |
| Processo Seletivo | `Processo Seletivo do CCU — seja membro \| CCU` | Faça parte do Clube de Consultoria Universitário: treinamentos, cases semanais, projetos e contato direto com consultorias. Veja etapas e prazos. |
| Prep4Consulting | `Prep4Consulting: curso para PS de consultoria` | Curso preparatório intensivo para processos seletivos de consultoria. Última edição: 82 alunos, nota média 9,7 e NPS 86. Desconto para bolsistas. |
| Sobre nós | `Sobre o CCU: missão, visão e valores \| CCU` | Organização gerida por alunos de graduação da Unicamp desde 2011, dedicada à carreira de consultoria estratégica e de gestão. |
| Alumni | `Alumni do CCU: onde estão nossos ex-membros` | 44 ex-membros do CCU atuam em BCG, Bain, McKinsey, Kearney, Oliver Wyman, Accenture e Mubadala. Conheça a rede alumni do Clube. |
| CWC | `Consulting Women's Community (CWC) \| CCU` | Comunidade do CCU para mulheres em consultoria: sete encontros com McKinsey, Accenture, Kearney, Roland Berger, Bain, Peers e BCG. |
| X-Ray | `X-Ray: pesquisa de carreira na Unicamp \| CCU` | Relatório que mapeia o interesse dos alunos da Unicamp pela carreira de consultoria. Seis edições publicadas, de 2014 a 2024. |
| Getting the Job | `Getting the Job: simulação de PS \| CCU` | Simulação completa de processo seletivo de consultoria, com cada etapa conduzida por uma consultoria parceira. Mais de 700 inscritos na 1ª edição. |
| Conteúdo | `Conteúdo gratuito para PS de consultoria \| CCU` | Trilha gratuita: fit e case interview, revisão de indústrias, frameworks, guesstimates e casebooks completos do CCU. Sem cadastro. |
| Casebooks | `Casebooks para treinar case interview \| CCU` | O casebook próprio do CCU e um banco com 15 casebooks de MIT, Harvard, Wharton, Kellogg, Ross, Darden, ESADE, NYU e Kearney. |
| Contato | `Fale com o CCU \| CCU` | Entre em contato com o Clube de Consultoria Universitário por e-mail, Instagram ou LinkedIn. Respondemos em até 3 dias úteis. |
| FAQ | `Perguntas frequentes sobre o CCU \| CCU` | Dúvidas sobre a carreira de consultoria, o Clube, o Processo Seletivo e o Prep4Consulting, respondidas em um só lugar. |

**Atenção:** três páginas hoje usam o título **"Início | Clube de Consultoria Universitário"** — a
home, `/blank-1` e `/getting-the-job`. Enquanto isso não for corrigido, o Google escolhe qual mostrar.

---

## 4. Prompts de imagem

### 4.1 Texto alternativo

Hoje o `alt` é o nome do arquivo (`cronograma-prep4consulting-2026-2_5.png`,
`y8-PTBaP90a-removebg-preview.png`) e duas imagens estão com `alt` vazio.

```
Escreva o texto alternativo desta imagem em português, com no máximo 120 caracteres, descrevendo o
que se vê e não o nome do arquivo. Sem "imagem de" nem "foto de" no começo. Se a imagem for
puramente decorativa, responda apenas: decorativa.
```

Para as fotos de evento, use direto:

| Arquivo | Texto alternativo |
|---|---|
| `ccu-evento-bain-turma` | Membros do CCU em evento na Bain & Company |
| `ccu-bain-logo` | Membros do CCU no escritório da Bain & Company |
| `cwc-mckinsey-broken-rung` | Participantes do Consulting Women's Community na sessão sobre The Broken Rung |
| `cwc-do-campus-a-consultoria` | Participantes do CWC em sessão com consultoria parceira |
| `cwc-networking` | Participantes do CWC em momento de networking |
| `ccu-evento-bain-retrato` | Membros do CCU em evento na Bain & Company |
| cronograma do curso | Cronograma do Prep4Consulting: 11 encontros ao vivo via Zoom |

### 4.2 As imagens pesadas

Não é prompt, é substituição. `/sobre-nos` carrega **4,1 MB em duas imagens**; `/loyalty` tem uma de
**6,8 MB**; um relatório do X-Ray tem **54,6 MB**. Use **Configurações de imagem → Ajustar** para
recortar ao tamanho real de exibição e reenvie em JPEG.

As 6 fotos de evento já vão prontas, na pasta `fotos-eventos-melhoradas/`, em três formatos:
`--hero` (1600×667), `--card` (800×600) e `--quadrado` / `--retrato`. Use o `--card` sempre que
possível: é o de melhor qualidade.

---

## 5. Prompt de revisão — rode no fim

```
Revise este texto contra as regras do site do CCU e me aponte o que estiver fora:
1. Tem promessa de aprovação, urgência ou tom de venda?
2. Tem data sem ano?
3. Tem número, nome de empresa ou depoimento que eu não forneci?
4. Tem parágrafo com mais de 3 linhas?
5. Tem erro de concordância ou pontuação?
6. A conclusão está na primeira frase?
Responda só com a lista de problemas e a correção de cada um.

Texto: [colar]
```

---

## 6. O que nenhum prompt resolve

Estas são as tarefas de maior impacto da auditoria, e todas são manuais. O caminho de clique está
no `Guia-Execucao-Wix-CCU.pdf`, nas tarefas indicadas.

| # | Tarefa | Tarefa no PDF |
|---|---|---|
| 1 | Reapontar o botão do PS (hoje vai ao formulário de 2022.1, fechado) | T1 |
| 2 | Pôr **Processo Seletivo** no menu — a página não recebe nenhum link hoje | T2 |
| 3 | Trocar os 7 slugs `blank-*` e criar os **31 redirecionamentos 301** | T3 |
| 4 | Religar os 3 CTAs de casebook que caem na home (libera 15 PDFs) | T4 |
| 5 | Ocultar os botões "Compre agora" enquanto a venda estiver encerrada | T5 |
| 6 | Excluir `/blank-1`, a página "Site em manutenção" indexável | T7 |
| 7 | Desinstalar Stores, Forum, Loyalty, Bookings, Members e Blog | T8 |
| 8 | Excluir as 14 páginas de evento residuais, duas chamadas "teste" | T9 |
| 9 | Ocultar `/eventos` (mostra "0 DIAS PARA O EVENTO") | T10 |
| 10 | Aplicar os Temas de Texto e remover as 3.948 formatações manuais | T11 |
| 11 | Criar a Política de Privacidade e o consentimento no mailing | T12 |
| 12 | Corrigir a divergência desktop/mobile na ementa do curso | T14 |

**Ordem que eu seguiria:** 1, 4 e 5 hoje (30 minutos, destravam os funis e 15 casebooks) → rodapé e
ortografia (seção 2) → SEO (seção 3) → depois o estrutural.

---

## 7. Procedência

`[FATO]` Erros de texto, slugs, páginas órfãs e valores citados vêm da coleta das 44 URLs do site em
16/09/2026. Cronograma do Prep4Consulting, programação do CWC e desconto de grupo foram transcritos
das peças publicadas pelo próprio clube no LinkedIn. Contrastes e contagens (3.948 formatações
manuais, 20 descrições vazias) medidos sobre o HTML servido.
`[FATO]` A limitação da IA do Editor clássico está na documentação do Wix.
`[HIPÓTESE]` O ano da edição do CWC retratada nas fotos — as imagens não têm EXIF.
**Não verificado:** os rótulos exatos dos botões de IA na conta do CCU, que variam por versão; e se
a IA de texto do Editor aceita prompts deste tamanho sem truncar.
