from main import fetch_weather_by_coordinates, fetch_hourly_forecast
import subprocess


def run_main():
    """
    Run functions from main.py
    """
    API_KEY = "b02dae730f1f04074ed7057c0a3eb2c3"

    print("Fetching weather data by coordinates...")
    fetch_weather_by_coordinates(20.5, 75.43, API_KEY)

    print("\nFetching hourly forecast data...")
    fetch_hourly_forecast(40.86, 56.26, API_KEY)

def run_pytest():
    """
    Run all pytest tests
    """
    print("\nRunning pytest...")
    result = subprocess.run(["python", "-m", "pytest"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)


if __name__ == "__main__":
    # Run everything
    run_main()
    run_pytest()
