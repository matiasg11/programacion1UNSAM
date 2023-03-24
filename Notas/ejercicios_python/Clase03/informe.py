import csv


def leer_camion(nombre_archivo):
    with open(nombre_archivo, "rt") as f:
        rows = csv.reader(f)
        headers = next(rows)
        camion = []
        for i, row in enumerate(rows):
            try:
                ncajones = int(row[1])
                precio = float(row[2])
                camion.append((row[0], ncajones, precio))
            except ValueError:
                print('Faltan datos en la línea', i, "del archivo")
        return camion


este_camion = leer_camion("../Data/camion.csv")
# [('Lima', 100, 32.2), ('Naranja', 50, 91.1), ('Caqui', 150, 103.44), ('Mandarina', 200, 51.23), ('Durazno', 95, 40.37), ('Mandarina', 50, 65.1), ('Naranja', 100, 70.44)]

#
#
# def costo_camion(nombre_archivo):
#     f = open(nombre_archivo, 'rt')
#     rows = csv.reader(f)
#     headers = next(rows)
#     costo_total = 0
#     for row in rows:
#         try:
#             costo_total = costo_total + int(row[1])*float(row[2])
#         except ValueError:
#             print(f'Falta precio para {row[0]}')

#         # print(row)
#     f.close()
#     return costo_total


# costo = costo_camion('../Data/camion.csv')
# print(f'El costo total fue ${costo}')

# costo_missing = costo_camion('../Data/missing.csv')
# print(f'El costo total fue ${costo_missing}')
