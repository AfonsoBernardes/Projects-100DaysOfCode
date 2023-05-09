import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

api_response = requests.get(f"https://opentdb.com/api.php", params=parameters)
api_response.raise_for_status()
question_data = api_response.json()["results"]
