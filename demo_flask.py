from flask import Flask
import repository

app = Flask(__name__)

@app.route("/")
def hello():
    repo = repository.BookCsvRepository("data/media/books.csv")
    books = repo.load()
    s = """
    <html><body><h1>Hello World <font color="red">!</font></h1>
    <table border='1'>"""
    for book in books:
        s += f"<tr><td>{book.title}</td><td>{book.price}</td></tr>"
    s += """
    </table>
    </body></html>
    """
    return s

@app.route("/toto")
def toto():
    return "toto"

app.run()

