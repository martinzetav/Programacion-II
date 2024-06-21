from Figura import FiguraGeometrica

class FiguraRectangulo(FiguraGeometrica):
    def __init__(self, cantidadLados):
        super().__init__(cantidadLados)

    def calcularArea(self):
        return self.lados[0]*self.lados[1]