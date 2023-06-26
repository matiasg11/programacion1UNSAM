class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        costo_lote = self.cajones * self.precio
        # print(costo_lote)
        return costo_lote

    def vender(self, n):
        if n > self.cajones:
            n = self.cajones
        self.cajones -= n
        # print(self.cajones)

    def __repr__(self):
        return f"Lote({self.nombre}, {self.cajones}, {self.precio})"
