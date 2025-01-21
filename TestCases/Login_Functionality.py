# Valid Credentials:
# 1. a33131678@gmail.com, ProjectOdoo118
# 2. amararora456@gmail.com, ProjectOddo118

# Invalid Credentials:
# 1. invalid@example.com, wrongpass
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
print(driver.title)

driver.get("http://localhost:8069/web/login")
time.sleep(5)

textbox1 = driver.find_element(By.NAME, "login")
textbox1.send_keys("a33131678@gmail.com")
time.sleep(2)

textbox2 = driver.find_element(By.NAME, "password")
textbox2.send_keys("ProjectOdoo118")
time.sleep(2)

click = driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]')
click.click()
time.sleep(2)
assert driver.title == "Inbox"



