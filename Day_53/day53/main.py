from zillow import ZillowScraper
from property_recorder import PropertyRecorder
import os

zillow_scraper = ZillowScraper()
listings = zillow_scraper.get_listings()
prop_recorder = PropertyRecorder(form_link=os.environ['GOOGLE_FORM_LINK'])

for listing in listings:
    prop_recorder.record_listing(address=listing[1], price=listing[0], link=listing[2])
