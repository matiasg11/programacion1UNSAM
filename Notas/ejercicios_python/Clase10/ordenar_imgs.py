import os
from listar_imgs import archivos_png
from datetime import datetime
import time


# Crear un nuevo directorio '../Data/imgs_procesadas/'
def crear_carpeta(directorio, nombre_carpeta):
    if nombre_carpeta in os.listdir(directorio):
        print("La carpeta existe")
    else:
        os.mkdir(os.path.join(directorio, nombre_carpeta))


directorio = "../Data"
carpeta_a_crear = "imgs_procesadas"
crear_carpeta(directorio, carpeta_a_crear)

# Buscar archivos png en la carpeta deseada
carpeta_de_busqueda = "ordenar"
path_carpeta_de_busqueda = os.path.join(directorio, carpeta_de_busqueda)
lista_archivos_png = archivos_png(os.path.join(path_carpeta_de_busqueda))

# Leer fecha de los últimos 8 digitos del archivo

# Formato de archivo: "nombrefinal_YYYYMMDD.png"
# Modificar fecha de edicion y acceso


def mod_fecha_edicion(archivo, fecha_nueva_str):
    fecha_datetime = datetime.strptime(fecha_nueva_str, "%Y%m%d")
    fecha_timestamp = fecha_datetime.timestamp()
    os.utime(archivo, (fecha_timestamp, fecha_timestamp))


def extraer_datos(archivo):
    nombre = str(archivo["name"])
    extension = nombre[-4:-1] + nombre[-1]
    fecha = nombre[-12:-4]
    nombre_nuevo = nombre[0:-13]
    # Debugger
    print(nombre, extension, fecha, nombre_nuevo)
    return tuple((nombre_nuevo, fecha, extension))


# def procesar_nombre(fname):

for archivo in lista_archivos_png:
    (nombre_nuevo, fecha, extension) = extraer_datos(archivo)
    mod_fecha_edicion(
        os.path.normpath(os.path.join(archivo["root"], archivo["name"])), fecha
    )


# Cambiar el nombre del archivo

# Mover archivo a la carpeta creada

# Borrar subcarpetas vacías
