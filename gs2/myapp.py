import requests

URL = "http://localhost:8000/student/"

data = {
    "name": "John Doe",
    "roll": 105,
    "city": "New York"
}

# Send a POST request with JSON data
r = requests.post(url=URL, json=data)

# Attempt to parse the response as JSON
try:
    response_data = r.json()
    print(response_data)
except requests.exceptions.JSONDecodeError:
    print("Failed to parse response as JSON.")
    print("Response text:", r.text)
