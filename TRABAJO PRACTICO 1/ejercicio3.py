class TiendaOnline:
    
    def __init__(self,  nombreTienda, productosDisponibles, ubicacion, ventasMensuales):
        self.nombreTienda = nombreTienda
        self.productosDisponibles = productosDisponibles
        self.ubicacion = ubicacion
        self.ventasMensuales = ventasMensuales

    def buscarProducto(self, producto):
        if producto.capitalize() in self.productosDisponibles:
            return "El producto " + producto + " esta DISPONIBLE"
        else:
            return "El producto no esta disponible"
        
    def calcularDescuento(self, montoCompra):
        if montoCompra >= 200:
            precio = montoCompra - (montoCompra * 0.20)
        elif montoCompra >= 100:
            precio = montoCompra - (montoCompra * 0.10)
        else:
            return "No hay descuento, debera pagar $" + str(montoCompra)
        return "El precio total con el descuento aplicado es " + str(precio)


tienda = TiendaOnline("Super Oscar", ["Coca", "Gaseosa", "Mani", "Tutuca"], "Chuquisaca", 200)
print(tienda.buscarProducto("coca"))
print(tienda.calcularDescuento(300))


