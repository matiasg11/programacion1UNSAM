#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:34:08 2021

@author: mcerdeiro
"""
# tabla_informe.py
import csv
import fileparse

# %%


def leer_camion(nombre_archivo):
    """Computa el precio total del camion (cajones * precio) de un archivo"""
    camion = fileparse.parse_csv(nombre_archivo)
    return camion


# %%


def leer_precios(nombre_archivo):
    precios = fileparse.parse_csv(nombre_archivo)
    return precios


# %%


def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios["nombre"]
        cambio = precio_venta - lote["precio"]
        t = (lote["nombre"], lote["cajones"], lote["precio"], cambio)
        lista.append(t)
    return lista


# %%


def imprimir_informe(informe):
    print("    Nombre    Cajones     Precio     Cambio")
    print("---------- ---------- ---------- ----------")
    for nombre, cajones, precio, cambio in informe:
        precio = f"${precio}"
        print(f"{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}")


# %%


def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)


# informe_camion('../Data/camion.csv', '../Data/precios.csv')


if __name__ == __main__:
    if len(sys.argv) > 2:
        rebotes(int(sys.argv[1]), int(sys.argv[2]))
