import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.implicitly_wait(30)
#

act = ActionChains(driver)
act.scroll_to_element(driver.find_element(By.XPATH,"//div[text()='India']"))
act.perform()

time.sleep(10)