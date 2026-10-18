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

Dentro de **Jupyter**, crea un notebook en la carpeta `work` y verifica las bibliotecas:

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

Modifica el `docker-compose.yml` para que la carpeta de **Jupyter** use un **volumen nombrado** y
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
