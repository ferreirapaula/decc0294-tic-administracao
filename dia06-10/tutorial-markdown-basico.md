# Tutorial Básico de Markdown

Guia exemplificativo para estudantes de Administração — DECC0294 / TIC na Administração.
Arquivo de prática do dia 06-10.

## 1. O que é Markdown?

Markdown é uma linguagem de marcação simples para formatar texto. É usada em README, documentação, GitHub, relatórios e anotações.

Você escreve texto puro e ele é convertido para HTML, PDF, etc.

## 2. Títulos e subtítulos

Use `#` no início da linha:

```markdown
# Título nível 1
## Título nível 2
### Título nível 3
```

Resultado:

# Título nível 1
## Título nível 2
### Título nível 3

> Use um único `#` por documento para o título principal.

## 3. Parágrafos e quebras de linha

Escreva normalmente. Para novo parágrafo, deixe uma linha em branco.

Exemplo:

```markdown
Primeiro parágrafo sobre planejamento estratégico.

Segundo parágrafo sobre controle financeiro.
```

## 4. Ênfase: negrito, itálico e riscado

```markdown
**negrito**
*itálico*
~~riscado~~
***negrito e itálico***
```

Resultado:

**negrito**
*itálico*
~~riscado~~
***negrito e itálico***

Exemplo aplicado à Administração:

A **margem de lucro** do trimestre foi de *12,5%*.

## 5. Listas

### 5.1 Lista não ordenada

```markdown
- Planejamento
- Organização
- Direção
- Controle
```

Resultado:

- Planejamento
- Organização
- Direção
- Controle

### 5.2 Lista ordenada

```markdown
1. Definir objetivo
2. Levantar dados
3. Analisar alternativas
4. Decidir
```

Resultado:

1. Definir objetivo
2. Levantar dados
3. Analisar alternativas
4. Decidir

### 5.3 Lista de tarefas (checkbox)

```markdown
- [x] Levantar custos
- [ ] Elaborar orçamento
- [ ] Apresentar à diretoria
```

Resultado:

- [x] Levantar custos
- [ ] Elaborar orçamento
- [ ] Apresentar à diretoria

## 6. Citações

Use `>`:

```markdown
> "Administrar é interpretar os objetivos propostos e transformá-los em ação." — Chiavenato
```

Resultado:

> "Administrar é interpretar os objetivos propostos e transformá-los em ação." — Chiavenato

## 7. Links

```markdown
[Portal do IBGE](https://www.ibge.gov.br)
```

Resultado:

[Portal do IBGE](https://www.ibge.gov.br)

## 8. Imagens

Sintaxe parecida com link, com `!` na frente:

```markdown
![Fluxo de caixa - exemplo](https://via.placeholder.com/400x150)
```

## 9. Código

### 9.1 Código inline

Use crases: `` ` ``

```markdown
O arquivo `orcamento_2026.xlsx` está na pasta `dados/`.
```

Resultado: O arquivo `orcamento_2026.xlsx` está na pasta `dados/`.

### 9.2 Bloco de código

Use três crases com a linguagem:

```python
receita = 150000
custo = 95000
lucro = receita - custo
print(f"Lucro: R$ {lucro}")
```

## 10. Tabelas

```markdown
| Indicador | 2024 | 2025 | Variação |
|-----------|------|------|----------|
| Receita   | 120k | 150k | +25%     |
| Custo     | 80k  | 95k  | +18,7%   |
| Lucro     | 40k  | 55k  | +37,5%   |
```

Resultado:

| Indicador | 2024 | 2025 | Variação |
|-----------|------|------|----------|
| Receita   | 120k | 150k | +25%     |
| Custo     | 80k  | 95k  | +18,7%   |
| Lucro     | 40k  | 55k  | +37,5%   |

> Alinhe com `:` — `|:---|` esquerda, `|:---:|` centro, `|---:|` direita.

## 11. Linha horizontal

Três traços `---`, asteriscos `***` ou underlines `___`:

---

## 12. Exercício rápido

Tente criar abaixo um mini-relatório usando o que aprendeu:

1. Um título com o nome da empresa fictícia
2. Um parágrafo com **negrito** e *itálico*
3. Uma lista com 3 metas
4. Uma tabela com 2 indicadores
5. Uma citação

---

*Arquivo criado para prática em 06-10 — edite à vontade para testar.*
