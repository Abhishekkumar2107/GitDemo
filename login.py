from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Username']"))).send_keys("Admin")

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Password']"))).send_keys("admin123")

wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

time.sleep(25)

driver.quit()
