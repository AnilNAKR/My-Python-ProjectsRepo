import os

import requests
from datetime import datetime
import os

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.environ.get("PIXELA_USER_NAME")
TOKEN = os.environ.get("PIXELA_TOKEN")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "mygraph3",
    "name": "Habit Tracker",
    "unit": "Minutes",
    "type": "int",
    "color": "momiji",
}

headers = {
    "X-User-Token": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

pixel_data = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '30',
}

# Post end point
response = requests.post(url=pixel_creation, json=pixel_data, headers=headers)
print(response.text)

# ----------------------------------------------------------------------------------------------------

# # Update End Point
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"
#
# new_pixel_data = {
#     'quantity': "10"
# }
#
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# --------------------------------------------------------------------------------------------------------

# #  Delete a Pixel
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
