import os
import json


# Test function to check if the response.json file exists
def test_file_created():
    assert os.path.exists("response.json"), "The JSON file was not created."


# Test function to check if the JSON file contains valid JSON
def test_valid_json():
    with open("response.json", "r") as json_file:
        try:
            data = json.load(json_file)  # This will raise an error if it's not valid JSON
        except json.JSONDecodeError:
            assert False, "The JSON file contains invalid JSON."


# Test function to check if specific key or value exists in the JSON file
def test_required_data():
    with open("response.json", "r") as json_file:
        data = json.load(json_file)
        assert len(data) > 0, "The JSON data is empty!"
        first_item = data[0]
        assert "title" in first_item, "The 'title' key is missing in the response data."
