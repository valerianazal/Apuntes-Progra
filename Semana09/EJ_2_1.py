import sys
from PyQt5.QtWidgets import QWidget, QApplication

class MiVentana(QWidget):
    def __init__(self, x, y, ancho, alto, nombre):
        super().__init__()
        self.setGeometry(x, y, ancho, alto)
        self.setWindowTitle(nombre)


if __name__ == '__main__':
    app = QApplication([])
    ventana = MiVentana(200, 100, 300, 300, 'Hola')
    ventana2 = MiVentana(500, 100, 400, 200, 'Chao')
    ventana.show()
    ventana2.show()
    sys.exit(app.exec_())