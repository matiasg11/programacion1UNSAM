from statistics import mode
import random

dias = 365


def cocumpleaños(gente):
    cumples = []
    for i in range(gente):
        cumples.append(random.randint(1, dias))
    # if len(set(cumples)) != len(cumples):
    #     print("Hay duplicados")
    duplicados = [x for i, x in enumerate(cumples) if i != cumples.index(x)]
    if duplicados != []:
        # print(duplicados)
        # print(f'Se repiten cumpleaños los días {set(duplicados)}')
        return True
    else:
        # print("\nno se repiten")
        return False


dic = {}
for gente in range(20, 30):
    dupl = 0
    for i in range(1000):
        if cocumpleaños(gente):
            dupl += 1
    dic[gente] = (dupl/1000)

print(dic)

# A partir del 23 la mayoría de las veces da un valor > 0.5
