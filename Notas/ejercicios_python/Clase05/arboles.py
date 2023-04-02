import csv


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


arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
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


diccionario_especies = {especie: altura_y_diametro(
    arboleda, especie) for especie in especies}

# Debugger
for especie in especies:
    print(len(diccionario_especies[especie]))
