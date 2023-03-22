
def buscar_precio(fruta):
    precio = False
    with open('../Data/precios.csv', 'rt') as f:
        headers = next(f).split(",")
        for line in f:
            row = line.split(",")
            if row[0] == fruta:
                precio = row[1]

        if precio == True:
            print(f'El precio de un cajón de {fruta} es ${precio}')
        else:
            print(f'{fruta} no está en el listado de precios')


buscar_precio("Frambuesa")
buscar_precio("Kale")
