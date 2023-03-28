import csv
from pprint import pprint


def leer_camion(nombre_archivo):
    with open(nombre_archivo, "rt", encoding="utf-8") as f:
        rows = csv.reader(f)
        headers = next(rows)
        camion = []
        for i, row in enumerate(rows, start=1):
            try:
                record = dict(zip(headers, row))
                obj = {}
                ncajones = int(record["cajones"])
                precio = float(record["precio"])
                obj["nombre"] = record["nombre"]
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
        headers = ["nombre", "precio"]
        precios = {}
        for i, row in enumerate(rows):
            try:

                if row == []:
                    continue
                else:
                    record = dict(zip(headers, row))
                    precios[record["nombre"]] = float(record["precio"])
            except ValueError:
                print('Faltan datos en la línea', i, "del archivo")
        return precios


def calcular_ganancias(camion, precios):
    bruto = 0
    costo = 0
    margen = 0

    for item in camion_list:
        costo += item["cajones"]*item["precio"]
        bruto += item["cajones"]*precios_venta[item["nombre"]]

    margen = bruto - costo
    print(
        f"Costo del camión: ${costo:0.2f}\nVenta del camión: ${bruto:0.2f}\nMargen neto: ${margen:0.2f}")


def hacer_informe(camion, precios):

    print("Ejercicio 4.8:\n")
    for item in camion:
        r = ((item["nombre"], item["cajones"], precios[item["nombre"]],
             precios[item["nombre"]]-item["precio"]))
        print(r)

    print("\nEjercicio 4.9:\n")

    for item in camion:
        print(
            f'{item["nombre"]:>10s} {item["cajones"]:>10d}  ${precios[item["nombre"]]:7.2f} ${precios[item["nombre"]]-item["precio"]:>6.2f}')


precios_venta = leer_precios('../Data/precios.csv')
camion_list = leer_camion('../Data/camion.csv')
camion_fecha = leer_camion('../Data/fecha_camion.csv')

# calcular_ganancias(camion_list, precios_venta)
# calcular_ganancias(camion_fecha, precios_venta)

hacer_informe(camion_list, precios_venta)
