# 1.22
frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'

lista_frutas = frutas.split(',')

fruta_inicial = lista_frutas[0]
fruta_final = lista_frutas[-1]
algunas = lista_frutas[0:2]
mas = lista_frutas.append("otrafruta")
menos = lista_frutas.pop()

# print(fruta_final, fruta_inicial, algunas, mas, menos)

for fruta in lista_frutas:
    print(fruta)

print("limon" in lista_frutas)

# 1.25 y 1.26

lista_frutas.append("Mango")
lista_frutas.insert(1, "Lima")
lista_frutas.remove("Mandarina")
lista_frutas.append("Banana")
print(lista_frutas, lista_frutas.index("Banana"))
lista_frutas.remove("Banana")
lista_frutas.sort()
print(lista_frutas)
lista_frutas.sort(reverse=True)
print(lista_frutas)

altogether = ", ".join(lista_frutas)
print(altogether)
