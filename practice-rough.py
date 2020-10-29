from selenium import webdriver
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.cricket.com/")
moreIcon = driver.find_element_by_xpath("//img[contains(@alt,'moreIcon')]")
login = driver.find_element_by_xpath("//*[@id='__next']/nav/div/div/div[2]/div[2]/div[4]/div[2]")

action = ActionChains(driver)
action.move_to_element(moreIcon).move_to_element(login).click().perform()
#driver.close()
time.sleep(5)
mobileNumber = driver.find_element_by_xpath("//input[contains(@placeholder,'Mobile number')]")
getOtp = driver.find_element_by_xpath("//div[contains(text(),'GET OTP')]")
mobileNumber.click()
driver.minimize_window()
user_number = input("enter 10 digit valid mobile number")
time.sleep(15)
driver.maximize_window()
mobileNumber.send_keys(user_number)
getOtp.click()
