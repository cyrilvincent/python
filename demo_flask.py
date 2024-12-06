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

@app.route("/house/<int:surface>/<type>")
def house(surface, type):
    dataframe = pd.read_csv("data/house/house.csv")
    dataframe = dataframe[dataframe.surface < surface]
    if type == "html":
        return dataframe.to_html(index=False)
    elif type == "csv":
        return dataframe.to_csv(index=False)
    elif type == "excel":
        return dataframe.to_excel(index=False)
    else:
        return dataframe.to_json(index=False)

@app.route("/house/describe")
def describe():
    dataframe = pd.read_csv("data/house/house.csv")
    describe = dataframe.describe()
    return describe.to_html(index=False)

# TP
# Reprendre mon code
# Ajouter une variable dans /house/200 qui filtre les houses par surface < 200
# Créer la route /house/describe qui affiche le describe(), describe retourne un dataframe, to_html







app.run(host="0.0.0.0")