from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()

flight_list = data_manager.get_data()
for flight in flight_list:
    destination = flight["city"]
    flight_id = flight["id"]

    iata_code = flight_search.get_destination_code(city_name=destination)  # Get IATA code for each destination.
    data_manager.populate_iaca(flight_id, iata_code)  # Populate google sheets with IATA codes.
