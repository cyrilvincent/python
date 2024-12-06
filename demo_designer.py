from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QLabel
from PyQt6 import uic
import sys
import tp_function
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import house_library as house

# c:\users\g-gre-fpa9\appdata\roaming\python\python311\site-packages
class Ui(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/MainWindow.ui", self)
        self.pushButton.clicked.connect(self.button_clicked)
        self.show()
        self.label_2.setVisible(False)
        self.df = house.load("data/house/house.csv")


    def button_clicked(self):  # Slot
        try:
            value = self.lineEdit.text()
            value = int(value)
            # result = tp_function.is_prime(value)
            # self.label.setText(f"Le nombre {value} est premier: {result}")
            df = house.filter(self.df, value)
            surface_mean, surface_std, loyer_mean, loyer_std = house.stats(df)
            self.label.setVisible(True)
            self.label_2.setVisible(False)
            self.label.setText(
                f"Surface mean={surface_mean:.2f} Surface std={surface_std:.2f} Loyer mean={loyer_mean:.2f} Loyer std={loyer_std:.2f}")
            house.show()
        except:
            self.label.setText(f"Erreur merci de saisir un entier")
            self.label.setVisible(False)
            self.label_2.setVisible(True)
        plt.plot(self.x, self.y)


app = QApplication(sys.argv)
window = Ui()
window.show()
app.exec()