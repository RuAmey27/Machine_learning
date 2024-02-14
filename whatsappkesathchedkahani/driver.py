from selenium import webdriver

# Initialize a WebDriver object
driver = webdriver.Chrome()

# List all attributes and methods of the WebDriver object
attributes_and_methods = dir(driver)
for attribute_or_method in attributes_and_methods:
    print(attribute_or_method)
