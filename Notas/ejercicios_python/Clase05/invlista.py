def invertir_lista(lista):
    invertida = []
    copia = lista
    while len(copia) > 0:
        invertida.append(copia.pop())
    print(invertida)
    return invertida


invertir_lista([1, 2, 3, 4, 5])
invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
