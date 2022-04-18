from helpers.scraper import Scraper
from helpers.csv_helper import get_data_from_csv
from helpers.listing_helper import update_listings

scraper = Scraper('https://facebook.com')

# Add login functionality to the scraper
scraper.add_login_functionality('https://facebook.com', 'a[href="/me/"]', 'facebook')

# Go to the marketplace page
scraper.element_click('a[href="https://www.facebook.com/marketplace/?ref=bookmark"]')

# Click on create new listing button
scraper.element_click('div[aria-label="Marketplace sidebar"] a[aria-label="Create new listing"]')

# Click on Your Listings button
scraper.element_click('div[aria-label="Marketplace Composer"] a[href="/marketplace/you/selling/"]:not([aria-current="page"])')

# Get data for item type listings from csvs/items.csv
item_listings = get_data_from_csv('items')
# Publish all of the items into the facebook marketplace
update_listings(item_listings, 'item', scraper)

# Get data for vechile type listings from csvs/vechiles.csv
vehicle_listings = get_data_from_csv('vehicles')
# Publish all of the vehicles into the facebook marketplace
update_listings(vehicle_listings, 'vehicle', scraper)
