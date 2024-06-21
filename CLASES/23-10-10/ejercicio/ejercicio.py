from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic 

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("23-10-10/ejercicio/ventana.ui", self)
        self.btn_calcular.clicked.connect(self.sumar2)

    def sumar(self):
        num1 = int(self.numero1.text())
        num2 = int(self.numero2.text())
        resultado = num1 + num2
        self.lbl_resultado.setText(str(resultado))


    def sumar2(self):
        if self.numero1.text().isdigit() and self.numero2.text().isdigit():
            num1 = int(self.numero1.text())
            num2 = int(self.numero2.text())
            resultado = num1 + num2
            self.lbl_resultado.setText(str(resultado))
        elif self.numero1.text().isdigit() and not self.numero2.text().isdigit():
            num1 = int(self.numero1.text())
            self.numero2.clear()
            self.lbl_resultado.setText(str(num1))
        elif self.numero2.text().isdigit() and not self.numero1.text().isdigit():
            num2 = int(self.numero2.text())
            self.numero1.clear()
            self.lbl_resultado.setText(str(num2))
        else:
            self.numero1.clear()
            self.numero2.clear()
        







app = QApplication([])
win = MiVentana()


win.show()
app.exec()