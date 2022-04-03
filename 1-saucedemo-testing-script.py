import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.maximize_window()

driver.get("https://www.saucedemo.com/")