

def costo_camion(nombre_archivo):
    with open(nombre_archivo, 'rt') as f:
        headers = next(f).split(",")
        costo_total = 0
        for line in f:
            row = line.split(",")
            try:
                costo_total = costo_total + int(row[1])*float(row[2])
            except ValueError:
                print(f'Falta precio para {row[0]}')
            # print(row)
    return costo_total


costo = costo_camion('../Data/camion.csv')
print(f'El costo total fue ${costo}')

costo_missing = costo_camion('../Data/missing.csv')
print(f'El costo total fue ${costo_missing}')
