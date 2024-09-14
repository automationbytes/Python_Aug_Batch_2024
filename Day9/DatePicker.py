import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://trains.abhibus.com/?channel=abhibus-web")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.ID,'dateOfJourney').click()

Dates = driver.find_elements(By.XPATH,"//span/p")
for d in Dates:
    print(d.text)
    if d.text == "19":
        d.click()
        break

time.sleep(10)