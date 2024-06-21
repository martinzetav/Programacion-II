class Estudiante:

    def __init__(self, nombre, edad, promedio, carrera):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio
        self.carrera = carrera

    def verificarAprobacion(self):
        if self.promedio >= 70:
            return "Aprobado"
        else:
            return "Reprobado"
        
    def esMayorDeEdad(self):
        return self.edad >= 18
    
estudiante = Estudiante("Jerome", 15, 50, "Veterinaria")
print(estudiante.verificarAprobacion())
print(estudiante.esMayorDeEdad())
        
    
