#//span[text()='Wall Decor']

import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.snapdeal.com/")
driver.maximize_window()
driver.implicitly_wait(30)
#
driver.find_element(By.XPATH,"//span[text()='Wall Decor']").click()
#driver.execute_script("arguments[0].click()",driver.find_element(By.XPATH,"//span[text()='Wall Decor']"))