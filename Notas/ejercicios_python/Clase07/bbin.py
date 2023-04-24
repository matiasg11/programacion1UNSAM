def busqueda_binaria(lista, x, verbose=False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1  # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1  # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1  # descarto mitad izquierda
    return pos


def donde_insertar(lista, x, verbose=False):
    '''Donde insertar
    Precondición: la lista está ordenada
    Si x está en la lista, devuelve p tal que lista[p+1] > x y lista[p-1] < x
    Sino, inserta el valor en posición p y devuelve p'''

    izq = 0
    der = len(lista)-1

    if x > lista[der]:
        return len(lista)
    elif x < lista[izq]:
        return izq
    else:
        while x > lista[izq] or x < lista[der]:
            medio = (izq + der) // 2
            pos = medio
            if lista[medio] == x:
                return pos
            if lista[der] == x:
                return der
            if lista[izq] == x:
                return izq     # elemento encontrado!
            if lista[medio] > x:
                der = medio - 1  # descarto mitad derecha
            else:               # if lista[medio] < x:
                izq = medio + 1  # descarto mitad izquierda
        medio = (izq + der) // 2
        pos = medio+1
        return pos


# print(donde_insertar([0, 2, 4, 6], -2))
# print(donde_insertar([0, 2, 4, 6], -1))
# print(donde_insertar([0, 2, 4, 6], 0))
# print(donde_insertar([0, 2, 4, 6], 1))
# print(donde_insertar([0, 2, 4, 6], 2))
# print(donde_insertar([0, 2, 4, 6], 3))
# print(donde_insertar([0, 2, 4, 6], 4))
# print(donde_insertar([0, 2, 4, 6], 5))
# print(donde_insertar([0, 2, 4, 6], 6))
# print(donde_insertar([0, 2, 4, 6], 7))
# print(donde_insertar([0, 2, 4, 6], 8))

def insertar(lista, x):
    '''Insertar
    Precondición: la lista está ordenada
    Devuelve p tal que lista[p+1] > x y lista[p-1] < x'''

    izq = 0
    der = len(lista)-1
    comps = 1
    if x > lista[der]:
        # comps += 1
        pos = len(lista)
        lista.insert(pos, x)
        return pos, comps
    elif x < lista[izq]:
        # comps += 1
        pos = izq
        lista.insert(pos, x)
        return pos, comps
    else:
        while x > lista[izq] or x < lista[der]:
            comps += 1
            medio = (izq + der) // 2
            pos = medio
            if lista[medio] == x:
                return pos
            if lista[der] == x:
                return der
            if lista[izq] == x:
                return izq     # elemento encontrado!
            if lista[medio] > x:
                der = medio - 1  # descarto mitad derecha
            else:               # if lista[medio] < x:
                izq = medio + 1  # descarto mitad izquierda
        medio = (izq + der) // 2
        pos = medio+1
        lista.insert(pos, x)
        return pos, comps


print(insertar([0, 2, 4, 6], -2))
print(insertar([0, 2, 4, 6], -1))
print(insertar([0, 2, 4, 6], 0))
print(insertar([0, 2, 4, 6], 1))
print(insertar([0, 2, 4, 6], 2))
print(insertar([0, 2, 4, 6], 3))
print(insertar([0, 2, 4, 6], 4))
print(insertar([0, 2, 4, 6], 5))
print(insertar([0, 2, 4, 6], 6))
print(insertar([0, 2, 4, 6], 7))
print(insertar(list(range(0, 1000, 2)), 500))
print(insertar(list(range(0, 1000, 2)), 125))
print(insertar(list(range(0, 1000, 2)), 343))
print(insertar(list(range(0, 1000, 2)), 919))
print(insertar(list(range(0, 1000, 2)), 713))
