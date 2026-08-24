import hashlib
import io
import os
import posixpath
import re
import subprocess
import tempfile
from pathlib import Path

from PIL import Image

PRERENDER = os.environ.get('PRERENDER_MERMAID', '0') == '1'
PUPPETEER_CONFIG = Path(__file__).parent / 'puppeteer-config.json'

_cache = {}

_current_page = ''
_site_dir = ''


def _mermaid_asset_dir() -> Path:
    d = Path(_site_dir) / 'assets' / 'mermaid'
    d.mkdir(parents=True, exist_ok=True)
    return d


def _relative_asset_path(page_url: str, filename: str) -> str:
    """Path to the shared mermaid asset dir, relative to the current page."""
    page_dir = posixpath.dirname(page_url)
    target = posixpath.join('assets', 'mermaid', filename)
    if not page_dir:
        return target
    return posixpath.relpath(target, start=page_dir)


def _mmdc_render(code: str, mmd_path: str, png_path: str) -> bool:
    args = [
        'mmdc', '-i', mmd_path, '-o', png_path,
        '-b', 'transparent', '-s', '1',
    ]
    if PUPPETEER_CONFIG.exists():
        args.extend(['-p', str(PUPPETEER_CONFIG)])
    result = subprocess.run(args, capture_output=True, text=True, timeout=30)
    return result.returncode == 0


_PNG_MAGIC = b'\x89PNG\r\n\x1a\n'
_PNG_MAX_DIMENSION = 2000  # px; una imagen mas alta o ancha que esto rompe la paginacion en el PDF


def _valid_png(data: bytes) -> bool:
    """Descarta PNG corruptos, vacios o desproporcionados antes de insertarlos en el HTML.

    Anadido el 2026-08-24 como defensa general: "returncode == 0" de mmdc no garantiza "imagen
    valida", asi que si el PNG esta corrupto, vacio o tiene un tamano fuera de lo razonable para
    un diagrama, se descarta aqui y el diagrama cae al texto plano de respaldo (siempre seguro).

    OJO: esto NO es el arreglo del corte de docs/Libro.pdf en produccion (sigue sin explicar,
    ver HISTORIAL.md 2026-08-24). Esta funcion solo protegeria contra un PNG de mmdc realmente
    corrupto o desproporcionado; los PNG que genera mmdc en la CI son validos, asi que este
    filtro no rechaza nada en la practica y no cambia el resultado del PDF truncado.
    """
    if len(data) < 100 or not data.startswith(_PNG_MAGIC):
        return False
    if len(data) < 33:
        return False
    width = int.from_bytes(data[16:20], 'big')
    height = int.from_bytes(data[20:24], 'big')
    if width <= 0 or height <= 0:
        return False
    if width > _PNG_MAX_DIMENSION or height > _PNG_MAX_DIMENSION:
        return False
    return True


_TALL_HEIGHT_LIMIT = 900  # px; por encima de esto, un diagrama mermaid vertical rompe el PDF


def _shrink_if_tall(data: bytes) -> bytes:
    """Reduce diagramas mermaid excesivamente altos y estrechos antes de insertarlos en el PDF.

    Hallazgo 2026-08-24, contrastado con el mismo problema en el repositorio hermano
    1DAMProgramacion: WeasyPrint 62.3 tiene un fallo de paginacion, sin excepcion ni aviso en el
    log, que se dispara al maquetar una imagen concreta con dimensiones nativas grandes y de
    aspecto muy vertical (alto/ancho alto) -confirmado alli con un diagrama de 486x1114 px al subir
    la escala de mmdc de -s 1 a -s 2-, y trunca el resto del documento sin dejar rastro. El
    diagrama `flowchart TD` con mas nodos encadenados de este sitio genera 567x1495 px incluso a
    escala 1 (la escala minima), justo en la unidad donde el PDF de producción se corta. El
    `style="max-height"` en CSS no evita el fallo porque este ocurre al decodificar/maquetar el
    PNG por sus dimensiones nativas, antes de que WeasyPrint aplique ningun estilo. Se reescala
    aqui con Pillow a una altura maxima segura, conservando el aspecto; con eso basta para que el
    PNG que llega a WeasyPrint tenga las dimensiones de cualquier otro diagrama del sitio que ya
    se sabe que renderiza bien.
    """
    with Image.open(io.BytesIO(data)) as img:
        width, height = img.size
        if height <= _TALL_HEIGHT_LIMIT:
            return data
        scale = _TALL_HEIGHT_LIMIT / height
        new_size = (max(1, round(width * scale)), _TALL_HEIGHT_LIMIT)
        resized = img.resize(new_size, Image.LANCZOS)
        buf = io.BytesIO()
        resized.save(buf, format='PNG')
        return buf.getvalue()


def _quote_labels(code: str) -> str:
    """Wrap unquoted labels in quotes to handle special characters."""
    def _wrap(m):
        inner = m.group(1)
        if inner.startswith('"') and inner.endswith('"'):
            return m.group(0)
        esc = inner.replace('\\', '\\\\').replace('"', '\\"')
        return f'["{esc}"]'
    return re.sub(r'\[([^\[\]]*)\]', _wrap, code)


def _render_mermaid_png(code: str, index: int) -> str | None:
    key = hashlib.sha256(code.encode()).hexdigest()
    if key in _cache:
        return _cache[key]

    result_png = b''

    def _attempt(mmd_text: str) -> bool:
        nonlocal result_png
        with tempfile.NamedTemporaryFile(suffix='.mmd', delete=False, mode='w') as f_in:
            f_in.write(mmd_text)
            mmd_path = f_in.name
        png_path = mmd_path.replace('.mmd', '.png')
        ok = _mmdc_render(mmd_text, mmd_path, png_path)
        if ok:
            data = Path(png_path).read_bytes()
            ok = _valid_png(data)
            if ok:
                result_png = _shrink_if_tall(data)
        for p in [mmd_path, png_path]:
            Path(p).unlink(missing_ok=True)
        return ok

    strategies = [
        ('original', code),
        ('quoted labels', _quote_labels(code)),
    ]

    for name, text in strategies:
        try:
            if _attempt(text):
                filename = f'{key}.png'
                out_path = _mermaid_asset_dir() / filename
                if not out_path.exists():
                    out_path.write_bytes(result_png)
                rel_path = _relative_asset_path(_current_page, filename)
                _cache[key] = rel_path
                return rel_path
        except Exception as e:
            print(f'  [hooks] mmdc {name} exception ({_current_page}, idx {index}): {e}')

    print(f'  [hooks] mmdc all strategies failed ({_current_page}, idx {index})')
    _cache[key] = None
    return None


MERMAID_RE = re.compile(
    r'<pre class="mermaid"[^>]*><code[^>]*>(.*?)</code></pre>',
    re.DOTALL,
)


def on_page_markdown(markdown, page, config, files):
    site_url = config.get('site_url', '').rstrip('/')
    return markdown.replace('{{ site_url }}', site_url)


def on_page_content(html, page, config, files):
    if not PRERENDER:
        return html

    _cache.clear()
    rendered = [0]
    global _current_page, _site_dir
    _current_page = page.url
    _site_dir = config['site_dir']

    def _replace(match):
        code = match.group(1)
        code = code.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&')
        code = code.replace('&quot;', '"').replace('&#39;', "'")

        rel_path = _render_mermaid_png(code, rendered[0])
        rendered[0] += 1

        if rel_path:
            return f'<p><img class="mermaid-rendered" src="{rel_path}" alt="Mermaid diagram" style="max-width:70%;height:auto;max-height:350px;" /></p>'
        return match.group(0)

    result = MERMAID_RE.sub(_replace, html)

    if rendered[0] > 0:
        print(f'  [hooks] Pre-rendered {rendered[0]} Mermaid diagram(s) on {page.url}')

    return result
