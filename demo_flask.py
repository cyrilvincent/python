import flask
import my_package.tp_function as tp

app = flask.Flask(__name__)

@app.route("/")
def root():
    return "Hello World!"

@app.route("/is_prime/<int:n>")
def is_prime(n):
    res = tp.is_prime(n)
    return f"is prime: {res}"

@app.route("/html")
def html():
    return """
    <html>
    <body>
    <h1>Hello <b>World<font color='red'>!</font></b></h1>
    blah blah
    """

app.run("0.0.0.0")