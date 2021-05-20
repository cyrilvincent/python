import flask
import house

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return f"""
<html>
        <header><title>Python</title></header>
        <body>
            <p><a href="/ping">Ping</a><p>
            <p><a href="/house">House</a><p>
        </body>
</html>
"""

@app.route("/ping")
def ping():
    return "pong"

@app.route("/house")
def house_html():
    model = house.HouseCsv("data/house.csv", ",")
    model.load()
    min, max, avg = model.min_max_avg(model.loyers_per_m2)
    res = f"""
    <html>
        <header><title>Python</title></header>
        <body>
            <h1>House</h1>
            <p>Loyers par m²</p>
            <p>Min: {min:.0f}</p>
            <p>Max: {max:.0f}</p>
            <p>Moyenne: {avg:.1f}</p>
            <table border="1" width="100%">
                <tr><td>Loyer</td><td>Surface</td></tr>"""
    for index, value in enumerate(model.loyers):
        res += f"<tr><td>{value}</td><td>{model.surfaces[index]}</td></tr>"
    res += """</table>
        </body>
    </html>
    """
    return res

if __name__ == '__main__':
    app.run(host="0.0.0.0")