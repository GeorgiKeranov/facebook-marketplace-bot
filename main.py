import time
from helpers.scraper import Scraper

scraper = Scraper('https://facebook.com')

# Add login functionality to the scraper
scraper.add_login_functionality('https://facebook.com', 'a[href="/me/"]', 'facebook')

# Go to the create new listing page
scraper.element_click('a[href="https://www.facebook.com/marketplace/?ref=bookmark"]')
