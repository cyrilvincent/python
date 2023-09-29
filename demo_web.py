import flask
import tp_function
import tp_house
app = flask.Flask(__name__)


@app.route("/")
def root():
    return f"Hello World! {tp_function.is_prime(7)}"

@app.route("/html")
def html():
    return """
        <html>
        <body>
        <h1><font color="red">Hello</font>
        <b>W</b><i>orld</i></h1>
        <a href="/">Link</a>
        </body></html>
    """

@app.route("/house")
def house():
    loyers, surfaces = tp_house.load_csv("data/house/house.csv")
    s = "<html><body><h1>House</h1><table border='1'>"
    for tuple in zip(loyers, surfaces):
        s += f"<tr><td>{tuple[0]}</td><td>{tuple[1]}</td></tr>"
    s+="</table></body></html>"
    return s

if __name__ == '__main__':
    app.run()

