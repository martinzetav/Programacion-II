class Banco:

    def __init__(self, nombreBanco, saldoTotal, tasasInteres, listaClientes):
        self.nombreBanco = nombreBanco
        self.saldoTotal = saldoTotal
        self.tasasInteres = tasasInteres
        self.listaClientes = listaClientes

    def abrirCuenta(self):
        intereses = (self.saldoTotal * self.tasasInteres) / 100
        return self.saldoTotal + intereses
    
bancoNacion = Banco("Banco Nacion", 100000, 87, ["Pedro", "Esteban", "Jorge", "Francisco"])
print(bancoNacion.saldoTotal)
print(bancoNacion.abrirCuenta())