# UD02 · Taller 2 — Sistema basado en reglas con experta

!!! important "Entregable de la unidad"
    Cuenta en el 40 % de actividades del RA2, junto con los otros talleres y la
    [actividad entregable](UD02_ActividadesEntregables.md).

!!! warning "Requisitos"
    ```bash
    pip install "frozendict>=2.3"
    pip install --no-deps experta
    pip install schema==0.6.7
    ```

!!! caution "`experta` necesita un parche en Python 3.10+"
    `experta` 1.9.4 importa `collections.Mapping`, retirado de la librería estándar. El parche
    (issue #34 del proyecto) va **siempre antes** de `from experta import *`, o el import falla con
    `ImportError: cannot import name 'Mapping' from 'collections'`. Ver Fase 2.

**Objetivo**: implementar un **mini sistema experto de diagnóstico** de un PC que no arranca, con
`experta`, y comprobar en código el ciclo reconocer-actuar de un sistema basado en reglas (RA2-e).

!!! tip "Hazlo en el notebook"
    Tienes este taller como **notebook con las celdas a rellenar**:
    [`UD02_T02_sistema_reglas.ipynb`](notebooks/UD02_T02_sistema_reglas.ipynb). Esta página es la
    referencia; lo que se entrega es el notebook completado.

### Fase 1 — Instala y verifica el parche

```bash
pip install "frozendict>=2.3"
pip install --no-deps experta
pip install schema==0.6.7
```

### Fase 2 — Parche de compatibilidad e importación

```python
import collections
import collections.abc
if not hasattr(collections, 'Mapping'):
    collections.Mapping = collections.abc.Mapping
    collections.Iterable = collections.abc.Iterable
    collections.MutableMapping = collections.abc.MutableMapping

from experta import *
```

### Fase 3 — Define el motor de conocimiento

```python
class DiagnosticoPC(KnowledgeEngine):
    @DefFacts()
    def inicio(self):
        yield Fact(accion="diagnosticar")

    @Rule(Fact(accion="diagnosticar"), salience=10)
    def arrancar(self):
        print("Diagnóstico del PC...")
        self.declare(Fact(luz_encendida=True))
        self.declare(Fact(sonido="pitidos_cortos"))
        self.declare(Fact(pantalla="negra"))

    @Rule(Fact(luz_encendida=True), Fact(sonido="pitidos_cortos"))
    def ram(self):
        self.declare(Fact(causa="problema_ram"))

    @Rule(Fact(luz_encendida=True), Fact(pantalla="negra"))
    def gpu(self):
        self.declare(Fact(causa="problema_grafica"))

    @Rule(Fact(causa="problema_ram"))
    def resultado_ram(self):
        print("DIAGNÓSTICO: Fallo de memoria RAM. Resitúa o sustituye los módulos.")

    @Rule(Fact(causa="problema_grafica"))
    def resultado_gpu(self):
        print("DIAGNÓSTICO: Fallo de gráfica o cable de vídeo. Revisa la conexión.")
```

### Fase 4 — Ejecuta y observa la agenda

```python
engine = DiagnosticoPC()
engine.reset()   # declara DefFacts + InitialFact
engine.run()     # ciclo reconocer-actuar
```

Registra en el informe la salida y explica qué hechos se declararon y qué reglas se dispararon.

### Fase 5 — Añade una regla con `salience` y variables

Modifica el motor para que el diagnóstico tenga **prioridad** y acepte un hecho parametrizado:

```python
    @Rule(Fact(causa="problema_ram"), salience=5)
    def prioridad(self):
        print("> (prioridad: revisar RAM antes que cualquier otra acción)")
```

### Fase 6 — Amplía el sistema

Añade dos reglas nuevas: si `luz_encendida=False` → `causa="sin_alimentacion"` con su mensaje de
diagnóstico, y si `pantalla="mensaje_bios"` → `causa="configuracion_bios"`. Responde en el informe:
*¿cuándo usarías lógica difusa (Taller 1) y cuándo un sistema basado en reglas como este? Justifica
con un ejemplo real.*

### Entrega del Taller 2

| Fase | Evidencia mínima |
|---|---|
| 1-2 | El parche aplicado y la importación sin errores |
| 3 | El código completo del motor de conocimiento |
| 4 | La salida de `engine.run()`, con los hechos declarados y las reglas disparadas explicados |
| 5 | La regla con `salience` añadida y su efecto comprobado |
| 6 | Las dos reglas nuevas y la respuesta comparando lógica difusa frente a reglas |

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD02](UD02_ES.md) · [Taller 1](UD02_T01_Control_difuso_ES.md) · [Ejercicios](UD02_Ejercicios.md)
