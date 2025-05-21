import flask
import tp_function

app = flask.Flask(__name__)

@app.route("/")
def root():
    return "<b>Hello</b> <font color='red'>World</font>!"

@app.route("/prime/<int:nb>")
def prime(nb: int):
    return str(tp_function.is_prime(nb))

app.run(host="0.0.0.0")


