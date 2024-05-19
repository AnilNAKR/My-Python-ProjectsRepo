import requests as rq
from datetime import datetime
import smtplib
import time
import os

email = os.environ.get('MYMAILID')
password = os.environ.get('MAILKEY')

my_lat = 11.4102
my_lon = 76.6950


def is_iss_overhead():
    response = rq.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if my_lat - 5 <= iss_latitude <= my_lat + 5 and my_lon - 5 <= iss_longitude <= my_lon + 5:
        return True


def is_night():
    parameters = {
        "lat": my_lat,
        "lng": my_lon,
        "formatted": 0,
    }
    response = rq.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['result']['sunrise'].split('T')[1].split[':'][0])
    sunset = int(data['result']['sunset'].split('T')[1].split[':'][0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(from_addr=email, to_addrs=os.environ.get('MYMAILID2'), msg="Subject: Look Up :) !\n\n"
                                                                                 "ISS Satellite Space "
                                                                                 "Station is passing above you.")
