class Animal:
    def __init__(self, peso, edad):
        self.peso = peso
        self.edad = edad

    def mostrar_datos(self):
        return f"Peso: {self.peso} kg, Edad: {self.edad} años"

class Perro(Animal):
    def __init__(self, peso, edad, raza):
        super().__init__(peso, edad)
        self.raza = raza

    def mostrar_edad_humana(self):
        edad_humana = self.edad * 7  # Suponiendo que 1 año de perro equivale a 7 años humanos
        return f"Edad equivalente en años humanos: {edad_humana} años"

class Gato(Animal):
    def __init__(self, peso, edad, pelaje):
        super().__init__(peso, edad)
        self.pelaje = pelaje

    def estado_salud(self):
        # Suponemos que un gato se considera sano si su peso es adecuado para su edad
        if self.edad <= 2 and self.peso >= 1.5:
            return "El gato está sano."
        elif self.edad > 2 and self.peso >= 2:
            return "El gato está sano."
        else:
            return "El gato podría tener problemas de salud."

# Ejemplo de uso de las clases
perro = Perro(10, 3, "Labrador")
gato = Gato(3, 4, "Largo")

print("Información del perro:")
print(perro.mostrar_datos())
print(f"Raza: {perro.raza}")
print(perro.mostrar_edad_humana())

print("\nInformación del gato:")
print(gato.mostrar_datos())
print(f"Pelaje: {gato.pelaje}")
print(gato.estado_salud())
