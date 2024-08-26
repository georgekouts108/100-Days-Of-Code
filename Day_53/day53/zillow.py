from bs4 import BeautifulSoup
import requests


class ZillowScraper:
    def __init__(self):
        pass

    def strip_price(self, price):
        price_raw = price.split(' ')[0]
        stop_at = -1
        while price_raw[stop_at] not in [str(i) for i in range(10)]:
            stop_at -= 1

        return price_raw[:stop_at + 1]

    def get_listings(self):
        ZILLOW = 'https://appbrewery.github.io/Zillow-Clone/'
        response_zillow = requests.get(ZILLOW)

        soup_zillow = BeautifulSoup(response_zillow.content, 'html.parser')
        listings = soup_zillow.find_all(id="zpid_2056905294")

        properties = []
        for prop in listings:
            prop_str = str(prop)

            monthly_price_index1 = prop_str.index('$')
            monthly_price_index2 = prop_str[monthly_price_index1:].index('</span>')
            price = prop_str[monthly_price_index1:monthly_price_index1 + monthly_price_index2]
            price = self.strip_price(price)

            address_index1 = prop_str.index('<address') + len('<address data-test="property-card-addr">')
            address_index2 = prop_str.index('</address')
            address = prop_str[address_index1: address_index2].strip()

            link_index1 = prop_str.index('href') + 6
            link_index2 = prop_str.index('tabindex="0"') - 2
            link = prop_str[link_index1: link_index2]

            properties.append([price, address, link])

        return properties
