# Guia de preparação · Boutique de IA · Projeto Cold Chain

Gerado a partir de `prompt-guia-boutique-ia.md`.
Versão aprofundada, com escopo do projeto incorporado.

Como usar. Leia a Parte 1 e a Parte 2 antes de qualquer coisa, porque elas
definem o terreno. As Partes 3 a 6 são o conteúdo técnico que sustenta a conversa.
As Partes 7 a 12 são operacionais, para usar na véspera.

Aviso de honestidade intelectual. Nenhum número neste guia é dado do cliente.
Benchmarks de mercado estão com fonte no final. Números de exemplo estão
rotulados como ilustrativos e servem só para você treinar a aritmética ao vivo.

---

## Parte 1. Decodificando a fala do interlocutor

A frase dele tem quatro informações de escopo embutidas. Quem percebe isso entra
na conversa com vantagem.

**"A gente está finalizando uma etapa do projeto de Cold Chain"**

Projeto já em curso, com uma fase entrando em encerramento. Em boutique de IA
aplicada, essa primeira fase é quase sempre diagnóstico, mapeamento de processo,
levantamento de dados disponíveis e priorização de casos de uso. O artefato final
dela costuma ser um diagnóstico com oportunidades quantificadas e um roadmap.
Consequência prática para você. Não chegue propondo diagnóstico, porque ele já
foi feito. Chegue perguntando o que o diagnóstico encontrou e o que ficou de fora.

**"que eu acho que é onde você vai agregar mais"**

Ele está te alocando mentalmente na fase seguinte, não na que está fechando.
Isso quer dizer trabalho de estruturação, documentação, modelagem e acompanhamento
de execução. É exatamente o tipo de trabalho em que seu repertório é verificável,
reestruturação de rotinas de fechamento, documentação de controles internos,
rastreabilidade de lançamento até comprovante, padronização de arquivo e
construção de base documental que sobreviveu a auditoria e due diligence.
Cadeia do frio é um ambiente regulado, e ambiente regulado premia exatamente
essa habilidade.

**"A gente vai ter que desenhar o playbook da área, como ela funciona"**

Aqui está o ponto mais importante e o mais fácil de ler errado. "Como ela funciona"
não é documentação do estado atual, é desenho de operating model. A área
provavelmente é nova, foi recém criada, ou está sendo reestruturada depois do
diagnóstico. O trabalho é definir processos, papéis, decisões, indicadores, rituais
e ferramentas de uma função que ainda não opera em regime. Isso é organizational
design com camada de IA, não projeto de tecnologia.

**"e provavelmente vamos executar essa implementação junto com eles"**

Três leituras. Primeira, o modelo de engajamento é híbrido, a boutique senta dentro
da operação do cliente em vez de entregar relatório e sair. Segunda, a palavra
"provavelmente" indica que essa fase ainda não está vendida ou não está assinada,
então existe uma proposta a ser construída, e quem ajuda a construir o caso dela
vira peça necessária do time. Terceira, implementação conjunta é o momento em que
projeto de IA morre ou vira resultado, porque é onde a adesão das pessoas entra
na equação.

Pergunta de abertura que demonstra essa leitura toda em uma frase.
"Quando você diz desenhar como a área funciona, estamos falando de formalizar o que
já acontece hoje ou de criar uma função que ainda não existe em regime?"

---

## Parte 2. One-pager de escopo do projeto

Formato que uma boutique usaria de verdade. Os campos marcados com **H** são
hipóteses a validar na conversa, não fatos.

| Campo | Conteúdo |
|---|---|
| Situação | Cliente opera ou depende de cadeia do frio e contratou a boutique para estruturar a gestão dessa cadeia com apoio de IA **H** |
| Complicação | Perda térmica, retrabalho e exposição regulatória não são gerenciáveis porque não existe processo formal nem dado confiável no nível do elo **H** |
| Pergunta central | Como transformar controle de temperatura em uma função gerida, com decisão padronizada e inteligência preditiva embarcada |
| Objetivo da fase atual | Encerrar diagnóstico com oportunidades priorizadas e roadmap |
| Objetivo da próxima fase | Desenhar o playbook da área, a estrutura de papéis e a arquitetura de decisão |
| Objetivo da fase seguinte | Implementar junto com o cliente e transferir a operação |

### Fases, entregáveis e critérios de aceite

| Fase | Trabalho | Entregável | Critério de aceite |
|---|---|---|---|
| F0 · Diagnóstico (encerrando) | Mapeamento da cadeia, inventário de dados e sensores, baseline de perda e desvio, priorização de casos de uso | Diagnóstico, baseline quantificado, roadmap | Baseline aceito pelo cliente como número oficial da casa |
| F1 · Desenho do playbook | Definição de processos, SOPs, RACI, SLA, árvore de KPIs, matriz de escalonamento, arquitetura de dados mínima, especificação dos casos de uso de IA | Playbook da área em versão 1.0, dicionário de indicadores, especificação funcional | Dono de cada processo nomeado e indicador calculável com o dado que existe hoje |
| F2 · Implementação conjunta | Construção dos modelos e painéis, piloto em escopo fechado, treinamento das pessoas, ajuste do playbook contra a realidade | Piloto em produção, playbook v1.1 revisado pelo uso, trilha de treinamento | Piloto rodando com usuário do cliente operando, não o consultor |
| F3 · Run e transferência | Estabilização, cadência de gestão em pé, plano de escala para outros elos | Manual de operação, plano de escala, critérios de saída | Área sustenta a cadência sem a boutique por um ciclo completo |

### Papéis na fase de desenho e implementação

| Papel | Responsabilidade |
|---|---|
| Sócio ou gerente da boutique | Relação com o patrocinador, escopo e venda da fase seguinte |
| Líder de delivery | Arquitetura da solução e coerência entre playbook e tecnologia |
| Analista de negócio (sua posição provável) | Desenho de processo, SOPs, árvore de KPIs, business case, documentação, acompanhamento de execução |
| Cientista ou engenheiro de dados | Pipeline, modelo preditivo, integração com telemetria e ERP ou WMS |
| Dono do processo no cliente | Decide, assina o SOP e responde pelo indicador |
| Patrocinador no cliente | Libera recurso e remove bloqueio político |

### Riscos do escopo, com antídoto

| Risco | Por que acontece | Antídoto |
|---|---|---|
| Playbook virar documento morto | Foi escrito pela consultoria e não pelo dono do processo | Cada SOP tem um dono nomeado do lado do cliente que escreve junto e assina |
| Dado insuficiente para o caso de uso priorizado | Diagnóstico priorizou valor sem checar viabilidade de dado | Em F1, cada caso de uso recebe uma ficha de pré-requisito de dado antes de entrar no roadmap |
| Escopo de implementação sem fronteira | "Executar junto com eles" é elástico por natureza | Definir em contrato o elo, a praça e a família de produto do piloto |
| Resistência da operação | Quem mede desvio passa a ser avaliado por desvio | Primeiro ciclo sem punição, com foco em registro correto, e meta só no ciclo seguinte |
| Piloto que não escala | Falta de dono, de orçamento de run e de integração | Critério de saída do piloto inclui orçamento de sustentação aprovado |

---

## Parte 3. Cadeia do frio sem floreio

### O conceito que separa amador de quem entende

Cadeia do frio não é caminhão refrigerado, é cadeia de custódia térmica. O produto
precisa provar que ficou dentro da faixa em todos os elos, incluindo as transições.
A implicação é que o problema quase nunca está no meio do trajeto com o motor
ligado, está nas transições e nas esperas, porque é ali que a responsabilidade
troca de mãos e o monitoramento costuma ter buraco.

### Faixas típicas

| Faixa | Temperatura | Exemplos |
|---|---|---|
| Ultracongelado | abaixo de -60 °C | algumas vacinas de mRNA, material biológico |
| Congelado | -18 °C ou menos | proteína, sorvete, polpa, alimento industrializado congelado |
| Refrigerado | 2 °C a 8 °C | vacinas em geral, biológicos, insulina, laticínios, hortifruti sensível |
| Fresco ou resfriado | 0 °C a 10 °C, varia por produto | carne resfriada, pescado, flores, frutas e vegetais |
| Temperatura controlada ambiente | 15 °C a 25 °C ou até 30 °C | boa parte dos medicamentos sólidos |

Nota prática. Faixa estreita é mais caríssima de operar que faixa baixa. Manter
2 a 8 °C é mais difícil que manter -18 °C, porque a janela é de seis graus e
qualquer parada em doca consome essa janela rápido.

### Os elos e onde a perda realmente acontece

1. Produção e embalagem primária, onde o produto entra na cadeia já na temperatura correta ou não entra nunca.
2. Armazenagem em câmara fria, com risco de estratificação térmica, ponto quente perto de porta e de evaporador, e falha de energia.
3. Expedição e doca, o elo mais crítico, porque é onde o produto fica exposto ao ambiente durante conferência, paletização e carregamento.
4. Transporte primário, em carreta ou contêiner refrigerado, com risco de set point errado, de falha de equipamento e de pré-resfriamento não feito.
5. Cross-docking e transbordo, onde o produto é manuseado por quem não é dono dele.
6. Espera em pátio e fila de recebimento, risco subestimado porque o veículo pode ficar horas com motor desligado.
7. Last mile, com abertura repetida de porta, embalagem passiva com validação limitada e entrega que falha e volta.
8. Recebimento e armazenagem no destino, onde o produto pode ficar na antecâmara esperando conferência.

Se em algum momento você tiver que escolher uma frase para mostrar domínio, use
esta. "Na maior parte das operações, o desvio não acontece em viagem, acontece em
doca e em espera, e normalmente é justamente ali que o monitoramento tem buraco."

### Conceitos técnicos que você precisa saber nomear

| Conceito | O que é | Por que importa |
|---|---|---|
| Excursão térmica | Episódio em que a temperatura sai da faixa especificada | É o evento central que o playbook precisa saber tratar |
| Desvio | Registro formal da excursão, com investigação e decisão sobre o lote | Transforma um evento físico em processo com rastro |
| Tempo fora de refrigeração | Soma acumulada do tempo em que o produto ficou fora da faixa ao longo da vida | Muitos produtos têm orçamento total de exposição, não um único limite |
| Temperatura cinética média | Temperatura única equivalente ao efeito cumulativo de um perfil de temperatura variável | Permite decidir liberar ou descartar um lote com base técnica em vez de medo |
| Mapeamento térmico | Estudo que identifica pontos quentes e frios de câmara ou baú | Define onde o sensor fica e onde não se deve paletizar produto sensível |
| Qualificação térmica | Comprovação documentada de que instalação, operação e desempenho atendem ao especificado | Exigência regulatória em medicamentos e base para defesa em auditoria |
| Validação de embalagem | Teste do sistema de embalagem passiva contra perfis de temperatura de pior caso | Sustenta a promessa de autonomia da caixa térmica em horas |
| Sistema passivo e sistema ativo | Passivo usa massa térmica, gelo ou gel, ativo usa equipamento com controle | Define custo, autonomia e dependência de energia |
| Data logger e telemetria | Registro local lido depois contra transmissão em tempo real | Só telemetria permite intervenção antes da perda, logger só permite autópsia |
| Calibração rastreável | Certificado que liga o sensor a um padrão metrológico | Sem isso, o dado não vale em auditoria nem como prova contratual |
| APPCC ou HACCP | Metodologia de análise de perigos e pontos críticos de controle | É o esqueleto conceitual que o playbook de alimentos vai herdar |

### Regulação brasileira aplicável

Depende do vertical, e descobrir o vertical é uma das suas primeiras perguntas.

Medicamentos. A referência é a [RDC 430/2020 da ANVISA](https://crfsp.org.br/noticias/11492-rdc-430-2020.html),
que dispõe sobre boas práticas de distribuição, armazenagem e transporte de
medicamentos, [atualizada pela RDC 653/2022](https://www.arghi.com.br/transporte-de-termolabeis-legislacao-e-boas-praticas).
Ela é o que [introduziu formalmente o conceito de qualificação térmica e a exigência de validação](https://accmetrologia.com.br/validacao-e-qualificacao-termica-na-industria-farmaceutica/)
nesse elo da cadeia. Conteúdo rephraseado para conformidade de licenciamento.

Alimentos. A lógica muda, com vigilância sanitária e, para produtos de origem
animal, exigências do MAPA, apoiadas em APPCC e em controle de temperatura por
tipo de produto. Vale confirmar com o interlocutor em vez de afirmar.

Vacinas em rede pública. Entra a lógica de rede de frio do Programa Nacional de
Imunizações, com instrumentos próprios de monitoramento e de tratativa de desvio.

Por que isso muda o projeto. Em ambiente regulado, o playbook não é só eficiência,
é prova. Cada decisão precisa deixar rastro auditável, e isso impõe requisito
direto sobre a arquitetura de dados e sobre o nível de autonomia que você pode
dar a um modelo.

### A economia da cadeia, que é onde você joga em casa

Os blocos de custo que o playbook precisa endereçar.

1. Perda de produto por desvio, que é o número mais visível e geralmente o mais mal medido.
2. Custo de energia em câmara e em equipamento de transporte, sensível a set point e a abertura de porta.
3. Custo de ativo térmico, em embalagem reutilizável, gelo técnico e sensor, com ciclo de retorno que quase ninguém controla.
4. Custo de retrabalho, em reentrega, recoleta e reprocesso de documentação.
5. Multa contratual e penalidade de nível de serviço com cliente e com canal.
6. Custo de exposição regulatória, de interdição de lote a recall, que é baixo em frequência e alto em severidade.
7. Custo de capital parado em estoque imobilizado por lote em quarentena aguardando decisão.

Mercado, para calibrar tamanho. A logística de cadeia do frio no Brasil é estimada
em torno de [USD 5,64 bilhões em 2026, com projeção de USD 6,92 bilhões até 2031](https://www.mordorintelligence.com/industry-reports/brazil-cold-chain-logistics-market).
Conteúdo rephraseado para conformidade de licenciamento.

---

## Parte 4. Onde a IA entra de verdade, e onde ela é teatro

Organize em camadas de maturidade. Essa é a estrutura que vai te fazer soar como
alguém que já viu projeto de IA de perto.

| Camada | O que faz | Técnica típica | Pré-requisito de dado |
|---|---|---|---|
| 1 · Descritiva | Enxergar a cadeia em um só lugar, com dado de temperatura, localização e identidade do ativo | Integração, modelagem de dados, painel, torre de controle | Telemetria com granularidade de minutos e chave que liga sensor, ativo, rota e lote |
| 2 · Diagnóstica | Explicar por que o desvio aconteceu e onde se concentra | Clusterização, análise de causa raiz, atribuição por rota, doca, turno e transportador | Histórico de desvio com registro de contexto, não só a curva de temperatura |
| 3 · Preditiva | Antecipar excursão, falha de equipamento e demanda de capacidade refrigerada | Séries temporais, gradient boosting, redes recorrentes, manutenção preditiva | Série histórica longa com rótulo de evento confiável |
| 4 · Prescritiva | Recomendar a ação, de roteirização dinâmica a decisão de liberar ou descartar lote | Otimização, simulação, regra de decisão apoiada em temperatura cinética média | Modelo de custo por decisão e especificação de estabilidade do produto |
| 5 · Agêntica | Executar a tratativa de desvio ponta a ponta, abrir o registro, reunir evidência, redigir investigação e acionar quem decide | Agentes com ferramenta, recuperação de documento, geração de texto com trilha de auditoria | Processo já formalizado, com SOP, porque agente sem processo só automatiza bagunça |

### Os casos de uso que valem a conversa

**Previsão de excursão com antecedência útil.** O ganho não é prever, é dar tempo
de agir. Existe literatura mostrando previsão de excursão com horas de antecedência
usando temperatura, umidade e outras variáveis ambientais, por exemplo um estudo
que relata [previsão com cerca de 3,5 horas de antecedência e R² próximo de 0,91](https://wjarr.com/sites/default/files/fulltext_pdf/WJARR-2026-0350.pdf).
A pergunta de consultor não é qual a acurácia, é o que a operação consegue fazer
em 3,5 horas. Se a resposta for nada, o modelo não vale nada.
Conteúdo rephraseado para conformidade de licenciamento.

**Manutenção preditiva do equipamento de refrigeração.** Compressor, evaporador,
porta e vedação. Falha de equipamento gera desvio correlacionado e caro, e esse é
um dos poucos casos em que o retorno aparece sem depender de mudança de comportamento.

**Decisão sobre lote após desvio.** Hoje muita operação descarta por precaução ou
libera por pressão comercial, as duas sem base técnica. Um motor que calcula
exposição acumulada contra a especificação de estabilidade do produto transforma
isso em decisão defensável. Esse é provavelmente o caso de uso com melhor relação
entre valor e esforço, porque reduz perda sem pedir sensor novo.

**Roteirização e sequenciamento sensíveis a risco térmico.** Não é só minimizar
distância, é minimizar exposição acumulada, priorizando o produto mais sensível no
início da rota e evitando o horário de pico de calor.

**Previsão de demanda para alocação de capacidade refrigerada.** Câmara ociosa e
câmara em overbooking são dois problemas de previsão, não de operação.

**Visão computacional em doca.** Checagem de lacre, de paletização e de porta
aberta além do tempo. Útil, porém depende de infraestrutura física e costuma ser
fase dois, não piloto inicial.

**Agente de tratativa de desvio e de resposta a auditoria.** Reúne a evidência,
monta o dossiê, propõe a investigação e o plano de ação, e deixa a decisão com o
responsável técnico. Em ambiente regulado, humano no circuito não é opção de
design, é requisito.

### Onde IA não é a resposta

Diga isso na conversa, porque é o que diferencia alguém que vai somar de alguém que
vai concordar com tudo.

1. Se o elo não tem sensor, o projeto é de instrumentação e de contrato com transportador, não de modelo.
2. Se o cadastro mestre de produto não tem a faixa correta de temperatura, nenhum modelo acerta, porque o rótulo está errado na origem.
3. Se o problema é tempo de doca, a solução provável é agendamento e layout, com o modelo servindo apenas para provar o tamanho do problema.
4. Se o contrato com o transportador não prevê penalidade nem obrigação de telemetria, o ganho não é capturável, é apenas visível.
5. Se ninguém é dono do indicador, o painel vira enfeite em seis semanas.

### O dado de mercado que você usa para se posicionar como cético competente

A taxa de mortalidade de piloto de IA é brutal. Pesquisas de 2026 colocam a
proporção de pilotos de agentes que não chegam a produção na casa dos
[88%](https://ud.hk/en/blogs/insight/article/2026-05-12-ai-agent-pilot-failure?),
há levantamento do MIT indicando que a maioria dos pilotos corporativos
[não entrega retorno mensurável](https://www.project44.com/blog/why-95-percent-of-ai-agent-pilots-fail-in-supply-chains/),
e o Gartner projeta que mais de
[40% das iniciativas de IA agêntica sejam canceladas até o fim de 2027](https://debales.ai/blog/agentic-ai-pilots-fail-logistics-scoping),
por custo, valor pouco claro e controle de risco insuficiente.
Conteúdo rephraseado para conformidade de licenciamento.

Como usar isso sem parecer pessimista. "O que me chama atenção nesse escopo é que
vocês estão desenhando o playbook antes de escalar a tecnologia. A maior parte dos
pilotos de IA morre exatamente por falta disso, então a ordem aqui está certa."

---

## Parte 5. Anatomia de um playbook de área

### A distinção que você precisa dominar

Playbook, SOP e runbook não são sinônimos, e confundi-los é o erro mais comum.
O playbook define o modo de operar da área, com propósito, fronteira, processos,
papéis, decisões e indicadores. O SOP padroniza uma tarefa repetível, com passo,
responsável e evidência. O runbook dá instrução para um cenário específico, do tipo
o que fazer quando a câmara perde energia às duas da manhã.
Conteúdo rephraseado para conformidade de licenciamento, com base em
[material sobre níveis de detalhe entre playbook, SOP e runbook](https://www.moxo.com/blog/operations-playbooks-template-library).

Em projeto de cadeia do frio, você precisa dos três. O playbook vende a área
internamente, os SOPs fazem a operação funcionar e os runbooks evitam que crise
dependa de improviso.

### Sumário proposto do playbook, em doze blocos

1. **Mandato da área.** Por que ela existe, qual problema ela responde, qual é a fronteira com logística, com qualidade e com comercial. Sem isso, o resto é organograma sem função.
2. **Escopo da cadeia.** Elos cobertos, famílias de produto, faixas de temperatura, praças, canais e parceiros envolvidos.
3. **Mapa de processos.** Processo ponta a ponta, com nível 1 de macroprocesso e nível 2 de atividade, e indicação de onde a decisão acontece.
4. **Catálogo de SOPs.** Lista dos procedimentos com dono, frequência, evidência exigida e data de revisão.
5. **Runbooks de exceção.** Falha de energia, falha de equipamento em trânsito, desvio em entrega, recusa de recebimento, perda de sensor, apreensão de carga.
6. **Estrutura e RACI.** Quem executa, quem decide, quem é consultado e quem é informado, por processo e não por cargo.
7. **Níveis de serviço e matriz de escalonamento.** Tempo máximo para registrar desvio, para decidir sobre lote, para comunicar cliente, com o degrau de escalonamento de cada estouro.
8. **Árvore de indicadores.** Indicador de resultado, indicador de processo e indicador de insumo, com dono, fórmula, fonte e frequência.
9. **Arquitetura de dados e ferramentas.** Fontes, integrações, dicionário de dados, regras de qualidade, onde os modelos de IA entram e qual é o nível de autonomia permitido em cada decisão.
10. **Cadência de gestão.** Ritual diário de desvio, ritual semanal de performance, revisão mensal de negócio, revisão trimestral do próprio playbook.
11. **Capacitação.** Trilha por papel, material, avaliação e critério de habilitação para quem opera decisão com efeito sanitário.
12. **Governança do documento.** Versão, aprovação, registro de mudança e gatilhos de revisão obrigatória, por exemplo mudança regulatória ou entrada de nova família de produto.

### RACI, exemplo de recorte ilustrativo

| Processo | Analista de cold chain | Operação e armazém | Qualidade | Transportador | Comercial |
|---|---|---|---|---|---|
| Monitoramento contínuo de temperatura | R | C | I | C | I |
| Registro de desvio | R | C | A | I | I |
| Decisão de liberar ou descartar lote | C | I | A e R | I | C |
| Tratativa com transportador | R | C | C | A | I |
| Comunicação ao cliente final | C | I | C | I | A e R |
| Revisão de SOP | A e R | C | C | I | I |

A regra de ouro do RACI em ambiente regulado. Decisão com efeito sanitário tem
accountable técnico nomeado, e isso não delega para modelo.

### Governança de IA dentro do playbook

Inclua um bloco curto definindo, para cada caso de uso, qual é o nível de autonomia
permitido. Três níveis bastam. Informar, em que o modelo só mostra. Recomendar, em
que o modelo sugere e o humano aprova. Agir, em que o modelo executa dentro de
limite pré-aprovado e registra. Ter esse quadro explícito é o que impede a discussão
emocional sobre confiar ou não na IA, e é também o que uma
[matriz de governança com responsabilidade clara por etapa do ciclo de vida](https://elevateconsult.com/insights/designing-the-ai-governance-operating-model-raci/)
busca resolver. Conteúdo rephraseado para conformidade de licenciamento.

---

## Parte 6. Árvore de indicadores e a conta do business case

### Árvore de indicadores

Resultado, o que o patrocinador olha.

1. Perda térmica em percentual do valor expedido.
2. Custo total da cadeia do frio por caixa ou por palete entregue.
3. Nível de serviço térmico, pedidos entregues dentro da faixa e com documentação completa.
4. Exposição regulatória, número de não conformidades abertas e tempo médio de fechamento.

Processo, o que a área gerencia no dia.

1. Taxa de excursão por elo, separando armazenagem, doca, transporte primário e last mile.
2. Tempo médio de permanência em doca e em pátio.
3. Tempo médio para registrar e para decidir um desvio.
4. Percentual de lotes recuperados após desvio, ou seja, liberados com base técnica em vez de descartados por precaução.
5. Aderência a SOP em auditoria interna.

Insumo, o que sustenta o resto.

1. Cobertura de monitoramento, percentual de embarques com telemetria e não apenas com logger.
2. Disponibilidade e qualidade do dado, percentual de séries sem lacuna.
3. Sensores com calibração vigente.
4. Taxa de retorno de embalagem térmica reutilizável.
5. Percentual de equipe habilitada na trilha de treinamento.

### A conta, com números ilustrativos

Todos os valores abaixo são inventados para treinar o raciocínio em voz alta.
Nunca apresente como se fossem do cliente.

Premissas ilustrativas. Volume anual expedido de 240 mil caixas. Valor médio de
R$ 400 por caixa, então R$ 96 milhões expedidos. Taxa de desvio de 3% dos embarques,
ou 7.200 caixas afetadas. Hoje, 70% das caixas afetadas são descartadas por
precaução, 5.040 caixas, o que dá R$ 2,016 milhões de perda. Custo de retrabalho e
reentrega de R$ 60 por caixa afetada, R$ 432 mil. Perda total ilustrativa em torno
de R$ 2,45 milhões por ano.

Três alavancas, com efeito separado.

| Alavanca | Mecanismo | Efeito ilustrativo |
|---|---|---|
| Decisão técnica sobre lote | Calcular exposição acumulada contra estabilidade do produto e cair de 70% para 40% de descarte | Evita 2.160 caixas, cerca de R$ 864 mil |
| Previsão de excursão com ação | Reduzir a taxa de desvio de 3% para 2,2% com intervenção antecipada em parte dos casos | Evita 1.920 caixas afetadas, cerca de R$ 653 mil entre perda e retrabalho |
| Disciplina de doca e pátio | Agendamento e limite de porta aberta, atacando o elo com maior concentração de desvio | Parte do ganho acima, então cuidado para não contar duas vezes |

A frase que mostra maturidade. "Essas alavancas se sobrepõem, então eu não somaria
os três números. Em business case de cadeia do frio, o erro mais comum é contar o
mesmo desvio evitado em duas iniciativas diferentes."

E a pergunta que vem depois, que é a boa. "Qual é a parcela desse ganho que é
capturável no exercício atual e qual depende de renegociação de contrato com
transportador ou de investimento em sensor?"

---

## Parte 7. Implementação conjunta, plano de 30, 60 e 90 dias

**Dias 1 a 30. Fechar fronteira e baseline.**
Escolher um recorte de piloto com elo, praça e família de produto definidos.
Nomear dono de processo do lado do cliente para cada SOP. Validar se o dado
necessário existe de fato, com extração real e não com promessa de sistema.
Publicar o dicionário de indicadores e congelar o baseline com o cliente assinando
embaixo, porque baseline discutido depois do resultado destrói qualquer projeto.

**Dias 31 a 60. Operar o playbook em modo manual antes de automatizar.**
Rodar a tratativa de desvio com o SOP na mão, sem modelo, para descobrir onde o
processo quebra. Subir o painel descritivo e a cadência diária. Treinar a equipe.
Começar a construir o modelo preditivo com o histórico já limpo nessa etapa. Essa
sequência parece lenta e é o que mais aumenta a chance de a coisa durar.

**Dias 61 a 90. Ligar a inteligência e provar valor em escopo fechado.**
Colocar o modelo em sombra, comparando previsão com o que aconteceu, antes de
deixá-lo disparar ação. Medir contra o baseline. Revisar o playbook com o que a
realidade mostrou, publicando a versão 1.1. Preparar o caso de escala, com
orçamento de sustentação explícito e critérios de saída da boutique.

### Modos de falha mais prováveis nessa fase

| Falha | Sinal precoce | Antídoto |
|---|---|---|
| Piloto que depende do consultor | O consultor é quem abre o registro de desvio | A partir da semana 6, consultor só observa e corrige |
| Baseline contestado no fim | Cliente diz que o ano foi atípico | Baseline assinado no dia 30, com definição de fórmula |
| Modelo bom sem ação possível | Alerta chega e ninguém tem autoridade para desviar a carga | Definir no SOP quem pode decidir e em quanto tempo, antes do modelo existir |
| Explosão de escopo | Pedidos de painel para outras áreas | Backlog único, com fila e dono, e repriorização só no ritual semanal |
| Dado que degrada | Séries começam a ter lacuna depois do piloto | Indicador de qualidade de dado entra na árvore de KPIs com dono |

---

## Parte 8. Perguntas para você fazer, por fase da conversa

**Para entender o projeto.**

1. Quando você diz que está finalizando uma etapa, o entregável dela é diagnóstico com roadmap ou já é especificação de solução?
2. O cliente está no vertical de farma, de alimentos ou de outro produto termolábil? A regulação muda completamente o desenho do playbook.
3. A área de cadeia do frio já existe no organograma ou vai nascer com esse projeto?
4. Quais elos da cadeia são próprios e quais são terceirizados? O ganho capturável depende muito disso.
5. O diagnóstico conseguiu quantificar a perda por elo ou ficou no agregado?

**Para entender o dado.**

6. Hoje o monitoramento é telemetria em tempo real ou logger lido depois do fato?
7. Existe chave que conecte o dado de temperatura ao lote, ao pedido e ao transportador, ou essas bases vivem separadas?
8. Qual a cobertura de monitoramento em last mile, que é normalmente o elo mais cego?
9. Existe histórico de desvio com registro de causa, ou só a curva de temperatura?

**Para entender o playbook.**

10. Quem vai ser o dono dos processos do lado do cliente depois que a gente sair?
11. Hoje a decisão de descartar ou liberar lote após desvio é técnica ou é por precaução?
12. Existe um SOP escrito hoje, mesmo que ruim, ou a gente parte do zero?
13. O playbook vai precisar passar por qualidade e por assuntos regulatórios para ser válido?

**Para entender o modelo de engajamento.**

14. Quando você diz executar junto com eles, o time da boutique fica dentro da operação do cliente ou atua em cadência de acompanhamento?
15. Essa fase de implementação já está contratada ou ainda vai ser proposta? Posso ajudar a montar o caso dela?
16. O que, nesse projeto, você considera que precisa estar de pé para a boutique sair sem que a área regrida?

A pergunta 16 é a melhor da lista. Ela mostra que você está pensando em
sustentação, que é a dor real de quem vende implementação.

---

## Parte 9. Perguntas que você vai receber, com respostas âncora

Use o repertório verificável. Nada de inventar experiência em logística que você
não tem. A ponte honesta é entre controle, rastreabilidade e dado, que é
exatamente o que cadeia do frio exige.

**"Você já trabalhou com logística ou cadeia do frio?"**
Seja direto. Não com cadeia do frio. Depois faça a ponte. Em operação física de
coleta e upcycling de resíduo têxtil, você gerenciou fluxo com dezenas de toneladas
mensais e parceria com rede varejista, o que te deu noção de operação com
contraparte, janela e volume. E na frente de controle, você reestruturou rotinas de
fechamento e documentação de controles internos de modo que cada lançamento ficasse
rastreável até o comprovante de origem, que é a mesma exigência estrutural de uma
cadeia de custódia térmica, só que com temperatura no lugar de valor.

**"Por que a gente deveria te colocar nessa fase do projeto?"**
Porque desenho de playbook é 70% de estruturação e documentação defensável e 30%
de conteúdo técnico novo, e a parte estruturante é onde você tem resultado
comprovado. Você já construiu a base documental que sustentou auditoria e due
diligence em uma operação real, já padronizou arquivo e convenção de nomes para
tornar documento localizável, e já traduziu operação em relatório gerencial que
diretoria usou para decidir alocação de orçamento.

**"O que você faria nos primeiros 30 dias?"**
Responda com a Parte 7 resumida. Fronteira do piloto, dono de processo nomeado,
validação de que o dado existe com extração real, dicionário de indicadores
publicado e baseline assinado. E explicite o motivo. Projeto de IA em operação
regulada morre por falta de dono e por baseline contestado, não por falta de modelo.

**"Qual caso de uso de IA você priorizaria?"**
Decisão técnica sobre lote após desvio, porque ataca a maior fonte de perda, não
exige investimento novo em sensor e produz um artefato auditável. Previsão de
excursão vem depois, condicionada à existência de uma ação possível dentro da
janela de antecedência. E diga a frase sobre o que a operação consegue fazer em
três horas.

**"Você sabe modelar isso?"**
Seja preciso sobre o nível. Python e SQL com uso real, incluindo modelos preditivos
e extração sobre base de mais de 1,2 milhão de registros em projetos de saúde e
transporte. Você não é cientista de dados sênior, e a posição provável não pede
isso. O que você entrega é a tradução entre a operação e o time de dados, com
especificação de indicador, lógica de negócio e validação do resultado.

**"Qual a sua maior dúvida sobre o projeto?"**
Boa oportunidade. Use a sustentação. A dúvida é como a área mantém a cadência
depois da saída da boutique, porque playbook sem ritual de gestão e sem dono vira
PDF arquivado.

---

## Parte 10. Glossário mínimo, português e inglês

| Português | Inglês | Observação |
|---|---|---|
| Cadeia do frio | Cold chain | Cadeia de custódia térmica ponta a ponta |
| Excursão térmica | Temperature excursion | Evento central do playbook |
| Desvio | Deviation | Registro formal com investigação |
| Temperatura cinética média | Mean kinetic temperature | Base técnica para decidir sobre lote |
| Tempo fora de refrigeração | Time out of refrigeration | Orçamento cumulativo de exposição |
| Mapeamento térmico | Thermal mapping | Identifica ponto quente e ponto frio |
| Qualificação térmica | Thermal qualification | Instalação, operação e desempenho |
| Validação de embalagem | Package validation | Teste contra perfil de pior caso |
| Registrador de dados | Data logger | Leitura posterior, serve para autópsia |
| Telemetria | Real time monitoring | Permite intervir antes da perda |
| Última milha | Last mile | Elo mais cego e mais caro |
| Doca e transbordo | Dock and cross docking | Onde o desvio mais acontece |
| Ação corretiva e preventiva | CAPA | Artefato que fecha o desvio |
| Torre de controle | Control tower | Camada descritiva da solução |
| Humano no circuito | Human in the loop | Requisito em decisão com efeito sanitário |
| Perda e quebra | Shrinkage e spoilage | Spoilage é perda por deterioração |
| Pré-resfriamento | Pre cooling | Baú resfriado antes do carregamento |
| Ponto de ajuste | Set point | Erro de set point é causa banal e frequente |

---

## Parte 11. Armadilhas de postura

1. Não repita de volta o que ele disse com outras palavras. Ele vai notar na hora.
2. Não cite acurácia de modelo sem falar da ação que ela habilita. Acurácia sem decisão é vaidade técnica.
3. Não prometa número sobre o negócio dele. Fale em estrutura de ganho e pergunte qual parcela é capturável.
4. Não use IA como substantivo mágico. Diga qual camada, qual dado e qual decisão.
5. Não trate o playbook como documentação. Trate como desenho de função, com dono, decisão e indicador.
6. Não esconda o que você não sabe. Em boutique, honestidade calibrada é critério de contratação, porque o cliente senta ao seu lado.
7. Não entre sem ter pelo menos uma pergunta sobre sustentação depois da saída da consultoria.
8. Evite falar em percentual de melhoria sem base. Se citar benchmark, cite a fonte e o contexto.

---

## Parte 12. Checklist das 48 horas finais

1. Reler as Partes 1, 2 e 8 deste guia, que são as que aparecem na conversa.
2. Decorar cinco termos técnicos da Parte 10 e usar dois ou três, não dez.
3. Treinar em voz alta a conta da Parte 6, inclusive a ressalva sobre não somar alavancas.
4. Pesquisar a boutique. Casos publicados, verticais, se o posicionamento é estratégia com IA ou engenharia de IA aplicada.
5. Checar se o cliente final ou o setor dele está identificável, porque isso define a regulação aplicável.
6. Preparar duas histórias de 90 segundos, uma de estruturação e documentação, outra de dado e modelo.
7. Escolher três perguntas da Parte 8 para fazer de qualquer jeito, incluindo a 16.
8. Ter uma resposta pronta e curta para a pergunta sobre não ter experiência em cadeia do frio, sem rodeio e sem desculpa.

---

## Fontes

Todas as referências abaixo foram parafraseadas, sem reprodução literal
significativa de trecho. Conteúdo rephraseado para conformidade com restrições de
licenciamento.

- [RDC 430/2020, boas práticas de distribuição, armazenagem e transporte de medicamentos, CRF-SP](https://crfsp.org.br/noticias/11492-rdc-430-2020.html)
- [Atualização pela RDC 653/2022 e transporte de termolábeis](https://www.arghi.com.br/transporte-de-termolabeis-legislacao-e-boas-praticas)
- [Qualificação térmica e validação na indústria farmacêutica](https://accmetrologia.com.br/validacao-e-qualificacao-termica-na-industria-farmaceutica/)
- [Desafios do transporte de medicamentos sob a RDC 430/2020](https://blog.pqegroup.com/pt-br/assuntos-regulatorios-farmacovigilancia/desafios-no-transporte-de-medicamentos-sob-a-rdc-430/2020-da-anvisa)
- [Mercado brasileiro de logística de cadeia do frio, Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/brazil-cold-chain-logistics-market)
- [Previsão de excursão térmica com IoT e aprendizado de máquina, WJARR](https://wjarr.com/sites/default/files/fulltext_pdf/WJARR-2026-0350.pdf)
- [Revisão sistemática sobre detecção e previsão de quebra de temperatura em cadeias de frutas e vegetais, Frontiers in AI](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1830032/full)
- [Evolução da tecnologia de prevenção de excursão térmica, PatSnap](https://www.patsnap.com/resources/blog/articles/cold-chain-temperature-excursion-tech-patents-2026/)
- [Taxa de pilotos de agentes de IA que não chegam a produção](https://ud.hk/en/blogs/insight/article/2026-05-12-ai-agent-pilot-failure?)
- [Falha de pilotos de agentes de IA em cadeia de suprimentos, project44](https://www.project44.com/blog/why-95-percent-of-ai-agent-pilots-fail-in-supply-chains/)
- [Projeção do Gartner sobre cancelamento de iniciativas de IA agêntica](https://debales.ai/blog/agentic-ai-pilots-fail-logistics-scoping)
- [Diferença entre playbook, SOP e runbook](https://www.moxo.com/blog/operations-playbooks-template-library)
- [Modelo operacional de governança de IA e matriz RACI](https://elevateconsult.com/insights/designing-the-ai-governance-operating-model-raci/)
- [Guia de desenho de target operating model, Umbrex](https://umbrex.com/resources/the-busy-consultants-guide-to-target-operating-model-design/)
