import csv


def parse_csv(
    nombre_archivo, select=None, types=None, has_headers=True, silence_errors=False
):
    """
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    Se puede convertir el tipo directamente con una lista de los tipos requeridos para cada elemento.
    """
    if select and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados")

    with open(nombre_archivo, "rt", encoding="utf-8") as f:
        rows = csv.reader(f)

        # Declara los índices por única vez
        indices = []
        # Lee los encabezados
        if has_headers:
            headers = next(rows)

            if select:
                indices = [headers.index(nombre_columna) for nombre_columna in select]
                headers = select

        registros = []
        for i, row in enumerate(rows):
            # Saltea filas sin datos
            # if not row or ("" in row):
            #     continue
            if indices:
                row = [row[index] for index in indices]
            if types:
                try:
                    row = [tipo(valor) for tipo, valor in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Fila {i+1}: No pude convertir {row}")
                        print(f"Fila {i+1}: Motivo: {e}")
                    continue

        if has_headers:
            registro = dict(zip(headers, row))
        else:
            registro = dict(zip(row[0], [row[i] for i in range(len(row))]))
        registros.append(registro)

    return registros


# camion = parse_csv("../Data/missing.csv", types=[str, int, float])
# print(camion)

# camion2 = parse_csv("../Data/missing.csv", types=[str, int, float], silence_errors=True)
# print(camion)
