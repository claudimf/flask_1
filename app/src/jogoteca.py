from flask import Flask


app = Flask(__name__)


@app.route('/inicio')
def ola():
    return '<h1>Olá Flask!</h1>'


@app.route("/")
def raiz():
    return "Homepage "


if __name__ == "__main__":
    app.run(host='0.0.0.0')
