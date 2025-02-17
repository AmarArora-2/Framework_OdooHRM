# test_case.py
import time
import pytest
from selenium import webdriver
from pom import LoginPage, HomePage


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_module_navigation(setup):
    driver = setup

    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.login("a33131678@gmail.com", "ProjectOdoo118")
    print("Login attempt made")
    time.sleep(3)

    # Step 2: Verify Home Menu
    home_page = HomePage(driver)
    if home_page.verify_home_menu():
        print("Home menu is displayed")
    else:
        print("Home menu is not displayed")

    # Step 3: Test each module's clickability
    modules = home_page.get_modules()
    print(f"Found {len(modules)} modules in the home menu")

    for index, module in enumerate(modules):
        try:
            module_name = module.text
            print(f"Testing clickability of module: {module_name}")

            # Click the module
            home_page.click_module(module)
            time.sleep(5)

            current_page_title = driver.title
            print(f"Successfully clicked module '{module_name}'. Current page title: {current_page_title}")

            # Go back to home page
            driver.get("http://localhost:8069/web")
            time.sleep(5)

        except Exception as e:
            print(f"Could not click on module {module_name}: {e}")

