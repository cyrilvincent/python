from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PyQt6 import uic
import sys
import tp_function

# c:\users\g-gre-fpa9\appdata\roaming\python\python311\site-packages

class Ui(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/MainWindow.ui", self)
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):  # Slot
        value = self.lineEdit.text()
        value = int(value)
        result = tp_function.is_prime(value)
        self.label.setText(f"Le nombre {value} est premier: {result}")

app = QApplication(sys.argv)
window = Ui()
window.show()
app.exec()