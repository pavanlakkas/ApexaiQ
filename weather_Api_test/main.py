import requests
import json


def fetch_weather_by_coordinates(lat, lon, api_key):
    """
    Fetch weather data by latitude and longitude.
    """
    api_url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {"lat": lat, "lon": lon, "appid": api_key}

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        data = response.json()

        # Save output to a JSON file
        with open("weather_by_coordinates.json", "w") as file:
            json.dump(data, file, indent=4)

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data by coordinates: {e}")
        return None


def fetch_hourly_forecast(lat, lon, api_key):
    """
    Fetch hourly forecast data by latitude and longitude.
    """
    api_url = f"https://api.openweathermap.org/data/2.5/forecast?"
    params = {"lat": lat, "lon": lon, "appid": api_key}

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        data = response.json()

        # Save output to a JSON file
        with open("hourly_forecast.json", "w") as file:
            json.dump(data, file, indent=4)

        return data

    except requests.exceptions.RequestException as e:
        print(f"Error fetching hourly forecast data: {e}")
        return None


if __name__ == "__main__":
    # API key
    API_KEY = "b02dae730f1f04074ed7057c0a3eb2c3"

    # Example calls
    print("Fetching weather data by coordinates...")
    fetch_weather_by_coordinates(20.5, 75.43, API_KEY)

    print("\nFetching hourly forecast data...")
    fetch_hourly_forecast(40.86, 56.26, API_KEY)
