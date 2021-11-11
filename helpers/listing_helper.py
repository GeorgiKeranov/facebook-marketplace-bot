def publish_listing(listing):
	# Click on create new listing button
	scraper.element_click('div[aria-label="Marketplace sidebar"] a[aria-label="Create new listing"]')

	# Choose listing type
	scraper.element_click('a[href="/marketplace/create/LISTING_TYPE_HERE/"]')

	# Add images to the the listing
	scraper.element_send_keys('input[accept="image/*,image/heif,image/heic"]', 'IMAGES_HERE')

	# ONLY FOR LISTING_TYPE - vehicle
	if listing['Listing Type'] == 'Vehicle':
		# Expand vehicle type select
		scraper.element_click('label[aria-label="Vehicle type"]')
		# Select vehicle type
		scraper.element_click_by_xpath('//span[text()="VEHICLE_TYPE_HERE"]')

		# Expand years select
		scraper.element_click('label[aria-label="Year"]')
		# Select year
		scraper.element_click_by_xpath('//span[text()="YEAR_HERE"]')

		# Click on the make input
		scraper.element_click('label[aria-label="Make"] input')
		# Type make
		scraper.element_send_keys('label[aria-label="Make"] input', 'MAKE_HERE')

		# Click on the model input
		scraper.element_click('label[aria-label="Model"] input')
		# Type model
		scraper.element_send_keys('label[aria-label="Model"] input', 'MODEL_HERE')

		# Click on the mileage input
		scraper.element_click('label[aria-label="Mileage"] input')
		# Type mileage
		scraper.element_send_keys('label[aria-label="Mileage"] input', 'MILEAGE_HERE')

		# Scroll to the bottom fields
		scraper.driver.execute_script("""var scrollDiv = document.querySelector('div[role="main"] > div:first-child > div:nth-child(4)'); scrollDiv.scrollTop = 850;""")

		# Expand fuel type select
		scraper.element_click('label[aria-label="Fuel type"]')
		# Select fuel type
		scraper.element_click_by_xpath('//span[text()="Gasoline"]')

	# ONLY FOR LISTING TYPE - item
	if listing['Listing Type'] == 'Item':
		# Click on the title input
		scraper.element_click('label[aria-label="Title"] input')
		# Type title
		scraper.element_send_keys('label[aria-label="Title"] input', 'TITLE_HERE')
	
		# Expand category select
		scraper.element_click('label[aria-label="Category"]')
		# Select category
		scraper.element_click_by_xpath('//span[text()="CATEGORY_HERE"]')

		# Expand category select
		scraper.element_click('label[aria-label="Condition"]')
		# Select category
		scraper.element_click_by_xpath('//span[text()="CONDITION_HERE"]')

		# Click on the brand input
		scraper.element_click('label[aria-label="Brand"] input')
		# Type brand
		scraper.element_send_keys('label[aria-label="Brand"] input', 'BRAND_HERE')

	# Click on the price input
	scraper.element_click('label[aria-label="Price"] input')
	# Type price
	scraper.element_send_keys('label[aria-label="Price"] input', 'PRICE_HERE')

	# Click on the description textarea
	scraper.element_click('label[aria-label="Description"] textarea')
	# Type description
	scraper.element_send_keys('label[aria-label="Description"] textarea', 'DESCRIPTION_HERE')

	# Go to the next step
	scraper.element_click('div [aria-label="Next"] > div')

	# List in groups
	scraper.element_click_by_xpath('//span[text()="GROUP_NAME_HERE"]')

	# Publish the listing
	scraper.element_click_by_xpath('//span[text()="Publish"]')
