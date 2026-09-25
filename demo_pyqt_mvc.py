from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
import main_window

# Sauvegarder le MyMainWindow.ui dans ui/
# python -m PyQt6.uic.pyuic ui/MyMainWindow.ui > main_window.py
# importer le fichier généré
# Taper le bootstrap suivant

class MainWindow(QMainWindow, main_window.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()