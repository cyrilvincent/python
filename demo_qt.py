from PyQt5 import QtWidgets, uic
import sys
import media

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.okButton.clicked.connect(self.okButton_clicked)
        self.book = None
        self.show()

    def okButton_clicked(self):
        price = self.lineEdit.text()
        self.book = media.Book("0", "Python", float(price))
        self.lineEdit_2.setText(f"NetPrice: {self.book.net_price():.2f}")


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()