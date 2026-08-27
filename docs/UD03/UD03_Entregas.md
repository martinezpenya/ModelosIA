# UD03 · Entregas

!!! important "Qué se entrega y qué es práctica"
    No todo lo de esta página se entrega. Las **entregas** se corrigen con la rúbrica de su
    tarea en Moodle, que puedes leer antes de empezar; la **práctica** se hace para preparar la
    prueba escrita y no se entrega ni puntúa.

    | Actividad | Régimen |
    |---|---|
    | [`T01` Del texto al vector](UD03_T01_Del_texto_al_vector_ES.md) | Entrega evaluable |
    | [`T02` Un sistema de PLN de punta a punta](UD03_T02_Sistema_PLN_ES.md) | Entrega evaluable |
    | `EX2` Clasificador de preguntas | Entrega evaluable |
    | `EX4` Análisis de sentimiento en IMDb | Entrega evaluable |
    | `EX5` Asistente virtual por voz | Entrega evaluable |
    | `EX1` Representación de texto | Práctica |
    | `EX3` NLTK y `cess_esp` | Práctica |

    `EX2` y `EX5` llevan además una **parte escrita** que cubre los criterios sobre el papel del
    lingüista, el trabajo cooperativo y la formación del investigador (RA3-b, RA3-e, RA3-f) — léela
    antes de empezar, porque cuenta en la rúbrica.

    El **peso** de cada entrega está en el libro de calificaciones de Moodle, no aquí.

!!! warning "Dos entornos"
    `EX1` y `EX3` van en el **contenedor** de la unidad. `EX2`, `EX4` y `EX5` usan
    `transformers` o audio: van en **Colab**.

!!! caution "Identificadores de *dataset* que ya no funcionan"
    Los nombres clásicos de algunos conjuntos de datos de Hugging Face **ya no resuelven**:
    `datasets` exige el formato `namespace/name`. `EX2` usa
    [`SetFit/TREC-QC`](https://huggingface.co/datasets/SetFit/TREC-QC) en vez de `trec`, y `EX4`
    usa [`stanfordnlp/imdb`](https://huggingface.co/datasets/stanfordnlp/imdb) en vez de `imdb`.

!!! caution "`EX5`: tres trampas verificadas"
    `pipeline("translation", ...)` ya no existe como tarea genérica (usa `AutoTokenizer` +
    `AutoModelForSeq2SeqLM`), cargar el audio con la ruta directa puede pedir `ffmpeg` (carga con
    `librosa` en su lugar) y el modelo de traducción necesita `sentencepiece`. Todo explicado en el
    propio notebook.

## EX1 · Representación de texto, por dos caminos

Tokenizar, quitar *stopwords* y construir una bolsa de palabras y un vector tf-idf, resuelto **con
NLTK y con TextBlob** — el mismo ejercicio, dos librerías.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_EX1_representacion_texto.ipynb`](notebooks/UD03_EX1_representacion_texto.ipynb) |

**Se entrega**: el notebook con los cuatro ejercicios resueltos por **uno** de los dos caminos —tú
eliges— y una comparación breve con el otro.

## EX2 · Clasificador de preguntas

Repite el proceso de `N02` —de la bolsa de palabras a un clasificador entrenado— sobre un conjunto
de **preguntas**, en vez de noticias.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_EX2_clasificador_preguntas.ipynb`](notebooks/UD03_EX2_clasificador_preguntas.ipynb) |

**Se entrega**: el notebook con el clasificador entrenado y evaluado, **y una sección de
conclusiones** que responda: ¿qué decisiones de anotación tomaría un lingüista con este conjunto de
preguntas? ¿Qué perfiles harían falta si el proyecto creciera? ¿Qué formación necesitarías tú para
mejorar este sistema?

## EX3 · NLTK y Python: etiquetado con `cess_esp`

Procesa el corpus español anotado `cess_esp`: separa entrenamiento y prueba, reduce el conjunto de
etiquetas morfosintácticas de 289 a un conjunto manejable, y valida con validación cruzada.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_EX3_nltk_python.ipynb`](notebooks/UD03_EX3_nltk_python.ipynb) |

**Se entrega**: el notebook con los seis apartados resueltos.

## EX4 · Análisis de sentimiento en reseñas de cine

*Transfer learning*: parte del DistilBERT de `N03` —afinado para tuits— y adáptalo a reseñas de
IMDb, un dominio distinto.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_EX4_sentimiento_imdb.ipynb`](notebooks/UD03_EX4_sentimiento_imdb.ipynb) |

**Se entrega**: el notebook con el modelo afinado y evaluado sobre las reseñas.

## EX5 · Asistente virtual por voz

Encadena tres modelos —voz a texto, traducción y texto a voz— en **una sola función** que reciba un
audio y devuelva otro.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_EX5_asistente_virtual.ipynb`](notebooks/UD03_EX5_asistente_virtual.ipynb) |
| Audio de prueba | [`OpenTheDoor.wav`](notebooks/OpenTheDoor.wav) |

**Se entrega**: el notebook con la función conjunta funcionando de punta a punta, **y una sección
final** que responda: ¿qué papel tendría un lingüista revisando las transcripciones y traducciones de
este asistente? ¿Qué formación necesitaría el equipo si el asistente tuviera que funcionar en varios
idiomas?

!!! info "La rúbrica está en Moodle"
    La rúbrica de cada entrega se ve **en la propia tarea de Moodle**, y puedes leerla **antes** de
    empezar: ahí tienes los criterios, los niveles y lo que puntúa cada uno. No se duplica aquí para
    que no haya dos versiones del mismo dato.

---
[Volver a la UD03](UD03_ES.md) · [Notebooks guiados](UD03_ActividadesGuiadas.md) · Talleres: [T01](UD03_T01_Del_texto_al_vector_ES.md) · [T02](UD03_T02_Sistema_PLN_ES.md)
