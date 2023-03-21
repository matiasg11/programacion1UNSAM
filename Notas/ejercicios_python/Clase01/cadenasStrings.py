# cadenasStrings.py
# 1.14

frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'

frutas[0]  # M
frutas[1]  # a
frutas[2]  # n
frutas[-1]  # i
frutas[-2]  # w

# 1.15 Concatenación de cadenas

frutas = frutas + ",Pera"
frutas = "Melón," + frutas
print(frutas)

# 1.16: Testeo de pertenencia (test de subcadena)
'Naranja' in frutas  # True
'nana' in frutas  # True
'Lima' in frutas  # False

# 1.17: Iteración sobre cadenas

cadena = "Ejemplo con for"
count = 0

for c in cadena:
    print('Caracter:', c)
    if (c == 'o'):
        count = count+1

print(count, "o en el texto")

# 1.20 f-strings

nombre = "Matías"
equipo = "Boca Juniors"
edad = 30
print(f'Soy {nombre}, tengo {edad} años y soy de {equipo}')
