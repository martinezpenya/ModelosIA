# UD04 · Taller 1 — Cinemática de un manipulador

!!! important "Entrega evaluable"
    Se entrega en Moodle y se corrige con su **rúbrica**, que puedes leer en la propia tarea
    antes de empezar. El **peso** de esta entrega está en el libro de calificaciones de Moodle.
    Fuera de plazo, la nota máxima del trabajo es **5 sobre 10**. Trabaja en parejas si lo indica el profesor.

!!! tip "Hazlo en el notebook"
    Tienes este taller como **notebook con las celdas a rellenar**:
    [`UD04_T01_cinematica_manipulador.ipynb`](notebooks/UD04_T01_cinematica_manipulador.ipynb).
    Esta página es la referencia; lo que se entrega es el notebook ejecutado.

!!! warning "Requisitos"
    ```bash
    pip install roboticstoolbox-python spatialmath-python numpy matplotlib
    ```

    En el aula se podrá usar además un simulador 3D (Webots o CoppeliaSim), según lo que decida el
    profesor y los equipos disponibles.

**Objetivo**: cargar un robot real (Panda de Franka o Puma 560), calcular su cinemática directa e
inversa, generar una trayectoria y detectar singularidades.

### Fase 1 — Carga el robot

```python
import roboticstoolbox as rtb
import spatialmath.base as smb

robot = rtb.models.Panda()
print(robot)
```

Anota en el informe: número de articulaciones, tipo de cada una y el nombre del modelo.

### Fase 2 — Cinemática directa (FK)

```python
import numpy as np

q = np.array([0, -0.8, 0.8, 0, 0.8, 0, 0])
pose = robot.fkine(q)
print(pose)
print("Posición del efector:", pose.t)
print("Orientación (ángulos de Euler):", smb.tr2eul(pose.A, unit='deg'))
```

Verifica que la posición del efector coincide con la que predice el modelo.

### Fase 3 — Cinemática inversa (IK)

```python
q_inv = robot.ikine_LM(pose)          # resuelve articulaciones para esa pose
print("Solución IK:", q_inv.q)
print("Pose reconstruida:", robot.fkine(q_inv.q).t)   # debe devolver la misma posición
```

Comprueba que al aplicar FK a la solución IK se recupera la pose original.

### Fase 4 — Genera una trayectoria

```python
from roboticstoolbox import jtraj

q0 = robot.qr          # configuración inicial (home)
q1 = np.array([0, -0.4, 1.2, 0, 0.8, 0, 0])
traj = jtraj(q0, q1, 50)     # 50 pasos entre q0 y q1
pose_t = robot.fkine(traj.q) # pose del efector a lo largo de la trayectoria
print(pose_t[:3, 3].T)       # posiciones (x,y,z) en cada paso
```

### Fase 5 — Detecta singularidades

```python
for i in range(0, 50, 10):
    J = robot.jacob0(traj.q[i])
    rango = np.linalg.matrix_rank(J)
    print(f"Fase {i}: rango del jacobiano = {rango}")
```

¿En algún punto el rango baja de 6? Si es así, anota cuál y por qué ocurre.

### Fase 6 — Visualiza la trayectoria

```python
import matplotlib.pyplot as plt

x = pose_t[:, 0, 3]
y = pose_t[:, 1, 3]
z = pose_t[:, 2, 3]
ax = plt.figure().add_subplot(projection='3d')
ax.plot(x, y, z, label='Trayectoria')
ax.scatter(x[0], y[0], z[0], c='g', label='Inicio')
ax.scatter(x[-1], y[-1], z[-1], c='r', label='Fin')
ax.legend()
plt.show()
```


### Entrega del Taller 1

Sube el **notebook ejecutado**. Se valora que **expliques lo que ocurre**, no solo que la celda dé
un resultado: una salida sin interpretar no demuestra que hayas entendido nada.

| Fase | Evidencia mínima |
|---|---|
| 1 | El robot cargado, con el número y el tipo de sus articulaciones |
| 2 | Posición y orientación del efector, y por qué la FK tiene una única solución |
| 3 | La solución de IK **verificada** con FK, y por qué los ángulos no coinciden con los de partida |
| 4 | La trayectoria generada y la diferencia entre `jtraj` y `ctraj` |
| 5 | El rango del jacobiano a lo largo de la trayectoria, y qué habría que cambiar para provocar una singularidad |
| 6 | El recorrido del efector dibujado en 3D, con inicio y fin marcados |

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD04](UD04_ES.md) · [Taller 2](UD04_T02_Diseno_sistema_robotizado_ES.md) · [Ejercicios](UD04_Ejercicios.md)
