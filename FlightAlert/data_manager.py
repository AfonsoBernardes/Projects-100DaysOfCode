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
        self.sheety_flight_list.raise_for_status()
        return self.sheety_flight_list

    def populate_iaca(self, flight_search):
        """
        Get IATA codes and update Google Sheet
        :param flight_search:
        :return:
        """

        flight_list = self.get_data()
        for flight in flight_list:
            destination = flight["city"]
            flight_id = flight["id"]

            iata_code = flight_search.get_destination_code(city_name=destination)  # Get IATA code for each destination.

            put_config = {
                "flight": {"iataCode": iata_code, }
            }

            put_response = requests.put(url=f"{self.sheety_endpoint}/{flight_id}",
                                        json=put_config,
                                        headers=self.sheety_headers)

        self.get_data()

    def update_sheet(self, flight, new_flight):
        """
        Get flight prices and if lower, update Google Sheet with relevant infomation.
        :param flight:
        :param new_flight:
        :return:
        """

        if flight["lowestPrice"] is None or float(flight["lowestPrice"]) > float(new_flight.price):
            flight_id = flight["id"]
            put_config = {
                "flight": {"lowestPrice": new_flight.price,
                           "flyFrom": f"{new_flight.origin_city}({new_flight.origin_airport})",
                           "departureDate": new_flight.depart_date,
                           "returnDate": new_flight.return_date,
                           "link": new_flight.link,
                           }
            }

            # Update new flight data to Google Sheets.
            put_response = requests.put(url=f"{self.sheety_endpoint}/{flight_id}",
                                        json=put_config,
                                        headers=self.sheety_headers)
