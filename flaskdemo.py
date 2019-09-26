import flask
import media

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello World from Cyril"

@app.route("/html")
def html():
    b = media.Book("Python",10,1)
    return f"""
        <html>
            <head>
                <title>Python</title>
            </head>
            <body>
                <p>Hello <b>Worl<i>d!</i></b></p>
                <p>
                    <table border="1">
                        <tr><td>{b.title}</td><td>{b.price}</td></tr>
                        <tr><td>C</td><td>D</td></tr>
                    </table>
                <p>
            </body>
        </html>
    """

if __name__ == '__main__':
    app.run("0.0.0.0")