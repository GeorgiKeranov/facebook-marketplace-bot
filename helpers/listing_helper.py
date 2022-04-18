import time

def remove_listing(title, scraper):
	# Enter the title of the listing in the input for search
	scraper.element_send_keys('input[placeholder="Search your listings"]', title)

	# Search for the listing by the title
	listing_title = scraper.find_element_by_xpath('//span[text()="' + title + '"]', False)
	# Listing not found so stop the function
	if not listing_title:
		return
	listing_title.click()

	# Click on the delete listing button
	scraper.element_click('div[aria-label="Delete"]')
	# Click on confirm button to delete
	scraper.element_click('div[aria-label="Delete Listing"] div[aria-label="Delete"][tabindex="0"]')
	# Wait until the popup is closed
	scraper.element_wait_to_be_invisible('div[aria-label="Your Listing"]')

def publish_listing(data, listing_type, scraper):
	# Click on create new listing button
	scraper.element_click('div[aria-label="Marketplace sidebar"] a[aria-label="Create new listing"]')
	# Choose listing type
	scraper.element_click('a[href="/marketplace/create/' + listing_type + '/"]')

	# Create string that contains all of the image paths separeted by \n
	images_path = generate_multiple_images_path(data['Photos Folder'], data['Photos Names'])
	# Add images to the the listing
	scraper.input_file_add_files('input[accept="image/*,image/heif,image/heic"]', images_path)

	# Add specific fields based on the listing_type
	function_name = 'add_fields_for_' + listing_type
	# Call function by name dynamically
	globals()[function_name](data, scraper)
	
	scraper.element_send_keys('label[aria-label="Price"] input', data['Price'])
	scraper.element_send_keys('label[aria-label="Description"] textarea', data['Description'])
	# Go to the next step
	scraper.element_click('div [aria-label="Next"] > div')
	# Publish the listing
	scraper.element_click_by_xpath('//span[text()="Publish"]')

def generate_multiple_images_path(path, images):
	images_path = ''
	
	# Split image names into array by this symbol ";"
	image_names = images.split(';')

	# Create string that contains all of the image paths separeted by \n
	if image_names:
		for image_name in image_names:
			# Remove whitespace before and after the string
			image_name = image_name.strip()

			# Add "\n" for indicating new file
			if images_path != '':
				images_path += '\n'

			images_path += path + image_name

	return images_path

# Add specific fields for listing from type vehicle
def add_fields_for_vehicle(data, scraper):
	# Expand vehicle type select
	scraper.element_click('label[aria-label="Vehicle type"]')
	# Select vehicle type
	scraper.element_click_by_xpath('//span[text()="' + data['Vehicle Type'] + '"]')

	# Scroll to years select
	scraper.scroll_to_element('label[aria-label="Year"]')
	# Expand years select
	scraper.element_click('label[aria-label="Year"]')
	scraper.element_click_by_xpath('//span[text()="' + data['Year'] + '"]')

	scraper.element_send_keys('label[aria-label="Make"] input', data['Make'])
	scraper.element_send_keys('label[aria-label="Model"] input', data['Model'])

	# Scroll to mileage input
	scraper.scroll_to_element('label[aria-label="Mileage"] input')	
	# Click on the mileage input
	scraper.element_send_keys('label[aria-label="Mileage"] input', data['Mileage'])

	# Expand fuel type select
	scraper.element_click('label[aria-label="Fuel type"]')
	# Select fuel type
	scraper.element_click_by_xpath('//span[text()="' + data['Fuel Type'] + '"]')

# Add specific fields for listing from type item
def add_fields_for_item(data, scraper):
	scraper.element_send_keys('label[aria-label="Title"] input', data['Title'])

	# Scroll to "Category" select field
	scraper.scroll_to_element('label[aria-label="Category"]')
	# Expand category select
	scraper.element_click('label[aria-label="Category"]')
	# Select category
	scraper.element_click_by_xpath('//span[text()="' + data['Category'] + '"]')

	# Expand category select
	scraper.element_click('label[aria-label="Condition"]')
	# Select category
	scraper.element_click_by_xpath('//span[@dir="auto"][text()="' + data['Condition'] + '"]')

	if data['Category'] == 'Sports & Outdoors':
		scraper.element_send_keys('label[aria-label="Brand"] input', data['Brand'])

def generate_title_for_listing_type(data, listing_type):
	title = ''

	if listing_type == 'item':
		title = data['Title']

	if listing_type == 'vehicle':
		title = data['Year'] + ' ' + data['Make'] + ' ' + data['Model']

	return title

def add_listing_to_multiple_groups(listing_title, groups, scraper):
	# If the groups are empty do not do nothing
	if not groups:
		return

	# Wait until "Your Listings" page is loaded
	scraper.find_element_by_xpath('//h1[text()="Your Listings"]')

	# Click on the title of the listing
	scraper.element_click_by_xpath('//span[text()="' + listing_title + '"]')

	# Click on the more button
	scraper.element_click('div[aria-label="More"] > i')

	# Get the "List in More Places" button
	list_in_more_places_button = scraper.find_element_by_xpath('//span[text()="List in More Places"]', False)

	# If the the "List in More Places" button is found list in all of the given groups
	if list_in_more_places_button:
		list_in_more_places_button.click()

		# Create an array for group names by spliting the string by this symbol ";"
		group_names = groups.split(';')
		
		# Post in different groups
		for group_name in group_names:
			# Remove whitespace before and after the name
			group_name = group_name.strip()

			scraper.element_click_by_xpath('//span[text()="' + group_name + '"]')

		# Click on the 'Post' button
		scraper.element_click('div[aria-label="Post"][tabindex="0"]')

	# Click on the 'X' button to close the current listing window
	scraper.element_click('div[aria-label="Your Listing"] div[aria-label="Close"]')