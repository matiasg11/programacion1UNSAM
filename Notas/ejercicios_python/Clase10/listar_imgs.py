import os
import datetime
import time


def archivos_png(directorio):
    """Arma una lista de todos los archivos .png que se encuentren en algún directorio o subdirectorio dado"""
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if ".png" in name:
                print(os.path.normpath(os.path.join(root, name)))


archivos_png("../Data/ordenar")
