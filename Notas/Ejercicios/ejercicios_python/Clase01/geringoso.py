# 1.18 Geringoso rústico

cadena = 'Geringoso'
capadepenapa = ""

for c in cadena:
    if c in 'aeiouAEIOU':
        capadepenapa = capadepenapa + c + 'p' + c
    else:
        capadepenapa = capadepenapa + c
print(capadepenapa)
