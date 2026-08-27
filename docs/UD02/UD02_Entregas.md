# UD02 · Entregas

!!! important "Seis entregas, tres con rúbrica y tres de requisito"
    En esta unidad se entregan seis cosas, pero **no todas cuentan igual**. Las tres primeras se
    corrigen con su rúbrica; las tres de entorno se marcan **hecho / no hecho**: hay que hacerlas,
    pero no llevan nota.
### Lo que no es un notebook

| # | Actividad | Qué se entrega | Cómo se corrige |
|---|---|---|---|
| `T01` | [Preparar el entorno para Robocode](UD02_T01_Preparar_entorno_ES.md) | Capturas del entorno funcionando | Hecho / no hecho |
| `T02` | [Control de versiones con GitHub](UD02_T02_GitHub_ES.md) | El repositorio creado | Hecho / no hecho |
| `T03` | [Documentar con Markdown](UD02_T03_Markdown_ES.md) | El documento en Markdown | Hecho / no hecho |
| `T04` | [**Robocode Tank Royale**](UD02_T04_Robocode_ES.md) | El código del bot y su memoria | Rúbrica, en la tarea de Moodle |

!!! tip "Robocode es la entrega grande de la unidad"
    Es la práctica de cierre del RA2 y **pesa mucho más que las otras dos evaluables**: son dos
    semanas de trabajo con bot y memoria, mientras que `N01` y `N02` son talleres cortos cuyas
    técnicas se vuelven a evaluar en el RA5. El peso exacto está en el libro de calificaciones de
    Moodle.

!!! info "Lo demás de esta unidad es práctica"
    Los [ejercicios de autoevaluación](UD02_Ejercicios.md) **no se entregan**. Y la
    [comparativa Java vs Python](UD02_Robocode_Comparativa_ES.md) —que es por donde se empieza, para
    elegir lenguaje— y los tutoriales de [Java](UD02_Robocode_Java_ES.md) y
    [Python](UD02_Robocode_Python_ES.md) son documentación de apoyo para Robocode, no entregas.

<!-- AUTO:notebooks inicio -->
| Notebook | Qué es | Descargar | Abrir en Colab |
|---|---|---|---|
| [`N01` · Control difuso con scikit-fuzzy](notebooks/UD02_N01_control_difuso.ipynb) | Control difuso Mamdani · la velocidad de un ventilador (§7) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD02/notebooks/UD02_N01_control_difuso.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD02/notebooks/UD02_N01_control_difuso.ipynb){:target="_blank"} |
| [`N02` · Sistema basado en reglas con experta](notebooks/UD02_N02_sistema_reglas.ipynb) | Sistema experto con `experta` · diagnóstico de un PC (§8) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD02/notebooks/UD02_N02_sistema_reglas.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD02/notebooks/UD02_N02_sistema_reglas.ipynb){:target="_blank"} |
<!-- AUTO:notebooks fin -->

## N01 · Control difuso con scikit-fuzzy

Construir un sistema de control difuso tipo Mamdani que decida la **velocidad de un ventilador**
según la temperatura y la humedad de una sala, recorriendo las tres fases del razonamiento
impreciso.

**Se entrega**: el notebook con el controlador funcionando y las figuras de las funciones de pertenencia.

## N02 · Sistema basado en reglas con `experta`

Implementar un **mini sistema experto de diagnóstico** de un PC que no arranca y comprobar en
código el ciclo reconocer-actuar de un sistema basado en reglas (RA2-e).

**Se entrega**: el notebook con el sistema resolviendo los casos de prueba.
---
[Volver a la UD02](UD02_ES.md) · [Ejercicios de autoevaluación](UD02_Ejercicios.md)
