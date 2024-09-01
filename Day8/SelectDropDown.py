'''

Select dropdown - uses select tag
we can directly handle with inbuild selenium methods

3 ways select the values
selectbyvalue - value attribute
selectbyvisibletext - ui
selectbyindex - occurence - starts with 0

'''


import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.CSS_SELECTOR,'a[data-testid="open-registration-form-button"]').click()
driver.find_element(By.XPATH,'//input[@aria-label="First name"]').send_keys("Tom")


dropdownDay = Select(driver.find_element(By.CSS_SELECTOR,'select[aria-label="Month"]'))
#dropdownDay.select_by_value("5")
#dropdownDay.select_by_visible_text("Dec")
dropdownDay.select_by_index(5)
time.sleep(20)
