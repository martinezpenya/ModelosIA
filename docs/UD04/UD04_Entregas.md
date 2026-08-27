# UD04 · Entregas

!!! important "Qué se entrega, y con qué se corrige cada cosa"
    En esta unidad hay tres regímenes. Las **entregas evaluables** se corrigen con la rúbrica
    de su tarea en Moodle, que puedes leer antes de empezar. Las de **apto / no apto** hay que
    hacerlas y entregarlas, pero no se puntúan con rúbrica: cuentan como hechas o no hechas.

    | Actividad | Régimen |
    |---|---|
    | [`N04` Cinemática de un manipulador](notebooks/UD04_N04_cinematica_manipulador.ipynb) | Entrega evaluable |
    | [`N05` Ejercicios de OpenCV](notebooks/UD04_N05_ejercicios_opencv.ipynb) | Entrega evaluable |
    | [`N06` Navegar con cámara, por reglas](notebooks/UD04_N06_navegar_camara.ipynb) | Entrega evaluable |
    | [`N07` Navegar con cámara, con lógica difusa](notebooks/UD04_N07_navegar_camara_difusa.ipynb) | Entrega evaluable |
    | [`N08` Generar los datos de entrenamiento](notebooks/UD04_N08_generar_datos_entrenamiento.ipynb) | Apto / no apto |
    | [`N09` Controlar el robot con una red neuronal](notebooks/UD04_N09_red_neuronal.ipynb) | Entrega evaluable |
    | [`N10` Aprendizaje por refuerzo con NEAT](notebooks/UD04_N10_neat.ipynb) | Apto / no apto |
    | [`N11` Diseño de un sistema robotizado](notebooks/UD04_N11_diseno_sistema_robotizado.ipynb) | Apto / no apto |

    El **peso** de cada entrega está en el libro de calificaciones de Moodle, no aquí.

!!! warning "No son independientes: son una secuencia"
    `N08` genera el fichero de datos que necesita `N09`. Si te saltas el orden o pierdes ese
    fichero, tendrás que volver atrás.

    ```mermaid
    flowchart LR
        A["N05 · OpenCV<br/>ver la imagen"] --> B["N06 · reglas<br/>seguir la línea"]
        B --> C["N07 · lógica difusa<br/>la misma línea, suave"]
        C --> D["N08 · generar datos<br/>conduces y se graba"]
        D -->|training_data.txt| E["N09 · red neuronal<br/>aprende de tus datos"]
        E -->|robot.keras| F["N10 · NEAT<br/>evoluciona sin datos"]
    ```

!!! note "Entorno"
    Todos funcionan en **Colab** y en el contenedor de la UD00. La primera celda instala lo
    necesario. Dos avisos que te ahorrarán tiempo:

    - **No instales `tensorflow` a mano.** `N09` usa **Keras 3**, que funciona con el backend que
      haya: en Colab usa el TensorFlow que ya viene, y en local, PyTorch.
    - Si ves código antiguo con `keras.backend.mean` o `keras.backend.abs`, **ya no existen** en
      Keras 3: el equivalente es `keras.ops.mean` y `keras.ops.abs`.

<!-- AUTO:notebooks inicio -->
| Notebook | Qué es | Descargar | Abrir en Colab |
|---|---|---|---|
| [`N04` · Cinemática de un manipulador](notebooks/UD04_N04_cinematica_manipulador.ipynb) | Cinemática directa e inversa de un robot real (Panda, Puma 560) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD04/notebooks/UD04_N04_cinematica_manipulador.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD04/notebooks/UD04_N04_cinematica_manipulador.ipynb){:target="_blank"} |
| [`N05` · Ejercicios de OpenCV](notebooks/UD04_N05_ejercicios_opencv.ipynb) | Visión · ejercicios de OpenCV sobre imagen y vídeo | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD04/notebooks/UD04_N05_ejercicios_opencv.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD04/notebooks/UD04_N05_ejercicios_opencv.ipynb){:target="_blank"} |
| [`N06` · Navegar con cámara](notebooks/UD04_N06_navegar_camara.ipynb) | Navegación por reglas con la cámara | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD04/notebooks/UD04_N06_navegar_camara.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD04/notebooks/UD04_N06_navegar_camara.ipynb){:target="_blank"} |
| [`N07` · Navegar con cámara difusa](notebooks/UD04_N07_navegar_camara_difusa.ipynb) | La misma navegación, con lógica difusa | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD04/notebooks/UD04_N07_navegar_camara_difusa.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD04/notebooks/UD04_N07_navegar_camara_difusa.ipynb){:target="_blank"} |
| [`N08` · Generar datos de entrenamiento](notebooks/UD04_N08_generar_datos_entrenamiento.ipynb) | Insumo de `N09` · genera el conjunto de entrenamiento | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD04/notebooks/UD04_N08_generar_datos_entrenamiento.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD04/notebooks/UD04_N08_generar_datos_entrenamiento.ipynb){:target="_blank"} |
| [`N09` · Controlar el robot con una red neuronal](notebooks/UD04_N09_red_neuronal.ipynb) | Navegación con una red neuronal entrenada | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD04/notebooks/UD04_N09_red_neuronal.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD04/notebooks/UD04_N09_red_neuronal.ipynb){:target="_blank"} |
| [`N10` · Aprendizaje por refuerzo con NEAT](notebooks/UD04_N10_neat.ipynb) | Aprendizaje por refuerzo · evolucionar la red con NEAT | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD04/notebooks/UD04_N10_neat.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD04/notebooks/UD04_N10_neat.ipynb){:target="_blank"} |
| [`N11` · Diseño de un sistema robotizado](notebooks/UD04_N11_diseno_sistema_robotizado.ipynb) | Diseño · evaluar alternativas para un problema real (CE d) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD04/notebooks/UD04_N11_diseno_sistema_robotizado.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD04/notebooks/UD04_N11_diseno_sistema_robotizado.ipynb){:target="_blank"} |
<!-- AUTO:notebooks fin -->

## N05 · Ejercicios de OpenCV

Tres ejercicios de visión sobre imagen y vídeo: detectar **bordes** y enmarcarlos, detectar
**movimiento** entre fotogramas consecutivos y calcular el **flujo óptico**.

| Recurso | Enlace |
|---|---|
**Se entrega**: el notebook con los tres ejercicios resueltos y sus salidas.

## N06 · Navegar con cámara, por reglas

El robot tiene que **seguir una línea** en el suelo usando solo lo que ve su cámara. Aquí escribes
tú todas las condiciones: dónde está la línea en la imagen, y qué hacer en cada caso.

Dos escenarios: **línea simple** y **línea doble**.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_N06_navegar_camara.ipynb`](notebooks/UD04_N06_navegar_camara.ipynb) |
| Pistas | [1](notebooks/EX2_pista_1.png) · [2](notebooks/EX2_pista_2.png) · [3](notebooks/EX2_pista_3.png) · [4](notebooks/EX2_pista_4.png) · [5](notebooks/EX2_pista_5.png) · [6](notebooks/EX2_pista_6.png) |

**Se entrega**: el notebook con el controlador funcionando en los dos escenarios.

## N07 · Navegar con cámara, con lógica difusa

El **mismo problema** que `N06`, resuelto con lógica difusa: variables lingüísticas, funciones de
pertenencia, reglas y desfuzzificación. Enlaza directamente con la UD05.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_N07_navegar_camara_difusa.ipynb`](notebooks/UD04_N07_navegar_camara_difusa.ipynb) |
| Pistas | Las mismas seis de `N06` |

**Se entrega**: el notebook con el sistema difuso completo y el robot navegando en los dos
escenarios.

!!! tip "Compara antes de entregar"
    Ya has resuelto el mismo problema de dos formas. Antes de entregar, apunta en qué se diferencian
    el comportamiento de `N06` y el de `N07`: no cuál «va mejor», sino **cómo se mueve el robot** en
    cada caso, y por qué.

## N08 · Generar los datos de entrenamiento

Aquí no se entrena nada todavía: **conduces tú el robot** y el notebook graba lo que ve la cámara
junto con lo que tú decidiste hacer. El resultado es un conjunto de ejemplos etiquetados.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_N08_generar_datos_entrenamiento.ipynb`](notebooks/UD04_N08_generar_datos_entrenamiento.ipynb) |

**Se entrega**: el notebook **y el fichero `training_data.txt` con tu nombre**. Guárdatelo: es la
entrada de `N09`.

## N09 · Controlar el robot con una red neuronal

Lees el `training_data.txt` de `N08`, **construyes y entrenas** una red neuronal con esos ejemplos y
la usas para conducir el robot. Tres celdas están vacías a propósito: la arquitectura de la red, el
entrenamiento y la función de control.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_N09_red_neuronal.ipynb`](notebooks/UD04_N09_red_neuronal.ipynb) |

**Se entrega**: el notebook **y el fichero `.keras` con tu nombre**, con la red ya entrenada. Con ese
fichero, la celda de carga permite **probar cómo se comporta tu red sin repetir el entrenamiento**
—que es largo—, y es así como se corrige.

!!! note "Antes de entrenar hay que mirar los datos"
    La rúbrica puntúa `classifica_moviments` y el **balanceo**, y no es un capricho: conduciendo, un
    robot va hacia delante muchísimo más de lo que gira, así que el conjunto sale **desequilibrado**.
    Una red entrenada con esos datos aprende a ir recto siempre, que es lo que más acierta de media
    y lo que peor sigue la línea.

## N10 · Aprendizaje por refuerzo con NEAT

El mismo control, sin ejemplos. **NEAT** evoluciona a la vez los pesos **y la topología** de la red:
tú solo defines qué entra, qué sale y cómo se mide si lo está haciendo bien.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_N10_neat.ipynb`](notebooks/UD04_N10_neat.ipynb) |

**Se entrega**: el notebook y una **memoria en PDF** con tus pruebas variando `fitness_threshold` y
`pop_size`, la justificación de `num_inputs` y `num_outputs`, y una reflexión sobre el aprendizaje
por refuerzo. Es de **apto / no apto**: sin la memoria no cuenta como entregado.

!!! info "La rúbrica está en Moodle"
    La rúbrica de cada entrega se ve **en la propia tarea de Moodle**, y puedes leerla **antes** de
    empezar: ahí tienes los criterios, los niveles y lo que puntúa cada uno. No se duplica aquí para
    que no haya dos versiones del mismo dato.

---
[Volver a la UD04](UD04_ES.md) · [Notebooks guiados](UD04_ActividadesGuiadas.md) · [Notebook 4](notebooks/UD04_N04_cinematica_manipulador.ipynb) · [Notebook 11](notebooks/UD04_N11_diseno_sistema_robotizado.ipynb)
