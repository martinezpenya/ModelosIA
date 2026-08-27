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


def apartados(fichas: list[dict], grupo: str) -> str:
    """Un apartado por notebook: titulo, resumen y —si es entrega— que se entrega.

    Decision del profesor (2026-08-27): «tabla con enlaces y a continuacion breve explicacion de
    cada notebook y con los materiales/enlaces extra que se necesiten». Se genera para que ninguna
    unidad se quede sin resumen y para que el orden sea siempre el numerico.
    """
    fuera = []
    for f in fichas:
        fuera.append(f"## `{f['codigo']}` · {f['titulo']}\n")
        fuera.append(f["resumen"])
        if f.get("materiales"):
            fuera.append("\n| Recurso | Enlace |\n|---|---|\n" + "\n".join(f["materiales"]))
        if grupo == "entregas" and f.get("se_entrega"):
            fuera.append(f"\n**Se entrega**: {f['se_entrega']}")
        elif f.get("se_entrega"):
            fuera.append(f"\n**Qué tienes que tener al terminar**: {f['se_entrega']}")
        fuera.append("")
    return "\n".join(fuera).strip()


def admonicion(grupo: str, n: int, ra: str | None, ud: str, extra: str | None,
               sin_rubrica: bool = False, hay_practica: bool = True) -> str:
    """La misma cabecera en las trece paginas, con lo que cambia entre unidades parametrizado."""
    prueba = f"la prueba escrita del {ra}" if ra else "el resto del módulo"
    if grupo == "practica":
        cuerpo = (f'!!! info "Práctica: se hace, no se entrega"\n'
                  f"    {n} notebook{'s' if n != 1 else ''} que se trabaja"
                  f"{'n' if n != 1 else ''} **en clase**, con el profesor. "
                  f"**No se entrega{'n' if n != 1 else ''} ni puntúa{'n' if n != 1 else ''}**: "
                  f"prepara{'n' if n != 1 else ''} las\n    [entregas de la unidad]({ud}_Entregas.md) y {prueba}.")
    else:
        titulo_adm = f"{n} entrega{'s' if n != 1 else ''}" + (f" en el {ra}" if ra else "")
        # La UD02 no tiene notebooks guiados, asi que no hay pagina de practica a la que enlazar.
        cola = (f" La [práctica de la unidad]({ud}_ActividadesGuiadas.md) no se entrega\n    ni puntúa."
                if hay_practica else
                f" Los [ejercicios de autoevaluación]({ud}_Ejercicios.md) son práctica\n    y no se entregan.")
        if sin_rubrica:
            medio = ("    Se entregan en Moodle y **no llevan rúbrica**: se marcan como hechas o no hechas."
                     + cola)
        else:
            medio = ("    Cada una se corrige con **su rúbrica**, que puedes leer antes de empezar en la propia\n"
                     "    tarea de Moodle. El **peso** de cada entrega está en el libro de calificaciones de\n"
                     "    Moodle, no aquí." + cola)
        cuerpo = f'!!! important "{titulo_adm}"\n{medio}' 
    if extra:
        cuerpo += "\n\n" + "\n".join(f"    {l}" if l.strip() else "" for l in extra.strip().split("\n"))
    return cuerpo


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


def etiquetas_descuadradas() -> list[tuple[str, str, str]]:
    """Enlaces cuya etiqueta cita un codigo distinto del notebook al que apuntan.

    Es el fallo que aparecio al renumerar: el destino se reapunta con un sed y la etiqueta se queda
    con el codigo viejo, asi que la pagina dice «N15» y abre el N09. No lo detecta el build, porque
    el enlace es valido.
    """
    patron = re.compile(r"\[([^\]\n]*?)\]\(([^)\s]*?(UD0\d)_(N\d+)_[^)\s]*?\.ipynb)\)")
    mal = []
    for f in DOCS.rglob("*.md"):
        if "Presentacion" in str(f):
            continue
        for m in patron.finditer(f.read_text(encoding="utf-8")):
            codigos = re.findall(r"\bN\d+\b", m.group(1))
            if codigos and m.group(4) not in codigos:
                mal.append((str(f.relative_to(RAIZ)), m.group(1)[:60], m.group(4)))
    return mal


def apartados_mal_colocados(datos: dict, entregas: set[str]) -> list[str]:
    """Apartados `## Nnn ...` que estan en la pagina del regimen equivocado.

    Al reclasificar, el apartado con el enunciado de una actividad se queda donde estaba aunque la
    actividad haya cambiado de regimen: la pagina de Entregas acaba describiendo notebooks que son
    practica. No lo detecta el build, porque la pagina es valida.
    """
    mal = []
    for ud, d in datos.items():
        for clave, grupo in (("_pagina_practica", "practica"), ("_pagina_entregas", "entregas")):
            pagina = d.get(clave)
            if not pagina:
                continue
            texto = (DOCS / ud / pagina).read_text(encoding="utf-8")
            for m in re.finditer(r"(?m)^## `?(N\d+)`?([^\n]*)$", texto):
                cod = m.group(1)
                es_entrega = any(n.startswith(f"{ud}_{cod}_") for n in entregas)
                deberia = "entregas" if es_entrega else "practica"
                if deberia != grupo:
                    mal.append(f"{ud}/{pagina}: «{cod}{m.group(2)[:40]}» es {deberia}, está en {grupo}")
    return mal


def lineas_absorbidas() -> list[str]:
    """Lineas pegadas a una fila de tabla, que Markdown se traga como si fueran otra fila.

    Paso dos veces al mover tablas con un script: un `## Titulo` o un `**Se entrega**` justo debajo
    de la ultima fila, sin linea en blanco, y la pagina lo pinta DENTRO de la tabla. El build no
    avisa, porque el markdown es valido. Los comentarios `<!-- ... -->` no cuentan: Markdown los
    descarta y el bloque AUTO los usa a proposito.
    """
    mal = []
    for f in sorted(DOCS.rglob("*.md")):
        if "Presentacion" in str(f):
            continue
        lineas = f.read_text(encoding="utf-8").split("\n")
        dentro = False
        for i in range(len(lineas) - 1):
            if lineas[i].strip().startswith("```"):
                dentro = not dentro
            if dentro:
                continue
            a, b = lineas[i].strip(), lineas[i + 1].strip()
            if a.startswith("|") and a.endswith("|") and b and not b.startswith(("|", "<!--")):
                mal.append(f"{f.relative_to(RAIZ)}:{i + 2} → «{b[:55]}»")
            if b == "---" and a and not a.startswith("<!--"):
                mal.append(f"{f.relative_to(RAIZ)}:{i + 2} → el separador «---» pegado a «{a[:40]}»")
    return mal


def entregas_sin_apartado(datos: dict, entregas: set[str]) -> list[str]:
    """Entregas que no tienen su resumen en la pagina.

    Decision del profesor (2026-08-27): cada entrega lleva en la pagina dos o tres lineas —que se
    pide y que se entrega— y el enunciado completo por fases vive en el notebook. Los notebooks que
    venian de talleres convertidos se quedaron sin ese resumen, y la pagina describia unas entregas
    y no otras.
    """
    faltan = []
    for ud, d in datos.items():
        pagina = d.get("_pagina_entregas")
        if not pagina:
            continue
        texto = (DOCS / ud / pagina).read_text(encoding="utf-8")
        tiene = {m.group(1) for m in re.finditer(r"(?m)^## `?(N\d+)`?", texto)}
        for nb in sorted(n for n in entregas if n.startswith(ud)):
            m = re.match(rf"{ud}_(N\d+)_", nb)
            if m and m.group(1) not in tiene:
                faltan.append(f"{ud}/{pagina}: falta el resumen de {m.group(1)}")
    return faltan


def recursos_redundantes() -> list[str]:
    """Filas de «Recurso | Enlace» que repiten lo que ya da la tabla generada.

    La tabla de arriba enlaza el notebook, su descarga y su Colab. Si un apartado vuelve a poner
    esas mismas filas, el alumno lee dos veces lo mismo. La tabla del apartado solo se justifica
    para el material de apoyo: imagenes, video, audio, CSV, pistas.
    """
    redundante = re.compile(r"^\|\s*(Notebook|Ejecutar en Colab|Colab|Abrir en Colab|Descargar)\s*\|", re.I)
    mal = []
    for f in sorted(DOCS.rglob("*.md")):
        if "Presentacion" in str(f):
            continue
        for m in re.finditer(r"\| Recurso \| Enlace \|\n\|---\|---\|\n((?:\|[^\n]*\|\n)+)",
                             f.read_text(encoding="utf-8")):
            for fila in m.group(1).strip().split("\n"):
                if redundante.match(fila.strip()):
                    mal.append(f"{f.relative_to(RAIZ)}: «{fila.split('|')[1].strip()}» ya está en la tabla generada")
    return mal


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
            if isinstance(que_es, dict) and not que_es.get("que_es"):
                que_es = None
            if que_es is None:
                sin_ficha.append(f"{ud}/{nb}")
                que_es = "—"
            ficha = dict(que_es) if isinstance(que_es, dict) else {"que_es": que_es}
            grupo = "entregas" if nb in entregas else "practica"
            fichas[grupo].append({"fichero": nb, "codigo": cod, "titulo": titulo(nb_path),
                                  "que_es": ficha.get("que_es", "—"),
                                  "resumen": ficha.get("resumen", ""),
                                  "se_entrega": ficha.get("se_entrega", ""),
                                  "materiales": ficha.get("materiales", [])})

        for grupo, pagina in (("practica", datos[ud].get("_pagina_practica")),
                              ("entregas", datos[ud].get("_pagina_entregas"))):
            if not pagina:
                continue
            p = DOCS / ud / pagina
            texto = p.read_text(encoding="utf-8")
            if INICIO not in texto:
                print(f"  {ud}/{pagina}: sin bloque AUTO:notebooks")
                continue
            i, j = texto.index(INICIO) + len(INICIO), texto.index(FIN)
            ra = datos[ud].get("_ra")
            extra = datos[ud].get(f"_nota_{grupo}")
            # Hay entregas que no son notebook —talleres, debates, Robocode— y cuentan en el total.
            n = len(fichas[grupo]) + (datos[ud].get("_entregas_extra", 0) if grupo == "entregas" else 0)
            nuevo = "\n" + admonicion(grupo, n, ra, ud, extra,
                                      datos[ud].get("_sin_rubrica", False),
                                      bool(datos[ud].get("_pagina_practica"))) + "\n"
            if fichas[grupo]:
                nuevo += ("\n" + tabla(fichas[grupo], ud)
                          + "\n\n" + apartados(fichas[grupo], grupo) + "\n")
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
    fuera = apartados_mal_colocados(datos, entregas)
    if fuera:
        print("\n  APARTADOS EN LA PÁGINA EQUIVOCADA:")
        for x in fuera:
            print(f"    {x}")

    faltan = entregas_sin_apartado(datos, entregas)
    if faltan:
        print("\n  ENTREGAS SIN RESUMEN EN LA PÁGINA:")
        for x in faltan:
            print(f"    {x}")

    repes = recursos_redundantes()
    if repes:
        print("\n  RECURSOS REPETIDOS · el apartado repite lo que da la tabla generada:")
        for x in repes:
            print(f"    {x}")

    absorbidas = lineas_absorbidas()
    if absorbidas:
        print("\n  LÍNEAS ABSORBIDAS POR UNA TABLA · falta la línea en blanco:")
        for x in absorbidas:
            print(f"    {x}")

    mal = etiquetas_descuadradas()
    if mal:
        print("\n  ETIQUETAS DESCUADRADAS · la etiqueta cita un código distinto del destino:")
        for ruta, etiqueta, cod in mal:
            print(f"    {ruta}: «{etiqueta}» apunta al {cod}")

    if check and (desfasados or mal or fuera or absorbidas or faltan or repes):
        if desfasados:
            print("\n  DESFASADAS: " + ", ".join(desfasados))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
