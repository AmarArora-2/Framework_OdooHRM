import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.severity(allure.severity_level.MINOR)
@allure.feature("login")



class TestCase:
    @pytest.mark.parametrize("username,password,exp",[("www","www","Invalid login, please try again"),("ssss","11111","Invalid login"),("satwinder@123","Satwinder@123","Satwinder Singh")])
    def test_loging(self,username,password,exp):
        driver=webdriver.Chrome()
        driver.get("https://online.btes.co.in/login/index.php")
        driver.find_element(By.XPATH,"//input[@id='username']").send_keys(username)
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys(password)
        driver.find_element(By.XPATH,"//button[@id='loginbtn']").click()
        try:
            if exp == "Satwinder Singh":
                act = driver.find_element(By.XPATH, "//*[@class='usertext mr-1']").text
            else:
                act = driver.find_element(By.XPATH, "//a[text()='Invalid login, please try again']").text
            assert act==exp
        except:
            allure.attach(driver.get_screenshot_as_png(), name="testlogin",attachment_type=AttachmentType.PNG)
            assert False