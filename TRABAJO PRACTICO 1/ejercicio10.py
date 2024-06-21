class AnimalDomestico:
    def __init__(self, nombre, especie, edad, duenioAnimal):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.duenioAnimal = duenioAnimal
    
    def sonidoAnimal(self, sonido):
        print(f"El sonido caracteristico de la especie \"{self.especie}\" es: {sonido}")

    def esJovenAdultoOAnciano(self):
        if self.edad > 0 and self.edad < 5:
            return f"es JOVEN"
        elif self.edad >= 5 and self.edad < 10:
            return f"es ADOLESCENTE"
        else:
            return f"es ANCIANO"

perro = AnimalDomestico("Jerome","Perro",5, "Martin")
perro.sonidoAnimal("GUAU GUAU!!!")
print(perro.esJovenAdultoOAnciano())

        
    