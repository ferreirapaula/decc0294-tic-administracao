import csv
import pathlib

LINHAS = list(csv.DictReader(open("dados/inep-2025/taxas_rendimento_tidy.csv", encoding="utf-8"), delimiter=";"))


def num(v):
    return None if v in (None, "", "None") else float(v)


def fmt(v):
    return f"{v:.1f}".replace(".", ",")


def seleciona(ano, unidade="Brasil", localizacao="Total", dependencia="Total"):
    for r in LINHAS:
        if (int(r["ano"]) == ano and r["unidade"] == unidade
                and r["localizacao"] == localizacao and r["dependencia"] == dependencia):
            return r
    raise SystemExit(f"nao encontrado: {ano} {unidade} {localizacao} {dependencia}")


# ---------------------------------------------------------------- serie 2019-2025
serie = [(ano, num(seleciona(ano)["em"])) for ano in range(2019, 2026)]

W, H = 1168, 372
esq, dir_, topo, base = 74, 1124, 26, 300

svg = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Taxa de abandono no ensino médio, Brasil, 2019 a 2025" '
       'style="width:100%;height:auto;display:block">']
svg.append('<rect x="0" y="0" width="1168" height="372" fill="#FFFFFF"/>')

# grade horizontal e rotulos do eixo y
for v in (0, 2, 4, 6):
    y = base - (v / 6) * (base - topo)
    svg.append(f'<line x1="{esq}" y1="{y:.1f}" x2="{dir_}" y2="{y:.1f}" stroke="#E3E3E3" stroke-width="1"/>')
    svg.append(f'<text x="{esq - 14}" y="{y + 5:.1f}" text-anchor="end" font-family="Segoe UI,Arial,sans-serif" '
               f'font-size="15" fill="#6B6B6B">{v}%</text>')

passo = (dir_ - esq) / (len(serie) - 1)
pontos = []
for i, (ano, valor) in enumerate(serie):
    x = esq + i * passo
    y = base - (valor / 6) * (base - topo)
    pontos.append((x, y, ano, valor))

# pontos e linha (sem area: a paleta nao preve cor de preenchimento para grafico)
d_linha = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y, _, _ in pontos)
svg.append(f'<path d="{d_linha}" fill="none" stroke="#8D0333" stroke-width="3"/>')

for x, y, ano, valor in pontos:
    destaque = ano == 2025
    svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{7 if destaque else 5}" fill="{"#D4B277" if destaque else "#8D0333"}" '
               f'stroke="#FFFFFF" stroke-width="2"/>')
    svg.append(f'<text x="{x:.1f}" y="{y - 16:.1f}" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" '
               f'font-size="{19 if destaque else 16}" font-weight="{700 if destaque else 400}" '
               f'fill="{"#8D0333" if destaque else "#333333"}">{fmt(valor)}%</text>')
    svg.append(f'<text x="{x:.1f}" y="{base + 30}" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" '
               f'font-size="16" fill="#6B6B6B">{ano}</text>')

# anotacao do ano atipico
x2020, y2020 = pontos[1][0], pontos[1][1]
svg.append(f'<text x="{x2020 + 10:.1f}" y="{y2020 + 34:.1f}" font-family="Segoe UI,Arial,sans-serif" font-size="14" '
           f'fill="#6B6B6B">2020: ano atípico</text>')

svg.append('</svg>')
pathlib.Path("dados/svg-serie.svg").write_text("\n".join(svg), encoding="utf-8")

# ---------------------------------------------------------------- ranking das UFs
REGIOES = {"Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"}
ufs = [r for r in LINHAS
       if int(r["ano"]) == 2025 and r["localizacao"] == "Total" and r["dependencia"] == "Total"
       and r["unidade"] not in REGIOES and r["unidade"] != "Brasil" and num(r["em"]) is not None]
ufs.sort(key=lambda r: num(r["em"]), reverse=True)
top = [(r["unidade"], num(r["em"])) for r in ufs[:10]]

W, H = 1168, 380
x0, x1 = 232, 1046
maxv = 4.6
svgl = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Dez maiores taxas de abandono no ensino médio por unidade da federação, 2025" '
        'style="width:100%;height:auto;display:block">']
svgl.append('<rect x="0" y="0" width="1168" height="380" fill="#FFFFFF"/>')
for v in (0, 1, 2, 3, 4):
    x = x0 + (v / maxv) * (x1 - x0)
    svgl.append(f'<line x1="{x:.1f}" y1="10" x2="{x:.1f}" y2="344" stroke="#E3E3E3" stroke-width="1"/>')
    svgl.append(f'<text x="{x:.1f}" y="366" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" '
                f'font-size="15" fill="#6B6B6B">{v}%</text>')

alt = 33
for i, (nome, valor) in enumerate(top):
    y = 18 + i * alt
    largura = (valor / maxv) * (x1 - x0)
    cor = "#D4B277" if nome == "Maranhão" else "#8D0333"
    svgl.append(f'<text x="{x0 - 14}" y="{y + 15}" text-anchor="end" font-family="Segoe UI,Arial,sans-serif" '
                f'font-size="16" fill="#333333">{nome}</text>')
    svgl.append(f'<rect x="{x0}" y="{y}" width="{largura:.1f}" height="21" fill="{cor}"/>')
    svgl.append(f'<text x="{x0 + largura + 10:.1f}" y="{y + 16}" font-family="Segoe UI,Arial,sans-serif" '
                f'font-size="16" font-weight="700" fill="#8D0333">{fmt(valor)}%</text>')
svgl.append('</svg>')
pathlib.Path("dados/svg-ranking.svg").write_text("\n".join(svgl), encoding="utf-8")

print("ok: dados/svg-serie.svg e dados/svg-ranking.svg")
print("serie:", serie)
print("top10:", top)
