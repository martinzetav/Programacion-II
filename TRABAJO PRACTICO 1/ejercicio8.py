class Restaurante:
    def __init__(self, nombre, tipoDeCocina, mesasDisponibles):
        self.nombre = nombre
        self.tipoDeCocina = tipoDeCocina
        self.mesasDisponibles = mesasDisponibles
        self.valoracion = ""
    
    def reservarMesas(self, mesas):
        if mesas <= self.mesasDisponibles:
            self.mesasDisponibles -= mesas
            print(f"Se reservaron {mesas} mesas, dejando {self.mesasDisponibles} mesas disponibles")
        else:
            print(f"No hay {mesas} mesas disponibles para reservar")

    def calificarRestaurante(self, valor):
        if valor > 0:
            if valor == 1:
                self.valoracion = "Malo"
            elif valor == 2:
                self.valoracion = "Regular"
            elif valor == 3:
                self.valoracion = "Bueno"
            elif valor == 4:
                self.valoracion = "Muy Bueno"
            else:
                self.valoracion = "Excelente"

laCasona = Restaurante("La Casona", "Surtido", 20)
laCasona.reservarMesas(21)
laCasona.calificarRestaurante(5)
print(laCasona.valoracion)