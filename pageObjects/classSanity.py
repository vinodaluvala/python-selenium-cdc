from selenium.webdriver import ActionChains
import time
from utilities.readProperties import Readconfig

class Sanity:

    fantasy_research_xpath = "//p[contains(text(),'Fantasy Research')]"
    criclytics_xpath = "//p[contains(text(),'Criclytics')]"
    schedule_xpath = "//p[contains(text(),'Schedule')]"
    series_xpath = "//p[contains(text(),'Series')]"
    news_xpath = "//p[contains(text(),'News')]"
    players_xpath = "//p[contains(text(),'Players')]"
    teams_xpath = "//p[contains(text(),'Teams')]"
    videos_xpath = "//p[contains(text(),'Videos')]"
    more_icon_xpath = "//img[contains(@alt,'moreIcon')]"
    stadiums_xpath = "//div[contains(text(),'Stadiums')]"
    rankings_xpath = "//div[contains(text(),'Rankings')]"
    records_xpath = "//div[contains(text(),'Records')]"
    profile_xpath = "//*[@id='__next']/nav/div/div/div[2]/div[2]/div[4]/div[2]"
    frc_upcoming_xpath = "//div[contains(text(),'UPCOMING')]"
    frc_live_xpath = "//div[contains(text(),'LIVE')]"
    frc_completed_xpath = "//div[contains(text(),'COMPLETED')]"
    frc_upcoming_match_xpath = "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]"
    frc_live_match_xpath = "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[4]/div[1]"
    frc_completed_match_xpath = "//body/div[@id='__next']/div[1]/div[1]/div[1]/div[4]/div[1]"
    fantasy_previews_xpath = "//span[contains(text(),'FANTASY PREVIEWS')]"
    fantasy_videos_xpath = "//div[contains(text(),'FANTASY VIDEOS')]"
    footer_xpath = "//body/div[@id='__next']/div[2]"

    def __init__(self, driver):
        self.driver = driver

    def frcClick(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'Fantasy Research')]").click()

    def frcUpcomingClick(self):
        self.driver.find_element_by_xpath("//div[contains(text(),'UPCOMING')]").click()

    def frcUpcomingCheck(self):
        self.driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]").is_displayed()


    def frcLiveCheck(self):
        self.driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[1]/div[1]/div[4]/div[1]").is_displayed()

    def frcCompletedCheck(self):
        self.driver.find_element_by_xpath("//body/div[@id='__next']/div[1]/div[1]/div[1]/div[4]/div[1]").is_displayed()

    def frcLiveClick(self):
        self.driver.find_element_by_xpath("//div[contains(text(),'LIVE')]").click()

    def frcCompletedClick(self):
        self.driver.find_element_by_xpath("//div[contains(text(),'COMPLETED')]").click()

    def frcFantasyPreviews(self):
        self.driver.find_elements_by_xpath("//span[contains(text(),'FANTASY PREVIEWS')]")
        p = len(self.fantasy_previews_xpath)
        if (p > 0):
            self.flag = True
            return self.flag
        else:
            self.flag = False
            return self.flag

    def frcFantasyVideos(self):
        self.driver.find_elements_by_xpath("//div[contains(text(),'FANTASY VIDEOS')]")
        v = len(self.fantasy_videos_xpath)
        if (v > 0):
            self.flag = True
            return self.flag
        else:
            self.flag = False
            return self.flag

    def criclyticsClick(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'Criclytics')]").click()

    def scheduleClick(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'Schedule')]").click()

    def seriesClick(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'Series')]").click()

    def newsClick(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'News')]").click()

    def playersClick(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'Players')]").click()

    def teamsClick(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'Teams')]").click()

    def videosClick(self):
        self.driver.find_element_by_xpath("//p[contains(text(),'Videos')]").click()

    def moreStadiumsIcon(self, driver):
        self.action = ActionChains(driver)
        self.more_icon_xpath = driver.find_element_by_xpath("//img[contains(@alt,'moreIcon')]")
        self.stadiums_xpath = driver.find_element_by_xpath("//div[contains(text(),'Stadiums')]")
        self.action.move_to_element(self.more_icon_xpath).move_to_element(self.stadiums_xpath).click().perform()

    def moreRankingsIcon(self, driver):
        self.action = ActionChains(driver)
        self.more_icon_xpath = driver.find_element_by_xpath("//img[contains(@alt,'moreIcon')]")
        self.rankings_xpath = driver.find_element_by_xpath("//div[contains(text(),'Rankings')]")
        self.action.move_to_element(self.more_icon_xpath).move_to_element(self.rankings_xpath).click().perform()

    def moreRecordsIcon(self, driver):
        self.action = ActionChains(driver)
        self.more_icon_xpath = driver.find_element_by_xpath("//img[contains(@alt,'moreIcon')]")
        self.records_xpath = driver.find_element_by_xpath("//div[contains(text(),'Records')]")
        self.action.move_to_element(self.more_icon_xpath).move_to_element(self.records_xpath).click().perform()

    def moreProfileIcon(self, driver):
        self.action = ActionChains(driver)
        self.more_icon_xpath = driver.find_element_by_xpath("//img[contains(@alt,'moreIcon')]")
        self.profile_xpath = driver.find_element_by_xpath("//*[@id='__next']/nav/div/div/div[2]/div[2]/div[4]/div[2]")
        self.action.move_to_element(self.more_icon_xpath).move_to_element(self.profile_xpath).click().perform()

    def dimensionFooter(self):
        footer_xpath = self.driver.find_element_by_xpath("//body/div[@id='__next']/div[2]")

        #self.footerLocation = Readconfig.getfooterLocation()
        self.footerSize = Readconfig.getfooterSize()
        if footer_xpath.size == self.footerSize:
            self.footflag = True
            return self.footflag
        else:
            self.footflag = False
            return self.footflag




