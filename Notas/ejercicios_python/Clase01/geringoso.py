# 1.18 Geringoso rústico

palabra = "Geringoso"


def geringosear(cadena):
    capadepenapa = ""
    for c in cadena:
        if c in "aeiouAEIOU":
            capadepenapa = capadepenapa + c + "p" + c
        else:
            capadepenapa = capadepenapa + c
    print(capadepenapa)


geringosear(palabra)
