import os
import datetime
import time


def archivos_png(directorio, debugger=False):
    """Arma una lista de todos los archivos .png que se encuentren en algún directorio o subdirectorio dado"""
    lista_archivos = []
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if ".png" in name:
                lista_archivos.append({"root": root, "name": name})
                if debugger:
                    print(os.path.normpath(os.path.join(root, name)))
    return lista_archivos


# archivos_png("../Data/ordenar")
