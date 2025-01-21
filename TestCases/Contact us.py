from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
print(driver.title)
try:
    driver.get("http://localhost:8069/web/login")
    time.sleep(3)

    contact_us_button = driver.find_element(By.XPATH, '//a[text()="Contact Us"]')
    contact_us_button.click()
    time.sleep(3)

    expected_url = "http://localhost:8069/contactus"  # Replace with the actual Contact Us URL
    current_url = driver.current_url
    if expected_url == current_url:
        print("Contact Us Button Test Passed")
    else:
        print("Contact Us Button Test Failed")

except Exception as e:
    print(f"An error occurred during Contact Us button testing: {e}")

finally:
    print(driver.current_url)
    driver.quit()
