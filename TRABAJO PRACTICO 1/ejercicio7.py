class Pelicula:
    def __init__(self, titulo, director, duracion, genero):
        self.titulo = titulo
        self.director = director
        self.duracion = duracion 
        self.genero = genero
    
    def reproducirPelicula(self):
        print(f"Titulo: {self.titulo}; Duracion: {self.duracion}")

    def recomendarPelicula(self, generoPreferido):
        if generoPreferido.capitalize() == self.genero.capitalize():
            print(f"La pelicula {self.titulo} es de tu genero preferido")
        else:
            print(f"No te recomiendo ver la pelicula {self.titulo}")


guerraMundialZ = Pelicula("Guerra Mundial Z", "Marc Forster", "01:56:00", "Accion")
genero = input("Ingrese si genero de pelicula preferido: ")
guerraMundialZ.recomendarPelicula(genero)