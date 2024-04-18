# Selenium library allows us to interact with the web
# Everything Selenium does is send the browser commands to do something or send requests for information.
# Selenium interfaces with the internet by using a web driver, which is a browser that Selenium can use to automate web processes.
# For example, as web drivers you can use Chrome or Gecko driver.
# To install Selenium, use python (pip3 install selenium)
# To install a driver, follow good instructions, its the best to download the latest stable version from the main website, brew didn't work as expected.

# Import the webdriver module
from selenium import webdriver
# Import Chrome options, they are essential for managing Chrome correctly (otherwise it closes immediately)
from selenium.webdriver.chrome.options import Options
# Import By to find web elements in DOM
from selenium.webdriver.common.by import By
# Import the Select object to be able to select something from dropdown lists
from selenium.webdriver.support.select import Select

# Mandatory Chrome options
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)

# Initialize the web driver
driver = webdriver.Chrome(options=chrome_options)
# Navigate to the web page
driver.get('https://www.selenium.dev/selenium/web/web-form.html')

# Find the text box and type something in it
messageField = driver.find_element(By.ID, 'my-text-id')
messageField.send_keys('Hello world!')

# Find the password box and type something in it
messageField = driver.find_element(By.NAME, 'my-password')
messageField.send_keys('password')

# Find the textarea box and type something in it
messageField = driver.find_element(By.NAME, 'my-textarea')
messageField.send_keys('I can type something here!')

# Locate the select element, then use it to initialize a Select object
selectElement = driver.find_element(By.NAME, 'my-select')
select = Select(selectElement)
# Select the preferred option
select.select_by_visible_text('Two')

# Datalist
input = driver.find_element(By.NAME, 'my-datalist')
option = driver.find_elements(By.XPATH, '//*[@id="my-options"]/option[2]')
# How to take a value from the list?
input.send_keys('New York')

# Checkboxes
Checkbox1 = driver.find_element(By.ID, 'my-check-1')
Checkbox2 = driver.find_element(By.ID, 'my-check-2')
Checkbox1.click()
Checkbox2.click()

# Radios
Radio1 = driver.find_element(By.ID, 'my-radio-1')
Radio2 = driver.find_element(By.ID, 'my-radio-2')
Radio1.click()
Radio2.click()

# Color Picker
# ColorPicker = driver.find_element(By.NAME, 'my-colors')


# There's so much more to learn! Fill in the rest of the form later!

# Find the Submit button and click it
# submitButton = driver.find_element(By.TAG_NAME, 'button')
# submitButton.click()