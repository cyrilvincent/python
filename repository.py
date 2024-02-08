from typing import List
import media
import csv


class GenericRepository:

    def __init__(self,path:str):
        self.path = path

    def load(self) -> List[media.Book]:
        pass

    def save(self, books: List[media.Book]):
        pass

class BookCsvRepository(GenericRepository):

    def __init__(self, path):
        super().__init__(path)

    def load(self) -> List[media.Book]:
        books = []
        with open(self.path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                title = row["title"]
                price = float(row["price"])
                book = media.Book(title, price)
                books.append(book)
        return books

    def save(self, books: List[media.Book]):
        with open(self.path, "w") as f:
            f.write("title,price\n")
            for book in books:
                f.write(f"{book.title},{book.price}\n")

if __name__ == '__main__':
    repo = BookCsvRepository("data/media/books.csv")
    res = repo.load()
    for book in res:
        print(book.title, book.price)
    repo2 = BookCsvRepository("data/media/books2.csv")
    repo2.save(res)


