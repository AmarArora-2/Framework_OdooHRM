# test_case.py
import time
import pytest
from selenium import webdriver
from pom import LoginPage, HomePage, EmployeesPage


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_employee_creation(setup):
    driver = setup

    # Step 1: Login
    login_page = LoginPage(driver)
    login_page.login("a33131678@gmail.com", "ProjectOdoo118")
    print("Login attempt made")

    # Step 2: Navigate to the Home page
    home_page = HomePage(driver)
    home_page.click_home_menu()
    print("Clicked on home menu")

    # Step 3: Create an employee
    employees_page = EmployeesPage(driver)
    employees_page.create_employee("NISHU", "Manager", "Administration")
    print("Employee details filled")

    # Step 4: Verify employee creation
    employees_page.verify_employee_creation()
    print("Employee creation successful")
