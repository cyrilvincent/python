import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/ping")
def ping():
    return "pong"

if __name__ == '__main__':
    app.run(host="0.0.0.0")