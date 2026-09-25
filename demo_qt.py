import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# app = QApplication(sys.argv)
#
# window = QMainWindow()
# window.show()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation Python")
        button = QPushButton("OK")
        self.setCentralWidget(button)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()