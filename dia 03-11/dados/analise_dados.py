import csv
import glob
import pathlib
import re

import openpyxl

# mapeamento dos dois layouts publicados pelo Inep
COLS_NOVO = {
    "ef": "3_CAT_FUN",
    "ef_ai": "3_CAT_FUN_AI",
    "ef_af": "3_CAT_FUN_AF",
    "em": "3_CAT_MED",
    "em_1": "3_CAT_MED_01",
    "em_2": "3_CAT_MED_02",
    "em_3": "3_CAT_MED_03",
    "aprov_ef": "1_CAT_FUN",
    "aprov_em": "1_CAT_MED",
    "reprov_ef": "2_CAT_FUN",
    "reprov_em": "2_CAT_MED",
}
COLS_VELHO = {
    "ef": "tab_FUN",
    "ef_ai": "tab_F14",
    "ef_af": "tab_F04",
    "em": "tab_MED",
    "em_1": "tab_M01",
    "em_2": "tab_M02",
    "em_3": "tab_M03",
    "aprov_ef": "tap_FUN",
    "aprov_em": "tap_MED",
    "reprov_ef": "tre_FUN",
    "reprov_em": "tre_MED",
}


def numero(v):
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v).strip().replace(",", ".")
    if s in ("", "--", "-", "..."):
        return None
    try:
        return float(s)
    except ValueError:
        return None


def ler_arquivo(caminho):
    ano = int(re.search(r"_(20\d\d)\.xlsx$", caminho).group(1))
    wb = openpyxl.load_workbook(caminho, data_only=True)
    ws = wb[wb.sheetnames[0]]
    rows = list(ws.iter_rows(values_only=True))
    idx = None
    for i, row in enumerate(rows):
        if not row:
            continue
        primeiro = str(row[0]).strip()
        # 2019/2020 usam "ano" (minusculo) na linha de codigos; 2021+ usam NU_ANO_CENSO
        if primeiro in ("NU_ANO_CENSO", "ano"):
            idx = i
            break
    if idx is None:
        raise SystemExit("linha de codigos nao encontrada: " + caminho)
    codigos = [str(c).strip() if c is not None else "" for c in rows[idx]]
    mapa = COLS_NOVO if "3_CAT_FUN" in codigos else COLS_VELHO
    col = {c: i for i, c in enumerate(codigos) if c}
    nome_unidade = "UNIDGEO" if "UNIDGEO" in col else None

    registros = []
    for row in rows[idx + 1:]:
        if not row or numero(row[0]) is None:
            continue
        unidade = str(row[1]).strip() if nome_unidade is not None else str(row[1]).strip()
        localizacao = str(row[col.get("NO_CATEGORIA", 2)]).strip() if "NO_CATEGORIA" in col else str(row[2]).strip()
        dependencia = str(row[col.get("NO_DEPENDENCIA", 3)]).strip() if "NO_DEPENDENCIA" in col else str(row[3]).strip()
        reg = {
            "ano": int(numero(row[0])),
            "unidade": unidade,
            "localizacao": localizacao,
            "dependencia": dependencia,
        }
        for chave, codigo in mapa.items():
            reg[chave] = numero(row[col[codigo]]) if codigo in col and col[codigo] < len(row) else None
        registros.append(reg)
    return registros


registros = []
for arq in sorted(glob.glob("dados/inep-2025/x_tx_rend_*/**/*.xlsx", recursive=True)):
    regs = ler_arquivo(arq)
    print(arq.split("\\")[-1], "->", len(regs), "linhas, anos:", sorted({r["ano"] for r in regs}))
    registros.extend(regs)

saida = pathlib.Path("dados/inep-2025/taxas_rendimento_tidy.csv")
campos = ["ano", "unidade", "localizacao", "dependencia", "ef", "ef_ai", "ef_af", "em", "em_1", "em_2", "em_3",
          "aprov_ef", "aprov_em", "reprov_ef", "reprov_em"]
with saida.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=campos, delimiter=";")
    w.writeheader()
    for r in registros:
        w.writerow({k: r.get(k) for k in campos})
print("total:", len(registros), "->", saida)

print("\nBrasil, Total/Total:")
for r in sorted([r for r in registros if r["unidade"] == "Brasil" and r["localizacao"] == "Total" and r["dependencia"] == "Total"], key=lambda x: x["ano"]):
    print(f"  {r['ano']}  EF abandono={r['ef']}  EM abandono={r['em']}  EM 1a serie={r['em_1']}")
