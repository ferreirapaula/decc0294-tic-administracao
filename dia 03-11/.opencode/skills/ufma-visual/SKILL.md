---
name: ufma-visual
description: Use quando o usuário pedir para criar, revisar ou padronizar material com o padrão visual da UFMA — slides, capa, relatório, painel, certificado ou página HTML — ou mencionar "identidade visual da UFMA", "padrão UFMA", "cores da UFMA", "slide da disciplina", "material do módulo" ou "capa institucional". Aplica paleta, tipografia, grid 16:9, componentes e checklist de validação.
---

# Identidade visual UFMA

Skill para produzir material didático e institucional com o padrão visual da UFMA:
paleta vinho e dourado, tipografia Segoe UI, slides 16:9 de 1280 × 720 e um conjunto
fixo de componentes (capa, divisor, cartões, passos, entrega, encerramento).

Os tokens foram extraídos dos módulos da disciplina DECC0294 deste repositório.
Se o manual oficial da UFMA divergir, altere apenas o bloco `:root` de
`assets/ufma.css` — ele é a fonte única das cores e medidas.

## Quando usar

- Criar ou revisar slides de aula, capa de módulo, relatório, painel ou certificado da UFMA.
- Padronizar um HTML que já existe para o visual institucional.
- O usuário citar "padrão UFMA", "identidade da UFMA", "cores da UFMA" ou "material do módulo".

Não usar quando a instituição for outra ou quando o usuário pedir explicitamente
outra identidade visual. Nesse caso, perguntar antes de aplicar a paleta da UFMA.

## Regras de marca (não negociáveis)

- **Vinho é dominante.** `#8D0333` em capa, divisor, barra superior, títulos e paginação.
- **Dourado é filete.** `#D4B277` em traços, realces e numeração — nunca como fundo de texto pequeno.
- **Teal e amarelo são funcionais.** `#0AB0AB` e `#FEC84D` codificam categorias (entrega, alerta); não são decoração.
- **Sem efeitos.** Nada de gradiente, sombra colorida, brilho, emoji ou ícone decorativo.
- **Brasão intocado.** Nunca recolorir, esticar, cortar ou aplicar filtro.
- **Uma ideia por slide.** Se o conteúdo não couber, dividir em dois slides em vez de reduzir a fonte.

## Tokens

| Token | Hex | Uso |
|---|---|---|
| `--vinho` | `#8D0333` | fundo institucional, títulos, barra, paginação |
| `--dourado` | `#D4B277` | filetes, traço da capa, numeração de ciclo |
| `--teal` | `#0AB0AB` | categoria "entrega", cabeçalho de checklist |
| `--amarelo` | `#FEC84D` | destaque pontual, terceira categoria |
| `--card` | `#F5F5F5` | fundo de cartões e listas |
| `--card2` | `#FAF7F8` | caixas de instrução e critérios |
| `--txt` | `#1A1A1A` | títulos internos e texto sobre dourado |
| `--body` | `#333333` | corpo de texto |
| `--muted` | `#6B6B6B` | apoio, legendas, rodapé |
| `--linha` | `#E3E3E3` | bordas de cartão |
| `--branco` | `#FFFFFF` | fundo do slide |

Contraste: texto branco só sobre vinho. Sobre dourado, teal e amarelo, usar `#1A1A1A`.
Nunca usar branco sobre teal ou amarelo em texto pequeno.

## Tipografia

Família: `"Segoe UI", Calibri, "Helvetica Neue", Arial, sans-serif`.
Apenas dois pesos: 400 e 700. Caixa alta só em `eyebrow`, `rot` e `rot2`, com
`letter-spacing` de 1 a 1,6 px.

| Elemento | Tamanho | Peso | Cor |
|---|---|---|---|
| Título da capa | 54 px / 1.14 | 700 | branco |
| Título de conteúdo (`h2`) | 40 px / 1.12 | 700 | vinho |
| Título de divisor | 44 px / 1.15 | 700 | branco |
| Subtítulo (`sub`) | 19 px | 400 | muted |
| Corpo, cartão e passo | 17–20 px / 1.35–1.45 | 400 | body |
| Rótulo (`eyebrow`, `rot`) | 14–15 px | 700 | vinho ou muted |
| Rodapé | 14 px | 400 | muted |

Máximo de 60 caracteres por linha no corpo e 6 marcadores por slide.

## Grade e medidas

- Slide: **1280 × 720 px** (16:9), fundo branco.
- Margem de conteúdo: **56 px** nas laterais. Capa, divisor e encerramento: **90 px**.
- Barra superior: 28 px de vinho.
- Rodapé de conteúdo: 66 px no total — 3 px de vinho + 13 px de dourado + texto.
- Área útil do corpo: de `top:180px` até `bottom:96px` (444 px de altura).
- Brasão: 132 × 132 px, no canto superior direito da capa (`top:56px; right:82px`).
- Nada pode invadir o rodapé. Se invadir, o slide tem conteúdo demais.

## Componentes

Todos os componentes já existem em `assets/ufma.css`. Reutilizar as classes; não
criar CSS novo sem necessidade.

| Classe | Uso | Limite |
|---|---|---|
| `.capa` | abertura do módulo | 1 por deck |
| `.divisor` | abertura de ciclo/seção | 1 por ciclo |
| `.conteudo` | slide padrão com barra e rodapé | — |
| `.cards.cols-2/3/4` | comparação de conceitos | até 3 colunas |
| `.steps` | sequência numerada | 3–4 passos |
| `.prompt` | instrução a ser executada | 1 por slide |
| `.bullets` | lista sem ordem | até 6 itens |
| `.overview` | mapa do módulo | 2–4 ciclos |
| `.entrega` | checklist + onde + critério | 3–5 itens |
| `.fim` | encerramento | 1 por deck |

Campos da capa: `mod` (módulo), `h1` (título, até 2 linhas), `tracinho`, `sub`
(encontro e tema) e `pe` (curso, disciplina e semestre).

Cada slide de conteúdo leva rodapé com três partes: instituição e curso à esquerda,
título curto ao centro e paginação à direita (`n / total`).

## Brasão

- Arquivo: `assets/brasao.png` (260 × 260 px, fundo transparente).
- Somente na capa, sobre o vinho, a 132 × 132 px e com `alt="Brasão da UFMA"`.
- Não usar em slides de conteúdo, sobre foto ou como marca d'água.
- Se existir o SVG oficial, preferir o SVG e manter as mesmas medidas.

## Como produzir

1. Ler o conteúdo de origem (roteiro, módulo, plano de aula) e listar as ideias.
2. Distribuir **uma ideia por slide**; calcular o total antes de escrever o HTML.
3. Copiar `assets/modelo-slides.html` para o destino e renomear para kebab-case.
4. Substituir textos mantendo as classes; não alterar o CSS do modelo.
5. Conferir se cada slide cabe na área útil, sem estourar o rodapé.
6. Empacotar em arquivo único (CSS e brasão embutidos):

   ```bash
   python .opencode/skills/ufma-visual/scripts/empacotar.py caminho/deck.html -o saidas/deck.html
   ```

7. Abrir no navegador em 1280 × 720, navegar com as setas e gerar o PDF com `Ctrl+P`.
8. Salvar a entrega em `saidas/` e informar o caminho no final.

## Checklist de validação

- [ ] Só as cores da paleta; nenhuma cor inventada.
- [ ] Capa com brasão, módulo, título, subtítulo e identificação do curso.
- [ ] Barra vinho e rodapé completo em todos os slides de conteúdo.
- [ ] Paginação correta e crescente, incluindo divisor.
- [ ] Títulos com no máximo 2 linhas; corpo com no máximo 6 marcadores.
- [ ] Nenhum texto encostando ou invadindo o rodapé.
- [ ] Contraste adequado (branco só sobre vinho).
- [ ] Arquivo final autossuficiente: abre sem pasta de assets.
- [ ] `lang="pt-BR"`, `alt` no brasão e navegação por teclado funcionando.
- [ ] PDF gerado e conferido página a página.

## Acessibilidade e impressão

- Não usar cor como único sinal: acompanhar com rótulo ou texto.
- Tamanho mínimo de 14 px na tela e 16 px no material impresso.
- Manter foco visível nos botões de navegação.
- O bloco `@media print` já define `@page` de 1280 × 720 e força todos os slides a aparecerem.
- Ordem de leitura: da esquerda para a direita, de cima para baixo.

## Arquivos da skill

- `assets/ufma.css` — tokens, grade, componentes, navegação e impressão.
- `assets/modelo-slides.html` — deck de exemplo com 7 slides, do capa ao encerramento.
- `assets/brasao.png` — brasão da UFMA extraído dos módulos do repositório.
- `scripts/empacotar.py` — embute CSS e brasão no HTML final.

## Ao entregar

1. Informar o caminho do arquivo e o número de slides.
2. Dizer quais componentes foram usados e o que ficou como texto de exemplo.
3. Declarar o que foi validado (checklist e PDF).
4. Não inventar dado, número ou referência para preencher um slide.
