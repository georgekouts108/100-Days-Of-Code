# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
import os
from datetime import *

SHEETY_ENDPOINT = os.environ['SHEETY_ENDPOINT']
SHEETY_AUTH_UNAME = os.environ['SHEETY_AUTH_UNAME']
SHEETY_AUTH_PWD = os.environ['SHEETY_AUTH_PWD']

data_manager = DataManager(sheety_endpoint=SHEETY_ENDPOINT, sheety_auth=(SHEETY_AUTH_UNAME, SHEETY_AUTH_PWD))
flight_search = FlightSearch()
notifier = NotificationManager()
sheet_data = data_manager.get_all_data()

for entry in sheet_data:
    if entry['iataCode'] == '':
        entry['iataCode'] = flight_search.get_iata_code(city=entry['city'])
        data_manager.add_iata_code(row_id=entry['id'], iata=entry['iataCode'])

pprint(sheet_data)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for entry in sheet_data:
    flights = flight_search.get_flights(
        origin_iata='LON',
        destination_iata=entry['iataCode'],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{entry['city']}: £{cheapest_flight.price}")
    try:
        if float(cheapest_flight.price) < float(entry['lowestPrice']):
            notifier.send_text_message(mobile_num=os.environ['MY_PHONE_NUM'], message=f"There's a cheaper flight from LON to {entry['city']}")
    except Exception:
        print("Something went wrong...")


