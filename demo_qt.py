import sys
from PyQt6.QtCore import QSize, pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel
import tp_function

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation Python")
        self.setMinimumSize(QSize(800, 600))
        self.button = QPushButton("OK")
        self.button.clicked.connect(self.button_clicked)
        self.input = QLineEdit()
        self.input.textChanged.connect(self.button_clicked)
        self.label = QLabel()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.input)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)
        self.i = 0

    @pyqtSlot()
    def button_clicked(self):
        self.setWindowTitle("Clicked")
        self.i += 1
        value = self.input.text()
        # self.label.setText(f"Clicked {self.i} times: {value}")
        value = int(value)
        result = tp_function.is_prime(value)
        self.label.setText(f"Le nombre {value} est premier: {result}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()