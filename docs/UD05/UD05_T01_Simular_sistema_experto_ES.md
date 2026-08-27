# UD05 · Taller 1 — Simular un sistema experto con `experta`

!!! important "Entrega evaluable"
    Se entrega en Moodle y se corrige con su **rúbrica**, que puedes leer en la propia tarea
    antes de empezar. El **peso** de esta entrega está en el libro de calificaciones de Moodle.
    Fuera de plazo, la nota máxima del trabajo es **5 sobre 10**. Trabaja en parejas si lo indica el profesor.

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

**Objetivo**: construir un sistema experto que **diagnostique** un problema y lo compare con uno
de **clasificación**, demostrando que un mismo motor simula comportamientos de ámbitos distintos
(CE b).

!!! tip "Hazlo en el notebook"
    Tienes este taller como **notebook con las celdas a rellenar**:
    [`UD05_T01_simular_sistema_experto.ipynb`](notebooks/UD05_T01_simular_sistema_experto.ipynb). Esta página es la referencia; lo que se
    entrega es el notebook completado.

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

motor = DiagnosticoConPregunta()
motor.reset()   # sin reset() los DefFacts no se cargan y NO se dispara nada
motor.run()
```

### Fase 6 — Analiza la sensibilidad

Añade una regla con umbral (`usuarios > 50 → critica`) y prueba con distintos valores (40, 55, 50).
¿Qué ocurre justo en el umbral? ¿Cómo lo harías robusto (histéresis, §9)?


### Entrega del Taller 1

Recopila las capturas y las explicaciones de las seis fases en **una memoria en PDF**. Se valora que
expliques **qué reglas se dispararon y en qué orden**, no solo la salida final.

| Fase | Evidencia mínima |
|---|---|
| 1 | El parche aplicado y `experta` importado sin error |
| 2 | El diagnóstico del coche funcionando, con las reglas que se dispararon |
| 3 | La clasificación del guepardo, y por qué el **mismo motor** sirve para otro ámbito |
| 4 | El cambio de `salience` y su efecto en el orden de disparo |
| 5 | La regla con `NOT` y la versión que pregunta al usuario |
| 6 | El umbral probado con tres valores, y tu propuesta de histéresis |

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD05](UD05_ES.md) · [Taller 2](UD05_T02_Logica_difusa_ES.md) · [Taller 3](UD05_T03_Controlador_experto_ES.md) · [Ejercicios](UD05_Ejercicios.md)
