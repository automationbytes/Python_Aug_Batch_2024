import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
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

driver.execute_script("window.scrollBy(0,1500)")
time.sleep(10)

driver.execute_script("window.scrollBy(0,-500)")

time.sleep(10)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

time.sleep(10)


driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")

time.sleep(10)

driver.execute_script("arguments[0].scrollIntoView(true)",driver.find_element(By.XPATH,"//div[text()='India']"))
time.sleep(10)