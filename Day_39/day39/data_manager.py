import requests
from pprint import pprint


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, sheety_endpoint, sheety_auth):
        self.sheety_auth = sheety_auth
        self.sheety_endpoint = sheety_endpoint

    def get_all_data(self):
        return requests.get(url=self.sheety_endpoint, auth=self.sheety_auth).json()['sheet1']

    def add_iata_code(self, row_id, iata):

        updated_entry = {
            'sheet1': {
                'iataCode': iata
            }
        }

        requests.put(url=self.sheety_endpoint + f'/{row_id}', json=updated_entry, auth=self.sheety_auth)