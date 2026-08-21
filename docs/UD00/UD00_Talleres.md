# UD00 — Talleres

!!! important "Unidad no calificable, pero requisito"
    El Taller 1 se entrega y se marca como **hecho / no hecho**: no lleva nota, pero se tiene en
    cuenta y **es requisito para las prácticas de la UD02** (sin entorno funcionando no se puede
    hacer Robocode). Los viernes no hay clase: son el momento de recopilar capturas y redactar la
    memoria.

## Taller 1 · Verificación del entorno y primer contenedor

**Objetivo**: dejar Docker funcionando en **tu** máquina y demostrarlo con evidencias.

**Entrega**: una memoria en PDF con las capturas y las explicaciones de las seis fases. Se marca
como **hecho / no hecho**.

### Fase 1 — Instala Docker y demuéstralo

1. Instala Docker en tu equipo siguiendo el apartado 5.2 de la teoría (Ubuntu o Docker Desktop,
   según tu sistema).
2. Ejecuta y captura la salida de:

```bash
docker --version
docker run hello-world
```

!!! warning "El error más común del primer día"
    Si aparece `permission denied while trying to connect to the Docker daemon socket`, te falta
    añadir tu usuario al grupo `docker` **y cerrar y volver a abrir la sesión**. Explica en la
    memoria por qué hace falta reiniciar la sesión.

### Fase 2 — Primer contenedor interactivo

```bash
docker run -it --name mi-python python:3.12 bash
```

Dentro del contenedor:

```bash
python --version
python -c "print('Hola desde Docker')"
exit
```

Comprueba que el contenedor **sigue existiendo** aunque esté parado, y vuelve a entrar:

```bash
docker ps -a
docker start mi-python
docker attach mi-python
```

En la memoria: explica la diferencia entre `docker run`, `docker start` y `docker attach`.

### Fase 3 — Un servicio en segundo plano

```bash
docker run -d --name mi-nginx -p 8080:80 nginx
docker ps
```

Abre `http://localhost:8080` y captura la página de bienvenida. Después inventaría lo que llevas
acumulado:

```bash
docker images     # ¿cuántas imágenes y de qué tamaño?
docker ps -a      # ¿cuántos contenedores y en qué estado?
```

### Fase 4 — El mismo código en dos versiones de Python

Esta fase reproduce el caso del apartado 6.5 con tus propias manos:

```bash
# Contenedor A
docker run --rm python:3.9-slim bash -c \
  "pip install -q experta && python -c 'from experta import KnowledgeEngine; print(\"OK\")'"

# Contenedor B
docker run --rm python:3.12-slim bash -c \
  "pip install -q experta && python -c 'from experta import KnowledgeEngine; print(\"OK\")'"
```

Captura **las dos salidas** y responde en la memoria:

1. ¿Qué error exacto da el contenedor B y por qué?
2. ¿Qué versión de `experta` se ha instalado en cada caso? ¿Y de `frozendict`?
3. Si tuvieras que entregar hoy un proyecto con `experta`, ¿qué imagen base elegirías y por qué?

### Fase 5 — Elige una imagen y escribe su Compose

1. Elige una imagen del **anexo B** de la teoría (o cualquiera de [Docker Hub](https://hub.docker.com/)).
2. Comprueba que está **mantenida**: mira la fecha de la última actualización.
3. Escribe su `docker-compose.yml` con puertos y, si lo necesita, un volumen para sus datos.
4. Levántalo con `docker compose up -d` y captura el servicio funcionando en el navegador.

### Fase 6 — Volúmenes y limpieza

Crea en tu equipo una carpeta `practicas` con un `app.py`:

```python
print("Mi primera app en un contenedor")
```

Ejecútala **sin instalar Python en el host**:

```bash
cd practicas
docker run --rm -v "$PWD":/app -w /app python:3.12 python app.py
```

Y deja la máquina limpia:

```bash
docker compose down          # si dejaste el servicio de la fase 5
docker stop mi-nginx
docker rm mi-nginx mi-python
docker ps -a                 # ya no deben aparecer
```

### Entrega del Taller 1

Recopila las capturas y las explicaciones de las seis fases en **una memoria en PDF**. Se valora
que expliques lo que ocurre, no solo que pegues pantallazos: una captura sin explicación no
demuestra que hayas entendido nada.

| Fase | Evidencia mínima |
|---|---|
| 1 | `docker run hello-world` correcto |
| 2 | Contenedor interactivo, con la versión de Python impresa desde dentro |
| 3 | nginx respondiendo en el navegador + inventario de imágenes y contenedores |
| 4 | Las dos salidas del caso `experta` y el error del contenedor B |
| 5 | `docker-compose.yml` propio y su servicio funcionando |
| 6 | La app del host ejecutada en el contenedor y la máquina limpia |

## Taller 2 · Contenedor de prácticas de IA

**Objetivo**: levantar un entorno **Jupyter** reproducible con las bibliotecas del curso.

### Fase 1 — Estructura de trabajo

```
practicas/
└── docker/
    ├── docker-compose.yml
    └── requirements-ia.txt
```

### Fase 2 — `requirements-ia.txt`

```text
numpy
pandas
matplotlib
scikit-learn
scikit-fuzzy
nltk
spacy
torch
experta
```

### Fase 3 — `docker-compose.yml`

```yaml
services:
  jupyter:
    image: jupyter/scipy-notebook
    ports:
      - "8888:8888"
    volumes:
      - ./practicas:/home/jovyan/work
    environment:
      - JUPYTER_TOKEN=cursoia
```

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

Dentro de Jupyter, crea un notebook en la carpeta `work` y verifica las bibliotecas:

```python
import numpy, pandas, matplotlib, sklearn, skfuzzy
import nltk, spacy, torch
print("Entorno de IA listo:", numpy.__version__)
```

!!! tip "Nota para spacy"
    Algunos modelos de `spacy` se descargan aparte (`python -m spacy download es_core_news_sm`).
    Lo veremos en la UD03.

### Fase 6 — Gestiona el servicio

```bash
docker compose logs -f jupyter     # sigue los logs (Ctrl+C para salir)
docker compose exec jupyter bash   # entra dentro del contenedor en marcha
docker compose down                # detiene y elimina
```

### Fase 7 — Persistencia (volúmenes nombrados)

Modifica el `docker-compose.yml` para que la carpeta de Jupyter use un **volumen nombrado** y
comprueba que tus notebooks sobreviven a un `down` + `up`:

```yaml
services:
  jupyter:
    image: jupyter/scipy-notebook
    ports:
      - "8888:8888"
    volumes:
      - jupyter-work:/home/jovyan/work
    environment:
      - JUPYTER_TOKEN=cursoia

volumes:
  jupyter-work:
```

### Entrega

Sube a Moodle un informe breve con:

1. Captura de la **fase 5 de este taller** (Jupyter abierto con el import correcto).
2. Salida de `docker compose ps` mostrando el servicio activo.
3. Respuesta a: *¿por qué este entorno es reproducible en cualquier equipo?*
4. Captura de la **fase 7** mostrando que un notebook sobrevive a `docker compose down`.

!!! note "Soluciones"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD00](UD00_ES.md) · [Ejercicios](UD00_Ejercicios.md)
