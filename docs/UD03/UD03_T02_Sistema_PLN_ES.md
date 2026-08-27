# UD03 · Taller 2 — Un sistema de PLN de punta a punta

!!! important "Entrega evaluable"
    Se entrega en Moodle y se corrige con su **rúbrica**, que puedes leer en la propia tarea
    antes de empezar. El **peso** de esta entrega está en el libro de calificaciones de Moodle.
    Trabaja en parejas si lo indica el profesor.

!!! tip "Hazlo en el notebook"
    Tienes este taller como **notebook con las celdas a rellenar**:
    [`UD03_T02_sistema_pln.ipynb`](notebooks/UD03_T02_sistema_pln.ipynb). Esta página es la referencia; lo que se entrega es el
    notebook completado.

!!! warning "Requisitos"
    Va en el **contenedor de la unidad** (`docker compose up -d` en la carpeta de la UD03), o en
    cualquier Python 3.12+ con:

    ```bash
    pip install nltk spacy scikit-learn
    python -m spacy download es_core_news_sm
    ```

    Este taller **no necesita GPU ni Colab**.

**Objetivo**: construir un **extractor de entidades** (NER) para textos de un dominio concreto con
`spaCy`, siguiendo la metodología del CE g (tarea → datos → herramienta → implementar → evaluar →
documentar).

### Fase 1 — Define la tarea

Elige un dominio (p. ej. **facturas**, **historias clínicas de ejemplo**, **noticias de
tecnología**). Decide qué entidades quieres extraer (nombres de empresa, personas, lugares,
fechas, importes, productos).

### Fase 2 — Datos

Crea al menos **10 textos de ejemplo** del dominio en un fichero `textos.txt` (pueden ser
inventados). Indica origen y licencia en el informe.

### Fase 3 — Implementa con spaCy

```python
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("es_core_news_sm")
matcher = Matcher(nlp.vocab)

# patrón propio: detectar "empresa de <algo>" o importes en euros
matcher.add("EMPRESA", [[{"LOWER": {"IN": ["empresa", "compañía"]}},
                         {"POS": "ADP", "OP": "?"},
                         {"IS_ALPHA": True, "OP": "+"}]])
matcher.add("IMPORTE", [[{"LIKE_NUM": True}, {"LOWER": {"IN": ["€", "euros"]}}]])

def extraer(texto):
    doc = nlp(texto)
    entidades = [(e.text, e.label_) for e in doc.ents]
    matches = matcher(doc)
    return entidades, [(doc[s:e].text, "PATRON_EMPRESA/IMPORTE") for _, s, e in matches]

for linea in open('textos.txt', encoding='utf-8'):
    print(extraer(linea.strip()))
```

### Fase 4 — Evalúa

Compara las entidades que devuelve spaCy con las que esperabas (anótalas a mano primero).
Calcula cuántas acertó y dónde falló. ¿Qué patrones añadirías?

### Fase 5 — Documenta

Escribe en el informe: la **tarea**, el **origen/licencia de los datos**, la **herramienta**
(spaCy + Matcher), las **reglas/patrones** usados, la **evaluación** (aciertos/fallos) y las
**limitaciones** (dominio, textos fuera de contexto, ambigüedad).

### Fase 6 — Mejora (reto)

Añade 2 patrones más de tu dominio (p. ej. fechas en formato "dd/mm/aaaa" o códigos de producto)
y repite la evaluación. ¿Mejoró la cobertura?

### Entrega del Taller 2

Sube el **notebook ejecutado**, siguiendo los seis pasos de la metodología del §12.1.

| Fase | Evidencia mínima |
|---|---|
| 1 | La tarea definida: qué entra, qué sale y para quién |
| 2 | Los datos, con **origen, tamaño y licencia** |
| 3 | El sistema implementado con spaCy y funcionando |
| 4 | La evaluación sobre datos no vistos, con el análisis de errores |
| 5 | La documentación: decisiones tomadas y **limitaciones asumidas** |
| 6 | La mejora propuesta, aunque no esté implementada |

Y la respuesta a: *¿por qué elegiste esa herramienta y no otra?* La respuesta buena habla de **los
datos que tenías**, no de lo moderna que sea la técnica.

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD03](UD03_ES.md) · [Taller 1](UD03_T01_Del_texto_al_vector_ES.md) · [Ejercicios](UD03_Ejercicios.md)
