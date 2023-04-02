
def buscar_u_elemento(lista, elemento):
    """Recibe una lista y un elemento, y devuelve la posición de la última aparición de ese elemento en la lista o -1 si el elemento no está"""
    i = len(lista)-1
    pos = -1
    while i >= 0:
        if lista[i] == elemento:
            pos = i
            break
        else:
            i -= 1
    print(pos)
    return pos


# buscar_u_elemento([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#                   0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
# buscar_u_elemento([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 8)
# buscar_u_elemento([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 22)


def buscar_n_elemento(lista, elemento):
    """Recibe una lista y un elemento, y devuelve la cantidad de  de la última aparición de ese elemento en la lista o -1 si el elemento no está"""
    i = len(lista)-1
    cant = 0
    while i >= 0:
        if lista[i] == elemento:
            cant += 1
        i -= 1
    print(cant)
    return cant


# buscar_n_elemento([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#                   0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
# buscar_n_elemento([0, 1, 8, 8, 8, 8, 8, 8, 8, 82, 3, 4, 5, 6, 7, 8, 9], 8)
# buscar_n_elemento([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 22)

def maximo(lista):
    """Devuelve el máximo de una lista"""
    m = lista[0]
    largo = len(lista)-1
    for i in range(1, largo):
        if lista[i] > m:
            m = lista[i]
    print(m)
    return (m)


# maximo([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
#         0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# maximo([0, 1, 8, 8, 8, 8, 8, 8, 8, 82, 3, 4, 5, 6, 7, 8, 9])
# maximo([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

def minimo(lista):
    """Devuelve el mínimo de una lista"""
    m = lista[0]
    largo = len(lista)-1
    for i in range(1, largo):
        if lista[i] < m:
            m = lista[i]
    print(m)
    return (m)


minimo([0, 1, 2, 3, -4, 5, 6, 7, 8, 9,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
minimo([0, 1, 8, -8, 8, 8, 8, 8, 8, 82, 3, 4, 5, 6, 7, 8, 9])
minimo([0, 1, 2, 3, 4, 5, 6, -7, 8, 9])
