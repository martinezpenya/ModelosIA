# UD06 · Taller 1 — Análisis de un caso ético

!!! important "Práctica: no se entrega"
    Este taller es **práctica**: se trabaja en clase y **no se entrega ni puntúa**. Sirve para
    preparar las entregas de la unidad y la prueba escrita del RA.

**Objetivo**: aplicar un método de análisis ético reproducible a un caso real de sesgo o riesgo de la
IA (RA6-a, RA6-c, RA6-f), argumentando con principios deontológicos, métricas y normativa.

**Resultado**: un informe con las cinco tablas rellenas y las respuestas de la Fase 6. No se
entrega: es la preparación del debate y de la auditoría de sesgos, que sí se entregan.

!!! tip "Hazlo en el notebook"
    Tienes este taller como **notebook con las celdas a rellenar**:
    [`UD06_T01_analisis_caso_etico.ipynb`](notebooks/UD06_T01_analisis_caso_etico.ipynb). Esta página es la referencia; el trabajo se
    hace sobre el notebook.

### Fase 1 — Elige el caso

Elige uno de estos casos (o propón otro y valídalo con el profesor):

| Caso | Dato de partida | Dónde está en la teoría |
|---|---|---|
| **COMPAS** (reincidencia penal) | Falsos positivos: **44,9 %** en personas negras frente al **23,5 %** en blancas, con la misma calibración | §9.4 |
| **Obermeyer** (gestión sanitaria) | El proxy «coste» en vez de «necesidad»: corregirlo pasaría del **17,7 % al 46,5 %** de pacientes negros derivados | §9.5 |
| **Amazon 2018** (reclutamiento) | Penalizaba currículos con términos asociados a mujeres | §4.1 |
| **Google Photos 2015** (visión) | Etiquetó a personas negras como gorilas; «arreglado» borrando la etiqueta | §4.1 |
| **Uber en Tempe 2018** (conducción autónoma) | 69 km/h · detección 6 s antes · **4,7 s sin actuar** | §4.1 |
| **Deepfake CFO** (Hong Kong, 2024) | Fraude de **25,6 M USD** con una videollamada falsa | §4.1 |
| **Ofqual 2020** (notas de acceso, Reino Unido) | Un algoritmo bajó el **36 %** de las notas propuestas por los centros | — |
| Una noticia de [actualidad](UD06_ActividadesGuiadas.md) | La que elijas | — |

### Fase 2 — Hechos y partes afectadas

| Elemento | Descripción |
|---|---|
| ¿Qué ocurrió? (hechos, con fechas) | |
| ¿Quiénes son las partes afectadas? | |
| ¿Quién decidió desplegar el sistema y con qué finalidad declarada? | |
| ¿Qué datos usaba el sistema? | |
| ¿Qué decisión tomaba el sistema y qué efecto tenía sobre una persona? | |
| ¿Había intervención humana significativa? | |

### Fase 3 — Principios en conflicto

Identifica al menos **dos principios éticos en conflicto** —eficiencia frente a no discriminación,
precisión frente a equidad, autonomía frente a supervisión humana, seguridad frente a privacidad— y
apóyalos en los marcos del §4.3 (ACM, IEEE EAD, UNESCO, Directrices de la UE).

| Principio | ¿Quién lo defiende en tu caso? | ¿A qué se opone? | Marco que lo respalda |
|---|---|---|---|
| | | | |
| | | | |

!!! tip "Cómo no quedarse en la superficie"
    No basta con decir «se vulneró la equidad». Di **qué definición de equidad** de las seis del §9.2
    se vulneró, porque en la mayoría de los casos reales **se cumplía otra**. Ese es el nivel de
    análisis que se pide.

### Fase 4 — Análisis técnico

Para tu caso, responde:

1. ¿Qué **fuente de sesgo o de riesgo** está presente? (datos históricos, subrepresentación, variable
   proxy, objetivo que minimiza el error agregado, el propio proceso de desarrollo, opacidad,
   manipulación…)
2. ¿Qué **métrica de equidad** se vería afectada: paridad demográfica, igualdad de oportunidades o
   calibración? ¿Alguna **se cumplía**?
3. ¿Hay **paradoja de Simpson** en juego? Es decir, ¿podría la métrica global decir algo distinto de
   las métricas por subgrupo?
4. Si el sistema fuera tuyo, ¿qué **modo de fallo** habría detectado un FMEA (§7.3) antes de
   desplegarlo?

### Fase 5 — Normativa aplicable

| Norma | ¿Aplica? | ¿Por qué? |
|---|---|---|
| RGPD art. 5 (principios: minimización, limitación de la finalidad) | | |
| RGPD art. 22 (decisiones automatizadas) | | |
| RGPD art. 25 (*privacy by design*) y art. 35 (EIPD) | | |
| LOPDGDD (derechos digitales concretos) | | |
| AI Act: nivel de riesgo y obligaciones asociadas | | |
| AI Act art. 50 (transparencia) | | |
| Ley 15/2022 (igualdad de trato; inversión de la carga de la prueba) | | |
| Directiva 2024/2853 (responsabilidad del producto) | | |

!!! warning "Cuidado con la fecha"
    Varios de estos casos son **anteriores** al AI Act, que se aplica con carácter general desde el
    **2 de agosto de 2026**. La pregunta interesante no es solo «¿era ilegal entonces?», sino
    **«¿sería legal hoy?»**. Contesta las dos.

### Fase 6 — Decisión y propuesta

Como equipo de auditoría, redactad:

1. La **decisión** sobre el caso: ¿el sistema podría desplegarse, con condiciones, o no?
2. Las **medidas de corrección**, separadas en: datos, modelo, proceso y gobernanza.
3. Cómo lo **documentaríais**: qué iría en el *datasheet* del conjunto de datos y qué en la *model
   card* del modelo.
4. Quién asume la **responsabilidad** si el sistema vuelve a fallar, y con qué norma lo justificáis.

### Qué tienes que tener al terminar

Un documento con las cinco tablas rellenas, las cuatro respuestas de la Fase 4 y los cuatro puntos
de la Fase 6. Extensión orientativa: **dos o tres páginas**. **No se sube a Moodle**: se comenta en
clase y te sirve de base para el debate.

!!! note "Corrección"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD06](UD06_ES.md) · [Ejercicios](UD06_Ejercicios.md) ·
[Taller 2](UD06_T02_Auditoria_sesgos_ES.md)
