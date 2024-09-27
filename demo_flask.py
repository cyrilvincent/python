# pip install Flask
import flask

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

if __name__ == '__main__':
    app.run(host="0.0.0.0")