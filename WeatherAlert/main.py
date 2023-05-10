import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

# Twilio Setup
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
PHONE_NUM_FROM = os.environ.get("PHONE_NUM_FROM")
PHONE_NUM_TO = os.environ.get("PHONE_NUM_TO")


# Work on PythonAnywhere

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
API_KEY = os.environ.get("API_KEY")
MY_LAT = 40.203316
MY_LON = -8.410257

request_parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}
# Retrieve API data.
api_response = requests.get(OWM_Endpoint, params=request_parameters)
api_response.raise_for_status()
weather_data = api_response.json()

# Get a hold of next twelve hours weather codes
weather_slice = weather_data["hourly"][:12]
# Loop next twelve hours and gather codes in list
twelve_hour_codes = [weather["weather"][0]["id"] for weather in weather_slice]
will_rain = any(code < 700 for code in twelve_hour_codes)  # True if any code is less than 700, implying it will rain.

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today, bring an umbrella.",
        from_=PHONE_NUM_FROM,
        to=PHONE_NUM_TO
    )

print(message.status)
