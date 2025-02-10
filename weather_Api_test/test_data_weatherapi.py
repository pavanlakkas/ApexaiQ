import pytest
import json


@pytest.fixture
def load_weather_by_coordinates():
    with open("weather_by_coordinates.json", "r") as file:
        data = json.load(file)
    return data


@pytest.fixture
def load_hourly_forecast():
    with open("hourly_forecast.json", "r") as file:
        data = json.load(file)
    return data


# Test 1: Validate weather data loaded from coordinates JSON file
def test_weather_data_json(load_weather_by_coordinates):
    data = load_weather_by_coordinates

    assert data is not None, "Weather data JSON should not be None"
    assert "coord" in data, "'coord' key should be present in the JSON"
    assert "main" in data, "'main' key should be present in the JSON"
    assert isinstance(data["main"], dict), "'main' key value should be a dictionary"


# Test 2: Validate hourly forecast data loaded from JSON file
def test_hourly_forecast_json(load_hourly_forecast):
    data = load_hourly_forecast

    assert data is not None, "Hourly forecast JSON should not be None"
    assert "list" in data, "'list' key should be present in the JSON"
    assert isinstance(data["list"], list), "'list' key value should be a list"
