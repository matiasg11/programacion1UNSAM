import csv


def parse_csv(nombre_archivo, select=None, types = None):
    '''
    Parsea un archivo CSV en una lista de registros.
        Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Lee los encabezados
        headers = next(rows)

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            if indices:
                row = [row[index] for index in indices]
            registro = dict(zip(headers, row))
            registros.append(registro)

    return registros
