import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://emicalculator.net/")
driver.maximize_window()
driver.implicitly_wait(30)
#

act = ActionChains(driver)
drag = driver.find_element(By.XPATH,"//span[text()='50L']/..")
drop = driver.find_element(By.XPATH,"//span[text()='125L']/..")
#
# act.drag_and_drop(drag,drop)
# act.perform()

act.click_and_hold(drag)
act.release(drop)
act.perform()


time.sleep(10)