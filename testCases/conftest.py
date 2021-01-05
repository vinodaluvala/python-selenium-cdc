import pytest
from selenium import webdriver
from pageObjects import classSanity

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Drivers/chromedriver_win32/chromedriver.exe")
        print("Launching on chrome browser")
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.28.0-win32\geckodriver")
        print("Launching on firefox browser")
    return driver

def pytest_addoption(parser):      #This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")