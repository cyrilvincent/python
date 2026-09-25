import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel

# app = QApplication(sys.argv)
#
# window = QMainWindow()
# window.show()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation Python")
        self.button = QPushButton("OK")
        self.lineEdit = QLineEdit()
        self.label = QLabel()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        self.button.clicked.connect(self.button_clicked)
        self.i = 0

    def button_clicked(self):
        self.i += 1
        self.label.setText(f"Clicked {self.i} {self.lineEdit.text()}")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()