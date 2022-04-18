import time
from helpers.scraper import Scraper
from helpers.csv_helper import get_data_from_csv
from helpers.listing_helper import remove_listing
from helpers.listing_helper import publish_listing
from helpers.listing_helper import generate_title_for_listing_type
from helpers.listing_helper import add_listing_to_multiple_groups

# Get data from csv then remove listings if already exist and finaly publish the listings into the facebook marketplace
def get_data_and_publish_listings(file_name, listings_type, scraper):
	# Get data from csv file
	listings = get_data_from_csv(file_name)

	# If data is empty stop the function
	if not listings:
		return

	# Check if listing is already listed and remove it then publish it like a new one
	for listing in listings:
		listing_title = generate_title_for_listing_type(listing, listings_type)

		# Remove listing if it is already published
		remove_listing(listing_title, scraper)

		# Publish the listing in marketplace
		publish_listing(listing, listings_type, scraper)

		# Add the published listing in multiple groups
		add_listing_to_multiple_groups(listing_title, listing['Groups'], scraper)

scraper = Scraper('https://facebook.com')

# Add login functionality to the scraper
scraper.add_login_functionality('https://facebook.com', 'a[href="/me/"]', 'facebook')

# Go to the marketplace page
scraper.element_click('a[href="https://www.facebook.com/marketplace/?ref=bookmark"]')

# Click on create new listing button
scraper.element_click('div[aria-label="Marketplace sidebar"] a[aria-label="Create new listing"]')

# Click on Your Listings button
scraper.element_click('div[aria-label="Marketplace Composer"] a[href="/marketplace/you/selling/"]:not([aria-current="page"])')

# Publish all the vehicles from csvs/items.csv into the facebook marketplace
get_data_and_publish_listings('items', 'item', scraper)

# Publish all the vehicles from csvs/vehicles.csv into the facebook marketplace
get_data_and_publish_listings('vehicles', 'vehicle', scraper)
