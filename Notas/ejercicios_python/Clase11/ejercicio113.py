import fileparse
import lote

with open("../Data/camion.csv") as lineas:
    camion_dicts = fileparse.parse_csv(
        lineas, select=["nombre", "cajones", "precio"], types=[str, int, float]
    )

camion = [lote.Lote(d["nombre"], d["cajones"], d["precio"]) for d in camion_dicts]

costos = sum([c.costo() for c in camion])
print(costos)
