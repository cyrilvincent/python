# from PyQt6.QtCore import QSize
# from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton

import PyQt6.QtWidgets as qt
import PyQt6.QtCore as qtc
import sys

class MainWindow(qt.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation")
        self.label = qt.QLabel("Bonjour")
        self.lineEdit = qt.QLineEdit()
        self.button = qt.QPushButton("Reset")
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
        self.lineEdit.textChanged.connect(self.lineEdit_textChanged)

    def button_clicked(self):
        self.label.setText("")
        self.lineEdit.setText("")

    def lineEdit_textChanged(self):
        self.label.setText(self.lineEdit.text())





if __name__ == '__main__':
    app = qt.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

