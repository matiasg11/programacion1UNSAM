import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

directorio = "../Data"
archivo = "arbolado-publico-lineal-2017-2018.csv"
fname = os.path.join(directorio, archivo)
df = pd.read_csv(fname)

cols = ["nombre_cientifico", "ancho_acera", "diametro_altura_pecho", "altura_arbol"]

df_cols = df[cols].copy()
cantidad = df_cols["nombre_cientifico"].value_counts()
print(cantidad.iloc[0:10])

especies_seleccionadas = ["Tilia x moltkei", "Jacaranda mimosifolia", "Tipuana tipu"]
df_lineal_seleccion = df_cols[df_cols["nombre_cientifico"].isin(especies_seleccionadas)]

# df_lineal_seleccion.boxplot("diametro_altura_pecho", by="nombre_cientifico")
# plt.show()
# df_lineal_seleccion.boxplot("altura_arbol", by="nombre_cientifico")
# plt.show()

sns.pairplot(data=df_lineal_seleccion[cols], hue="nombre_cientifico")
