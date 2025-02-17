
import time
import pytest
from selenium import webdriver
from pom import LoginPage, ContactUsPage


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_contact_us_button(setup):
    driver = setup

    try:
        # Step 1: Navigate to the login page
        driver.get("http://localhost:8069/web/login")
        time.sleep(3)

        # Step 2: Click on the "Contact Us" button
        login_page = LoginPage(driver)
        login_page.click_contact_us()
        time.sleep(3)

        # Step 3: Verify the "Contact Us" page URL
        contact_us_page = ContactUsPage(driver)
        expected_url = "http://localhost:8069/contactus"  # Replace with the actual Contact Us URL
        if contact_us_page.verify_contact_us_page(expected_url):
            print("Contact Us Button Test Passed")
        else:
            print("Contact Us Button Test Failed")

    except Exception as e:
        print(f"An error occurred during Contact Us button testing: {e}")

    finally:
        print(driver.current_url)
