import requests
from twilio.rest import Client
import os

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_TOKEN')

api_key = os.environ.get('WEATHER_API_KEY')
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

# cordinates are for Kolkata city that has rainfall at the current time
parameters = {
    "lat": 22.5744,
    "lon": 88.3629,
    "cnt": 4,
    "appid": api_key,
}

response = requests.get(OWM_endpoint, params=parameters)
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()

# weather_code = weather_data['list'][0]['weather'][0]['id']
will_rain = False
for i in range(len(weather_data['list'])):
    condition_code = weather_data['list'][i]['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today! So, Carry an Umbrella ☂️",
        from_=os.environ.get('MOBILE_FROM'),
        to=os.environ.get('MOBILE_TO')
    )
    print(message.status)
