import matplotlib.pyplot as plt
from bbin import busqueda_binaria_comps
from bbin import busqueda_secuencial_comps
import random
import numpy as np


def generar_lista(n, m):
    l = random.sample(range(m), k=n)
    l.sort()
    return l


def generar_elemento(m):
    return random.randint(0, m-1)


def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_comps(lista, x)[1]

    comps_prom = comps_tot / k
    return comps_prom


def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_comps(lista, x)[1]

    comps_prom = comps_tot / k
    return comps_prom

# print(experimento_secuencial_promedio(lista, m, k))


n = 100
m = 1000
k = 1000


def datos_secuencial(cant_datos):
    largos = np.arange(cant_datos) + 1
    comps_promedio = np.zeros(cant_datos)
    for i, n in enumerate(largos):
        lista = generar_lista(n, m)  # genero lista de largo n
        comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)
    return largos, comps_promedio


def datos_binaria(cant_datos):
    largos = np.arange(cant_datos) + 1
    comps_promedio = np.zeros(cant_datos)
    for i, n in enumerate(largos):
        lista = generar_lista(n, m)  # genero lista de largo n
        comps_promedio[i] = experimento_binario_promedio(lista, m, k)
    return largos, comps_promedio


def graficar_bbin_vs_bseq(m, k):
    secuencial = datos_secuencial(256)
    binaria = datos_binaria(256)
    plt.plot(secuencial[0], secuencial[1], label='Búsqueda Secuencial')
    plt.plot(binaria[0], binaria[1], label='Búsqueda Binaria')

    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.ylim(0, 20)
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()


graficar_bbin_vs_bseq(m, k)
