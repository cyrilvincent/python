import sys

from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout
import repository

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formation Python")
        self.edit = QLineEdit()
        self.button = QPushButton("Search")
        self.label = QLabel()
        self.button.clicked.connect(self.button_clicked)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.edit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)
        self.repository = repository.BookCsvRepository("data/media/books.csv")
        self.books = self.repository.load()
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def button_clicked(self):
        title = self.edit.text().upper()
        book = None
        for b in self.books:
            if title in b.title.upper():
                book = b
                break
        if book != None:
            self.label.setText(f"{book.price}")





app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()