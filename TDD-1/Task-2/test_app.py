import pytest
import json
from app import app

def test_get_weather_unknown_city():
    client = app.test_client()

    response = client.get('/weather/San Francisco')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['temperature'] == 14
    assert data['weather'] == 'Cloudy'

def test_add_weather():
    client = app.test_client()
    new_weather = {
        "city": "Chicago",
        "temperature": 18,
        "weather": "Cloudy"
    }

    response = client.post('/weather', json=new_weather)
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data['temperature'] == 18
    assert data['weather'] == "Cloudy"


def test_update_weather():
    client = app.test_client()
    updated_weather = {
        "temperature": 25,
        "weather": "Sunny"
    }

    response = client.put('/weather/Chicago', json=updated_weather)

    assert response.status_code == 200
    assert response.json == updated_weather


def test_delete_weather():
    client = app.test_client()

    response = client.delete('/weather/Chicago')

    assert response.status_code == 204
