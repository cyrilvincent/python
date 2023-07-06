from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow): # QDialog vient de widget.class dans .ui
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('ui/main.ui', self) # Load the .ui file
        self.label_2.setText("Hello")
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.show() # Show the GUI

    def pushButton_clicked(self):
        self.label_2.setText(f"{self.lineEdit.text()} Clicked")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
