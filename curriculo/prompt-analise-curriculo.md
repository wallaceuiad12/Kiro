# Prompt — Auditoria e Revisão Completa de Currículo

> Uso: cole o bloco abaixo em uma IA (Claude, ChatGPT, Gemini) **junto com o arquivo**
> `prints/CV - Matteo Lucato.pdf` anexado. Se a ferramenta não aceitar anexo, cole o
> texto do currículo no lugar indicado.

---

## PROMPT

Você é um revisor sênior de currículos para processos seletivos competitivos em
finanças e consultoria no Brasil (bancos de investimento, consultorias estratégicas,
private equity, asset management). Você já triou milhares de currículos de
universitários e sabe exatamente o que faz um recrutador descartar um candidato em
7 segundos.

Sua tarefa: **auditar o currículo anexado por completo, identificar todos os problemas
e aplicar as correções que julgar viáveis**, entregando uma versão revisada.

### REGRA INVIOLÁVEL — não inventar

Este currículo descreve a vida real de uma pessoa. Você **não tem** acesso aos fatos
por trás dele.

- Nunca crie, infle ou substitua um dado por outro dado inventado.
- Se uma correção depende de informação que você não tem, **não adivinhe**: escreva a
  sugestão como uma pergunta na seção "Perguntas abertas" e deixe o texto original
  marcado como pendente.
- Ao remover um número, **não coloque outro número no lugar**. Reescreva sem número.
- Você pode reformular, reordenar, cortar, reenquadrar e melhorar redação livremente.
  Você não pode alterar a substância factual: cargos, empresas, datas, escopo real.

### MUDANÇAS JÁ DETERMINADAS (aplicar sem discutir)

Estas cinco decisões já foram tomadas e validadas pelo candidato. Aplique-as
literalmente e **não** as reabra para discussão nem as liste como perguntas.

**1. Data de formatura.** A formação na UNICAMP está como `Fevereiro 2023 – Julho 2027`.
Corrija o término para **Dezembro 2027**. Verifique se essa data aparece em outro ponto
do documento e ajuste em todos.

**2. Data de início na Nunes&Lucato.** Está como `Fevereiro 2022 – Dezembro 2025`.
Corrija o início para **Fevereiro 2023**, ficando `Fevereiro 2023 – Dezembro 2025`.
Isso elimina a incoerência de o cargo começar antes do ingresso na graduação. Ao aplicar,
confira se algum bullet dessa experiência faz referência a período anterior a 2023 e
ajuste a redação para não contradizer a nova data — o bullet que cita `(2023–2024)` e
`por +1 ano` deve permanecer coerente.

**3. Paralelismo gramatical.** O bullet da IME Jr que começa com substantivo
(`Condução de análise SWOT, identificando...`) rompe o padrão dos demais, todos em
primeira pessoa do passado. Corrija para:

> `Conduzi análise SWOT, identificando pontos fortes (captação de recursos) e análise de
> despesas operacionais via Excel para otimização de custos, resultando em uma economia
> mensal de 20% para a empresa júnior.`

Depois varra o documento inteiro e garanta que **todos** os bullets abram com verbo em
primeira pessoa do passado, sem exceção.

**4. Atribuição de crédito no primeiro bullet da V4 Company.** A redação atual sugere
que o candidato — analista júnior — comandou a alocação de R$ 5M/ano, o que soa
inflado e convida a uma pergunta desconfortável em entrevista. O valor deve aparecer
como **escopo do orçamento que ele apoiava**, não como decisão dele. Substitua:

> **Antes:** `Conduzi análises mensais de DRE, modelagem financeira e projeções de
> caixa, elaborando relatórios gerenciais que embasaram a alocação de +R$ 5M/ano e
> otimizaram a precisão das previsões em 15%.`
>
> **Depois:** `Conduzi análises mensais de DRE, modelagem financeira e projeções de
> caixa, produzindo os relatórios gerenciais que a diretoria usava para decidir a
> alocação de um orçamento anual superior a R$ 5M.`

A mudança preserva a dimensão real (orçamento de R$ 5M é escopo verificável), devolve a
decisão a quem a tomou e sai mais natural. O `15% de precisão das previsões` foi removido
por não ter base de comparação declarada — ver categoria B do protocolo abaixo; se o
candidato fornecer o antes/depois do erro de previsão, pode voltar.

Aplique o mesmo raciocínio a **qualquer outro** bullet onde o candidato reivindique
resultado que pertence ao time ou à liderança.

**5. Excesso de quantificação.** Hoje **100% dos bullet points contêm número ou
percentual**. Essa uniformidade produz o efeito oposto do pretendido: em vez de parecer
orientado a resultado, o currículo parece construído para impressionar, e passa a
impressão de que os números foram fabricados. Corrija conforme o protocolo abaixo.

### PROTOCOLO PARA A QUESTÃO DOS NÚMEROS

Não se trata de apagar métricas — métrica boa é o que diferencia um currículo. Trata-se
de **manter só as que se sustentam sob pergunta em entrevista**.

Classifique **cada** bullet em uma das quatro categorias e trate conforme:

| Categoria | Critério | Ação |
|---|---|---|
| **A — Sólida** | O número tem unidade natural, fonte óbvia e o candidato saberia explicar como chegou nele (volume de transações, toneladas, orçamento, nº de alunos, nº de respostas) | **Mantém** |
| **B — Sem lastro** | O número é plausível, mas exige uma base de comparação que o currículo não dá ("reduziu X em 25%" — de quanto para quanto?) | Mantém **só se** o candidato fornecer a base; senão reescreve sem número e registra em "Perguntas abertas" |
| **C — Não-mensurável** | O número quantifica algo que não tem unidade natural (rastreabilidade, engajamento, precisão subjetiva, qualidade de processo) | **Remove o número obrigatoriamente.** É o tell mais forte de invenção |
| **D — Contraproducente** | O número é verdadeiro mas pequeno demais, e quantificá-lo chama atenção para o tamanho modesto do feito | **Remove o número.** Descreva o escopo qualitativamente |

Alvo final: **entre 40% e 60% dos bullets com métrica**, concentradas nas de categoria A.
O resto deve convencer por escopo e especificidade, não por dígito.

**Como reescrever um bullet ao tirar o número:** um bullet sem número não pode virar
vago — isso seria uma piora. Substitua o número por especificidade concreta: qual
ferramenta, para qual área, que decisão aquilo destravou, qual era a complexidade real.
"Padronizei o arquivo financeiro e jurídico da empresa júnior, criando a estrutura de
pastas e a convenção de nomes que passou a ser usada pelos times seguintes" é mais
forte que "aumentei a rastreabilidade em 40%" — e é defensável.

**Atenção especial** aos bullets que quantificam rastreabilidade, engajamento de marca
e precisão de previsão: são os candidatos mais prováveis à categoria C.

### EIXOS DE AUDITORIA COMPLETA

Além do acima, examine e corrija:

**1. Consistência cronológica e credibilidade**
Com as datas já corrigidas nos itens 1 e 2 acima, **refaça** a linha do tempo completa e
confronte todas as entradas entre si. Verifique o que restou:
- Períodos com três ou mais vínculos simultâneos. Após a correção, o intervalo
  `Agosto 2025 – Dezembro 2025` concentra Nunes&Lucato, IME Jr e Clube de Consultoria ao
  mesmo tempo, e `Janeiro 2026 – Agosto 2026` concentra V4 e Clube de Consultoria.
  É plausível para estudante, mas avalie se a redação deixa claro o caráter de
  atividade extracurricular e não sugere carga impossível.
- Qualquer bullet cujo período interno contradiga as datas novas do cabeçalho.
- Lacunas não explicadas.

**2. Atribuição de crédito (além do caso já resolvido)**
O primeiro bullet da V4 já foi corrigido no item 4 acima. Varra **todos os demais**
buscando o mesmo padrão: resultado de time ou de liderança apresentado como conquista
individual. Reenquadre para a contribuição real sem diminuir o feito. Atenção aos verbos
que prometem mais autoridade do que o cargo tinha.

**3. Paralelismo gramatical (verificação)**
A correção pontual está no item 3 acima. Aqui, confirme o resultado: percorra os doze
bullets e ateste que todos abrem com verbo em primeira pessoa do passado. Reporte a lista
verificada.

**4. Alocação de espaço**
Em currículo de uma página, cada linha compete. Avalie:
- Detalhamento de ensino médio e fundamental em candidato de 4º/5º ano de graduação —
  quase sempre desperdício. Ensino fundamental não pertence a um currículo universitário.
- Endereço residencial completo: sem função e expõe dado pessoal. Cidade/estado basta.
- Telefone sem formatação.
- O espaço liberado deve ir para experiência e resultado.

**5. Categorização das seções**
Verifique se cada item está na seção correta. Certificações profissionais listadas como
disciplinas acadêmicas, colocação em competição listada como certificação, e título de
seção cuja ordem não corresponde à ordem interna do conteúdo são erros de organização
que sinalizam descuido.

**6. Representação de certificações em andamento**
Credenciais como CFA têm regras próprias de como a candidatura pode ser declarada.
Verifique se a redação está correta e sinalize se o status depende de matrícula
efetivada.

**7. Subvenda e contradição interna**
Procure onde o currículo se contradiz **para baixo**. Exemplo do tipo a caçar: nível de
idioma declarado como intermediário/avançado quando o próprio documento menciona
formação em currículo internacional naquele idioma. Isso é inconsistência que custa
oportunidade.

**8. Linguagem vazia**
Marque e substitua expressões que não dizem nada verificável: "melhores práticas de
mercado", "impacto positivo", "dezenas de", "visando otimização". Troque por fato
concreto ou corte.

**9. Leitura por ATS**
Sinalize qualquer elemento que quebre parsing automático: caracteres especiais em
bullets, dado de contato em posição não convencional, densidade insuficiente de termos
técnicos que a vaga-alvo exige.

**10. Teste final dos 7 segundos**
Ao terminar, releia como recrutador com 7 segundos. O que salta primeiro? É o ativo mais
forte do candidato? Se não, reordene.

### FORMATO DE SAÍDA

Entregue exatamente nesta ordem:

**1. Diagnóstico** — os 5 problemas mais graves, em ordem de impacto, uma frase cada.

**2. Tabela de alterações** — toda mudança aplicada:

| # | Seção | Antes (literal) | Depois | Categoria | Por quê |
|---|---|---|---|---|---|

Para bullets, informe a categoria (A/B/C/D) do protocolo de números.

**3. Currículo revisado completo** — texto integral, pronto para uso, preservando a
estrutura de uma página.

**4. Perguntas abertas** — toda correção que você **não** aplicou por falta de
informação factual, cada uma como pergunta direta e respondível. Seja específico: em vez
de "confirmar os números", pergunte "a inadimplência caiu de qual patamar para qual?".

**5. Contagem de métricas** — quantos bullets tinham número antes, quantos têm depois,
e a lista de quais foram preservados com a justificativa de cada.

### TEXTO DO CURRÍCULO

```
Matteo Lucato
Rua Engenheiro Edward de Vita Godoy, 909 | 11945911942
m246226@dac.unicamp.br | linkedin.com/in/matteo-lucato

FORMAÇÃO ACADÊMICA

UNICAMP — São Paulo, Brasil
Bacharelado em Economia (Instituto de Economia)          Fevereiro 2023 – Julho 2027
● Disciplinas Relevantes: Finanças Corporativas, Contabilidade e Análise de Balanços,
  Econometria, Estatística, Derivativos e Gestão de Portfólio, Matemática Financeira,
  Mercado de Capitais e Métodos Computacionais.
● CPA-20, Candidato ao CFA Nível 1

Agostiniano Mendel — São Paulo, Brasil
Ensino Médio, Ensino Fundamental
● Calvert Academy: High School Internacional com ênfase em Economia, Tecnologia,
  Finanças e Matemática
  ○ Disciplinas Relevantes: AP Economics, AP Statistics, Introduction to Careers in
    Finance, Fundamentals of Programming / Coding.

EXPERIÊNCIA PROFISSIONAL

V4 Company — Campinas, Brasil
Analista Financeiro Júnior                              Janeiro 2026 – Agosto 2026
● Conduzi análises mensais de DRE, modelagem financeira e projeções de caixa,
  elaborando relatórios gerenciais que embasaram a alocação de +R$ 5M/ano e
  otimizaram a precisão das previsões em 15%.
● Administrei fluxo de caixa, conciliação bancária e rotinas de contas a pagar/receber
  (+400 transações/mês), implementando controles diários rigorosos que reduziram a
  taxa de inadimplência corporativa em 25%.
● Reestruturei rotinas financeiras visando melhores práticas de mercado e mitigação de
  riscos, garantindo 100% de rastreabilidade em auditorias e Due Diligence, reduzindo
  o tempo de fechamento mensal em 20%.

Nunes&Lucato — São Paulo, Brasil
Gestor de Projetos                                      Fevereiro 2022 – Dezembro 2025
● Prospectei e mantive parcerias estratégicas (NK Store, Track&Field) por +1 ano,
  garantindo alocação total de resíduos e impulsionando aumento de 35% na receita e
  60% em volume (2023–2024).
● Gerenciei projetos de upcycling (Midea, Carrier, Santista S.A.), administrando
  orçamento de R$ 150 mil para produzir mais de 2.500 itens, elevando o engajamento
  sustentável das marcas em 15%.
● Supervisionei o projeto Bom Retiro Recicla, realocando mais de 40 toneladas/mês de
  resíduos têxteis para reciclagem, evitando assim o descarte inadequado e gerando
  impacto sustentável positivo.

ATIVIDADES EXTRACURRICULARES E POSIÇÕES DE RELEVÂNCIA

IME Jr — São Paulo, Brasil
Analista Financeiro, Departamento Jurídico-Financeiro    Agosto 2024 – Dezembro 2025
● Estruturei modelos preditivos em Python e extração de dados em SQL para projetos nos
  setores de Saúde e Transporte, processando e analisando grandes bases de informações
  (+1,2M de registros).
● Condução de análise SWOT, identificando pontos fortes (captação de recursos) e
  análise de despesas operacionais via Excel para otimização de custos, resultando em
  uma economia mensal de 20% para a empresa júnior.
● Organizei mais de 12 pastas financeiras e jurídicas (fluxo de caixa, orçamentos,
  contratos e notas fiscais), padronizando o ambiente digital e aumentando a
  rastreabilidade documental em 40%.

Clube de Consultoria da Unicamp — São Paulo, Brasil
Diretor de Gestão de Pessoas                            Agosto 2025 – Agosto 2026
● Atuei como instrutor no programa Prep4Consulting, ministrando aulas de Finanças e
  Case Interview para mais de 100 alunos, capacitando os participantes na estruturação
  e resolução de problemas para processos seletivos.
● Conduzi sessões de preparação no programa Getting the Job, realizando mais de 30
  simulações de entrevistas e revisões estratégicas de currículo, capacitando dezenas
  de candidatos para vagas nas principais consultorias.
● Colaborei na promoção do XRAY 2025, censo da Unicamp focado em identificar o
  interesse dos alunos no mercado de consultoria, registrando um recorde de 626
  respostas em apenas 2 semanas.

INTERESSES E HABILIDADES

Habilidades Técnicas: Pacote Office (Avançado), Python, SQL, Power BI, VBA.
Outras Certificações: Curso de Financial & Valuation Modelling (WSP), Semifinalista do
Challenge Ágora, Excel Avançado (Fundação Bradesco), Derivativos e Gestão de Portfólio
(GMF), Análise de Demonstrações Financeiras (GMF).
Línguas: Fluente em Português, Avançado em Inglês, Intermediário em Espanhol.
Interesses: Jogar tênis, Xadrez, Ler livros de não-ficção.
```
