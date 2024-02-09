import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation Python")
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.button = QPushButton("+")
        self.button.setEnabled(False)
        self.label = QLabel()
        self.button.clicked.connect(self.button_clicked)
        self.edit1.textChanged.connect(self.edit_textChanged)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.edit1)
        self.layout.addWidget(self.edit2)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def button_clicked(self):
        try:
            value1 = float(self.edit1.text())
            value2 = float(self.edit2.text())
            res = value1 + value2
            self.label.setText(f"Le résultat est {res}")
        except:
            self.label.setText(f"Error")

    def edit_textChanged(self):
        try:
            value = float(self.edit1.text())
            self.button.setEnabled(True)
        except:
            self.label.setText(f"Error")



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()