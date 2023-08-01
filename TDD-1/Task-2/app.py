from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Sample weather data dictionary with city names as keys and weather information as values.
weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

# Endpoint to get weather data for a specific city by sending a GET request with the city name.
@app.route('/weather/<string:city>')
def get_weather(city):
    # Check if the weather data for the specified city exists in the weather_data dictionary.
    # If found, return the weather data as JSON with a 200 status code. Otherwise, return a 404 status code.
    weather = weather_data.get(city)
    if weather:
        return jsonify(weather), 200
    else:
        return jsonify({"message": f"Weather data not found for {city}"}), 404

# Endpoint to add new weather data for a city by sending a POST request with JSON data.
@app.route('/weather', methods=['POST'])
def add_weather():
    # Extract JSON data from the request and retrieve the city name.
    new_weather = request.get_json()
    city = new_weather.get('city')

    # Check if the city is provided and does not already exist in the weather_data dictionary.
    # If valid, add the new weather data to the dictionary and return the added data as JSON with a 201 status code.
    # Otherwise, abort the request with a 400 status code and an error message.
    if city and city not in weather_data:
        weather_data[city] = {
            'temperature': new_weather.get('temperature'),
            'weather': new_weather.get('weather')
        }
        return jsonify(weather_data[city]), 201
    else:
        abort(400, 'Invalid request')

# Endpoint to update weather data for a city by sending a PUT request with JSON data and the city name in the URL.
@app.route('/weather/<string:city>', methods=['PUT'])
def update_weather(city):
    # Check if the city exists in the weather_data dictionary.
    # If found, update the weather data with the provided JSON data and return the updated data as JSON.
    # Otherwise, abort the request with a 404 status code and an error message.
    if city in weather_data:
        updated_weather = request.get_json()
        weather_data[city].update(updated_weather)
        return jsonify(weather_data[city])
    else:
        abort(404, f"Weather data not found for {city}")

# Endpoint to delete weather data for a city by sending a DELETE request with the city name in the URL.
@app.route('/weather/<string:city>', methods=['DELETE'])
def delete_weather(city):
    # Check if the city exists in the weather_data dictionary.
    # If found, delete the weather data for that city and return a 204 status code (no content).
    # Otherwise, abort the request with a 404 status code and an error message.
    if city in weather_data:
        del weather_data[city]
        return '', 204
    else:
        abort(404, f"Weather data not found for {city}")

# This block runs the Flask application when the script is executed.
if __name__ == "__main__":
    app.run()
