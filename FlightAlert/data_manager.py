import os
import requests


class DataManager:
    """
    This class is responsible for talking to the Google Sheet.
    """
    def __init__(self):
        # Sheety Setup
        self.sheety_flight_list = None
        self.sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")
        self.sheety_headers = {
            "Authorization": os.environ.get("AUTHORIZATION")
        }

    def get_data(self):
        """
        Returns list of flights from GoogleSheets.
        :return:
        """
        self.sheety_flight_list = requests.get(url=self.sheety_endpoint, headers=self.sheety_headers).json()["flights"]
        return self.sheety_flight_list

    def populate_iaca(self, flight_id, iata_code):

        put_config = {
            "flight": {"iataCode": iata_code, }
        }

        put_response = requests.put(url=f"{self.sheety_endpoint}/{flight_id}",
                                    json=put_config,
                                    headers=self.sheety_headers)
        print(put_response.text)
