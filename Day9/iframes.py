'''

iframes - html inside a html

3 ways
1) id / name (string)
2) any of locators (driver.find...)
3) index (num)

'''

import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.XPATH,'//a[@title="Change Orientation"]').click()

driver.switch_to.frame("iframeResult")

driver.find_element(By.XPATH,"//button[text()='Try it']").click()

'''

alert = popup

accept - Okay, Yes
dismiss - Cancel, No
text - get the text of the alert message
sendkeys - send the values


'''

print(driver.switch_to.alert.text)
driver.switch_to.alert.send_keys("Devops")
#driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()

#go back to the original frame
driver.switch_to.parent_frame()
#or
#driver.switch_to.default_content() #it will go the first screen
driver.find_element(By.XPATH,'//a[@title="Change Orientation"]').click()

time.sleep(15) #hard wait