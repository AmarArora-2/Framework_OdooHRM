import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(5)
try:
    driver.get("http://localhost:8069/web/login")
    print("Navigated to login page")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
    driver.find_element(By.NAME, "login").send_keys("a33131678@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("ProjectOdoo118")
    driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()
    print("Login attempt made")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//i[@class="oi oi-apps"]')))
    home_menu = driver.find_element(By.XPATH, '//i[@class="oi oi-apps"]')

    if home_menu.is_displayed():
        print("Home menu is displayed")
    else:
        raise Exception("Home menu is not displayed")

    home_menu.click()
    print("Clicked on home menu")
    time.sleep(3)

    employees_module = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(@data-menu-xmlid, 'hr.menu_hr_root')]"))
    )
    time.sleep(5)
    employees_module.click()
    print("Clicked on Employees module")
    time.sleep(3)

    new_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="btn btn-primary o-kanban-button-new"]'))
    )
    time.sleep(5)
    new_button.click()
    print("Clicked on 'Create' button")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name_0"]'))).send_keys(
        "NISHU")
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="job_title_0"]').send_keys("Manager")
    driver.find_element(By.XPATH, '//*[@id="department_id_0"]').send_keys("Administration", Keys.ENTER)
    print("Filled in employee details")

    save_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div[3]/div/button[1]/i')
    save_button.click()
    time.sleep(5)
    print("Clicked on 'Save' button")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'John Doe')]")))
    print("Employee creation successful")
    time.sleep(5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
