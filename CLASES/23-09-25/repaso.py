class Persona:
    def __init__(self, nombre, apellido, edad, altura, peso):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.edad} años - {self.altura} m - {self.peso} kg."
    
    def año_nacimiento(self, año_actual):
        return año_actual-self.edad
    
# Alumno -> Att-> Carrera, Matricula, Año_Ingreso, Comision, Notas
#        -> Met-> Calcular_Promedio, Antiguedad_Carrera

class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, carrera, matricula, año_ingreso, comision):
        super().__init__(nombre, apellido, edad, altura=None, peso=None)
        # del super().altura
        # del super().peso
        self.carrera = carrera
        self.matricula = matricula
        self.año_ingreso = año_ingreso
        self.comision = comision
        self.notas = []

    def calcular_promedio(self):
        sumatoria = sum(self.notas)
        # ac = 0
        # for nota in self.notas:
        #     ac+= nota
        promedio = sumatoria/len(self.notas)
        return promedio
    
    def antiguedad_carrera(self, año_actual):
        return año_actual - self.año_ingreso
        
    def cargar_nota(self, nota):
        self.notas.append(nota)


class AlumnoPrimaria(Persona):
    def __init__(self, nombre, apellido, edad, altura, peso, tutor):
        super().__init__(nombre, apellido, edad, altura, peso)
        self.tutor = tutor
        self.notas = []
    
    def datos_tutor(self):
        return self.tutor

    def año_egreso_primaria(self):
        return 12 - self.edad
    
    def cargar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        sumatoria = sum(self.notas)
        promedio = sumatoria/len(self.notas)
        return promedio

persona1 = Persona("Juan", "Perez", 34, 1.80, 90)
alumno = AlumnoPrimaria("Matias", "Lucero", 8, 1.20, 63, persona1) 

print(alumno.datos_tutor())
print(alumno.año_egreso_primaria())
