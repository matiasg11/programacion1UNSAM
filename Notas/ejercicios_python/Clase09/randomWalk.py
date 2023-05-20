import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()  #Array de ubicaciones

N=1000
caminantes = []
for i in range(12):
    caminantes.append(randomwalk(N))
   
maximos = []
tiempo = np.array(range(0, N))
for caminante in caminantes:
    print(caminante.max(), caminante.min())
    maximos.append(max(caminante.max(), abs(caminante.min())))
    plt.plot(tiempo, caminante, color=np.random.rand(3,), linewidth=1.0, linestyle="-", label=i+1)

print(maximos)
print("El que más se aleja es el caminante", maximos.index(max(maximos))+1, "que llega hasta la posición", max(maximos))
print("El que menos se aleja es el caminante", maximos.index(min(maximos))+1, "que llega hasta la posición", min(maximos))



#plt.show()