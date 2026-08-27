# UD05 · Entregas

!!! important "Seis entregas en el RA5"
    A los cinco sistemas de esta página se suma **`N10`**, simular un sistema experto, que también se
    entrega. Cuatro tienen dominio fijo (`N11`-`N14`) y `N15` es de **libre elección**: los tres
    dominios distintos son a propósito, porque el criterio RA5-b pide representar y simular sistemas
    «de muy diversos ámbitos».

    | Actividad | Régimen |
    |---|---|
    | [`N10` Simular un sistema experto](notebooks/UD05_N10_simular_sistema_experto.ipynb) | Entrega evaluable |
    | [`N11` Detectar lesiones de rodilla](notebooks/UD05_N11_lesiones_rodilla.ipynb) | Entrega evaluable |
    | [`N12` Previsión del valor de mercado](notebooks/UD05_N12_valor_mercado_jugadores.ipynb) | Entrega evaluable |
    | [`N13` Centrocampistas con potencial](notebooks/UD05_N13_centrocampistas_jovenes.ipynb) | Entrega evaluable |
    | [`N14` Simulador de quemador de gas](notebooks/UD05_N14_quemador_gas.ipynb) | Entrega evaluable |
    | [`N15` Sistema experto de libre elección](notebooks/UD05_N15_sistema_experto_libre.ipynb) | Entrega evaluable |

    **No se promedian a partes iguales**: cada entrega tiene su propio peso, y lo tienes en el libro
    de calificaciones de Moodle.
!!! note "`N12` y `N13` comparten el mismo fichero de datos"
    Descarga `EX2.-players_22.csv` una vez y súbelo a la carpeta de archivos de Colab (o colócalo
    junto al notebook si trabajas en local) antes de ejecutar cualquiera de los dos.

!!! info "La rúbrica está en Moodle"
    La rúbrica de cada entrega se ve **en la propia tarea de Moodle**, y puedes leerla **antes** de
    empezar: ahí tienes los criterios, los niveles y lo que puntúa cada uno. No se duplica aquí para
    que no haya dos versiones del mismo dato.

<!-- AUTO:notebooks inicio -->
| Notebook | Qué es | Descargar | Abrir en Colab |
|---|---|---|---|
| [`N10` · Simular un sistema experto con experta](notebooks/UD05_N10_simular_sistema_experto.ipynb) | Motor de inferencia a mano · diagnóstico frente a clasificación | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N10_simular_sistema_experto.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N10_simular_sistema_experto.ipynb){:target="_blank"} |
| [`N11` · Detectar lesiones de rodilla](notebooks/UD05_N11_lesiones_rodilla.ipynb) | Medicina · sistema experto de diagnóstico | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N11_lesiones_rodilla.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N11_lesiones_rodilla.ipynb){:target="_blank"} |
| [`N12` · Previsión del valor de mercado de jugadores](notebooks/UD05_N12_valor_mercado_jugadores.ipynb) | Deporte · sistema híbrido reglas + aprendizaje (§7) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N12_valor_mercado_jugadores.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N12_valor_mercado_jugadores.ipynb){:target="_blank"} |
| [`N13` · Centrocampistas jóvenes con potencial](notebooks/UD05_N13_centrocampistas_jovenes.ipynb) | Deporte · lógica difusa sobre datos reales del FIFA 22 (§8) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N13_centrocampistas_jovenes.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N13_centrocampistas_jovenes.ipynb){:target="_blank"} |
| [`N14` · Simulador de quemador de gas](notebooks/UD05_N14_quemador_gas.ipynb) | Industria · control de un proceso real (§10-11) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N14_quemador_gas.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N14_quemador_gas.ipynb){:target="_blank"} |
| [`N15` · Sistema experto de libre elección](notebooks/UD05_N15_sistema_experto_libre.ipynb) | El dominio que tú elijas · «muy diversos ámbitos» (CE b) | [![Descargar](https://img.shields.io/badge/Descargar-.ipynb-blue?logo=jupyter)](https://raw.githubusercontent.com/martinezpenya/ModelosIA/main/docs/UD05/notebooks/UD05_N15_sistema_experto_libre.ipynb){:target="_blank"} | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/martinezpenya/ModelosIA/blob/main/docs/UD05/notebooks/UD05_N15_sistema_experto_libre.ipynb){:target="_blank"} |
<!-- AUTO:notebooks fin -->

## N10 · Simular un sistema experto

Construir un sistema experto que **diagnostique** un problema y compararlo con uno de
**clasificación**, para ver que un mismo motor simula comportamientos de ámbitos distintos (CE b).

**Se entrega**: el notebook con los dos sistemas funcionando y la comparación entre ambos.

## N11 · Detectar lesiones de rodilla

Sistema experto de **diagnóstico médico**: a partir de los síntomas, distinguir entre las lesiones
de rodilla más comunes —ligamento cruzado, menisco, esguince—.

**Se entrega**: el notebook con el sistema resolviendo los casos de prueba y las reglas justificadas.

## N12 · Previsión del valor de mercado de jugadores

Sistema **híbrido**: reglas escritas a mano sobre la salida de un modelo de aprendizaje
automático, para prever el valor de mercado de jugadores emergentes (§7).

**Se entrega**: el notebook con el sistema híbrido funcionando sobre los datos del FIFA 22.

## N13 · Centrocampistas jóvenes con potencial

Sistema experto con **lógica difusa** para detectar centrocampistas jóvenes con buen potencial,
partiendo del trabajo publicado de Luka Radovanović (§8).

**Se entrega**: el notebook con las variables difusas, las reglas y los jugadores detectados.

## N14 · Simulador de quemador de gas

**Control de un proceso industrial**: un quemador con sensor de temperatura y un actuador que
regula el gas, con el objetivo de mantener la consigna (§10-11).

**Se entrega**: el notebook con el controlador y la respuesta del sistema medida.

## N15 · Sistema experto de libre elección

Un sistema basado en reglas del **dominio que tú elijas**. Es la entrega que cubre el «muy diversos
ámbitos» del CE b: cada alumno trae un dominio distinto.

**Se entrega**: el notebook y una memoria con la descripción del sistema, el esquema del conocimiento integrado
y los casos de prueba.

---
[Volver a la UD05](UD05_ES.md) · [Ejercicios](UD05_Ejercicios.md) · [Notebook 10](notebooks/UD05_N10_simular_sistema_experto.ipynb) · [Notebook 5](notebooks/UD05_N05_logica_difusa_propinas.ipynb) · [Notebook 8](notebooks/UD05_N08_controlador_experto.ipynb) ·
[Notebooks guiados](UD05_ActividadesGuiadas.md)
