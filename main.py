import time
from scraper import Scraper

scraper = Scraper('https://facebook.com')

# Add login functionality to the scraper
scraper.add_login_functionality('https://facebook.com', 'a[href="/me/"]', 'facebook')

# Go to the create new listing page
scraper.element_click('a[href="https://www.facebook.com/marketplace/?ref=bookmark"]')
scraper.element_click('div[aria-label="Marketplace sidebar"] a[aria-label="Create new listing"]')

# Choose listing type - Item
scraper.element_click('a[href="/marketplace/create/item/"]')

# Add images to the the listing
scraper.element_send_keys('input[accept="image/*,image/heif,image/heic"]', "F:\Pictures and Videos\Ads\Екип крос\Ръкавици\IMG_4252.JPG \n F:\Pictures and Videos\Ads\Екип крос\Ръкавици\IMG_4255.JPG")

# Click on the title input
scraper.element_click('label[aria-label="Title"] input')
# Type title
scraper.element_send_keys('label[aria-label="Title"] input', 'Oneal ръкавици мотокрос крос ендуро вело')

# Click on the price input
scraper.element_click('label[aria-label="Price"] input')
# Type price
scraper.element_send_keys('label[aria-label="Price"] input', '20')

# Expand category select
scraper.element_click('label[aria-label="Category"]')
# Select category
scraper.element_click_by_xpath('//span[text()="Sports & Outdoors"]')

# Expand category select
scraper.element_click('label[aria-label="Condition"]')
# Select category
scraper.element_click_by_xpath('//span[text()="Used - Good"]')

# Click on the description textarea
scraper.element_click('label[aria-label="Description"] textarea')
# Type description
scraper.element_send_keys('label[aria-label="Description"] textarea', """Цената е в лева - 20лв
Ръкавиците са размер - L

Мотокрос / Ендуро / Вело / ръкавици Oneal

Изпращам ги с Еконт и Спиди с преглед и тест.
""")

# Click on the brand input
scraper.element_click('label[aria-label="Brand"] input')
# Type brand
scraper.element_send_keys('label[aria-label="Brand"] input', 'Oneal')

# Go to the next step
scraper.element_click('div [aria-label="Next"] > div')

# List in groups
scraper.element_click_by_xpath('//span[text()="МОТО ПАЗАР ( МОТОРИ ЕКИПИРОВКА ЧАСТИ АКСЕСОАРИ )"]')

# Publish the listing
scraper.element_click_by_xpath('//span[text()="Publish"]')

time.sleep(300)

def publish_vehicle():
	# Choose listing type - Vehicle
	scraper.element_click('a[href="/marketplace/create/vehicle/"]')

	# Expand vehicle type select
	scraper.element_click('label[aria-label="Vehicle type"]')
	# Select vehicle type
	scraper.element_click_by_xpath('//span[text()="Motorcycle"]')

	# Add images to the the listing
	scraper.element_send_keys('input[accept="image/*,image/heif,image/heic"]', "F:\Pictures and Videos\Ads\Мотори\CRF450R\With Label\IMG_3144.jpg \n F:\Pictures and Videos\Ads\Мотори\CRF450R\With Label\IMG_3147.jpg")

	# Expand years select
	scraper.element_click('label[aria-label="Year"]')
	# Select year
	scraper.element_click_by_xpath('//span[text()="2003"]')

	# Click on the make input
	scraper.element_click('label[aria-label="Make"] input')
	# Type make
	scraper.element_send_keys('label[aria-label="Make"] input', 'Honda')

	# Click on the model input
	scraper.element_click('label[aria-label="Model"] input')
	# Type model
	scraper.element_send_keys('label[aria-label="Model"] input', 'CRF450R На Части')

	# Click on the mileage input
	scraper.element_click('label[aria-label="Mileage"] input')
	# Type mileage
	scraper.element_send_keys('label[aria-label="Mileage"] input', '1234')

	# Scroll to the other fields
	scraper.driver.execute_script("""var scrollDiv = document.querySelector('div[role="main"] > div:first-child > div:nth-child(4)'); scrollDiv.scrollTop = 850;""")

	# Click on the price input
	scraper.element_click('label[aria-label="Price"] input')
	# Type price
	scraper.element_send_keys('label[aria-label="Price"] input', '1000')

	# Expand fuel type select
	scraper.element_click('label[aria-label="Fuel type"]')
	# Select fuel type
	scraper.element_click_by_xpath('//span[text()="Gasoline"]')

	# Click on the description textarea
	scraper.element_click('label[aria-label="Description"] textarea')
	# Type description
	scraper.element_send_keys('label[aria-label="Description"] textarea', 'Моторът се продава само на части!')

	# Go to the next step
	scraper.element_click('div [aria-label="Next"] > div')

	# List in groups
	scraper.element_click_by_xpath('//span[text()="МОТО ПАЗАР ( МОТОРИ ЕКИПИРОВКА ЧАСТИ АКСЕСОАРИ )"]')

	# Publish the listing
	scraper.element_click_by_xpath('//span[text()="Publish"]')

