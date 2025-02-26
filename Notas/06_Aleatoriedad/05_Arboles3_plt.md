[Contenidos](../Contenidos.md) \| [Anterior (4 Introducción a matplotlib)](04_Intro_mpl.md) \| [Próximo (6 Cierre de la clase)](06_Cierre.md)

# 6.5 Gráficos del Arbolado porteño

## Ploteando datos reales

En esta sección retomamos el dataset del arbolado porteño (arbolado-en-espacios-verdes.csv) para hacer algunos gráficos que nos permitan visualizar los datos. Te damos una guía muy elemental sobre cómo hacer esto y un par de punteros a la documentación oficial. Ya esperamos que empieces a poder buscar por tu cuenta la info que falte.

Seguiremos trabajando en el archivo `arboles.py`. Nos basaremos en el trabajo hecho con comprensión de listas la clase pasada. Los siguientes tres ejercicios hacelos dentro de tres funciones diferentes, guardalas y entregá el archivo `arboles.py` con estos agregados.

### Ejercicio 6.10: Histograma de altos de Jacarandás
Usando tu trabajo en el [Ejercicio 5.16](../05_Listas/05_Arboles2_LC.md#ejercicio-516-lista-de-altos-de-jacaranda), generá un histograma con las alturas de los Jacarandás en el dataset.

Tu código debería verse similar a este:

```python
import os
import matplotlib.pyplot as plt
os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
altos = [comprensión de listas]
plt.hist(altos,bins=...)
```

_Observación:_ Spyder tiene opciones para mostrar las figuras dentro de la misma ventana o en una ventana nueva (Tools -> Preferences -> IPython console -> Graphics -> Backend). Te recomendamos generarlas en una ventana nueva. Luego, con `plt.clf()` podés borrar la figura actual y con `plt.figure()` generás una nueva figura por si querés dejar varias abiertas a la vez.

### Ejercicio 6.11: Scatterplot (diámetro vs alto) de Jacarandás
En este ejercicio introducimos un nuevo tipo de gráfico: _el gráfico de dispersión_  o _scatterplot_. El mismo usa coordenadas cartesianas para mostrar los valores de dos variables para un conjunto de datos. 

En este caso vamos a graficar un punto en el plano (x,y) por cada árbol en el dataset (o para cada árbol de cierta especie). El punto correspondiente a un árbol con diámetro *d* y altura *h* será ubicado en la posición *x=d* e *y=h*. Este tipo de gráfico permite visualizar relaciones o tendencias entre las variables y es muy útil en el análisis exploratorio de datos.

Escribí una función `scatter_hd(lista_de_pares)` que a partir de una lista de pares como la que generaste en el [Ejercicio 5.17](../05_Listas/05_Arboles2_LC.md#ejercicio-517-lista-de-altos-y-diametros-de-jacaranda) genere un scatterplot para visualizar la relación entre altura y diámetro de los Jacarandás del dataset.

Ayuda: si ya tenés una lista o un vector *d* con diámetros y otra *h* con altos, es sencillo hacer un primer scatterplot:

```python
import matplotlib.pyplot as plt
plt.scatter(d,h)
```

Algunas recomendaciones:

1. Convertí la lista generada en un `ndarray` de `numpy`, de esa forma podés usar rebanadas para obtener un vector *d* con diámteros y otro *h* con alturas inmediatamente.
2. Mirá algun ejemplo como [este](https://matplotlib.org/stable/gallery/shapes_and_collections/scatter.html#sphx-glr-gallery-shapes-and-collections-scatter-py) y tratá de entender cómo se usan los parámetros opcionales *s* (de size, tamaño) y *c* (de color) y *alpha* (de transparencia) de la función [matplotlib.pyplot.scatter](https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter). 
3. Usando el parámetro *alpha* hacé que el gráfico permita visualizar dónde hay mayor densidad de datos.

¿Ves alguna relación entre el diámetro y el alto de los Jacarndás? ¿Te parece que es una relación lineal o de otro tipo?

Agregale nombres a los ejes y a la figura usando los siguientes comandos:
```python
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
```

### Ejercicio 6.12: Scatterplot para diferentes especies
Ahora vamos a usar la función `medidas_de_especies()` definida en el [Ejercicio 5.18](../05_Listas/05_Arboles2_LC.md#ejercicio-518-diccionario-con-medidas).

Comenzando con éste código, hacé tres gráficos como en el ejercicio anterior, uno por cada especie.

```python
import os
import matplotlib.pyplot as plt

os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)
```

¿Se mantienen las relaciones que viste en el ejercicio anterior para las tres especies? ¿Hay diferencias entre las especies? Para un mismo alto, ¿cuál tiene mayor diámetro (típicamente)?

Para poder comparar diferentes especies resulta conveniente fijar los límites en los ejes *x* e *y* en las diferentes figuras usando las funciones `xlim()` e  `ylim()`. A continuación un ejemplo:
```python
plt.xlim(0,30) 
plt.ylim(0,100) 
```

Acordate siempre de ponerle título a las figuras y nombres y unidades a los ejes. Guardá los últimos tres ejercicios dentro de tres funciones diferentes en tu archivo `arboles.py`. Te pediremos que lo entregues en la próxima página.

_Extra:_ ¿podés hacer un solo gráfico que muestre dos de estas tres especies en diferentes colores y resulte claro? ¿Y las tres especies?


[Contenidos](../Contenidos.md) \| [Anterior (4 Introducción a matplotlib)](04_Intro_mpl.md) \| [Próximo (6 Cierre de la clase)](06_Cierre.md)

