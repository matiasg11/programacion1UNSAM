
# solucion_de_errores.py
# Ejercicios de errores en el código
# %%
# Ejercicio 3.5. Semántica
# Comentario: Evalua cada letra y devuelve si es "a" o no. No importa el resto de las letras de la palabra.
#    No evalúa mayusculas o minusculas
#    Debería evaluar la palabra entera antes de definir si tiene "a"
#    A continuación va el código corregido

from pprint import pprint
import csv


def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if (expresion[i] == 'a' or expresion[i] == "A"):
            return True
        i += 1
    return False


# %%
# Ejercicio 3.6. Sintaxis
# Pasa lo mismo que la "A" anterior
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if (expresion[i] == 'a' or expresion[i] == "A"):
            return True
        i += 1
    return False


# %%
# Ejercicio 3.7. Tipos
# No reconoce si no es un "str" el ingreso
def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i < n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


# print(tiene_uno('UNSAM 2020'))
# print(tiene_uno('abracadabra'))
# print(tiene_uno('La novela 1984 de George Orwell'))
# print(tiene_uno('fsdfgsjoerihgntrbiutrnibuebtiuentiueitrnbieurbnliuerbneutbeibirbneurbnielrutnbeiubietkudtkundti'))
# print(tiene_uno(19233))
# print(tiene_uno(9233))


# Ejercicio 3.8. Alcances
# Suma a y b y se lo asigna a c
# No se fija si los tipos son numeros (int o float)
# No hace nada con c, termina el programa. Debería devolver el valor.
def suma(a, b):
    c = a + b
    return c


a = 2
b = 3
c = suma(a, b)
print(f"La suma da {a} + {b} = {c}")

# Ejercicio 3.9. Pisando Memoria
# Siempre asigna un valor al diccionario "registro", No transmite el valor sino la asignación.
# Esto hace que el ultimo valor sea el reemplazado en todos.
# Se soluciona creando un nuevo diccionario para cada fila, es decir, pasando la asignación dentro del for


def leer_camion(nombre_archivo):
    camion = []
    with open(nombre_archivo, "rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion


camion = leer_camion('../Data/camion.csv')
pprint(camion)
