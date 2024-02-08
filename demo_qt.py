import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation Python")
        self.button = QPushButton("OK")
        self.count = 0
        self.button.clicked.connect(self.button_clicked)
        self.edit = QLineEdit()
        self.edit.textChanged.connect(self.editTextChanged)
        self.label = QLabel()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def button_clicked(self):
        self.count += 1
        self.button.setText(f"{self.count}")

    def editTextChanged(self):
        self.label.setText(self.edit.text())

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()