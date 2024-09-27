import PyQt6.QtWidgets as qt
import PyQt6.uic as uic
import sys
import book_lib

class Ui(qt.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("ui/test.ui", self)
        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.actionOpen.triggered.connect(self.pushButton_clicked)
        self.books = book_lib.load("data/media/books.json")
        self.prices = []
        for book in self.books:
            self.listWidget.addItem(book["title"])
        self.listWidget.currentItemChanged.connect(self.list_Widget_CurrentItemChanged)
        self.show()

    def pushButton_clicked(self):
        self.prices=[]
        self.label_2.setText(f"Vide")

    def list_Widget_CurrentItemChanged(self):
        # print(self.listWidget.currentItem().text(), self.listWidget.currentRow())
        row_num = self.listWidget.currentRow()
        self.prices.append(float(self.books[row_num]["price"]))
        total = sum(self.prices)
        self.label_2.setText(f"Le total est {total}")

if __name__ == '__main__':
    app = qt.QApplication(sys.argv)
    window = Ui()
    app.exec()

# Dans un module book_lib créer la fonction load(path) qui charge data/media/books.json avec le package json (json.load())
# Créer dans qtdesigner une fenetre qui affiche la liste des livres
# Créer un bouton add to cart
# Créer un label qui affiche la somme des livres ajouté au panier