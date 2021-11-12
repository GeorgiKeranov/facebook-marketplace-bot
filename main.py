import time
from helpers.scraper import Scraper
from helpers.csv_helper import get_data_from_csv
from helpers.listing_helper import publish_listing

scraper = Scraper('https://facebook.com')

# Add login functionality to the scraper
scraper.add_login_functionality('https://facebook.com', 'a[href="/me/"]', 'facebook')

# Go to the create new listing page
scraper.element_click('a[href="https://www.facebook.com/marketplace/?ref=bookmark"]')

# Publish items
items = get_data_from_csv('items')
if items:
	for item in items:
		publish_listing(item, 'item', scraper)

# Publish vehicles
vehicles = get_data_from_csv('vehicles')
if vehicles:
	for vehicle in vehicles:
		publish_listing(vehicle, 'vehicle', scraper)

# Wait some time before closing the Chrome
time.sleep(15)
