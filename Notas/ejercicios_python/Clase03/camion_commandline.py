import csv
import sys


def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    costo_total = 0
    for row in rows:
        try:
            costo_total = costo_total + int(row[1])*float(row[2])
        except ValueError:
            print(f'Falta precio para {row[0]}')

        # print(row)
    f.close()
    return costo_total


# costo = costo_camion('../Data/camion.csv')
# print(f'El costo total fue ${costo}')

# costo_missing = costo_camion('../Data/missing.csv')
# print(f'El costo total fue ${costo_missing}')

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'


costo = costo_camion(nombre_archivo)
print(f'El costo total fue ${costo}')
