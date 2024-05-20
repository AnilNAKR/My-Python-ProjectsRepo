import requests
from datetime import datetime

my_lat = 11.4102
my_lon = 76.6950

parameters = {
    "lat": my_lat,
    "lng": my_lon,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(sunrise.split('T'), sunset.split('T'))

time_now = datetime.now()
print(time_now)