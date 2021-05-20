import flask

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/ping")
def ping():
    return "pong"

@app.route("/html")
def html():
    loyers = [1000, 2000, 3000]
    surfaces = [50, 100, 200]
    min = 35
    res = f"""
    <html>
        <header><title>Python</title></header>
        <body>
            <h1>Hello Python</h1>
            <p>Min {min}</p>
            <table border="1" width="100%">
                <tr><td>Loyer</td><td>Surface</td></tr>"""
    for index, value in enumerate(loyers):
        res += f"<tr><td>{value}</td><td>{surfaces[index]}</td></tr>"
    res += """</table>
        </body>
    </html>
    """
    return res

if __name__ == '__main__':
    app.run(host="0.0.0.0")