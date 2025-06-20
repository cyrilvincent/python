# python -m PyQt6.uic.pyuic ui\MainWindow.ui -o generated_ui.py

import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QLayout, QLineEdit, QLabel, QVBoxLayout, QWidget
import tp_function
import generated_ui

class MainWindow(QMainWindow, generated_ui.Ui_MainWindow):


    # 1 Taper la commande : python -m PyQt6.uic.pyuic ui\NomDeVotreUi.ui -o generated_ui.py
    # 2 import generated_ui
    # 3 Ajouter l'héritage generated_ui.Ui_MainWindow
    # 4 Remplacer uic.loadUi par self.setupUi(self)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.pushButton.clicked.connect(self.button_clicked)
        # self.errorLabel.setVisible(False)
        # self.actionPrime.triggered.connect(self.button_clicked)



    def button_clicked(self):
        try:
            nb = int(self.lineEdit.text())
            result = tp_function.is_prime(nb)
            self.label_2.setText(str(result))
            self.errorLabel.setVisible(False)
        except:
            self.errorLabel.setVisible(True)
            self.label_2.setText("")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


