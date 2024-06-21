from Figura import FiguraGeometrica

class FiguraTriangulo(FiguraGeometrica):
    def __init__(self, cantidadLados, altura):
        super().__init__(cantidadLados)
        self.altura = altura

    def calcularArea(self):
        return self.lados[2] * self.altura/2

triangulo1 = FiguraTriangulo(3,4)
triangulo1.ingresarLados()