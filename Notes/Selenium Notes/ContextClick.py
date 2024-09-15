import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
driver.implicitly_wait(30)
#

act = ActionChains(driver)
act.context_click(driver.find_element(By.XPATH,"//span[text()='right click me']"))
act.move_to_element(driver.find_element(By.XPATH,"//span[text()='Copy']"))
act.click(driver.find_element(By.XPATH,"//span[text()='Copy']"))

act.perform()

driver.switch_to.alert.accept()
time.sleep(10)