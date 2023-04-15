import csv
import os
import matplotlib.pyplot as plt
import numpy as np


def leer_arboles(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        # print(headers)
        arboleda = []
        for i, row in enumerate(rows, start=1):
            try:
                record = dict(zip(headers, row))
                arboleda.append(record)
            except ValueError:
                print('Faltan datos en la línea', i, "del archivo")
        return arboleda


# %% Todos los árboles
# lista_alturas_tot = [float(s['altura_tot']) for s in arboleda]
# altura_total_todos = sum([altura for altura in lista_alturas_tot])
# altura_prom = altura_total_todos/len(lista_alturas_tot)


# %% Solo los Jacaranda y alturas
# lista_alturas_jacaranda = [float(arbol['altura_tot'])
#                            for arbol in arboleda if arbol['nombre_com'] == "Jacarandá"]
# cantidad_jacaranda = len(lista_alturas_jacaranda)
# altura_total_jacaranda = sum([altura for altura in lista_alturas_jacaranda])
# alt_prom_jacaranda = altura_total_jacaranda/cantidad_jacaranda

# %% Jacarandá: Alturas y diámetros
# lista_jacaranda = [(float(arbol['altura_tot']), float(arbol['diametro']))
#                    for arbol in arboleda if arbol['nombre_com'] == "Jacarandá"]

# print(len(lista_jacaranda))
# for i in range(-5, 0):
#     print(lista_jacaranda[i])

# %% 5.18 Diccionario con medidas para 3 especies
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']


def altura_y_diametro(lista_arboles, especie):
    lista_filtrada = [(float(arbol['altura_tot']), float(arbol['diametro']))
                      for arbol in lista_arboles if arbol['nombre_com'] == especie]

    return lista_filtrada


# diccionario_especies = {especie: altura_y_diametro(
#     arboleda, especie) for especie in especies}

# Debugger
# for especie in especies:
#     print(len(diccionario_especies[especie]))

arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
altos = [(float(arbol['altura_tot']))
         for arbol in arboleda if arbol['nombre_com'] == "Jacarandá"]
diametros = [(float(arbol['diametro']))
             for arbol in arboleda if arbol['nombre_com'] == "Jacarandá"]

hyd2 = altura_y_diametro(arboleda, "Jacarandá")
hyd = [(altos[i], diametros[i]) for i in range(0, len(altos))]

# plt.hist(altos, bins=25)
# plt.ylabel("Cantidad (árboles)")
# plt.xlabel("Alto (m)")
# plt.title("Histograma de alturas para Jacarandás")
# plt.show()

# print(hyd == hyd2)


def crear_ejes(lista_de_pares):
    x_y = np.array(lista_de_pares)
    x = x_y[:, 0]
    y = x_y[:, 1]
    return x, y


def scatter_hd(lista_de_pares):
    h, d = crear_ejes(lista_de_pares)
    plt.xlabel("Diametro (cm)")
    plt.ylabel("Alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.xlim(0, 100)
    plt.ylim(0, 30)
    plt.scatter(d, h, c="b", alpha=0.5)
    plt.show()


# scatter_hd(hyd)

# %%

def medidas_de_especies(especies, arboleda):
    colors = ["r", "g", "y"]
    for especie in especies:
        alt_diam = altura_y_diametro(arboleda, especie)
        y, x = crear_ejes(alt_diam)
        plt.scatter(x, y, alpha=(0.35-0.15*(especies.index(especie))), label=especie,
                    color=colors[(especies.index(especie))])


medidas_de_especies(especies, arboleda)
plt.xlabel("Diametro (cm)")
plt.ylabel("Alto (m)")
plt.title("Relación diámetro-alto para Eucaliptos, Palos Borrachos yJacarandás")
plt.xlim(0, 200)
plt.ylim(0, 50)
plt.legend()
plt.show()
