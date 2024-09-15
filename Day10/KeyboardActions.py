import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.openmultipleurl.com/")
driver.maximize_window()
driver.implicitly_wait(30)
#
driver.find_element(By.ID,"list_urls").send_keys("hello")
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
time.sleep(5)
actions.key_down(Keys.DELETE).key_up(Keys.DELETE)
actions.perform()

time.sleep(10)