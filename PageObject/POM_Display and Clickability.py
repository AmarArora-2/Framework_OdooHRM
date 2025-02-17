# pom.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.NAME, "login")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, '//*[@class="btn btn-primary"]')

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.email_input))
        self.driver.find_element(*self.email_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.home_menu = (By.XPATH, '//i[@class="oi oi-apps"]')
        self.modules = (By.XPATH, '//a[@role="menuitem"]')

    def verify_home_menu(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.home_menu))
        return self.driver.find_element(*self.home_menu).is_displayed()

    def get_modules(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.modules))
        return self.driver.find_elements(*self.modules)

    def click_module(self, module):
        actions = ActionChains(self.driver)
        actions.move_to_element(module).click().perform()
