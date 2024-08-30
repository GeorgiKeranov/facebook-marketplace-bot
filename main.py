from helpers.scraper import Scraper
from helpers.csv_helper import get_data_from_csv
from helpers.listing_helper import update_listings
from helpers.logging_helper import log

scraper = Scraper('https://facebook.com')

# Add login functionality to the scraper
scraper.add_login_functionality('https://facebook.com', 'svg[aria-label="Your profile"]', 'facebook')
scraper.go_to_page('https://facebook.com/marketplace/you/selling')

try:

    # Get data for item type listings from csvs/items.csv
    item_listings = get_data_from_csv('items')
    #replace small dash if lister uses it.
    for item in item_listings:
        if "Condition" in item:
            item["Condition"] = item["Condition"].replace("-","–")
    # Publish all of the items into the facebook marketplace
    update_listings(item_listings, 'item', scraper)

except:
    log("failed to post item listing")

try:
    # Get data for vechile type listings from csvs/vechiles.csv
    vehicle_listings = get_data_from_csv('vehicles')
    # Publish all of the vehicles into the facebook marketplace
    update_listings(vehicle_listings, 'vehicle', scraper)
except:
    log("failed to post vehicle listing")

try:
    # Get data for rental type listings from csvs/items.csv
    rental_listings = get_data_from_csv('rentals')
    # Publish all of the rentals into the facebook marketplace
    update_listings(rental_listings, 'rental', scraper)
except:
    log("failed to post rental listing")
