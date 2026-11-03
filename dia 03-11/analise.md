# Evasão escolar no Brasil em 2025

**Leitura dos dados do Censo Escolar (Inep) — taxas de rendimento e abandono**
Disciplina DECC0294 · Tecnologia da Informação e Comunicação Aplicada à Administração · 2026.2
Data da análise: 3 de novembro de 2026

---

## 1. Pergunta e recorte

**Pergunta:** qual é a magnitude da evasão escolar no Brasil em 2025, onde ela se concentra e
como evoluiu nos últimos anos?

**Recorte:**

- Indicador: **taxa de abandono** do Censo Escolar da Educação Básica.
- Ano de referência: **2025**; série histórica de **2019 a 2025**.
- Geografia: Brasil, grandes regiões e 27 unidades da federação.
- Etapas: ensino fundamental (anos iniciais e finais) e ensino médio (total e por série).
- Redes: federal, estadual, municipal e privada; localização urbana e rural.

"Evasão" é usada aqui no sentido corrente do fenômeno — o estudante que deixa a escola.
O indicador oficial correspondente é a **taxa de abandono**, que mede a proporção de
matrículas que não termina o ano letivo nem por aprovação nem por reprovação. Os dois termos
não são sinônimos perfeitos: "abandono" é o indicador; "evasão" é o conceito mais amplo.

---

## 2. Fonte dos dados

**Fonte primária:** Inep — Indicadores Educacionais, *Taxas de Rendimento Escolar 2025*.
Planilha oficial `tx_rend_brasil_regioes_ufs_2025.xlsx`, publicada em 26/06/2026.

- Página: <https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar/2025>
- Arquivo: <https://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/2025/tx_rend_brasil_regioes_ufs_2025.zip>
- Matrícula no ensino médio (para a estimativa da seção 4): Censo Escolar 2025, apresentação
  dos resultados — <https://download.inep.gov.br/censo_escolar/resultados/2025/apresentacao_coletiva.pdf>

### Sobre o acesso pela API

A solicitação era usar a API do Inep. O que foi testado nesta rede:

| Endpoint | Resultado |
|---|---|
| `https://servicodados.inep.gov.br/api/` | DNS não resolve (NXDOMAIN, confirmado em DNS público) |
| `https://api.inep.gov.br/` | DNS resolve (200.130.24.209), mas a conexão é recusada (porta 80) ou resetada (porta 443) |

Como a interface de API não respondeu, a análise usou a **planilha oficial** do mesmo
indicador, publicada pelo Inep no portal de Dados Abertos. O dado é o mesmo que alimenta os
painéis do instituto; muda o meio de acesso, não o conteúdo. Todos os números deste
documento saem dessa planilha, sem ajuste manual.

---

## 3. Como o indicador é calculado

A taxa de abandono é o complemento das taxas de aprovação e reprovação:

```
taxa de abandono = 100% − taxa de aprovação − taxa de reprovação
```

Ela é calculada sobre a matrícula de cada etapa e rede, a partir da situação do aluno
registrada no Censo Escolar. Consequências para a leitura:

- é uma **proporção**, não um número absoluto de estudantes;
- **não mede aprendizagem** nem qualidade do ensino;
- **não identifica a causa** da saída (trabalho, gravidez, violência, reprovação repetida etc.);
- **não conta** quem nunca se matriculou (evasão antes do ingresso).

---

## 4. Resultado nacional em 2025

Brasil, todas as redes e localizações:

| Etapa | Taxa de abandono |
|---|---:|
| Ensino fundamental — total | **0,5%** |
| · anos iniciais | 0,2% |
| · anos finais | 0,9% |
| Ensino médio — total | **2,2%** |
| · 1ª série | 2,6% |
| · 2ª série | 2,2% |
| · 3ª série | 1,5% |
| · 4ª série | 2,0% |
| · não seriado | 6,1% |

Para contexto, no ensino médio a taxa de aprovação foi 94,8% e a de reprovação, 3,0%.
No ensino fundamental: 97,4% de aprovação e 2,1% de reprovação.

**Estimativa de estudantes:** com 7.364.013 matrículas presenciais no ensino médio em 2025,
uma taxa de 2,2% corresponde a aproximadamente **162 mil estudantes** que deixaram a etapa
ao longo do ano. É uma estimativa (matrícula × taxa), não uma contagem oficial de pessoas.

### Por dependência administrativa (ensino médio)

| Rede | Abandono |
|---|---:|
| Federal | 1,4% |
| Estadual | **2,6%** |
| Municipal | 1,7% |
| Privada | 0,3% |
| **Total** | **2,2%** |

A rede estadual, que concentra a maior parte da oferta, tem taxa **8,7 vezes** maior que a
privada. No ensino fundamental a diferença é menor: 0,8% na estadual e 0,1% na privada.

### Por localização (ensino médio)

| Localização | Abandono |
|---|---:|
| Urbana | 2,1% |
| Rural | **2,5%** |

No ensino fundamental a distância é maior: 0,5% na urbana e 0,8% na rural.

### Por grande região (ensino médio)

| Região | Abandono |
|---|---:|
| Centro-Oeste | 1,1% |
| Nordeste | 1,9% |
| Norte | 2,2% |
| Sudeste | **2,7%** |
| Sul | 1,9% |

---

## 5. Onde a evasão se concentra

Dez maiores taxas de abandono no ensino médio, 2025:

| # | UF | Taxa |
|---:|---|---:|
| 1 | Amapá | 4,4% |
| 2 | Acre | 4,3% |
| 3 | Rondônia | 4,0% |
| 4 | Roraima | 4,0% |
| 5 | Amazonas | 3,9% |
| 6 | Paraíba | 3,4% |
| 7 | Santa Catarina | 3,3% |
| 8 | Rio de Janeiro | 3,1% |
| 9 | Maranhão | 3,0% |
| 10 | Distrito Federal | 3,0% |

- As **cinco maiores** taxas estão todas na região Norte.
- **15 das 27 UFs** ficaram acima da média nacional (2,2%).
- A dispersão é grande: de **0,1% no Mato Grosso** a **4,4% no Amapá** — 44 vezes.
- O **Maranhão** aparece em 9º lugar, com 3,0%, acima da média nacional.

---

## 6. Série histórica (Brasil, todas as redes)

| Ano | Ensino fundamental | Ensino médio | 1ª série do EM |
|---|---:|---:|---:|
| 2019 | 1,2% | 4,8% | 6,1% |
| 2020 | 1,0% | 2,3% | 2,7% |
| 2021 | 1,2% | 5,0% | 4,2% |
| 2022 | 1,1% | 5,7% | 5,5% |
| 2023 | 0,7% | 3,4% | 3,6% |
| 2024 | 0,6% | 3,2% | 3,7% |
| 2025 | **0,5%** | **2,2%** | **2,6%** |

Variações:

- ensino médio: **−31,3%** de 2024 para 2025 e **−61,4%** de 2022 para 2025;
- ensino fundamental: **−58,3%** de 2019 para 2025;
- 1ª série do ensino médio: **−29,7%** de 2024 para 2025.

2025 é o **menor valor da série 2019–2025** nas três colunas. O ano de 2020 é atípico:
as taxas de aprovação subiram com as políticas emergenciais da pandemia, o que derruba
artificialmente o abandono naquele ano. Por isso, a comparação mais informativa é com
2022–2024, não com 2020.

---

## 7. Três leituras que os dados sustentam

1. **A saída se concentra no início do ensino médio.** A 1ª série tem 2,6%, contra 1,5% na
   3ª série. É na transição para o ensino médio que a escola perde mais gente.
2. **A rede pública estadual é o ponto crítico.** 2,6% contra 0,3% da privada. Como a
   estadual responde pela maior parte das matrículas, pequenas variações nela mudam o
   resultado nacional.
3. **O problema não é só regional, mas tem endereço.** As cinco maiores taxas estão no
   Norte, mas o Sudeste tem a maior média regional (2,7%), puxada por Rio de Janeiro (3,1%)
   e São Paulo (2,8%). Média regional esconde outliers nos dois sentidos.

---

## 8. Limitações

- **Taxa, não contagem.** Os 162 mil estudantes são estimativa; o Inep não publica, nesta
  planilha, o número absoluto de abandonos por etapa.
- **Indicador declarado.** A situação do aluno é informada pelas escolas e consolidada pelo
  Inep; os valores estão sujeitos a revisão do instituto.
- **Sem causalidade.** Os dados mostram magnitude e distribuição, não explicam por que o
  estudante saiu. Afirmar causas exigiria outra base (Pnad Contínua, estudos qualitativos,
  cruzamento com renda e trabalho).
- **Sem corte por raça, renda ou sexo.** A planilha de taxas de rendimento não traz esses
  recortes; eles existem em outros produtos do Censo, com outra metodologia.
- **2020 não é comparável.** O ano pandêmico distorce a série; a leitura de tendência deve
  começar em 2022.
- **Evasão ≠ abandono.** O indicador capta a saída durante o ano letivo; quem conclui e não
  volta no ano seguinte, ou quem nunca ingressa, não aparece aqui.

---

## 9. Reprodutibilidade

Arquivos gerados nesta análise:

| Arquivo | Conteúdo |
|---|---|
| `dados/inep-2025/taxas_rendimento_tidy.csv` | base tratada, 4.105 linhas, 2019–2025 |
| `dados/analise_dados.py` | leitura das planilhas e geração da base tratada |
| `dados/indicadores.py` | cálculo dos indicadores usados no texto |
| `dados/gerar_svg.py` | geração dos gráficos do deck |
| `dados/conferir.py` | conferência dos números citados no texto |
| `evasao-escolar-2025.html` | deck final, autossuficiente (13 slides) |
| `evasao-escolar-2025.pdf` | versão impressa do deck, 13 páginas |
| `deck-fonte.html` | fonte editável do deck |
| `dados/inep-2025/x_tx_rend_*/` | planilhas XLSX originais de 2019 a 2025 |

Para refazer a base:

```bash
python dados/analise_dados.py
python dados/indicadores.py
python dados/gerar_svg.py
```

Para regerar o deck:

```bash
python .opencode/skills/ufma-visual/scripts/empacotar.py \
  deck-fonte.html \
  -o evasao-escolar-2025.html
```

---

## 10. Referências

- INEP. **Taxas de Rendimento Escolar 2025**. Indicadores Educacionais, 2026.
  <https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/taxas-de-rendimento-escolar/2025>
- INEP. **Censo Escolar da Educação Básica 2025 — Resumo Técnico**. 2026.
  <https://download.inep.gov.br/publicacoes/institucionais/estatisticas_e_indicadores/resumo_tecnico_censo_da_educacao_basica_2025.pdf>
- INEP. **Censo Escolar 2025 — Apresentação dos resultados**. 2026.
  <https://download.inep.gov.br/censo_escolar/resultados/2025/apresentacao_coletiva.pdf>
