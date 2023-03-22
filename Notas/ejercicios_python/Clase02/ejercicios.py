# 2.1

# with open('../Data/camion.csv', 'rt') as f:
#     data = f.read()
#     print(data)

import gzip
with open('../Data/camion.csv', 'rt') as f:
    headers = next(f).split(",")

    for line in f:
        row = line.split(",")
        print(row)

# 2.3 Precio naranja

g = open('../Data/precios.csv', 'rt')

for line in g:
    row = line.split(',')
    if row[0] == "Naranja":
        print(f'La {row[0]} vale ${float(row[1])} el kg.')

g.close()


# 2.4 archivos comprimidos
with gzip.open('../Data/camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end='')
