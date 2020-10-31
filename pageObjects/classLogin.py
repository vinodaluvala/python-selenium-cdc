class Loginpage:

    more_icon_xpath = "//img[contains(@alt,'moreIcon')]"
    profile_xpath = "//*[@id='__next']/nav/div/div/div[2]/div[2]/div[4]/div[2]"
    mobileNumber_xpath = "//input[contains(@placeholder,'Mobile number')]"
    button_getOtp_xpath = "//div[contains(text(),'GET OTP')]"
    otp_xpath = "//input[@id='name2']"
    button_confirm_xpath = ""
    signOut_xpath = "//div[contains(text(),'SIGN OUT')]"
    button_reSend_xpath = "//b[contains(@text, RESEND)]"

    def __init__(self,driver):
        self.driver = driver

    def setMobilenumber(self, user_number):
        self.driver.find_element_by_xpath("//input[contains(@placeholder,'Mobile number')]").click()
        self.driver.find_element_by_xpath("//input[contains(@placeholder,'Mobile number')]").send_keys(user_number)

    def clickGetOtp(self):
        self.driver.find_element_by_xpath("//div[contains(text(),'GET OTP')]").click()

    def giveOTP(self, user_otp):
        self.driver.find_element_by_xpath("//div[contains(text(),'GET OTP')]").send_keys(user_otp)

    def clickConfirm(self):
        self.driver.find_element_by_xpath("").click()




