import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation Python")
        self.button = QPushButton("OK")

        self.setCentralWidget(self.button)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.button.setText("Clicked")
        self.setWindowTitle("Clicked")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


