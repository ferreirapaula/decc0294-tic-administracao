"""Calcula e analisa a taxa de turnover (rotatividade) a partir de um CSV de movimentacoes.

Uso:
    python calcular_turnover.py movimentacoes.csv [--inicio 2025-01-01] [--fim 2025-12-31] [--quadro-inicio 100] [--quadro-fim 102]

Formato do CSV (colunas obrigatorias): tipo,data
Colunas opcionais: departamento,nivel,gestor,saida,tenure_dias
  tipo: admissao | desligamento
  data: AAAA-MM-DD
  saida: voluntario | involuntario  (apenas em desligamentos)
  tenure_dias: dias de casa na data da saida (apenas em desligamentos)
"""

import argparse
import csv
import sys
from collections import defaultdict
from datetime import datetime

BENCHMARKS_SETOR = {
    "tecnologia": (20, 30),
    "varejo": (25, 35),
    "servicos financeiros": (12, 18),
    "industria": (12, 18),
    "servicos": (12, 25),
    "setor publico": (5, 10),
}


def interpretar(taxa):
    if taxa < 12:
        return "baixo (bem)"
    if taxa <= 20:
        return "normal"
    if taxa <= 30:
        return "alto (problema)"
    return "muito alto (risco ao negocio)"


def ler_movimentos(caminho, inicio, fim):
    admissoes, desligamentos = [], []
    with open(caminho, newline="", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)
        if "tipo" not in leitor.fieldnames or "data" not in leitor.fieldnames:
            sys.exit("Erro: o CSV precisa das colunas 'tipo' e 'data'.")
        for linha in leitor:
            data = datetime.strptime(linha["data"].strip(), "%Y-%m-%d").date()
            if inicio and data < inicio:
                continue
            if fim and data > fim:
                continue
            tipo = linha["tipo"].strip().lower()
            if tipo == "admissao":
                admissoes.append(linha)
            elif tipo == "desligamento":
                desligamentos.append(linha)
            else:
                sys.exit(f"Erro: tipo desconhecido '{linha['tipo']}'. Use admissao ou desligamento.")
    return admissoes, desligamentos


def taxa(admissoes, desligamentos, quadro_inicio, quadro_fim):
    if quadro_inicio is None or quadro_fim is None:
        sys.exit("Erro: informe --quadro-inicio e --quadro-fim (colaboradores no inicio e no fim do periodo).")
    quadro_medio = (quadro_inicio + quadro_fim) / 2
    if quadro_medio == 0:
        return 0.0, quadro_medio
    valor = (len(admissoes) + len(desligamentos)) / 2 / quadro_medio * 100
    return valor, quadro_medio


def segmentar(desligamentos, chave):
    contagem = defaultdict(int)
    for item in desligamentos:
        contagem[item.get(chave, "").strip() or "nao informado"] += 1
    return dict(sorted(contagem.items(), key=lambda par: par[1], reverse=True))


def main():
    parser = argparse.ArgumentParser(description="Analise de turnover")
    parser.add_argument("csv", help="arquivo CSV de movimentacoes")
    parser.add_argument("--inicio", help="data inicial AAAA-MM-DD")
    parser.add_argument("--fim", help="data final AAAA-MM-DD")
    parser.add_argument("--quadro-inicio", type=int, help="colaboradores no inicio do periodo")
    parser.add_argument("--quadro-fim", type=int, help="colaboradores no fim do periodo")
    parser.add_argument("--setor", help="setor da empresa para comparar com o benchmark")
    args = parser.parse_args()

    inicio = datetime.strptime(args.inicio, "%Y-%m-%d").date() if args.inicio else None
    fim = datetime.strptime(args.fim, "%Y-%m-%d").date() if args.fim else None

    admissoes, desligamentos = ler_movimentos(args.csv, inicio, fim)
    valor, quadro_medio = taxa(admissoes, desligamentos, args.quadro_inicio, args.quadro_fim)

    voluntarios = sum(1 for d in desligamentos if d.get("saida", "").strip().lower() == "voluntario")
    involuntarios = sum(1 for d in desligamentos if d.get("saida", "").strip().lower() == "involuntario")
    new_hires = sum(
        1
        for d in desligamentos
        if d.get("tenure_dias", "").strip().isdigit() and int(d["tenure_dias"]) <= 365
    )

    print("=" * 60)
    print("ANALISE DE TURNOVER")
    print("=" * 60)
    print(f"Periodo: {args.inicio or 'indefinido'} a {args.fim or 'indefinido'}")
    print(f"Admissoes: {len(admissoes)} | Desligamentos: {len(desligamentos)}")
    print(f"Quadro medio: {quadro_medio:.1f}")
    print(f"Formula: [(A + D) / 2] / quadro medio x 100")
    print(f"TAXA DE TURNOVER: {valor:.2f}% -> {interpretar(valor)}")
    print()
    print(f"Desligamentos voluntarios: {voluntarios}")
    print(f"Desligamentos involuntarios: {involuntarios}")
    print(f"Saidas nos primeiros 12 meses: {new_hires}")
    if len(desligamentos) > 0:
        print(f"New hire turnover: {new_hires / len(desligamentos) * 100:.1f}% das saidas")
    print()

    for chave, rotulo in (("departamento", "Por departamento"), ("nivel", "Por nivel"), ("gestor", "Por gestor")):
        if any(item.get(chave, "").strip() for item in desligamentos):
            contagem = segmentar(desligamentos, chave)
            total = sum(contagem.values())
            print(rotulo)
            for nome, quantidade in contagem.items():
                print(f"  {nome}: {quantidade} ({quantidade / total * 100:.0f}% das saidas)")
            print()

    if args.setor:
        chave = args.setor.strip().lower()
        faixa = BENCHMARKS_SETOR.get(chave)
        if faixa:
            situacao = "dentro da faixa" if faixa[0] <= valor <= faixa[1] else "fora da faixa"
            print(f"Benchmark {args.setor}: {faixa[0]}-{faixa[1]}% -> sua taxa esta {situacao}")
        else:
            print(f"Setor '{args.setor}' sem benchmark cadastrado. Facaixas disponiveis: {', '.join(BENCHMARKS_SETOR)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
