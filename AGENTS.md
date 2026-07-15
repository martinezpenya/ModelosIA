# AGENTS.md — ModelosIA

## What this is

MkDocs Material site with course notes for "Modelos de Inteligencia Artificial" (CE IA&BD). No application code — pure documentation.

## Commands

```bash
mkdocs serve          # dev server with live reload
mkdocs build          # build static site
mkdocs build --clean  # fresh build
```

The PDF (`docs/Libro.pdf`) is generated automatically during `mkdocs build` via the `mkdocs-with-pdf` plugin — no separate step needed.

## Setup

```bash
python3 -m venv ~/virtual-envs/mkdocs
source ~/virtual-envs/mkdocs/bin/activate
pip install -r requirements.txt
```

Or just run `./serve.sh` which does all the above then `mkdocs serve`.

## Key config

- `mkdocs.yml` is the single source of truth for nav, theme, plugins, and extensions
- `use_directory_urls: false` — page URLs use `.html` extension
- Math rendering via MathJax (configured in `js/mathjax-config.js`); math in markdown uses `\(...\)` / `\[...\]` (enabled by `pymdownx.arithmatex`)
- **Do NOT add `polyfill.io`** — the service was sold to a malicious actor (2024) and removed from `extra_javascript`
- Mermaid diagrams via `pymdownx.superfences` custom fence
- Extra CSS from `extra_sass/style.css.scss` compiled by `mkdocs-extra-sass-plugin`

## PDF output

- `mkdocs-with-pdf` plugin outputs `docs/Libro.pdf`
- Custom cover/back-cover templates in `templates/`
- `pdf_event_hook/__init__.py` injects a PDF download button into the nav bar
- The `offline` plugin is commented out (it would break SEO)

## Structure

```
docs/          → markdown source files, one per nav entry
  UD01..UD05/  → units, each with theory, slides, guided activities, deliverables
  assets/      → images, portada.png
  css/         → extra.css
mkdocs.yml     → site config
```

## Style conventions

- Content language is Spanish (`language: es` in mkdocs.yml, `search.language: es`)
- Admonitions heavily used (note, tip, warning, danger, example, etc.)
- Light/dark mode toggle via Material palette
- CC BY-NC-SA 4.0 license
