'''
input#email -id
#any tags
input[placeholder="Email address or phone number"]

#contains
input[placeholder*='address or phone number']

#text
button

'''


import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.CSS_SELECTOR,'a[data-testid="open-registration-form-button"]').click()
driver.find_element(By.XPATH,'//input[@aria-label="First name"]').send_keys("Tom")
time.sleep(20)