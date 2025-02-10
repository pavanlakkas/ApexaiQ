import pytest
from main import fetch_weather_by_coordinates, fetch_hourly_forecast

# API key
API_KEY = "b02dae730f1f04074ed7057c0a3eb2c3"


# Test 1: Ensure weather API call returns data for coordinates
@pytest.mark.parametrize("lat, lon", [
    (20.5, 75.43),  # Example coordinates
])
def test_weather_by_coordinates(lat, lon):
    data = fetch_weather_by_coordinates(lat, lon, API_KEY)
    assert data is not None, "API response for coordinates should not be None"
    assert "main" in data, "'main' key should be in the API response"


# Test 2: Ensure hourly forecast call returns data
@pytest.mark.parametrize("lat, lon", [
    (40.86, 56.26),  # Example coordinates
])
def test_hourly_forecast(lat, lon):
    data = fetch_hourly_forecast(lat, lon, API_KEY)
    assert data is not None, "API response for hourly forecast should not be None"
    assert "list" in data, "'list' key should be in the hourly forecast response"
