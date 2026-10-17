# Boutique de IA · Preparação para o projeto de Cold Chain

Material de preparação para a conversa com a boutique de consultoria com foco em
IA, considerando o projeto de Cold Chain que está encerrando a etapa de diagnóstico
e seguindo para desenho de playbook da área e implementação conjunta.

## Arquivos

| Arquivo | O que é |
|---|---|
| `prompt-guia-boutique-ia.md` | Prompt reutilizável que gera e complementa o guia. Contém papel, objetivo, contexto, instruções de execução, restrições de forma e critério de qualidade |
| `guia-boutique-ia-cold-chain.md` | Guia executado, em doze partes. Decodificação da fala do interlocutor, one-pager de escopo, fundamentos de cadeia do frio, casos de uso de IA por camada, anatomia do playbook, árvore de KPIs com business case, plano de 30/60/90, perguntas para fazer e para responder, glossário, armadilhas e checklist final |
| `guia-boutique-ia-cold-chain.pdf` | Versão agregada para leitura e impressão, com capa, sumário paginado, o guia completo e os dois anexos |
| `gerar_pdf.py` | Gerador do PDF. Converte o markdown em flowables do reportlab, monta capa, sumário em duas passadas, cabeçalho e rodapé |

## Ordem de leitura sugerida

1. Partes 1 e 2 do guia, que definem escopo e fase do projeto.
2. Partes 3 a 6, que são a sustentação técnica da conversa.
3. Partes 8 e 9 na véspera, que são as que aparecem na conversa de verdade.
4. Parte 12 nas 48 horas finais.

## Gerar o PDF

```
python3 gerar_pdf.py
```

Precisa de reportlab e fonttools. No sandbox foi usado um venv separado porque o
site-packages do sistema é somente leitura.

```
python3 -m venv .venv-pdf && .venv-pdf/bin/pip install reportlab fonttools
.venv-pdf/bin/python gerar_pdf.py
```

As fontes variáveis Noto Sans e JetBrains Mono são congeladas em pesos estáticos
dentro de `.fonts/` durante o build, porque o reportlab não lê eixo variável. Essa
pasta é cache e não entra no repositório.

## Regerar ou aprofundar

Rode novamente o conteúdo de `prompt-guia-boutique-ia.md`, acrescentando no bloco
de contexto qualquer informação nova que surgir, por exemplo o vertical do cliente
final, a cobertura atual de telemetria ou o entregável exato da etapa que está sendo
encerrada. Quanto mais específico o vertical, mais preciso fica o bloco de regulação.
