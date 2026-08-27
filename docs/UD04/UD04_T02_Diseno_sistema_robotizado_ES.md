# UD04 · Taller 2 — Diseño de un sistema robotizado

!!! important "Entrega de apto / no apto"
    Se entrega en Moodle, pero **no se corrige con rúbrica**: cuenta como hecha o no hecha.
    Tiene un peso pequeño dentro del RA, y lo tienes en el libro de calificaciones de Moodle.
    Trabaja en parejas si lo indica el profesor.

!!! tip "Hazlo en el notebook"
    Tienes este taller como **notebook con las celdas a rellenar**:
    [`UD04_T02_diseno_sistema_robotizado.ipynb`](notebooks/UD04_T02_diseno_sistema_robotizado.ipynb).
    Es un taller de análisis: casi todas las celdas son de texto y **no hace falta instalar nada**.

**Objetivo**: aplicar los criterios de diseño e implementación (CE d) para proponer un sistema
robotizado que resuelva un caso real, justificando la selección y la seguridad.

### Fase 1 — Elige el caso

Elige uno de estos casos (o propón otro al profesor):

- **A. Paletizado**: cajas de 12 kg, 1.400 mm de alcance, 20 cajas/min, célula aislada.
- **B. Montaje asistido**: piezas de 2 kg, alcance 850 mm, comparte espacio con personas,
  precisión ±0,1 mm.
- **C. Inspección por visión**: piezas pequeñas en cinta, robot de picking + cámara, ritmo 40/min.

### Fase 2 — Selección del robot

Con los criterios de la teoría (payload, alcance, repetibilidad, entorno), selecciona un modelo
entre estos:

| Robot | Payload | Alcance | Repetibilidad | Tipo |
|---|---|---|---|---|
| UR5e | 5 kg | 850 mm | ±0,05 mm | Cobot |
| UR10e | 12,5 kg | 1.300 mm | ±0,05 mm | Cobot |
| KUKA KR AGILUS 6 | 6 kg | 1.101 mm | ±0,02 mm | Industrial |
| FANUC M-410 | 700 kg | 3,1 m | ±0,2 mm | Industrial (paletizado) |

Justifica en el informe: ¿por qué ese modelo y no otro para tu caso?

### Fase 3 — Sensores y herramienta

Para tu caso, indica:
- Qué **sensores** necesita (visión, fuerza, proximidad) y por qué.
- Qué **herramienta (EOAT)** lleva el efector (pinza, ventosa, pistola, cámara).

### Fase 4 — Diseño de la célula y la Industria 4.0

Dibuja (a mano o con texto) la **célula robotizada**: robot, conveyor, sensores, PLC, vallado/
zona colaborativa. Indica:
- Qué protocolos de comunicación usarías (PROFINET/EtherCAT, OPC UA/MQTT).
- Qué datos enviarías a un gemelo digital para mantenimiento predictivo.

### Fase 5 — Seguridad y normativa

Aplica la normativa a tu caso:

| Elemento | Tu decisión |
|---|---|
| Tipo de aplicación (industrial aislada o colaborativa) | |
| Vallado / zonas de seguridad | |
| Límites biomecánicos (si es colaborativo, ISO 10218:2025) | |
| Ciberseguridad de la célula | |

Justifica cada decisión con la normativa.

### Fase 6 — Presentación y evaluación

Prepara una **ficha técnica** de tu sistema (1 página) con: tarea, robot elegido (y por qué),
sensores/herramienta, layout, comunicaciones, seguridad y un **KPI** de mejora (p. ej. cadencia,
coste por pieza, tiempo de ciclo).



### Entrega del Taller 2

Sube el **notebook ejecutado**. Aquí no hay respuestas correctas, hay **decisiones justificadas**:
cada elección tiene que citar el criterio o la norma que la respalda.

| Fase | Evidencia mínima |
|---|---|
| 1 | El caso elegido y por qué |
| 2 | El **payload real** calculado (pieza + herramienta + cables), el robot elegido y **por qué descartas los otros tres** |
| 3 | Sensores exteroceptivos y propioceptivos, y la herramienta, justificados |
| 4 | El esquema de la célula, el bus de campo, el protocolo de telemetría y qué datos irían al gemelo digital |
| 5 | La tabla de seguridad **con la norma citada en cada fila** |
| 6 | La ficha técnica completa, con un **KPI medible** |

Y la respuesta a: *¿qué relación hay entre la robótica y las técnicas de IA de las unidades
anteriores (percepción, razonamiento, acción)?*

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD04](UD04_ES.md) · [Taller 1](UD04_T01_Cinematica_manipulador_ES.md) · [Ejercicios](UD04_Ejercicios.md)
