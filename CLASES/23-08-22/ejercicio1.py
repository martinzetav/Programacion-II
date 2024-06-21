# class Persona:
#     def __init__(self, nombre, apellido, altura, fecha_nacimiento):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.altura = altura
#         self.fecha_nacimiento = fecha_nacimiento

#     def calcularEdad(self):
#         edad = 2023 - self.fecha_nacimiento
#         return edad
    
#     def presentar(self):
#         print("Hola me llamo " + self.nombre + " " + self.apellido)


# martin = Persona("Martin", "Zalazar", 1.70, 2000)

# print("Mido", martin.altura)
# print("Tengo" , martin.calcularEdad() ,"años.")
# martin.presentar()

class Operacion:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(self):
        suma = self.numero1 + self.numero2
        return suma
    
    def restar(self):
        if self.numero1 > self.numero2:
            resultado = self.numero1 - self.numero2
        else:
            resultado = self.numero2 - self.numero1
        return resultado
    
    def multiplicar(self):
        resultado = self.numero1 * self.numero2
        return resultado
    
    def division(self):
        if self.numero2 == 0:
            mensaje = "Numero 2 es igual a 0 y no es posible realizar la division"
            return mensaje
        else:
            resultado = self.numero1/self.numero2
            return resultado

      

operacionUno = Operacion(4,3)
print(operacionUno.sumar())
print(operacionUno.restar())
print(operacionUno.multiplicar())
print(operacionUno.division())

#Modelar clase que se llame Circunferencia. Dicha clase tiene como atributos el radio y como metodos su area y perimetro
import math
class Circunferencia:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        resultado = math.pi * (self.radio**2)
        return resultado
    
    def perimetro(self):
        resultado = 2*math.pi*self.radio
        return resultado
    
circulo = Circunferencia(10)
print(circulo.perimetro())
print(circulo.area())