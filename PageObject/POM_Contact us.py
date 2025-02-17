# pom.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.contact_us_button = (By.XPATH, '//a[text()="Contact Us"]')

    def click_contact_us(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.contact_us_button))
        self.driver.find_element(*self.contact_us_button).click()

class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_contact_us_page(self, expected_url):
        current_url = self.driver.current_url
        return current_url == expected_url
