'''

implicit wait
Explicit wait
fluent wait (also included inside explicit wait)


'''

import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(30)


driver.find_element(By.ID,"user-name").send_keys("performance_glitch_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions="Exception")
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//a[@data-test="shopping-cart-link"]')))
driver.find_element(By.XPATH,'//a[@data-test="shopping-cart-link"]').click()



time.sleep(50)