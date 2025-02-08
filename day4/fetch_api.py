import requests
import json

# URL of the Public API
api_url = "https://jsonplaceholder.typicode.com/posts"

# Step 1: Make an API request
response = requests.get(api_url)

# Step 2: Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print("API call successful!")

    # Step 3: Save the data to a JSON file
    with open("response.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("Response saved to response.json!")
else:
    print(f"API call failed with status code {response.status_code}")
