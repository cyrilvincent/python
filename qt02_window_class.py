import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Fenetre(QWidget):
    def __init__(self, title):
        # QWidget.__init__(self)
        super().__init__()
        self.setWindowTitle(title)

if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    fen = Fenetre("Ma fenêtre")
    fen.show()

    app.exec_()