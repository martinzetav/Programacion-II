#Crear una clase "Equipo" que guarde una lista de objetos "Jugador"
# --------------- Clase JUGADOR --------------
class Jugador:
    def __init__(self, nombre, apellido, numero, anioDeIngreso):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.anioDeIngreso = anioDeIngreso

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nNumero: {self.numero}\nAño de Ingreso: {self.anioDeIngreso}"

# --------------- Clase EQUIPO --------------
class Equipo:
    def __init__(self, cantidadMaxima):
        self.cantidadMaxima = cantidadMaxima
        self.listaJugadores = []*self.cantidadMaxima

    def agregarJugador(self, jugador):
        self.listaJugadores.append(jugador)

    def mostrarListado(self):
        for jugador in self.listaJugadores:
            print(jugador)
            print("-----------------------------")

    def jugadorJovenYVeterano(self):
        masJoven = self.listaJugadores[0]
        masVeterano = self.listaJugadores[0]
        for jugador in self.listaJugadores:
            if jugador.anioDeIngreso > masJoven.anioDeIngreso:
                masJoven = jugador
            elif jugador.anioDeIngreso < masVeterano.anioDeIngreso:
                masVeterano = jugador
        print(f"El jugador mas JOVEN es {masJoven.nombre} {masJoven.apellido} que ingreso en el año {masJoven.anioDeIngreso} y el jugador mas VETERANO es {masVeterano.nombre} {masVeterano.apellido} que ingreso en el año {masVeterano.anioDeIngreso}")

#----- Otra alternativa para saber jugador mas joven y mas veterano, utilizando lambda
    # def mostrar_jugador(self, jugador):
    #     print(f"Nombre: {self.nombre}\nApellido: {self.apellido}\nNumero: {self.numero}\nAño de Ingreso: {self.anioDeIngreso}")

    # def jugadorNuevoVereranoDos(self):
    #     jugador_viejo = min(self.listaJugadores, key = lambda x : x.anioIngreso)
    #     jugador_nuevo = max(self.listaJugadores, key = lambda x : x.anioIngreso)
    #     print(self.mostrar_jugador(jugador_viejo))
    #     print(self.mostrar_jugador(jugador_nuevo))

#--- Otra alternativa valida pero mas larga para saber el jugador mas joven y el mas veterano ---
    # def jugadorMasViejoYMasJoven(self):
    #     f = 0          
    #     for jugador in self.listaJugadores:
    #         if f == 0:
    #             masJoven = jugador
    #             masVeterano = jugador
    #             f = 1
    #         if jugador.anioDeIngreso > masJoven.anioDeIngreso:
    #             masJoven = jugador
    #         elif jugador.anioDeIngreso < masVeterano.anioDeIngreso:
    #             masVeterano = jugador
    #     print(f"El jugador mas JOVEN es {masJoven.nombre} {masJoven.apellido} que ingreso en el año {masJoven.anioDeIngreso} y el jugador mas VETERANO es {masVeterano.nombre} {masVeterano.apellido} que ingreso en el año {masVeterano.anioDeIngreso}")

    def plazasDisponibles(self):
        plazasDisponibles = self.cantidadMaxima - len(self.listaJugadores)
        print(f"Hay {plazasDisponibles} lugares disponibles de {self.cantidadMaxima} lugares")

equipo1 = Equipo(11)

#----------------------- MENU ------------------

opcion = 5
while opcion != 4:
    opcion = int(input("Ingrese una Opcion:\n1. Agregar Jugador\n2. Mostrar Listado\n3. Mostrar jugador mas joven y mas viejo\n4. Salir\n"))
    if opcion == 1:
        nombre = input("Ingrese el NOMBRE del jugador: ")
        apellido = input("Ingrese el APELLIDO del jugador: ")
        numero = input("Ingrese el NUMERO del jugador: ")
        anio = int(input("Ingrese el AÑO DE INGRESO del jugador: "))

        jugadorUno = Jugador(nombre, apellido, numero, anio)
        equipo1.agregarJugador(jugadorUno)
        print("----- JUGADOR AGREGADO EXITOSAMENTE")
    elif opcion == 2:
        equipo1.mostrarListado()
    elif opcion == 3:
        equipo1.jugadorJovenYVeterano()

print("PROGRAMA FINALIZADO")
