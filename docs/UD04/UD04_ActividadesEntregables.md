# UD04 · Entregas
!!! important "Qué se entrega, y con qué se corrige cada cosa"
    En esta unidad hay tres regímenes. Las **entregas evaluables** se corrigen con su
    [rúbrica](#rubricas), que puedes leer antes de empezar. Las de **apto / no apto** hay que
    hacerlas y entregarlas, pero no se puntúan con rúbrica: cuentan como hechas o no hechas.

    | Actividad | Régimen |
    |---|---|
    | [`T01` Cinemática de un manipulador](UD04_T01_Cinematica_manipulador_ES.md) | Entrega evaluable |
    | `EX1` Ejercicios de OpenCV | Entrega evaluable |
    | `EX2` Navegar con cámara, por reglas | Entrega evaluable |
    | `EX3` Navegar con cámara, con lógica difusa | Entrega evaluable |
    | `EX5` Controlar el robot con una red neuronal | Entrega evaluable |
    | [`T02` Diseño de un sistema robotizado](UD04_T02_Diseno_sistema_robotizado_ES.md) | Apto / no apto |
    | `EX4` Generar los datos de entrenamiento | Apto / no apto |
    | `EX6` Aprendizaje por refuerzo con NEAT | Apto / no apto |

    El **peso** de cada entrega está en el libro de calificaciones de Moodle, no aquí.
!!! warning "Fuera de plazo, la nota máxima es 5"
    El plazo se cierra en la fecha indicada en Moodle. Si necesitas entregar después, **avisa al
    profesor** y se reabre la tarea un tiempo limitado; en ese caso la nota máxima del trabajo es
    **5 sobre 10**. La rúbrica lo recoge de forma explícita.


!!! warning "No son independientes: son una secuencia"
    `EX4` genera el fichero de datos que necesita `EX5`. Si te saltas el orden o pierdes ese
    fichero, tendrás que volver atrás.

    ```mermaid
    flowchart LR
        A["EX1 · OpenCV<br/>ver la imagen"] --> B["EX2 · reglas<br/>seguir la línea"]
        B --> C["EX3 · lógica difusa<br/>la misma línea, suave"]
        C --> D["EX4 · generar datos<br/>conduces y se graba"]
        D -->|training_data.txt| E["EX5 · red neuronal<br/>aprende de tus datos"]
        E -->|robot.keras| F["EX6 · NEAT<br/>evoluciona sin datos"]
    ```

!!! note "Entorno"
    Todos funcionan en **Colab** y en el contenedor de la UD00. La primera celda instala lo
    necesario. Dos avisos que te ahorrarán tiempo:

    - **No instales `tensorflow` a mano.** `EX5` usa **Keras 3**, que funciona con el backend que
      haya: en Colab usa el TensorFlow que ya viene, y en local, PyTorch.
    - Si ves código antiguo con `keras.backend.mean` o `keras.backend.abs`, **ya no existen** en
      Keras 3: el equivalente es `keras.ops.mean` y `keras.ops.abs`.

## EX1 · Ejercicios de OpenCV

Tres ejercicios de visión sobre imagen y vídeo: detectar **bordes** y enmarcarlos, detectar
**movimiento** entre fotogramas consecutivos y calcular el **flujo óptico**.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_EX1_ejercicios_opencv.ipynb`](notebooks/UD04_EX1_ejercicios_opencv.ipynb) |
| Imagen | [`EX1.-camp.png`](notebooks/EX1.-camp.png) |
| Vídeo | [`EX1.-vtest.mp4`](notebooks/EX1.-vtest.mp4) |

**Se entrega**: el notebook con los tres ejercicios resueltos y sus salidas.

## EX2 · Navegar con cámara, por reglas

El robot tiene que **seguir una línea** en el suelo usando solo lo que ve su cámara. Aquí escribes
tú todas las condiciones: dónde está la línea en la imagen, y qué hacer en cada caso.

Dos escenarios: **línea simple** y **línea doble**.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_EX2_navegar_camara.ipynb`](notebooks/UD04_EX2_navegar_camara.ipynb) |
| Pistas | [1](notebooks/EX2_pista_1.png) · [2](notebooks/EX2_pista_2.png) · [3](notebooks/EX2_pista_3.png) · [4](notebooks/EX2_pista_4.png) · [5](notebooks/EX2_pista_5.png) · [6](notebooks/EX2_pista_6.png) |

**Se entrega**: el notebook con el controlador funcionando en los dos escenarios.

## EX3 · Navegar con cámara, con lógica difusa

El **mismo problema** que `EX2`, resuelto con lógica difusa: variables lingüísticas, funciones de
pertenencia, reglas y desfuzzificación. Enlaza directamente con la UD05.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_EX3_navegar_camara_difusa.ipynb`](notebooks/UD04_EX3_navegar_camara_difusa.ipynb) |
| Pistas | Las mismas seis de `EX2` |

**Se entrega**: el notebook con el sistema difuso completo y el robot navegando en los dos
escenarios.

!!! tip "Compara antes de entregar"
    Ya has resuelto el mismo problema de dos formas. Antes de entregar, apunta en qué se diferencian
    el comportamiento de `EX2` y el de `EX3`: no cuál «va mejor», sino **cómo se mueve el robot** en
    cada caso, y por qué.

## EX4 · Generar los datos de entrenamiento

Aquí no se entrena nada todavía: **conduces tú el robot** y el notebook graba lo que ve la cámara
junto con lo que tú decidiste hacer. El resultado es un conjunto de ejemplos etiquetados.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_EX4_generar_datos_entrenamiento.ipynb`](notebooks/UD04_EX4_generar_datos_entrenamiento.ipynb) |

**Se entrega**: el notebook **y el fichero `training_data.txt` con tu nombre**. Guárdatelo: es la
entrada de `EX5`.

## EX5 · Controlar el robot con una red neuronal

Lees el `training_data.txt` de `EX4`, **construyes y entrenas** una red neuronal con esos ejemplos y
la usas para conducir el robot. Tres celdas están vacías a propósito: la arquitectura de la red, el
entrenamiento y la función de control.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_EX5_red_neuronal.ipynb`](notebooks/UD04_EX5_red_neuronal.ipynb) |

**Se entrega**: el notebook **y el fichero `.keras` con tu nombre**, con la red ya entrenada. Con ese
fichero, la celda de carga permite **probar cómo se comporta tu red sin repetir el entrenamiento**
—que es largo—, y es así como se corrige.

!!! note "Antes de entrenar hay que mirar los datos"
    La rúbrica puntúa `classifica_moviments` y el **balanceo**, y no es un capricho: conduciendo, un
    robot va hacia delante muchísimo más de lo que gira, así que el conjunto sale **desequilibrado**.
    Una red entrenada con esos datos aprende a ir recto siempre, que es lo que más acierta de media
    y lo que peor sigue la línea.

## EX6 · Aprendizaje por refuerzo con NEAT

El mismo control, sin ejemplos. **NEAT** evoluciona a la vez los pesos **y la topología** de la red:
tú solo defines qué entra, qué sale y cómo se mide si lo está haciendo bien.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_EX6_neat.ipynb`](notebooks/UD04_EX6_neat.ipynb) |

**Se entrega**: el notebook y una **memoria en PDF** con tus pruebas variando `fitness_threshold` y
`pop_size`, la justificación de `num_inputs` y `num_outputs`, y una reflexión sobre el aprendizaje
por refuerzo. Es de **apto / no apto**: sin la memoria no cuenta como entregado.

## Rúbricas

Son las rúbricas reales del curso. Las seis tareas se califican **sobre 10**; los puntos de cada
rúbrica se **escalan** a esa nota.

Los niveles son los mismos en casi todos los criterios: **No entregada** (0) · **Incorrecta** ·
**Parcialmente incorrecta** · **Bien pero fuera de plazo** · **Correcta**.

!!! warning "Entregar tarde cuesta casi lo mismo que entregar a medias"
    Fíjate en los niveles: «bien pero fuera de plazo» puntúa igual o casi igual que «parcialmente
    incorrecta». No es un redondeo: es la forma de decir que el plazo cuenta.

### EX1 · Ejercicios de OpenCV (8 puntos)

| Criterio | Correcta | Parcial o fuera de plazo | Incorrecta |
|---|---|---|---|
| Ejercicio 1 · bordes | 4 | 2 | 0,5 |
| Ejercicio 2 · detección de movimiento | 2 | 1 | 0,5 |
| Ejercicio 3 · flujo óptico | 2 | 1-2 | 0,5 |

### EX2 · Navegar con cámara (6 puntos)

| Criterio | Correcta | Parcial o fuera de plazo | Incorrecta |
|---|---|---|---|
| Seguidor de línea simple | 4 | 2 | 0,5 |
| Seguimiento de línea doble | 2 | 1 | 0,5 |

### EX3 · Navegar con cámara difusa (15 puntos)

Cinco criterios de **3 puntos** cada uno (correcta 3 · parcial 2 · fuera de plazo 1,5 · incorrecta 1):

| Criterio |
|---|
| Variable de entrada y funciones de pertenencia |
| Variables de salida |
| Reglas, sistema de control y simulación |
| Controlador del robot · línea simple |
| Controlador del robot · línea doble |

### EX4 · Generar datos de entrenamiento (14 puntos)

| Criterio | Correcta | Parcial o fuera de plazo | Incorrecta |
|---|---|---|---|
| Entrega `training_data.txt` con tu nombre | 2 | 1 | 1 |
| `determine_move` devuelve movimiento, rotación y centro | **6** | 3 | 1 |
| Normalización de datos | 3 | 2 · 1,5 | 1 |
| Generación masiva de datos | 3 | 2 · 1,5 | 1 |

`determine_move` vale **6 de 14**: casi la mitad de la tarea.

### EX5 · Red neuronal con los datos de EX4 (14 puntos)

| Criterio | Correcta | Parcial o fuera de plazo | Incorrecta |
|---|---|---|---|
| `classifica_moviments` | 3 | 2 · 1,5 | 1 |
| Balanceo de movimientos | 3 | 2 · 1,5 | 1 |
| Crear y entrenar la red neuronal | 3 | 2 · 1,5 | 1 |
| `network_driver` · controlar el robot con la red | 3 | 2 · 1,5 | 1 |
| Entrega el `.keras` con tu nombre y la red entrenada | 2 | 1 | 1 |

### EX6 · Aprendizaje por refuerzo con NEAT (12 puntos)

Cuatro criterios de **3 puntos** (correcta 3 · parcial 2 · fuera de plazo 1,5 · incorrecta 1):

| Criterio |
|---|
| Decisión de `num_inputs` y `num_outputs` |
| Pruebas con `fitness_threshold` y `pop_size` |
| Reflexión sobre el aprendizaje por refuerzo |
| Formato de la memoria en PDF (portada, pie, etc.) |

La reflexión y el formato son **6 de 12**: la mitad. Es el entregable más abierto de la unidad y el
único cuya rúbrica puntúa explícitamente cómo comunicas el trabajo.

---
[Volver a la UD04](UD04_ES.md) · [Notebooks guiados](UD04_ActividadesGuiadas.md) · [Taller 1](UD04_T01_Cinematica_manipulador_ES.md) · [Taller 2](UD04_T02_Diseno_sistema_robotizado_ES.md)
