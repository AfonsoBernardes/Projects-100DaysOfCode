import time

import requests
import smtplib
from datetime import datetime

SEND_EMAIL = ""
PASSWORD = ""
TO_EMAIL = ""

MY_LAT = 51.507351
MY_LONG = -0.127758
FORMAT = 0  # 0 for 24H format; 1 for 12h format


def iss_above_me():
    # ISS Position API
    response_iss = requests.get("http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()
    iss_lat = float(data_iss["iss_position"]["latitude"])
    iss_long = float(data_iss["iss_position"]["longitude"])

    if (iss_lat - 5 <= MY_LAT <= iss_lat + 5) and (iss_long - 5 <= MY_LONG <= iss_long + 5):
        return True
    return False


def is_night():
    # Sunrise/Sunset API Request and data treatment.
    api_parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": FORMAT,
    }

    response_time = requests.get("https://api.sunrise-sunset.org/json", params=api_parameters)
    response_time.raise_for_status()
    data_time = response_time.json()

    sunrise_hour = int(data_time["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data_time["results"]["sunset"].split("T")[1].split(":")[0])
    hour_now = datetime.now().hour

    if hour_now <= sunrise_hour or hour_now >= sunset_hour:
        return True
    return False


while True:
    time.sleep(60)
    if is_night() and iss_above_me():
        # Email Setup
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Transport Layer Security - Secures connection to email server.
            connection.login(user=SEND_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=SEND_EMAIL,
                                to_addrs=TO_EMAIL,
                                msg=f"Subject: Look up!.\n\n"
                                    f"The ISS is above you in the sky."
                                )
