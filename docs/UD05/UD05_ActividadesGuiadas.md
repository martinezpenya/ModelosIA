# UD05 · Notebooks guiados

!!! info "Se trabajan en clase: es práctica, no se entrega"
    **Ocho** notebooks de introducción y práctica guiada, en dominios distintos (§6.1 de la teoría),
    ordenados de menor a mayor dificultad y dependencia: los cuatro primeros son reglas, los tres
    siguientes lógica difusa y el último, control.
    **No se entregan ni puntúan**: preparan las [entregas de la unidad](UD05_Entregas.md)
    y la prueba escrita del RA5.
!!! tip "Si Google Colab da un error de versión"
    Los notebooks `N05`, `N06` y `N07` necesitan una versión concreta del entorno de ejecución de Colab
    ([Editar] → [Configuración del cuaderno] → **2025.7** en vez de «Última (recomendada)»), o
    puedes usar el `docker-compose.yml` de la unidad para ejecutarlos en local.

<!-- AUTO:notebooks inicio -->
| Notebook | Qué es | Descargar | Abrir en Colab |
|---|---|---|---|
| [`N01` · Sistema experto con Python y Experta](notebooks/UD05_N01_experta_primeros_pasos.ipynb) | Introducción a `experta` · hechos, reglas y `DefFacts` | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N01_experta_primeros_pasos.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N01_experta_primeros_pasos.ipynb){:target="_blank"} |
| [`N02` · Piedra, papel o tijera](notebooks/UD05_N02_piedra_papel_tijera.ipynb) | Juego decidido por reglas | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N02_piedra_papel_tijera.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N02_piedra_papel_tijera.ipynb){:target="_blank"} |
| [`N03` · Clasificación de animales](notebooks/UD05_N03_clasificacion_animales.ipynb) | Zoología · encadenamiento hacia delante | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N03_clasificacion_animales.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N03_clasificacion_animales.ipynb){:target="_blank"} |
| [`N04` · Reglas sobre datos: el Titanic](notebooks/UD05_N04_reglas_desde_datos_titanic.ipynb) | Reglas **extraídas** de datos, no escritas a mano (§7) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N04_reglas_desde_datos_titanic.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N04_reglas_desde_datos_titanic.ipynb){:target="_blank"} |
| [`N05` · Lógica difusa: el problema de las propinas](notebooks/UD05_N05_logica_difusa_propinas.ipynb) | Introducción a `scikit-fuzzy` · el caso canónico (§8.4) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N05_logica_difusa_propinas.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N05_logica_difusa_propinas.ipynb){:target="_blank"} |
| [`N06` · Lógica difusa: ¿quién jugará?](notebooks/UD05_N06_logica_difusa_quien_jugara.ipynb) | Deporte · cuántos minutos jugará un futbolista (§8) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N06_logica_difusa_quien_jugara.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N06_logica_difusa_quien_jugara.ipynb){:target="_blank"} |
| [`N07` · Control difuso: regar el césped](notebooks/UD05_N07_control_difuso_riego.ipynb) | Control difuso · regar el césped (§8, §10) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N07_control_difuso_riego.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N07_control_difuso_riego.ipynb){:target="_blank"} |
| [`N08` · Sistema experto como controlador de un proceso](notebooks/UD05_N08_controlador_experto.ipynb) | Control de una sala con `experta` (§10-11) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N08_controlador_experto.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N08_controlador_experto.ipynb){:target="_blank"} |
| [`N09` · Referencia: tasación de vehículos (original en CLIPS)](notebooks/UD05_N09_referencia_tasacion_vehiculos.ipynb) | Referencia resuelta · un sistema experto grande, original en CLIPS | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N09_referencia_tasacion_vehiculos.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N09_referencia_tasacion_vehiculos.ipynb){:target="_blank"} |
<!-- AUTO:notebooks fin -->

## Referencia: un sistema experto grande, resuelto

[`N09` · Tasación de vehículos usados](notebooks/UD05_N09_referencia_tasacion_vehiculos.ipynb)
([descargar](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N09_referencia_tasacion_vehiculos.ipynb){:target="_blank"} ·
[Colab](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N09_referencia_tasacion_vehiculos.ipynb){:target="_blank"})
es un ejemplo **extenso ya resuelto**, portado de una práctica original en CLIPS: no es un
enunciado que tengas que entregar: es una referencia para ver cómo se estructura un sistema
experto grande de principio a fin, con más reglas y más profundidad que los ejemplos guiados de
arriba.

---
[Volver a la UD05](UD05_ES.md) · [Ejercicios](UD05_Ejercicios.md) · [Notebook 10](notebooks/UD05_N10_simular_sistema_experto.ipynb) · [Notebook 5](notebooks/UD05_N05_logica_difusa_propinas.ipynb) · [Notebook 8](notebooks/UD05_N08_controlador_experto.ipynb) ·
[Entregas](UD05_Entregas.md)
