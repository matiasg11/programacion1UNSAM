import random
import numpy as np


# Cantidad de figuritas
n = 670

# Figuritas por paquete
m = 5

# Album


def crear_album(numero_figuritas):
    return np.zeros(numero_figuritas)


album = crear_album(n)


def album_incompleto(A):
    return (0 in A)


print(album_incompleto(album))
