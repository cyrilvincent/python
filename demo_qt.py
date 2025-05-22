import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QLayout, QLineEdit, QLabel, QVBoxLayout, QWidget
import tp_function

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation Python")
        self.button = QPushButton("OK")
        self.lineEdit = QLineEdit()
        self.label = QLabel()
        self.layout = QVBoxLayout()
        self.errorLabel = QLabel("Erreur")
        self.errorLabel.setVisible(False)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.errorLabel)
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        try:
            nb = int(self.lineEdit.text())
            result = tp_function.is_prime(nb)
            self.label.setText(str(result))
            self.errorLabel.setVisible(False)
        except:
            self.errorLabel.setVisible(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


