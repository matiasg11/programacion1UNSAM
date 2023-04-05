import random


def generar_punto():
    x = random.random()
    y = random.random()
    return x, y


N = 10000
M = 0
F = 100
for n in range(F):
    lista = []
    for i in range(N):
        (x, y) = generar_punto()
        if (x**2 + y**2 <= 1):
            M += 1
    lista.append(4*M/N)
print((sum([v for v in lista])/F))
