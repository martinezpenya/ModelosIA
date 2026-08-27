# UD03 · Notebooks guiados

!!! info "Cómo se trabajan"
    Estos cinco notebooks **no se entregan**: se hacen en clase, con el profesor, y son la
    preparación de las [entregas de la unidad](UD03_Entregas.md). Están ejecutados: puedes
    leerlos antes de tocar nada para ver qué hace cada celda.

!!! warning "Dos entornos"
    - **`N01` y `N04`**: van en el **contenedor de la unidad** (`docker compose up -d` en esta
      carpeta) o en cualquier Python 3.12+ con `nltk` y spaCy.
    - **`N02`, `N03` y `N05`**: usan `transformers`, entrenan modelos o procesan audio. Van en
      **Colab**, que tiene GPU — en local, sin GPU, tardan horas.

<!-- AUTO:notebooks inicio -->
| Notebook | Qué es | Descargar | Abrir en Colab |
|---|---|---|---|
| [`N01` · Introducción al procesamiento del lenguaje natural](notebooks/UD03_N01_introduccion_pln.ipynb) | Introducción · el pipeline de PLN de punta a punta | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N01_introduccion_pln.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N01_introduccion_pln.ipynb){:target="_blank"} |
| [`N02` · Clasificador de noticias](notebooks/UD03_N02_clasificacion_texto_torch.ipynb) | Clasificación de texto con PyTorch | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N02_clasificacion_texto_torch.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N02_clasificacion_texto_torch.ipynb){:target="_blank"} |
| [`N03` · Modelos de lenguaje, DistilBERT](notebooks/UD03_N03_modelos_lenguaje_distilbert.ipynb) | Modelos de lenguaje · DistilBERT | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N03_modelos_lenguaje_distilbert.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N03_modelos_lenguaje_distilbert.ipynb){:target="_blank"} |
| [`N04` · Primeros pasos con spaCy](notebooks/UD03_N04_spacy_primeros_pasos.ipynb) | Primeros pasos con spaCy | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N04_spacy_primeros_pasos.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N04_spacy_primeros_pasos.ipynb){:target="_blank"} |
| [`N05` · Ampliación: clasificador de géneros musicales](notebooks/UD03_N05_ampliacion_generos_musicales.ipynb) | Ampliación · clasificador de géneros musicales | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N05_ampliacion_generos_musicales.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N05_ampliacion_generos_musicales.ipynb){:target="_blank"} |
| [`N06` · Representación de texto](notebooks/UD03_N06_representacion_texto.ipynb) | Práctica · representación de texto por dos caminos | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N06_representacion_texto.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N06_representacion_texto.ipynb){:target="_blank"} |
| [`N07` · NLTK y Python](notebooks/UD03_N07_nltk_python.ipynb) | Práctica · etiquetado con NLTK y `cess_esp` | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD03/notebooks/UD03_N07_nltk_python.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD03/notebooks/UD03_N07_nltk_python.ipynb){:target="_blank"} |
<!-- AUTO:notebooks fin -->

## N01 · Introducción al PLN

Los fundamentos con `nltk` y TextBlob: tokenizar, quitar *stopwords*, etiquetar categorías
gramaticales, extraer frases nominales y construir representaciones bolsa de palabras, tf-idf y
*word embeddings*.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_N01_introduccion_pln.ipynb`](notebooks/UD03_N01_introduccion_pln.ipynb) |
!!! caution "`gensim` no instala en Python 3.14"
    La celda de *Word2Vec* usa `gensim`, que **todavía no publica rueda para Python 3.14** (su
    última versión, 4.4.0, llega hasta 3.13). En el contenedor de la unidad no pasa nada —lleva
    Python 3.12—, pero si trabajas con un intérprete más nuevo, esa celda concreta fallará al
    instalar. El resto del notebook no depende de `gensim`.

## N02 · Clasificación de texto con PyTorch

Construye un clasificador de texto **desde cero**: de la bolsa de palabras a los *word embeddings*,
con un modelo de PyTorch entrenado y evaluado. Es el notebook que `N09` repite sobre datos propios.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_N02_clasificacion_texto_torch.ipynb`](notebooks/UD03_N02_clasificacion_texto_torch.ipynb) |

## N03 · Modelos de lenguaje: afinar DistilBERT

*Transfer learning* de manual: parte de un **DistilBERT** preentrenado y lo afina para análisis de
sentimiento con una base de datos de tuits. `N10` repite el proceso sobre reseñas de cine.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_N03_modelos_lenguaje_distilbert.ipynb`](notebooks/UD03_N03_modelos_lenguaje_distilbert.ipynb) |

## N04 · spaCy, primeros pasos

El *pipeline* de spaCy de una sola pasada: tokenización, POS, dependencias y entidades, sobre texto
en español.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_N04_spacy_primeros_pasos.ipynb`](notebooks/UD03_N04_spacy_primeros_pasos.ipynb) |

## N05 · Ampliación: clasificador de géneros musicales

Un sistema de PLN aplicado a **audio**: clasificar el género de una canción combinando `librosa` y
`transformers`. Es el notebook más largo del módulo (240 celdas) y **no cuenta horas de la unidad**:
queda como material de ampliación para quien quiera ir más allá de `N11`.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_N05_ampliacion_generos_musicales.ipynb`](notebooks/UD03_N05_ampliacion_generos_musicales.ipynb) |

---
[Volver a la UD03](UD03_ES.md) · [Entregas](UD03_Entregas.md)
