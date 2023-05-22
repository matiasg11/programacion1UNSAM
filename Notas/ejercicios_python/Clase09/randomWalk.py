import numpy as np
import matplotlib.pyplot as plt


def randomwalk(largo):
    pasos = np.random.randint(-1, 2, largo)
    return pasos.cumsum()  # Array de ubicaciones


def cm2inch(value):
    return value / 2.54


fig = plt.figure(figsize=(cm2inch(12.8), cm2inch(9.6)))

N = 10000
caminantes = []
for i in range(12):
    caminantes.append(randomwalk(N))

maximos = []

tiempo = np.array(range(0, N))

plt.subplot(2, 1, 1)
plt.title("12 caminatas al azar")
for i, caminante in enumerate(caminantes):
    # print(caminante.max(), caminante.min())
    maximos.append(max(caminante.max(), abs(caminante.min())))
    plt.plot(
        tiempo,
        caminante,
        linewidth=1.0,
        linestyle="-",
        label=str(i + 1),
    )

plt.legend(loc="upper right")
# plt.xticks(np.linspace(0, N, 5))
# plt.yticks(np.linspace(-N / 20, N / 20, 11))
plt.ylim(-max(maximos) * 1.1, max(maximos) * 1.1)
plt.xlim(0, N)


plt.subplot(2, 2, 3)
plt.title("La caminata que más se aleja")

plt.plot(
    tiempo,
    caminantes[maximos.index(max(maximos))],
    label=str(maximos.index(max(maximos)) + 1),
)
plt.legend(loc="lower left")
plt.xticks(np.linspace(0, N, 5))
plt.yticks(np.linspace(-N / 20, N / 20, 11))
# plt.ylim(-N / 20, N / 20)
plt.ylim(-max(maximos) * 1.1, max(maximos) * 1.1)

plt.xlim(0, N)


plt.subplot(2, 2, 4)
plt.title("La caminata que menos se aleja")

plt.plot(
    tiempo,
    caminantes[maximos.index(min(maximos))],
    label=str(maximos.index(min(maximos)) + 1),
)

plt.legend(loc="lower right")
plt.xticks(np.linspace(0, N, 5))
plt.yticks(np.linspace(-N / 20, N / 20, 11))
# plt.ylim(-N / 20, N / 20)
plt.ylim(-max(maximos) * 1.1, max(maximos) * 1.1)

plt.xlim(0, N)

print(maximos)
print(
    "El que más se aleja es el caminante",
    maximos.index(max(maximos)) + 1,
    "que llega hasta la posición",
    max(maximos),
)
print(
    "El que menos se aleja es el caminante",
    maximos.index(min(maximos)) + 1,
    "que llega hasta la posición",
    min(maximos),
)


plt.show()
