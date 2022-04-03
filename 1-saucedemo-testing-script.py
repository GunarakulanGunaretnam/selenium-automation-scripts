import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.maximize_window()

driver.get("https://www.saucedemo.com/")

driver.find_element_by_id("user-name").send_keys("standard_user")
driver.find_element_by_id("password").send_keys("secret_sauce")
driver.find_element_by_id("login-button").click()

lenth_of_item = int(len(driver.find_elements_by_css_selector(".btn_inventory")))

for x in range(lenth_of_item):
	driver.find_elements_by_css_selector(".btn_inventory")[x].click()


driver.find_element_by_id("shopping_cart_container").click()
driver.find_element_by_id("checkout").click()


driver.find_element_by_id("first-name").send_keys("Gunarakulan")
driver.find_element_by_id("last-name").send_keys("Gunaretnam")
driver.find_element_by_id("postal-code").send_keys("3456754321345")

driver.find_element_by_id("continue").click()

driver.find_element_by_id("finish").click()

driver.find_element_by_id("back-to-products").click()



