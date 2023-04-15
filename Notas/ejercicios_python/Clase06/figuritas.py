import random
import numpy as np


# Cantidad de figuritas
n = 670

# Figuritas por paquete
m = 5

# Album


def crear_album(numero_figuritas):
    return np.zeros(numero_figuritas)


# album = crear_album(n)


def album_incompleto(A):
    return (0 in A)


def comprar_figu(figus_total):
    return random.randint(1, figus_total)


def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    compradas = 0
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu-1] += 1
        compradas += 1
    # print(compradas)
    return compradas


# cuantas_figus(n)
n_repeticiones = 1000
resultados = [cuantas_figus(6) for i in range(n_repeticiones)]
# for i in range(n_repeticiones):
#     resultados.append(cuantas_figus(6))

resultados = np.array(resultados)
print(np.mean(resultados))
