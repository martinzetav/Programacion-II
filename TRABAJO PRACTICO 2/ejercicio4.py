class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return f"Depósito exitoso. Saldo actual: ${self.saldo}"
        else:
            return "El monto de depósito debe ser mayor que cero."

    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            return f"Retiro exitoso. Saldo actual: ${self.saldo}"
        else:
            return "No tiene fondos suficientes para realizar el retiro."

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo=0, limite_credito=0):
        super().__init__(titular, saldo)
        self.limite_credito = limite_credito

    def sobregiro(self, monto):
        if monto > 0 and monto <= self.limite_credito:
            self.saldo -= monto
            return f"Sobregiro exitoso. Saldo actual: ${self.saldo}"
        else:
            return "La cantidad de sobregiro no es válida o excede el límite de crédito."

class CuentaAhorros(CuentaBancaria):
    def __init__(self, titular, saldo=0, interes_anual=0):
        super().__init__(titular, saldo)
        self.interes_anual = interes_anual

    def calcular_intereses(self, meses):
        intereses = (self.saldo * self.interes_anual / 12) * meses
        self.saldo += intereses
        return f"Intereses ganados en {meses} meses: ${intereses}. Saldo actual: ${self.saldo}"

# Ejemplo de uso de las clases
cuenta_corriente = CuentaCorriente("Juan Pérez", 1000, 500)
cuenta_ahorros = CuentaAhorros("Ana López", 5000, 0.02)  # Tasa de interés anual del 2%

print("Cuenta Corriente:")
print(cuenta_corriente.titular)
print(cuenta_corriente.saldo)
print(cuenta_corriente.sobregiro(300))
print(cuenta_corriente.depositar(200))
print(cuenta_corriente.retirar(1500))

print("\nCuenta de Ahorros:")
print(cuenta_ahorros.titular)
print(cuenta_ahorros.saldo)
print(cuenta_ahorros.calcular_intereses(6))
print(cuenta_ahorros.retirar(1000))
