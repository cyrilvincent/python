from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout
import sys
import demo_function


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation Python")
        self.label = QLabel("Du texte")
        self.errorLabel = QLabel()
        self.setVisible(False)
        self.edit = QLineEdit()
        self.button = QPushButton("OK")
        # self.setCentralWidget(self.button)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.errorLabel)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)


        self.setMinimumSize(QSize(640,480))
        self.button.clicked.connect(self.button_clicked)
        # self.edit.textChanged.connect(self.button_clicked)
        self.nb = 0

    def button_clicked(self):
        self.nb += 1
        # self.button.setText(f"Clicked {self.nb}")
        # self.label.setText(f"Vous avez saisi {self.edit.text()} {self.nb}")
        try:
            nb = int(self.edit.text())
            result = demo_function.factorielle(nb)
            self.label.setText(f"{nb}!={result}")
            self.errorLabel.setVisible(False)
        except ValueError as ex:
            self.errorLabel.setText(str(ex))
            self.errorLabel.setVisible(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()