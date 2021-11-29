from flask import Flask, render_template
app = Flask(__name__)

class GalileanMoons:
    def __init__ (self,first,second,third,fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/datast") 
def hello_world():
    movies = [
        "Avenger",
        "Spiderman",
        "Ironman"
    ]
    car = {
        "brand":"tesla",
        "model":"roadster",
        "year": "2020"
    }

    moons = GalileanMoons("Io","Europa","Ganymede","Callisto")

    return render_template("data_structures.html",movies=movies,car=car,moons=moons)