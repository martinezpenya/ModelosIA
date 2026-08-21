#!/usr/bin/env bash
# Sirve el sitio en local para revisarlo, sin generar el PDF.
# El plugin with-pdf necesita weasyprint (y librerías del sistema: pango, cairo), que no hacen
# falta para revisar contenido. Este script genera una copia de mkdocs.yml sin ese plugin.
set -euo pipefail
cd "$(dirname "$0")"
VENV=~/virtual-envs/modelosia
[ -d "$VENV" ] || python3 -m venv "$VENV"
grep -v -iE 'weasyprint|pydyf|with-pdf' requirements.txt > /tmp/req-local.txt
"$VENV/bin/pip" install -q -r /tmp/req-local.txt

python3 - <<'PY'
import re
from pathlib import Path
out, saltando = [], False
for l in Path("mkdocs.yml").read_text(encoding="utf-8").splitlines():
    if re.match(r"^\s{4}- with-pdf:", l):
        saltando = True; continue
    if saltando:
        if re.match(r"^\s{4}- \w", l) or re.match(r"^\S", l):
            saltando = False
        else:
            continue
    out.append(l)
Path("mkdocs.local.yml").write_text("\n".join(out) + "\n", encoding="utf-8")
PY

echo "Sirviendo en http://127.0.0.1:8000  (Ctrl+C para parar)"
exec "$VENV/bin/mkdocs" serve -f mkdocs.local.yml -a 127.0.0.1:8000
