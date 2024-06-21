from clases.jugadores import Jugador, Equipo

menu = '''### MENU ###
- 1 Agregar Jugador
- 2 Mostrar Jugadores
- 3 Ver Antiguedad
- 4 Ver Plazas Disponibles
- 5 Salir'''

opcion = "0"

equipo_nuevo = Equipo(11)

while opcion != "5":
    print(menu)
    opcion = input("Ingrese Opcion: ")
    if opcion == "1":
        nombre = input("Ingrese el NOMBRE del jugador: ")
        apellido = input("Ingrese el APELLIDO del jugador: ")
        numero = input("Ingrese el NUMERO del jugador: ")
        año_ingreso = int(input("Ingrese el AÑO DE INGRESO del jugador: "))
        jugador_ingresado = Jugador(nombre, apellido, numero, año_ingreso)
        equipo_nuevo.agregarJugador(jugador_ingresado)
    elif opcion == "2":
        equipo_nuevo.mostrarListado()
    elif opcion == "3":
        equipo_nuevo.jugadorJovenYVeterano()
    elif opcion == "4":
        equipo_nuevo.plazasDisponibles()
