import os
import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome("./chromedriver")
driver.maximize_window()
driver.get("file:///C:/Users/Gunarakulan/Desktop/selenium-with-ocr/index.html")



def clean_up(text):
    text = text.replace(" ","").replace("01)", "").replace("02)", "").replace("03)", "").replace("04)", "").replace("\n\x0c", "").replace("\n","|")
    return text

for filename in os.listdir('inputs/'):

    text = pytesseract.image_to_string(Image.open(f'inputs/{filename}'))

    cleaned_data = clean_up(text)

    splited_data = cleaned_data.split("|")


    for x in splited_data:

        if x != "":
            entity_name = x.split("=")[0].strip()
            entity_value = x.split("=")[1].strip()

        

            if entity_name == "FirstName":
                driver.find_element_by_id("firstname").send_keys(entity_value)

            elif entity_name == "LastName":
                driver.find_element_by_id("lastname").send_keys(entity_value)

            elif entity_name == "Age":
                driver.find_element_by_id("age").send_keys(entity_value)

            elif entity_name == "Designation":
                driver.find_element_by_id("designation").send_keys(entity_value)

    driver.find_element_by_id("btn").click()




