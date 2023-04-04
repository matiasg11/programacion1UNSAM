import random


def crear_mazo():
    valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
    palos = ['oro', 'copa', 'espada', 'basto']
    naipes = [(int(valor), palo) for valor in valores for palo in palos]
    return naipes


def barajar_mano(naipes):
    mano = (random.sample(naipes, k=3))
    return mano


def calcular_envido(mano):
    suma12 = 0
    suma13 = 0
    suma23 = 0

    # Cartas 1 y 2
    canto = 0
    if (mano[0][1] == mano[1][1]):
        canto = max(20, canto)
        if (mano[0][0] < 10):
            canto = max(canto+mano[0][0], canto)
        if (mano[1][0] < 10):
            canto = max(canto+mano[1][0], canto)
        suma12 = canto
    # Cartas 1 y 3
    canto = 0
    if (mano[0][1] == mano[2][1]):
        canto = max(20, canto)
        if (mano[0][0] < 10):
            canto = max(canto+mano[0][0], canto)
        if (mano[2][0] < 10):
            canto = max(canto+mano[2][0], canto)
        suma13 = canto
    # Cartas 2 y 3
    canto = 0
    if (mano[1][1] == mano[2][1]):

        canto = max(20, canto)
        if (mano[1][0] < 10):
            canto = max(canto+mano[1][0], canto)

        if (mano[2][0] < 10):
            canto = max(canto+mano[2][0], canto)

    # Todas distintas
    if mano[0][0] > canto and mano[0][0] < 10:
        canto = mano[0][0]
    if mano[1][0] > canto and mano[1][0] < 10:
        canto = mano[1][0]
    if mano[2][0] > canto and mano[2][0] < 10:
        canto = mano[2][0]
    suma23 = canto
    return max(suma12, suma23, suma13)


naipes = crear_mazo()
lista_envido = []
for n in range(600):
    mano = barajar_mano(naipes)
    lista_envido.append((calcular_envido(mano), mano))
print(max(lista_envido))
