import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCase:
    driver=webdriver.Chrome()
    driver.get("http://localhost:8069/web/login")
    driver.find_element(By.NAME, "login").send_keys("a33131678@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("ProjectOdoo118")
    driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()
    act=driver.find_element(By.XPATH,'/html/body/header/nav/a')
    exp = "Discuss"
    assert act==exp
