import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

driver.find_element_by_id("user-name").send_keys("standard_user")
driver.find_element_by_id("password").send_keys("secret_sauce")
driver.find_element_by_id("login-button").click()
