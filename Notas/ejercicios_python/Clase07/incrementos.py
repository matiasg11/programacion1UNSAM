def incrementar(s):
    '''Para una lista binaria dada devuelve la secuencia siguiente'''
    carry = 1
    l = len(s)

    for i in range(l-1, -1, -1):
        if (s[i] == 1 and carry == 1):
            s[i] = 0
            carry = 1
        else:
            s[i] = s[i] + carry
            carry = 0
    return s


def listar_secuencias(n):
    lista = [0]*n
    lista_maestra = []
    while not all(lista):
        lista_maestra.append(lista.copy())
        incrementar(lista)
    lista_maestra.append(lista.copy())
    return lista_maestra


print(len(listar_secuencias(15)))
print(len(listar_secuencias(20)))
