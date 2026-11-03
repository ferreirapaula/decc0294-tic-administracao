import csv
from collections import defaultdict

REGIOES = {"Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"}
linhas = list(csv.DictReader(open("dados/inep-2025/taxas_rendimento_tidy.csv", encoding="utf-8"), delimiter=";"))


def f(v):
    if v in (None, "", "None"):
        return None
    return float(v)


for r in linhas:
    for k in ("ef", "ef_ai", "ef_af", "em", "em_1", "em_2", "em_3", "aprov_ef", "aprov_em", "reprov_ef", "reprov_em"):
        r[k] = f(r[k])
    r["ano"] = int(r["ano"])


def seleciona(ano, unidade="Brasil", localizacao="Total", dependencia="Total"):
    for r in linhas:
        if r["ano"] == ano and r["unidade"] == unidade and r["localizacao"] == localizacao and r["dependencia"] == dependencia:
            return r
    return None


print("=== BRASIL 2025 - Total / Total")
b = seleciona(2025)
for k in ("ef", "ef_ai", "ef_af", "em", "em_1", "em_2", "em_3", "aprov_ef", "aprov_em", "reprov_ef", "reprov_em"):
    print(f"  {k}: {b[k]}")

print("\n=== BRASIL 2025 - abandono por dependencia (localizacao Total)")
for dep in ("Federal", "Estadual", "Municipal", "Privada", "Total"):
    r = seleciona(2025, dependencia=dep)
    if r:
        print(f"  {dep:10s} EF={r['ef']}  EM={r['em']}  EM_1={r['em_1']}")

print("\n=== BRASIL 2025 - abandono por localizacao")
for loc in ("Urbana", "Rural", "Total"):
    r = seleciona(2025, localizacao=loc)
    print(f"  {loc:8s} EF={r['ef']}  EM={r['em']}")

print("\n=== SERIE HISTORICA BRASIL (Total/Total)")
for ano in range(2019, 2026):
    r = seleciona(ano)
    print(f"  {ano}  EF={r['ef']}  EF_AF={r['ef_af']}  EM={r['em']}  EM_1={r['em_1']}  aprov_EM={r['aprov_em']}  reprov_EM={r['reprov_em']}")

print("\n=== REGIOES 2025 (EM abandono)")
for reg in sorted(REGIOES):
    r = seleciona(2025, unidade=reg)
    if r:
        print(f"  {reg:12s} EF={r['ef']}  EM={r['em']}")

print("\n=== UFs 2025: ranking por abandono no EM")
ufs = [r for r in linhas if r["ano"] == 2025 and r["localizacao"] == "Total" and r["dependencia"] == "Total"
       and r["unidade"] not in REGIOES and r["unidade"] != "Brasil" and r["em"] is not None]
ufs.sort(key=lambda r: r["em"], reverse=True)
for i, r in enumerate(ufs, 1):
    print(f"  {i:2d}. {r['unidade']:22s} EM={r['em']:.1f}  EF={r['ef']}")
print("  total UFs:", len(ufs))
acima = [r for r in ufs if r["em"] > b["em"]]
print("  UFs acima da media nacional:", len(acima))

print("\n=== MARANHAO - serie historica")
for ano in range(2019, 2026):
    r = seleciona(ano, unidade="Maranhao") or seleciona(ano, unidade="Maranhão")
    if r:
        print(f"  {ano}  EF={r['ef']}  EM={r['em']}  EM_1={r['em_1']}")

print("\n=== estimativa de alunos (matricula EM presencial 2025 = 7.364.013)")
mat = 7364013
for taxa in (b["em"], b["em_1"]):
    print(f"  taxa {taxa}% -> {mat * taxa / 100:,.0f} alunos")
