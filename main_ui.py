import sys

from PyQt6.QtWidgets import QMainWindow
from base_ui import Ui_MainWindow
from PyQt6 import QtWidgets, uic

class MyApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.show()

    def pushButton_clicked(self):
        value = self.myLineEdit.text()
        self.label.setText(f"Hello {value}")

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
app.exec()

# pip install PyQt6
# Download qtdesigner
# Créer répertoire ui/
# Sauvegarder dans main.ui
# Taper  Python -m PyQt6.uic.pyuic .\ui\main.ui -o base_ui.py
# Puis le code ci dessus