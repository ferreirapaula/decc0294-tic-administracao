---
name: turnover-analysis
description: Use quando o usuário pedir para analisar, calcular ou interpretar turnover/rotatividade de colaboradores, montar relatório ou dashboard de turnover, ou citar "análise de turnover", "taxa de rotatividade", "exit interview" ou "índice de turnover". Aplica o passo a passo completo com fórmulas, benchmarks do Brasil e plano de ação.
---

# Análise de Turnover

Skill para conduzir uma análise de turnover (rotatividade de pessoal) do início ao fim: coleta de dados, cálculo, segmentação, interpretação, investigação de causas, custo e plano de ação.

## Quando usar

- Usuário pede para calcular ou analisar turnover/rotatividade.
- Usuário quer um relatório, planilha ou dashboard de turnover.
- Usuário pergunta como interpretar o índice ou comparar com o mercado.

## Passo a passo obrigatório

### 1. Definir período e coletar dados
- Ideal: período de 12 meses (evita distorção por sazonalidade).
- Dados necessários:
  - Admissões (A) no período
  - Desligamentos (D) no período
  - Colaboradores no início e no fim do período
  - Motivo de cada saída: voluntário (pediu demissão) ou involuntário (empresa demitiu)
  - Departamento, cargo, nível (júnior/sênior), gestor e tempo de casa de cada saída

### 2. Calcular a taxa
Duas fórmulas aceitas no Brasil:

- **Fórmula da média:** `Taxa = [(A + D) / 2] / N × 100`
- **Fórmula clássica:** `Taxa = D / Quadro médio × 100`, onde `Quadro médio = (início + fim) / 2`

Sempre informar qual fórmula foi usada e aplicar a mesma em todas as comparações.

Exemplo: 100 funcionários, 10 admissões e 2 demissões → (10+2)/2 = 6 → 6/100 = 6%.

### 3. Segmentar os dados
Nunca entregar só o número agregado. Separar por:
- Voluntário × involuntário
- Departamento/setor
- Nível (júnior × pleno × sênior)
- Gestor
- Tempo de casa (*tenure*)
- **New hire turnover:** saídas nos primeiros 12 meses → sinal de problema em seleção ou onboarding (benchmark: até 30% aceitável)

### 4. Interpretar com benchmarks (Brasil)
- Abaixo de 12% = baixo
- 12–20% = normal
- Acima de 20% = alto
- Acima de 30% = muito alto (risco ao negócio)

Por setor: Tecnologia 20–30% | Varejo 25–35% | Serviços financeiros 12–18% | Setor público 5–10%.
Por porte: pequenas 20–28% | médias 15–22% | grandes 12–18%.

Nunca anualizar multiplicando por 2 um cálculo de 6 meses — refaça o cálculo em 12 meses.

### 5. Investigar as causas
- **Exit interviews** (entrevistas de desligamento): perguntas abertas, conduzidas por pessoa neutra (não pelo gestor direto).
- Cruzar padrões dos dados com as respostas (ex.: 80% citam falta de crescimento → problema é desenvolvimento).
- Pesquisas de engajamento/*pulse survey* para detectar risco antes da saída.

Principais causas globais: (1) remuneração, (2) falta de desenvolvimento/carreira, (3) gestão/liderança ruim, (4) cultura, (5) carga de trabalho.

### 6. Estimar o custo
- Custo direto por saída (recrutamento + onboarding): 1–2 salários mensais do cargo.
- Custo total por saída: 50–200% do salário anual, conforme o nível.
- Custo indireto: perda de produtividade, perda de conhecimento, impacto no clima.

### 7. Interpretação estratégica
- Turnover alto de baixo desempenho pode ser bom; turnover de talentos-chave é ruim.
- Turnover muito baixo também pode ser sinal de estagnação.
- Sinais de problema (3+ ocorrências = agir): não saber o índice exato, tendência de alta ano a ano, saída desproporcional de sêniors, vagas críticas abertas há meses, ausência de exit interviews.

### 8. Plano de ação
- **Semana 1:** calcular turnover de 12 meses, separar voluntário/involuntário.
- **Semanas 2–3:** 5–10 exit interviews.
- **Semana 4:** identificar o padrão principal de saída.
- **Semanas 5–8:** implementar 1–2 ações (mentoria, revisão de salários vs. mercado, melhoria de onboarding, treinamento de liderança).
- **Mês 6:** reavaliar o índice e ajustar.

## Script pronto (executar antes de calcular na mão)

A skill inclui `calcular_turnover.py`, que faz os passos 1 a 6 automaticamente:

```bash
python .opencode/skills/turnover-analysis/calcular_turnover.py movimentacoes.csv \
  --inicio 2025-01-01 --fim 2025-12-31 \
  --quadro-inicio 100 --quadro-fim 99 \
  --setor tecnologia
```

- Entrada: CSV com colunas `tipo` (`admissao`|`desligamento`), `data` (AAAA-MM-DD) e opcionais `departamento`, `nivel`, `gestor`, `saida` (`voluntario`|`involuntario`), `tenure_dias`.
- Modelo de entrada: `exemplo_movimentacoes.csv` (mesma pasta da skill).
- Saída: taxa total, classificação, voluntário/involuntário, new hire turnover, segmentações por departamento/nível/gestor e comparação com benchmark do setor.
- Se não houver CSV, pedir os dados ao usuário ou montar o CSV com ele antes de calcular.

## Referências (usar como fonte no trabalho)

- Edusense — Como calcular turnover: https://www.edusense.com.br/blog/como-calcular-turnover/
- oHub Base RH — Turnover: como calcular, interpretar e agir: https://base.ohub.com.br/rh/conteudos/digital-e-analytics/people-analytics/turnover-como-calcular-interpretar-e-agir
- Convenia — Como calcular Turnover: https://blog.convenia.com.br/como-calcular-turnover/
- Buk — Fórmula de turnover: https://www.buk.com.br/blog/entenda-como-calcular-o-turnover
- Código do Turnover — Cálculo e erros comuns: https://codigodoturnover.com/conteudos/como-calcular-turnover
- PlanilhaRH — Planilha de turnover: https://www.planilharh.com/planilha/de-turnover-e-rotatividade/

## Ao entregar o resultado

1. Mostrar a fórmula usada e os números (A, D, quadro médio).
2. Apresentar a taxa total + segmentações.
3. Comparar com o benchmark do setor.
4. Listar as causas prováveis e o custo estimado.
5. Propor o plano de ação com prazos.
6. Citar as fontes com link.
