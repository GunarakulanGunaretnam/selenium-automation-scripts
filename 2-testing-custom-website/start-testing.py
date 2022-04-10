import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("./chromedriver")
driver.maximize_window()
driver.get("file:///C:/Users/Gunarakulan/Desktop/selenium-tutorial-python/2-testing-custom-website/index.html")


person1 = []
person2 = []


with open("person-1-list.txt") as person1_file:
	for line in person1_file:
		person1.append(line.strip())


with open("person-2-list.txt") as person2_file:
	for line in person2_file:
		person2.append(line.strip())


for x in range(1, 100):

	driver.find_element_by_id("fname").send_keys(person1[x])
	driver.find_element_by_id("lname").send_keys(person2[x])

	driver.find_element_by_id("btn").click()