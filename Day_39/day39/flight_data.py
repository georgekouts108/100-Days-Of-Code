class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, origin, destination, departure_date, return_date):
        self.price = price
        self.origin = origin
        self.destination = destination
        self.departure_date = departure_date
        self.return_date = return_date


def find_cheapest_flight(data):
    if data is None or not data['data']:
        print("No flights.")
        return FlightData('N/A', 'N/A', 'N/A', 'N/A', 'N/A')

    first_flight = data['data'][0]
    cheapest_price = float(first_flight['price']['grandTotal'])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(cheapest_price, origin, destination, departure_date, return_date)

    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < cheapest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            departure_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, departure_date, return_date)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight
