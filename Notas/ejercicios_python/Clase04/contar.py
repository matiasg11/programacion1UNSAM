# 4.1 Contar
from pprint import pprint

# for n in range(10):
#     print(n, end=' ')

# for n in range(10, 0, -1):
#     print(n, end=" ")

# for n in range(0, 10, 2):
#     print(n, end=" ")


# 4.2
data = [4, 9, 1, 25, 16, 100, 49]

# print(min(data), max(data), sum(data))


# for x in data:
#     print(x**2)

for n, x in enumerate(data):
    print(n, x, x*2)

# for n in range(len(data)):
#     print(data[n])
