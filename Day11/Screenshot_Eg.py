import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://www.redbus.in/")

# currentDir = os.getcwd()
# print(currentDir)
# filepath = os.path.join(currentDir,"1.jpg")
# driver.find_element(By.ID,"j_idt88:j_idt89_input").send_keys(filepath)
#driver.save_screenshot("leafground.png")
driver.fullscreen_window()
driver.get_screenshot_as_file("red.png")
driver.get_full_page_screenshot_as_file("redbus.png")



time.sleep(10)