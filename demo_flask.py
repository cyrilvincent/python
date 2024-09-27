# pip install Flask
import flask
import tp3
import pandas as pd

app = flask.Flask(__name__)

@app.route("/")
def root():
    return "Hello World!!!!!"

@app.route("/toto/<x>")
def toto(x):
    return f"toto {x}"

@app.route("/add/<x>/<y>")
def add(x, y):
    x = int(x)
    y = int(y)
    return str(x + y)

# Importer tp3
# Créer la route isprime/7 qui répond True ou False

@app.route("/isprime/<x>")
def is_prime(x):
    x = int(x)
    return str(tp3.is_prime(x))

@app.route("/house/<surface>")
def house(surface):
    dataframe = pd.read_csv("data/house/house.csv")
    dataframe = dataframe[dataframe.surface < int(surface)]
    html = dataframe.to_html()
    return html

if __name__ == '__main__':
    app.run(host="0.0.0.0")