import os
import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self._api_key = os.environ['AMADEUS_API_KEY']
        self._api_secret = os.environ['AMADEUS_API_SECRET']
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        TOKEN_ENDPOINT = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)

        return response.json()['access_token']

    def get_flights(self, origin_iata, destination_iata, from_time, to_time):
        FLIGHT_OFFERS_ENDPOINT = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            'originLocationCode': origin_iata,
            'destinationLocationCode': destination_iata,
            'adults': '1',
            'nonStop': 'true',
            'currencyCode': 'GBP',
            'max':'10',
            'departureDate': from_time.strftime('%Y-%m-%d'),
            'returnDate': to_time.strftime('%Y-%m-%d')
        }
        response = requests.get(url=FLIGHT_OFFERS_ENDPOINT, headers=headers, params=query)

        if response.status_code != 200:
            return None

        return response.json()

    def get_iata_code(self, city):
        CITY_SEARCH_ENDPOINT = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=CITY_SEARCH_ENDPOINT,
            headers=headers,
            params=query
        )

        return response.json()['data'][0]['iataCode']
