@echo off
pytest -v -s --alluredir="report" allureReport.py
allure serve "D:\BEBO-tech\Selenium\Selenium\framwork\allureReports\first\report"
pause