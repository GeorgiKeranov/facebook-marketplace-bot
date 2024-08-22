from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Facebook credentials
email = "rwatida.tinder@gmail.com"
password = "Tnr18062001!"
auto_reply_message = "Hello! We will get back to you soon."

# Initialize ChromeOptions
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

# Initialize WebDriver
service = Service(r'C:\chromedriver\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.facebook.com/")

# Log into Facebook
email_field = driver.find_element(By.ID, "email")
email_field.send_keys(email)
password_field = driver.find_element(By.ID, "pass")
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

time.sleep(5)  # Wait for login to complete

# Navigate to Messenger
driver.get("https://www.facebook.com/messages/t/")
time.sleep(5)  # Wait for Messenger to load

try:
    # Check for unread messages
    unread_messages = driver.find_elements(By.XPATH, "//div[@aria-label='Mark as read']")
    for message in unread_messages:
        message.click()
        time.sleep(2)  # Wait for message to open

        # Send auto-reply
        message_box = driver.find_element(By.XPATH, "//div[@aria-label='Type a message...']")
        message_box.send_keys(auto_reply_message)
        message_box.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for message to send
except:
    print("it failed here")

# Close the browser
driver.quit()
