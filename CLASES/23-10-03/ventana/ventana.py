from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic 

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("23-10-03/ventana/ventana.ui", self)

app = QApplication([])
win = MiVentana()

print(win.cosito.text())

win.show()
app.exec()