from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation Python")
        button = QPushButton("OK")
        self.setCentralWidget(button)
        self.setMinimumSize(QSize(640,480))


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()