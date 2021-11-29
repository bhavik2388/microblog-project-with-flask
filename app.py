from flask import Flask, render_template
app = Flask(__name__)

class GalileanMoons:
    def __init__ (self,first,second,third,fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/cond") 
def hello_world():
    user_os = {
        "bhavik":"Windows",
        "anuj":"MacOS",
        "aman":"Linux"
    }

    return render_template("loops_and_conditionals.html",user_os=user_os)