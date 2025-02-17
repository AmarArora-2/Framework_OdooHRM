# pom.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.login_field = (By.NAME, "login")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, '//*[@class="btn btn-primary"]')

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login_field))
        self.driver.find_element(*self.login_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.home_menu = (By.XPATH, '//i[@class="oi oi-apps"]')

    def click_home_menu(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.home_menu))
        self.driver.find_element(*self.home_menu).click()

class EmployeesPage:
    def __init__(self, driver):
        self.driver = driver
        self.employees_module = (By.XPATH, "//*[contains(@data-menu-xmlid, 'hr.menu_hr_root')]")
        self.new_button = (By.XPATH, '//*[@class="btn btn-primary o-kanban-button-new"]')
        self.name_field = (By.XPATH, '//*[@id="name_0"]')
        self.job_title_field = (By.XPATH, '//*[@id="job_title_0"]')
        self.department_field = (By.XPATH, '//*[@id="department_id_0"]')
        self.save_button = (By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div[3]/div/button[1]/i')
        self.success_message = (By.XPATH, "//*[contains(text(), 'John Doe')]")

    def create_employee(self, name, job_title, department):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.employees_module)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.new_button)).click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.name_field)).send_keys(name)
        self.driver.find_element(*self.job_title_field).send_keys(job_title)
        self.driver.find_element(*self.department_field).send_keys(department, Keys.ENTER)
        self.driver.find_element(*self.save_button).click()

    def verify_employee_creation(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.success_message))
