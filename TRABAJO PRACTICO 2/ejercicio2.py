class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def obtener_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"
    
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_carroceria, cilindraje):
        super().__init__(marca, modelo, año)
        self.tipo_carroceria = tipo_carroceria
        self.cilindraje = cilindraje

    def calcular_impuesto(self):
        impuesto = 0
        if self.año >= 2023:
            impuesto = self.cilindraje * 2
        return impuesto


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_motor, potencia):
        super().__init__(marca, modelo, año)
        self.tipo_motor = tipo_motor
        self.potencia = potencia

    def calcular_seguro(self):
        costo_seguro = 100 + self.potencia
        return costo_seguro


class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, carga_maxima):
        super().__init__(marca, modelo, año)
        self.carga_maxima = carga_maxima

    def verificar_carga(self, carga_actual):
        if carga_actual > self.carga_maxima:
            return "¡Cuidado! La carga actual supera la carga máxima permitida."
        else:
            return "Carga dentro de los límites permitidos."

