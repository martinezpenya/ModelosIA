# UD05 · Talleres de sistemas expertos

!!! important "Entregables de la unidad"
    Cuentan en el 40 % de actividades del RA5, junto con los notebooks entregables
    ([actividades entregables](UD05_ActividadesEntregables.md)). Trabaja en parejas si lo indica
    el profesor. Al terminar, sube un breve informe con capturas a Moodle.

!!! warning "Requisitos"
    Necesitas Python 3.10+ con `experta` funcionando. Recuerda el **parche de compatibilidad**
    (`collections.Mapping` desapareció en Python 3.10):

    ```python
    import collections, collections.abc
    if not hasattr(collections, 'Mapping'):
        collections.Mapping = collections.abc.Mapping
        collections.Iterable = collections.abc.Iterable
        collections.MutableMapping = collections.abc.MutableMapping
    ```

    Para el Taller 2 necesitas además `pip install scikit-fuzzy networkx`.

!!! caution "`scikit-fuzzy`: dos versiones y una trampa"
    La versión **0.4.2**, que era la habitual hasta hace poco, **ya no arranca** en Python 3.12 o
    posterior: importa `imp` y `distutils`, dos módulos que se eliminaron del lenguaje. Instala
    la **0.5.0** (es lo que hace `pip install scikit-fuzzy` sin fijar versión).

    En la 0.5.0 funciona todo menos **`ControlSystem.view()`**, el dibujo del grafo del sistema:
    lanza `AttributeError: 'ControlSystemVisualizer' object has no attribute 'ctrl'`. Es un error
    de la librería —la línea que guarda el sistema quedó dentro de un `if` y nunca se ejecuta—, no
    tuyo. Si lo necesitas, párchealo antes de usarlo:

    ```python
    from skfuzzy.control.visualization import ControlSystemVisualizer

    _init_original = ControlSystemVisualizer.__init__

    def _init_parcheado(self, control_system):
        _init_original(self, control_system)
        self.ctrl = control_system

    ControlSystemVisualizer.__init__ = _init_parcheado
    ```

    Los dibujos de cada variable (`servicio.view()`, `propina.view(sim=sim)`) no están afectados:
    funcionan tal cual, y son los que se usan en este taller.

## Taller 1 · Simular un sistema experto con `experta`

**Objetivo**: construir un sistema experto que **diagnostique** un problema y lo compare con uno
de **clasificación**, demostrando que un mismo motor simula comportamientos de ámbitos distintos
(CE b).

### Fase 1 — Parche e importación

```python
import collections, collections.abc
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping
    collections.Iterable = collections.abc.Iterable
    collections.MutableMapping = collections.abc.MutableMapping

from experta import *
```

### Fase 2 — Sistema de diagnóstico de un coche que no arranca

```python
class DiagnosticoCoche(KnowledgeEngine):
    @DefFacts()
    def inicio(self):
        yield Fact(accion="diagnosticar")

    @Rule(Fact(accion="diagnosticar"), salience=10)
    def arrancar(self):
        print("Diagnóstico del vehículo...")
        self.declare(Fact(luces="no_encienden"), Fact(sonido="ninguno"))
        self.declare(Fact(bateria="dudosa"))

    @Rule(Fact(luces="no_encienden"), Fact(sonido="ninguno"))
    def sin_corriente(self):
        self.declare(Fact(causa="bateria_descargada"))

    @Rule(Fact(causa="bateria_descargada"))
    def resultado(self):
        print("CAUSA PROBABLE: Batería descargada. Recarga o sustituye.")

engine = DiagnosticoCoche()
engine.reset()
engine.run()
```

**Salida esperada:**

```text
Diagnóstico del vehículo...
CAUSA PROBABLE: Batería descargada. Recarga o sustituye.
```

Anota la salida y explica qué reglas se dispararon y en qué orden.

### Fase 3 — Sistema de clasificación (otro ámbito)

```python
class Animales(KnowledgeEngine):
    @DefFacts()
    def inicio(self):
        yield Fact(analizar=True)

    @Rule(Fact(analizar=True), salience=10)
    def datos(self):
        self.declare(Fact(pelo=True), Fact(carnivoro=True),
                     Fact(color="leonado"), Fact(manchas="oscuras"))

    @Rule(Fact(pelo=True))
    def mamifero(self):
        self.declare(Fact(mamifero=True))

    @Rule(Fact(mamifero=True), Fact(carnivoro=True), Fact(color="leonado"),
          Fact(manchas="oscuras"))
    def guepardo(self):
        print("IDENTIFICADO: guepardo")

engine = Animales()
engine.reset()
engine.run()
```

!!! warning "El fallo más habitual de esta fase"
    Si llamas a `Animales().run()` sin **`reset()`** antes, no se dispara ninguna regla: `run()`
    solo ejecuta el ciclo de inferencia sobre los hechos ya cargados, y es `reset()` quien invoca
    `@DefFacts()` para cargarlos. Sin ese paso, `engine.facts` queda casi vacío y no hay nada que
    coincida con las reglas.

### Fase 4 — Analiza el orden de disparo

Modifica la regla `mamifero` para que tenga `salience=5` y vuelve a ejecutar. ¿Qué cambia? Explica
la **resolución de conflictos**.

### Fase 5 — Añade una regla con `NOT` y pregunta al usuario

```python
class DiagnosticoConPregunta(KnowledgeEngine):
    @DefFacts()
    def inicio(self):
        yield Fact(accion="diagnosticar")

    @Rule(Fact(accion="diagnosticar"), salience=10)
    def preguntar(self):
        r = input("¿Encienden las luces? (s/n): ").strip().lower()
        self.declare(Fact(luces=(r == "s")))

    @Rule(Fact(luces=True))
    def con_luces(self):
        print("Hay corriente: revisa arranque y combustible.")

    @Rule(Fact(luces=False))
    def sin_luces(self):
        print("Sin corriente: revisa batería y conexiones.")

DiagnosticoConPregunta().run()
```

### Fase 6 — Analiza la sensibilidad

Añade una regla con umbral (`usuarios > 50 → critica`) y prueba con distintos valores (40, 55, 50).
¿Qué ocurre justo en el umbral? ¿Cómo lo harías robusto (histéresis, §9)?

## Taller 2 · Lógica difusa con `scikit-fuzzy`: el problema de las propinas

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

## Taller 3 · Sistema experto como controlador de un proceso

**Objetivo**: implementar un **controlador experto** que regule la temperatura de una sala,
definiendo las especificaciones de respuesta (CE d) y observando cómo influye en el comportamiento
del sistema (CE e).

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

### Entrega

Sube a Moodle un informe breve con:

1. **Taller 1**: capturas de los tres sistemas (diagnóstico, clasificación, con pregunta) y las
   respuestas a las preguntas.
2. **Taller 2**: las cuatro figuras de las funciones de pertenencia, los dos escenarios de
   propina calculados y la comparación con el sistema de reglas duras.
3. **Taller 3**: la simulación del controlador con la tabla de especificaciones (error,
   asentamiento, sobreimpulso) antes y después de la perturbación, y las respuestas a las
   preguntas.
4. Respuesta a: *¿qué relación tiene un sistema experto con los sistemas híbridos reglas/datos del
   §7 y la lógica difusa del §8? ¿Cuándo usarías cada uno?*

!!! note "Corrección"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD05](UD05_ES.md) · [Ejercicios](UD05_Ejercicios.md)
