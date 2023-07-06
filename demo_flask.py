from flask import Flask
app = Flask(__name__)
import demo_file

@app.route("/")
def root():
    return "Hello World"

@app.route("/html")
def html():
    loyers, surfaces = demo_file.parse_house_csv("data/house/house.csv")
    s = """
    <html><body><h1>Démo <b><i><font color="red">Red</font></i></b></h1>
    <table border="1">
    <tr><td>Loyer</td><td>Surface</td></tr>
    """
    for loyer, surface in zip(loyers, surfaces):
        s+=f"<tr><td>{loyer}</td><td>{surface}</td></tr>"
    s+="""
    </table>
    </body></html>
    """
    return s

if __name__ == '__main__':
    app.run(host="0.0.0.0")
