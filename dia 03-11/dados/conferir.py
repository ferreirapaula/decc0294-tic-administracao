import csv
rows = list(csv.DictReader(open("dados/inep-2025/taxas_rendimento_tidy.csv", encoding="utf-8"), delimiter=";"))
def sel(ano, un, loc="Total", dep="Total"):
    for r in rows:
        if int(r["ano"])==ano and r["unidade"]==un and r["localizacao"]==loc and r["dependencia"]==dep:
            return r
for uf in ["Sao Paulo","São Paulo","Rio de Janeiro","Mato Grosso","Maranhao","Maranhão","Amapa","Amapá"]:
    r = sel(2025, uf)
    if r: print(uf, "EM=", r["em"], "EF=", r["ef"])
regs = ["Norte","Nordeste","Sudeste","Sul","Centro-Oeste"]
print("regioes:", [(x, sel(2025,x)["em"]) for x in regs])
ufs = [r for r in rows if int(r["ano"])==2025 and r["localizacao"]=="Total" and r["dependencia"]=="Total" and r["unidade"] not in regs+["Brasil"] and r["em"] not in ("","None")]
vals = sorted((float(r["em"]), r["unidade"]) for r in ufs)
print("n UFs:", len(vals))
print("acima de 2.2:", sum(1 for v,_ in vals if v>2.2))
print("min:", vals[0], "max:", vals[-1])
