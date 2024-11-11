from flask import Flask
app = Flask(__name__)

@app.route('/WeatherForecast')
def getWeatherOnline():
    return 'Today is gonna be a great snowy day for a Python service!'