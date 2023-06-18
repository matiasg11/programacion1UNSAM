import os


# Crear un nuevo directorio '../Data/imgs_procesadas/'
def crear_carpeta(directorio, nombre_carpeta):
    os.mkdir(os.path.join(directorio, nombre_carpeta))


directorio = "../Data"
carpeta_a_crear = "imgs_procesadas"
crear_carpeta(directorio, carpeta_a_crear)

# Buscar archivos png en la carpeta deseada

# Leer fecha de los últimos 8 digitos del archivo

# Modificar fecha de edicion y acceso

# Cambiar el nombre del archivo

# Mover archivo a la carpeta creada

# Borrar subcarpetas vacías
