import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


def crear_df(directorio, nombre_archivo):
    filename = os.path.join(directorio, nombre_archivo)
    return pd.read_csv(filename)


# Llamamos directorio a donde están guardados los archivos
directorio = "..\Data"
# Nombramos los archivos
path_veredas = "arbolado-publico-lineal-2017-2018.csv"
path_parques = "arbolado-en-espacios-verdes.csv"

# #Creamos el path entero hasta los archivos
# file_veredas = os.path.join(directorio, path_veredas)
# file_parques = os.path.join(directorio, path_parques)

# Creamos los data frames leyendo los archivos csv
# df_veredas = pd.read_csv(file_veredas)
# df_parques = pd.read_csv(file_parques)

# Esto no se hace porque usamos la función que definimos más arriba

# Creamos los dataframes leyendo los archivos con la funcion creada
df_parques = crear_df(directorio, path_parques)
df_veredas = crear_df(directorio, path_veredas)

# Usamos las columnas que nos importan
columnas_veredas = ["nombre_cientifico", "diametro_altura_pecho", "altura_arbol"]
columnas_parques = ["nombre_cie", "diametro", "altura_tot"]


def filtrar_arbol(dataframe, lista_especies, columna_nombre):
    return dataframe[dataframe[columna_nombre].isin(lista_especies)].copy()


# Filtrar por tipo de arbol que esté en la lista
df_tipas_veredas = filtrar_arbol(df_veredas, ["Tipuana tipu"], "nombre_cientifico")
df_tipas_parques = filtrar_arbol(df_parques, ["Tipuana Tipu"], "nombre_cie")

# Filtrar por columnas que estén en la lista de columnas
df_tipas_veredas = df_tipas_veredas[columnas_veredas]
df_tipas_parques = df_tipas_parques[columnas_parques]

df_tipas_veredas = df_tipas_veredas.rename(
    columns={
        "nombre_cientifico": "nombre",
        "diametro_altura_pecho": "diametro",
        "altura_arbol": "altura",
    }
)
df_tipas_parques = df_tipas_parques.rename(
    columns={"nombre_cie": "nombre", "altura_tot": "altura"}
)

df_tipas_parques["ambiente"] = "parque"
df_tipas_veredas["ambiente"] = "vereda"

df_tipas = pd.concat([df_tipas_parques, df_tipas_veredas]).copy()

df_tipas.boxplot("diametro", by="ambiente")
plt.show()

df_tipas.boxplot("altura", by="ambiente")
plt.show()
