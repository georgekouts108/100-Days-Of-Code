import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def __init__(self, sheety_endpoint, sheety_auth):
        self.sheety_auth = sheety_auth
        self.sheety_endpoint = sheety_endpoint

    def get_customer_emails(self):
        response = requests.get(url=f'{self.sheety_endpoint}/users', auth=self.sheety_auth)
        data = response.json()
        customer_data = data['users']
        return customer_data

    def get_all_data(self):
        return requests.get(url=f'{self.sheety_endpoint}/prices', auth=self.sheety_auth).json()['prices']

    def add_iata_code(self, row_id, iata):

        updated_entry = {
            'price': {
                'iataCode': iata
            }
        }

        requests.put(url=f'{self.sheety_endpoint}/prices/{row_id}', json=updated_entry, auth=self.sheety_auth)