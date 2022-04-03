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
	print(x)
	#driver.find_elements_by_css_selector(".btn_inventory")[x].click()




