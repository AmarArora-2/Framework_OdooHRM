from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
print(driver.title)
try:
    driver.get("http://localhost:8069/web/login")
    time.sleep(3)

    reset_password_link = driver.find_element(By.XPATH, '//a[text()="Reset Password"]')
    reset_password_link.click()
    time.sleep(3)

    email_input = driver.find_element(By.NAME, "login")
    email_input.send_keys("amararora456.com")
    time.sleep(2)

    reset_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    reset_button.click()
    time.sleep(3)

    success_message = driver.find_element(By.XPATH, '//p[@class="alert alert-info"]').text
    expected_message = "An email has been sent with instructions to reset your password."
    if success_message == expected_message:
        print("Password Reset Test Passed")
    else:
        print("Password Reset Test Failed")

except Exception as e:
    print(f"An error occurred during password reset testing: {e}")

finally:
    print(driver.current_url)
    driver.quit()
