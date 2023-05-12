from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch


data_manager = DataManager()
flight_search = FlightSearch()

data_manager.populate_iaca(flight_search)  # Populate Google sheets with IATA codes.

date_from = datetime.now().date().strftime("%d/%m/%Y")
date_to = (datetime.now().date() + timedelta(days=180)).strftime("%d/%m/%Y")


flight_search.get_flight_prices(data_manager, fly_from_code="PT", date_from=date_from, date_to=date_to)

