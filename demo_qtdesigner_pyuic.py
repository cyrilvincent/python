import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QLayout, QLineEdit, QLabel, QVBoxLayout, QWidget
import tp_function
import mainwindow # python -m PyQt6.uic.pyuic ui\MainWindow.ui -o mainwindow.py
import mywidget # python -m PyQt6.uic.pyuic ui\MyWidget.ui -o mywidget.py

class MyWidget(QWidget, mywidget.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.mywidget = MyWidget()
        self.pushButton.clicked.connect(self.button_clicked)
        self.errorLabel.setVisible(False)
        self.actionPrime.triggered.connect(self.button_clicked)


    def button_clicked(self):
        try:
            nb = int(self.lineEdit.text())
            result = tp_function.is_prime(nb)
            self.label_2.setText(str(result))
            self.errorLabel.setVisible(False)
            self.mywidget.show()
        except:
            self.errorLabel.setVisible(True)
            self.label_2.setText("")





app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()


