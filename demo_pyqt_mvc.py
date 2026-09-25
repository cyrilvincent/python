from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
import main_window
import geometry

# Sauvegarder le MyMainWindow.ui dans ui/
# python -m PyQt6.uic.pyuic ui/MyMainWindow.ui > main_window.py
# importer le fichier généré
# Taper le bootstrap suivant

class MainWindow(QMainWindow, main_window.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_clicked)
        self.rectangle = geometry.Rectangle(0,0,geometry.Point(0,0))

    def button_clicked(self):
        width = int(self.lineEdit.text())
        length = int(self.lineEdit_2.text())
        self.rectangle.width = width
        self.rectangle.length = length
        area = self.rectangle.area()
        self.label.setText(f"{area}")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()