
lineas = []

for i in range(0, 10):
    linea = []
    x = 0
    for j in range(0, 10):
        linea.append(x)
        x += i
    lineas.append(tuple(linea))

print('%9s %4s %4s %4s %4s %4s %4s %4s %4s %4s ' % (
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))
print(f'{"":->55s}')
for linea in lineas:
    print('%4d:' % linea[1] +
          '%4d %4d %4d %4d %4d %4d %4d %4d %4d %4d ' % linea)
