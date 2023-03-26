import csv
from pprint import pprint


def leer_camion(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        camion = []
        for i, row in enumerate(rows):
            try:
                obj = {}
                ncajones = int(row[1])
                precio = float(row[2])
                obj["nombre"] = row[0]
                obj["cajones"] = ncajones
                obj["precio"] = precio
                camion.append(obj)
            except ValueError:
                print('Faltan datos en la línea', i, "del archivo")
        return camion


# este_camion = leer_camion("../Data/camion.csv")
# pprint(este_camion)
# [('Lima', 100, 32.2), ('Naranja', 50, 91.1), ('Caqui', 150, 103.44), ('Mandarina', 200, 51.23), ('Durazno', 95, 40.37), ('Mandarina', 50, 65.1), ('Naranja', 100, 70.44)]

def leer_precios(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf-8") as f:
        rows = csv.reader(f)
        precios = {}
        for i, row in enumerate(rows):

            try:
                if row == []:
                    continue
                else:
                    precios[row[0]] = float(row[1])
            except ValueError:
                print('Faltan datos en la línea', i, "del archivo")
        return precios


precios_venta = leer_precios('../Data/precios.csv')
camion_list = leer_camion('../Data/camion.csv')

bruto = 0
costo = 0
margen = 0

for item in camion_list:
    costo += item["cajones"]*item["precio"]
    bruto += item["cajones"]*precios_venta[item["nombre"]]

margen = bruto - costo
print(
    f"Costo del camión: ${costo:0.2f}\nVenta del camión: ${bruto:0.2f}\nMargen neto: ${margen:0.2f}")
