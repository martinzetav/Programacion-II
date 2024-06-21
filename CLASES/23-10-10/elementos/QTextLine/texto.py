from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic 

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("23-10-10/elementos/QTextLine/ventana.ui", self)
        self.boton.clicked.connect(self.boton_click)

    def boton_click(self):
        print(self.texto.text())
        self.texto.setText("")


app = QApplication([])
win = MiVentana()


win.show()
app.exec()