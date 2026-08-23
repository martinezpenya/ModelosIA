# UD05 · Taller 2 — Lógica difusa: el problema de las propinas

!!! important "Entregable de la unidad"
    Cuenta en el 40 % de actividades del RA5, junto con los
    [notebooks entregables](UD05_ActividadesEntregables.md). Trabaja en parejas si lo indica el
    profesor.

!!! warning "Requisitos"
    ```bash
    pip install scikit-fuzzy networkx
    ```

!!! caution "`scikit-fuzzy`: dos versiones y una trampa"
    La versión **0.4.2** ya **no arranca** en Python 3.12 o posterior: importa `imp` y `distutils`,
    eliminados del lenguaje. Instala la **0.5.0** (es lo que hace `pip install scikit-fuzzy`).

    En la 0.5.0 falla solo **`ControlSystem.view()`**, el dibujo del grafo del sistema, por un error
    de la librería. Los dibujos de cada variable (`servicio.view()`, `propina.view(sim=sim)`) no
    están afectados, y son los que se usan aquí. Si necesitas el grafo, párchealo:

    ```python
    from skfuzzy.control.visualization import ControlSystemVisualizer

    _init_original = ControlSystemVisualizer.__init__

    def _init_parcheado(self, control_system):
        _init_original(self, control_system)
        self.ctrl = control_system

    ControlSystemVisualizer.__init__ = _init_parcheado
    ```

**Objetivo**: implementar de principio a fin el ejemplo difuso de la teoría (§8.4) y comprobar en
código las tres fases de un sistema de razonamiento impreciso: fuzzificación, evaluación de reglas
y desfuzzificación (CE b).

### Fase 1 — Instalación y variables de entrada

```bash
pip install scikit-fuzzy networkx
```

```python
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
comida = ctrl.Antecedent(np.arange(0, 11, 1), 'comida')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

servicio['baja'] = fuzz.trimf(servicio.universe, [0, 0, 5])
servicio['media'] = fuzz.trimf(servicio.universe, [0, 5, 10])
servicio['alta'] = fuzz.trimf(servicio.universe, [5, 10, 10])

comida['mala'] = fuzz.trimf(comida.universe, [0, 0, 5])
comida['media'] = fuzz.trimf(comida.universe, [0, 5, 10])
comida['buena'] = fuzz.trimf(comida.universe, [5, 10, 10])
```

### Fase 2 — Variable de salida y reglas

```python
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

regla1 = ctrl.Rule(servicio['baja'] | comida['mala'], propina['baja'])
regla2 = ctrl.Rule(servicio['media'], propina['media'])
regla3 = ctrl.Rule(servicio['alta'] | comida['buena'], propina['alta'])

sistema = ctrl.ControlSystem([regla1, regla2, regla3])
sim = ctrl.ControlSystemSimulation(sistema)
```

### Fase 3 — Inferencia con el caso de la teoría

```python
sim.input['servicio'] = 9.8
sim.input['comida'] = 6.5
sim.compute()
print(f"Propina calculada: {sim.output['propina']:.2f} €")
```

!!! note "Tu número puede no ser exactamente el de la teoría"
    Con esta discretización del universo (`np.arange(0, 26, 1)`), el resultado ronda **19-20 €**,
    cerca de los 19,24 € de la teoría pero no idéntico: la **resolución de los universos** de
    entrada y salida afecta al resultado de la desfuzzificación por centro de gravedad. Es el
    mismo fenómeno de **sensibilidad** del §9: un parámetro que parece un detalle técnico
    (cuántos puntos tiene el universo discreto) cambia la respuesta del sistema.

### Fase 4 — Visualiza las funciones de pertenencia

```python
servicio.view()
comida.view()
propina.view()
sim.compute()
propina.view(sim=sim)
```

Guarda las cuatro figuras: son la evidencia de las fases de fuzzificación (dos primeras) y
desfuzzificación (última, con la línea vertical del resultado).

### Fase 5 — Cambia el escenario

Repite la Fase 3 con un servicio de 3 (malo) y una comida de 8 (buena). ¿Qué regla domina? ¿Es
coherente el resultado con lo que esperarías de un cliente que recibió un trato mediocre pero comió
muy bien?

### Fase 6 — Compara con un sistema de reglas «duro»

Escribe en `experta` una versión sin lógica difusa del mismo problema (reglas con umbrales fijos,
p. ej. `servicio >= 8 → propina alta`). Ejecuta los mismos dos escenarios de las Fases 3 y 5 y
compara los resultados. ¿En qué casos da lo mismo la versión difusa y la de reglas duras? ¿En
cuáles no?


### Entrega del Taller 2

Recopila las figuras y las explicaciones de las seis fases en **una memoria en PDF**.

| Fase | Evidencia mínima |
|---|---|
| 1 | Las dos variables de entrada con sus funciones de pertenencia |
| 2 | La variable de salida y las tres reglas |
| 3 | La propina calculada para el caso de la teoría, y **por qué no sale exactamente la misma cifra** |
| 4 | Las figuras de las funciones de pertenencia y del resultado |
| 5 | Un escenario propio, con su resultado interpretado |
| 6 | La comparación con un sistema de reglas «duro»: qué cambia en la respuesta |

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD05](UD05_ES.md) · [Taller 1](UD05_T01_Simular_sistema_experto_ES.md) · [Taller 3](UD05_T03_Controlador_experto_ES.md) · [Ejercicios](UD05_Ejercicios.md)
