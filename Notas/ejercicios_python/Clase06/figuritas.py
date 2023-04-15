import random
import numpy as np
import matplotlib.pyplot as plt

# Cantidad de figuritas
n = 670

# Figuritas por paquete
m = 5

# Album


def crear_album(numero_figuritas):
    return np.zeros(numero_figuritas)


# album = crear_album(n)


def album_incompleto(A):
    return (0 in A)


def comprar_figu(figus_total):
    return random.randint(1, figus_total)


def cuantas_figus(figus_total):
    album = crear_album(figus_total)
    compradas = 0
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu-1] += 1
        compradas += 1
    # print(compradas)
    return compradas


# cuantas_figus(n)
n_repeticiones = 1000

# Comprension de listas
resultados = [cuantas_figus(6) for i in range(n_repeticiones)]

# De otra forma
# for i in range(n_repeticiones):
#     resultados.append(cuantas_figus(6))

resultados = np.array(resultados)
# print(np.mean(resultados))


def experimento_figus(n_repeticiones, figus_total):
    result = [cuantas_figus(figus_total) for i in range(n_repeticiones)]
    result = np.array(result)
    print(np.mean(result))
    return np.mean(result)


def exp_figus_paq(n_repeticiones, figus_total, figus_paquete):
    result = [cuantos_paquetes(figus_total, figus_paquete)
              for i in range(n_repeticiones)]
    result = np.array(result)
    print(np.mean(result))
    return (result)


def cuantos_paquetes(figus_total, figus_paquete):
    album = crear_album(figus_total)
    comprados = 0
    while album_incompleto(album):
        figus = comprar_paquete(figus_total, figus_paquete)
        # print(figus)
        for figu in figus:
            album[figu-1] += 1
        comprados += 1
    # print(compradas)
    return comprados


def comprar_paquete(figus_total, figus_paquete):
    todas_figuritas = [i for i in range(1, figus_total+1)]
    figus_p = figus_paquete
    figus = random.sample(todas_figuritas, k=figus_p)
    figus = np.array(figus)
    # print(figus)
    return figus


# experimento_figus(100, 670)

# comprar_paquete(670)
n_paquetes_hasta_llenar = np.array(
    [cuantos_paquetes(670, 5) for i in range(100)])
cantidad = (n_paquetes_hasta_llenar <= 850).sum()
print(cantidad)


def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while len(paquete) > 0:
            album[paquete.pop()-1] = 1
        figus_pegadas = (album > 0).sum()
        historia_figus_pegadas.append(figus_pegadas)
    return historia_figus_pegadas


# figus_total = 670
# figus_paquete = 6

# plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
# plt.xlabel("Cantidad de paquetes comprados.")
# plt.ylabel("Cantidad de figuritas pegadas.")
# plt.title("La curva de llenado se desacelera al final")
# plt.show()
