import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.google.com")
print(driver.title)
search_bar = driver.find_element_by_name("q")
search_bar.clear()
search_bar.send_keys("facebook")
search_bar.send_keys(Keys.RETURN)
driver.find_element_by_xpath('/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div[1]/div/a/h3').click()

time.sleep(2)
driver.find_element_by_id("email").send_keys("testing_email@fake.com")
driver.find_element_by_id("pass").send_keys("12345678909876543")

time.sleep(1)

driver.find_element_by_name("login").click()



