

import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2FAdmin%2FOrder%2FList")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.ID,"RememberMe").click()
#
# if(driver.find_element(By.ID,"RememberMe").get_attribute("checked") == "true"):
#     print("Checkbox is selected")

checkbox = driver.find_element(By.ID,"RememberMe").is_selected()
if checkbox:
    print("Checkbox Selected")
else:
    print("Not Selected")
time.sleep(10)