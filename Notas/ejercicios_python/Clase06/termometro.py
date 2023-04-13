import random
import numpy as np


def medir_temp(n):
    lista = []
    for i in range(n):
        lista.append(random.normalvariate(37.5, 0.2))
    np.save('../Data/temperaturas', lista)
    return lista


def resumen_temp(n):
    lista = sorted(medir_temp(n))
    maximo = max(lista)
    minimo = min(lista)
    promedio = sum([a for a in lista])/n
    if len(lista) % 2 != 0:
        mediana = (lista[int((n-1)/2)] + lista[int((n+1)/2)])/2
        cuartil1 = (lista[int((n-1)/4)] + lista[int((n+1)/4)])/2
        cuartil3 = (lista[int(3*(n-1)/4)] + lista[int(3*(n+1)/4)])/2
    else:
        mediana = lista[int(n/2)]
        cuartil1 = lista[int(n/4)]
        cuartil3 = lista[int(3*n/4)]

    print(f'{maximo:0.2f}, {minimo:0.2f}, {promedio:0.2f}, {cuartil1:0.2f} {mediana:0.2f} {cuartil3:0.2f}')
    return (maximo, minimo, promedio, cuartil1, mediana, cuartil3)


# resumen_temp(100)
medir_temp(999)
