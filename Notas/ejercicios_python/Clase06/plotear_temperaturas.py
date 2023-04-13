import matplotlib.pyplot as plt
import numpy as np


def plotear_temperaturas(archivo):
    lista = np.load(archivo)
    print(lista)
    plt.hist(lista, bins=10)
    plt.show()


plotear_temperaturas("../Data/temperaturas.npy")
