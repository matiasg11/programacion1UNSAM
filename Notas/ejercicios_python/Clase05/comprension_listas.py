# %%
from pprint import pprint
import csv
nums = [1, 2, 3, 4, 5]

cuadrados = [x**2 for x in nums]

dobles = [x*2 for x in nums]

copia = [x for x in nums]

copia.pop()
# %%


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


camion = leer_camion('../Data/camion.csv')
precios = leer_precios("../Data/precios.csv")
costo = sum(s['cajones']*s['precio'] for s in camion)
valor = sum(s['cajones']*precios[s['nombre']] for s in camion)
neto = valor - costo

print(f'${costo:0.2f} de costo\n${valor:0.2f} de las ventas\n${neto:0.2f} de ganancia')

myn = [s for s in camion if s['nombre'] in {'Mandarina', 'Naranja'}]
myn2 = sum([s['cajones']*s['precio']
           for s in myn if s['nombre'] == "Mandarina"])
# %%
nombre_cajones = {(s['nombre'], s['cajones']) for s in camion}
nombres = {s['nombre'] for s in camion}
stock = {nombre: 0 for nombre in nombres}
for s in camion:
    stock[s['nombre']] += s['cajones']

costos_ind = {nombre: 0 for nombre in nombres}
for s in camion:
    costos_ind[s['nombre']] += s['cajones']*s['precio']

print(stock)
print(costos_ind)
