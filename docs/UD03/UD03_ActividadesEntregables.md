# UD03 · Actividades entregables

!!! important "Los cinco cuentan para la nota del RA3"
    Los cinco notebooks forman el **40 % de actividades** del RA3. Cada uno se califica **sobre 10**
    con su [rúbrica](#rubricas), que tienes más abajo. `EX2` y `EX4` llevan además una **parte
    escrita** que cubre los criterios sobre el papel del lingüista, el trabajo cooperativo y la
    formación del investigador (RA3-b, RA3-e, RA3-f) — léela antes de empezar, porque cuenta en la
    rúbrica.

!!! warning "Dos entornos"
    `EX1` y `EX2.5` van en el **contenedor** de la unidad. `EX2`, `EX3` y `EX4` usan
    `transformers` o audio: van en **Colab**.

!!! caution "Identificadores de *dataset* que ya no funcionan"
    Los nombres clásicos de algunos conjuntos de datos de Hugging Face **ya no resuelven**:
    `datasets` exige el formato `namespace/name`. `EX2` usa
    [`SetFit/TREC-QC`](https://huggingface.co/datasets/SetFit/TREC-QC) en vez de `trec`, y `EX3`
    usa [`stanfordnlp/imdb`](https://huggingface.co/datasets/stanfordnlp/imdb) en vez de `imdb`.

!!! caution "`EX4`: tres trampas verificadas"
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

## EX2.5 · NLTK y Python: etiquetado con `cess_esp`

Procesa el corpus español anotado `cess_esp`: separa entrenamiento y prueba, reduce el conjunto de
etiquetas morfosintácticas de 289 a un conjunto manejable, y valida con validación cruzada.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_EX2_5_nltk_python.ipynb`](notebooks/UD03_EX2_5_nltk_python.ipynb) |

**Se entrega**: el notebook con los seis apartados resueltos.

## EX3 · Análisis de sentimiento en reseñas de cine

*Transfer learning*: parte del DistilBERT de `N03` —afinado para tuits— y adáptalo a reseñas de
IMDb, un dominio distinto.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_EX3_sentimiento_imdb.ipynb`](notebooks/UD03_EX3_sentimiento_imdb.ipynb) |

**Se entrega**: el notebook con el modelo afinado y evaluado sobre las reseñas.

## EX4 · Asistente virtual por voz

Encadena tres modelos —voz a texto, traducción y texto a voz— en **una sola función** que reciba un
audio y devuelva otro.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD03_EX4_asistente_virtual.ipynb`](notebooks/UD03_EX4_asistente_virtual.ipynb) |
| Audio de prueba | [`OpenTheDoor.wav`](notebooks/OpenTheDoor.wav) |

**Se entrega**: el notebook con la función conjunta funcionando de punta a punta, **y una sección
final** que responda: ¿qué papel tendría un lingüista revisando las transcripciones y traducciones de
este asistente? ¿Qué formación necesitaría el equipo si el asistente tuviera que funcionar en varios
idiomas?

## Rúbricas

Son las rúbricas reales del curso. Las cinco tareas se califican **sobre 10**; los puntos de cada
rúbrica se **escalan** a esa nota.

### EX1 · Representación de texto (8 puntos)

Cuatro criterios de 2 puntos, uno por ejercicio (correcta 2 · parcial 1 · incorrecta 0,5).

### EX2 · Clasificador de preguntas (18 puntos)

| Criterio | Puntos |
|---|---|
| Preparación del entorno | 2 |
| Cargar el *dataset* | 2 |
| Tokenización | 2 |
| Bolsa de palabras | 2 |
| *Word embeddings* | 2 |
| Crear el modelo neuronal | 2 |
| Entrenar | 2 |
| Evaluación | 2 |
| **Conclusiones o comentarios** | 2 |

El último criterio es donde se puntúa la **parte escrita** sobre el lingüista y la cooperación.

### EX2.5 · NLTK y `cess_esp` (10 puntos)

Cinco criterios de 2 puntos, apartados a) a e).

### EX3 · Sentimiento en IMDb (10 puntos)

| Criterio | Puntos |
|---|---|
| Cargar el *dataset* | 2 |
| Evaluación previa | 2 |
| Definir las etiquetas | 2 |
| Afinar el modelo (*fine-tuning*) | 2 |
| Inferencia | 2 |

### EX4 · Asistente virtual (8 puntos)

| Criterio | Puntos |
|---|---|
| Modelo voz a texto | 2 |
| Modelo de traducción | 2 |
| Modelo texto a voz | 2 |
| **Función conjunta con todos los pasos** | 2 |

El cuarto criterio es el que demuestra RA3-g: encadenar los tres modelos en un sistema, no usarlos
por separado.

---
[Volver a la UD03](UD03_ES.md) · [Actividades guiadas](UD03_ActividadesGuiadas.md) · Talleres: [T01](UD03_T01_Del_texto_al_vector_ES.md) · [T02](UD03_T02_Sistema_PLN_ES.md)
