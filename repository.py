from typing import List
import media
import csv
import pickle
import json


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

class BookPickleRepository(GenericRepository):

    def __init__(self, path):
        super().__init__(path)

    def save(self, books: List[media.Book]):
        with open(self.path, "wb") as f:
            pickle.dump(books, f)

    def load(self) -> List[media.Book]:
        with open(self.path, "rb") as f:
            books = pickle.load(f)
            return books

class BookJsonRepository(GenericRepository):

    def __init__(self, path):
        super().__init__(path)

    def load(self) -> List[media.Book]:
        books = []
        with open(self.path) as f:
            l = json.load(f)
            for dict in l:
                book = media.Book(dict["title"], dict["price"])
                books.append(book)
        return books

    def save(self, books: List[media.Book]):
        res = []
        with open(self.path, "w") as f:
            for book in books:
                res.append({"title":book.title, "price":book.price})
            json.dump(res, f)






if __name__ == '__main__':
    repo = BookCsvRepository("data/media/books.csv")
    res = repo.load()
    for book in res:
        print(book.title, book.price)
    repo2 = BookCsvRepository("data/media/books2.csv")
    repo2.save(res)
    repo3 = BookPickleRepository("data/media/books.pickle")
    repo3.save(res)
    res = repo3.load()
    print(res)
    repo4 = BookJsonRepository("data/media/books.json")
    res = repo4.load()
    print(res)
    for book in res:
        print(book.title, book.price)
    repo5 = BookJsonRepository("data/media/books2.json")
    repo5.save(res)


