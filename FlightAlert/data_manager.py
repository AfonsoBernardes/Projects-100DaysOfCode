import os
import requests


class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """
    def __init__(self):
        # Sheety Setup
        self.sheety_response = None
        self.sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
        self.sheety_headers = {
            "Authorization": os.environ.get("AUTHORIZATION")
        }

    def get_data(self):
        """
        Returns list of flights from GoogleSheets.
        :return:
        """
        self.sheety_response = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers).json()["flights"]
        return self.sheety_response
