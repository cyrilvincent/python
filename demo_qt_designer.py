import PyQt6.QtWidgets as qt
import PyQt6.uic as uic
import sys

class Ui(qt.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/test.ui", self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.actionOpen.triggered.connect(self.pushButton_clicked)
        self.show()

    def pushButton_clicked(self):
        self.label_2.setText("Coucou")

if __name__ == '__main__':
    app = qt.QApplication(sys.argv)
    window = Ui()
    app.exec()