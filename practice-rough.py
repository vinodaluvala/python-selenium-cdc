from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import io
from io import StringIO


import sys


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.27.0-win64\geckodriver.exe")

driver.get("https://www.cricket.com/")
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
fantasy_research_xpath = driver.find_element_by_xpath("//p[contains(text(),'Fantasy Research')]").click()
time.sleep(3)

#frctitle = driver.title
#print(frctitle)
#old_stdout = sys.stdout
#new_stdout = io.StringIO()
#sys.stdout = new_stdout

footer_xpath = driver.find_element_by_xpath("//body/div[@id='__next']/div[2]")
driver.execute_script("arguments[0].scrollIntoView();",footer_xpath)
time.sleep(5)
loc = footer_xpath.location
si = footer_xpath.size
print(loc)
print(si)

#output = new_stdout.getvalue()
#sys.stdout = old_stdout

#print(output)

driver.close()
#moreIcon = driver.find_element_by_xpath("//img[contains(@alt,'moreIcon')]")
#login = driver.find_element_by_xpath("//*[@id='__next']/nav/div/div/div[2]/div[2]/div[4]/div[2]")
#act_title = driver.title


#action = ActionChains(driver)
#action.move_to_element(moreIcon).move_to_element(login).click().perform()
#driver.close()
#time.sleep(5)
#mobileNumber = driver.find_element_by_xpath("//input[contains(@placeholder,'Mobile number')]")
#getOtp = driver.find_element_by_xpath("//div[contains(text(),'GET OTP')]")
#mobileNumber.click()
#driver.minimize_window()
#user_number = input("enter 10 digit valid mobile number")
#time.sleep(15)
#driver.maximize_window()
#mobileNumber.send_keys(user_number)
#getOtp.click()
#driver.minimize_window()
#if act_title == "Cricket Score, Match Schedule & Predictions, Latest News | Cricket.com":
#            assert True
#else:
#            assert False
#            driver.close
#user_otp = input("enter 4 digit otp number")
#time.sleep(15)
#driver.maximize_window()
#otp = driver.find_element_by_xpath("//input[@id='name2']")
#otp.send_keys(user_otp)
#button_confirm = driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[5]/div[1]")
#time.sleep(5)
#button_confirm.click()
#driver.find_element()
//*[@id="__next"]/div[2]/div/div/div[3]/div[1]
