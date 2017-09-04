from flask import Flask, render_template, jsonify, request, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/weather_info', methods=['POST'])
def weather_info():
    city = request.form["weather"]
    city = requests.get('http://weathers.co/api.php?city={}'.format(city))
    weather = city.json()
    # Get data
    _location = weather.get('data').get('location', 'Error')
    _temp = weather.get('data').get('temperature', 'Error')
    _skytext = weather.get('data').get('skytext', 'Error')
    _wind = weather.get('data').get('wind', 'Error')
    if _temp == 'Error':
        return redirect(url_for('error'))
    return render_template('weather.html',
    location=_location, temp=_temp, skytext=_skytext, wind=_wind)

@app.route('/')
def weather_search():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
