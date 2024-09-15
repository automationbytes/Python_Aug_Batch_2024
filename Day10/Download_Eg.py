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
driver.get("https://www.leafground.com/file.xhtml")

driver.find_element(By.XPATH,"//span[text()='Download']").click()
time.sleep(10)