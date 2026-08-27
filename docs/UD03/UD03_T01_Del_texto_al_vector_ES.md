# UD03 · Taller 1 — Del texto al vector: análisis de sentimiento

!!! important "Entrega evaluable"
    Se entrega en Moodle y se corrige con su **rúbrica**, que puedes leer en la propia tarea
    antes de empezar. El **peso** de esta entrega está en el libro de calificaciones de Moodle.
    Trabaja en parejas si lo indica el profesor.

!!! tip "Hazlo en el notebook"
    Tienes este taller como **notebook con las celdas a rellenar**:
    [`UD03_T01_del_texto_al_vector.ipynb`](notebooks/UD03_T01_del_texto_al_vector.ipynb). Esta página es la referencia; lo que se entrega es el
    notebook completado.

!!! warning "Requisitos"
    Va en el **contenedor de la unidad** (`docker compose up -d` en la carpeta de la UD03), o en
    cualquier Python 3.12+ con:

    ```bash
    pip install nltk spacy scikit-learn
    python -m spacy download es_core_news_sm
    ```

    Este taller **no necesita GPU ni Colab**.

**Objetivo**: construir un clasificador que determine si una reseña es positiva o negativa,
usando un dataset anotado por el alumnado y `scikit-learn`.

### Fase 1 — Crea tu dataset (origen y licencia)

Crea un fichero `reseñas.csv` con al menos **30 reseñas cortas** en español (por parejas: 20 de
entrenamiento, 10 de prueba) y su etiqueta (`1` = positiva, `0` = negativa). Anota en el informe el
**origen** (opiniones propias o de un restaurante ficticio) y la **licencia** (p. ej. anotación
propia bajo CC BY).

| texto | etiqueta |
|---|---|
| La comida estaba riquísima y el servicio rápido | 1 |
| Pedimos y el plato llegó frío | 0 |
| ... | ... |

### Fase 2 — Preprocesado con nltk

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download(['punkt_tab', 'stopwords'])

STOP = set(stopwords.words('spanish'))

def limpiar(texto):
    tokens = word_tokenize(texto.lower(), language='spanish')
    return ' '.join(t for t in tokens if t.isalpha() and t not in STOP)
```

Aplica `limpiar` a todas las reseñas y muestra 3 ejemplos antes/después.

### Fase 3 — Vectorizar y entrenar

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

df = pd.read_csv('reseñas.csv')
X = df['texto'].apply(limpiar)
y = df['etiqueta']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

pipe = make_pipeline(TfidfVectorizer(), LogisticRegression())
pipe.fit(X_train, y_train)
print("Exactitud:", pipe.score(X_test, y_test))
```

### Fase 4 — Matriz de confusión

```python
from sklearn.metrics import confusion_matrix, classification_report
pred = pipe.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
```

Interpeta la matriz: ¿cuántos positivos correctos, cuántos falsos positivos?

### Fase 5 — Prueba con reseñas nuevas

```python
for texto in ["El local está bien pero se notaba sucio", "¡Espectacular, volveré mañana!"]:
    print(pipe.predict([limpiar(texto)])[0], "←", texto)
```

### Fase 6 — Análisis de errores

Busca en el test al menos **2 errores** del modelo e intenta explicarlos (jerga, ironía,
ambigüedad, vocabulario nuevo). Documenta la conclusión.

### Entrega del Taller 1

Sube el **notebook ejecutado**. Se valora que **interpretes** los resultados, no solo que las celdas
den un número.

| Fase | Evidencia mínima |
|---|---|
| 1 | El conjunto de reseñas, con su **origen y licencia** declarados |
| 2 | El texto preprocesado: tokens, sin *stopwords*, normalizado |
| 3 | El clasificador entrenado y su exactitud sobre datos **no vistos** |
| 4 | La matriz de confusión, **interpretada**: qué confunde con qué |
| 5 | Las predicciones sobre reseñas nuevas, tuyas |
| 6 | **Dos errores leídos uno a uno** y qué tipo de ambigüedad los explica |

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD03](UD03_ES.md) · [Taller 2](UD03_T02_Sistema_PLN_ES.md) · [Ejercicios](UD03_Ejercicios.md)
