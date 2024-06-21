class FiguraGeometrica:
    def __init__(self, cantidadLados):
        self.lados = []
        self.cantidadLados = cantidadLados

    def ingresarLados(self):
        for i in range(0, self.cantidadLados):
            lado = int(input(f"Ingresar el lado {i+1}: "))
            self.lados.append(lado)

    def calcularPerimetro(self):
        perimetro = 0
        for lado in self.lados:
            ac += lado
        return perimetro

# figura1 = FiguraGeometrica(3)
# figura1.ingresarLados()
# print(figura1.lados)