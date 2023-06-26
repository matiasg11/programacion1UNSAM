class FormatoTabla:
    def encabezado(self, headers):
        """
        Crea el encabezado de la tabla
        """
        raise NotImplementedError()

    def fila(self, rowdata):
        """
        Crea una única fila de datos de la tabla
        """
        raise NotImplementedError()


class FormatoTablaTXT(FormatoTabla):
    """
    Genera una tabla en formato .txt
    """

    def encabezado(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def fila(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class FormatoTablaCSV(FormatoTabla):
    """
    Genera una tabla en formato .csv
    """

    def encabezado(self, headers):
        print(",".join(headers))

    def fila(self, data_fila):
        print(",".join(data_fila))


class FormatoTablaHTML(FormatoTabla):
    """
    Genera una tabla en formato html
    """

    def encabezado(self, headers):
        row = "<tr>"
        for h in headers:
            row += "<th>" + h + "</th>"
        row += "</tr>"
        print(row)

    def fila(self, data_fila):
        row = "<tr>"
        for h in data_fila:
            row += "<td>" + h + "</td>"
        row += "</tr>"
        print(row)


def crear_formateador(formato):
    # Elige formato
    if formato == "txt":
        return FormatoTablaTXT()
    elif formato == "csv":
        return FormatoTablaCSV()
    elif formato == "html":
        return FormatoTablaHTML()
    else:
        raise RuntimeError(f"Unknown format {formato}")


def imprimir_tabla(datos, columnas, formateador):
    import lote

    # formateador = crear_formateador(formato)
    formateador.encabezado(columnas)
    for lote in datos:
        rowdata = []
        for col in columnas:
            rowdata.append(str(getattr(lote, col)))
        formateador.fila(rowdata)
