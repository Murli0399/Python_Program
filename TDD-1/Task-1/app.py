from flask import Flask

app = Flask(__name__)

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@app.route('/weather/<string:city>')
def get_weather(city):
    if city in weather_data:
        weather = weather_data[city]
        return f"The weather for {city} is {weather['weather']} with a temperature of {weather['temperature']}°C."
    else:
        return f"The weather for {city} is unknown."

if __name__ == "__main__":
    app.run()