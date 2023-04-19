import csv
import informe_funciones


def costo_camion(nombre_archivo):
    camion = informe_funciones.leer_camion(nombre_archivo)
    costo_total = 0
    for cajon in camion:
        try:
            costo_total = costo_total + \
                int(cajon["cajones"])*float(cajon["precio"])
        except ValueError:
            print(f'No pude interpretar una fila')
    return costo_total


costo = costo_camion('../Data/camion.csv')
print(f'El costo total fue ${costo}')

costo_missing = costo_camion('../Data/missing.csv')
print(f'El costo total fue ${costo_missing}')

costo_fechas = costo_camion('../Data/fecha_camion.csv')
print(f'El costo total fue ${costo_fechas}')
