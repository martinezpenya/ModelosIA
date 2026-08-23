# UD05 · Actividades entregables

!!! important "Cinco entregables, promediados, 40 % de la nota de RA5"
    Los cinco cuentan para la nota (decisión del profesor, 2026-08-22): se promedian sobre 10.
    Cuatro tienen dominio fijo (`EX1`-`EX4`); `EX0` es de libre elección.

| Notebook | Dominio | Descargar | Ejecutar |
|---|---|---|---|
| [EX0 · Sistema experto de libre elección](notebooks/EX0.-PracticaExperta.ipynb) | El que tú elijas | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/EX0.-PracticaExperta.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/EX0.-PracticaExperta.ipynb){:target="_blank"} |
| [EX1 · Sistema experto: detectar lesiones de rodilla](notebooks/EX1.-genoll_ES.ipynb) | Medicina | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/EX1.-genoll_ES.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/EX1.-genoll_ES.ipynb){:target="_blank"} |
| [EX2 · Sistema basado en reglas: previsión del valor de mercado](notebooks/EX2.-preveure_valor_mercat_ES.ipynb) | Deporte · sistema híbrido (§7) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/EX2.-preveure_valor_mercat_ES.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/EX2.-preveure_valor_mercat_ES.ipynb){:target="_blank"} |
| CSV de jugadores del FIFA 22 (para `EX2` y `EX3`) | — | [![CSV](https://img.shields.io/badge/CSV-players__22.csv-blue?logo=pandas)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/EX2.-players_22.csv){:target="_blank"} | — |
| [EX3 · Lógica difusa: centrocampistas con potencial](notebooks/EX3.-detectar_centrocampistes_joves_ES.ipynb) | Deporte · lógica difusa (§8) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/EX3.-detectar_centrocampistes_joves_ES.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/EX3.-detectar_centrocampistes_joves_ES.ipynb){:target="_blank"} |
| [EX4 · Sistema de control: simulador de quemador de gas](notebooks/EX4.-cremador_ES.ipynb) | Industria · control real (§10-11) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/EX4.-cremador_ES.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/EX4.-cremador_ES.ipynb){:target="_blank"} |

!!! note "`EX2` y `EX3` comparten el mismo fichero de datos"
    Descarga `EX2.-players_22.csv` una vez y súbelo a la carpeta de archivos de Colab (o colócalo
    junto al notebook si trabajas en local) antes de ejecutar cualquiera de los dos.

## Rúbricas

Las cinco rúbricas son las mismas que ya se usaban en Moodle. Cada una puntúa sobre el máximo de su
tabla, y esa suma se escala a la nota final de la tarea sobre 10.

### EX0 · Sistema experto de libre elección

| Criterio | Mínimo (0) | Niveles intermedios | Máximo |
|---|---|---|---|
| Variabilidad de las reglas | No entregado | No ha usado reglas (2) · fuera de plazo (2,5) · todas iguales (3) · dos tipos (4) | Tres o más tipos de reglas (5) |
| Memoria | No entregada | Insuficiente (2) · fuera de plazo (2,5) · suficiente (3) · bien (4) | Muy bien (5) |
| Hechos iniciales (`@DefFacts`) | No entregado | Ninguno (2) · fuera de plazo (2,5) · uno (3) · dos (4) | Tres o más (5) |
| Reglas (`@Rule`) | No entregado | Ninguna (2) · fuera de plazo (2,5) · una (3) · dos (4) | Tres o más (5) |
| Originalidad | No entregado | Nada original (2) · fuera de plazo (2,5) · poco original (3) · original (4) | Muy original (5) |
| Funciones extra (preguntas, respuestas, matemáticas…) | No entregado | Ninguna (2) · fuera de plazo (2,5) · una (3) · dos (4) | Tres o más (5) |

### EX1 · Detectar lesiones de rodilla

| Criterio | Mínimo (0) | Niveles intermedios | Máximo |
|---|---|---|---|
| Regla de diagnóstico | No entregada | No la ha definido, pero muestra algo (1) | Correctamente definida (2) |
| Método para añadir hechos | No entregado o con `declare` | — | Definido correctamente (1) |
| Pruebas | No entregado | Fallan algunas celdas (1) | Todas las celdas de prueba funcionan (2) |
| Reglas (`@Rule`) | No entregado | Sin reglas (1) · casi todas (8) | Todas las reglas correctamente definidas (10) |

### EX2 · Previsión del valor de mercado

| Criterio | Mínimo (0) | Niveles intermedios | Máximo |
|---|---|---|---|
| `FunctionClassifier` de Human-Learn (`score`) | No entregado | Muy mal (1) · mal (2) · fuera de plazo (2,5) · neutral (3) · bien (4) | Muy bien (5) |
| `FIGSClassifier` (`fit`, predicción, `score`) | No entregado | Muy mal (1) · mal (2) · fuera de plazo (2,5) · neutral (3) · bien (4) | Muy bien (5) |
| `FIGS` sin campos evidentes | No entregado | Muy mal (1) · mal (2) · fuera de plazo (2,5) · neutral (3) · bien (4) | Muy bien (5) |

### EX3 · Centrocampistas con potencial

| Criterio | Mínimo (0) | Niveles intermedios | Máximo |
|---|---|---|---|
| Antecedentes y consecuentes | No entregado | Muy mal (1) · mal (2) · fuera de plazo (2,5) · neutral (3) · bien (4) | Muy bien (5) |
| Funciones de pertenencia (×3) | No entregado | Muy mal (1) · mal (2) · fuera de plazo (2,5) · neutral (3) · bien (4) | Muy bien (5) |
| Reglas + `ControlSystem` + `view` | No entregado | Muy mal (1) · mal (2) · fuera de plazo (2,5) · neutral (3) · bien (4) | Muy bien (5) |
| Pruebas del potencial (×4) | No entregado | Muy mal (1) · mal (2) · fuera de plazo (2,5) · neutral (3) · bien (4) | Muy bien (5) |
| Columna de potencial en el `DataFrame` | No entregado | Muy mal (1) · mal (2) · fuera de plazo (2,5) · neutral (3) · bien (4) | Muy bien (5) |
| Conclusiones | No entregado | Muy mal (1) · mal (2) · fuera de plazo (2,5) · neutral (3) · bien (4) | Muy bien (5) |

### EX4 · Simulador de quemador de gas

!!! important "Pide dos enfoques, no uno"
    Esta rúbrica evalúa **dos soluciones distintas** para el mismo quemador: un controlador
    simple y un enfoque alternativo. No es un error del enunciado entregar dos veces «lo mismo»
    con matices: es lo que se pide.

| Criterio | Mínimo (0) | Niveles intermedios | Máximo |
|---|---|---|---|
| Controlador simple | No entregado | Muy mal (1) · mal (2) · neutral (3) · bien (4) | Muy bien (5) |
| Antecedentes, consecuente y conjuntos difusos | No entregado | Muy mal (1) · mal (2) · neutral (3) · bien (4) | Muy bien (5) |
| 4 reglas, controlador y `view` | No entregado | Muy mal (1) · mal (2) · neutral (3) · bien (4) | Muy bien (5) |
| Enfoque alternativo: antecedentes, consecuente, conjuntos difusos | No entregado | Muy mal (1) · mal (2) · neutral (3) · bien (4) | Muy bien (5) |
| 3 reglas, controlador y `view` (del enfoque alternativo) | No entregado | Muy mal (1) · mal (2) · neutral (3) · bien (4) | Muy bien (5) |

---
[Volver a la UD05](UD05_ES.md) · [Ejercicios](UD05_Ejercicios.md) · [Talleres](UD05_Talleres.md) ·
[Actividades guiadas](UD05_ActividadesGuiadas.md)
