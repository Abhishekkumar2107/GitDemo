from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

# Date of Birth
driver.find_element(By.XPATH,"//input[@id='dob']").click()
time.sleep(10)
driver.maximize_window()