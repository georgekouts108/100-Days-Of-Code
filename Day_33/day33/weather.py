import requests

county_cork = {
    'lat': 51.897869,
    'lng': -8.471090
}
budakeszi = {
    'lat': 47.4806101,
    'lng': 18.8340464,
    'formatted':0
}
response_cork = requests.get("https://api.sunrise-sunset.org/json", params=county_cork)
response_cork.raise_for_status()
data_cork = response_cork.json()
print(data_cork)

response_buda = requests.get("https://api.sunrise-sunset.org/json", params=budakeszi)
response_buda.raise_for_status()
data_buda = response_buda.json()
print(data_buda)