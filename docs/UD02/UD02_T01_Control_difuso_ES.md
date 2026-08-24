# UD02 · Taller 1 — Control difuso con scikit-fuzzy

!!! important "Entregable de la unidad"
    Cuenta en el 40 % de actividades del RA2, junto con los otros talleres y la
    [actividad entregable](UD02_ActividadesEntregables.md).

!!! warning "Requisitos"
    Necesitas el **contenedor de prácticas de IA** de la UD00 funcionando, o un entorno Python
    3.12+ con `numpy` y `scikit-fuzzy`:

    ```bash
    docker compose up -d            # si usas el contenedor del curso
    pip install scikit-fuzzy==0.5.0
    ```

**Objetivo**: construir un sistema de control difuso tipo Mamdani que decida la **velocidad de un
ventilador** según la temperatura y la humedad de una sala, recorriendo las tres fases de un
sistema de razonamiento impreciso — fuzzificación, evaluación de reglas y desfuzzificación (RA2-d).

!!! tip "Hazlo en el notebook"
    Tienes este taller como **notebook con las celdas a rellenar**:
    [`UD02_T01_control_difuso.ipynb`](notebooks/UD02_T01_control_difuso.ipynb). Esta página es la
    referencia; lo que se entrega es el notebook completado.

### Fase 1 — Importa las librerías y define los universos

```python
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temperatura = ctrl.Antecedent(np.arange(0, 41, 1), 'temperatura')
humedad = ctrl.Antecedent(np.arange(0, 101, 1), 'humedad')
velocidad = ctrl.Consequent(np.arange(0, 101, 1), 'velocidad')
```

### Fase 2 — Funciones de pertenencia (términos lingüísticos)

```python
temperatura['fresca'] = fuzz.trimf(temperatura.universe, [0, 0, 18])
temperatura['agradable'] = fuzz.trimf(temperatura.universe, [15, 22, 28])
temperatura['caliente'] = fuzz.trapmf(temperatura.universe, [24, 30, 40, 40])

humedad['seca'] = fuzz.trimf(humedad.universe, [0, 0, 45])
humedad['media'] = fuzz.trimf(humedad.universe, [35, 55, 75])
humedad['humeda'] = fuzz.trapmf(humedad.universe, [60, 75, 100, 100])

velocidad['baja'] = fuzz.trimf(velocidad.universe, [0, 0, 40])
velocidad['media'] = fuzz.trimf(velocidad.universe, [25, 50, 75])
velocidad['alta'] = fuzz.trimf(velocidad.universe, [60, 100, 100])
```

!!! tip "¿Por qué trapezoidal en los extremos?"
    Las funciones de los extremos suelen ser trapezoidales para que «fresca» o «caliente»
    mantengan pertenencia plena hasta el límite del universo, y triangulares en el centro.

### Fase 3 — Reglas IF-THEN

```python
r1 = ctrl.Rule(temperatura['fresca'] & humedad['seca'], velocidad['baja'])
r2 = ctrl.Rule(temperatura['agradable'] & humedad['media'], velocidad['media'])
r3 = ctrl.Rule(temperatura['caliente'] | humedad['humeda'], velocidad['alta'])
```

### Fase 4 — Sistema y simulación

```python
sistema = ctrl.ControlSystem([r1, r2, r3])
sim = ctrl.ControlSystemSimulation(sistema)

sim.input['temperatura'] = 20
sim.input['humedad'] = 50
sim.compute()
print("Velocidad a 20 ºC / 50 %:", f"{sim.output['velocidad']:.1f}%")

sim.input['temperatura'] = 33
sim.input['humedad'] = 85
sim.compute()
print("Velocidad a 33 ºC / 85 %:", f"{sim.output['velocidad']:.1f}%")
```

### Fase 5 — Visualiza las funciones de pertenencia

```python
velocidad.view()      # o temperatura.view()
```

Añade al informe una captura de la gráfica y explica qué ocurre en cada simulación.

### Fase 6 — Experimento (respuesta razonada)

Prueba estas combinaciones y anota el resultado en una tabla:

| Temperatura | Humedad | Velocidad (%) | ¿Coherente? |
|---|---|---|---|
| 10 | 30 | | |
| 25 | 50 | | |
| 38 | 90 | | |
| 18 | 80 | | |

### Entrega del Taller 1

| Fase | Evidencia mínima |
|---|---|
| 1-2 | Las dos variables de entrada y la de salida, con sus funciones de pertenencia |
| 3 | Las tres reglas IF-THEN |
| 4 | Las dos simulaciones (20 ºC/50 % y 33 ºC/85 %) con su velocidad resultante |
| 5 | La captura de `velocidad.view()` |
| 6 | La tabla de experimentos completa, con la columna «¿Coherente?» justificada |

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD02](UD02_ES.md) · [Taller 2](UD02_T02_Sistema_reglas_ES.md) · [Ejercicios](UD02_Ejercicios.md)
