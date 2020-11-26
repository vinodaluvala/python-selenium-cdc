import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path="C:/Drivers/chromedriver_win32/chromedriver.exe")
    return driver