'''

Absolute Xpath - Full path starting from HTML node - /
Relative Xpath - particular node level - // (always recommended)

//tagname[@attribute = 'value']
//input[@type="password"]
//input[@data-testid="royal_pass"]

//tagname[@attribute = "value" and @attribute2 = "value2"]
//input[@type="password" and @data-testid="royal_pass"]

//tagname[contains(@attribute,"va")]
//a[contains(@data-testid,"-form-")]


//tagname[contains(@attribute,"va") and @attribute2 = "value2"]
//a[contains(@data-testid,"-form-") and @role="button"]

//tagname[text()='value']
//a[text()='Create new account']
//button[text()='Log in']




'''
import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.XPATH,"//a[text()='Create new account']").click()
driver.find_element(By.XPATH,'//input[@aria-label="First name"]').send_keys("Tom")
time.sleep(20)