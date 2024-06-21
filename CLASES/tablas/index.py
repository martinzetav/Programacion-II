from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt6 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("tablas/tabla.ui", self)
        self.boton_agregar.clicked.connect(self.agregar)
        self.boton_quitar.clicked.connect(self.eliminar)
        self.boton_editar.clicked.connect(self.editar)
        self.tabla.currentItemChanged.connect(self.seleccionar)


        # item = self.tabla.currentItem()
        # fila = item.row()

    def editar(self):
        nombre = self.text_nombre.text()
        apellido = self.text_apellido.text()

        self.tabla.setItem(self.tabla.currentRow(), 0, QTableWidgetItem(nombre))
        self.tabla.setItem(self.tabla.currentRow(), 1, QTableWidgetItem(apellido))


    def seleccionar(self):
        #Me traigo los valores seleccionados de la tabla
        nombre_fila = self.tabla.item(self.tabla.currentRow(),0).text()
        apellido_fila = self.tabla.item(self.tabla.currentRow(),1).text()

        self.text_nombre.setText(nombre_fila)
        self.text_apellido.setText(apellido_fila)


    def agregar(self):        
        cantidad_filas = self.tabla.rowCount() #Devuelve la cantidad de filas de mi tabla
        #Creo una fila nueva
        self.tabla.setRowCount(cantidad_filas+1) #Suma una fila mas en mi tabla
        #Traigo los datos para insertar en la fila
        nombre = self.text_nombre.text()
        apellido = self.text_apellido.text()
        #Inserto los datos en la fila nueva creada
        self.tabla.setItem(cantidad_filas, 0, QTableWidgetItem(nombre)) #Crea un item
        self.tabla.setItem(cantidad_filas, 1, QTableWidgetItem(apellido)) #Crea un item

        #Limpio los campos luego de agregar
        self.text_nombre.setText("")
        self.text_apellido.setText("")


    def eliminar(self):
        fila_actual = self.tabla.currentRow()
        self.tabla.removeRow(fila_actual)

 

app = QApplication([])
win = MiVentana()
win.show()
app.exec()