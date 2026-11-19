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
        cantidadPalabras = len(textoSeparado)
        self.tvPalabras.setText(f"Palabras:{cantidadPalabras}")
        # Contar los caracteres   
        totalCaracteres = 0
        for palabra in textoSeparado:
            totalCaracteres += len(palabra)
        totalCaracteres
        self.tvCaracteres.setText(f"Caracteres: {totalCaracteres}")    


app = QtWidgets.QApplication(sys.argv)        
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec_())