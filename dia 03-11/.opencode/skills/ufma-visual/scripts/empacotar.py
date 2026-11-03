#!/usr/bin/env python3
"""Empacota um deck do padrao UFMA em um unico arquivo HTML.

Uso:
    python empacotar.py deck.html
    python empacotar.py deck.html -o saidas/deck-final.html

O script troca o <link> de ufma.css por um <style> embutido e o src de
brasao.png por um data URI. Assim o arquivo abre sem a pasta de assets.
"""

import argparse
import base64
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r'<link\b[^>]*href=["\']([^"\']*ufma\.css)["\'][^>]*>', re.I)
IMG_RE = re.compile(r'(<img\b[^>]*src=["\'])([^"\']*brasao\.png)(["\'])', re.I)


def localizar(base: Path, rel: str) -> Path:
    """Aceita caminho relativo ao HTML ou o nome do arquivo dentro de assets/."""
    nome = Path(rel.replace("\\", "/")).name
    candidatos = [
        base / rel,
        base / nome,
        base / "assets" / nome,
        base.parent / "assets" / nome,
    ]
    for caminho in candidatos:
        if caminho.is_file():
            return caminho
    tentados = "\n".join(f"  - {c}" for c in candidatos)
    raise FileNotFoundError(f"Arquivo nao encontrado: {rel}\nTentativas:\n{tentados}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Embute ufma.css e brasao.png em um deck HTML."
    )
    parser.add_argument("html", help="arquivo HTML de entrada")
    parser.add_argument(
        "-o", "--saida", help="arquivo de saida (padrao: <nome>-final.html)"
    )
    args = parser.parse_args()

    origem = Path(args.html).resolve()
    if not origem.is_file():
        print(f"Erro: nao encontrei {origem}", file=sys.stderr)
        return 1

    base = origem.parent
    texto = origem.read_text(encoding="utf-8")
    embutidos = []

    def troca_css(match: re.Match) -> str:
        caminho = localizar(base, match.group(1))
        css = caminho.read_text(encoding="utf-8").replace("</style>", "<\\/style>")
        embutidos.append(caminho.name)
        return "<style>\n" + css + "\n</style>"

    def troca_img(match: re.Match) -> str:
        caminho = localizar(base, match.group(2))
        dados = base64.b64encode(caminho.read_bytes()).decode("ascii")
        embutidos.append(caminho.name)
        return f"{match.group(1)}data:image/png;base64,{dados}{match.group(3)}"

    texto, total_css = LINK_RE.subn(troca_css, texto)
    texto, total_img = IMG_RE.subn(troca_img, texto)

    if total_css == 0 and total_img == 0:
        print(
            "Erro: nenhum <link> de ufma.css nem <img> de brasao.png encontrado. "
            "O HTML ja esta empacotado ou usa outro caminho.",
            file=sys.stderr,
        )
        return 1

    destino = (
        Path(args.saida).resolve()
        if args.saida
        else origem.with_name(origem.stem + "-final.html")
    )
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(texto, encoding="utf-8")

    if LINK_RE.search(texto) or IMG_RE.search(texto):
        print("Aviso: ainda ha referencia a arquivo externo no HTML.", file=sys.stderr)

    print(f"OK: {destino}")
    print(
        f"CSS: {total_css} | brasao: {total_img} | "
        f"{destino.stat().st_size / 1024:.0f} KB"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
