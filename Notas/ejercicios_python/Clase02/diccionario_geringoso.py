
def diccionario_geringoso(lista):
    diccionario = {}
    for palabra in lista:
        geringosa = ""
        for c in palabra:
            if c in 'aeiouAEIOU':
                geringosa = geringosa + c + 'p' + c
            else:
                geringosa = geringosa + c
        print(geringosa)
        diccionario[palabra] = geringosa
    print(diccionario)
    return diccionario


lista_palabras = diccionario_geringoso(
    ['banana', 'manzana', 'mandarina'])
