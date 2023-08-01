import pytest
import json
from app import app

# Test function to check if the application handles an unknown city correctly.
def test_get_weather_unknown_city():
    # Create a test client for the Flask application.
    client = app.test_client()

    # Send a GET request to the '/weather' endpoint with the city 'San Francisco'.
    response = client.get('/weather/San Francisco')

    # Assert that the response status code is 200 (OK).
    assert response.status_code == 200

    # Deserialize the JSON data from the response.
    data = json.loads(response.data)

    # Assert that the temperature and weather in the response match the expected values for 'San Francisco'.
    assert data['temperature'] == 14
    assert data['weather'] == 'Cloudy'

# Test function to check if the application can add new weather data for a city.
def test_add_weather():
    # Create a test client for the Flask application.
    client = app.test_client()

    # Create a new weather data object for 'Chicago'.
    new_weather = {
        "city": "Chicago",
        "temperature": 18,
        "weather": "Cloudy"
    }

    # Send a POST request to the '/weather' endpoint with the new weather data.
    response = client.post('/weather', json=new_weather)

    # Deserialize the JSON data from the response.
    data = json.loads(response.data)

    # Assert that the response status code is 201 (Created).
    assert response.status_code == 201

    # Assert that the temperature and weather in the response match the added data for 'Chicago'.
    assert data['temperature'] == 18
    assert data['weather'] == "Cloudy"

# Test function to check if the application can update weather data for a city.
def test_update_weather():
    # Create a test client for the Flask application.
    client = app.test_client()

    # Create updated weather data for 'Chicago'.
    updated_weather = {
        "temperature": 25,
        "weather": "Sunny"
    }

    # Send a PUT request to the '/weather' endpoint with the updated weather data.
    response = client.put('/weather/Chicago', json=updated_weather)

    # Assert that the response status code is 200 (OK).
    assert response.status_code == 200

    # Assert that the response JSON data matches the updated weather data for 'Chicago'.
    assert response.json == updated_weather

# Test function to check if the application can delete weather data for a city.
def test_delete_weather():
    # Create a test client for the Flask application.
    client = app.test_client()

    # Send a DELETE request to the '/weather' endpoint for 'Chicago'.
    response = client.delete('/weather/Chicago')

    # Assert that the response status code is 204 (No Content) to indicate successful deletion.
    assert response.status_code == 204
