from flask import Flask
import pandas as pd
import tp_function
import numpy as np
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def root():
    return "Hello World!"

@app.route("/toto")
def toto():
    return "TOTO"

@app.route("/isprime/<int:x>")
def is_prime(x):
    result = tp_function.is_prime(x)
    if result == True:
        return f"Le nombre {x} est premier"
    else:
        return f"Le nombre {x} n'est pas premier"

@app.route("/house")
def house():
    dataframe = pd.read_csv("data/house/house.csv")
    html = dataframe.to_html()
    return html
# TP
# Reprendre mon code
# Ajouter une variable dans /house/200 qui filtre les houses par surface < 200
# Créer la route /house/describe qui affiche le describe(), describe retourne un dataframe, to_html

@app.route("/xsinx")
def xsinx():
    x = np.arange(0, 10, 0.1)
    y = x * np.sin(x)
    plt.plot(x, y)
    plt.savefig("data/fig.png")
    return f"<img src='/data/fig.png'>"





app.run(host="0.0.0.0")