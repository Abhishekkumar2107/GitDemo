from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ===== USER INPUT =====
date = input("Enter date (DD): ")
month = input("Enter month (May): ")
year = input("Enter year (2026): ")

# ===== DRIVER SETUP =====
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://jqueryui.com/datepicker/")

wait = WebDriverWait(driver, 15)

# ===== SWITCH TO IFRAME =====
wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "demo-frame")))

# ===== OPEN DATE PICKER =====
wait.until(EC.element_to_be_clickable((By.ID, "datepicker"))).click()

# ===== SELECT MONTH & YEAR =====
while True:
    current_month = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ui-datepicker-month"))
    ).text

    current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

    if current_month == month and current_year == year:
        break

    # 🔥 FIX: wait + JS click (avoids ElementNotInteractableException)
    next_btn = wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[@title='Next']"))
    )

    driver.execute_script("arguments[0].click();", next_btn)
    time.sleep(1)

# ===== SELECT DATE =====
wait.until(
    EC.element_to_be_clickable((By.XPATH, f"//a[text()='{date}']"))
).click()

print("✅ Date selected successfully!")

time.sleep(5)
driver.quit()