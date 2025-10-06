#
# Notes  :
# 1) Selenium is a free (open source) automated testing suite for web applications across different browsers and platforms.
# 2) ChromeDriver - WebDriver for Chrome. WebDriver is an open source tool for automated testing of webapps across many browsers.
#

#
# Imports
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#
# Functions
#
def create_driver():
    # Get Google Chrome driver, must be on path
    driver = webdriver.Chrome()
    return driver

def close_driver(driver):
    driver.close()

def search_pythonorg(driver,search_value):
    # Navigate to page
    driver.get("http://www.python.org")

    # Capture the <Title> element
    title = driver.title

    # Find the element whoose name = "q". This should be the main search field on the home page!
    elem = driver.find_element(By.NAME,"q")

    # Send some characters to this element
    # - firstly clear the element in case any characters are in query field by default
    # - then use send_keys to put text into the query field (this simulates as if you entered the text manually)
    elem.clear()
    elem.send_keys(search_value)
    elem.send_keys(Keys.RETURN)

    # Capture the HTML page
    page_source = driver.page_source

    # Return captured values
    return title, page_source
