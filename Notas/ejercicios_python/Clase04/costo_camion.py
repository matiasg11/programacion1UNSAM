import csv


def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    headers = next(rows)
    costo_total = 0
    for i, row in enumerate(rows, start=1):
        try:
            record = dict(zip(headers, row))
            costo_total = costo_total + \
                int(record["cajones"])*float(record["precio"])
        except ValueError:
            print(f'Fila {i}: No pude interpretar: {row}')

        # Debugger
        print(record)
    f.close()
    return costo_total


costo = costo_camion('../Data/camion.csv')
print(f'El costo total fue ${costo}')

costo_missing = costo_camion('../Data/missing.csv')
print(f'El costo total fue ${costo_missing}')

costo_fechas = costo_camion('../Data/fecha_camion.csv')
print(f'El costo total fue ${costo_fechas}')
