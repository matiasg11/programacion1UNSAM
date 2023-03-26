precios = {
    'Pera': 490.1,
    'Lima': 23.45,
    'Naranja': 91.1,
    'Mandarina': 34.23
}

print(precios.items())


invertido_dict = dict(zip(precios.values(), precios.keys()))
invertido = list(zip(precios.values(), precios.keys()))
print(invertido, min(invertido), max(invertido), sorted(invertido))
