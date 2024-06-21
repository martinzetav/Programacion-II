class Coche:

    def __init__(self, marca, modelo, anio, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.velocidad = velocidad

    def acelerar(self, km):
        self.velocidad += km
        if self.velocidad >= 457:
            self.velocidad = 457

    def frenar(self, km):
        if km > self.velocidad:
            self.velocidad = 0
        else:
            self.velocidad -= km

auto = Coche("Ford", "Ka", "2007", 200)
print(auto.velocidad)
auto.acelerar(100)
print(auto.velocidad)
auto.frenar(500)
print(auto.velocidad)