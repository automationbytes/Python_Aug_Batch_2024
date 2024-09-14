'''
ul - unordered list
li - list item

ol - ordered list
li - list item

'''

import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.ID,"src").send_keys("Ch")

srcDropdown = driver.find_elements(By.XPATH,"//ul/li//text[1]")
for s in srcDropdown:
    print(s.text)
    if s.text == "Chandigarh": #full match
        s.click()
        break


driver.find_element(By.ID,"dest").send_keys("Ba")
destDropdown = driver.find_elements(By.XPATH,"//ul/li//text[1]")
for d in destDropdown:
    print(d.text)
    if "Airport" in d.text: #partial match
        d.click()
        break

driver.find_element(By.ID,"onwardCal").click()


time.sleep(10)