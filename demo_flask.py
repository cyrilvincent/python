import flask
import tp_function
import json
app = flask.Flask(__name__)

@app.route("/")
def root():
    return "<h1>Hello <font color='red'>World</font>!</h1>"

@app.route("/prime/<int:value>")
def prime(value):
    result = tp_function.is_prime(value)
    return str(result)

@app.route("/dict")
def dict():
    my_dict = {"toto": "titi", "value":7}
    return json.dumps(my_dict)

app.run(host="0.0.0.0")


