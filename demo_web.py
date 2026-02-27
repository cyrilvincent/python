from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return "Hello World"

@app.route("/html")
def html():
    return """<h1>Gros titre</h1><br>Voici du texte <b>en gras</b> et en <i>italique</i><br>
    <font color="red">En rouge</font>"""

@app.route("/add/<int:i>/<int:j>")
def add(i, j):
    return f"{i}+{j}={i+j}"

app.run()
