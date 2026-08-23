# UD04 · Actividades guiadas

!!! info "Cómo se trabajan"
    Estos tres notebooks **no se entregan**: se hacen en clase, con el profesor, y son la
    preparación de los [seis entregables](UD04_ActividadesEntregables.md). Están ejecutados: puedes
    leerlos antes de tocar nada para ver qué hace cada celda.

!!! warning "Entorno"
    Los notebooks de robot móvil usan el simulador **AITK**, que funciona dentro del propio
    notebook. La primera celda de cada uno instala lo que hace falta:

    ```bash
    pip install aitk aitk.robots opencv-python-headless matplotlib numpy requests
    ```

    Funcionan igual en **Colab** y en el contenedor de prácticas de la UD00.

## 1 · Introducción a OpenCV

Visión por computador aplicada: cargar una imagen, detectar **bordes**, detectar **movimiento**
comparando fotogramas consecutivos y calcular el **flujo óptico**. Es la base de `EX1` y de todo lo
que viene después, porque la cámara es el único sensor del robot en esta unidad.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_N01_introduccion_opencv.ipynb`](notebooks/UD04_N01_introduccion_opencv.ipynb) |
| Imágenes de apoyo | [`1.-line.png`](notebooks/1.-line.png) · [`1.-line_left.png`](notebooks/1.-line_left.png) · [`1.-line_right.png`](notebooks/1.-line_right.png) |
| Vídeo de apoyo | [`1.-motionvideo.mp4`](notebooks/1.-motionvideo.mp4) |

## 2 · Vehículos de Braitenberg

El control más simple que existe: conectar un sensor directamente a un motor, sin representación
interna ni planificación. Con dos sensores y dos motores aparecen comportamientos que **parecen**
intencionados —perseguir la luz, huir de ella— sin que haya ninguna intención programada.

Es el punto de partida del §10.3: la técnica de programación más barata, contra la que comparar
todas las demás.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_N02_vehiculos_braitenberg.ipynb`](notebooks/UD04_N02_vehiculos_braitenberg.ipynb) |

## 3 · Ejemplos de robots en AITK

Recorrido por los robots del simulador: qué sensores puede llevar cada uno, cómo se define un mundo
con obstáculos y cómo se le pasa una función de control. Es el notebook que hay que tener a mano
mientras se hacen `EX2` a `EX6`.

| Recurso | Enlace |
|---|---|
| Notebook | [`UD04_N03_ejemplos_robots.ipynb`](notebooks/UD04_N03_ejemplos_robots.ipynb) |

---
[Volver a la UD04](UD04_ES.md) · [Entregables](UD04_ActividadesEntregables.md)
