from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic 

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("23-10-25/MessageBox/ventana.ui", self)
        self.mensaje.clicked.connect(self.on_mensaje)

    def on_mensaje(self):
        msg = QMessageBox()
        msg.setWindowTitle("Titulo de mensaje")
        msg.setText("Este es un mensaje")
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel)

        respuesta = msg.exec()

        if respuesta == QMessageBox.StandardButton.Yes:
            print("Eligio SI")
        elif respuesta == QMessageBox.StandardButton.No:
            print("Eligio NO")
        else:
            print("Eligio CANCELAR")


        

app = QApplication([])
win = MiVentana()


win.show()
app.exec()