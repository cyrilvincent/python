from flask import Flask
app = Flask(__name__)
import demo_file

@app.route("/")
def root():
    return "Hello World"

@app.route("/html")
def html():
    loyers, surfaces = demo_file.parse_house_csv("")
    s = """
    <html><body><h1>Démo <b><i><font color="red">Red</font></i></b></h1>
    <table border="1">
    """
    for i in range(100):
        s+=f"<tr><td>A{i}</td><td>B{i}</td></tr>"
    s+="""
    </table>
    </body></html>
    """
    return s

if __name__ == '__main__':
    app.run(host="0.0.0.0")
