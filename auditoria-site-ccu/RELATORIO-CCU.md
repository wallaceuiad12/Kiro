# Auditoria do site do CCU — diagnóstico e plano de ação
**Site auditado:** https://www.consultoriaunicamp.com/ · **Coleta:** 16/09/2026 · **Benchmark primário:** Poli Consulting Club

---

## 0. Premissas e método (declarados, não perguntados)

Não houve bloqueio real que justificasse parar para perguntar. Segui com as seguintes premissas declaradas:

| # | Premissa adotada | Base |
|---|---|---|
| P1 | O site é **Wix Editor clássico**, não Wix Studio. Todas as instruções abaixo usam seções/strips, âncoras e **editor mobile separado**. | [FATO] HTML da home contém `"isResponsive":false`, `"editorType":""`, `<meta name="viewport" id="wixDesktopViewport">` |
| P2 | Não existe manual de marca acessível publicamente; tratei a **paleta e os Temas de Texto já configurados no site** como a marca de fato. | [FATO] Site Styles expõe paleta `--color_0..65` e temas `--font_0..10` coerentes |
| P3 | O Prep4Consulting é a principal fonte de receita (é o único produto com preço, CNPJ, política de reembolso e app de venda ativo). | [FATO] `/prep4consulting-2026-2` + `/politica-troca` + Wix Events com ingressos |
| P4 | Loja, fórum, fidelidade, agendamento e blog **não estão em uso**. Recomendo desinstalar. | [FATO] `/shop` "Não temos nenhum produto", `/forum` erro de widget, `/blog` sem posts, `/loyalty` recompensa loja vazia |
| P5 | Público prioritário: aluno de graduação da Unicamp (candidato a membro) **e** candidato externo pagante (aluno do curso). Os dois funis têm peso igual. | [FATO] `/blank-6` (PS) e `/prep4consulting-2026-2` (curso) |

**Método:** baixei o HTML bruto (SSR) das **44 URLs indexáveis** (28 do `pages-sitemap.xml`, 15 do `event-pages-sitemap.xml`, 1 do `booking-services-sitemap.xml`), extraí metadados, grafo de links, texto visível, tokens de tipografia/cor, e testei cada link e arquivo por HTTP. Repeti a coleta com *user-agent* de iPhone para comparar breakpoints. Mesma medição aplicada a PoliCC, UFRJ CC, USC Consulting Club e Rice Consulting.

**Legenda:** `[FATO OBSERVADO]` = verificado no HTML/HTTP nesta coleta · `[HIPÓTESE]` = inferência plausível não confirmada · `[RECOMENDAÇÃO]` = ação proposta.

> **Ressalva de escopo:** avaliei o **HTML servido**, não a renderização pixel-a-pixel em navegador. Contraste, tipografia e divergência de breakpoint vêm dos tokens CSS e do texto realmente servido em cada UA — não de inspeção visual. Onde não pude verificar, escrevi "não verificado".

---

## 1. Sumário executivo

1. **Os dois funis de conversão do CCU estão quebrados hoje, simultaneamente.** [FATO] O botão "Inscreva-se já!" do Processo Seletivo aponta para um Google Forms que redireciona para `.../closedform` — formulário fechado. E os dois botões "Compre agora" do curso levam a uma página que responde **"O registro está fechado / Vendas encerradas"**. O site está no ar sem nenhum caminho de entrada funcional, nem para membro nem para aluno pagante.
2. **A página do Processo Seletivo é órfã: não há um único link para ela em nenhum lugar do site.** [FATO] `/blank-6` (título SEO "N Processo Seletivo") não aparece no menu, no rodapé, nem em qualquer página. O funil de recrutamento existe, custou trabalho, e é inalcançável por navegação.
3. **Um link errado em `/conteudo` derruba toda a vertical de Casebooks.** [FATO] O card "Cases completos" → "Ver mais" aponta para a raiz do site em vez de `/blank-2`. Como `/blank-3` e `/blank-4` só são alcançáveis a partir de `/blank-2`, **15 casebooks em PDF que funcionam perfeitamente (HTTP 200)** estão inacessíveis. O mesmo erro se repete em `/blank-3` ("CONFIRA") e em `/guesstimate` ("...confira algumas resoluções de case") — três CTAs distintos caindo na home.
4. **Recomendação central: o CCU não precisa de redesign — precisa de religamento e poda.** O site já tem os ativos que faltam à concorrência (82 alunos, nota 9,7, NPS 86, 19 cursos de graduação, 44 alumni nomeados em BCG/Bain/McKinsey/Kearney/Oliver Wyman/Mubadala, 15 casebooks, 6 relatórios X-Ray) e já tem um sistema de estilos coerente configurado. O problema é que os ativos estão em páginas órfãs e o sistema de estilos é sobrescrito. Ondas 1 e 2 são quase todas de religar, renomear e apagar.
5. **48% das URLs indexáveis do site são órfãs.** [FATO] 21 das 44 URLs não recebem nenhum link interno, incluindo `/blank-1`, cujo H1 é **"Site em manutenção"** e cujo título SEO é **idêntico ao da home** ("Início | Clube de Consultoria Universitário"). Há ainda 13 páginas de evento residuais indexáveis, duas delas intituladas literalmente **"teste"** e **"teste (1)"**.
6. **A home não comunica proposta de valor, não tem nenhum dado e não tem nenhum CTA de conversão.** [FATO] Zero `<h1>`, zero `<h2>` — a única heading da home é um `<h6>`. São 408 palavras em parágrafos corridos, e o único CTA de conteúdo é "Conheça nossa missão, visão e valor". Nenhum dos números do clube aparece ali.
7. **O desktop do curso perdeu conteúdo que só existe no mobile.** [FATO] O módulo **"Estrutura do PS"** aparece no mobile e **não existe no desktop**; em contrapartida o mobile carrega os textos soltos **"Faça perguntas de clarificação"** e **"Avalie os dados cuidadosamente"** (copiados de `/entrevista`), invisíveis no desktop. Os dois layouts do Wix clássico divergiram. Na home, os quatro rótulos dos projetos ("Projeto externo de...") existem só no desktop.
8. **O site contradiz por escrito dois valores que o próprio clube declara.** [FATO] "Poder de comunicação": o rodapé global diz **"Todos os seus são direitos reservados"** em todas as 44 páginas, e há erro em `/`, `/sobre-nos`, `/conteudo`, `/mailing`, `/politica-troca`, `/blank`, `/revisao-industrias`, `/x-ray`, `/getting-the-job`. Tom institucional: `/blank-6` traz **"Não perca tempo! Garanta sua vaga no PS!"** — literalmente o hype de infoproduto que a política do clube proíbe.
9. **Há risco comercial e de LGPD concreto, não só descuido.** [FATO] O rodapé diz **"©2023"**; `/politica-troca` fixa prazos em **"até o dia 14/jul" sem ano** e cita **"as 4 opções disponíveis"** quando a página de vendas mostra 2; a taxa de serviço (**+R$ 4,75**, 2,5%) só aparece no checkout, não na página de preço. **Não existe política de privacidade em nenhum lugar do site**, e o formulário de `/mailing` coleta **data de nascimento e gênero como campo obrigatório** sem finalidade declarada.
10. **O PoliCC é melhor referência de arquitetura e pior referência de higiene — não copie a estrutura dele.** [FATO] 35 das 64 páginas do sitemap do PoliCC são `cópia-*` (55%), **9 itens do menu de produção apontam para páginas `cópia-*`**, `/equipe` responde **404**, e `/sobre-nos` e `/sobre-nós` fazem **301 para a home**. O que vale adotar é o padrão do funil duplo e do FAQ; a implementação é antipadrão.

---

## 2. Placar (rubrica)

Notas de 0 a 5. "Melhor referência observada" indica qual dos cinco sites medidos lidera a dimensão.

| # | Dimensão | Peso | CCU | PoliCC | Melhor referência observada | Justificativa (evidência) |
|---|---|---|---|---|---|---|
| 1 | Clareza da proposta de valor em 5s na home | 15% | **1** | **4** | PoliCC / UFRJ (4) | CCU: 0 `<h1>`/`<h2>` na home, abre com a saudação "BEM-VINDO AO CLUBE DE CONSULTORIA UNIVERSITÁRIO" e 408 palavras corridas. PoliCC: uma frase — "Venha se preparar para os processos seletivos das maiores consultorias do mundo..." |
| 2 | Nitidez dos dois funis | 15% | **0** | **4** | PoliCC (4) | CCU: PS órfã + formulário em `/closedform`; curso com "Compre agora" → "Vendas encerradas". PoliCC: "Curso e PS" é o 1º item do menu, dois blocos na home com datas |
| 3 | Frescor da informação | 15% | **1** | **2** | UFRJ CC (4) | CCU: "0 DIAS PARA O EVENTO", "©2023", "14/jul" sem ano, e-book "PS 2022.1", X-Ray mais recente de 2024. PoliCC: "®2020" e datas sem ano. UFRJ: "© 2026 por UFRJ Consulting Club" e 4 artigos recentes na home |
| 4 | Higiene estrutural | 10% | **1** | **0** | UFRJ CC (3) | CCU: 21/44 URLs órfãs, 6 slugs `blank-*`, 2 páginas "teste". PoliCC: 35/64 páginas `cópia-*`, menu sobre páginas cópia, `/equipe` 404. UFRJ: 3/17 cópias |
| 5 | Consistência visual e disciplina tipográfica | 10% | **1** | **3** | USC / Rice (5) | CCU: **46** tamanhos de fonte, **34** famílias, **3.948** `<span>` com fonte inline (**141/página**), 3 pretos distintos. PoliCC: 26 tamanhos, 28 spans/página. USC e Rice: **0** overrides inline |
| 6 | Densidade e escaneabilidade | 10% | **1** | **4** | PoliCC (4) | CCU: home 408 palavras / 0 headings; `/consulting-women-consulting` 3 parágrafos de adjetivos, 0 headings, 0 CTA. PoliCC: home 169 palavras, selos e FAQ em acordeão numerado |
| 7 | Prova social e credibilidade | 10% | **3** | **2** | **CCU (3)** | CCU tem 82 alunos / 9,7 / NPS 86 / 19 cursos, 44 alumni nomeados com empresa e cargo, 18 logos de consultoria, 6 relatórios X-Ray, 15 casebooks — mas nada disso na home. PoliCC tem selos de parceiros sem números |
| 8 | Confiança e transparência | 5% | **1** | **2** | PoliCC (2) | CCU: `/blank-7` ("Fale Conosco") **vazia**, sem política de privacidade, gênero obrigatório no mailing, "4 opções" vs 2 exibidas, taxa oculta. PoliCC: CNPJ, endereço, e-mail e link de política corretos no rodapé |
| 9 | Experiência mobile | 5% | **1** | **3** | PoliCC (3) | CCU: breakpoints divergentes com **perda de conteúdo** ("Estrutura do PS" só no mobile; rótulos dos projetos só no desktop), imagens de 6,8 MB / 5,2 MB / 2,8 MB, PDF de **54,6 MB**. PoliCC: divergência só de truncamento no rodapé |
| 10 | SEO técnico e de conteúdo | 5% | **1** | **1** | UFRJ CC (3) | CCU: meta description **vazia** em quase toda página-chave, 3 páginas com o título da home, prefixos "N ", slugs `blank-N`, home sem `<h1>`, alt = nome do arquivo. PoliCC: sufixo "policonsultingclub" minúsculo, slugs acentuados, `/incriçãops20211` |
| | **Média ponderada** | 100% | **1,15** | **2,60** | — | |

**Gap prioritário:** dimensões **2 (funis)** e **3 (frescor)** — juntas somam 30% do peso e são onde o CCU tem as duas piores notas absolutas (0 e 1). São também as mais baratas de corrigir: nenhuma exige design novo, só religar links, reabrir/atualizar formulário e trocar datas. A dimensão 7 (prova social) é o **ativo** a explorar: o CCU já lidera e só precisa mover o conteúdo para a home.

---

## 3. Inventário completo de páginas (Fase 1)

44 URLs indexáveis. "Entradas" = número de páginas distintas que linkam para ela **fora** de menu e rodapé globais.

### 3.1 Páginas estáticas (`pages-sitemap.xml`, 28)

| URL | Título SEO real | Finalidade aparente | Conteúdo? | No menu? | Entradas | Última atualização aparente | Veredito |
|---|---|---|---|---|---|---|---|
| `/` | Início \| Clube de Consultoria Universitário | Home | Sim (408 pal., 0 H1) | Sim | — | rodapé "©2023" | **Reescrever** |
| `/sobre-nos` | Sobre nós \| Clube de Consultoria Universitário | Institucional + equipe | Sim (365 pal., 18 H1 + 40 H2) | Sim | 0 | equipe atual | **Reescrever + dividir** |
| `/blank-7` | Fale Conosco \| Clube de Consultoria | Contato | **Vazia (só rodapé)** | Não | **0 — ÓRFÃ** | n/d | **Reescrever no slug `/contato`** |
| `/mailing` | Mailing \| Clube de Consultoria | Captura de lead | Sim (form) | Sim | 0 | n/d | **Manter + corrigir LGPD** |
| `/prep4consulting-2026-2` | Prep4Consulting \| Clube de Consultoria Universitário | Página do curso (funil pago) | Sim (541 pal., 14 H1) | Sim | 0 | edição 2026.2 (encerrada) | **Reescrever + slug perene** |
| `/x-ray` | X-Ray \| Clube de Consultoria Universitário | Projeto externo | Sim (214 pal., 0 heading) | Sim | 0 | relatório mais recente 2024 | **Manter + atualizar** |
| `/consulting-women-consulting` | Consulting Women's Consulting \| Clube de Consultoria Universitário | Projeto CWC | Sim (236 pal., 0 heading, 0 CTA) | Sim | 0 | n/d | **Reescrever + renomear** |
| `/blank-6` | N Processo Seletivo \| Clube de Consultoria | **Funil de recrutamento** | Sim (213 pal.) | **Não** | **0 — ÓRFÃ** | e-book "PS 2022.1" | **Reescrever em `/processo-seletivo` + pôr no menu** |
| `/conteudo` | Conteúdo \| Clube de Consultoria Universitário | Hub de conteúdo | Sim (211 pal., 0 heading) | Sim | 0 | n/d | **Manter + corrigir link** |
| `/blank-2` | N Casebooks \| Clube de Consultoria | Índice de casebooks | Sim (107 pal.) | Não | **0 — ÓRFÃ** | n/d | **Consolidar em `/casebooks`** |
| `/blank-3` | Casebook CCU \| Clube de Consultoria | Casebook próprio | Sim (161 pal.) — **CTA quebrado** | Não | 1 (`/blank-2`) | n/d | **Manter em `/casebook-ccu` + arrumar CTA** |
| `/blank-4` | Banco de Casebooks \| Clube de Consultoria | 15 casebooks externos | **Sim** (15 PDFs, todos 200) | Não | 1 (`/blank-2`) | casebook mais novo: 2019 | **Manter em `/banco-de-casebooks`** |
| `/blank-5` | N Insights \| Clube de Consultoria | Links de insights | Sim (102 pal.) | Não | **0 — ÓRFÃ** | n/d | **Consolidar em `/conteudo`** |
| `/revisao-industrias` | Revisão das Indústrias \| Clube de Consultoria Universitário | Material de estudo | Sim (194 pal., 0 heading) | Sim | 1 (`/entrevista`) | n/d | **Manter** |
| `/framework` | Framework \| Clube de Consultoria Universitário | Material de estudo | Sim (195 pal., 0 heading) | Sim | 1 | n/d | **Manter** |
| `/guesstimate` | Guesstimate \| Clube de Consultoria Universitário | Material de estudo | Sim (321 pal.) — **CTA final quebrado** | Sim | 1 | n/d | **Manter + arrumar CTA** |
| `/entrevista` | Entrevista \| Clube de Consultoria Universitário | Material de estudo | Sim (726 pal. — a maior) | Sim | 1 | n/d | **Manter + hierarquizar** |
| `/getting-the-job` | **Início \| Clube de Consultoria Universitário** ⚠ | Projeto externo | Sim (233 pal.) | Sim | 0 | "+700 na 1ª edição" | **Reescrever + corrigir título** |
| `/blog` | Blog \| Clube de Consultoria **Unicamp** ⚠ | Blog | **Vazio** ("Verifique em breve") | Não | 0 | sem posts | **Excluir + desinstalar app** |
| `/blank` | Alumni \| Clube de Consultoria | Rede alumni (44 nomes) | Sim (368 pal., 44 H1) | Sim | 0 | n/d | **Manter em `/alumni`** |
| `/members` | Members \| Clube de Consultoria | Área de membros | **Totalmente vazia** | Não | **0 — ÓRFÃ** | n/d | **Excluir + desinstalar app** |
| `/shop` | Loja \| Clube de Consultoria Universitário | Loja | **Vazia** ("Não temos nenhum produto") | Não | **0 — ÓRFÃ** | meta diz "inscrições abertas" | **Excluir + desinstalar app** |
| `/loyalty` | Programa de fidelidade \| Clube de Consultoria | Fidelidade | Sim, mas **inoperante** | Não | **0 — ÓRFÃ** | "Sign up to the site" (EN) | **Excluir + desinstalar app** |
| `/book-online` | Agendamento online \| Clube de Consultoria | Agendamento | **Travada** ("Carregando os dias...") | Não | 1 (`/service-page/...`) | n/d | **Excluir + desinstalar app** |
| `/forum` | Fórum \| Clube de Consultoria | Fórum | **Erro** ("Widget Didn't Load") | Não | **0 — ÓRFÃ** | n/d | **Excluir + desinstalar app** |
| `/eventos` | Eventos \| Clube de Consultoria | Vitrine de eventos | Sim — **"0 DIAS PARA O EVENTO"** | Não | **0 — ÓRFÃ** | 2026.2 encerrada | **Manter + pôr no menu ou ocultar** |
| `/politica-troca` | Política de troca, devolução e reembolso \| Clube de Consultoria | Política comercial | Sim (265 pal.) | Rodapé | 0 | "14/jul" sem ano | **Reescrever** |
| `/blank-1` | **Início \| Clube de Consultoria Universitário** ⚠ | — | **"Site em manutenção"** | Não | **0 — ÓRFÃ / DUPLICADA** | n/d | **Excluir + 301 → `/`** |

### 3.2 Página do app Bookings (`booking-services-sitemap.xml`, 1) — não constava do inventário informado

| URL | Título SEO real | Conteúdo? | Entradas | Veredito |
|---|---|---|---|---|
| `/service-page/processo-seletivo` | Processo Seletivo \| Clube de Consultoria | "Esse serviço não está disponível." + texto que fala com **empresas**, não candidatos | **0 — ÓRFÃ** | **Excluir serviço + desinstalar Bookings** |

### 3.3 Páginas de evento (`event-pages-sitemap.xml`, 15) — todas com `robots=index`

| URL | Título SEO / H1 | `lastmod` | Entradas | Veredito |
|---|---|---|---|---|
| `/event-details/prep4consulting-2026-2` | Prep4Consulting 2026.2 | 2026-07-19 | 2 | **Manter** (edição corrente) |
| `/event-details/prep4consulting-2025-2-1-1` | **"Prep4Consulting 2026.1 "** (espaço final) em slug de 2025.2 | 2026-06-20 | **0 — ÓRFÃ** | **Excluir + 301 → `/eventos`** |
| `/event-details/prep4consulting-2025-2-1` | **"teste"** | 2025-09-04 | **0 — ÓRFÃ** | **Excluir + 301** |
| `/event-details/teste-1` | **"teste (1)"** | 2025-09-04 | **0 — ÓRFÃ** | **Excluir + 301** |
| `/event-details/prep4consulting-2025-1-old` | Prep4Consulting 2025.1 **(old)** | 2025-01-02 | **0 — ÓRFÃ** | **Excluir + 301** |
| `/event-details/prep4consulting-2025-2` | Prep4Consulting 2025.2 | 2025-07-03 | **0 — ÓRFÃ** | **Excluir + 301** |
| `/event-details/prep4consulting-2025-1-2` | Prep4Consulting 2025.1 | 2025-01-23 | **0 — ÓRFÃ** | **Excluir + 301** |
| `/event-details/prep4consulting-2024-2` | Prep4Consulting 2024.2 | 2024-12-16 | **0 — ÓRFÃ** | **Excluir + 301** |
| `/event-details/prep4consulting-2024-1-1` | Prep4Consulting 2024.1 | 2024-06-19 | **0 — ÓRFÃ** | **Excluir + 301** |
| `/event-details/prep4consulting-2023-2` | Prep4Consulting 2023.2 | 2023-06-26 | 1 (link **obsoleto** em `/prep4consulting-2026-2`) | **Excluir + 301 + remover link** |
| `/event-details/prep4consulting-4` | Prep4Consulting | 2023-01-16 | **0 — ÓRFÃ** | **Excluir + 301** |
| `/event-details/prep4consulting-3` | "Prep4Consulting " (espaço final) | 2022-08-02 | **0 — ÓRFÃ** | **Excluir + 301** |
| `/event-details/prep4consulting-2` | Prep4Consulting | 2022-02-05 | **0 — ÓRFÃ** | **Excluir + 301** |
| `/event-details/prep4consulting` | Prep4Consulting | 2021-07-12 | **0 — ÓRFÃ** | **Excluir + 301** |
| `/event-details/getting-the-job` | Getting the Job | 2021-07-04 | **0 — ÓRFÃ** | **Excluir + 301 → `/getting-the-job`** |

**Resumo do inventário:** 44 URLs indexáveis · **21 órfãs (48%)** · 3 com o título da home · 6 slugs `blank-*` em páginas centrais · 7 páginas de app vazias/quebradas · 14 páginas de evento residuais.


---

## 4. Achados críticos

Ordenados por severidade. Esforço: **P** = até 30 min · **M** = 1 a 4 h · **G** = mais de 4 h ou exige produção de conteúdo/decisão.

---

### C-01 · O formulário do Processo Seletivo está fechado e o botão continua convidando
**Evidência** — `/blank-6`, botão **"Inscreva-se já!"** → `https://forms.gle/gWXZmxHAxWAhH1VW8`, que responde HTTP 200 após redirecionar para `https://docs.google.com/forms/d/e/1FAIpQLSc.../closedform`. A mesma página anuncia: *"Não perca tempo! Garanta sua vaga no PS!"*
**Por que importa** — É o funil de entrada de membros, o mecanismo pelo qual o clube cumpre a missão declarada de "promover a carreira de consultoria no ambiente universitário". Um convite ativo para um formulário fechado é a pior combinação possível: gasta a intenção do visitante e entrega frustração. Some-se que a frase viola diretamente a política de tom institucional do próprio CCU.
**Correção** — Enquanto o PS estiver fechado, trocar o bloco de CTA por estado honesto: "As inscrições para o Processo Seletivo 2026.2 estão encerradas. As próximas abrem em [mês/ano] — entre na mailing para ser avisado" + botão secundário → `/mailing`. Quando abrir, repor o formulário **com data de encerramento explícita (dia/mês/ano)**. Reescrever o título para "O Clube está em busca de novos membros" sem exclamação dupla.
**Passo-a-passo no Wix** — Editor → página Processo Seletivo → clicar no botão → **Link** → trocar destino para `/mailing` → alterar rótulo para "Quero ser avisado do próximo PS" → editar a caixa de texto acima → **Publicar** → repetir no **editor mobile** (ícone de celular no topo).
**Esforço** P · **Risco** Baixo

---

### C-02 · A página do Processo Seletivo é órfã — zero links de entrada em todo o site
**Evidência** — `/blank-6` não recebe nenhum link. Não está no menu (que é: Início · Sobre nós · Projetos ▸ [Prep4Consulting, X-Ray, Consulting Women's Community, Getting The Job] · Parceiros · Conteúdo ▸ [Entrevista, Revisão das Indústrias, Framework, Guesstimate] · Alumni · Mailing · Mais), não está no rodapé (Início · Sobre nós · Projetos · Parceiros · Conteúdo · Política de Troca) e nenhuma página aponta para ela.
**Por que importa** — Metade da razão de existir do site é invisível. O visitante que quer entrar no clube não tem caminho. É também o motivo de o CCU pontuar 0 na dimensão de funis: o PoliCC põe "Curso e PS" como **primeiro** item do menu.
**Correção** — Promover a página a item de primeiro nível do menu, no slug `/processo-seletivo`, e adicionar um bloco de entrada na home (ver C-06).
**Passo-a-passo no Wix** — Editor → **Menus e Páginas** → selecionar a página `blank-6` → engrenagem → **SEO básico** → mudar slug para `processo-seletivo` → arrastar a página para o topo da lista do menu → renomear o item para "Processo Seletivo" → **SEO → Gerenciador de Redirecionamentos de URL** → criar 301 `/blank-6` → `/processo-seletivo`.
**Esforço** P · **Risco** Baixo (o 301 preserva qualquer link externo existente)

---

### C-03 · O funil pago termina em "Vendas encerradas"
**Evidência** — `/prep4consulting-2026-2` exibe preços ativos (**"ESTUDANTE de R$ 209,99 POR R$189,99"**, **"FORMADO de R$ 259,99 POR R$239,99"**) e dois botões **"Compre agora"**, ambos apontando para `/event-details/prep4consulting-2026-2`, que responde **"O registro está fechado"** e **"Vendas encerradas"**.
**Por que importa** — O CCU tem CNPJ (45.692.698/0001-91) e vende um produto. Uma página de vendas com preço e botão de compra que leva a um checkout fechado é falha de transparência comercial, não estética. E é a página do curso que está no menu principal.
**Correção** — Transformar a página em **perene** (ver C-08): manter a descrição do curso, os números da última edição e a ementa; substituir o bloco de preço/compra por "Inscrições para a próxima edição (2027.1) abrem em [mês/ano]" + captura de lista de espera → `/mailing`. Quando a edição abrir, repor preço e botão único.
**Passo-a-passo no Wix** — Editor → página Prep4Consulting → selecionar os dois botões "Compre agora" → **Configurações → Ocultar** (não excluir, para reusar na próxima edição) → adicionar caixa de texto com o aviso + 1 botão secundário → `/mailing` → **Publicar** → repetir no **editor mobile**.
**Esforço** P · **Risco** Baixo

---

### C-04 · Um link errado orfana 15 casebooks funcionais
**Evidência** — Três CTAs distintos que deveriam levar aos casebooks apontam para a raiz do site:
| Origem | Rótulo literal | `href` observado |
|---|---|---|
| `/conteudo` | "Ver mais" (card **"Cases completos"**) | `https://www.consultoriaunicamp.com` |
| `/blank-3` | **"CONFIRA"** | `https://www.consultoriaunicamp.com` |
| `/guesstimate` | "Agora que você conheceu alguns frameworks e sabe resolver guesstimates, clique aqui e confira algumas resoluções de case" | `https://www.consultoriaunicamp.com` |

Nenhum deles tem atributo `data-anchor` — ou seja, não são âncoras, são links mortos para a home. Consequência: `/blank-2` fica órfã e, como `/blank-3` e `/blank-4` só recebem link de `/blank-2`, toda a vertical morre. `/blank-4` contém **15 casebooks (MIT, Darden ×2, ESADE ×2, Harvard, Illinois, Kearney, Kellogg, NYU, Ross ×3, Wharton ×2)** e **todos respondem HTTP 200 `application/pdf`**.
**Por que importa** — É o material gratuito de maior valor do clube, já produzido e hospedado, invisível. A política do CCU proíbe aumentar a barreira ao conteúdo gratuito; aqui a barreira é acidental, mas total. Também quebra a trilha de aprendizado: `/entrevista` → `/revisao-industrias` → `/framework` → `/guesstimate` → **∅**.
**Correção** — Apontar os três CTAs para `/casebooks` (slug novo de `/blank-2`).
**Passo-a-passo no Wix** — Para cada um dos três elementos: Editor → clicar no botão/texto → ícone de **link** → **Uma página do meu site** → escolher "Casebooks" → **Concluído**. Verificar no **editor mobile** que o link foi herdado (links são compartilhados entre breakpoints, mas confirme o elemento existe no mobile). **Publicar**.
**Esforço** P · **Risco** Baixo

---

### C-05 · Desktop e mobile divergiram, com perda de conteúdo em ambos os lados
**Evidência** — Comparando o HTML servido a UA de desktop e de iPhone:

| String | Desktop | Mobile |
|---|---|---|
| `Estrutura do PS` (módulo do Ciclo 1) | **ausente** | presente |
| `Faça perguntas de clarificação` | ausente | **presente** (texto solto no Ciclo 3) |
| `Avalie os dados cuidadosamente` | ausente | **presente** (texto solto no Ciclo 3) |
| `Consulting 101` / `Consulting101` | com espaço | sem espaço |
| `Fit Interview` / `Fit interview` | maiúscula | minúscula |
| `Projeto externo de preparação de processos seletivos` (home) | **presente** | ausente |

No desktop, "Ciclo 2" e "Ciclo 3" aparecem coladas e todos os módulos são despejados depois — a ordem de leitura está quebrada. No mobile a estrutura está correta (Ciclo 1: Prep 101, Consulting101, Screening, Estrutura do PS · Ciclo 2: GMAT ×4 + Business Case Test · Ciclo 3: Finanças, Framework, Fit interview, Case interview, Guesstimate, Estratégia para Cases · Ciclo 4: Wrap up), mas contaminada com dois textos copiados de `/entrevista`.
**Por que importa** — Um curso que ensina comunicação estruturada exibe sua própria ementa fora de ordem, e cobra por ela. Além disso, quem compara desktop e mobile vê ementas diferentes. Este é o risco clássico do Wix Editor clássico: dois layouts editados de forma independente.
**Correção** — Reconstruir a ementa como **um único elemento por ciclo** (uma caixa de texto com lista, ou 4 acordeões), no desktop, e replicar no mobile. Excluir os dois textos soltos no mobile. Padronizar capitalização ("Consulting 101", "Fit Interview", "Case Interview").
**Passo-a-passo no Wix** — Editor (desktop) → selecionar as caixas de texto dos módulos → excluir → inserir **4 caixas de texto** (uma por ciclo) com lista de tópicos, usando o **Tema de Texto** "Parágrafo 2" (sem formatação manual) → alinhar em 4 colunas com **Organizar → Distribuir horizontalmente** → alternar para **editor mobile** → arrastar os 4 blocos para empilhar → localizar e **excluir** "Faça perguntas de clarificação" e "Avalie os dados cuidadosamente" → **Publicar**.
**Esforço** M · **Risco** Médio (mexe em layout; publique fora de janela de inscrição)

---

### C-06 · A home não tem proposta de valor, heading, dado nem CTA de conversão
**Evidência** — `/` tem **0 `<h1>`, 0 `<h2>`, 0 `<h3>`, 0 `<h4>`, 0 `<h5>` e 1 `<h6>`**. Abre com "BEM-VINDO AO CLUBE DE CONSULTORIA UNIVERSITÁRIO". 408 palavras, sendo o maior bloco um parágrafo único de 47 palavras. Único CTA de conteúdo: "Conheça nossa missão, visão e valor". Nenhum número. Meta description **vazia**.
Contraste — PoliCC: *"Venha se preparar para os processos seletivos das maiores consultorias do mundo, aprender a resolver problemas profissionais de maneira estruturada e alavancar sua carreira profissional!"* + selos *"Treinamento especial com empresas parceiras: BCG — GMAT · BTC — Entrevistas · Bain & Company — Estruturação Geral"* + dois blocos de CTA com datas. Total: 169 palavras.
**Por que importa** — Viola as duas restrições de design do CCU. "Resposta primeiro": a home responde "somos bem-vindos" antes de "o que fazemos por você". "Prova sobre promessa": o clube **tem** 82 alunos, 9,7 de nota média, NPS 86, 19 cursos de graduação e 44 alumni em BCG/Bain/McKinsey/Kearney/Oliver Wyman/Mubadala — e não usa nenhum. A ausência de `<h1>` também custa SEO e navegação por leitor de tela.
**Correção** — Reestruturar a home em 6 seções MECE, resposta primeiro:
1. **H1** + uma frase: *"O Clube de Consultoria Universitário prepara alunos da Unicamp e de todo o Brasil para os processos seletivos das principais consultorias estratégicas."*
2. **Faixa de números** (4 cards, da última edição): 82 alunos · 9,7 nota média · NPS 86 · 19 cursos de graduação.
3. **Funil duplo, lado a lado:** card "Quero entrar no Clube" → `/processo-seletivo`; card "Quero fazer o curso" → `/prep4consulting`. Cada um com status e data explícita.
4. **Alumni:** 6 logos + "44 ex-membros em BCG, Bain, McKinsey, Kearney, Oliver Wyman e outras" → `/alumni`.
5. **Conteúdo gratuito:** 3 cards → `/conteudo`, `/casebooks`, `/x-ray`.
6. **Parceiros:** grade de logos padronizada.
Mover os 3 parágrafos atuais para `/sobre-nos`.
**Passo-a-passo no Wix** — Editor → home → converter o texto de abertura em **H1** via **Temas de Texto → Título 1** (não via tamanho manual) → **Adicionar → Faixa/Seção** para cada bloco → usar **Adicionar → Caixa de Texto** com Temas de Texto → botões via **Adicionar → Botão**, estilo primário único → **Configurações da página → SEO** → preencher a meta description → replicar no **editor mobile** → **Publicar**.
**Esforço** G · **Risco** Médio

---

### C-07 · `/blank-1` é uma página "Site em manutenção" indexável com o título da home
**Evidência** — `/blank-1`: `<title>Início | Clube de Consultoria Universitário</title>` — **idêntico** ao de `/`. `<h1>Site em manutenção</h1>` + "Atualizações em breve!". `<link rel="canonical" href=".../blank-1">` (auto-canônica, não aponta para a home). Está no `pages-sitemap.xml`, responde 200, e é órfã. Um terceiro caso: `/getting-the-job` **também** usa o título "Início | Clube de Consultoria Universitário".
**Por que importa** — Três URLs disputando o mesmo título é canibalização direta: o Google escolhe qual mostrar para "Clube de Consultoria Universitário", e pode escolher a que diz "Site em manutenção". Além do dano de imagem — um clube que ensina rigor com uma página de manutenção pública.
**Correção** — Excluir `/blank-1` com 301 → `/`. Corrigir o título de `/getting-the-job`.
**Passo-a-passo no Wix** — Editor → **Menus e Páginas** → `blank-1` → **Excluir** → **SEO → Gerenciador de Redirecionamentos de URL → + Novo redirecionamento**: de `/blank-1` para `/` (tipo 301). Depois: página Getting The Job → engrenagem → **SEO básico** → **Título do SEO** → "Getting the Job: simulação de processo seletivo | CCU".
**Esforço** P · **Risco** Baixo

---

### C-08 · Informação vencida em produção, em cinco lugares
**Evidência** (todos verificados em 16/09/2026):

| Local | Trecho literal | Problema |
|---|---|---|
| Rodapé global (44 páginas) | `©2023 Clube de Consultoria Universitário` | 3 anos defasado |
| `/eventos` | `0 DIAS PARA O EVENTO` · `Inscrições até 17/07/2026!` · `Início: 20/07/2026!` · `Você pode comparecer?` | Contador zerado e convite de RSVP para evento encerrado |
| `/politica-troca` | `até o dia 14/jul` (2×) | Sem ano; preso a uma edição |
| `/blank-6` | Link para `E-book PS 2022.1 [CCU].pdf` (Drive, acessível) | Material de 2022.1 no PS de 2026 |
| `/x-ray` | Relatórios: `2014 · 2015/2016 · 2018/2019 · 2020 · 2023 · 2024` | Mais recente é 2024; sem 2025 nem 2026 |
| `/prep4consulting-2026-2` | Link para `/event-details/prep4consulting-2023-2` | Página do curso 2026.2 linkando evento de 2023 |

**Por que importa** — Transparência comercial é restrição declarada: "informação vencida ou ambígua é risco, não só descuido". Um prazo de reembolso "até 14/jul" sem ano é inexequível juridicamente e injusto com o aluno.
**Correção** — Rodapé: trocar por "© 2026 Clube de Consultoria Universitário". `/politica-troca`: substituir datas fixas por regra relativa — "até 3 dias antes do início das aulas da edição contratada, cuja data consta na página da edição" — e datar a política ("Versão vigente desde 01/2026"). `/eventos`: ocultar do menu enquanto não houver evento aberto. `/blank-6`: substituir o e-book por versão atual ou remover o bloco. `/x-ray`: publicar 2025/2026 ou rotular a lista como "Edições anteriores".
**Passo-a-passo no Wix** — Rodapé: Editor → clicar no rodapé → editar a caixa de texto (uma vez; o rodapé é global). `/politica-troca`: editar texto. `/eventos`: **Menus e Páginas** → engrenagem → **Ocultar do menu** *(atenção: isso não despublica; para sair do Google use também **SEO básico → Ocultar esta página dos resultados de busca**)*. Link obsoleto: clicar no elemento em `/prep4consulting-2026-2` → **Link** → corrigir ou remover.
**Esforço** P (rodapé, datas) / M (X-Ray, e-book) · **Risco** Baixo

---

### C-09 · Erros de português e texto fragmentado contradizem o valor "poder de comunicação"
**Evidência** — trechos literais:

| URL | Trecho literal | Correção |
|---|---|---|
| rodapé global | `Todos os seus são direitos reservados` | `Todos os direitos reservados.` |
| `/` | `os projetos tem têm como objetivo principal` | `têm como objetivo principal` |
| `/` | `os projetos externos, prepararam pessoas externas` | `preparam pessoas externas` |
| `/` | `Conheça nossa missão, visão e valor` | `...e valores` |
| `/sobre-nos` | cabeçalho `VALOR` sobre 5 itens | `VALORES` |
| `/sobre-nos` | `Nossos pilares` aparece **3×** no HTML | manter 1 |
| `/sobre-nos` | `Engenhria Mecânica` | `Engenharia Mecânica` |
| `/conteudo` | `Prepara-se com esses materiais` | `Prepare-se` |
| `/conteudo` | `Guesstimate exclusivos` | `Guesstimates exclusivos` |
| `/mailing` | `treinamentos e processo seletivos` | `processos seletivos` |
| `/politica-troca` | `...a troca até o dia 14/jul Devido à disponibilização...` | falta ponto entre as frases |
| `/revisao-industrias` | `framework para os tema mais recorrentes` | `os temas mais recorrentes` |
| `/x-ray` | `através de um formulário e partir desses dados` | `e a partir desses dados` |
| `/getting-the-job` | `Essas essas empresas contribuíram` | `Essas empresas contribuíram` |
| `/blank` | `Mastecard` | `Mastercard` |
| `/blank` | `Enterpreneurship Analyst` | `Entrepreneurship Analyst` |
| `/blank` | `Presidentes anterior` + `es` (quebrado em 2 caixas) | uma caixa: `Presidentes anteriores` |
| `/prep4consulting-2026-2` | `+ módulos d` + `e consultorias` + `parceiras` (3 caixas, quebra no meio da palavra) | uma caixa |
| `/prep4consulting-2026-2` | `Âncora 1` visível (desktop **e** mobile) | renomear a âncora / ocultar rótulo |
| `/blank-6` | `O` / `Clube` / `está` / `em busca de` / `Novos Membros` (5 caixas) | uma caixa |
| `/sobre-nos` | caracteres invisíveis antes de `Clarissa` e `Diego` (word-joiner U+2060) | limpar |

**Por que importa** — Não é preciosismo: "poder de comunicação" é um dos cinco valores declarados em `/sobre-nos`. Uma frase quebrada no rodapé de **todas** as 44 páginas é a assinatura do clube. E a fragmentação em caixas de texto é a causa mecânica de vários problemas: quebra no meio de palavra, ordem de leitura errada e divergência mobile.
**Correção** — Revisão textual completa + consolidar cada frase em **uma** caixa de texto.
**Passo-a-passo no Wix** — Para cada item: Editor → duplo clique no texto → corrigir. Para fragmentos: selecionar as caixas extras → **Excluir** → reescrever a frase inteira na caixa que sobrou (usando **Temas de Texto**, não formatação manual) → repetir no **editor mobile**. Para "Âncora 1": Editor → clicar na âncora → renomear para `precos` (o rótulo visível some quando a âncora é reposicionada corretamente; se persistir, mover a âncora para fora da área de conteúdo).
**Esforço** M · **Risco** Baixo

---

### C-10 · A seção de equipe tem cargos e nomes trocados
**Evidência** — `/sobre-nos`, seção "Nossa equipe", ordem de leitura servida no HTML: `Lucas Ferro / Engenharia Elétrica / Vice-Presidente / Lucas Ferro / **Diretora de Preparação** / Frederico Jon Campos / Engenharia de Controle e Automação / Frederico Jon Campos`. O cargo "Diretora de Preparação" (feminino) flutua entre dois nomes masculinos. Adiante: `Clarissa Victória Alves / Farmácia / Rafaela Iochida Padia / Engenharia Civil / Assessora / Rafaela / ⁠Clarissa Victória Alves` — Clarissa aparece sem cargo. E: `Leonardo Passos / Engenharia Mecânica / Marcos Gabriel Plácido De Almeida / Engenharia Mecânica / Assessor / Leonardo Mota Passos / Marcus`. Nomes também divergem entre rótulo e legenda: `Gustavo Gomes`/`Gustavo Costa`, `Pedro Fernandes`/`Pedro Augusto Fernandes`, `Marcos Gabriel Plácido De Almeida`/`Marcus`. A página tem **18 `<h1>` e 40 `<h2>`** (58 headings).
**Por que importa** — Atribuir o cargo errado a uma pessoa real é o erro mais custoso da lista: afeta a reputação individual dos membros e a credibilidade institucional. `[HIPÓTESE]` a causa é sobreposição de caixas de texto e imagens sem agrupamento, o que explica também a ordem embaralhada.
**Correção** — Reconstruir a seção com **um componente repetido** (Wix Repeater ou Galeria Pro), um item por pessoa, com campos fixos: foto, nome, curso, cargo. Conferir nome e cargo de cada pessoa com a diretoria antes de publicar.
**Passo-a-passo no Wix** — Editor → excluir as caixas soltas da seção → **Adicionar → Lista e Grade → Repetidor** → configurar 1 item com imagem + 3 textos (Título 3 / Parágrafo 2 / Legenda) → duplicar o item por pessoa → preencher → **editor mobile**: definir 1 coluna → **Publicar**. `[RECOMENDAÇÃO]` mover para página própria `/equipe` (ver mapa).
**Esforço** G · **Risco** Baixo (alto valor reputacional)

---

### C-11 · Sete páginas de app publicadas, vazias ou quebradas
**Evidência**

| URL | Texto literal servido |
|---|---|
| `/forum` | `Widget Didn't Load` / `Check your internet and refresh this page.` / `If that doesn't work, contact us.` |
| `/shop` | `Não temos nenhum produto para mostrar no momento.` — porém a **meta description** diz: `O Prep4Consulting, nosso curso preparatório para processos seletivos de consultoria, está com inscrições abert...` |
| `/loyalty` | `Sign up to the site` (não traduzido) · recompensas `10% em produtos da loja` apontando para a loja vazia |
| `/book-online` | `Carregando os dias...` (travado) + um `.` solto |
| `/service-page/processo-seletivo` | `Esse serviço não está disponível. Contate-nos para obter mais informações.` + `Se você é uma empresa que queira divulgar seu processo, clique aqui!` |
| `/members` | (nenhum conteúdo) |
| `/blog` | `Verifique em breve` / `Assim que novos posts forem publicados, você poderá vê-los aqui.` |

Nenhuma está no menu; todas responden 200 e estão em sitemap. `/loyalty` carrega uma imagem de **6,8 MB**.
**Por que importa** — Uma mensagem de erro em inglês e um programa de fidelidade que promete desconto numa loja inexistente são promessas quebradas, indexáveis. A meta description da `/shop` faz o Google anunciar "inscrições abertas" a partir de uma página vazia. E ocultar do menu não resolve: as páginas continuam publicadas e indexáveis.
**Correção** — **Desinstalar os apps**, não apenas ocultar as páginas: Wix Forum, Wix Stores, Wix Loyalty, Wix Bookings, Members Area e Wix Blog. Desinstalar remove as páginas e o peso de script.
**Passo-a-passo no Wix** — Painel do site → **Apps → Gerenciar Apps** → em cada app: ⋯ → **Excluir/Desinstalar** → confirmar. Depois: **SEO → Gerenciador de Redirecionamentos de URL** → 301 de `/shop`, `/forum`, `/loyalty`, `/book-online`, `/members`, `/blog`, `/service-page/processo-seletivo` → `/`. Verificar `pages-sitemap.xml` em ~48 h.
*`[RECOMENDAÇÃO]`* Se a diretoria quiser manter blog no futuro, mantenha o app **mas** publique 3 posts antes de expor a página no menu — o padrão do UFRJ CC (4 artigos recentes na home) só funciona com produção real.
**Esforço** P · **Risco** Médio (verifique com a diretoria se a área de membros/loja está prevista antes de desinstalar; a venda do curso usa **Wix Events**, que deve **permanecer**)

---

### C-12 · 14 páginas de evento residuais indexáveis, duas chamadas "teste"
**Evidência** — `event-pages-sitemap.xml` lista 15 páginas, todas com `<meta name="robots" content="index">`. Entre elas: `/event-details/prep4consulting-2025-2-1` com `<h1>teste</h1>`; `/event-details/teste-1` com `<h1>teste (1)</h1>`; `/event-details/prep4consulting-2025-1-old` ("Prep4Consulting 2025.1 (old)"); e `/event-details/prep4consulting-2025-2-1-1`, cujo H1 é **"Prep4Consulting 2026.1"** — a edição de 2026.1 vivendo num slug de 2025.2 com sufixo duplo. Além disso, **13 dessas páginas têm meta description quase idêntica** (293–299 caracteres, todas começando em "O curso completo e com o melhor custo-benefício para processos seletivos de consultoria está de volta!").
**Por que importa** — 13 páginas com a mesma descrição competindo pelo termo "curso preparatório consultoria" é canibalização de manual. E "teste" indexável é o oposto de rigor.
**Correção** — Excluir os eventos encerrados no app Wix Events e criar 301 para `/eventos`. Manter no máximo a edição corrente + 1 anterior.
**Passo-a-passo no Wix** — Painel → **Eventos** → selecionar cada evento passado → ⋯ → **Excluir**. Para os que a diretoria quiser preservar como histórico: abrir o evento → **SEO** → marcar **"Ocultar dos motores de busca"** e reescrever a meta description para ser única. Depois criar os 301 no **Gerenciador de Redirecionamentos**.
**Esforço** M · **Risco** Baixo

---

### C-13 · Não existe política de privacidade, e o mailing coleta gênero obrigatório
**Evidência** — Nenhuma URL de política de privacidade em nenhum sitemap; o rodapé global linka apenas "Política de Troca, Devolução e Reembolso". O formulário de `/mailing` coleta: `Nome`, `Sobrenome`, `E-mail`, `Data de nascimento`, `Profissão / Curso`, `Qual seu gênero? *` com a marcação **`Obrigatório`** (opções `Homem · Mulher · Trans · Outro · Prefiro não informar`) e `Que tipo de conteúdo você busca...`. Não há finalidade declarada, base legal, prazo de retenção nem caixa de consentimento. Formulários equivalentes existem em `/x-ray` (`[HIPÓTESE]` — a coleta é descrita no texto: *"A coleta de dados é realizada através de um formulário"*, hospedado fora do site; **não verificado**) e no PS (Google Forms).
**Por que importa** — O CCU é pessoa jurídica com CNPJ e trata dados de terceiros. Data de nascimento + gênero, sem finalidade declarada e sem política acessível, é exposição real sob a LGPD. `[RECOMENDAÇÃO]` adicionalmente: as opções misturam identidade de gênero com condição trans (`Homem · Mulher · Trans`), o que é tecnicamente inconsistente e desalinhado do cuidado que o próprio clube demonstra com o CWC — o padrão usual é `Mulher cisgênero · Homem cisgênero · Mulher transgênero · Homem transgênero · Não-binário · Prefiro não informar`, ou simplesmente um campo aberto.
**Correção** — (a) Criar `/politica-privacidade` com: quem é o controlador (razão social + CNPJ), quais dados são coletados, finalidade de cada um, base legal (consentimento), prazo de retenção, com quem é compartilhado, e como solicitar exclusão (e-mail). (b) Linkar no rodapé global. (c) Tornar gênero **opcional** e declarar a finalidade ao lado do campo (ex.: "usamos para medir a diversidade do nosso público e desenhar o CWC"). (d) Adicionar caixa de consentimento explícita antes de "Participar". (e) Remover data de nascimento se não houver uso definido — minimização de dados.
**Passo-a-passo no Wix** — **Menus e Páginas → + Adicionar Página** → nome "Política de Privacidade", slug `politica-privacidade` → **Ocultar do menu** (mas manter indexável) → escrever o conteúdo → clicar no rodapé → adicionar link de texto. Formulário: Editor → clicar no formulário → **Adicionar campo → Caixa de seleção** para consentimento → clicar no campo de gênero → desmarcar **Obrigatório** → **Publicar**.
**Esforço** M · **Risco** Baixo (reduz risco jurídico)

---

### C-14 · A ementa e o cronograma do curso são imagens
**Evidência** — `/prep4consulting-2026-2` tem 12 `<img>`. O cronograma é `cronograma-prep4consulting-2026-2_5.png`, com `alt="cronograma-prep4consulting-2026-2_5.png"` — o alt é o próprio nome do arquivo. Nenhuma data do curso aparece como texto na página. Outros alts: `hq1_edited.png`, `Google-Classroom-Logo.png`, `y8-PTBaP90a-removebg-preview.png`, e **2 imagens com `alt=""`**.
**Por que importa** — Três consequências: (1) as datas do curso são invisíveis para o Google — quem busca "prep4consulting datas" não acha; (2) são inacessíveis a leitor de tela; (3) cada nova edição exige reexportar uma imagem (o sufixo `_5` sugere que já houve 5 versões), o que é exatamente o mecanismo pelo qual a informação vence. Alt = nome de arquivo não é alt: é ruído.
**Correção** — Converter o cronograma em **tabela ou lista de texto** (data · módulo · horário). Manter a imagem apenas como reforço visual, com alt descritivo. Reescrever o alt de todas as imagens-chave.
**Passo-a-passo no Wix** — Editor → substituir a imagem por **Adicionar → Tabela** (ou lista de texto) → preencher com as datas. Para alt text: **Gerenciador de Mídia** ou clicar na imagem → **Configurações → Texto alternativo**. Sugestões: cronograma → `Cronograma do Prep4Consulting 2027.1: 11 encontros ao vivo via Zoom, das 18h às 22h`; `hq1_edited.png` → `Turma do Prep4Consulting em aula online`; logo Classroom → `Google Classroom` (ou `alt=""` se decorativo).
**Esforço** M · **Risco** Baixo

---

### C-15 · Tipografia: o sistema existe e é sobrescrito 3.948 vezes
**Evidência** — O site **já tem** Temas de Texto coerentes configurados:
`--font_3: 88px brandon-grot-w01-light` · `--font_4: 72px` · `--font_5: 50px` · `--font_6: 40px` · `--font_2: 28px` · `--font_0: 22px` (títulos, Brandon Grotesque Light) · `--font_7: 20px avenir-lt-w01_35-light` · `--font_8: 18px` · `--font_9: 15px` · `--font_10: 14px` (corpo, Avenir LT Light). Todos com `color: rgb(var(--color_15))`.
Contra isso, nas 28 páginas do CCU: **46 tamanhos de fonte inline distintos** (de `5px` a `98px`), **34 famílias de fonte referenciadas** — incluindo `メイリオ/meiryo` e `ヒラギノ角ゴ pro w3/hiragino kaku gothic pro` (fallbacks japoneses de template), um `arial)` malformado, além de `montserrat`, `k2d`, `lulo-clean`, `futura`, `helvetica`, `madefor` — e **3.948 `<span style="...font-...">`**, ou **141 por página**. Três pretos em uso (`#181818`, `#000`, `#080808`) e dois brancos (`#FFFFFF`, `#FBFAFA`). Um único rótulo ("Cases completos" em `/conteudo`) está embrulhado em **10 `<span>` aninhados**, declarando `font-size:20px` e depois `18px`, `font-weight:normal` e depois `bold`.
Comparação normalizada: **CCU 141 spans/página · PoliCC 28 · USC e Rice (Squarespace) 0**.
**Por que importa** — A conclusão é boa notícia: o CCU **não precisa criar** um design system, precisa **parar de contrariar** o que já tem. Cada correção manual futura custa 10× mais caro enquanto a formatação viver dentro de cada caixa.
**Correção** — Ver §6 (design system mínimo). Regra operacional: **nenhuma formatação de fonte por caixa de texto**; toda tipografia vem de Temas de Texto.
**Passo-a-passo no Wix** — Editor → **Site → Temas de Texto** → ajustar os 6 temas propostos em §6 (mudança global e instantânea). Depois, por página: selecionar cada texto → no painel de texto clicar em **Temas** e escolher o tema (isso descarta o override inline). Prioridade: home, `/prep4consulting`, `/sobre-nos`, `/processo-seletivo`, `/conteudo`.
**Esforço** G (mas incremental, página a página) · **Risco** Baixo

---

### C-16 · Contraste: dois tons da paleta falham WCAG AA e estão em uso
**Evidência** — Contraste calculado sobre os valores reais da paleta do site:

| Par | Uso | Razão | AA texto (4.5) | AA ≥18pt (3.0) |
|---|---|---|---|---|
| `#181818` sobre `#FBFAFA` | corpo padrão | **17,04:1** | Passa | Passa |
| `#C1272D` sobre `#FBFAFA` | destaque/título vermelho | **5,61:1** | Passa | Passa |
| `#FFFFFF` sobre `#C1272D` | texto em botão vermelho | **5,84:1** | Passa | Passa |
| `#515151` sobre `#FBFAFA` | texto secundário | **7,62:1** | Passa | Passa |
| `#181818` sobre `#C1272D` | texto escuro sobre vermelho | **3,04:1** | **FALHA** | Passa |
| `#898989` (color_8) sobre `#FBFAFA` | texto secundário | **3,36:1** | **FALHA** | Passa |
| `#D68084` (color_17) sobre `#FBFAFA` | — | **2,77:1** | **FALHA** | **FALHA** |
| `#EAACAE` (color_16) sobre `#FBFAFA` | — | **1,83:1** | **FALHA** | **FALHA** |
| `#C2C2C2` (color_7) sobre `#FBFAFA` | — | **1,71:1** | **FALHA** | **FALHA** |
| `#C44C4C` (color_2) sobre `#FBFAFA` | — | **4,49:1** | **FALHA** (por 0,01) | Passa |

`[FATO]` `color_17` e `color_16` aparecem 59 e 58 vezes nas páginas do CCU — ou seja, os dois piores pares estão em uso. `[HIPÓTESE]` provavelmente como fundo ou detalhe, não como texto corrido; **não verificado visualmente**.
**Por que importa** — Acessibilidade aqui é continuidade da política de acesso do próprio CCU: o material é gratuito, mas ilegível não é acessível. O público é universitário e majoritariamente móvel, onde brilho de tela e luz ambiente agravam qualquer contraste baixo. Há também um ganho de disciplina: o site tem 66 slots de cor na paleta com muita duplicação, e reduzir o uso a 6 tokens elimina a decisão caso a caso — que é o que produz inconsistência.
**Correção** — Banir `color_7`, `color_8`, `color_16`, `color_17` e `color_2` para **texto**. Usar `color_14` (`#515151`, 7,62:1) para texto secundário. Nunca texto `#181818` sobre vermelho — use `#FFFFFF`.
**Passo-a-passo no Wix** — Editor → **Site → Cores do Site (Paleta)**: a paleta já está bem formada (linha principal `#FBFAFA · #C2C2C2 · #898989 · #515151 · #181818`; segunda linha, rampa vermelha `#EAACAE · #D68084 · #C1272D · #811A1E · #400D0F`). Não mude os valores — mude o **uso**: percorra os textos que usam cinza claro e troque para `color_14`.
**Esforço** M · **Risco** Baixo

---

### C-17 · Peso de mídia: imagens de vários MB e um PDF de 54,6 MB
**Evidência**

| Arquivo | Peso | Página |
|---|---|---|
| `11062b_afc56c8c...~mv2.jpeg` | **6.839 KB** | `/loyalty` (página a desinstalar) |
| `6a09dadbfe8e...jpg` | **5.189 KB** | `/blank-2` (Casebooks) |
| `11062b_ae0a0b1d...~mv2.jpg` | **3.082 KB** | `/blank-6` (Processo Seletivo) |
| `7208bc_0e454a5d...~mv2.png` | **2.813 KB** | `/sobre-nos` |
| `7208bc_197bd5ce...~mv2.png` | **1.324 KB** | `/sobre-nos` |
| X-Ray (1 relatório) | **54.621 KB** | `/x-ray` |
| X-Ray (outro relatório) | **15.985 KB** | `/x-ray` |
| Casebook Ross 2016 | **14.414 KB** | `/blank-4` |

Formatos referenciados no site: **1.785 PNG · 178 JPG · 30 JPEG · 0 WebP · 0 AVIF**. `[HIPÓTESE]` os arquivos com prefixo `11062b_` (contra `7208bc_` do site) são imagens de template nunca substituídas nem otimizadas — os três mais pesados têm esse prefixo.
**Por que importa** — `/sobre-nos` carrega ~4,1 MB só em duas imagens; um relatório de 54,6 MB é inviável em rede móvel. Como o público é universitário e majoritariamente móvel, isso é barreira de acesso ao conteúdo gratuito.
**Correção** — Recomprimir; usar JPG (ou WebP) para fotografia e reservar PNG para logos/transparência; comprimir os PDFs do X-Ray para < 10 MB.
**Passo-a-passo no Wix** — **Gerenciador de Mídia** → substituir os arquivos pesados por versões redimensionadas ao tamanho real de exibição (largura máx. ~1.920 px) e exportadas em JPG qualidade 80. Para os PDFs: recomprimir fora do Wix e reenviar, atualizando o link. As imagens de `/loyalty` e `/blank-6` saem de graça se os apps forem desinstalados (C-11).
**Esforço** M · **Risco** Baixo

---

### C-18 · Hierarquia de headings inexistente em todo o site
**Evidência** — contagem de `<h1>`–`<h6>` por página:

| Página | H1 | H2 | H3 | H4 | H5 | H6 |
|---|---|---|---|---|---|---|
| `/` | **0** | 0 | 0 | 0 | 0 | 1 |
| `/conteudo` | 0 | 0 | 0 | 0 | 0 | 1 |
| `/x-ray` | 0 | 0 | 0 | 0 | 0 | 1 |
| `/consulting-women-consulting` | 0 | 0 | 0 | 0 | 0 | 1 |
| `/framework`, `/guesstimate`, `/revisao-industrias` | 0 | 0 | 0 | 0 | 0 | 1 |
| `/blank-7`, `/members`, `/forum`, `/blog`, `/eventos` | 0 | 0 | 0 | 0 | 0 | 0 |
| `/prep4consulting-2026-2` | **14** | 8 | 0 | 0 | 0 | 1 |
| `/sobre-nos` | **18** | 40 | 0 | 0 | 0 | 1 |
| `/blank` (Alumni) | **44** | 6 | 0 | 0 | 0 | 0 |
| `/blank-5` | 1 (um parágrafo de 2 frases como H1) | 0 | 0 | 0 | 0 | 1 |

**Nenhuma página do site usa H3, H4 ou H5.** Em `/prep4consulting-2026-2`, três dos 14 H1 são: `*Desconto válido para uma quantidade limitada de vagas`, `ESTUDANTE`, `de R$ 209,99`. Em `/entrevista`, os H1 são `2 MODELOS Da CASE INTERVIEW` (com "Da" capitalizado no meio) e `formato da CASE INTERVIEW`.
**Por que importa** — Headings estão sendo usados como tamanho de fonte, não como estrutura. Efeito prático: o Google não entende do que a página trata (uma nota de rodapé com asterisco é o "título" da página do curso), leitores de tela ficam inúteis, e o site de um clube que ensina MECE não é MECE.
**Correção** — Um `<h1>` por página, igual ao assunto da página; `<h2>` para seções; `<h3>` para subitens. Nunca heading para preço, rótulo ou nota de rodapé.
**Passo-a-passo no Wix** — Editor → selecionar o texto → no painel de texto, dropdown de **Tema/Tag** → escolher a tag semântica (Wix separa "aparência" de "tag HTML": use **Título 1** para o H1 e mude a *tag* dos rótulos indevidos para **Parágrafo**). Fazer na ordem: home → `/prep4consulting` → `/sobre-nos` → `/conteudo` → demais.
**Esforço** M · **Risco** Baixo

---

### C-19 · Slugs e títulos de template em páginas centrais
**Evidência** — 6 páginas centrais em slugs `blank-*`: `/blank` (Alumni), `/blank-2` (Casebooks), `/blank-3` (Casebook CCU), `/blank-4` (Banco de Casebooks), `/blank-5` (Insights), `/blank-6` (Processo Seletivo), `/blank-7` (Fale Conosco). Três títulos SEO com prefixo residual **"N "**: `N Casebooks`, `N Insights`, `N Processo Seletivo`. Três sufixos de marca concorrentes: `| Clube de Consultoria` (19 páginas), `| Clube de Consultoria Universitário` (10), `| Clube de Consultoria Unicamp` (1, em `/blog`). Nome do projeto CWC inconsistente em três lugares: título `Consulting Women's Consulting`, texto `Consulting Women's Community (CWC)`, slug `/consulting-women-consulting`.
**Por que importa** — Slug é conteúdo: `/blank-6` compartilhado no WhatsApp não diz nada; `/processo-seletivo` diz tudo. "N Processo Seletivo" no Google parece erro de banco de dados. E três variantes de sufixo diluem a marca.
**Correção** — Ver §7 (tabela de SEO) e §5 (mapa de 301). Padronizar o sufixo em **`| CCU`** (curto, cabe em 60 caracteres) e o nome do projeto em **Consulting Women's Community (CWC)** nos três lugares.
**Passo-a-passo no Wix** — Para cada página: **Menus e Páginas** → engrenagem → **SEO básico** → editar **URL/slug** e **Título do SEO**. **Imediatamente depois**, **SEO → Gerenciador de Redirecionamentos de URL** → criar o 301 do slug antigo para o novo. Nunca troque slug sem criar o 301 na mesma sessão.
**Esforço** M · **Risco** Médio (perde-se tráfego se os 301 não forem criados)

---

### C-20 · Meta descriptions vazias nas páginas que mais importam
**Evidência** — Meta description **ausente** em: `/`, `/sobre-nos`, `/prep4consulting-2026-2`, `/conteudo`, `/blank-6`, `/blank`, `/x-ray`, `/consulting-women-consulting`, `/getting-the-job`, `/mailing`, `/entrevista`, `/framework`, `/guesstimate`, `/revisao-industrias`, `/politica-troca`, `/blank-2`, `/blank-4`, `/blank-5`, `/blank-7`, `/eventos` — praticamente todo o site. Só 3 grupos têm: `/blank-3` (139 car., adequada), `/shop` (144 car., mas anuncia "inscrições abertas" numa loja vazia) e as 15 páginas de evento (**293–299 car.**, acima do limite e quase idênticas entre si).
**Por que importa** — Sem meta description o Google recorta um trecho arbitrário; na home, o trecho disponível é "BEM-VINDO AO CLUBE..." ou um parágrafo com o erro "os projetos tem têm". O clube perde controle do que aparece na busca justamente onde a decisão acontece.
**Correção** — Ver §7. Todas ≤155 caracteres, com um dado verificável quando houver.
**Passo-a-passo no Wix** — **Menus e Páginas** → engrenagem → **SEO básico** → **Descrição do SEO**. Alternativamente Painel → **SEO → Ferramentas de SEO** para editar em lote. Use também o **Assistente de configuração de SEO do Wix** (SEO Setup Checklist) para acompanhar pendências.
**Esforço** M · **Risco** Baixo

---

### C-21 · Transparência de preço: taxa não divulgada e "4 opções" que não existem
**Evidência** — `/prep4consulting-2026-2` anuncia `POR R$189,99` e `POR R$239,99`. O checkout (`/event-details/prep4consulting-2026-2`) mostra `R$ 189,99` **`+ R$ 4,75 de taxa de serviço de ingresso`** — preço real R$ 194,74. A página de vendas não menciona a taxa; `/politica-troca` menciona ("2,5% do valor do produto"), o que confere com 4,75/189,99. Além disso `/politica-troca` diz: *"Em caso de escolha da opção errada no ato da inscrição (**dentre as 4 opções disponíveis**)"* — mas a página de vendas apresenta **2** opções (Estudante, Formado), e o checkout exibe **1** tipo de ingresso ("Estudante"). O desconto para bolsista (**R$ 70,00**) está num parágrafo corrido no fim da seção de preços, não como terceira opção visível.
**Por que importa** — Duas restrições declaradas do CCU são afetadas: transparência comercial (preço e prazos acessíveis, sem ambiguidade) e acesso/inclusão ("o desconto para bolsistas deve ser visível e digno, não nota de pé de página"). Hoje a opção mais barata — a que serve o aluno com menos recursos — é a menos visível da página.
**Correção** — (a) Exibir **três cards de igual peso visual**: Bolsista R$ 70,00 · Estudante R$ 189,99 · Formado R$ 239,99, cada um com "+ taxa de serviço de 2,5%" em legenda. (b) Corrigir "4 opções" para o número real. (c) Descrever o processo de comprovação do desconto de bolsista como passo numerado, não parágrafo.
**Passo-a-passo no Wix** — Editor → seção Preços → duplicar um dos cards existentes (**Ctrl+D**) para criar o card Bolsista → reordenar → adicionar legenda com a taxa usando o tema **Legenda** → editar `/politica-troca` → **editor mobile** → **Publicar**.
**Esforço** M · **Risco** Baixo

---

### C-22 · "Getting the Job" e "CWC" são páginas sem prova e sem saída
**Evidência** — `/getting-the-job`: 233 palavras, **0 CTA de conteúdo**, único dado é `+700 Inscritos na 1ª edição` — referência à **primeira** edição, com o rótulo "Última edição" seguido de `Essas essas empresas contribuíram`. `/consulting-women-consulting`: 236 palavras em 3 parágrafos, **0 heading, 0 dado, 0 CTA** — não há como se inscrever no CWC, nem calendário, nem contato. `/x-ray`: 214 palavras, 0 heading, 6 relatórios, o mais recente de 2024.
**Por que importa** — "Prova sobre promessa" e "acesso e inclusão" são restrições declaradas. O CWC é um compromisso do clube e sua página é a mais fraca do site: puro adjetivo ("espaço de união, integração e capacitação", "ambiente propício"), nenhum número, nenhuma porta de entrada. Citar a 1ª edição sugere que o projeto parou.
**Correção** — Para cada página de projeto, o mesmo esqueleto: H1 · uma frase de definição · 3 números da última edição · o que acontece (etapas/datas) · 1 CTA primário (inscrição ou mailing) · logos das consultorias envolvidas com alt text. Para o CWC, adicionar um CTA de entrada — mesmo que seja "entre na mailing do CWC".
**Passo-a-passo no Wix** — Construir **uma** página modelo (sugestão: `/x-ray`, que já tem relatórios como prova) com as 6 faixas acima, usando Temas de Texto e o botão primário. Depois: **Menus e Páginas** → engrenagem da página → **Duplicar** → renomear e trocar o conteúdo — assim as três páginas de projeto ficam consistentes sem remontagem. *Atenção:* duplicar página gera slug automático (`x-ray-1`); corrija o slug em **SEO básico** antes de publicar, senão o site volta a acumular slugs de template. Para o bloco de números, use **Adicionar → Caixa** com 3 colunas (Título 2 para o número, Legenda para o rótulo). Replicar no **editor mobile** e **Publicar**.
**Esforço** G (depende de dados da diretoria) · **Risco** Baixo

---

### C-23 · A página de contato está vazia e o e-mail é um Gmail
**Evidência** — `/blank-7`, título SEO "Fale Conosco", serve **72 palavras: apenas menu e rodapé**. Não está no menu. É órfã. O único canal de contato do site é `equipeccu@gmail.com`, no rodapé. Comparação: UFRJ CC tem seção de contato na home com três canais e e-mail institucional `consultingclub@poli.ufrj.br`; Rice Consulting tem "Contact Us" como item de menu; PoliCC tem `contato@policc.com.br`.
**Por que importa** — Uma organização com CNPJ que vende curso precisa de canal de contato acessível — é requisito de confiança e de defesa do consumidor. Ter a página criada, nomeada e vazia é pior que não tê-la.
**Correção** — Preencher `/contato` com: e-mail, prazo de resposta esperado, links de Instagram/LinkedIn (já existem no rodapé), e um formulário simples com finalidade declarada. `[RECOMENDAÇÃO]` migrar para e-mail em domínio próprio (`contato@consultoriaunicamp.com`) — o CCU já paga o domínio, e um Gmail enfraquece a percepção institucional.
**Passo-a-passo no Wix** — Editor → página `blank-7` → **SEO básico** → slug `contato` → adicionar conteúdo → **Adicionar → Contato → Formulário de contato** → pôr no menu → criar 301 `/blank-7` → `/contato`. Para o e-mail: Painel → **Domínios → Wix Mail / Google Workspace**.
**Esforço** P (conteúdo) / M (e-mail de domínio) · **Risco** Baixo


---

## 5. Benchmark

Cinco sites medidos com o mesmo método: **CCU**, **Poli Consulting Club** (Wix), **UFRJ Consulting Club** (Wix), **USC Consulting Club** (Squarespace), **Rice Consulting** (Squarespace).

### 5.1 Comparação de arquitetura de informação

| Elemento | CCU | PoliCC | UFRJ CC | USC | Rice |
|---|---|---|---|---|---|
| Itens no 1º nível do menu | 9 (+8 em submenu) | 12 (+ "Mais...") | 14 (+ "More") | **6** | **6** |
| Funil do curso no menu | dentro de "Projetos ▸" | **1º item** ("Curso e PS") | "Academia de Preparação" | — | — |
| Funil de PS no menu | **ausente** | dentro de "Curso e PS" | **"Processo Seletivo"** (3º) | **"Apply"** | — |
| Página de Equipe/Diretoria | seção em `/sobre-nos` | `/cópia-equipe-1` + `/cópia-diretoria` (`/equipe` = **404**) | `/organizacao` | `/whoistcc` | `/team` |
| FAQ | **ausente** | **`/perguntas-frequentes`** (3 categorias, acordeão numerado) | ausente | ausente | ausente |
| Página de Parceiros | **âncora na home** (`data-anchor`), não é página | **`/parceiros`** | seção na home | — | — |
| Contato | `/blank-7` **vazia**, fora do menu | e-mail no rodapé | **seção na home, 3 canais** | — | **`/contact-us`** no menu |
| Blog/artigos | app instalado, **0 posts** | — | **4 artigos recentes na home** | — | `/resources` |
| Números na home | **0** | 0 (tem selos) | 0 | 0 | 0 |
| Copyright no rodapé | **©2023** | **®2020** | **© 2026** | não verificado | não verificado |
| Páginas duplicadas no sitemap | 6 `blank-*` + 14 eventos | **35/64 `cópia-*` (55%)** | 3/17 (18%) | não verificado | não verificado |
| Overrides de fonte inline por página | **141** | 28 | 197 (1 pág.) | **0** | **0** |

### 5.2 O que adotar — o padrão, não o layout

| # | Padrão | Onde observei | Por que transferir ao CCU |
|---|---|---|---|
| B-1 | **Funil duplo explícito na entrada.** Dois blocos irmãos na home, cada um com público, ação e prazo. | PoliCC home: bloco "curso" (*"Inscrições: 20/07 a 23/08 · Duração do Curso: 24/08 a 18/09"*) e bloco PS (*"Se interessou por nossos projetos... quer fazer parte do Clube? Inscreva-se no nosso Processo Seletivo!"*), com âncoras `curso` e `processo` | Resolve o achado mais grave do CCU (C-02): hoje o PS é invisível. **Adapte, não copie:** o PoliCC omite o ano nas datas — o CCU deve usar dia/mês/ano completo |
| B-2 | **Selo de parceiro nomeando o módulo que a firma ensina.** | PoliCC: *"Treinamento especial com empresas parceiras: BCG — GMAT · BTC — Entrevistas · Bain & Company — Estruturação Geral"*; e no bloco de PS, *"McKinsey & Company"* | O CCU diz genericamente "módulos exclusivos ministrados por consultorias parceiras" e nunca diz **quais** nem **o quê**. Nomear converte uma promessa em prova, sem inventar dado |
| B-3 | **FAQ em acordeão, agrupado por intenção e numerado.** | PoliCC `/perguntas-frequentes`: 3 categorias ("A Carreira de consultoria", "O Clube", "Nosso Processo Seletivo"), perguntas numeradas `01`–`06` | É a forma MECE de reduzir densidade sem perder conteúdo. Absorveria boa parte dos parágrafos corridos do CCU e é a lacuna estrutural nº 1 dele |
| B-4 | **Página de Parceiros de verdade, com contrapartida.** | PoliCC `/parceiros` (212 palavras); UFRJ: *"contamos com o apoio de diversos parceiros, que englobam órgãos acadêmicos da UFRJ, grandes consultorias estratégicas e empresas reconhecidas"* | No CCU, "Parceiros" é âncora para uma grade de 18 logos sem uma linha sobre o que a parceria envolve. Uma página permite explicar a contrapartida e serve de material de prospecção |
| B-5 | **Copyright dinâmico e correto.** | UFRJ: `© 2026 por UFRJ Consulting Club` | O CCU está em ©2023 e o PoliCC em ®2020. É o item de menor esforço e maior sinal de site vivo do relatório |
| B-6 | **Contato como destino de primeira classe.** | UFRJ (seção na home com 3 canais + e-mail `@poli.ufrj.br`); Rice (`/contact-us` no menu + e-mail no rodapé) | Resolve C-23. O e-mail em domínio institucional é o detalhe que mais separa "organização" de "grupo de alunos" |
| B-7 | **Menu enxuto de ~6 itens.** | USC: About · Our Team · Client Services · Recruitment · Alumni · Apply. Rice: Home · Our Team · Our Services · Resources · For Members · Contact Us | O CCU tem 9 itens + 8 subitens e ainda esconde coisas em "Mais". Ambos os clubes americanos cabem em 6 sem perder função |
| B-8 | **Ação de conversão única e nomeada no menu.** | USC: **"Apply"** como item próprio | O CCU não tem nenhum verbo no menu — só substantivos. Um item "Processo Seletivo" e um "Prep4Consulting" resolvem |
| B-9 | **Meta description da home como proposta de valor.** | USC: *"USC Consulting Club is the official case preparation organization on campus..."*; UFRJ title *"Consultoria UFRJ \| UFRJ Consulting Club \| Brasil"* (termo de busca primeiro) | A home do CCU não tem meta description nenhuma (C-20) |
| B-10 | **Tipografia 100% do tema, 0% da caixa.** | USC e Rice: **0** `font-size` inline, **0** `<span style="font-...">` | É a prova de que o alvo de C-15 é alcançável. Não é característica do Squarespace: o CCU já tem os temas prontos — só precisa aplicá-los |
| B-11 | **Sinal de vida na home.** | UFRJ: "ÚLTIMOS ARTIGOS" com 4 posts reais e substantivos (MEI e crédito, cambismo, etanol, bitcoin) | O CCU tem um blog vazio. Se não vai produzir, desinstale (C-11); se vai, o padrão é puxar os últimos posts para a home |
| B-12 | **Página de transparência.** | UFRJ: item de menu "Transparência" | `[RECOMENDAÇÃO]` para uma entidade estudantil com CNPJ que vende curso, é diferencial de confiança barato. Onda 3 |

### 5.3 O que **não** adotar — antipadrões dos benchmarks

| # | Antipadrão | Evidência | Por que não copiar |
|---|---|---|---|
| A-1 | **Construir a IA sobre páginas "cópia".** | PoliCC: 35 de 64 páginas do sitemap são `cópia-*`; **9 itens do menu de produção apontam para elas** (Sobre nós → `/cópia-sobre-nós-1`, Diretoria → `/cópia-diretoria`, Equipe → `/cópia-equipe-1`, Alumni → `/cópia-alumni`, Conselho, Presidência, Case Team, REC, Business Team) | É a versão terminal da doença que o CCU tem em `blank-*`. Quando o menu depende de páginas-rascunho, ninguém consegue mais distinguir produção de teste. **O CCU já está melhor aqui** e deve resolver antes de chegar nesse ponto |
| A-2 | **Trocar slug sem 301 — ou pior, redirecionar para a home.** | PoliCC: `/sobre-nos` **e** `/sobre-nós` fazem **301 para `/`**, e `/equipe` responde **404** enquanto o conteúdo vive em `/cópia-equipe-1` | Redirecionar uma página específica para a home destrói o sinal de relevância e frustra quem clicou. Todo 301 do CCU (§7) deve ir para o **equivalente semântico**, nunca para `/` — exceto onde a página deixa de existir de fato |
| A-3 | **Slug de uma edição servindo outra edição.** | PoliCC: item de menu "Informações do Curso 2026.2" → **`/incriçãops20211`** (slug que diz "inscrição PS 2021.1", com erro de grafia) | Exatamente o erro do CCU em `/event-details/prep4consulting-2025-2-1-1` (H1 "Prep4Consulting 2026.1") e em `/prep4consulting-2026-2`. A lição é o slug **perene** (`/prep4consulting`) com a edição no conteúdo |
| A-4 | **Datas sem ano.** | PoliCC home: `Inscrições: 20/07 a 23/08` · `Duração do Curso: 24/08 a 18/09` · `Inscrições: 03/08 a 28/08` — nenhuma com ano | Idêntico ao `14/jul` do CCU. A política do CCU exige dia/mês/ano. **Aqui o benchmark é tão ruim quanto o CCU** — não use o PoliCC como referência de frescor |
| A-5 | **Botão de inscrição ativo depois do prazo.** | PoliCC home: "INSCREVA-SE" ativo com janela `20/07 a 23/08`. `[HIPÓTESE]` sendo a edição 2026.2 (conforme o menu), a janela fechou em 23/08/2026, antes desta coleta — mesmo problema do CCU. **Não verificado** se o destino aceita inscrição | O CCU não deve se consolar: deve resolver (C-01, C-03) |
| A-6 | **Placeholder de versão em produção.** | PoliCC `/cursodeproblemsolving`: `EM BREVE...` / `disponível na versão 2.1 do site`; rodapé `Design original Poli Consulting Club - REC, V2.2 ®2020policonsultingclub` | Mesma classe do `/blank-1` "Site em manutenção" do CCU. Versionamento interno e aviso de obra não pertencem ao site público |
| A-7 | **Sufixo de marca inconsistente e em caixa baixa.** | PoliCC: `Projetos \| policonsultingclub`, `Conteúdo \| policonsultingclub`, `FAQ \| policonsultingclub`, `Diretoria  \| policonsultingclub` (espaço duplo) vs `Início \| Poli Consulting Club \| USP` | O CCU tem o mesmo problema em 3 variantes (C-19). A correção é escolher **uma** forma e aplicá-la a todas as páginas |
| A-8 | **Slug acentuado / com caracteres perdidos.** | PoliCC: `/cópia-sobre-nós`, `/política-de`, `/cópia-cópia-formulario-de-inscriçõe` (truncado), e a base de eventos `/informa-es-do-evento-e-registro/` ("informações" mutilado) | Slugs devem ser ASCII, minúsculos, com hífen. O CCU já acerta nisso — **não regrida** ao renomear as páginas `blank-*` |
| A-9 | **Item de menu apontando para página "copy".** | UFRJ CC: "Transparência" → `/copy-of-produtos-de-negócios`; "Produtos de Negócios" → `/copy-of-ebooks`; "Carta Macro" → `/cópia-eventos` | Versão menor de A-1, no site que é melhor em frescor. Ninguém está imune: a disciplina precisa ser um hábito de manutenção (§9), não um mutirão único |
| A-10 | **Título de página fragmentado em várias caixas com link.** | UFRJ: a frase de valor da home está partida em `Uma das principais pontes entre`, `e o`, `mundo de`, cada pedaço um `<a>` para `/objetivo` | Mesma doença do CCU (`Presidentes anterior`+`es`, `+ módulos d`+`e consultorias`). Uma frase = uma caixa de texto |

### 5.4 Onde o CCU já é superior

| # | Vantagem do CCU | Evidência | Como preservar |
|---|---|---|---|
| S-1 | **Prova quantitativa real.** `82 Alunos`, `9,7 Nota média`, `19 Cursos de graduação distintos`, `86 NPS`, rotulados "Última edição (2026.1)". Nenhum dos quatro benchmarks apresenta métricas próprias de resultado. | `/prep4consulting-2026-2` | Levar para a home (C-06) e atualizar a cada edição (§9) |
| S-2 | **Rede alumni nomeada e verificável:** 44 pessoas com empresa e cargo — BCG, Bain & Company, McKinsey (2), Kearney (3), Oliver Wyman, Accenture, Mubadala Capital, Peers (5), Pragmatis, Kea & Partners, Altman Solon, EloGroup, Advisia, Google, Walmart, Shopee, Mercado Livre, XP, Itaú, Bradesco, BTG Pactual, P&G, AstraZeneca, Cielo, Mastercard. O PoliCC mantém a lista em `/cópia-alumni`. | `/blank` | Mover para `/alumni`, corrigir `Mastecard` e `Enterpreneurship`, unificar as categorias "Presidentes anteriores" e "Ex-Presidentes" |
| S-3 | **Biblioteca de conteúdo gratuito substancial e funcional:** 15 casebooks (MIT, Harvard, Wharton ×2, Kellogg, Ross ×3, Darden ×2, ESADE ×2, NYU, Illinois, Kearney) + 4 páginas de material próprio com PDF + 6 relatórios X-Ray — **todos HTTP 200**. | `/blank-4`, `/framework`, `/guesstimate`, `/revisao-industrias`, `/x-ray` | Religar (C-04). É o maior ativo desperdiçado do site |
| S-4 | **Trilha de aprendizado pedagogicamente pensada:** `/entrevista` → `/revisao-industrias` → `/framework` → `/guesstimate` → (cases), com CTAs que explicam o próximo passo. Nenhum benchmark tem sequência guiada. | CTAs "Agora que você adquiriu mais business sense..." | Consertar só o último elo (C-04) — a arquitetura pedagógica já está certa |
| S-5 | **Compromisso de acesso explícito e quantificado:** desconto para bolsista a `R$70,00` (63% de desconto sobre R$189,99), com procedimento de comprovação descrito. Nenhum benchmark menciona política de acesso. | `/prep4consulting-2026-2` | Promover a card de primeira classe (C-21) |
| S-6 | **Higiene de slug melhor que a dos dois benchmarks Wix:** slugs ASCII, sem acento, sem truncamento; sem página-cópia servindo o menu; sem 404 no menu. | `pages-sitemap.xml` | Não regredir ao renomear (A-8) |
| S-7 | **Rodapé com dados cadastrais completos:** endereço (`Cidade Universitária "Zeferino Vaz", Campinas - SP`), `CNPJ: 45.692.698/0001-91`, e-mail e link de política — em todas as páginas. | rodapé global | Corrigir a frase e o ano (C-08, C-09); a estrutura já está certa |
| S-8 | **Projeto de equidade institucionalizado (CWC),** com página própria. Nenhum benchmark tem iniciativa equivalente. | `/consulting-women-consulting` | Dar-lhe prova, dados e porta de entrada (C-22) |

---

## 6. Mapa do site: antes → depois

### 6.1 Antes — 44 URLs indexáveis (21 órfãs)

```
/ (home, 0 H1, 0 CTA de conversão)
├── MENU
│   ├── Início ................................ /
│   ├── Sobre nós ............................. /sobre-nos          [equipe embutida, cargos trocados]
│   ├── Projetos ▸ ............................ ÂNCORA na home (não é página)
│   │   ├── Prep4Consulting ................... /prep4consulting-2026-2   [slug de edição; "Compre agora" → vendas encerradas]
│   │   ├── X-Ray ............................. /x-ray              [relatório mais recente: 2024]
│   │   ├── Consulting Women's Community ...... /consulting-women-consulting  [0 dado, 0 CTA]
│   │   └── Getting The Job ................... /getting-the-job    [título SEO = "Início"]
│   ├── Parceiros ............................. ÂNCORA na home (não é página)
│   ├── Conteúdo ▸ ............................ /conteudo
│   │   ├── Entrevista ........................ /entrevista
│   │   ├── Revisão das Indústrias ............ /revisao-industrias
│   │   ├── Framework ......................... /framework
│   │   └── Guesstimate ....................... /guesstimate        [CTA final → home ✗]
│   ├── Alumni ................................ /blank              [44 H1]
│   ├── Mailing ............................... /mailing            [gênero obrigatório, sem política]
│   └── Mais ▸ ................................ (?)
├── RODAPÉ .................................... /politica-troca     ["14/jul" sem ano]
│
├── ÓRFÃS — sem nenhum link de entrada (21)
│   ├── /blank-6 .............................. PROCESSO SELETIVO   ⚠ funil principal + form fechado
│   ├── /blank-2 .............................. Casebooks           ⚠ raiz da vertical morta
│   │   ├── /blank-3 .......................... Casebook CCU        [CTA "CONFIRA" → home ✗]
│   │   └── /blank-4 .......................... Banco de Casebooks  [15 PDFs, todos 200]
│   ├── /blank-5 .............................. Insights
│   ├── /blank-7 .............................. Fale Conosco        ⚠ VAZIA
│   ├── /blank-1 .............................. ⚠ "Site em manutenção" + título da home
│   ├── /eventos .............................. ⚠ "0 DIAS PARA O EVENTO"
│   ├── /shop /forum /members /loyalty /book-online /blog ......... apps vazios/quebrados
│   ├── /service-page/processo-seletivo ....... "serviço não está disponível"
│   └── /event-details/… (13) .................. inclui "teste", "teste (1)", "2025.1 (old)"
└── /event-details/prep4consulting-2026-2 ..... [única viva] "Vendas encerradas"
```

### 6.2 Depois — 25 URLs indexáveis, 0 órfãs

```
/ (home: H1 + números + funil duplo + prova + conteúdo + parceiros)
├── 1. Processo Seletivo ...................... /processo-seletivo      ← de /blank-6  [NOVO NO MENU]
├── 2. Prep4Consulting ....................... /prep4consulting        ← de /prep4consulting-2026-2  [slug perene]
├── 3. Sobre nós ▸
│   ├── Sobre nós ............................ /sobre-nos              [missão/visão/valores + os 3 parágrafos da home]
│   ├── Equipe ............................... /equipe                 [NOVA — extraída de /sobre-nos, via Repetidor]
│   ├── Alumni ............................... /alumni                 ← de /blank
│   └── Parceiros ............................ /parceiros              [NOVA — deixa de ser âncora]
├── 4. Projetos ▸
│   ├── X-Ray ................................ /x-ray
│   ├── Consulting Women's Community ......... /consulting-womens-community  ← de /consulting-women-consulting
│   └── Getting the Job ...................... /getting-the-job
├── 5. Conteúdo ▸ ............................ /conteudo               [hub; inclui Insights incorporado]
│   ├── Entrevista ........................... /entrevista
│   ├── Revisão das Indústrias ............... /revisao-industrias
│   ├── Framework ............................ /framework
│   ├── Guesstimate .......................... /guesstimate            [CTA final → /casebooks ✓]
│   └── Casebooks ............................ /casebooks              ← de /blank-2  [RELIGADA ✓]
│       ├── Casebook CCU ..................... /casebook-ccu           ← de /blank-3
│       └── Banco de Casebooks ............... /banco-de-casebooks     ← de /blank-4  [15 PDFs acessíveis]
├── 6. FAQ ................................... /faq                    [NOVA — padrão B-3]
├── 7. Contato ............................... /contato                ← de /blank-7  [PREENCHIDA]
├── 8. Mailing ............................... /mailing                [+ consentimento e finalidade]
│
├── FORA DO MENU (indexáveis, linkadas do rodapé)
│   ├── /politica-troca ...................... [datas relativas + versão datada]
│   ├── /politica-privacidade ................ [NOVA — LGPD]
│   └── /eventos ............................. [visível só quando houver edição aberta]
└── /event-details/prep4consulting-2027-1 .... [1 evento vivo por vez]

EXCLUÍDAS + 301: /blank-1 · /blog · /shop · /forum · /members · /loyalty ·
                 /book-online · /service-page/processo-seletivo · 14 /event-details antigas
```

### 6.3 Contagem

| | Antes | Depois | Δ |
|---|---|---|---|
| URLs indexáveis | **44** | **25** | −19 (−43%) |
| Páginas órfãs | **21 (48%)** | **0** | −21 |
| Páginas com slug de template (`blank-*`) | 7 | **0** | −7 |
| Páginas vazias / quebradas / de teste | 10 | **0** | −10 |
| Páginas de evento indexáveis | 15 | **1** | −14 |
| Páginas com o título "Início \| ..." | 3 | **1** | −2 |
| Páginas sem meta description | 20 | **0** | −20 |
| Páginas novas a criar | — | 4 (`/equipe`, `/parceiros`, `/faq`, `/politica-privacidade`) | +4 |
| Itens no 1º nível do menu | 9 | **8** | −1 (mas com os 2 funis visíveis) |
| Redirecionamentos 301 a criar | — | **31** | — |

---

## 7. Design system mínimo

**Descoberta central:** o CCU **não precisa criar** um design system — ele já tem um, coerente, com 2 famílias e 1 cor de texto, e o sobrescreve 3.948 vezes. O trabalho é de **redução e disciplina**, não de criação.

### 7.1 Tipografia — 3 títulos + 2 corpos + 1 legenda

Valores atuais lidos do site e valores propostos. Configurar em **Editor → Site → Temas de Texto**.

| Token proposto | Tema do Wix | Valor atual observado | Valor proposto | Uso |
|---|---|---|---|---|
| **Título 1** | `font_5` | `50px/1.34 brandon-grot-w01-light` | **44px/1.2 Brandon Grotesque Light** | Um `<h1>` por página |
| **Título 2** | `font_6` | `40px/1.35 brandon-grot-w01-light` | **32px/1.3 Brandon Grotesque Light** | Seções (`<h2>`) |
| **Título 3** | `font_2` | `28px/1.375 brandon-grot-w01-light` | **24px/1.35 Brandon Grotesque Light** | Cards e subitens (`<h3>`) |
| **Corpo** | `font_8` | `18px/1.75 avenir-lt-w01_35-light` | **18px/1.6 Avenir LT 35 Light** | Texto padrão |
| **Corpo destaque** | `font_7` | `20px/1.67 avenir-lt-w01_35-light` | **20px/1.5 Avenir LT 35 Light** | Frase de valor, intro de seção |
| **Legenda** | `font_10` | `14px/1.79 avenir-lt-w01_35-light` | **14px/1.5 Avenir LT 35 Light** | Notas, taxas, fonte de dado |

**Aposentar (não usar mais):** `font_3` (88px) · `font_4` (72px) · `font_0` (22px) · `font_9` (15px — muito próximo de 14px e 18px) · `font_1` (14px, duplicata de `font_10`).
**Banir:** todo `font-size` inline (46 valores hoje, incl. 5px, 6px, 7px, 98px) e todas as famílias fora de Brandon Grotesque e Avenir — hoje há 34 referenciadas, incluindo os fallbacks japoneses `メイリオ`/`ヒラギノ角ゴ Pro W3` e um `arial)` malformado, além de `montserrat`, `k2d`, `lulo-clean`, `futura`, `madefor`, `helvetica`.

### 7.2 Cor — 1 marca + 1 destaque + 3 neutros

A paleta do Wix já está bem formada. **Não altere os valores** — altere o uso. Em **Editor → Site → Cores do Site**.

| Token | Slot Wix | Hex | Uso | Contraste verificado |
|---|---|---|---|---|
| **Marca** | `color_18` | `#C1272D` | Botão primário, destaque, ícones | 5,61:1 sobre `#FBFAFA` — AA ✓ |
| **Destaque / hover** | `color_19` | `#811A1E` | Hover do botão primário, links visitados | **10,00:1** com `#FFFFFF` — AAA ✓ |
| **Neutro 1 — fundo** | `color_11` | `#FBFAFA` | Fundo de página | — |
| **Neutro 2 — texto** | `color_15` | `#181818` | Texto e títulos | 17,04:1 — AAA ✓ |
| **Neutro 3 — secundário** | `color_14` | `#515151` | Legendas, metadados | 7,62:1 — AAA ✓ |
| **Apoio** | `color_26` | `#FFFFFF` | Texto sobre a marca | 5,84:1 sobre `#C1272D` — AA ✓ |

**Proibido para texto** (falham AA, medidos sobre `#FBFAFA`): `color_7` `#C2C2C2` (1,71:1) · `color_16` `#EAACAE` (1,83:1) · `color_17` `#D68084` (2,77:1) · `color_8` `#898989` (3,36:1) · `color_2` `#C44C4C` (4,49:1). Também proibido: texto `#181818` sobre `#C1272D` (3,04:1). **Unificar os pretos:** hoje coexistem `#181818`, `#000` e `#080808` — usar só `color_15`.

### 7.3 Botões — 1 primário + 1 secundário

| Estilo | Fundo | Texto | Borda | Hover | Regra de uso |
|---|---|---|---|---|---|
| **Primário** | `color_18` `#C1272D` | `color_26` `#FFFFFF` | nenhuma, raio 4px | fundo `color_19` `#811A1E` | **Um por página.** Sempre a ação de conversão da página |
| **Secundário** | transparente | `color_18` `#C1272D` | 1px `color_18` | fundo `color_18`, texto `#FFFFFF` | Ações de apoio ("Entrar na mailing", "Ver material") |

Configurar em **Editor → clicar no botão → Design → Personalizar design → Salvar como tema do botão**, para que os novos botões herdem.
Regra derivada dos achados: `/prep4consulting-2026-2` tem hoje **dois** botões "Compre agora" idênticos concorrendo; a home tem **zero**. O alvo é exatamente um primário por página.

### 7.4 Regras operacionais (as que evitam a recaída)

1. Toda tipografia vem de **Temas de Texto**. Se precisar de um tamanho novo, mude o tema — nunca a caixa.
2. Uma frase = **uma** caixa de texto. Nunca quebre palavra ou frase entre caixas.
3. Um `<h1>` por página, igual ao assunto da página. Preço, rótulo e nota de rodapé **nunca** são heading.
4. Toda imagem recebe **alt** descritivo — nunca o nome do arquivo.
5. Fotografia em **JPG** (largura máx. 1.920 px, qualidade ~80); PNG só para logo/transparência.
6. Toda mudança de layout no desktop é replicada no **editor mobile** na mesma sessão.
7. Toda mudança de slug cria o **301** na mesma sessão.

---

## 8. Tabela de SEO

Títulos ≤60 caracteres, descrições ≤155. Sufixo padronizado em **`| CCU`**. Contagem entre parênteses.

| Página (slug novo) | Título SEO proposto | Meta description proposta | Slug antigo → novo | 301 |
|---|---|---|---|---|
| `/` | `Clube de Consultoria Universitário — Unicamp` (44) | `Preparamos alunos da Unicamp e de todo o Brasil para os processos seletivos das principais consultorias estratégicas. Curso, conteúdo e alumni.` (147) | — | — |
| `/processo-seletivo` | `Processo Seletivo do CCU — seja membro \| CCU` (44) | `Faça parte do Clube de Consultoria Universitário: treinamentos, cases semanais, projetos e contato direto com consultorias. Veja etapas e prazos.` (150) | `/blank-6` | ✅ |
| `/prep4consulting` | `Prep4Consulting: curso para PS de consultoria` (45) | `Curso preparatório intensivo para processos seletivos de consultoria. Última edição: 82 alunos, nota média 9,7 e NPS 86. Desconto para bolsistas.` (149) | `/prep4consulting-2026-2` | ✅ |
| `/sobre-nos` | `Sobre o CCU: missão, visão e valores \| CCU` (42) | `O Clube de Consultoria Universitário é gerido por alunos de graduação da Unicamp e promove a carreira de consultoria estratégica e de gestão.` (144) | — | — |
| `/equipe` | `Equipe e diretoria do CCU \| CCU` (31) | `Conheça a diretoria e os assessores do Clube de Consultoria Universitário, com os cursos de graduação da Unicamp que cada um representa.` (139) | *(nova)* | — |
| `/alumni` | `Alumni do CCU: onde estão nossos ex-membros` (43) | `44 ex-membros do CCU atuam em BCG, Bain, McKinsey, Kearney, Oliver Wyman, Accenture e Mubadala. Veja a rede alumni do Clube.` (127) | `/blank` | ✅ |
| `/parceiros` | `Parceiros do CCU: consultorias parceiras \| CCU` (46) | `As consultorias parceiras do CCU ministram módulos do Prep4Consulting e participam dos nossos projetos e eventos. Conheça a parceria.` (135) | *(nova)* | — |
| `/x-ray` | `X-Ray: pesquisa de carreira na Unicamp \| CCU` (44) | `Relatório anual que mapeia o perfil e o interesse dos alunos da Unicamp pela carreira de consultoria. Edições de 2014 a 2024 para download.` (142) | — | — |
| `/consulting-womens-community` | `Consulting Women's Community (CWC) \| CCU` (40) | `Comunidade do CCU exclusiva para mulheres interessadas em consultoria: treinamentos, capacitação, mentoria e troca de experiências.` (133) | `/consulting-women-consulting` | ✅ |
| `/getting-the-job` | `Getting the Job: simulação de PS \| CCU` (38) | `Simulação completa de processo seletivo de consultoria, com cada etapa conduzida por uma consultoria parceira. Mais de 700 inscritos na 1ª edição.` (150) | — | — |
| `/conteudo` | `Conteúdo gratuito para PS de consultoria \| CCU` (46) | `Trilha gratuita de preparação: fit e case interview, revisão de indústrias, frameworks, guesstimates e casebooks completos do CCU.` (132) | — | — |
| `/entrevista` | `Case e fit interview: como funcionam \| CCU` (42) | `Entenda os dois modelos de case interview e o formato da fase de entrevistas nos processos seletivos das consultorias estratégicas.` (132) | — | — |
| `/revisao-industrias` | `Revisão de indústrias para business sense \| CCU` (47) | `Revisão de diferentes setores da economia para desenvolver business sense e se preparar para case interviews. Material em PDF do CCU.` (135) | — | — |
| `/framework` | `Frameworks para case interview \| CCU` (36) | `Estruturas sugeridas pelo CCU para os temas mais recorrentes de case interview em processos seletivos de consultoria. PDF gratuito.` (132) | — | — |
| `/guesstimate` | `Guesstimates resolvidos passo a passo \| CCU` (43) | `Guesstimates elaborados e resolvidos pelo CCU para treinar habilidade quantitativa e estruturação em case interviews. PDF gratuito.` (133) | — | — |
| `/casebooks` | `Casebooks para treinar case interview \| CCU` (43) | `O casebook próprio do CCU e um banco com 15 casebooks de MIT, Harvard, Wharton, Kellogg, Ross, Darden, ESADE, NYU e Kearney.` (127) | `/blank-2` | ✅ |
| `/casebook-ccu` | `Casebook do CCU: cases e guesstimates \| CCU` (43) | `Casebook desenvolvido pelo CCU com revisão de indústrias, informações de consultorias, frameworks, guesstimates e cases completos.` (132) | `/blank-3` | ✅ |
| `/banco-de-casebooks` | `Banco de casebooks internacionais \| CCU` (39) | `15 casebooks de MIT, Harvard, Wharton, Kellogg, Ross, Darden, ESADE, Illinois, NYU e Kearney para complementar sua preparação.` (130) | `/blank-4` | ✅ |
| `/faq` | `Perguntas frequentes sobre o CCU \| CCU` (38) | `Dúvidas sobre a carreira de consultoria, o Clube, o Processo Seletivo e o Prep4Consulting — respondidas em um só lugar.` (121) | *(nova)* | — |
| `/contato` | `Fale com o CCU \| CCU` (20) | `Entre em contato com o Clube de Consultoria Universitário por e-mail, Instagram ou LinkedIn. Respondemos em até 3 dias úteis.` (127) | `/blank-7` | ✅ |
| `/mailing` | `Mailing do CCU: vagas e eventos \| CCU` (37) | `Receba avisos de processos seletivos de consultorias, eventos, oportunidades e materiais de preparação do CCU no seu e-mail.` (126) | — | — |
| `/politica-troca` | `Política de troca e reembolso \| CCU` (35) | `Regras de troca, cancelamento e reembolso das inscrições nos cursos do Clube de Consultoria Universitário. Versão vigente de 2026.` (132) | — | — |
| `/politica-privacidade` | `Política de Privacidade \| CCU` (29) | `Como o Clube de Consultoria Universitário coleta, usa, armazena e exclui dados pessoais, conforme a LGPD. Contato do controlador.` (132) | *(nova)* | — |
| `/eventos` | `Eventos e turmas abertas \| CCU` (30) | `Próximas turmas do Prep4Consulting e eventos abertos do Clube de Consultoria Universitário, com datas e prazos de inscrição.` (127) | — | — |

### 8.1 Mapa completo de redirecionamentos 301

Criar em **Painel → SEO → Gerenciador de Redirecionamentos de URL**. **Regra:** cada 301 vai para o equivalente semântico mais próximo, nunca para `/` — exceto onde a página deixa de existir de fato (antipadrão A-2 do PoliCC).

| # | De | Para | Motivo |
|---|---|---|---|
| 1 | `/blank` | `/alumni` | slug semântico |
| 2 | `/blank-2` | `/casebooks` | slug semântico |
| 3 | `/blank-3` | `/casebook-ccu` | slug semântico |
| 4 | `/blank-4` | `/banco-de-casebooks` | slug semântico |
| 5 | `/blank-5` | `/conteudo` | Insights incorporado ao hub |
| 6 | `/blank-6` | `/processo-seletivo` | slug semântico |
| 7 | `/blank-7` | `/contato` | slug semântico |
| 8 | `/blank-1` | `/` | página excluída (era duplicata da home) |
| 9 | `/prep4consulting-2026-2` | `/prep4consulting` | slug perene |
| 10 | `/consulting-women-consulting` | `/consulting-womens-community` | nome correto do projeto |
| 11 | `/shop` | `/prep4consulting` | app desinstalado; intenção comercial |
| 12 | `/loyalty` | `/prep4consulting` | app desinstalado |
| 13 | `/book-online` | `/contato` | app desinstalado |
| 14 | `/service-page/processo-seletivo` | `/processo-seletivo` | app desinstalado |
| 15 | `/members` | `/processo-seletivo` | app desinstalado; intenção de "ser membro" |
| 16 | `/forum` | `/conteudo` | app desinstalado |
| 17 | `/blog` | `/conteudo` | app desinstalado (0 posts) |
| 18 | `/event-details/getting-the-job` | `/getting-the-job` | evento encerrado |
| 19–31 | `/event-details/prep4consulting`, `-2`, `-3`, `-4`, `-2023-2`, `-2024-1-1`, `-2024-2`, `-2025-1-2`, `-2025-1-old`, `-2025-2`, `-2025-2-1`, `-2025-2-1-1`, `/event-details/teste-1` | `/eventos` | 13 eventos encerrados/de teste |

### 8.2 Canibalização e títulos duplicados a resolver

| Problema | Páginas envolvidas | Ação |
|---|---|---|
| **3 páginas com o título `Início \| Clube de Consultoria Universitário`** | `/`, `/blank-1`, `/getting-the-job` | Excluir `/blank-1`; retitular `/getting-the-job`; manter só a home |
| **13 meta descriptions quase idênticas** (293–299 car., "O curso completo e com o melhor custo-benefício...") | 13 `/event-details/prep4consulting-*` | Excluir os eventos encerrados; a edição viva recebe descrição própria ≤155 car. |
| **Prefixo residual "N "** | `N Casebooks`, `N Insights`, `N Processo Seletivo` | Reescrever os 3 títulos |
| **3 sufixos de marca concorrentes** | `\| Clube de Consultoria` (19), `\| Clube de Consultoria Universitário` (10), `\| Clube de Consultoria Unicamp` (1) | Padronizar em `\| CCU` |
| **Duas páginas sobre "Processo Seletivo"** | `/blank-6` e `/service-page/processo-seletivo` | Manter `/processo-seletivo`; desinstalar Bookings |
| **Casebooks tratados em 3 páginas** com termos sobrepostos ("Cases completos" em `/conteudo`, `/blank-3` e `/blank-4`) | `/conteudo`, `/casebooks`, `/casebook-ccu`, `/banco-de-casebooks` | Manter a hierarquia, mas diferenciar os títulos (feito na tabela acima): "para treinar" / "do CCU" / "internacionais" |
| **`/getting-the-job` vs `/event-details/getting-the-job`** | ambas | 301 da segunda para a primeira |


---

## 9. Backlog em 3 ondas

Ordenado por (impacto × urgência) ÷ esforço. Responsáveis sugeridos: **MKT** = marketing/comunicação · **DES** = design · **DIR** = diretoria.

### Onda 1 — Higiene (dias · esforço quase zero · risco quase zero)

| # | Item | Achado | Resp. | Esf. | Critério de aceite verificável |
|---|---|---|---|---|---|
| 1.1 | Trocar o CTA do PS por estado honesto + link para mailing | C-01 | MKT | P | `/blank-6` não contém mais nenhum link para `forms.gle/gWXZmxHAxWAhH1VW8`; a frase "Não perca tempo! Garanta sua vaga no PS!" não existe no HTML |
| 1.2 | Ocultar os botões "Compre agora" e informar próxima edição | C-03 | MKT | P | `curl` em `/prep4consulting-2026-2` retorna 0 ocorrências de "Compre agora"; há 1 link para `/mailing` |
| 1.3 | Corrigir os 3 links quebrados dos casebooks | C-04 | MKT | P | Os 3 CTAs em `/conteudo`, `/blank-3` e `/guesstimate` apontam para `/casebooks` (ou `/blank-2`); nenhum tem `href` igual à raiz do site |
| 1.4 | Corrigir o rodapé global: ano e frase | C-08, C-09 | MKT | P | Todas as páginas contêm "© 2026" e "Todos os direitos reservados."; 0 ocorrências de "©2023" e de "Todos os seus são direitos reservados" |
| 1.5 | Excluir `/blank-1` + 301 → `/` | C-07 | MKT | P | `/blank-1` retorna 301; apenas 1 página no site tem o título "Início \| ..." |
| 1.6 | Corrigir o título SEO de `/getting-the-job` | C-07 | MKT | P | `<title>` de `/getting-the-job` não contém "Início" |
| 1.7 | Ocultar `/eventos` do menu e da busca enquanto não houver edição aberta | C-08 | MKT | P | `/eventos` não aparece em `pages-sitemap.xml` **ou** não exibe "0 DIAS PARA O EVENTO" |
| 1.8 | Remover o link obsoleto para o evento de 2023 na página do curso | C-08 | MKT | P | `/prep4consulting-2026-2` tem 0 links para `/event-details/prep4consulting-2023-2` |
| 1.9 | Revisão ortográfica das 20 correções de texto listadas | C-09 | MKT | M | Busca por "tem têm", "prepararam", "Prepara-se", "processo seletivos", "os tema", "e partir desses", "Essas essas", "Mastecard", "Enterpreneurship", "Engenhria" retorna 0 no site |
| 1.10 | Consolidar frases fragmentadas (`Presidentes anterior`+`es`, `+ módulos d`+`e`, `O`/`Clube`/`está`) | C-09 | DES | M | Cada frase existe em uma única caixa; nenhuma palavra quebrada entre elementos |
| 1.11 | Eliminar o rótulo visível "Âncora 1" | C-09 | DES | P | 0 ocorrências de "Âncora 1" no HTML de desktop **e** de mobile |
| 1.12 | Excluir os 14 eventos encerrados + 301 → `/eventos` | C-12 | MKT | M | `event-pages-sitemap.xml` lista ≤2 URLs; 0 ocorrências de "teste" e "(old)" |
| 1.13 | Desinstalar Forum, Stores, Loyalty, Bookings, Members Area e Blog + 301 | C-11 | DIR + MKT | P | `/shop`, `/forum`, `/loyalty`, `/book-online`, `/members`, `/blog`, `/service-page/processo-seletivo` retornam 301; `pages-sitemap.xml` cai de 28 para ~21 |
| 1.14 | Remover os textos soltos do mobile do curso | C-05 | DES | P | HTML mobile de `/prep4consulting-2026-2` tem 0 ocorrências de "Faça perguntas de clarificação" e "Avalie os dados cuidadosamente" |
| 1.15 | Substituir/remover o e-book "PS 2022.1" | C-08 | MKT | P | `/blank-6` não linka arquivo cujo nome contenha "2022.1" |
| 1.16 | Corrigir "4 opções" na política e divulgar a taxa de 2,5% na página de preço | C-21 | DIR + MKT | P | `/politica-troca` cita o nº real de opções; `/prep4consulting-2026-2` menciona "taxa de serviço" |
| 1.17 | Datar a política de troca e trocar "14/jul" por regra relativa | C-08 | DIR | P | 0 ocorrências de "14/jul"; a página contém "Versão vigente desde" |

### Onda 2 — Estrutura (semanas)

| # | Item | Achado | Resp. | Esf. | Critério de aceite verificável |
|---|---|---|---|---|---|
| 2.1 | Renomear os 7 slugs `blank-*` + criar os 31 redirects 301 | C-19, §8.1 | MKT | M | 0 URLs `blank-*` em `pages-sitemap.xml`; todos os 31 slugs antigos retornam 301 para o destino da tabela §8.1 |
| 2.2 | Pôr "Processo Seletivo" e "Prep4Consulting" no 1º nível do menu | C-02 | DIR + DES | P | O HTML do menu contém links para `/processo-seletivo` e `/prep4consulting`; 0 páginas órfãs no grafo de links internos |
| 2.3 | Reestruturar a home (H1 + números + funil duplo + prova) | C-06 | DES + MKT | G | `/` tem exatamente 1 `<h1>`; contém "82", "9,7", "86" e "19"; contém 1 link para `/processo-seletivo` e 1 para `/prep4consulting` |
| 2.4 | Criar `/faq` com 3 categorias em acordeão | B-3 | MKT | G | `/faq` responde 200, está no menu, tem ≥12 perguntas em ≥3 grupos e 1 `<h1>` |
| 2.5 | Criar `/contato` a partir de `/blank-7` | C-23 | MKT | P | `/contato` tem >150 palavras de conteúdo, está no menu, e `/blank-7` retorna 301 |
| 2.6 | Extrair `/equipe` de `/sobre-nos` e reconstruir com Repetidor | C-10 | DES + DIR | G | `/equipe` tem 1 `<h1>`; cada pessoa tem exatamente 1 nome, 1 curso e 1 cargo; `/sobre-nos` cai de 58 headings para ≤10 |
| 2.7 | Criar `/parceiros` (deixa de ser âncora) | B-4 | MKT + DIR | M | `/parceiros` responde 200, está no menu, descreve a contrapartida da parceria e tem logos com alt text |
| 2.8 | Criar `/politica-privacidade` e linkar no rodapé | C-13 | DIR | M | `/politica-privacidade` responde 200 e é linkada de todas as páginas |
| 2.9 | Ajustar o formulário de mailing (consentimento, gênero opcional, finalidade) | C-13 | MKT | P | O campo de gênero não é obrigatório; existe caixa de consentimento; a finalidade está declarada no formulário |
| 2.10 | Aplicar os 6 Temas de Texto e remover overrides nas 5 páginas principais | C-15, §7.1 | DES | G | `<span style="...font-...">` cai de 141/página para ≤20/página em `/`, `/prep4consulting`, `/sobre-nos`, `/processo-seletivo`, `/conteudo` |
| 2.11 | Corrigir a hierarquia de headings em todas as páginas | C-18 | DES | M | Toda página tem exatamente 1 `<h1>`; nenhuma tem >12 headings; `/alumni` cai de 44 `<h1>` para 1 |
| 2.12 | Reconstruir a ementa do curso em 4 blocos (1 por ciclo), desktop e mobile | C-05 | DES | M | "Estrutura do PS" aparece no HTML de desktop **e** de mobile; a ordem Ciclo 1→2→3→4 é sequencial em ambos |
| 2.13 | Converter o cronograma de imagem em tabela de texto | C-14 | MKT + DES | M | As datas da edição aparecem como texto no HTML de `/prep4consulting` |
| 2.14 | Reescrever alt text das imagens-chave | C-14 | MKT | M | 0 imagens com `alt` igual ao nome do arquivo nas 8 páginas principais; 0 `alt=""` em imagem informativa |
| 2.15 | Preencher as 20 meta descriptions ausentes | C-20 | MKT | M | 0 páginas sem meta description; nenhuma acima de 155 caracteres |
| 2.16 | Substituir tons de contraste insuficiente em texto | C-16 | DES | M | 0 texto usando `color_7`, `color_8`, `color_16`, `color_17`; texto secundário usa `color_14` |
| 2.17 | Recomprimir as imagens acima de 1 MB e os PDFs do X-Ray | C-17 | DES | M | Nenhuma imagem servida acima de 500 KB; nenhum PDF acima de 10 MB |
| 2.18 | Card de bolsista com peso igual aos demais | C-21 | DES + DIR | M | A seção de preços tem 3 cards de mesmo tamanho, um deles "Bolsista — R$ 70,00" |

### Onda 3 — Evolução (semestre)

| # | Item | Achado | Resp. | Esf. | Critério de aceite verificável |
|---|---|---|---|---|---|
| 3.1 | Nomear, por módulo, qual consultoria parceira ministra | B-2 | DIR | G | `/prep4consulting` associa ≥3 módulos a ≥3 consultorias nomeadas |
| 3.2 | Publicar o X-Ray 2025 e/ou 2026 | C-08 | DIR | G | `/x-ray` linka relatório de 2025 ou posterior |
| 3.3 | Dar prova e porta de entrada ao CWC | C-22 | DIR + MKT | G | `/consulting-womens-community` tem ≥2 dados verificáveis e 1 CTA funcional |
| 3.4 | Atualizar o Getting the Job com dados da última edição | C-22 | DIR | M | A página cita a edição mais recente, não a 1ª; 0 ocorrências de "Essas essas" |
| 3.5 | Migrar para e-mail em domínio próprio | C-23 | DIR | M | O rodapé usa `@consultoriaunicamp.com`; 0 ocorrências de `equipeccu@gmail.com` |
| 3.6 | Atualizar o Casebook CCU e publicar o arquivo (hoje o CTA não entrega nada) | C-04 | DIR | G | O CTA de `/casebook-ccu` aponta para um PDF que responde 200 |
| 3.7 | Decidir sobre blog: produzir 3 posts ou manter desinstalado | B-11 | DIR | G | Ou `/blog` não existe, ou tem ≥3 posts e aparece na home |
| 3.8 | Padronizar os logos de parceiros (mesma altura, fundo transparente, alt) | §7.4 | DES | M | Todos os logos de `/parceiros` têm a mesma altura renderizada e alt com o nome da empresa |
| 3.9 | Renovar os casebooks do banco (mais recente é de 2019) | Inventário | DIR | G | O banco inclui ≥3 casebooks de 2022 ou posteriores |
| 3.10 | Página de Transparência | B-12 | DIR | G | Página publicada com prestação de contas do último exercício |
| 3.11 | Revisar a taxonomia do campo de gênero no mailing | C-13 | DIR + MKT | P | As opções não misturam identidade de gênero com condição trans |
| 3.12 | Unificar as categorias "Presidentes anteriores" e "Ex-Presidentes" em `/alumni` | S-2 | MKT | P | `/alumni` tem categorias mutuamente exclusivas (MECE) |

---

## 10. Checklist de manutenção recorrente

### 10.1 A cada edição do Prep4Consulting

**Antes de abrir as inscrições**

- [ ] Criar **um** evento no Wix Events, com slug limpo (`prep4consulting-2027-1`) — nunca duplicar um evento antigo, porque é assim que nascem os slugs `-2`, `-3`, `-2025-2-1-1`.
- [ ] Conferir se o H1 e o título do evento têm a edição correta e **sem espaço no final**.
- [ ] Escrever meta description **única** para o evento, ≤155 caracteres (não reaproveitar a dos 13 anteriores).
- [ ] Atualizar o cronograma **como texto**, não como imagem nova (C-14).
- [ ] Atualizar os 4 números da última edição na home e na página do curso: alunos · nota média · NPS · cursos de graduação.
- [ ] Conferir os 3 cards de preço, incluindo o de bolsista, e a menção à taxa de serviço de 2,5%.
- [ ] Atualizar `/politica-troca`: prazo relativo correto + "Versão vigente desde MM/AAAA".
- [ ] Reexibir os botões de compra (ocultados ao fim da edição anterior) e conferir que apontam para o evento **novo**.
- [ ] Publicar `/eventos` no menu.
- [ ] Verificar no **editor mobile** que todas as alterações apareceram.

**Ao fechar as inscrições (mesmo dia)**

- [ ] Ocultar os botões "Compre agora" e publicar o aviso de próxima edição + captura de lista de espera.
- [ ] Ocultar `/eventos` do menu **e** dos motores de busca.
- [ ] Trocar o CTA do PS/curso por link para `/mailing`.

**Ao encerrar a edição**

- [ ] Excluir o evento da edição **anterior à anterior** e criar o 301 para `/eventos`.
- [ ] Conferir `event-pages-sitemap.xml`: deve listar no máximo 2 URLs.
- [ ] Arquivar os números da edição encerrada e substituir pelos novos.

### 10.2 A cada troca de diretoria

- [ ] Atualizar `/equipe`: nome, curso e cargo de cada pessoa — **conferir individualmente**, este foi o erro C-10.
- [ ] Mover os que saíram para `/alumni`, com empresa e cargo atuais.
- [ ] Atualizar o ano do rodapé (© AAAA).
- [ ] Reabrir/atualizar o formulário do Processo Seletivo e conferir que **não** está em `/closedform`.
- [ ] Substituir o e-book do PS pela edição vigente.
- [ ] Repassar as credenciais do Wix, do Google Drive dos materiais e do e-mail institucional.
- [ ] Registrar quem é o responsável pelo site no semestre.

### 10.3 Auditoria trimestral (30 minutos, qualquer pessoa)

- [ ] Abrir `consultoriaunicamp.com/pages-sitemap.xml` e `event-pages-sitemap.xml`. **Toda** URL listada precisa ter dono e propósito. Se aparecer `blank-*`, `cópia-*`, `teste`, `old` ou `copy-of-*`: excluir + 301.
- [ ] Conferir que nenhuma página nova está órfã: toda página publicada deve receber link do menu, do rodapé ou de outra página.
- [ ] Clicar em **todos** os CTAs do site. Qualquer um que caia na home é link quebrado (foi assim que 15 casebooks sumiram).
- [ ] Buscar no site por datas passadas apresentadas como futuras e por contadores em "0 dias".
- [ ] Abrir a home, `/prep4consulting` e `/processo-seletivo` **no celular** e comparar com o desktop: mesmo conteúdo, mesma ordem.
- [ ] Confirmar que o ano do rodapé é o corrente.
- [ ] Testar os links externos: Google Forms (não deve estar em `closedform`), Drive (deve abrir sem pedir acesso), PDFs.
- [ ] Rodar o **Assistente de configuração de SEO do Wix** (Painel → SEO) e zerar as pendências.
- [ ] Conferir se algum texto novo foi formatado manualmente em vez de usar Temas de Texto.

### 10.4 Regra de ouro para não reacumular entulho

> **No Wix, "ocultar do menu" ≠ "ocultar da busca" ≠ "despublicar" ≠ "excluir".**
> Uma página oculta do menu continua publicada, indexável e no sitemap — foi exatamente assim que o CCU acumulou 21 páginas órfãs e o PoliCC 35 páginas `cópia-*`.
> Quando uma página deixa de servir: **exclua e crie o 301**. Se precisar preservar histórico, exclua a página e guarde o conteúdo fora do site (Drive).
> E nunca duplique uma página para criar a próxima edição: duplicar é a origem de `blank-1`…`blank-7` e de `prep4consulting-2025-2-1-1`.

---

## Apêndice — Correções ao Anexo A do briefing

Revalidei os 25 itens do Anexo A. **21 confirmados**, 3 imprecisos, 1 incompleto:

| Item do Anexo A | Veredito | Observação |
|---|---|---|
| `/blank-4` ("Banco de Casebooks") está "só rodapé, sem conteúdo" | ❌ **Incorreto** | Tem 114 palavras e **15 links de casebook, todos HTTP 200 `application/pdf`**. O problema não é vazio: é ser órfã (C-04) |
| `/blank-2` (Casebooks) não citada como problema | ⚠️ **Incompleto** | É **órfã**, e é a raiz da vertical morta. A causa é o link de "Cases completos" em `/conteudo` |
| `/forum` está "só rodapé, sem conteúdo" | ⚠️ **Impreciso** | Não está vazia: exibe erro em inglês — `Widget Didn't Load / Check your internet and refresh this page.` |
| `/shop` está "só rodapé, sem conteúdo" | ⚠️ **Impreciso** | Exibe "Não temos nenhum produto…" **e** tem meta description anunciando "inscrições abertas" |
| Só `/blank-1` duplica o título da home | ⚠️ **Incompleto** | São **três** páginas com `Início \| Clube de Consultoria Universitário`: `/`, `/blank-1` e **`/getting-the-job`** |
| Sufixo alterna entre 2 formas | ⚠️ **Incompleto** | São **3**: `\| Clube de Consultoria`, `\| Clube de Consultoria Universitário` e `\| Clube de Consultoria Unicamp` (`/blog`) |
| "~10 edições antigas do Prep4Consulting" | ✔️ Confirmado (preciso: **14**) | 15 páginas de evento, 14 residuais |
| PoliCC `/projetos` e `/perguntas-frequentes` "retornaram só o rodapé" | ❌ **Incorreto** | `/perguntas-frequentes` tem FAQ real (3 categorias, 6+ perguntas, 561 palavras) e `/projetos` tem conteúdo. São as **melhores** referências de padrão a adotar (B-3) |
| Demais itens (©2023, "Todos os seus são direitos reservados", "tem têm", "prepararam", "VALOR", "Nossos pilares" repetido, "Âncora 1", asterisco solto, Ciclo 2/3, "0 DIAS", "14/jul", `/loyalty` com "Sign up to the site", slugs `blank-*`, prefixo "N ", nome do CWC inconsistente, menu, ativos subaproveitados, rodapé do PoliCC, `cópia-*` do PoliCC, títulos em minúsculas) | ✔️ **Todos confirmados** | — |

**Achados relevantes que não constavam do Anexo A:** formulário do PS em `/closedform` (C-01) · `/blank-6` órfã (C-02) · "Compre agora" → "Vendas encerradas" (C-03) · os 3 CTAs de casebook apontando para a home (C-04) · divergência desktop/mobile com perda de conteúdo (C-05) · home sem nenhum `<h1>` (C-06) · `/getting-the-job` com o título da home (C-07) · `/service-page/processo-seletivo` (não estava no inventário) · ausência total de política de privacidade e gênero obrigatório no mailing (C-13) · cronograma como imagem e alt = nome de arquivo (C-14) · 3.948 overrides de fonte (C-15) · `color_16`/`color_17`/`color_8` reprovando WCAG AA em uso (C-16) · PDF de 54,6 MB e imagens de 6,8 MB (C-17) · nenhuma página usando H3/H4/H5 (C-18) · 20 meta descriptions vazias (C-20) · taxa de R$ 4,75 não divulgada e "4 opções" inexistentes (C-21) · cargos e nomes trocados na equipe (C-10) · `/equipe` do PoliCC = 404 e menu do PoliCC sobre 9 páginas `cópia-*` (A-1, A-2).


---

## Adendo — Coleta no LinkedIn e no Instagram (16/09/2026)

Coleta complementar feita a pedido, para associar imagens aos eventos. **Instagram
(`@ccuclubedeconsultoria`): não verificado** — exige autenticação, redirecionou para
`/accounts/login`. **LinkedIn (`/company/clube-de-consultoria-universitario`): público**, rendeu
17 imagens e informação que **contradiz o site**. Entregue como PDF ilustrado em
`Guia-Execucao-Wix-CCU.pdf`.

### A.1 Achados que alteram conclusões do relatório

| ID | Achado | Efeito no relatório |
|---|---|---|
| **L-01** | `[FATO]` O **CWC 2026 está em andamento** — 3ª edição, 7 sessões de 19/08 a 24/09/2026, com **McKinsey, Accenture, Kearney, Roland Berger, Bain & Company, Peers e BCG**. A sessão de 16/09 é a da Bain; encerra em 24/09. | **Agrava C-22 de forma decisiva.** Não é uma página fraca de um projeto parado: é a página mais fraca do site descrevendo o projeto **mais ativo** do clube, em pleno curso, com 7 consultorias de primeira linha. Sobe para o topo da Onda 2. |
| **L-02** | `[FATO]` O **PS 2026.2 rodou de 17/08 a 07/09/2026** e foi divulgado com *"Inscreva-se pelo link nos comentários"* — não pelo site. | **Agrava C-01 e C-02.** O clube conduziu a captação principal **sem usar o site**. A página do PS ficou órfã durante toda a campanha. O site não é parte do funil hoje. |
| **L-03** | `[FATO]` O formulário linkado em `/blank-6` é o **"Formulário de Inscrição PS Interno CCU 2022.1"**. | **Corrige C-01.** Não é só "formulário fechado": é o formulário **errado**, de 4 anos atrás — coerente com o e-book "PS 2022.1" na mesma página. A página está congelada em 2022.1. |
| **L-04** | `[FATO]` A peça do cronograma do Prep4Consulting 2026.2 traz **dia, hora, módulo e a consultoria de cada módulo**: McKinsey (20/07), BCG (24/07), EloGroup (27/07), Kearney (28/07), Visagio (29/07), btc (30/07), Bain (31/07). | **Corrige B-2.** O relatório recomendava *adotar do PoliCC* o padrão de nomear o parceiro por módulo. O CCU **já produz isso** — só não publica no site. A recomendação deixa de ser "criar" e passa a ser "transcrever", o que reduz o esforço de G para M. Resolve C-14 no mesmo movimento. |
| **L-05** | `[FATO]` Existe **desconto de grupo** não divulgado no site: *"4 a 7 pessoas: 40% OFF · 8 a 12: 50% OFF · 13 ou mais: 60% OFF"*, via cupom por e-mail. | **Amplia C-21.** Um desconto de até 60% ausente da página de vendas. Reforça o achado de transparência comercial e a política de acesso. |
| **L-06** | `[FATO]` Datas conflitantes: LinkedIn diz **"Inscrições até 19/07"** (dois posts); o site diz **"Inscrições até 17/07/2026"**. | Novo achado de frescor: **dois prazos diferentes publicados** para a mesma edição. |
| **L-07** | `[FATO]` O clube usa a tagline **"CCU — da Unicamp para o Mundo"** (perfil e banner do formulário) e informa **"Criado em 2011"**; tem **1.854 seguidores**. Nada disso está no site. | **Insumo para C-06.** A home não precisa inventar proposta de valor: já existe uma tagline consolidada e 15 anos de história para citar. |
| **L-08** | `[FATO]` As 17 peças do LinkedIn pesam **79–167 KB**; as imagens do site chegam a **6.839 KB**, **5.189 KB** e **3.082 KB**. | **Reforça C-17.** O material gráfico do próprio clube é ~40× mais leve do que o publicado. |
| **L-09** | `[FATO]` A identidade real usa **fundo escuro** com vermelho, amarelo e verde; o CWC tem sub-marca própria em **tom mauve**. O site usa fundo off-white `#FBFAFA`. | **Refina C-16.** Recalculado: `#EAACAE` (9,31:1), `#D68084` (6,16:1), `#C2C2C2` (9,97:1) e `#898989` (5,08:1) **passam AA sobre `#181818`** e reprovam sobre `#FBFAFA`; o vermelho `#C1272D` faz o oposto (3,04:1 no escuro, 5,61:1 no claro). Os rosas não são erro de paleta — são a sub-marca do CWC, desenhada para fundo escuro. A regra correta é **escolher a cor conforme o fundo da seção**, não banir os rosas. |
| **L-10** | `[FATO]` Dois ativos de conteúdo já produzidos e não publicados no site: um **glossário de termos de consultoria** (3 cartões) e um post **"6 diferenciais"** do curso. | Alimenta `/conteudo` e `/faq` (itens 2.4 e 3.7) sem produção nova. |

### A.2 Conclusão do adendo

O diagnóstico central do relatório se mantém, mas com uma inversão importante de causa.
`[FATO OBSERVADO]` O CCU **não tem** um problema de produção de conteúdo: produz cronograma
detalhado, prova de parceria, glossário, política de desconto e campanha de PS — com regularidade e
qualidade gráfica melhor que a do site. `[HIPÓTESE]` O site não está no fluxo de trabalho do clube:
as campanhas nascem e morrem no Instagram e no LinkedIn, e o site virou um arquivo de 2022–2023 que
ninguém abre. Isso explica por que 21 das 44 URLs são órfãs, por que o rodapé está em ©2023 e por
que a página do PS aponta para um formulário de 2022.1.

`[RECOMENDAÇÃO]` Acrescentar um item à rotina de manutenção (§10.3): **a cada post de campanha no
LinkedIn ou Instagram, atualizar a página correspondente do site no mesmo dia.** É o único item
deste relatório que não corrige um defeito, e sim a causa deles.
