import csv


def parse_csv(nombre_archivo, select=None, types=None, has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede convertir el tipo directamente con una lista de los tipos requeridos para cada elemento.
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)

        # Declara los índices por única vez
        indices = []
        # Lee los encabezados
        if has_headers:
            headers = next(rows)

            if select:
                indices = [headers.index(nombre_columna)
                           for nombre_columna in select]
                headers = select

        registros = []
        for row in rows:
            if not row:    # Saltea filas sin datos
                continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                row = [tipo(valor) for tipo, valor in zip(types, row)]

            if has_headers:
                registro = dict(zip(headers, row))
            else:
                registro = (row[i] for i in len(row))
            registros.append(registro)

    return registros
