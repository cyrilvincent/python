from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PyQt6 import uic
import sys
import tp_function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

# c:\users\g-gre-fpa9\appdata\roaming\python\python311\site-packages
class Ui(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/MainWindow.ui", self)
        self.pushButton.clicked.connect(self.button_clicked)
        self.show()
        self.x = np.arange(0,10,0.1)
        self.y = self.x * np.sin(self.x)


    def button_clicked(self):  # Slot
        value = self.lineEdit.text()
        value = int(value)
        result = tp_function.is_prime(value)
        self.label.setText(f"Le nombre {value} est premier: {result}")
        plt.plot(self.x, self.y)
        plt.show()


app = QApplication(sys.argv)
window = Ui()
window.show()
app.exec()