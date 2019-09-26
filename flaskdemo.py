import flask
import media
import jsonpickle

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello World from Cyril"

@app.route("/html")
def html():
    db = media.BookDb("data/books.db3")
    books = db.getAll()
    s = f"""
        <html>
            <head>
                <title>Python</title>
            </head>
            <body>
                <p>Hello <b>Worl<i>d!</i></b></p>
                <p>
                    <table border="1">"""
    for b in books:
        s += f"<tr><td>{b.title}</td><td>{b.price}</td></tr>"
    s+="""    </table>
                <p>
            </body>
        </html>
    """
    return s

@app.route("/json/<title>")
def jsonpage(title):
    db = media.BookDb("data/books.db3")
    b = list(db.getByTitle(title))
    s = jsonpickle.encode(b, unpicklable=False)
    return s

if __name__ == '__main__':
    app.run("0.0.0.0")