import sys
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from main_window import Ui_MainWindow
from PyQt6 import QtWidgets


class MyApp(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.show()

    def pushButton_clicked(self):
        value = self.lineEdit.text()
        self.label.setText(f"H {value}")

   

app = QtWidgets.QApplication(sys.argv)
window = MyApp()
app.exec()
