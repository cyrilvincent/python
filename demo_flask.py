import flask
import tp_function
import demo_dico

app = flask.Flask(__name__)

@app.route("/")
def root():
    return "<b>Hello</b> <font color='red'>World</font>!"

@app.route("/prime/<int:nb>")
def prime(nb: int):
    return str(tp_function.is_prime(nb))

@app.route("/config")
def config():
    return demo_dico.config

@app.route("/instrument/<int:id>")
def instrument(id: int):
    return demo_dico.config


app.run(host="0.0.0.0")


