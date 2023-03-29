import requests
from datetime import datetime
import time
from notify import iss_notification

MY_LAT = float(27.700769),  # Your latitude
MY_LONG = float(85.300140)  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    # parameter for sunrise and sunset API
    parameters = {
        "lat": MY_LAT,  # mandatory parameter
        "lng": MY_LONG,  # mandatory parameter
        "formatted": 0,  # optional parameter
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    if hour_now <= sunrise or hour_now >= sunset:
        return True


while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        iss_notification("Hey,\nIss is above you.Please go out and look up☝️ in the sky.")
