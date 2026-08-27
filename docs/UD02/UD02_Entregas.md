# UD02 · Entregas

<!-- AUTO:notebooks inicio -->
!!! important "6 entregas en el RA2"
    Cada una se corrige con **su rúbrica**, que puedes leer antes de empezar en la propia
    tarea de Moodle. El **peso** de cada entrega está en el libro de calificaciones de
    Moodle, no aquí. Los [ejercicios de autoevaluación](UD02_Ejercicios.md) son práctica
    y no se entregan.

    **Robocode (`T04`) pesa mucho más que las otras dos**: son dos semanas con bot y memoria, mientras
    que `N01` y `N02` son cortos y sus técnicas se vuelven a evaluar en el RA5. Los talleres `T01`-`T03`
    se entregan como **hecho / no hecho**: son requisito, pero no puntúan.

| Notebook | Qué es | Descargar | Abrir en Colab |
|---|---|---|---|
| [`N01` · Control difuso con scikit-fuzzy](notebooks/UD02_N01_control_difuso.ipynb) | Control difuso Mamdani · la velocidad de un ventilador (§7) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD02/notebooks/UD02_N01_control_difuso.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD02/notebooks/UD02_N01_control_difuso.ipynb){:target="_blank"} |
| [`N02` · Sistema basado en reglas con experta](notebooks/UD02_N02_sistema_reglas.ipynb) | Sistema experto con `experta` · diagnóstico de un PC (§8) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD02/notebooks/UD02_N02_sistema_reglas.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD02/notebooks/UD02_N02_sistema_reglas.ipynb){:target="_blank"} |

## `N01` · Control difuso con scikit-fuzzy

Construir un sistema de control difuso tipo Mamdani que decida la **velocidad de un ventilador** según la temperatura y la humedad de una sala, recorriendo las tres fases del razonamiento impreciso.

**Se entrega**: el notebook con el controlador funcionando y las figuras de las funciones de pertenencia.

## `N02` · Sistema basado en reglas con experta

Implementar un **mini sistema experto de diagnóstico** de un PC que no arranca y comprobar en código el ciclo reconocer-actuar de un sistema basado en reglas (RA2-e).

**Se entrega**: el notebook con el sistema resolviendo los casos de prueba.
<!-- AUTO:notebooks fin -->

---
[Volver a la UD02](UD02_ES.md) · [Ejercicios de autoevaluación](UD02_Ejercicios.md)
