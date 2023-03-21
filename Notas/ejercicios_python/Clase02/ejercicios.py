# 2.1

# with open('../Data/camion.csv', 'rt') as f:
#     data = f.read()
#     print(data)

with open('../Data/camion.csv', 'rt') as f:
    headers = next(f).split(",")

    for line in f:
        row = line.split(",")
        print(row)
