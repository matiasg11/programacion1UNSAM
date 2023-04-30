# rebotes.py
# Archivo de ejemplo
# Ejercicio

"""Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. 
Escribí un programa `rebotes.py` que imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes."""
import sys


def rebotes(altura_i, reb=10):
    altura_inicial = 100
    altura = altura_i or altura_inicial
    rebote = 3 / 5
    count = 0
    while altura >= 0 and count < reb:
        count = count + 1
        altura = altura * rebote
        print(count, "\t", round(altura, 4))


altura_inicial = 100
if __name__ == "__main__":
    if len(sys.argv) > 2:
        rebotes(int(sys.argv[1]), int(sys.argv[2]))
    elif len(sys.argv) > 1:
        rebotes(int(sys.argv[1]))
    else:
        rebotes(altura_inicial)
