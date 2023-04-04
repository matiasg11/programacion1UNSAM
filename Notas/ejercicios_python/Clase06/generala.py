from statistics import mode
import random


def tirar():
    return random.randint(1, 6)


def tirada():
    tirada = []
    for i in range(5):
        tirada.append(tirar())
    return tirada


def es_generala(tirada):
    for i in range(1, 7):
        if (all(dados == i for dados in tirada)):
            return True
    return False

# Probando si funciona
# tiros = tirada()
# print(tiros)
# print(es_generala(tiros))

# Calcula la probabilidad de sacar generala servida
# results = []
# for m in range(20):
#     N = 100000  # Intentos
#     n = 0  # Cantidad de generalas servidas
#     for i in range(N):
#         if es_generala(tirada()):
#             n += 1
#     results.append(n/N)
#     print(f'{n/N:6.6f}')


# promedio = sum([result for result in results])/len(results)
# print(promedio)


def tres_tiradas():
    resultado = []
    for i in range(5):
        resultado.append(tirar())
    repetida = mode(resultado)
    # print(resultado, repetida)
    for i in range(5):
        if resultado[i] != repetida:
            resultado[i] = tirar()
    repetida = mode(resultado)
    # print(resultado, repetida)

    for i in range(5):
        if resultado[i] != repetida:
            resultado[i] = tirar()
    # Debugger
    # print(resultado)
    return resultado


# for i in range(10):
#     tres_tiradas()


def prob_generala(N):
    n = 0
    for i in range(N):
        if es_generala(tres_tiradas()):
            n += 1
    print(f'{n/N:6.5f}')
    return n/N


prob_generala(100000)
