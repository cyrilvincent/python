from PyQt6 import QtWidgets, uic
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/mock.ui", self)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
