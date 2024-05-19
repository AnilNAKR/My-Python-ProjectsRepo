import requests
from datetime import datetime
import os

# -------------------------------------------------------------------------------
# Step 1 - Creating User Account on Pixela

pixela_endpoint = "https://pixe.la/v1/users"

# Username & Token are created by user itself

USERNAME = os.environ.get("PIXELA_USER_NAME")
TOKEN = os.environ.get("PIXELA_TOKEN")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Comment the below 2 line after creating the account in pixela

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# -----------------------------------------------------------------------------

# Step 2 - Creating a new pixela graph with Graph name, id, unit of measurement, & theme

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Defines the display color of the pixel in the pixelation graph.
# shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black)

graph_config = {
    "id": "mygraph",
    "name": "Daily Running Practice Tracker",
    "unit": "Minutes",
    "type": "int",
    "color": "sora",
}
headers = {
    "X-User-Token": TOKEN
}
# Comment the below 2 graph after graph is created

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# ----------------------------------------------------------------------------------
# Step 3 - Posting value to the graph

pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()

# date format eg.20240524 - (yearmonthday)
print(f"Today's Date: {today.strftime("%Y%m%d")}")
# formatdate = today.strftime("%Y%m%d")
formatdate = "20240510"
pixel_data = {
    'date': formatdate,
    'quantity': '15',
}

# Comment the below 2 line while using update or delete methods

response = requests.post(url=pixel_creation, json=pixel_data, headers=headers)
print(response.text)

# ----------------------------------------------------------------------------------------------------

# Step 4 - Updating value in the graph

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"
# update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/20200519"

new_pixel_data = {
    'quantity': "10"
}

# Comment the below 2 line while using post or delete methods

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# --------------------------------------------------------------------------------------------------------

# Step 5 - Delete a Pixel in a graph by passing in the data in eg.20240520 format

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/20240519"

# Comment the below 2 line while using post or update methods

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)

# ------------------------------------------------------------------------------------------------
# Step 6 - Delete a graph

delete_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

response = requests.delete(url=delete_graph_endpoint, headers=headers)
print(response.text)

# ----------------------------------------------------------------------------------------------
# Step 7 - Post multiple pixels at once

multiple_post_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/pixels"

pixel_data1 = [{'date': 20240504, 'quantity': '45'}, {'date': 20240505, 'quantity': '15'}, {'date': 20240506, 'quantity': '25'},
              {'date': 20240507, 'quantity': '45'}, {'date': 20240508, 'quantity': '40'}, {'date': 20240509, 'quantity': '45'},
              {'date': 20240510, 'quantity': '60'}, {'date': 20240511, 'quantity': '30'}, {'date': 20240512, 'quantity': '45'},
              {'date': 20240513, 'quantity': '80'}, {'date': 20240514, 'quantity': '50'}, {'date': 20240515, 'quantity': '45'},
              {'date': 20240516, 'quantity': '45'}, {'date': 20240517, 'quantity': '75'}, {'date': 20240518, 'quantity': '65'}]
response = requests.post(url=multiple_post_graph_endpoint, json=pixel_data1, headers=headers)
print(response.text)



