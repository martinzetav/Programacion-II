from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6 import uic 

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("23-10-17/miventana.ui", self)
        # self.comboBox.currentIndexChanged.connect(self.onChange)
        self.comboBox.currentTextChanged.connect(self.onChange)
        self.btnRemove.clicked.connect(self.onRemove)
        self.btnAdd.clicked.connect(self.onAdd)

# onChange: La interaccion se realiza cuando cambio de elemento en el combo box y no cuando hago click como tal.
    def onChange(self):
        print(self.comboBox.currentText())
        print(self.comboBox.currentIndex())

    def onRemove(self):
        msg = QMessageBox()
        msg.setWindowTitle("Advertencia")
        msg.setText("¿Desea eliminar la provincia seleccionada?")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        respuesta = msg.exec()
        
        if respuesta == QMessageBox.StandardButton.Yes:
            index = self.comboBox.currentIndex()
            self.comboBox.removeItem(index)

        if self.comboBox.count() == 0:
            self.btnRemove.setEnabled(False)


    def onAdd(self):
        text = self.addText.text()
        self.comboBox.addItem(text)


        

app = QApplication([])
win = MiVentana()


win.show()
app.exec()

#METODOS DE COMBO BOX
# - .currentText() -> estoy llamando al texto relacionado en el momento de hacer click sobre el elemento del combo box y no click como tal.
# - .currentIndex() -> estoy llamando la posicion del elemento seleccionado
# - .count() -> indica la cantidad de opciones/elementos
# - .addItem("texto") -> agrega un elemento al combo 
# - .removeItem(indice) -> elimina un elemento del combo 