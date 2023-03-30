import csv
from collections import Counter


def leer_parque(nombre_archivo, parque):
    f = open(nombre_archivo, 'rt', encoding="utf-8")
    rows = csv.reader(f)
    headers = next(rows)
    idx = headers.index("espacio_ve")
    lista = []
    count = 0
    for i, row in enumerate(rows, start=1):
        if row[idx] == parque:
            record = {}
            try:
                record = dict(zip(headers, row))
                lista.append(record)
            except ValueError:
                print(f'Fila {i}: No pude interpretar: {row}')
            # Debugger
            #  print(record)
            count += 1
    print(count)
    return lista


lista_arboles = leer_parque(
    '../Data/arbolado-en-espacios-verdes.csv', "GENERAL PAZ")


def especies(lista_arboles):
    lista_especies = []
    for arbol in lista_arboles:
        lista_especies.append(arbol["nombre_com"])

    dict_especies = set(lista_especies)
    print((dict_especies))
    return dict_especies


especies(lista_arboles)


def contar_ejemplares(lista_arboles):
    total_por_especie = Counter()
    lista_especies = especies(lista_arboles)
    for nombre_com in lista_especies:
        total_por_especie[nombre_com] += 1

    print(total_por_especie)
    return total_por_especie


contar_ejemplares(lista_arboles)
