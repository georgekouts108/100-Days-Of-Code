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
today = datetime.now()
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '4.5'
}
headers = {
    'X-USER-TOKEN': TOKEN
}

response_put = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response_put.text)
response_del = requests.delete(url=delete_endpoint, headers=headers)
print(response_del.text)