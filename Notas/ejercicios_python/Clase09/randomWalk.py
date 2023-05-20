import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()  #Array de ubicaciones

N=1000
caminantes = []
for i in range(12):
    caminantes.append(randomwalk(N))

tiempo = np.array(range(0, N))
for caminante in caminantes:
    plt.plot(tiempo, caminante)
plt.show()