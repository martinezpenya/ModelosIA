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
# UD02: Modelos de IA y resolución de problemas
#### Modelos de Inteligencia Artificial
###### version: 2026-08-24

---
<!-- footer: d.martinezpena@edu.gva.es -->
<!-- header: Modelos de Inteligencia Artificial 26-27 (UD02_1)-->
<style scoped>section { font-size: 28px; }</style>

# ¿Qué veremos?
1. Sistema de resolución de problemas y búsqueda
2. Clasificación de modelos de IA
3. Automatización de tareas
4. Razonamiento impreciso: lógica difusa
5. Sistemas basados en reglas
6. Adecuación del modelo, y Robocode como caso completo

---

## RA2 y sus criterios de evaluación

**RA2**: implementa sistemas de resolución de problemas con modelos de IA.

| CE | Criterio |
|---|---|
| a | Requisitos de un SRP |
| b, c | Clasificación de modelos de IA y automatización de tareas |
| d, e | Razonamiento impreciso y sistemas basados en reglas |
| f | Adecuación del modelo |

---

## Hilo conductor de la unidad

**Antes de programar IA hay que saber formalizar un problema y elegir bien el modelo.**

Modelar → clasificar → automatizar → razonar (difuso y por reglas) → decidir → implementar.

El cierre de la unidad, Robocode, recorre las seis fases con un bot de combate real.

---
<!-- _class: lead -->
# 1. Sistema de resolución de problemas (RA2-a)

---

## Cinco requisitos de un SRP

1. **Representación**: elegir estructura y modelo fieles al problema.
2. **Razonamiento y decisión**: lógica, aprendizaje o búsqueda heurística.
3. **Aprendizaje y adaptabilidad**: mejorar con la experiencia.
4. **Eficiencia computacional**: respuestas rápidas y escalables.
5. **Interacción con las personas usuarias**: interfaz comprensible.

---

## El espacio de estados

```mermaid
flowchart LR
    S0[Estado inicial] --> A1[Acción] --> S1[Estado 1] --> SOBJ[Estado objetivo]
    S0 --> A2[Acción] --> S2[Estado 2] --> SOBJ
```

Un problema bien planteado responde a: ¿estado inicial?, ¿acciones aplicables?, ¿modelo de transición?, ¿test de objetivo?, ¿coste de camino?

---

## Ejemplos clásicos de representación

| Problema | Representación | Detalle |
|---|---|---|
| Jarras 8-5-3 | `[jarra8, jarra5, jarra3]` | De `[8,0,0]` a `[4,4,0]` |
| Misioneros y caníbales | `⟨m,c,barca⟩` | De `⟨3,3,1⟩` a `⟨0,0,0⟩` |
| 8-reinas | Permutación de 1..8 | 40.320 arreglos, **92 soluciones** |
| 15-puzzle | Matriz 4×4 | ≈10,46·10¹² estados |

---

## La explosión combinatoria

El número de estados crece **exponencialmente** con el tamaño del problema (factor de ramificación `b` elevado a profundidad `d`).

Un espacio real (rutas de reparto, planificación) es enorme: hace falta una estrategia de búsqueda y, cuando se puede, una heurística.

---

## BFS, DFS y A*

| Criterio | BFS | DFS | A* |
|---|---|---|---|
| Estructura | Cola (FIFO) | Pila (LIFO) | Cola de prioridad `f=g+h` |
| Completa | Sí | No | Sí |
| Óptima | Sí (coste unitario) | No | Sí (heurística admisible) |
| Cuándo usar | Camino más corto en pasos | Exploración exhaustiva | Ruta óptima con costes variados |

---

## Heurística: A* en el 8-puzzle

`f(n) = g(n) + h(n)`: coste acumulado más una estimación de lo que falta.

Heurísticas admisibles habituales: número de fichas mal colocadas, o distancia de Manhattan.

**Regla práctica** (Red Blob Games): usa el algoritmo más simple que puedas — BFS si todos los costes son iguales, A* con la heurística más simple si buscas un único objetivo.

---
<!-- _class: lead -->
# 2. Clasificación de modelos de IA (RA2-b)

---

## Por paradigma de aprendizaje

| | Supervisado | No supervisado | Refuerzo |
|---|---|---|---|
| Datos | Etiquetados | Sin etiquetas | Recompensas |
| Objetivo | Predecir la salida | Descubrir patrones | Maximizar recompensa |
| Ejemplos | Spam, precio de coche | Segmentar clientes | AlphaGo, robots |

**Todo ML es IA, pero no toda IA es ML**: reglas y lógica difusa son IA sin aprender de datos.

---

## Por tipo de análisis y por base

| Análisis | Pregunta | Ejemplo |
|---|---|---|
| Descriptivo | ¿Qué pasó? | Informe de ventas |
| Predictivo | ¿Qué pasará? | Previsión de demanda |
| Prescriptivo | ¿Qué hacer? | Precio óptimo a fijar |

Basados en **conocimiento** (reglas explícitas, interpretable) frente a basados en **datos** (ML/DL, flexible pero caja negra).

---

## Mapa de los modelos de IA

```mermaid
flowchart TD
    IA[Modelos de IA] --> CONOC[Basados en conocimiento]
    IA --> DATOS[Basados en datos]
    CONOC --> REGLAS[Reglas]
    CONOC --> DIFUSA[Lógica difusa]
    DATOS --> ML[Machine Learning]
    DATOS --> DL[Deep Learning]
```

---
<!-- _class: lead -->
# 3. Automatización de tareas (RA2-c)

---

## RPA frente a IA

| | RPA | IA |
|---|---|---|
| Qué hace | **Hace**: replica tareas en la interfaz | **Piensa**: reconoce patrones y decide |
| Base | Reglas predefinidas | Datos y modelos |
| Se adapta | No | Sí, con la experiencia |

**RPA no es IA**: se complementan — la IA decide, el RPA ejecuta. IA + BPM + RPA = automatización inteligente.

---

## Agentes software y tareas cognitivas

De más simple a más avanzado: reflejo simple → reflejo con modelo → basado en objetivos → basado en utilidad → con aprendizaje.

Tareas cognitivas automatizables: **extracción** (OCR, NER), **clasificación** (spam, prioridades, reconocimiento de voz) y **generación** (IA generativa).

---
<!-- _class: lead -->
# 4. Razonamiento impreciso: lógica difusa (RA2-d)

---

## De lo booleano a lo difuso

La lógica clásica solo admite verdadero/falso. La **lógica difusa** (Zadeh, 1965) permite grados de verdad entre 0 y 1.

Modela la **vaguedad** del lenguaje humano — la probabilidad, en cambio, modela la incertidumbre.

Ejemplo: "18 ºC es frío con 0,7" en vez de "18 ºC es frío: sí/no".

---

## Funciones de pertenencia

| Función | Forma | Uso típico |
|---|---|---|
| Triangular | Pico en un punto | Variables simples |
| Trapezoidal | Meseta central | Intervalos |
| Gaussiana | Campana suave | Variables continuas |
| Sigmoidal | Escalón suave | Extremos |

Se recomiendan entre 3 y 7 curvas por variable, solapadas para que no existan huecos.

---

## El sistema de inferencia difuso (FIS)

```mermaid
flowchart LR
    A[Entradas crisp] --> B[Fuzzificación]
    B --> C[Reglas IF-THEN]
    C --> D[Agregación]
    D --> E[Defuzzificación]
    E --> F[Salida crisp]
```

Dos familias: **Mamdani** (salida difusa defuzzificada, la usa `scikit-fuzzy`) y **Sugeno/TSK** (salida funcional).

---

## Lógica difusa en el mundo real

Metro de Sendai (frenado y aceleración) · autofocus de Canon (13 reglas, 1,1 KB) · ABS de los frenos · lavadoras y aires acondicionados.

**Control de tráfico**: ajuste de semáforos según el flujo vehicular en tiempo real.

**Apoyo al diagnóstico médico**: valoración preliminar cuando los resultados de las pruebas no son concluyentes.

---

## Práctica: el problema de la propina

```python
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

regla1 = ctrl.Rule(calidad['mala'] | servicio['pobre'], propina['baja'])
sim.compute()
# Propina sugerida: ~20%
```

`scikit-fuzzy==0.5.0`: fija la versión, es una librería semi-mantenida.

---
<!-- _class: lead -->
# 5. Sistemas basados en reglas (RA2-e)

---

## El ciclo reconocer-actuar

```mermaid
flowchart LR
    A[Memoria de trabajo] --> B[Reconocer: match]
    B --> C[Agenda]
    C --> D[Resolver: salience]
    D --> E[Actuar]
    E -->|declara/retracta| A
```

Motores industriales usan el algoritmo **RETE** (Forgy, 1974) para no reevaluar todas las reglas.

---

## Encadenamiento, CLIPS y experta

**Hacia delante** (data-driven): parte de los hechos, deduce hechos nuevos — lo usan CLIPS y `experta`.

**Hacia atrás** (goal-driven): parte de una meta y pregunta solo lo necesario — propio del diagnóstico (MYCIN).

`experta`: librería Python inspirada en CLIPS, fork de `pyknow`, motor RETE con sintaxis nativa.

---

## Reglas en el día a día

**Sistemas de recomendación**: Amazon sugiere productos con reglas sobre el historial de compras.

**Soporte al diagnóstico médico**: reglas sobre síntomas dan una recomendación preliminar antes de la atención profesional.

Ventaja frente al ML: el razonamiento es **transparente y explicable**.

---

## Práctica con experta

```python
# PARCHE para Python 3.10+
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping
from experta import *

class DiagnosticoVehiculo(KnowledgeEngine):
    @Rule(Fact(bateria="descargada"), Fact(luces="no_encienden"))
    def bateria(self):
        self.declare(Fact(causa="bateria_descargada"))
```

---

## Sistemas expertos que cambiaron su sector

| Sistema | Origen | Dato relevante |
|---|---|---|
| MYCIN | Stanford, 1972 | 65-70 % de acierto |
| XCON/R1 | DEC, 1978 | ~25 M$/año de ahorro |
| SID | DEC, años 80 | 93 % de puertas del VAX 9000 |

**Reglas** si el dominio está acotado y hace falta explicabilidad; **ML** si hay datos y patrones complejos.

---
<!-- _class: lead -->
# 6. Adecuación del modelo (RA2-f)

---

## Cinco criterios para elegir modelo

**Datos** disponibles · **explicabilidad** exigida · **coste** de cómputo y mantenimiento · **precisión** requerida · **tiempo real** o latencia admisible.

**La regla de oro**: empieza simple. Reglas o heurística → árbol/regresión → ensamble → deep learning, solo si hace falta.

El teorema **No Free Lunch** (Wolpert y Macready, 1997): ningún algoritmo es mejor en promedio sobre todos los problemas.

---
<!-- _class: lead -->
# Caso de estudio: Robocode

---

## Robocode como sistema de resolución de problemas

**Representación**: el estado del bot y del campo de batalla en variables legibles cada turno. **Razonamiento**: reglas fijas, lógica difusa o una combinación para decidir disparo y movimiento.

**Eficiencia**: decisión en tiempo real, turno a turno. **Adecuación (CE f)**: sin datos previos, el punto de partida es la regla o heurística, no el ML.

---

## Puntos clave de la unidad

Un SRP se formaliza con estado inicial, acciones, transición, objetivo y coste; BFS/DFS/A* recorren el espacio de estados con garantías distintas. Los modelos se clasifican por aprendizaje, análisis y base (conocimiento/datos).

RPA hace, la IA piensa; la difusa modela vaguedad, las reglas ejecutan reconocer-actuar. Elegir modelo (CE f): datos, explicabilidad, coste, precisión, tiempo real — empieza simple.

---

## La unidad en la práctica

**5 talleres**: control difuso (`scikit-fuzzy`) · sistema de reglas (`experta`) · preparar el entorno · GitHub · Markdown.

**Actividad entregable**: Robocode Tank Royale, del 23 de noviembre al 3 de diciembre.

---

## Evaluación

| Peso | Instrumento |
|---|---|
| 40 % | Talleres + Robocode |
| 60 % | Prueba escrita del RA2 |

Hace falta un **5 o más** en el RA para superarlo.

---
<!-- _class: lead -->
# ¿Preguntas?

Diapositivas, apuntes y talleres en el sitio del módulo.
