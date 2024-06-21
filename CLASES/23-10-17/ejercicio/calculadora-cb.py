from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic 


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("23-10-17/ejercicio/calculator.ui", self)
        # self.btn_calcular.clicked.connect(self.operacion)
        self.comboBox.currentTextChanged.connect(self.operacion)


    def sumar(self):
        num1 = int(self.numero1.text())
        num2 = int(self.numero2.text())
        resultado = num1 + num2
        self.lbl_resultado.setText(str(resultado))

    def restar(self):
        num1 = int(self.numero1.text())
        num2 = int(self.numero2.text())
        resultado = num1 - num2
        self.lbl_resultado.setText(str(resultado))
        
    def multiplicar(self):
        num1 = int(self.numero1.text())
        num2 = int(self.numero2.text())
        resultado = num1 * num2
        self.lbl_resultado.setText(str(resultado))

    def dividir(self):
        num1 = int(self.numero1.text())
        if self.numero2.text() != "0":
            num2 = int(self.numero2.text())
            resultado = num1 / num2
            self.lbl_resultado.setText(f"{resultado:.3f}")
        else:
            self.lbl_resultado.setText("ERROR")

    def potencia(self):
        num1 = int(self.numero1.text())
        num2 = int(self.numero2.text())
        resultado = num1 ** num2
        self.lbl_resultado.setText(str(resultado))

    def raiz(self):
        num1 = int(self.numero1.text())
        if num1 >=0:
            num2 = int(self.numero2.text())
            resultado = num1 ** (1/num2)
            self.lbl_resultado.setText(f"{resultado:.3f}")
        else:
            self.lbl_resultado.setText("ERROR")

    def operacion(self):
        if self.comboBox.currentText() == "SUMAR":
            self.sumar()
        elif self.comboBox.currentText() == "RESTAR":
            self.restar()
        elif self.comboBox.currentText() == "MULTIPLICAR":
            self.multiplicar()
        elif self.comboBox.currentText() == "DIVIDIR":
            self.dividir()
        elif self.comboBox.currentText() == "POTENCIA":
            self.potencia()
        else:
            self.raiz()
        
        






        

app = QApplication([])
win = MiVentana()


win.show()
app.exec()
