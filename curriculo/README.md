# Currículo — Matteo Lucato

Auditoria e revisão do currículo, com o documento reconstruído preservando a
formatação original.

## Arquivos

| Arquivo | O que é |
|---|---|
| `CV - Matteo Lucato (original).pdf` | Documento de partida, como enviado |
| `CV - Matteo Lucato (revisado).pdf` | **Versão final**, pronta para uso |
| `preview-cv-revisado.png` | Prévia em imagem, para conferir sem abrir o PDF |
| `curriculo-revisado.md` | Texto do revisado + perguntas abertas |
| `build-cv-revisado.py` | Gera o PDF revisado (`python3 build-cv-revisado.py`) |
| `prompt-analise-curriculo.md` | Prompt de auditoria usado, reutilizável |

## O que mudou

**Correções de data e coerência**
- Formatura na UNICAMP: `Julho 2027` → `Dezembro 2027`.
- Nunes&Lucato: início `Fevereiro 2022` → `Fevereiro 2023`, eliminando a
  incoerência de o cargo começar antes do ingresso na graduação.
- V4 Company e Clube de Consultoria: término estendido para `Setembro 2026`.
- UNICAMP e Clube de Consultoria estavam localizados em "São Paulo"; o Instituto de
  Economia fica em **Campinas**. Padronizado para `Cidade, SP`.

**Excesso de quantificação**
O documento original tinha número ou percentual em **100% dos bullet points**, o que
sugere fabricação em vez de orientação a resultado. Ao classificar cada métrica,
apareceu um padrão: *todos* os nove percentuais eram indefensáveis sob pergunta em
entrevista (sem base de comparação, ou medindo algo sem unidade natural, como
"rastreabilidade em 40%" e "engajamento sustentável em 15%"), enquanto *todas* as
quantidades absolutas eram sólidas.

Resultado: **9 percentuais → 0**. Preservadas as oito métricas verificáveis
(R$ 5M de orçamento, 400 transações/mês, R$ 150 mil, 2.500 itens, 40 toneladas/mês,
1,2 milhão de registros, 100 alunos, 626 respostas).

**Atribuição de crédito**
`relatórios que embasaram a alocação de +R$ 5M/ano` passou a
`relatórios gerenciais que a diretoria utilizava como base para decidir a alocação de
um orçamento anual superior a R$ 5M`. O valor continua no documento como escopo real
do trabalho, sem atribuir ao analista júnior uma decisão que era da diretoria.

**Paralelismo**
Um bullet abria com substantivo (`Condução de análise SWOT`) entre onze em primeira
pessoa do passado. Os doze agora seguem o mesmo padrão.

**Redação e espaço**
- Sem travessão (`—`) no texto corrido, que denuncia redação automatizada. O `–` das
  faixas de data permanece, por ser a convenção correta para intervalos.
- Removidos endereço residencial completo, "Ensino Fundamental" e a lista de
  disciplinas do ensino médio; telefone formatado.
- Linguagem vazia cortada: "visando melhores práticas de mercado", "impacto
  sustentável positivo", "dezenas de".
- CPA-20 e CFA saíram de "disciplinas acadêmicas" para Certificações; "Semifinalista
  do Challenge Ágora" saiu de Certificações para Competições.
- Ordem cronológica das atividades extracurriculares corrigida.

**Tipografia preservada**
Fonte do corpo 10.1pt e leading ~12.8pt, iguais ao original. O texto cresceu de
4.141 para 4.646 caracteres e ocupa a página inteira, com 20pt de margem inferior.
O original terminava a 0.5pt da borda, com risco de corte na impressão.

## Pendências

O `curriculo-revisado.md` lista as perguntas abertas. As duas de maior impacto:

1. **Setembro 2026 é término ou os vínculos seguem em curso?** Se V4 e Clube
   continuam, o correto é `Presente`, que lê muito melhor que uma data de saída no
   mês corrente.
2. **Inglês possivelmente subvendido:** declarado "avançado", mas o próprio currículo
   registra ensino médio com currículo internacional norte-americano e disciplinas AP.

As demais destravam métricas removidas: cada base de comparação fornecida
(ex.: "inadimplência caiu de 8% para 6% da carteira") devolve o número ao documento,
agora defensável.
