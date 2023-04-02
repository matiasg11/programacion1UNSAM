import csv
f = open('../Data/camion.csv')
rows = csv.reader(f)
headers = next(rows)
types = [str, int, float]
row = next(rows)
converted = [func(val) for func, val in zip(types, row)]
print(converted)

objeto = {nombre: func(val) for nombre, func, val in zip(headers, types, row)}
print(objeto)
f.close()


f = open('../Data/dowstocks.csv')
rows = csv.reader(f)
headers = next(rows)
row = next(rows)
types = [str, float, str, str, float, float, float, float, int]
converted = [func(val) for func, val in zip(types, row)]
record = dict(zip(headers, converted))
date = record["date"].split("/")
record["date"] = str(f'({(date[0])}, {(date[1])}, {(date[2])})')
print(record)
