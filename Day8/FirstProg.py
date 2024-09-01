'''
id
name
link text
partial link text
class name
tag name
xpath
css

'''

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["enable-automation"])

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()

driver.find_element(By.ID,"email").send_keys("tom")
driver.find_element(By.NAME,"pass").send_keys("hello")
#driver.find_element(By.NAME,"login").click()
#driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Meta").click()

time.sleep(20)
#selenium 3
# driver.find_element_by_id("email").send_keys("tom")
