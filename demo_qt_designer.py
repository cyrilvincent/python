import PyQt6.QtWidgets as qt
import PyQt6.uic as uic
import sys

class Ui(qt.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/test.ui", self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.actionOpen.triggered.connect(self.pushButton_clicked)
        for i in range(10):
            self.listWidget.addItem(f"Python {i}")
        self.listWidget.currentItemChanged.connect(self.list_Widget_CurrentItemChanged)
        self.show()

    def pushButton_clicked(self):
        self.label_2.setText("Coucou")

    def list_Widget_CurrentItemChanged(self):
        print(self.listWidget.currentItem().text(), self.listWidget.currentRow())

if __name__ == '__main__':
    app = qt.QApplication(sys.argv)
    window = Ui()
    app.exec()

# Dans un module book_lib créer la fonction load(path) qui charge data/media/books.json avec le package json (json.load())
# Créer dans qtdesigner une fenetre qui affiche la liste des livres
# Créer un bouton add to cart
# Créer un label qui affiche la somme des livres ajouté au panier