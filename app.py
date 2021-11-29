from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/html")
def htmol():
    return """
    <h1> HELLOOOOOO PEPCODERSS...... </h1>
    """
