import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.maximize_window()
driver.get("file:///C:/Users/Gunarakulan/Desktop/selenium-tutorial-python/4-selenium-with-csv-file/index.html")

html = driver.find_element_by_tag_name("html")
html.send_keys(Keys.PAGE_DOWN)

df = pd.read_csv("dataset.csv",skiprows=1)

for index, row in df.iterrows():
	
	driver.find_element_by_id("employee_id").send_keys(row[0])

	driver.find_element_by_id("fullname").send_keys(row[1])

	driver.find_element_by_id("dob").send_keys(row[2])

	driver.find_element_by_id("phone_number").send_keys(row[3])

	driver.find_element_by_id("email").send_keys(row[4])

	if row[5] == "male":
		driver.find_element_by_id("inlineRadio1").click()

	elif row[5] == "female":
		driver.find_element_by_id("inlineRadio2").click()

	driver.find_element_by_id("department").send_keys(row[6])

	driver.find_element_by_id("address").send_keys(row[7])

	if row[8] == "yes":
		driver.find_element_by_id("epf").click()

	driver.find_element_by_id("btn").click()





