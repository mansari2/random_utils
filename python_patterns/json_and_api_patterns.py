import json
import requests

"""
This script provides common patterns for dealing with JSON data, making HTTP requests, and hitting API endpoints.

Key Topics Covered:
- Parsing JSON data
- Writing JSON to files
- Making GET and POST requests with requests
- Handling API responses and errors
"""

# 1. Working with JSON Data

def load_json_from_file(file_path):
    """Loads JSON data from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def write_json_to_file(file_path, data):
    """Writes JSON data to a file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print(f"JSON data written to {file_path}")

def parse_json_string(json_string):
    """Parses a JSON string into a Python dictionary."""
    return json.loads(json_string)

# 2. Making HTTP Requests

def make_get_request(url, params=None):
    """Makes a GET request to the given URL with optional query parameters."""
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error making GET request: {e}")
        return None

def make_post_request(url, data, headers=None):
    """Makes a POST request to the given URL with JSON data."""
    try:
        headers = headers or {'Content-Type': 'application/json'}
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error making POST request: {e}")
        return None

# 3. Example Usage (Uncomment to run)
# sample_json = '{"name": "Alice", "age": 30}'
# parsed_data = parse_json_string(sample_json)
# print(parsed_data)

# write_json_to_file("data.json", {"status": "success", "message": "Hello"})
# loaded_data = load_json_from_file("data.json")
# print(loaded_data)

# api_response = make_get_request("https://jsonplaceholder.typicode.com/posts/1")
# print(api_response)

# post_response = make_post_request("https://jsonplaceholder.typicode.com/posts", {"title": "Test", "body": "Content", "userId": 1})
# print(post_response)

