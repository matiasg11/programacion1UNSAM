# Obelisco.py
"""Una mañana ponés un billete en la vereda al lado del obelisco porteño.
A partir de ahí, cada día vas y duplicás la cantidad de billetes, apilándolos prolijamente. 
¿Cuánto tiempo pasa antes de que la pila de billetes sea más alta que el obelisco?"""

import math

grosor = 0.11 * 0.001  # grosor en mm * 1 m/1000 mm
obelisco = 67.5  # en m
tiempo = 1
billetes = 1

while billetes*grosor <= obelisco:
    tiempo = tiempo + 1
    billetes = billetes*2

print("Tardó", tiempo, "dias. La altura total fue", billetes *
      grosor, "metros y se usaron", billetes, "billetes, o 2 a la", round(math.log2(billetes)), "que es lo mismo.")
