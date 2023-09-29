from PyQt5 import QtWidgets, uic
# pyqt5-tools
import sys
import tp_house

class Ui(QtWidgets.QMainWindow): # QDialog vient de widget.class dans .ui
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/main.ui', self) # Load the .ui file
        self.show() # Show the GUI
        self.lineEdit.setText("Hello")
        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.lineEdit.setText("Clicked")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()