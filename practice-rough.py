from selenium import webdriver
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.cricket.com/")
time.sleep(3)
fantasy_research_xpath = driver.find_element_by_xpath("//p[contains(text(),'Fantasy Research')]").click()
frctitle = driver.title
print(frctitle)
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

