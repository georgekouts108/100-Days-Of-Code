import requests
import os

pixela_endpoint = 'https://pixe.la/v1/users'
user_params = {
    'token': os.environ.get('TOKEN'),
    'username': 'georgekouts',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
