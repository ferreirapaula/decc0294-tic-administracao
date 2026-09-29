"""Simulação de dados de RH - Empresa fictícia (200 funcionários)."""
import random
from datetime import date, timedelta
import pandas as pd

random.seed(42)

N = 200

nomes_masc = ["Miguel","Arthur","Gael","Theo","Heloísa","Davi","Bernardo","Gabriel","Pedro","Lucas","Matheus","Rafael","Bruno","Thiago","Felipe","João","Paulo","Carlos","André","Marcos","Vinícius","Eduardo","Gustavo","Fernando","Rodrigo","Diego","Caio","Renan","Igor","Otávio"]
sobrenomes = ["Silva","Santos","Oliveira","Souza","Costa","Pereira","Almeida","Carvalho","Ferreira","Ribeiro","Martins","Rocha","Barbosa","Cardoso","Teixeira","Moreira","Correia","Dias","Nunes","Mendes","Vieira","Freitas","Barros","Moura","Pinto","Cavalcanti","Azevedo","Lima","Araújo","Fernandes"]
nomes_fem = ["Alice","Laura","Manuela","Valentina","Sophia","Isabella","Helena","Cecília","Lorena","Maria","Ana","Julia","Beatriz","Mariana","Camila","Fernanda","Patrícia","Aline","Vanessa","Priscila","Tatiane","Renata","Daniela","Paula","Bruna","Larissa","Gabriela","Letícia","Clara"," Marina".strip()]

departamentos_cargos = {
    "Vendas": [("Vendedor Júnior", 2500, 3500), ("Vendedor Pleno", 3500, 5500), ("Gerente de Vendas", 8000, 12000)],
    "TI": [("Analista de Suporte", 3500, 5000), ("Desenvolvedor Júnior", 4000, 6000), ("Desenvolvedor Pleno", 7000, 10000), ("Desenvolvedor Sênior", 11000, 16000), ("Gerente de TI", 13000, 18000)],
    "RH": [("Assistente de RH", 2800, 4000), ("Analista de RH", 4500, 6500), ("Gerente de RH", 9000, 13000)],
    "Financeiro": [("Assistente Financeiro", 3000, 4200), ("Analista Financeiro", 5000, 7500), ("Gerente Financeiro", 10000, 14000)],
    "Marketing": [("Assistente de Marketing", 2800, 4000), ("Analista de Marketing", 4500, 7000), ("Gerente de Marketing", 9000, 13000)],
    "Operações": [("Auxiliar Operacional", 2000, 3000), ("Analista de Operações", 4000, 6000), ("Supervisor de Operações", 6500, 9000), ("Gerente de Operações", 9500, 13500)],
    "Atendimento": [("Atendente", 1800, 2800), ("Analista de Atendimento", 3200, 4500), ("Supervisor de Atendimento", 5500, 7500)],
}

escolaridades = ["Ensino Médio", "Ensino Médio", "Graduação", "Graduação", "Graduação", "Pós-graduação", "Pós-graduação", "Mestrado"]
estados_civis = ["Solteiro(a)", "Casado(a)", "Casado(a)", "Solteiro(a)", "Divorciado(a)", "União Estável"]
deps = list(departamentos_cargos.keys())
pesos_dep = [0.22, 0.18, 0.08, 0.12, 0.10, 0.18, 0.12]  # Vendas e TI maiores

hoje = date(2026, 9, 29)
dados = []
for i in range(1, N + 1):
    sexo = random.choices(["F", "M"], weights=[0.48, 0.52])[0]
    primeiro = random.choice(nomes_fem if sexo == "F" else nomes_masc)
    nome = f"{primeiro} {random.choice(sobrenomes)} {random.choice(sobrenomes)}"
    idade = max(18, min(65, int(random.gauss(35, 9))))
    estado_civil = random.choice(estados_civis)
    escolaridade = random.choice(escolaridades)

    dep = random.choices(deps, weights=pesos_dep)[0]
    # cargos mais júnior são mais frequentes
    cargos = departamentos_cargos[dep]
    idx = random.choices(range(len(cargos)), weights=list(range(len(cargos), 0, -1)))[0]
    cargo, sal_min, sal_max = cargos[idx]
    salario = round(random.uniform(sal_min, sal_max) / 10) * 10

    # admissão: até 10 anos atrás
    dias_empresa = random.randint(30, 3650)
    admissao = hoje - timedelta(days=dias_empresa)
    tempo_anos = round(dias_empresa / 365, 1)

    avaliacao = random.choices([1, 2, 3, 4, 5], weights=[0.05, 0.12, 0.33, 0.35, 0.15])[0]
    # correlação: avaliação baixa + pouco tempo + salário baixo => maior chance de desligado
    risco = 0.12 + (0.15 if avaliacao <= 2 else 0) + (0.08 if tempo_anos < 1.5 else 0)
    status = "Desligado(a)" if random.random() < risco else "Ativo(a)"

    absenteismo = max(0, int(random.gauss(4 if avaliacao >= 4 else 8, 4)))
    promocao = "Sim" if (avaliacao >= 4 and tempo_anos >= 1.5 and random.random() < 0.35) else "Não"
    horas_trein = max(0, int(random.gauss(30 if dep == "TI" else 20, 12)))
    satisfacao = random.choices([1, 2, 3, 4, 5], weights=[0.06, 0.12, 0.27, 0.35, 0.20])[0]
    engajamento = random.choice(["Baixo", "Médio", "Alto"]) if satisfacao <= 3 else random.choice(["Médio", "Alto", "Alto"])

    # ajuste: desligados tendem a ter satisfação menor
    if status.startswith("Deslig"):
        satisfacao = max(1, satisfacao - random.choice([0, 1, 1]))

    dados.append({
        "ID": f"FUNC{i:04d}",
        "Nome": nome,
        "Sexo": "Feminino" if sexo == "F" else "Masculino",
        "Idade": idade,
        "Estado Civil": estado_civil,
        "Escolaridade": escolaridade,
        "Departamento": dep,
        "Cargo": cargo,
        "Salário (R$)": salario,
        "Data Admissão": admissao.strftime("%d/%m/%Y"),
        "Tempo Empresa (anos)": tempo_anos,
        "Status": status,
        "Avaliação Desempenho (1-5)": avaliacao,
        "Dias Ausência (ano)": absenteismo,
        "Promoção último ano": promocao,
        "Horas Treinamento (ano)": horas_trein,
        "Satisfação (1-5)": satisfacao,
        "Engajamento": engajamento,
    })

df = pd.DataFrame(dados)
df.to_csv("rh_funcionarios.csv", index=False, encoding="utf-8-sig", sep=";")

# Excel com 2 abas: base + resumo
with pd.ExcelWriter("rh_funcionarios.xlsx", engine="openpyxl") as w:
    df.to_excel(w, sheet_name="Funcionários", index=False)
    resumo = pd.DataFrame({
        "Métrica": [
            "Total funcionários", "Ativos", "Desligados", "Taxa Turnover",
            "Salário médio (R$)", "Idade média", "Avaliação média",
            "Satisfação média", "Média dias ausência", "% Promovidos",
            "Média horas treinamento",
        ],
        "Valor": [
            len(df),
            (df["Status"] == "Ativo(a)").sum(),
            (df["Status"] == "Desligado(a)").sum(),
            f"{(df['Status'] == 'Desligado(a)').mean()*100:.1f}%",
            f"R$ {df['Salário (R$)'].mean():,.2f}",
            round(df["Idade"].mean(), 1),
            round(df["Avaliação Desempenho (1-5)"].mean(), 2),
            round(df["Satisfação (1-5)"].mean(), 2),
            round(df["Dias Ausência (ano)"].mean(), 1),
            f"{(df['Promoção último ano'] == 'Sim').mean()*100:.1f}%",
            round(df["Horas Treinamento (ano)"].mean(), 1),
        ],
    })
    resumo.to_excel(w, sheet_name="Resumo", index=False)
    # ajuste largura colunas
    for ws in w.sheets.values():
        for col in ws.columns:
            ws.column_dimensions[col[0].column_letter].width = 22

print(f"OK: {len(df)} funcionários | turnover {(df['Status']=='Desligado(a)').mean()*100:.1f}% | salário médio R$ {df['Salário (R$)'].mean():,.2f}")
