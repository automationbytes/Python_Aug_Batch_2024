import os
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--safebrowsing-disable-download-protection")
prefs = {"download.default_directory": os.getcwd()}
options.add_experimental_option("prefs",prefs)


driver = webdriver.Chrome(options = options)
driver.get("https://demo.guru99.com/test/web-table-element.php")
time.sleep(2)


row = driver.find_elements(By.XPATH,'//table[@class="dataTable"]//tr')
rowsize = len(row)
print(rowsize)

#//table[@class="estimate-table"]//tr//td[2]

for i in range(1, rowsize):
    productName = driver.find_element(By.XPATH,f'//table[@class="dataTable"]//tr[{i}]//td/a').text
    print(productName)
    if productName == "Ujjivan Financial":
        CurrentPrice = driver.find_element(By.XPATH, f'//table[@class="dataTable"]//tr[{i}]//td[4]').text
        print(CurrentPrice)
        break
