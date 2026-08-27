#!/usr/bin/env python3
"""Genera las tablas de notebooks de las paginas de Practica y Entregas de cada unidad.

    python3 scripts/generar_tablas_notebooks.py            # escribe
    python3 scripts/generar_tablas_notebooks.py --check    # solo avisa si estan desfasadas

Rellena los bloques  <!-- AUTO:notebooks inicio --> ... <!-- AUTO:notebooks fin -->  con una tabla
de cuatro columnas: el notebook renderizado, que es, la descarga del .ipynb y el badge de Colab.

Por que existe: estas tablas se escribieron a mano tres veces y se desalinearon las tres (codigos
viejos, notebooks sin badge, filas que apuntaban a un fichero renombrado). Los datos salen de:

  - El TITULO H1 del propio notebook, que es la fuente de su nombre y su numero.
  - `datos/notebooks.yml`, que solo guarda la columna «que es» y el regimen, porque eso no se puede
    deducir del fichero.
  - El `nav` de mkdocs.yml, que es quien decide si un notebook es entrega o practica.
"""
import json
import re
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
DOCS = RAIZ / "docs"
GH = "https://github.com/martinezpenya/ModelosIA/blob/main/docs"
RAW = "https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs"
COLAB = "https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs"
INICIO, FIN = "<!-- AUTO:notebooks inicio -->", "<!-- AUTO:notebooks fin -->"


def titulo(nb_path: Path) -> str:
    """Parte descriptiva del H1 del notebook: lo que va tras el guion largo."""
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    for c in nb.get("cells", []):
        if c.get("cell_type") != "markdown":
            continue
        for linea in "".join(c.get("source", [])).split("\n"):
            if linea.startswith("# "):
                return linea.split("—")[-1].strip() if "—" in linea else linea[2:].strip()
    return nb_path.stem


def entregas_del_nav() -> set[str]:
    """Ficheros de notebook que el nav coloca bajo «Entregas». El nav es la autoridad."""
    texto = (RAIZ / "mkdocs.yml").read_text(encoding="utf-8")
    lineas_todas = texto[texto.index("\nnav:") + 1:].split("\n")
    lineas_nav = [lineas_todas[0]]
    for l in lineas_todas[1:]:
        if l and not l.startswith(" "):
            break
        lineas_nav.append(l)
    entregas, dentro = set(), False
    for linea in lineas_nav:
        if re.match(r"^    - (Entregas|Documentación)", linea):
            dentro = linea.strip().startswith("- Entregas")
            continue
        if re.match(r"^    - \w", linea):
            dentro = False
        m = re.search(r"(UD0\d/notebooks/\S+\.ipynb)", linea)
        if m and dentro:
            entregas.add(m.group(1).split("/")[-1])
    return entregas


def tabla(fichas: list[dict], ud: str) -> str:
    filas = ["| Notebook | Qué es | Descargar | Abrir en Colab |", "|---|---|---|---|"]
    for f in fichas:
        nb, cod = f["fichero"], f["codigo"]
        filas.append(
            f"| [`{cod}` · {f['titulo']}](notebooks/{nb}) | {f['que_es']} | "
            f"[![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)]"
            f"({RAW}/{ud}/notebooks/{nb}){{:target=\"_blank\"}} | "
            f"[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]"
            f"({COLAB}/{ud}/notebooks/{nb}){{:target=\"_blank\"}} |")
    return "\n".join(filas)


def main() -> int:
    check = "--check" in sys.argv
    datos = yaml.safe_load((RAIZ / "datos" / "notebooks.yml").read_text(encoding="utf-8"))
    entregas = entregas_del_nav()
    desfasados, sin_ficha = [], []

    for ud in sorted(datos):
        fichas = {"practica": [], "entregas": []}
        for nb_path in sorted((DOCS / ud / "notebooks").glob(f"{ud}_N*.ipynb")):
            nb = nb_path.name
            cod = re.match(rf"{ud}_(N\d+)_", nb).group(1)
            que_es = datos[ud].get(nb)
            if que_es is None:
                sin_ficha.append(f"{ud}/{nb}")
                que_es = "—"
            grupo = "entregas" if nb in entregas else "practica"
            fichas[grupo].append({"fichero": nb, "codigo": cod,
                                  "titulo": titulo(nb_path), "que_es": que_es})

        for grupo, pagina in (("practica", datos[ud].get("_pagina_practica")),
                              ("entregas", datos[ud].get("_pagina_entregas"))):
            if not pagina or not fichas[grupo]:
                continue
            p = DOCS / ud / pagina
            texto = p.read_text(encoding="utf-8")
            if INICIO not in texto:
                print(f"  {ud}/{pagina}: sin bloque AUTO:notebooks")
                continue
            i, j = texto.index(INICIO) + len(INICIO), texto.index(FIN)
            nuevo = f"\n{tabla(fichas[grupo], ud)}\n"
            if texto[i:j] == nuevo:
                print(f"  al día: {ud}/{pagina} [{grupo}]")
                continue
            desfasados.append(f"{ud}/{pagina} [{grupo}]")
            if not check:
                p.write_text(texto[:i] + nuevo + texto[j:], encoding="utf-8")
                print(f"  actualizado: {ud}/{pagina} [{grupo}] · {len(fichas[grupo])} notebooks")

    if sin_ficha:
        print("\n  AVISO · notebooks sin descripción en datos/notebooks.yml:")
        for s in sin_ficha:
            print(f"    {s}")
    if check and desfasados:
        print("\n  DESFASADAS: " + ", ".join(desfasados))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
