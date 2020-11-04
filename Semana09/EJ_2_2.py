import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap

class MiVentana(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
    
    def init_gui(self):
        self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('Crear Usuario')

        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 100, 100)

        ruta_imagen = os.path.join('img', 'usuario.jpg')

        pixeles = QPixmap(ruta_imagen)

        self.label.setPixmap(pixeles)
        
        self.label.setScaledContents(True)
        self.show()

if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana()
    sys.exit(app.exec_())