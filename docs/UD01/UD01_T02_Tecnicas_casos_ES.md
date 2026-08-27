# UD01 · Taller 2 — Técnicas de IA en casos reales

!!! important "Entrega evaluable"
    Se entrega en Moodle y se corrige con su **rúbrica**, que puedes leer en la propia tarea
    antes de empezar. El **peso** de esta entrega está en el libro de calificaciones de Moodle.
    Fuera de plazo, la nota máxima del trabajo es **5 sobre 10**.

**Objetivo**: clasificar técnicas de IA, justificar la elección y comprobarla contra la
documentación oficial.

**Resultado esperado**: una tabla de decisión técnica de 6 casos, contrastada con fuentes.

### Fase 1 — Clasifica los seis casos

Toma los **6 casos del ejercicio 19** de la página de ejercicios y clasifica cada uno en:
aprendizaje supervisado, no supervisado, PLN, visión artificial, robótica o sistema experto.

| Caso | Técnica principal | ¿Por qué esa y no otra? |
|---|---|---|
| Detectar grietas en piezas con fotos | | |
| Agrupar clientes por comportamiento de compra | | |
| Predecir si un correo es spam | | |
| Brazo robot que empaqueta cajas | | |
| Asistente que responde por voz | | |
| Recomendar rutas con reglas de un logista | | |

### Fase 2 — Propón una técnica alternativa

Para cada caso, indica **una técnica alternativa** viable y justifica en una frase por qué la
elegirías (o por qué la descartas): coste de etiquetado, volumen de datos, necesidad de explicar
la decisión, tiempo de respuesta.

### Fase 3 — Decide si el aprendizaje profundo aporta algo

Elige **3 de los 6 casos** y responde: ¿tendría sentido usar *deep learning*? Justifica con dos
criterios de los vistos en la teoría (volumen de datos disponible, necesidad de extraer
características automáticamente, coste computacional, explicabilidad exigida).

!!! warning "Empezar simple no es rendirse"
    Un modelo clásico bien ajustado, entrenado en segundos y explicable, suele ser mejor punto de
    partida que una red profunda. El *deep learning* se justifica cuando los datos son abundantes
    y las características difíciles de definir a mano (imagen, audio, texto libre).

### Fase 4 — Comprueba tu criterio con la documentación oficial

Abre la documentación de **scikit-learn** y contrasta dos de tus decisiones:

- Aprendizaje supervisado: <https://scikit-learn.org/stable/supervised_learning.html>
- Agrupamiento (*clustering*): <https://scikit-learn.org/stable/modules/clustering.html>

La página de *clustering* incluye una **tabla comparativa** de algoritmos con su escalabilidad,
su caso de uso y la geometría que asumen (K-Means para grupos convexos de tamaño similar, DBSCAN
para geometrías no planas y detección de valores atípicos, jerárquico cuando hay muchos grupos o
restricciones de conectividad). Anota:

1. Qué algoritmo concreto usarías en el caso de agrupamiento de clientes y **con qué argumento de
   la tabla oficial** lo defiendes.
2. Si la documentación te ha hecho **cambiar** alguna decisión de las fases 1-3.

### Fase 5 — Entrega

Una tabla final con: caso → técnica → técnica alternativa → justificación → ¿tiene sentido DL? →
qué dice la documentación oficial. Añade las dos referencias consultadas.

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD01](UD01_ES.md) · [Taller 1](UD01_T01_Mapa_sistemas_ES.md) · [Taller 3](UD01_T03_Nuevas_interacciones_ES.md)
