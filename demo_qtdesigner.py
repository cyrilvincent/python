import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QLayout, QLineEdit, QLabel, QVBoxLayout, QWidget
import tp_function

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/MainWindow.ui", self)
        self.pushButton.clicked.connect(self.button_clicked)
        self.errorLabel.setVisible(False)
        self.actionPrime.triggered.connect(self.button_clicked)


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


