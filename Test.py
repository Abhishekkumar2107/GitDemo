from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver =webdriver.Chrome()

time.sleep(5)

driver.get("https://www.selenium.dev/downloads/")

driver.find_element(By.name "username").send_keys("abhishek.123")
driver.find_element(By.polder "username").send_keys("abhishek.123")
driver.find_element(By.placeholder "username").click()
time.sleep(5)

driver.quit()