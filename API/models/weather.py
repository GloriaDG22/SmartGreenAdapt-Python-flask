import connexion

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
#from flask_cors import CORS
#from flask_heroky import flask_heroku

app = Flask(__name__)
#CORS(app)

lat = 39.4789255,
lon = -6.3423358
API_key = '0db5d912986a7c8d9443ea0ccc7e19b8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'

#heroku = Heroku(app)
db = SQLAlchemy(app)


class Weather(db.Model):
    __tablename__ = 'weather'
    id = db.Column(db.Interger, primary_key=True)
    # state
    temp = db.Column(db.Interger)
    temp_feel = db.Column(db.Interger)
    temp_min = db.Column(db.Interger)
    temp_max = db.Column(db.Interger)
    pressure = db.Column(db.Interger)
    humidity = db.Column(db.Interger)
    wind = db.Column(db.Interger)
    date = db.Column(db.Interger)
    season = db.Column(db.Interger)

    def __init__(self, temp, temp_feel, temp_min, temp_max, pressure, humidity, wind, date, season):
        self.temp = temp
        self.temp_feel = temp_feel
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.pressure = pressure
        self.humidity = humidity
        self.wind = wind
        self.date = date
        self.season = season

