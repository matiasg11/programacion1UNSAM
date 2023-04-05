import random


def medir_temp(n):
    lista = []
    for i in range(n):
        lista.append(random.normalvariate(37.5, 0.2))
    return lista


def resumen_temp(n):
    lista = sorted(medir_temp(n))
    maximo = max(lista)
    minimo = min(lista)
    promedio = sum([a for a in lista])/n
    if len(lista) % 2 != 0:
        mediana = (lista[int((n-1)/2)] + lista[int((n+1)/2)])/2
    else:
        mediana = lista[int(n/2)]
    print(f'{maximo:0.2f}, {minimo:0.2f}, {promedio:0.2f}, {mediana:0.2f}')
    return (maximo, minimo, promedio, mediana)


resumen_temp(10)
