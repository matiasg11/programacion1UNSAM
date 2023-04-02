def propagar(lista):
    lista_nueva = lista
    lista_previa = []
    while lista_nueva != lista_previa:
        lista_previa = lista_nueva.copy()
        for i in range(0, len(lista_nueva)):
            if lista_nueva[i] == 1 and i != 0 and lista_nueva[i-1] != -1:
                lista_nueva[i-1] = 1
        for i in range(len(lista_nueva)-1, 0, -1):
            if lista_nueva[i] == 1 and i != len(lista)-1 and lista_nueva[i+1] != -1:
                lista_nueva[i+1] = 1
    print(lista_nueva)
    return lista_nueva


propagar([0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0])
propagar([0, 0, 0, 1, -1, 0, 0, 0, -1, 0, 1, 0, 0])
propagar([0, 0, 0, 1, 0, 0])
