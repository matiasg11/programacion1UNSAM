#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# informe_final.py

# %% ejercicio 7.7
import fileparse
import lote
import formato_tabla


def leer_camion(nombre_archivo):
    """Computa el precio total del camion (cajones * precio) de un archivo"""
    with open(nombre_archivo) as f:
        camion_dicts = fileparse.parse_csv(
            f,
            select=["nombre", "cajones", "precio"],
            types=[str, int, float],
            has_headers=True,
        )
    camion = [lote.Lote(d["nombre"], d["cajones"], d["precio"]) for d in camion_dicts]
    return camion


def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types=[str, float], has_headers=False)
    return precios


def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        cambio = precios[lote.nombre] - lote.precio
        t = (lote.nombre, lote.cajones, lote.precio, cambio)
        lista.append(t)
    return lista


# def imprimir_informe(informe):
#     print("    Nombre    Cajones     Precio     Cambio")
#     print("---------- ---------- ---------- ----------")
#     for nombre, cajones, precio, cambio in informe:
#         precio = f"${precio}"
#         print(f"{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}")


def imprimir_informe(data_informe, formateador):
    """
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia)
    """
    formateador.encabezado(["Nombre", "Cantidad", "Precio", "Cambio"])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f"{precio:0.2f}", f"{cambio:0.2f}"]
        formateador.fila(rowdata)


def informe_camion(nombre_archivo_camion, nombre_archivo_precios, formato="txt"):
    """
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es txt
    Alternativas: csv o html
    """
    camion = leer_camion(nombre_archivo_camion)
    precios = dict(leer_precios(nombre_archivo_precios))

    data_informe = hacer_informe(camion, precios)
    formateador = formato_tabla.crear_formateador(formato)

    imprimir_informe(data_informe, formateador)


# %%
def f_principal(argumentos):
    if len(argumentos) > 3:
        informe_camion(argumentos[1], argumentos[2], argumentos[3])

    else:
        informe_camion(argumentos[1], argumentos[2])


if __name__ == "__main__":
    import sys

    f_principal(sys.argv)
