import math

class Figura:
    def __init__(self, cantidad_lados):
        self.cantidad_lados = cantidad_lados

class Circulo(Figura):
    def __init__(self, cantidad_lados, radio):
        super().__init__(cantidad_lados)
        self.radio = radio

    def calcular_area(self):
        PI = math.pi
        area = PI * (self.radio**2)
        return area

    def circunferencia_perimetro(self):
        PI = math.pi
        circunferencia = 2 * PI * self.radio
        return circunferencia
    
class Triangulo(Figura):
    def __init__(self, cantidad_lados, base, altura):
        super().__init__(cantidad_lados)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = 0.5 * self.base * self.altura
        return area
    
    def calcular_perimetro(self):
        perimetro = self.base * 3
        return perimetro
    
class Cuadrado(Figura):
    def __init__(self, cantidad_lados, lado):
        super().__init__(cantidad_lados)
        self.lado = lado

    def calcular_area(self):
        area = self.lado * self.lado
        return area
    
    def calcular_perimetro(self):
        perimetro = self.lado * 4
        return perimetro
    
    