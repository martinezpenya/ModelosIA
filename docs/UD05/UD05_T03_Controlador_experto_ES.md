# UD05 · Taller 3 — Sistema experto como controlador de un proceso

!!! important "Entregable de la unidad"
    Cuenta en el 40 % de actividades del RA5, junto con los
    [notebooks entregables](UD05_ActividadesEntregables.md). Trabaja en parejas si lo indica el
    profesor.

!!! warning "Requisitos"
    Python 3.10+ con `experta`. Recuerda el **parche de compatibilidad**
    (`collections.Mapping` desapareció en Python 3.10):

    ```python
    import collections, collections.abc
    if not hasattr(collections, 'Mapping'):
        collections.Mapping = collections.abc.Mapping
        collections.Iterable = collections.abc.Iterable
        collections.MutableMapping = collections.abc.MutableMapping
    ```

**Objetivo**: implementar un **controlador experto** que regule la temperatura de una sala,
definiendo las especificaciones de respuesta (CE d) y observando cómo influye en el comportamiento
del sistema (CE e).

!!! tip "Hazlo en el notebook"
    Tienes este taller como **notebook con las celdas a rellenar**:
    [`UD05_T03_controlador_experto.ipynb`](notebooks/UD05_T03_controlador_experto.ipynb). Esta página es la referencia; lo que se
    entrega es el notebook completado.

### Fase 1 — La planta (modelo simple)

```python
def simular_planta(temp, potencia, dt=1.6, inercia=0.05, exterior=15.0):
    """Modelo simple de una sala con inercia térmica."""
    return temp + inercia * (exterior - temp) + potencia * dt
```

### Fase 2 — El controlador experto

```python
from experta import P  # constraint de predicado: envuelve el lambda

class ControladorClima(KnowledgeEngine):
    def __init__(self, setpoint=21.0):
        super().__init__()
        self.setpoint = setpoint
        self.potencia = 0.0

    @DefFacts()
    def inicio(self):
        yield Fact(controlar=True)

    @Rule(Fact(controlar=True), salience=10)
    def leer(self):
        # simula la lectura del sensor
        error = self.setpoint - self._temp
        self.declare(Fact(error=round(error, 2)))

    @Rule(Fact(error=P(lambda e: e > 3)))
    def alta(self):
        self.potencia = 1.0

    @Rule(Fact(error=P(lambda e: 0 < e <= 3)))
    def media(self):
        self.potencia = 0.5

    @Rule(Fact(error=P(lambda e: -1 <= e <= 0)))
    def baja(self):
        self.potencia = 0.2

    @Rule(Fact(error=P(lambda e: e < -1)))
    def apagar(self):
        self.potencia = 0.0

    def paso(self, temp):
        self._temp = temp
        self.reset()
        self.run()
        return self.potencia

ctrl = ControladorClima(setpoint=21.0)
temp = 15.0
for i in range(80):
    potencia = ctrl.paso(temp)
    temp = simular_planta(temp, potencia)
    if i % 5 == 0:
        print(f"t={i:3d}: temp={temp:.2f}  potencia={potencia:.2f}")
```

!!! warning "Por qué el condicional va envuelto en `P(...)`"
    `experta` compara el valor de un campo de un `Fact` por **igualdad**, no lo evalúa: si escribes
    `Fact(error=lambda e: e > 3)`, la regla busca un hecho cuyo `error` sea literalmente esa
    función, y nunca lo encuentra. `P(...)` es el **constraint de predicado** de `experta`: le dice
    al motor «aplica esta función al valor del campo y compara el resultado con verdadero».
    Sin `P()`, el controlador de esta fase se queda **congelado con potencia 0** para siempre y no
    parece un error evidente, porque no lanza ninguna excepción.

Con estos parámetros, la temperatura entra en la banda 20,5-21,5 ºC hacia el paso 5 y se estabiliza
en torno a **21,4 ºC**, dentro de la especificación.

### Fase 3 — Mide las especificaciones de respuesta

Añade código para medir:

- **Error en régimen permanente** (temperatura final − setpoint).
- **Tiempo de asentamiento** (en qué paso entra en la banda 20,5-21,5 ºC, y no vuelve a salir).
- **Sobreimpulso** (¿supera alguna vez 21,5 ºC?).

### Fase 4 — Añade una perturbación

En el paso 40, cambia la temperatura exterior a 5 ºC (ventana abierta) y observa cómo responde el
controlador. ¿Mantiene la temperatura en la banda?

### Fase 5 — Analiza la sensibilidad

Cambia el umbral de la regla `media` (de 3 a 1,5) y compara la respuesta. ¿Qué pasa con el
sobreimpulso? ¿Y con el tiempo de asentamiento? Registra los valores en una tabla.

### Fase 6 — Compara con un PID (conceptual)

Dibuja (o describe) cómo respondería un PID sintonizado frente al controlador experto y explica
qué ventaja tiene cada uno. ¿Cuándo usarías cada uno?



### Entrega del Taller 3

Recopila la simulación y las explicaciones de las seis fases en **una memoria en PDF**.

| Fase | Evidencia mínima |
|---|---|
| 1 | La planta simulada y qué representa cada parámetro |
| 2 | El controlador experto funcionando, con las reglas que se disparan en cada tramo |
| 3 | La **tabla de especificaciones**: error en régimen permanente, tiempo de asentamiento y sobreimpulso |
| 4 | La respuesta ante la perturbación, y si se mantiene en la banda |
| 5 | La misma tabla **antes y después** de cambiar el umbral |
| 6 | La comparación razonada con un PID: cuándo usarías cada uno |

Y la respuesta a: *¿qué relación tiene un sistema experto con los sistemas híbridos reglas/datos y
la lógica difusa? ¿Cuándo usarías cada uno?*

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD05](UD05_ES.md) · [Taller 1](UD05_T01_Simular_sistema_experto_ES.md) · [Taller 2](UD05_T02_Logica_difusa_ES.md) · [Ejercicios](UD05_Ejercicios.md)
