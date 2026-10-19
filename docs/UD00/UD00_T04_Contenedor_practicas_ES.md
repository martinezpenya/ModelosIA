# UD00 · Taller 4 — Contenedor de prácticas de IA

!!! important "Entrega · hecho / no hecho"
    Se entrega en Aules y se califica como **hecho / no hecho**: se registra en el libro de
    calificaciones con **peso 0** —no puntúa, pero consta— y **es requisito**. Al terminar
    tendrás el **entorno del curso levantado**, que es el que usarás en el resto de las unidades. Sin él no se pueden hacer las prácticas de la UD02.

**Objetivo**: levantar un entorno **Jupyter** reproducible con las bibliotecas del curso.

### Fase 1 — Estructura de trabajo

```
practicas/
└── docker/
    ├── docker-compose.yml
    ├── requirements-ia.txt
    └── notebooks/          ← tus notebooks: créala tú antes de arrancar
```

### Fase 2 — `requirements-ia.txt`

```text
# torch en su versión solo CPU: sin las librerías de CUDA, varios GB menos de descarga
--extra-index-url https://download.pytorch.org/whl/cpu
numpy
pandas
matplotlib
scikit-learn
scikit-fuzzy
nltk
spacy
torch
```

!!! note "¿Y `experta`?"
    No va en este fichero: exige `frozendict==1.2`, y en esta imagen esa versión rompe el propio
    `conda`, que necesita la 2.x. Se instala aparte, sin dependencias, en la primera celda del notebook (fase 5) (lo explicamos
    en el apartado 6.5 de los apuntes).

### Fase 3 — `docker-compose.yml`

```yaml
services:
  jupyter:
    image: quay.io/jupyter/scipy-notebook
    ports:
      - "8888:8888"
    volumes:
      - ./notebooks:/home/jovyan/work
      - ./requirements-ia.txt:/home/jovyan/requirements-ia.txt:ro
    environment:
      - JUPYTER_TOKEN=cursoia
```

!!! warning "La imagen está en `quay.io`, no en Docker Hub"
    Las imágenes `jupyter/*` de Docker Hub dejaron de actualizarse en 2023: el proyecto Jupyter
    publica ahora en `quay.io/jupyter/…`. Escribe el nombre completo, con el prefijo `quay.io/`.

### Fase 4 — Verifica la configuración antes de arrancar

```bash
docker compose config
```

Comprueba que el puerto `8888:8888` y el token quedan resueltos correctamente.

### Fase 5 — Arranca Jupyter

```bash
docker compose up -d
docker compose ps
```

Abre en el navegador `http://localhost:8888` y usa el token `cursoia`.

??? failure "El contenedor se para nada más arrancar (`Exited (1)`)"
    Mira el motivo con `docker compose logs jupyter`. Si aparece un `tarfile.ReadError: empty file`
    o cualquier error al leer un fichero de `/opt/conda`, la imagen se descargó mal (descarga
    interrumpida o disco lleno). El fallo está en la imagen, no en tu `docker-compose.yml`: bórrala
    y descárgala de nuevo.

    ```bash
    docker compose down
    docker image rm quay.io/jupyter/scipy-notebook
    docker compose pull
    docker compose up -d
    ```

Dentro de Jupyter, crea un notebook en la carpeta `work`. La imagen ya trae numpy, pandas,
matplotlib y scikit-learn; el resto de bibliotecas del curso las instala la **primera celda**, a
partir del `requirements-ia.txt` que el compose monta en `/home/jovyan` (un nivel por encima de
`work`):

```python
%pip install -q -r ../requirements-ia.txt
%pip install -q --no-deps experta schema
```

La primera vez tarda unos minutos (torch y spacy pesan); si ya están instaladas, pip lo comprueba
en unos segundos. La segunda línea instala `experta` sin dejar que baje `frozendict` a la 1.2.
El aviso *«you may need to restart the kernel»* solo importa si alguna biblioteca ya estaba
importada antes de instalarla; en ese caso, *Kernel → Restart Kernel* y sigue.

En la siguiente celda, verifica las bibliotecas:

```python
import numpy, pandas, matplotlib, sklearn, skfuzzy
import nltk, spacy, torch, experta
print("Entorno de IA listo:", numpy.__version__)
```

!!! warning "Los paquetes viven en el contenedor, no en la imagen"
    Lo que instala `%pip` desaparece con `docker compose down`, porque el siguiente `up` crea un
    contenedor nuevo a partir de la imagen. Tus notebooks no se pierden (están en `notebooks/`):
    basta con volver a ejecutar la primera celda. `stop` y `start` no borran el contenedor y
    conservan lo instalado.

!!! tip "Nota para spacy"
    Algunos modelos de `spacy` se descargan aparte (`python -m spacy download es_core_news_sm`).
    Lo veremos en la UD03.

### Fase 6 — Gestiona el servicio

```bash
docker compose logs -f jupyter     # sigue los logs (Ctrl+C para salir)
docker compose exec jupyter bash   # entra dentro del contenedor en marcha
docker compose stop                # lo detiene sin borrarlo (conserva lo instalado)
docker compose start               # lo vuelve a arrancar
docker compose down                # detiene y elimina (hay que reinstalar los paquetes)
```

### Fase 7 — Persistencia (volúmenes nombrados)

Modifica el `docker-compose.yml` para que la carpeta de Jupyter use un **volumen nombrado** y
comprueba que tus notebooks sobreviven a un `down` + `up`:

```yaml
services:
  jupyter:
    image: quay.io/jupyter/scipy-notebook
    ports:
      - "8888:8888"
    volumes:
      - jupyter-work:/home/jovyan/work
      - ./requirements-ia.txt:/home/jovyan/requirements-ia.txt:ro
    environment:
      - JUPYTER_TOKEN=cursoia

volumes:
  jupyter-work:
```

<!-- AUTO:entrega inicio -->
## Entrega

Sube a la tarea **T04 · Contenedor de prácticas de IA** de Aules un único fichero **PDF** con:

- la memoria con las evidencias pedidas en el apartado «Entrega» (capturas de las fases 5 y 7, salida de `docker compose ps` y la respuesta razonada).

Aules **solo acepta un PDF** en esta tarea. El plazo acaba a las **23:59** del día que marca la tarea; después la tarea se cierra y ya no admite entregas.
<!-- AUTO:entrega fin -->

**Qué tiene que verse en la memoria**

1. Captura de la **fase 5 de este taller** (Jupyter abierto con el import correcto).
2. Salida de `docker compose ps` mostrando el servicio activo.
3. Respuesta a: *¿por qué este entorno es reproducible en cualquier equipo?*
4. Captura de la **fase 7** mostrando que un notebook sobrevive a `docker compose down`.

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD00](UD00_ES.md) · [Ejercicios](UD00_Ejercicios.md) · [Taller 3](UD00_T03_Verificacion_entorno_ES.md)
