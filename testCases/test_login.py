import pytest
from selenium import webdriver
from pageObjects.classLogin import Loginpage
from selenium.webdriver import ActionChains
import time

class Test_001_Login:

    baseURL = "https://www.cricket.com/"
    user_number = "9494645182"

    def test_homePageTitle(self):
        self.driver = webdriver.Chrome(executable_path="C:/Drivers/chromedriver_win32/chromedriver.exe")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Cricket Score, Match Schedule & Predictions, Latest News | Cricket.com":
            assert True
        else:
            assert False

    def test_Login(self):
        self.driver = webdriver.Chrome(executable_path="C:/Drivers/chromedriver_win32/chromedriver.exe")
        self.driver.get(self.baseURL)
        self.lp = Loginpage(self.driver)
        self.lp.more_Icon(self.driver)
        time.sleep(5)
        self.lp.setMobilenumber(self.user_number)
        self.lp.clickGetOtp()
        self.driver.minimize_window()
        self.user_otp = input("enter 4 digit otp number")
        time.sleep(15)
        self.driver.maximize_window()
        self.lp.giveOTP(self.user_otp)
        time.sleep(5)
        self.lp.clickConfirm()
        time.sleep(8)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Cricket Score, Match Schedule & Predictions, Latest News | Cricket.com":
            assert True
        else:
            assert False



