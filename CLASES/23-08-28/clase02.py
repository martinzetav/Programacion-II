#Modelar una clase "Agenda" y una clase "Contacto"
#Agenda ---> lista de contactos[list] (atributo)
# La listaContactos es un listado de objetos de tipo Contacto
#Contacto ---> nombre [str], apellido[str], telefono[int] (atributo)

class Contacto:

    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre}, {self.apellido}, {self.telefono}"
    

class Agenda:
    
    def __init__(self):
        self.listadoContactos = []

    def agregarContacto(self, contacto):
        self.listadoContactos.append(contacto)

    def mostrarContacto(self):
        for elemento in self.listadoContactos:
            print(elemento)

    

# contacto1 = Contacto("Jose", "Perez", 3804748212)
# contacto2 = Contacto("Maria", "Lopez", 3804094891)
# contacto3 = Contacto("Luciano", "Moreno", 3804489120)

# listaContactos = []
# listaContactos.append(contacto1)
# listaContactos.append(contacto2)
# listaContactos.append(contacto3)

# for elemento in listaContactos:
#     print(elemento)

agenda1 = Agenda()
# agenda1.agregarContacto(contacto1)
# agenda1.agregarContacto(contacto2)
# agenda1.agregarContacto(contacto3)
# agenda1.mostrarContacto()

opcion = "0"
while opcion != "3":
    opcion = input("Ingrese una Opcion:\n1. Agregar Contacto\n2. MostrarListado\n3. Salir\n")
    if opcion == "1":
        nombre = input("Ingrese el NOMBRE:\n")
        apellido = input("Ingrese el APELLIDO:\n")
        telefono = input("Ingrese el TELEFONO:\n")
        contacto1 = Contacto(nombre, apellido, telefono)
        agenda1.agregarContacto(contacto1)
        print("Contacto Guardado")
        
    elif opcion == "2":
        agenda1.mostrarContacto()




