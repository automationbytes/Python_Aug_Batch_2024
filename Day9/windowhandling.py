
import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.LINK_TEXT,"Instagram").click()
driver.find_element(By.LINK_TEXT,"Meta Pay").click()

print(driver.title) #title
print(driver.current_url) #url

parentwindow = driver.current_window_handle #store the current window #pid
print(parentwindow)

allwindows = driver.window_handles #it includes parent window
print(allwindows)

for a in allwindows:
    if a != parentwindow:
        driver.switch_to.window(a)
        print(driver.title)
        print(driver.current_url)
        if driver.title == "Instagram":
            break

print(driver.title)
print(driver.current_url)

driver.find_element(By.NAME,"username").send_keys("Hello")

time.sleep(10)
