# UD06 · Entregas

!!! important "Qué cuenta y qué es práctica"
    El RA6 se califica con **40 % de entregas + 60 % de prueba escrita**, y hay que superar el RA
    con **≥ 5**. Se entregan **tres cosas**: los dos debates y la auditoría de sesgos. El taller 1 y
    el notebook `N01` son **práctica**: se hacen en clase para preparar el debate y la auditoría, y
    para la prueba escrita, pero no se entregan ni puntúan.

    El **peso** de cada entrega está en el libro de calificaciones de Moodle, no aquí.

<!-- AUTO:notebooks inicio -->
| Notebook | Qué es | Descargar | Abrir en Colab |
|---|---|---|---|
| [`N03` · Auditoría de sesgos con Fairlearn](notebooks/UD06_N03_auditoria_sesgos.ipynb) | Auditoría con Fairlearn · medir, mitigar y ver el precio que se paga | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD06/notebooks/UD06_N03_auditoria_sesgos.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD06/notebooks/UD06_N03_auditoria_sesgos.ipynb){:target="_blank"} |
<!-- AUTO:notebooks fin -->

## Resumen de entregas y práctica

| # | Actividad | Cuándo | Qué se entrega | Cómo se corrige |
|---|---|---|---|---|
| 1 | [**Debate 1** · Límites éticos de la IA](UD06_D01_Debate_limites_eticos_ES.md) | Sesión 2 | Participación en el aula **+** reflexión escrita de máx. **300 palabras** en Moodle | Rúbrica de debate en Moodle, 100 puntos escalados sobre 10 |
| 2 | [**Debate 2** · El algoritmo contra el crimen](UD06_D02_Debate_algoritmo_crimen_ES.md) | Sesión 4 | Participación en el aula **+** reflexión escrita de máx. **300 palabras** en Moodle | La **misma** rúbrica |
| — | [**Notebook 2** · Análisis de un caso ético](notebooks/UD06_N02_analisis_caso_etico.ipynb) | Sesión 3 | **Práctica**: se trabaja en clase, no se entrega | Se corrige en clase |
| 3 | [**Notebook 3** · Auditoría de sesgos con Fairlearn](notebooks/UD06_N03_auditoria_sesgos.ipynb) | Sesión 3 | Informe con las métricas antes/después y las seis respuestas | Rúbrica propia, en la tarea de Moodle |
| — | [**Notebook N01** · Detección de sesgos](notebooks/UD06_N01_sesgos_ia.ipynb) | Sesión 3 | **Práctica**: da soporte a la auditoría, no se entrega | Se revisa en clase |
| — | [Tertulia de ciencia-ficción](#tertulia-de-ciencia-ficcion) | Libre | Voluntaria, de ampliación | Sin nota |

!!! warning "Los debates no se recuperan repitiéndolos"
    **70 de los 100 puntos** de la rúbrica se observan **en directo**: dominio del rol,
    argumentación, participación y empatía. Si faltas a la sesión, esa parte no se puede reproducir
    después. Los otros 30 son la reflexión escrita, que sí se entrega fuera de clase.

!!! info "La rúbrica está en Moodle"
    La rúbrica de los debates y la auditoría se ve **en la propia tarea de Moodle**, y puedes leerla **antes** de
    empezar: ahí tienes los criterios, los niveles y lo que puntúa cada uno. No se duplica aquí para
    que no haya dos versiones del mismo dato.

## Tertulia de ciencia-ficción

Actividad **voluntaria de ampliación**, sin nota. La ciencia-ficción lleva décadas planteando los
dilemas de esta unidad antes de que fueran técnicamente posibles, y sirve para llegar al debate con
ejemplos que todo el mundo reconoce.

Elige **una** obra, míralas o léela, y prepara tres minutos: qué dilema plantea, con qué apartado de
la teoría se corresponde y si lo que describe ya es posible hoy.

| Obra | Año | Temas | Apartado |
|---|---|---|---|
| **Black Mirror** (serie) | 2011– | Privacidad y datos personales («Nosedive», «The Entire History of You»); responsabilidad y rendición de cuentas («White Bear», «Hated in the Nation») | §5, §6.2 |
| **Westworld** (serie) | 2016-2022 | Autonomía y control humano; conciencia y moralidad de crear seres conscientes | §4.3, FAQ de derechos de los robots |
| **Person of Interest** (serie) | 2011-2016 | Vigilancia masiva y prevención de delitos; supervisión humana de un sistema autónomo | §5.5, §9.4 |
| **Years and Years** (serie) | 2019 | Vigilancia masiva y autoritarismo digital: reconocimiento facial y crédito social | §5.5, §6.1 (usos prohibidos) |
| **Cassandra** (serie) | 2025 | Un asistente doméstico con IA diseñado en los años 60: problemas de diseño y de convivencia cotidiana | §7.3, §7.4 |
| **Ex Machina** | 2014 | Transparencia y explicabilidad; sesgos y dinámicas de poder entre creador y criatura | §6.3, §9 |
| **Her** | 2013 | Privacidad en la interacción con una IA; responsabilidad emocional | §5, §9.6 |
| **Minority Report** | 2002 | Predicción del delito y precrimen; libertad frente a determinismo | **§9.4** |
| **The Matrix** | 1999 | Control y manipulación de la realidad; impacto social y económico | §4.5, §7.4 |
| **El hombre bicentenario** | 1999 | Derechos de las IA; identidad y autonomía | FAQ de derechos de los robots |
| **1984**, de George Orwell (novela) | 1949 | Vigilancia y control totalitario; manipulación de la información | §5.5 |

!!! tip "La pregunta que hace interesante la tertulia"
    No es «¿esto podría pasar?». Es **«¿qué parte de esto ya está pasando, y con qué nombre técnico
    lo llamamos en esta unidad?»**. *Minority Report* es puntuación de riesgo (§9.4). *Nosedive* es
    puntuación social, que el AI Act **prohíbe** (§6.1). *Years and Years* es reconocimiento facial
    masivo, también prohibido. La ficción envejeció; el temario, no.

## N03 · Auditoría de sesgos con Fairlearn

Medir el sesgo de un modelo real con **Fairlearn**, mitigarlo y **comprobar el precio que se paga**
por hacerlo (RA6-f, con conexión a RA6-b y RA6-e).

**Se entrega**: el informe con las métricas antes y después de mitigar, y las seis respuestas.
---
[Volver a la UD06](UD06_ES.md) · [Notebooks guiados](UD06_ActividadesGuiadas.md) ·
[Ejercicios](UD06_Ejercicios.md)
