import requests
from datetime import datetime
import os

USERNAME = 'georgekouts'
TOKEN = os.environ.get('TOKEN')

pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime.now()
pixel_config = {
    'date': today.strftime('%Y') + today.strftime('%m') + today.strftime('%d'),
    'quantity': '9.74'
}
# graph_config = {
#     'id': 'graph1',
#     'name': 'Cycling Graph',
#     'unit': 'Km',
#     'type': 'float',
#     'color': 'ajisai'
# }
headers = {
    'X-USER-TOKEN': TOKEN
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)