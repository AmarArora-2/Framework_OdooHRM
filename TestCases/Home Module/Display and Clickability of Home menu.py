import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
try:
    driver.get("http://localhost:8069/web/login")
    time.sleep(3)

    email_input = driver.find_element(By.NAME, "login")
    email_input.send_keys("a33131678@gmail.com")
    time.sleep(2)

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("ProjectOdoo118")
    time.sleep(2)

    login_button = driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]')
    login_button.click()
    time.sleep(5)

    home_menu = driver.find_element(By.XPATH, '//i[@class="oi oi-apps"]')
    if home_menu.is_displayed():
        print("Home menu is displayed")
    else:
        print("Home menu is not displayed")


    modules = driver.find_elements(By.XPATH, '//a[@role="menuitem"]')
    print(f"Found {len(modules)} modules in the home menu")

    for index, module in enumerate(modules):
        try:
            module_name = module.text
            print(f"Testing clickability of module: {module_name}")

            actions = ActionChains(driver)
            actions.move_to_element(module).click().perform()
            time.sleep(5)

            current_page_title = driver.title
            print(f"Successfully clicked module '{module_name}'. Current page title: {current_page_title}")

            driver.get("http://localhost:8069/web")
            time.sleep(5)

        except Exception as e:
            print(f"Could not click on module {module_name}: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
