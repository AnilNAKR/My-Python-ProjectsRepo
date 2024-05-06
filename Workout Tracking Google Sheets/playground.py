#  Basic Authentication
import requests
import os

sheety_username = "anilnakr7"
sheety_auth = os.environ.get('SHEETY_AUTH')

sheety_endpoint = "https://api.sheety.co/b6c3d1ccfb8159ba8a9aa21cc4446c85/myWorkoutsTracker/workouts"

sheet_response = requests.get(url=sheety_endpoint, auth=(sheety_username, sheety_auth))
print(sheet_response.text)

#Bearer Token Authentication
# bearer_headers = {
# "Authorization": "Bearer YOUR_TOKEN"
# }
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     headers=bearer_headers
# )
