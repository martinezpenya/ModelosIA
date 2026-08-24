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
# UD01: Caracterización de sistemas de IA
#### Modelos de Inteligencia Artificial
###### version: 2026-08-24

---
<!-- footer: d.martinezpena@edu.gva.es -->
<!-- header: Modelos de Inteligencia Artificial 26-27 (UD01_1)-->
<style scoped>section { font-size: 28px; }</style>

# ¿Qué veremos?
1. Fundamentos de los sistemas inteligentes
2. Escuelas de pensamiento y clasificaciones de la IA
3. IA, machine learning, deep learning e IA generativa
4. Campos de aplicación
5. Nuevas formas de interacción y eficiencia operativa
6. Beneficios, riesgos y ética

---

## RA1 y sus criterios de evaluación

**RA1**: caracteriza sistemas de IA y su relación con la mejora de la eficiencia operativa.

| CE | Criterio |
|---|---|
| a | Principios de los sistemas inteligentes |
| b | Campos de aplicación de la IA |
| c | Técnicas básicas de la IA |
| d | Nuevas formas de interacción y mejora operativa |

---

## Hilo conductor de la unidad

**Antes de programar nada hace falta saber qué es un sistema inteligente, cómo se clasifica y qué mejora aporta.**

Fundamentos → clasificar → distinguir técnicas → identificar campos → conectar con la mejora operativa.

El taller 3 cierra la unidad calculando esa mejora con KPIs sobre un caso de negocio.

---
<!-- _class: lead -->
# 1. Fundamentos de los sistemas inteligentes (RA1-a)

---

## ¿Qué es la inteligencia artificial?

La **IA** permite a las máquinas **simular** aprendizaje, comprensión, resolución de problemas, decisión y creatividad humanas.

Ve e identifica objetos, entiende y responde al lenguaje, aprende de la experiencia y puede **actuar de forma autónoma** (un coche autónomo).

---

## El ciclo percepción → razonamiento → acción

```mermaid
flowchart LR
    A[Percepcion] --> B[Razonamiento]
    B --> C[Accion]
    C -. retroalimentacion .-> A
```

**Percepción**: datos, sensores, texto, imagen, audio. **Razonamiento**: modelo, reglas o búsqueda. **Acción**: respuesta, decisión, control.

---

## Características de un sistema inteligente

| Característica | Descripción |
|---|---|
| **Autonomía** | Opera sin supervisión humana constante |
| **Adaptación** | Aprende de los datos y mejora con la experiencia |
| **Toma de decisiones** | Recomienda o actúa a partir de datos, no solo de reglas fijas |

Un termostato con reglas `si...entonces...` ya es, formalmente, IA basada en reglas.

---

## IA débil frente a IA fuerte

**Débil (narrow)**: una tarea concreta, reactiva, no flexible, sin conciencia. **Es toda la IA que existe hoy** (Siri, Alexa).

**Fuerte (AGI)**: igualaría a una persona en cualquier tarea, sería proactiva y flexible. **Es puramente teórica**: ningún sistema actual se aproxima.

La IA débil también tiene riesgos: ejecuta su tarea sin evaluar consecuencias como lo haría una persona.

---
<!-- _class: lead -->
# 2. Escuelas y clasificaciones de la IA (RA1-a)

---

## Dos escuelas: convencional y computacional

| | Convencional | Computacional |
|---|---|---|
| Cómo razona | Análisis formal explícito | Aprendizaje a partir de datos |
| Técnicas | Reglas, sistemas expertos | Redes neuronales, difusa |
| Originó | La automatización clásica | El machine learning actual |

---

## Russell y Norvig (1995): cuatro categorías

| Categoría | Enfoque |
|---|---|
| **Sistemas cognitivos** | Piensan como humanos |
| **Test de Turing** | Actúan como humanos |
| **Leyes del pensamiento** | Piensan con lógica formal |
| **Agentes racionales** | Actúan racionalmente |

De *Artificial Intelligence: A Modern Approach*, el libro de texto de IA más usado.

---

## Hintze (2016): clasificación por capacidades

```mermaid
flowchart LR
    A[Reactivas] --> B[Memoria limitada]
    B --> C[Teoria de la mente]
    C --> D[Autoconciencia]
```

**Reactivas**: Deep Blue, sin memoria. **Memoria limitada**: coches autónomos. **Teoría de la mente** y **autoconciencia**: aún teóricas, ningún sistema actual llega ahí.

---

## Breve historia de la IA

**1950** Test de Turing · **1956** Dartmouth acuña «inteligencia artificial» · **1958** perceptrón de Rosenblatt · **1997** Deep Blue vence a Kasparov · **2016** AlphaGo gana en Go.

**2017**: *Attention Is All You Need* propone el **Transformer** — la base técnica de los LLM y la IA generativa. **2022**: los LLM cambian la industria.

---
<!-- _class: lead -->
# 3. IA, ML, DL e IA generativa (RA1-c)

---

## Cajas anidadas

```mermaid
flowchart TD
    IA[Inteligencia Artificial] --> ML[Machine Learning]
    ML --> DL[Deep Learning]
    DL --> GEN[IA generativa]
```

**Todo ML es IA, pero no toda IA es ML.** Todo DL es ML, y la IA generativa es una parte del DL.

---

## Cómo funciona un modelo de ML

1. **Representar** los datos como vectores de *features*.
2. **Entrenar**: ajustar parámetros para minimizar el error.
3. **Evaluar** con datos no vistos (evita el sobreajuste).
4. **Inferir**: predecir sobre datos nuevos en producción.

`Precio = A·superficie + B·habitaciones − C·edad + base`: el ML busca los valores de A, B, C.

---

## Tipos de aprendizaje

| Tipo | Datos | Ejemplos |
|---|---|---|
| **Supervisado** | Etiquetados | Spam, precio de vivienda |
| **No supervisado** | Sin etiquetas | Segmentar clientes |
| **Refuerzo** | Recompensas | Robots, juegos |
| **Semi / auto-supervisado** | Pocas o ninguna etiqueta | Entrenar LLM |

---

## Deep learning e IA generativa

**DL**: redes con muchas capas, backpropagation, necesita datos y GPU. **CNN** (imágenes), **RNN/LSTM** (secuencias), **Transformers** (atención, base de los LLM).

**IA generativa**: modelo de base entrenado con datos masivos → ajuste (*fine-tuning*, RLHF) → generación, a veces con **RAG**. Los **agentes de IA** van un paso más allá: actúan, no solo responden.

---
<!-- _class: lead -->
# 4. Campos de aplicación (RA1-b)

---

## Campos de aplicación de la IA

| Campo | Ejemplo | Beneficio |
|---|---|---|
| Industria | Mantenimiento predictivo | Menos paradas |
| Salud | Diagnóstico por imagen | Mayor precisión |
| Finanzas | Fraude, scoring | Menos pérdidas |
| Comercio, educación, RRHH | Recomendación, tutoría, cribado de CV | Más ventas, menos tiempo |

---

## Casos de estudio con beneficio medible

**Fraude en banca**: modelo de ML sobre datos etiquetados → alerta inmediata en vez de revisión manual posterior.

**Mantenimiento predictivo**: sensores predicen el fallo antes de que ocurra → sustitución programada, menos paradas.

**Atención al cliente con PLN**: chatbot 24/7 para consultas frecuentes, deriva las complejas a personas.

---
<!-- _class: lead -->
# 5. Nuevas interacciones y eficiencia operativa (RA1-d)

---

## Nuevas formas de interacción

| Interacción | Ejemplo |
|---|---|
| **Asistente virtual** | Siri, Alexa |
| **Chatbot** | Soporte de tienda online |
| **Voz / visión** | Transcripción, lectura de documentos |
| **Agentes autónomos** | Reservar un vuelo |

Detrás del texto y la voz hay tareas de **PLN** — se estudian en la UD03.

---

## Eficiencia operativa y KPIs

La IA mejora la eficiencia cuando reduce **costes, tiempos o errores**. Se mide comparando **antes/después** con indicadores: tiempo de ciclo, coste unitario, tasa de error, disponibilidad.

KPIs por ámbito: **FCR** y **AHT** (atención al cliente), **OEE** y **MTBF** (industria).

---

## Ejemplo resuelto: un centro de atención

1.000 consultas/día, 3 €/5 min cada una. Un chatbot resuelve el 60 % en 10 s a 0,10 €.

Coste antes: 1.000 × 3 € = **3.000 €**. Coste después: 600 × 0,10 € + 400 × 3 € = **1.260 €**.

**Reducción de coste ≈ 58 %**, y el tiempo medio baja de 5 a ~2 minutos.

---
<!-- _class: lead -->
# 6. Beneficios, riesgos y ética

---

## Una visión general (se profundiza en la UD06)

**Beneficios**: automatización de tareas repetitivas, mejor toma de decisiones, disponibilidad 24×7, menos errores humanos.

**Riesgos**: datos con sesgos, modelos alterados, *model drift*, privacidad.

**Marco normativo**: el **AI Act** clasifica la IA por riesgo (prácticas prohibidas desde 2/2025); el **RGPD** limita el uso de datos personales.

---

## Puntos clave de la unidad

Un sistema inteligente **percibe, razona y actúa**; se clasifica por tarea (débil/fuerte), por escuela (convencional/computacional) y por capacidades (Russell-Norvig, Hintze).

**IA > ML > DL > IA generativa**: todo ML es IA, pero no toda IA es ML.

Las nuevas interacciones (chatbots, voz, visión, agentes) mejoran la eficiencia operativa reduciendo coste, tiempo o error — y eso se mide con KPIs.

---

## La unidad en la práctica

**4 talleres**: mapa de sistemas inteligentes · técnicas en casos reales · nuevas interacciones · línea del tiempo de la IA.

**Actividad guiada**: notebook demo de aprendizaje supervisado, no supervisado y medición de la mejora operativa.

---

## Evaluación

| Peso | Instrumento |
|---|---|
| 40 % | Media de los 4 talleres |
| 60 % | Prueba escrita del RA1 |

Hace falta un **5 o más** en el RA para superarlo.

---
<!-- _class: lead -->
# ¿Preguntas?

Diapositivas, apuntes y talleres en el sitio del módulo.
