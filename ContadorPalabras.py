import sys
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        #Carga de nuestra vista
        uic.loadUi("ContadorPalabras.ui",self)
        self.btnContar.clicked.connect(self.ContarPalabras)


    def ContarPalabras(self):
        # Recuperar el texto 
        texto = self.edtCaracteres.text()

        # Separar las palabras
        textoSeparado = texto.split()
        print(textoSeparado)
        
        # Contar las palabras
        # Contar los caracteres   

app = QtWidgets.QApplication(sys.argv)        
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec_())