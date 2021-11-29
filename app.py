from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("example.html")

@app.route("/html")
def htmol():
    return render_template("ex 2.html")
