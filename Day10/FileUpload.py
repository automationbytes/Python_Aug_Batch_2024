import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.leafground.com/file.xhtml")

currentDir = os.getcwd()
print(currentDir)
filepath = os.path.join(currentDir,"1.jpg")
driver.find_element(By.ID,"j_idt88:j_idt89_input").send_keys(filepath)
time.sleep(10)