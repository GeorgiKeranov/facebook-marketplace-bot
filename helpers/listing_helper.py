# Remove and then publish each listing
import os


class Listing:
	def __init__(self, scraper):
		self.scraper = scraper

	def update_listings(self, listings, listing_type):
		# If listings are empty stop the function
		if not listings:
			return

		# Check if listing is already listed and remove it then publish it like a new one
		for listing in listings:
			# Remove listing if it is already published
			self.remove_listing(listing, listing_type)

			# Publish the listing in marketplace
			self.publish_listing(listing, listing_type)

	def remove_listing(self, data, listing_type):
		title = self.generate_title_for_listing_type(data, listing_type)
		listing_title = self.find_listing_by_title(title)

		# Listing not found so stop the function
		if not listing_title:
			return

		listing_title.click()

		# Click on the delete listing button
		self.scraper.element_click('div:not([role="gridcell"]) > div[aria-label="Delete"][tabindex="0"]')

		# Click on confirm button to delete
		confirm_delete_selector = 'div[aria-label="Delete listing"] div[aria-label="Delete"][tabindex="0"]'
		if self.scraper.find_element(confirm_delete_selector, False, 3):
			self.scraper.element_click(confirm_delete_selector)
		else:
			if self.scraper.find_element(confirm_delete_selector, True, 3):
				self.scraper.element_click(confirm_delete_selector)

		# Wait until the popup is closed
		self.scraper.element_wait_to_be_invisible('div[aria-label="Your Listing"]')

	def publish_listing(self, data, listing_type):
		# Click on create new listing button
		self.scraper.element_click('div[aria-label="Marketplace sidebar"] a[aria-label="Create new listing"]')
		# Choose listing type
		self.scraper.element_click(f'a[href="/marketplace/create/{listing_type}/"]')

		# Create string that contains all the image paths separated by \n
		images_path = self.generate_multiple_images_path(data['Photos Folder'], data['Photos Names'])
		# Add images to the listing
		# TODO: Allow image file-like objects to be referenced instead of a string/path.
		self.scraper.input_file_add_files('input[accept="image/*,image/heif,image/heic"]', images_path)

		# Add specific fields based on the listing_type
		function_name = f'add_fields_for_{listing_type}'
		# Call functions by name dynamically
		globals()[function_name](data)

		self.scraper.element_send_keys('label[aria-label="Price"] input', data['Price'])
		self.scraper.element_send_keys('label[aria-label="Description"] textarea', data['Description'])
		self.scraper.element_send_keys('label[aria-label="Location"] input', data['Location'])
		self.scraper.element_click('ul[role="listbox"] li:first-child > div')

		next_button_selector = 'div [aria-label="Next"] > div'
		next_button = self.scraper.find_element(next_button_selector, False, 3)
		if next_button:
			# Go to the next step
			self.scraper.element_click(next_button_selector)
			# Add listing to multiple groups
			self.add_listing_to_multiple_groups(data)

		# Publish the listing
		self.scraper.element_click('div[aria-label="Publish"]:not([aria-disabled])')

		if not next_button:
			self.post_listing_to_multiple_groups(data, listing_type)

	@staticmethod
	def generate_multiple_images_path(path, image_names):
		# Last character must be '/' because after that we are adding the name of the image
		if path[-1] != os.path.sep:
			path += os.path.sep

		images_path = ''

		# Create string that contains all the image paths separated by \n
		if image_names:
			for image_name in image_names:
				# Remove whitespace before and after the string
				image_name = image_name.strip()

				# Add "\n" for indicating new file
				if images_path != '':
					images_path += '\n'

				images_path += f'{path}{image_name}'

		return images_path

	# Add specific fields for listing from type vehicle
	def add_fields_for_vehicle(self, data, ):
		# Expand vehicle type select
		self.scraper.element_click('label[aria-label="Vehicle type"]')
		# Select vehicle type
		self.scraper.element_click_by_xpath(f'//span[text()="{data["Vehicle Type"]}"]')

		# Scroll to years select
		self.scraper.scroll_to_element('label[aria-label="Year"]')
		# Expand years select
		self.scraper.element_click('label[aria-label="Year"]')
		self.scraper.element_click_by_xpath(f'//span[text()="{data["Year"]}"]')

		self.scraper.element_send_keys('label[aria-label="Make"] input', data['Make'])
		self.scraper.element_send_keys('label[aria-label="Model"] input', data['Model'])

		# Scroll to mileage input
		self.scraper.scroll_to_element('label[aria-label="Mileage"] input')
		# Click on the mileage input
		self.scraper.element_send_keys('label[aria-label="Mileage"] input', data['Mileage'])

		# Expand fuel type select
		self.scraper.element_click('label[aria-label="Fuel type"]')
		# Select fuel type
		self.scraper.element_click_by_xpath(f'//span[text()="{data["Fuel Type"]}"]')

	# Add specific fields for listing from type item
	def add_fields_for_item(self, data):
		self.scraper.element_send_keys('label[aria-label="Title"] input', data['Title'])

		# Scroll to "Category" select field
		self.scraper.scroll_to_element('label[aria-label="Category"]')
		# Expand category select
		self.scraper.element_click('label[aria-label="Category"]')
		# Select category
		self.scraper.element_click_by_xpath(f'//span[text()="{data["Category"]}"]')

		# Expand category select
		self.scraper.element_click('label[aria-label="Condition"]')
		# Select category
		self.scraper.element_click_by_xpath(f'//span[@dir="auto"][text()="{data["Condition"]}"]')

		if data['Category'] == 'Sports & Outdoors':
			self.scraper.element_send_keys('label[aria-label="Brand"] input', data['Brand'])

	@staticmethod
	def generate_title_for_listing_type(data, listing_type):
		title = ''

		if listing_type == 'item':
			title = data['Title']

		if listing_type == 'vehicle':
			title = f'{data["Year"]} {data["Make"]} {data["Model"]}'

		return title

	def add_listing_to_multiple_groups(self, data):
		# Create an array for group names by splitting the string by this symbol ";"
		group_names = data['Groups'].split(';')

		# If the groups are empty do not do anything
		if not group_names:
			return

		# Post in different groups
		for group_name in group_names:
			# Remove whitespace before and after the name
			group_name = group_name.strip()

			self.scraper.element_click_by_xpath(f'//span[text()="{group_name}"]')

	def post_listing_to_multiple_groups(self, data, listing_type):
		title = self.generate_title_for_listing_type(data, listing_type)
		title_element = self.find_listing_by_title(title)

		# If there is no add with this title do not do anything
		if not title_element:
			return None

		# Create an array for group names by splitting the string by this symbol ";"
		group_names = data['Groups'].split(';')

		# If the groups are empty do not do anything
		if not group_names:
			return None

		search_input_selector = '[aria-label="Search for groups"]'

		# Post in different groups
		for group_name in group_names:
			# Click on the Share button to the listing that we want to share
			self.scraper.element_click(f'[aria-label="{title}"] + div [aria-label="Share"]')
			# Click on the Share to a group button
			self.scraper.element_click_by_xpath('//span[text()="Share to a group"]')

			# Remove whitespace before and after the name
			group_name = group_name.strip()

			# Remove current text from this input
			self.scraper.element_delete_text(search_input_selector)
			# Enter the title of the group in the input for search
			self.scraper.element_send_keys(search_input_selector, group_name[:51])

			self.scraper.element_click_by_xpath(f'//span[text()="{group_name}"]')

			if self.scraper.find_element('[aria-label="Create a public post…"]', False, 3):
				self.scraper.element_send_keys('[aria-label="Create a public post…"]', data['Description'])
			elif self.scraper.find_element('[aria-label="Write something..."]', False, 3):
				self.scraper.element_send_keys('[aria-label="Write something..."]', data['Description'])

			self.scraper.element_click('[aria-label="Post"]:not([aria-disabled])')
			# Wait till the post is posted successfully
			self.scraper.element_wait_to_be_invisible('[role="dialog"]')
			self.scraper.element_wait_to_be_invisible('[aria-label="Loading...]"')
			self.scraper.find_element_by_xpath('//span[text()="Shared to your group."]', False, 10)

	def find_listing_by_title(self, title):
		search_input = self.scraper.find_element('input[placeholder="Search your listings"]', False)
		# Search input field is not existing
		if not search_input:
			return None

		# Clear input field for searching listings before entering title
		self.scraper.element_delete_text('input[placeholder="Search your listings"]')
		# Enter the title of the listing in the input for search
		self.scraper.element_send_keys('input[placeholder="Search your listings"]', title)

		return self.scraper.find_element_by_xpath(f'//span[text()="{title}"]', False, 10)
