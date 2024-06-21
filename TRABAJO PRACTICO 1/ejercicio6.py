class ProductoElectronico:
    def __init__(self, nombre, marca, precio, disponible):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.disponible = disponible

    def compraProducto(self):
        self.disponible = False
    
    def garantiaProducto(self, defecto):
        siTiene = ["SI","Si","si","sI"]
        noTiene = ["NO", "No", "no", "nO"]
        if defecto in siTiene:
            print("Hay garantia porque el producto esta dañado")
        elif defecto in noTiene:
            print("El producto esta en buen esta, no hay garantia")   

pavaElectica = ProductoElectronico("Pava Electrica", "PHILIPS", 23000, True)
pavaElectica.compraProducto()
garantia = input('¿El producto esta dañado? RESPONDA CON "SI" O "NO"')
pavaElectica.garantiaProducto("si")