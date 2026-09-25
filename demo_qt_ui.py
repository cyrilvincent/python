import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel
from PyQt6 import uic

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/MainWindow.ui", self)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()