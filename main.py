import logging
from helpers.scraper import Scraper
from helpers.csv_helper import get_data_from_csv
from helpers.listing_helper import Listing

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

scraper = Scraper('https://facebook.com')

# Add login functionality to the scraper
scraper.add_login_functionality('https://facebook.com', 'svg[aria-label="Your profile"]', 'facebook')
scraper.go_to_page('https://facebook.com/marketplace/you/selling')

# Get Listing Instance
listing = Listing(scraper)

# Get data for item type listings from csvs/items.csv
item_listings = get_data_from_csv('csvs', 'items.csv')
# Publish all of the items into the facebook marketplace
listing.update_listings(item_listings, 'item')

# Get data for vechile type listings from csvs/vechiles.csv
vehicle_listings = get_data_from_csv('csvs', 'vehicles.csv')
# Publish all of the vehicles into the facebook marketplace
listing.update_listings(vehicle_listings, 'vehicle')
