#CREAR CLASE
#self es igual a this. Hace referencia al objeto mismo
class Persona:
    #Atributos
    #Constructor
    def __init__(self, nombre, apellido, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        
    #Metodos
    def calcular_edad(self):
        edad = 2023 - self.fecha_nacimiento
        return edad

#Crear objeto
martin = Persona("Martin", "Zalazar", 2000)

#Para acceder a un metodo o atributo de un objeto ya creado, utilizamos "."
#Acceder a atributo del objeto
print(martin.apellido)
#Acceder a metodo del objeto
print(martin.calcular_edad())