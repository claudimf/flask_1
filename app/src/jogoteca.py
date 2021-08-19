from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def raiz():
    return "Homepage"


@app.route('/inicio')
def ola():
    return render_template('lista.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
