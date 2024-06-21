from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic 

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("23-10-10/elementos/QLabel/ventana.ui", self)
        self.boton.clicked.connect(self.on_clicked)


    def on_clicked(self):
        if self.etiqueta.text().capitalize() == "Hola mUndo!".capitalize():
            self.etiqueta.setText("Chau mundo!")
        elif self.etiqueta.text().capitalize() == "Chau mundo!".capitalize():
            self.etiqueta.setText("Hola mundo!")





app = QApplication([])
win = MiVentana()

#Se utiliza win porque debemos llamar al atributo etiqueta
print(win.etiqueta.text()) #text trae el texto del label
# win.etiqueta.setText("Chau") 


win.show()
app.exec()

#EVENTOS: Son acciones que disparan señales y ejemplos de acciones pueden ser presionar una tecla, hacer click, etc
# Las señales se llaman TRIGGER
# Entonces al realizar una accion (click), se envia una señal la cual sera conectada con un metodo.
