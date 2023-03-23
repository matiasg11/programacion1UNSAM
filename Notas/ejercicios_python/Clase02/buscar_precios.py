
def buscar_precio(fruta):
    precio = None
    with open('../Data/precios.csv', 'rt') as f:
        headers = next(f).split(",")
        for line in f:
            row = line.split(",")
            if fruta in row[0]:
                precio = row[1]

        if precio:
            print(f'El precio de un cajón de {fruta} es ${precio}')
        else:
            print(f'{fruta} no está en el listado de precios')


buscar_precio("Naranja")
buscar_precio("Kale")
