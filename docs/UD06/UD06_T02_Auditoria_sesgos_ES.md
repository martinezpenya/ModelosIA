# UD06 · Taller 2 — Auditoría de sesgos con Fairlearn

!!! important "Entregable · cuenta en el 40 % de actividades del RA6"
    Se trabaja en la sesión 3, con el notebook [N01](notebooks/UD06_N01_sesgos_ia.ipynb) abierto. Se
    entrega en Moodle un informe con las métricas obtenidas y las respuestas de la Fase 6.

**Objetivo**: medir el sesgo de un modelo real con **Fairlearn**, mitigarlo y **comprobar el precio
que se paga** por hacerlo (RA6-f, con conexión a RA6-b y RA6-e).

!!! note "Todo el código de este taller está ejecutado"
    Las cifras que verás abajo son las que salen de verdad al ejecutarlo con `fairlearn 0.14.0`,
    `scikit-learn 1.9.0` y `pandas 3.0.5`. Si tus números difieren un poco, revisa las versiones: no
    revises tu razonamiento.

### Fase 1 — Prepara el entorno y carga los datos

Usaremos el conjunto **UCI Adult** (48.842 filas), que predice si una persona gana más de 50 000 $ al
año a partir de datos demográficos y laborales. Fairlearn lo trae ya empaquetado, así que **no hay
que descargar nada a mano**.

```bash
pip install fairlearn scikit-learn pandas
```

```python
import pandas as pd
from fairlearn.datasets import fetch_adult

datos = fetch_adult(as_frame=True)

# Quitamos «sex» de las características: no queremos que el modelo la use para decidir…
X = datos.data.drop(columns=["sex"])
y = (datos.target == ">50K").astype(int)
# …pero la conservamos aparte, porque SIN ella no se puede auditar (§9.2)
sexo = datos.data["sex"]

print("filas:", len(X), "| columnas:", len(X.columns))
print(sexo.value_counts().to_dict())
```

```text
filas: 48842 | columnas: 13
{'Male': 32650, 'Female': 16192}
```

!!! tip "La primera lección aparece antes de entrenar"
    Fíjate en lo que acabas de hacer: **has quitado el sexo de las características y lo has guardado
    aparte**. Eso no es un truco: es la única forma de auditar. Si borras el atributo del todo
    —«equidad por desconocimiento», §9.2— pierdes la capacidad de comprobar si discriminas. Y eso
    choca de frente con la minimización del RGPD: es la **paradoja de los sesgos** del §9.8, en la
    primera celda del taller.

Antes de seguir, mide las **tasas base** de cada grupo, porque de eso depende todo lo demás:

```python
print(y.groupby(sexo, observed=True).mean().round(4).to_dict())
```

```text
{'Female': 0.1093, 'Male': 0.3038}
```

!!! important "Anota este dato"
    **El 10,93 % de las mujeres del conjunto gana más de 50 000 $, frente al 30,38 % de los hombres.**
    Las tasas base son **muy distintas**, y esa es exactamente la condición del resultado de
    imposibilidad de **Kleinberg et al. (2016)** (§9.4). Recuérdalo en la Fase 5, cuando veas que no
    puedes arreglarlo todo a la vez.

### Fase 2 — Entrena un modelo

```python
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

categoricas = X.select_dtypes(include=["category", "object"]).columns.tolist()
prep = ColumnTransformer(
    [("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categoricas)],
    remainder="passthrough")
modelo = Pipeline([("prep", prep),
                   ("clf", HistGradientBoostingClassifier(random_state=42))])

X_tr, X_te, y_tr, y_te, s_tr, s_te = train_test_split(
    X, y, sexo, test_size=0.3, random_state=42, stratify=y)

modelo.fit(X_tr, y_tr)
pred = modelo.predict(X_te)
```

!!! warning "`sparse_output=False` no es opcional"
    `HistGradientBoostingClassifier` **no acepta matrices dispersas**. Si dejas el
    `OneHotEncoder` por defecto, el `fit` revienta con
    `TypeError: Sparse data was passed for X, but dense data is required`. Es el fallo más habitual
    de este taller.

### Fase 3 — Mide la equidad

```python
from sklearn.metrics import accuracy_score
from fairlearn.metrics import (MetricFrame, demographic_parity_difference,
                               equalized_odds_difference, selection_rate)

print("exactitud global:", round(accuracy_score(y_te, pred), 4))
print("paridad demográfica (dif):",
      round(demographic_parity_difference(y_te, pred, sensitive_features=s_te), 4))
print("igualdad de oportunidades (dif):",
      round(equalized_odds_difference(y_te, pred, sensitive_features=s_te), 4))
```

```text
exactitud global: 0.8753
paridad demográfica (dif): 0.1687
igualdad de oportunidades (dif): 0.0731
```

- **Diferencia ≈ 0** significa que la métrica se cumple entre grupos.
- **Paridad demográfica 0,1687**: hay **17 puntos** de diferencia en la tasa de selección. Mucho.
- **Igualdad de oportunidades 0,0731**: 7 puntos. Menos, pero no cero.

### Fase 4 — Compara por grupo (y desconfía de la métrica global)

```python
mf = MetricFrame(
    metrics={"exactitud": accuracy_score, "tasa de selección": selection_rate},
    y_true=y_te, y_pred=pred, sensitive_features=s_te)
print(mf.by_group)
```

```text
        exactitud  tasa de selección
sex
Female   0.935763           0.085032
Male     0.845345           0.253777
```

!!! important "Aquí está el corazón del taller"
    La exactitud global era 0,8753, un número respetable. Pero por grupo:

    - El modelo acierta **más** con las mujeres (0,9358) que con los hombres (0,8453). ¿Es que
      funciona mejor para ellas? **No.** Acierta más porque solo el 10,93 % de las mujeres son
      positivas, así que **decir «no» casi siempre ya acierta**. La exactitud es una métrica
      tramposa con clases desequilibradas.
    - La **tasa de selección** es del **8,5 % para las mujeres y del 25,4 % para los hombres**: el
      modelo propone a un hombre para el grupo de altos ingresos **tres veces más a menudo**.

    Una sola cifra global habría ocultado las dos cosas. Esto es, en la práctica, lo que enseña la
    **paradoja de Simpson** (§9.5) y por qué el checklist del §9.7 insiste en **medir por subgrupo**.

### Fase 5 — Mitiga el sesgo y mide el precio

`ThresholdOptimizer` ajusta **un umbral distinto por grupo** para forzar la métrica que le pidas. Es
mitigación de **postprocesado**: no toca los datos ni reentrena el modelo.

```python
from fairlearn.postprocessing import ThresholdOptimizer

opt = ThresholdOptimizer(estimator=modelo, constraints="equalized_odds",
                         predict_method="predict_proba", prefit=True)
opt.fit(X_tr, y_tr, sensitive_features=s_tr)
pred_opt = opt.predict(X_te, sensitive_features=s_te, random_state=42)

print("exactitud global:", round(accuracy_score(y_te, pred_opt), 4))
print("igualdad de oportunidades (dif):",
      round(equalized_odds_difference(y_te, pred_opt, sensitive_features=s_te), 4))
print("paridad demográfica (dif):",
      round(demographic_parity_difference(y_te, pred_opt, sensitive_features=s_te), 4))

mf2 = MetricFrame(
    metrics={"exactitud": accuracy_score, "tasa de selección": selection_rate},
    y_true=y_te, y_pred=pred_opt, sensitive_features=s_te)
print(mf2.by_group)
```

```text
exactitud global: 0.8611
igualdad de oportunidades (dif): 0.0014
paridad demográfica (dif): 0.095
        exactitud  tasa de selección
sex
Female   0.910850           0.101709
Male     0.836464           0.196713
```

Rellena esta tabla en tu informe con **tus** números:

| Métrica | Antes | Después | ¿Mejoró? |
|---|---|---|---|
| Exactitud global | 0,8753 | 0,8611 | |
| Igualdad de oportunidades (dif) | 0,0731 | 0,0014 | |
| Paridad demográfica (dif) | 0,1687 | 0,0950 | |
| Tasa de selección · mujeres | 0,0850 | 0,1017 | |
| Tasa de selección · hombres | 0,2538 | 0,1967 | |

!!! important "Las tres cosas que hay que ver en esta tabla"
    1. **La igualdad de oportunidades se ha resuelto**: de 0,0731 a **0,0014**, prácticamente cero.
       Es lo que le pedimos con `constraints="equalized_odds"`, y lo cumple.
    2. **Se paga un precio**: la exactitud global baja de 0,8753 a **0,8611**, 1,4 puntos. No es
       gratis, y hay que poder justificar ese coste ante quien paga el sistema.
    3. **La paradoja demográfica NO se ha resuelto**: mejora de 0,1687 a 0,0950, pero sigue lejos de
       cero. **Y no es un fallo de la herramienta.** Las tasas base son 10,93 % y 30,38 % (Fase 1),
       así que por **Kleinberg et al. (2016)** no puedes tener a la vez calibración e igualdad de
       oportunidades, y forzar la igualdad de oportunidades **no** te da paridad demográfica.

    Prueba a cambiar `constraints="demographic_parity"` y observa qué se rompe entonces. Eso es el
    ejercicio 79 hecho con datos.

### Fase 6 — Reflexión ética y normativa

Responde en el informe:

1. Has quitado `sex` de las características pero lo has usado para auditar. ¿Cómo justificarías ese
   tratamiento ante el principio de **minimización** del RGPD (§5.2)? ¿Qué base legal y qué plazo
   pondrías?
2. Si no pudieras tratar el sexo de ninguna manera, ¿cómo auditarías el modelo con **variables
   proxy** (§9.8)? Nombra dos columnas del conjunto que podrían servir y explica el riesgo de usarlas.
3. Este sistema, aplicado a selección de personal, ¿qué **nivel de riesgo** tendría en el AI Act y
   qué obligaciones concretas le tocarían (§6.1)?
4. Bajo la **Ley 15/2022**, si una candidata denuncia discriminación, ¿quién tiene que demostrar qué?
   ¿Qué documento de este taller usarías como prueba?
5. La exactitud bajó 1,4 puntos al mitigar. Redacta en **tres frases** cómo se lo explicarías a un
   responsable que solo mira la exactitud global.
6. Aplica una técnica del §8.2 a este conjunto de datos: si tuvieras que **publicarlo** para que otro
   centro replicara el estudio, ¿qué harías y por qué no basta con borrar el nombre?

### Entrega

Sube a Moodle un informe con la tabla de la Fase 5 rellena, la salida por grupo de la Fase 4 y las
seis respuestas de la Fase 6. Extensión orientativa: **dos o tres páginas**.

!!! note "Corrección"
    Las soluciones no se publican: se corrigen y comentan en clase.

---
[Volver a la UD06](UD06_ES.md) · [Ejercicios](UD06_Ejercicios.md) ·
[Taller 1](UD06_T01_Analisis_caso_etico_ES.md)
