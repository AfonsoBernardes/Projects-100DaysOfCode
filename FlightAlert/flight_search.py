import os
import requests
from flight_data import FlightData

KIWI_ENDPOINT = os.environ.get("KIWI_ENDPOINT")
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
KIWI_HEADERS = {"apikey": KIWI_API_KEY, }


class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API.
    """

    def get_destination_code(self, city_name):
        # Setup FlightSearch API
        kiwi_query_endpoint = f'{KIWI_ENDPOINT}/locations/query'

        query = {
            "term": city_name,
            "location_types": "city"
        }

        kiwi_response = requests.get(url=kiwi_query_endpoint, params=query, headers=KIWI_HEADERS).json()
        code = kiwi_response["locations"][0]["code"]
        return code

    def get_flight_prices(self, data_manager, fly_from_code, date_from, date_to):
        kiwi_flights_endpoint = f'{KIWI_ENDPOINT}/v2/search'

        for flight in data_manager.get_data():
            flight_params = {
                "fly_from": fly_from_code,
                "fly_to": flight["iataCode"],
                "date_from": date_from,
                "date_to": date_to,
            }

            kiwi_response = requests.get(url=kiwi_flights_endpoint, params=flight_params, headers=KIWI_HEADERS).json()
            flight_data = kiwi_response["data"][0]

            # TODO: Test try-except block.
            try:
                return_date = flight_data["route"][1]["local_departure"].split("T")[0]
            except IndexError:
                print("No return info available.")
                return_date = "Not Available"
            finally:
                flight_data = FlightData(price=flight_data["price"],
                                         origin_city=flight_data["route"][0]["cityFrom"],
                                         origin_airport=flight_data["route"][0]["flyFrom"],
                                         destination_city=flight_data["route"][0]["cityTo"],
                                         destination_airport=flight_data["route"][0]["flyTo"],
                                         depart_date=flight_data["route"][0]["local_departure"].split("T")[0],
                                         return_date=return_date,
                                         link=flight_data["deep_link"]
                                         )

            data_manager.update_sheet(flight=flight, new_flight=flight_data)
