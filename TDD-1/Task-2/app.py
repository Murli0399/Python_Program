from flask import Flask, jsonify, request, abort

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
    weather = weather_data.get(city)
    if weather:
        return jsonify(weather), 200
    else:
        return jsonify({"message": f"Weather data not found for {city}"}), 404


@app.route('/weather', methods=['POST'])
def add_weather():
    new_weather = request.get_json()
    city = new_weather.get('city')

    if city and city not in weather_data:
        weather_data[city] = {
            'temperature': new_weather.get('temperature'),
            'weather': new_weather.get('weather')
        }
        return jsonify(weather_data[city]), 201
    else:
        abort(400, 'Invalid request')


@app.route('/weather/<string:city>', methods=['PUT'])
def update_weather(city):
    if city in weather_data:
        updated_weather = request.get_json()
        weather_data[city].update(updated_weather)
        return jsonify(weather_data[city])
    else:
        abort(404, f"Weather data not found for {city}")


@app.route('/weather/<string:city>', methods=['DELETE'])
def delete_weather(city):
    if city in weather_data:
        del weather_data[city]
        return '', 204
    else:
        abort(404, f"Weather data not found for {city}")


if __name__ == "__main__":
    app.run()