import requests
from datetime import datetime
import os

date_data = datetime.now()
today_date = date_data.strftime("%d/%m/%Y")
present_time = date_data.strftime("%X")

APP_ID = os.environ.get('APP_ID')
APP_KEY = os.environ.get('APP_KEY')

parameters = {
    "query": input("Enter your workout info: "),
    "weight_kg": 66,
    "height_cm": 171,
    "age": 27,
}

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
}

response = requests.post(url=nutrition_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

# Accessing and adding/Posting data to Google Sheets using Sheety REST API---------------------------------------

sheety_username = "anilnakr7"
sheety_auth = os.environ.get('SHEETY_AUTH')

sheety_endpoint = "https://api.sheety.co/b6c3d1ccfb8159ba8a9aa21cc4446c85/myWorkoutsTracker/workouts"

sheets_data_input = {
    'workout': {
        "date": today_date,
        "time": present_time,
        "exercise": result['exercises'][0]['name'].title(),
        "duration": result['exercises'][0]['duration_min'],
        "calories": result['exercises'][0]['nf_calories']
    }
}

sheet_response = requests.post(url=sheety_endpoint, json=sheets_data_input, auth=(sheety_username, sheety_auth))
print(sheet_response.text)
