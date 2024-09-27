import PyQt6.QtWidgets as qt
import PyQt6.uic as uic
import sys

class Ui(qt.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/test.ui", self)
        self.show()

if __name__ == '__main__':
    app = qt.QApplication(sys.argv)
    window = Ui()
    app.exec()