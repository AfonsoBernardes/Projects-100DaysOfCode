import os
import requests


class FlightSearch:
    """
    This class is responsible for talking to the Flight Search API.
    """

    def get_destination_code(self, city_name):
        # Setup FlightSearch API
        kiwi_endpoint = os.environ.get("KIWI_ENDPOINT")
        kiwi_api_key = os.environ.get("KIWI_API_KEY")
        kiwi_query_endpoint = f'{kiwi_endpoint}/locations/query'

        kiwi_headers = {"apikey": kiwi_api_key,}

        query = {
            "term": city_name,
            "location_types": "city"
        }

        kiwi_response = requests.get(url=kiwi_query_endpoint, params=query, headers=kiwi_headers).json()
        code = kiwi_response["locations"][0]["code"]
        return code



