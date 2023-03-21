# 1.29
import re
# frase = input("Ingrese su frase")
# frase = "Todos somos programadores"

# palabras = frase.split()
# result = []

# for palabra in palabras:
#     if palabra.endswith("os"):
#         separado = list(palabra)
#         separado[-2] = "e"
#         # print(separado)
#         result.append("".join(separado))
#     else:
#         result.append(palabra)
#     # print(result)
# print(" ".join(result))


frases = ['Los hermanos sean unidos porque ésa es la ley primera',
          '¿cómo transmitir a los otros el infinito Aleph?', 'Todos, tu también']

for oracion in frases:
    palabras = oracion.split()
    result = []

    for palabra in palabras:
        if (re.search("os.?$", palabra)):
            separado = list(palabra)
            idx = "".join(reversed(separado)).index("o")
            # hay que ajustar acá para que me cambie la o en vez de la s
            separado[len(separado)-idx-1] = "e"
            # print(separado)
            result.append("".join(separado))
        else:
            result.append(palabra)
        # print(result)
    print(" ".join(result))
