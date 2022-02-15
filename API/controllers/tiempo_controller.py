import connexion

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from ..models.weather import Weather

app = Flask(__name__)
db = SQLAlchemy(app)


def calculate_season(date):
    month = date.getMonth() + 1

    if month > 2 & month < 6:
        return 'Spring'
    elif month > 5 & month < 9:
        return 'Summer'
    elif month > 8 & month < 12:
        return 'Autumn'
    elif month < 3 | month > 11:
        return 'Winter'


def calculate_celsius(tempk):
    return round(tempk - 273.15, 2)


@app.route('/service/weather/post', methods=['POST'])
def post_weather(self):
    if request.content_type == 'application/json':
        data = request.get_json()
        temp = self.calculate_celsius(data.get('temp'))
        temp_feel = self.calculate_celsius(data.get('temp_feel'))
        temp_min = self.calculate_celsius(data.get('temp_min'))
        temp_max = self.calculate_celsius(data.get('temp_max'))
        pressure = data.get('pressure')
        humidity = data.get('humidity')
        wind = data.get('speed')
        date = data.get('date')
        season = self.calculate_season(data.get('season'))

        weather = Weather(temp, temp_feel, temp_min, temp_max, pressure, humidity, wind, date, season)
        db.session.add(weather)
        db.sesion.commit()

        return jsonify('Data Posted')
