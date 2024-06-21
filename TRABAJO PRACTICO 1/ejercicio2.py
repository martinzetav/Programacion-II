class Libro:
    
    def __init__(self, titulo, autor, anioPublicacion, disponible):
        self.titulo = titulo
        self.autor = autor
        self.anioPublicacion = anioPublicacion
        self.disponible = disponible

    def solicitarPrestamo(self):
        if self.disponible:
            self.disponible = False
            return "El libro ha sido prestado"
        else:
            return "El libro no puede ser prestado"
    
    def devolverLibro(self, dias):
        if dias > 7:
            return "La multa es de $2500"
        else:
            return "El libro ha sido devuelto"


libro = Libro("Tarzan", "Jerome", "2000", True)
print(libro.disponible)
print(libro.solicitarPrestamo())
print(libro.devolverLibro(3))

