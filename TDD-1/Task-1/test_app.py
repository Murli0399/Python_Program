import pytest
from app import app

def test_get_weather_unknown_city():
    client = app.test_client()

    response = client.get('/weather/SanFrancisco')

    assert response.status_code == 200
    assert response.data == b'The weather for SanFrancisco is unknown.'
