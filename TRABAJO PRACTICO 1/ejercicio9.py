class Empleado:
    def __init__(self, nombre, edad, salario, cargoEmpleado):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargoEmpleado = cargoEmpleado

    def aumentoSalario(self, porcentaje):
        if porcentaje > 0:
            nuevoSalario = (self.salario * porcentaje) / 100
            self.salario += nuevoSalario

    def cambiarCargo(self, cargo):
        self.cargoEmpleado = cargo
    

empleadoUno = Empleado("Roberto", 36, 11000, "Ordenanza")
empleadoUno.cambiarCargo("Administracion")
print(empleadoUno.cargoEmpleado)