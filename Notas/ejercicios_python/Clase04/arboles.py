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
    # print(count)
    return lista


lista_arboles = leer_parque(
    '../Data/arbolado-en-espacios-verdes.csv', "GENERAL PAZ")


def especies(lista_arboles):
    lista_especies = []
    for arbol in lista_arboles:
        lista_especies.append(arbol["nombre_com"])

    dict_especies = set(lista_especies)
    # print((dict_especies))
    return dict_especies


especies(lista_arboles)


def contar_ejemplares(lista_arboles):
    total_por_especie = Counter()
    lista_especies = especies(lista_arboles)
    for nombre in lista_especies:
        for arbol in lista_arboles:
            if arbol["nombre_com"] == nombre:
                total_por_especie[nombre] += 1

    # print(total_por_especie)
    return total_por_especie


contar_ejemplares(lista_arboles)

parques = ["GENERAL PAZ", "ANDES, LOS", "CENTENARIO"]
archivo = "../Data/arbolado-en-espacios-verdes.csv"


def mas_comunes_en_parque(parques, archivo):
    print('%25s %25s %25s' % tuple(parques))
    print(f'{"":-<25s} {"":-<25s} {"":-<25s}')
    lista_ejemplares = []
    for parque in parques:
        lista_arb = leer_parque(archivo, parque)
        ejemplares = contar_ejemplares(lista_arb)
        lista_ejemplares.append(ejemplares.most_common(5))
    # print(lista_ejemplares)

    ordenada = []
    for i in range(0, 5):
        sub = []
        for j in range(0, 3):
            sub.append((lista_ejemplares[j][i][0], lista_ejemplares[j][i][1]))
        ordenada.append(sub)

    for i in range(len(ordenada)):
        renglon = []
        for m in range(len(ordenada[i])):
            for g in range(0, 2):
                renglon.append(ordenada[i][m][g])
        print('%25s:%3d|%25s:%3d|%25s:%3d' % tuple(renglon))
    # print(renglon)


mas_comunes_en_parque(parques, archivo)
