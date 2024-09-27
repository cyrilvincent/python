# from PyQt6.QtCore import QSize
# from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

import PyQt6.QtWidgets as qt
import PyQt6.QtCore as qtc
import sys
import tp3

class MainWindow(qt.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation")
        self.label = qt.QLabel("Saisir un nombre")
        self.lineEdit = qt.QLineEdit()
        self.button = qt.QPushButton("OK")
        self.setMinimumSize(qtc.QSize(400,300))
        self.layout = qt.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button)
        container = qt.QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        self.button.clicked.connect(self.button_clicked)
        # button.clicked.connect(self.button_clicked2)
        # self.lineEdit.textChanged.connect(self.lineEdit_textChanged)

    def button_clicked(self):
        # self.label.setText("")
        # self.lineEdit.setText("")
        x = int(self.lineEdit.text())
        res = tp3.is_prime(x)
        if res == True:
            self.label.setText(f"Le nombre {x} est premier")
        else:
            self.label.setText(f"Le nombre {x} n'est pas premier")

    def lineEdit_textChanged(self):
        self.label.setText(self.lineEdit.text())





if __name__ == '__main__':
    print(sys.executable)
    app = qt.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

