---
marp: true
---
<!--
theme: gaia
size: 16:9
_class: lead
paginate: true
marp: false
backgroundColor: #000
backgroundImage: url('img/hero-backgroundIES.jpg')
-->
<style>
section::after {
  content: attr(data-marpit-pagination) '/' attr(data-marpit-pagination-total);}
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
table {
  margin-left: auto;
  margin-right: auto;
}
footer {
  font-size: 20px;
 }
header {
  font-size: 16px;
 }
</style>
<style scoped>
section {
  @extend .markdown-body;
  font-size: 28px;
  justify-content: top;
 }
</style>

![h:260 center](../assets/cover.png)
# UD03: Procesamiento del Lenguaje Natural
#### Modelos de Inteligencia Artificial
###### version: 2026-08-23

---
<!-- footer: d.martinezpena@edu.gva.es -->
<!-- header: Modelos de Inteligencia Artificial 26-27 (UD03_1)-->
<style scoped>section { font-size: 28px; }</style>

# ¿Qué veremos?

1. Qué es el PLN
2. El potencial, con cifras
3. La ambigüedad
4. Desambiguación y POS *tagging*
5. Las demás limitaciones
6. Cuándo es factible: la lupa del AI Act
7. Quién hace un proyecto de PLN
8. Las herramientas en Python
9. Construir un sistema orientado a una tarea

---
<style scoped>section { font-size: 25px; }</style>

<style scoped>section { font-size: 24px; }</style>

## RA3 y sus criterios de evaluación

> **RA3** — Relaciona el PLN con sus aplicaciones, su potencial y sus limitaciones.

| CE | Criterio | Dónde |
|---|---|---|
| **a** | Caracterizar el PLN | §1, §4 |
| **b** | Papel del lingüista | §7 |
| **c** | Potencial y limitaciones | §2-5 |
| **d** | Cuándo es factible | §6 |
| **e** | Trabajo cooperativo | §7 |
| **f** | Formación del investigador | §7 |
| **g** | Elaborar un sistema | §8-9 |

**Siete criterios**: los más de todo el módulo.

---
<style scoped>section { font-size: 23px; }</style>

## Al terminar la unidad serás capaz de…

- **Explicar** qué es el PLN y situarlo entre lingüística e informática.
- **Distinguir** los seis tipos de ambigüedad en frases reales.
- **Explicar** cómo el etiquetado POS desambigua, y qué cuesta elegir el conjunto de etiquetas.
- **Determinar** cuándo es factible aplicar PLN, con el AI Act.
- **Justificar** el papel del lingüista y **evaluar** la cooperación con informáticos.
- **Usar** `nltk` y spaCy para tareas básicas en español.
- **Construir y evaluar** un sistema de PLN orientado a una tarea.

---
<!-- _class: lead -->

# 1. Qué es el PLN

###### RA3-a

---

<style scoped>section { font-size: 25px; }</style>

## Tres disciplinas, un campo

| Disciplina | Qué aporta |
|---|---|
| **Lingüística computacional** | Modelos del lenguaje: morfología, sintaxis, semántica |
| **Estadística y ML** | Aprender patrones de los textos |
| **Aprendizaje profundo** | Representaciones del lenguaje (*transformers*) |

**No es magia**: se procesa **estadísticamente**, no se «entiende» como una persona.

---
<style scoped>section { font-size: 24px; }</style>

## Los niveles del lenguaje

| Nivel | Analiza | Tarea de PLN |
|---|---|---|
| **Fonética/fonología** | Sonidos | ASR, TTS |
| **Morfología** | Estructura de palabras | *Stemming*, lematización, **POS** |
| **Sintaxis** | Estructura de oraciones | Análisis sintáctico |
| **Semántica** | Significado | Desambiguación, entidades |
| **Pragmática** | Según contexto | Correferencia, sentimiento |

Hay ambigüedad en **todos** los niveles: es el mapa del bloque 3.

---
<style scoped>section { font-size: 24px; }</style>

## Las tareas del PLN

| Tarea | Ejemplo |
|---|---|
| Tokenización | «Hola mundo» → [«Hola», «mundo»] |
| Etiquetado POS | «correr» → verbo |
| Entidades (NER) | «María vive en Madrid» → PER, LOC |
| Sentimiento | «¡Genial!» → positivo |
| Traducción, resumen, generación | — |
| Respuesta a preguntas | Asistentes, buscadores |

---

## El *pipeline*, siempre igual

```text
Texto ──► Preprocesado ──► Representación ──► Modelo ──► Salida
          tokenizar,       BoW, tf-idf,        ML o red   clasificación,
          minúsculas,      embeddings          profunda   entidades...
          stopwords
```

El corrector, el buscador y el asistente de voz son los mismos cuatro pasos.

---
<!-- _class: lead -->

# 2. El potencial

###### RA3-c

---
<style scoped>section { font-size: 24px; }</style>

## Qué se consigue hoy

| Aplicación | Estado |
|---|---|
| Buscadores, asistentes de voz | Entienden, extraen entidades, responden |
| Traducción automática | Calidad funcional en tiempo real |
| Análisis de opinión | Miles de reseñas, automático |
| Extracción de información | Facturas y contratos, sin tocarlos a mano |
| Modelos generativos | Redactar, resumir, traducir |

---

## Tres cifras para calibrar

- **SQuAD 2.0**: los mejores sistemas **superan la precisión humana** (EM ~91 frente a ~87).
- Sentimiento en IMDb: de ~89 % (2011) a **95-97 %** con *transformers*.
- Hugging Face: más de **2 millones de modelos**, 500.000 *datasets*.

---

## Los modelos de uso general

El **AI Act** los define: **≥ 1.000 millones de parámetros**, autosupervisión a gran escala, competentes en muchas tareas. Los LLM son el ejemplo típico.

**Capacidades de gran impacto**: cuando el cómputo del entrenamiento supera **10²⁵ FLOPS** (art. 51.2) → documentación y evaluación adicionales. Se ve a fondo en la UD06.

---
<!-- _class: lead -->

# 3. La ambigüedad

### el problema de fondo

###### RA3-c

---

<style scoped>section { font-size: 25px; }</style>

## Seis tipos

| Tipo | Cuándo aparece |
|---|---|
| **Sintáctica** | Más de un análisis gramatical posible |
| **Léxica / morfológica** | Un término admite varias lecturas |
| **Semántica** | Un elemento tiene varios sentidos |
| **Pragmática** | Depende del contexto y de quién habla |
| **Fonológica** | Una cadena de sonidos confunde |
| **Funcional** | Doble función gramatical |

---
<style scoped>section { font-size: 24px; }</style>

## Los seis, con frases reales

- **Sintáctica** — *«Compro los libros baratos»*: ¿los baratos, o libros que además son baratos?
- **Léxica** — *«Usted aquí no pinta nada»*: ¿mando, o pintar una pared?
- **Semántica** — *«Pedro quiere pelearse con un italiano»*: ¿cualquiera, o uno concreto?
- **Pragmática** — *«Golpeó el armario con el bastón y lo rompió»*: ¿qué se rompió?
- **Fonológica** — *«es-conde»*: ¿esconder, o «es» + «conde»?
- **Funcional** — *«He vuelto a oler»*: ¿recuperé el olfato, o regresé a oler algo?

---

## Un banco de frases para probar cualquier sistema

- El cura recibió una cura en su habitación.
- Antonio no nada nada.
- No puedo ir a la fiesta porque no traje traje.
- El Villarreal le ganó al Valencia en su campo.
- Me quedé esperándote en el banco.

Casi todas se resuelven **con el contexto**, no con la frase.

---

## No se arregla: se decide

La ambigüedad **no es un error** del lenguaje: es una propiedad, y además útil.

**Forma ≠ significado** (Bender y Koller): un modelo entrenado solo con la forma **no tiene forma *a priori*** de aprender el significado. Aprende correlaciones, no comprensión.

Por eso un modelo generativo puede sonar impecable **y** estar equivocado.

---
<!-- _class: lead -->

# 4. Desambiguación y POS

###### RA3-a, RA3-c

---

## El mismo «sobre», tres categorías

- *«Mételo en ese **sobre**»* → **nombre**
- *«Déjalo **sobre** la mesa»* → **preposición**
- *«Dame lo que te **sobre**»* → **verbo**

Ningún diccionario resuelve esto: hace falta el **contexto**. Es el primer paso de casi todo lo demás.

---
<style scoped>section { font-size: 25px; }</style>

## Elegir el *tagset*: un compromiso

Más etiquetas = **más información** y **más difícil acertar**.

| *Tagset* | Etiquetas |
|---|---|
| Penn Treebank | 45 |
| Brown Corpus | 87 |
| LexEsp (PAROLE) | ~250 |
| Susanne | 350 |

Categorías **abiertas** (nombres, verbos) admiten palabras nuevas; **cerradas** (preposiciones), no.

---

## Por qué esto es del lingüista

Decidir el *tagset* y escribir la guía de anotación **no es programación**: es lingüística aplicada, y condiciona **todo** lo que el modelo puede aprender después.

Es el ejemplo más concreto del **RA3-b**.

---

## Cómo se etiqueta

| Enfoque | Cómo | Dónde |
|---|---|---|
| **Reglas** | A mano, sobre el contexto | Dominios muy acotados |
| **HMM / TnT** | Probabilidad de una secuencia | `cess_esp` con `nltk` |
| **Neuronal** | Con el contexto completo | spaCy, *transformers* |

---
<!-- _class: lead -->

# 5. Las demás limitaciones

###### RA3-c

---

## Falta de comprensión real

Los modelos **generan sin comprender**: no verifican hechos, no razonan, pueden **alucinar** — inventar datos con total seguridad.

En cualquier tarea con consecuencias, **la salida se verifica**.

---

## Sesgos

- Sesgo de **género** en *embeddings*: «médico → hombre», «enfermera → mujer».
- Sesgos **raciales y culturales** en los datos de entrenamiento.
- El AI Act: pueden **perpetuarse y amplificarse** en bucles de retroalimentación.

**Prohibido**: inferir emociones **en el trabajo y en centros educativos** — base científica débil, uso discriminatorio.

---

## Lenguas con pocos recursos, e ironía

- Casi todo se entrena en **inglés**. En lenguas minoritarias, lo **estadístico clásico** puede
  ganar a lo neuronal.
- *«¡Qué buena idea, se me ha caído el móvil al agua!»*: literalmente positivo, pragmáticamente
  negativo. Los modelos fallan a menudo.

---
<!-- _class: lead -->

# 6. Cuándo es factible

### la lupa del AI Act

###### RA3-d

---

## Cinco criterios

| Criterio | Pregunta guía |
|---|---|
| Tarea clara y acotada | ¿Qué salida exacta quiero? |
| Datos disponibles | ¿Hay textos suficientes y anotados? |
| Dominio conocido | ¿Vocabulario acotado? |
| Calidad realista | ¿Acepto un 5-10 % de error? |
| Regulación | ¿Lo prohíbe o restringe el AI Act? |

---
<style scoped>section { font-size: 23px; }</style>

## Factible y no factible

| Factible hoy | Prohibido o no factible |
|---|---|
| Clasificar documentos, detectar duplicados | **Inferir emociones** en trabajo o educación |
| Mejorar el registro de un texto | Extracción no selectiva de rostros |
| Traducción funcional | Manipulación subliminal |
| Análisis de sentimiento acotado | Alto riesgo sin verificación |

**Considerando 53** (bajo riesgo) + **artículo 5** (prohibiciones) = lista de comprobación antes de construir.

---
<!-- _class: lead -->

# 7. Quién hace un proyecto de PLN

###### RA3-b, RA3-e, RA3-f

---

## Qué aporta el lingüista

| Aportación | Ejemplo |
|---|---|
| Anotar datos | Etiquetar entidades, sentimiento |
| Diseñar el *tagset* y la guía | El compromiso del bloque 4 |
| Recursos lingüísticos | Corpus y *treebanks* |
| Evaluar errores | Por qué falla el modelo |

**Las anotaciones deciden las predicciones.** No se arregla con más datos.

---
<style scoped>section { font-size: 24px; }</style>

## Cooperación: dos casos reales

- **Meta NLLB** (200 idiomas): hablantes nativos anotaron y evaluaron → **+44 % de BLEU**.
- **Masakhane** (PLN africano): 1.000+ participantes, 30 países. Los lingüistas locales son
  **investigadores**, no «solo anotadores». Rechazan la investigación **paracaidista**.

| Se gana | Cuesta |
|---|---|
| Datos y evaluación mejores | Vocabularios distintos |
| Cobertura de lenguas minoritarias | Anotación lenta y cara |
| Mejor ciencia | Riesgo de explotar comunidades |

---

## La formación del investigador

**Tres patas**: lingüística · estadística y ML · informática.

**Itinerario**: Jurafsky y Martin → NLTK → spaCy → *transformers*.

**Perfiles nuevos**: anotador especializado, *prompt engineer*, evaluador de sesgos. Todos parten de la misma base.

---

## Cómo se evalúan estos tres criterios

**No con un examen aparte**: con la **parte escrita** de `EX2` y `EX4`.

Se pide justificar qué decisiones tomaría un lingüista, qué aporta cada perfil y qué formación haría falta. **Está en la rúbrica, y cuenta.**

---
<!-- _class: lead -->

# 8. Las herramientas

### en Python

###### RA3-c, RA3-g

---

## Dos entornos

- **Contenedor de la unidad**: `nltk`, spaCy, scikit-learn. Todo lo que no entrena redes grandes.
- **Colab**: `transformers`, entrenamiento, audio. Ahí hay GPU.

---

## NLTK, para entender

Transparente: cada paso, a mano.

```python
tokens = word_tokenize(texto, language='spanish')
sin_vacias = [t for t in tokens if t.lower() not in stopwords.words('spanish')]
stem = SnowballStemmer('spanish').stem
```

**Pipeline**: tokenizar → limpiar *stopwords* → normalizar (*stemming* o lematización) → enriquecer (POS, entidades, frecuencias).

---

## spaCy, para producir

Un objeto `nlp`, todo el *pipeline* de una pasada:

```text
Texto → Tokenizador → POS → Dependencias → Entidades → Lematizador
```

En una frase corriente, el analizador puede encontrar **miles de análisis posibles**: spaCy elige el más probable. La ambigüedad **no se elimina, se decide**.

**NLTK para aprender, spaCy para producir.**

---

## Sentimiento y *transformers*

- **scikit-learn** (tf-idf + regresión logística): funciona en español, sin GPU. Cuidado:
  `stop_words` solo acepta `'english'` — para español, una **lista**.
- **DistilBERT**: 40 % menos parámetros, 60 % más rápido, 97 % de la capacidad de BERT. El modelo
  de esta unidad, porque cabe en una sesión.

---
<!-- _class: lead -->

# 9. Construir un sistema

### orientado a una tarea

###### RA3-g

---
<style scoped>section { font-size: 24px; }</style>

## Seis pasos

```text
1. Definir la tarea → 2. Datos y licencia → 3. Elegir herramienta
         ↓
6. Documentar ← 5. Evaluar y analizar errores ← 4. Implementar
```

El paso que más se salta es el **5**: mirar los errores, no solo la métrica.

---
<style scoped>section { font-size: 23px; }</style>

## La progresión de los notebooks

| Notebook | Construye | Representación |
|---|---|---|
| `N01` | Tokenizar, BoW, tf-idf | Cuenta de palabras |
| `N02` | Clasificador con PyTorch | *Word embeddings* |
| `N03` | Afinar DistilBERT | *Embeddings* contextuales |
| `N04` | *Pipeline* de spaCy | Modelo preentrenado |

Y los cuatro entregables aplican cada nivel a un problema propio: **EX1** representación · **EX2** clasificador · **EX3** *transfer learning* · **EX4** asistente de punta a punta.

---

## Ejemplo guiado: clasificador de reseñas

**1** clasificar positiva/negativa · **2** 60 reseñas anotadas · **3** tf-idf, no *transformer* · **4** `TfidfVectorizer → LogisticRegression` · **5** exactitud + leer 2 errores · **6** documentar origen y límites.

**La herramienta se elige por los datos que hay**, no por lo moderna que sea.

---
<!-- _class: lead -->

# Cierre

---
<style scoped>section { font-size: 21px; }</style>

## Puntos clave (I)

- El PLN combina lingüística, estadística y aprendizaje profundo para que las máquinas comprendan
  y se comuniquen con el lenguaje humano.
- El potencial es alto y medible: SQuAD supera al humano, sentimiento al 95-97 %.
- La **ambigüedad** tiene seis formas y **no se elimina: se decide** con el contexto.
- El **POS *tagging*** desambigua categorías; el *tagset* es un compromiso información/dificultad.
- Sesgos, falta de comprensión, lenguas con pocos recursos e ironía son limitaciones reales.

---
<style scoped>section { font-size: 21px; }</style>

## Puntos clave (II)

- El **AI Act** es una herramienta de diseño: bajo riesgo (considerando 53) y prohibiciones
  (artículo 5).
- El **lingüista** diseña el *tagset* y anota; **las anotaciones deciden las predicciones**.
- La **cooperación** se evalúa: NLLB y Masakhane frente a la investigación paracaidista.
- **NLTK para aprender, spaCy para producir**; la herramienta se elige por los datos que hay.
- Construir un sistema son **seis pasos**, y el que más se salta es **mirar los errores**.

---
<style scoped>section { font-size: 25px; }</style>

## Cómo se evalúa

| Peso | Instrumento |
|---|---|
| **40 %** | Media de los **cinco entregables** (`EX1`, `EX2`, `EX2.5`, `EX3`, `EX4`) |
| **60 %** | Prueba del RA3: test y desarrollo sobre el contenido de la unidad |

`EX2` y `EX4` llevan una **parte escrita** que cubre RA3-b, RA3-e y RA3-f. **Cuenta.**

La normativa exige alcanzar todos los RA; el centro lo concreta en **≥ 5 en cada uno**.

---
<!-- _class: lead -->

## ¿Y ahora?

El lenguaje es la interfaz más natural entre personas y máquinas — y la más ambigua.

### A construir un sistema que la resuelva.
