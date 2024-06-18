import requests
from twilio.rest import Client
import os

account_sid = os.environ.get('ONW_ACCT_SID')
auth_token = os.environ.get('ONW_AUTH_TOKEN')
client = Client(account_sid, auth_token)

open_weather_api_key = os.environ.get('ONW_API_KEY')
owm_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'

your_mobile_number = '+1XXXXXXXXXX'
weather_params = {
    'lat': 45.5088,
    'lon': -73.5878,
    'appid': open_weather_api_key,
    'cnt': 4  # count only 4 timestamps
}

response = requests.get(owm_endpoint, params=weather_params)
response.raise_for_status()
data = response.json()

will_rain = False
for timestamp in data['list']:
    weather_id = timestamp['weather'][0]['id']
    if weather_id < 700:
        will_rain = True
if will_rain:
    message = client.messages.create(
        from_='+16508259151',
        to=your_mobile_number,
        body='Bring an umbrella ☔️'
    )