import pytest
from selenium import webdriver
from pageObjects.classSanity import Sanity
from selenium.webdriver import ActionChains
import time
from utilities.readProperties import Readconfig


class Test_002_Sanity:

    baseURL = Readconfig.getappURL()
    footerLocation = Readconfig.getfooterLocation()
    footerSize = Readconfig.getfooterSize()



    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Cricket Score, Match Schedule & Predictions, Latest News | Cricket.com":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots")
            assert False

    def test_FRC(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.frcClick()
        time.sleep(3)

        self.sa.frcUpcomingClick()              # to verify the FRC upcoming elements
        time.sleep(5)
        self.footer_xpath3 = self.driver.find_element_by_xpath("//body/div[@id='__next']/div[2]")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.footer_xpath3)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
        time.sleep(5)

        self.sa.frcFantasyPreviews()
        if self.sa.flag == True:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_FRC_Pre.png")
            self.driver.close()
            assert False

        self.sa.frcFantasyVideos()
        if self.sa.flag == True:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_FRC_Vids.png")
            self.driver.close()
            assert False

        self.sa.dimensionFooter()
        if self.sa.flag == True:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_FRC_foot.png")
            self.driver.close()
            assert False

        self.sa.frcLiveClick()        # to verify the FRC Live elements
        time.sleep(3)
        self.footer_xpath1 = self.driver.find_element_by_xpath("//body/div[@id='__next']/div[2]")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.footer_xpath1)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
        time.sleep(5)

        self.sa.frcCompletedClick()         # to verify the FRC completed elements
        time.sleep(5)
        self.footer_xpath2 = self.driver.find_element_by_xpath("//body/div[@id='__next']/div[2]")
        self.driver.execute_script("arguments[0].scrollIntoView();", self.footer_xpath2)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0,-document.body.scrollHeight)")
        time.sleep(5)
        self.driver.close()

    @pytest.mark.skip
    def test_Criclytics(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.criclyticsClick()
        time.sleep(3)

        self.driver.close()

    @pytest.mark.skip
    def test_Schedule(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.scheduleClick()
        time.sleep(3)

        self.driver.close()

    @pytest.mark.skip
    def test_Series(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.seriesClick()
        time.sleep(3)

        self.driver.close()

    @pytest.mark.skip
    def test_News(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.newsClick()
        time.sleep(3)

        self.driver.close()

    @pytest.mark.skip
    def test_Players(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.newsClick()
        time.sleep(3)

        self.driver.close()

    @pytest.mark.skip
    def test_Teams(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.teamsClick()
        time.sleep(3)

        self.driver.close()

    @pytest.mark.skip
    def test_Videos(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.videosClick()
        time.sleep(3)

        self.driver.close()

    @pytest.mark.skip
    def test_MoreStadiums(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.moreStadiumsIcon(self.driver)
        time.sleep(3)

        self.driver.close()

    @pytest.mark.skip
    def test_MoreRankings(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.moreRankingsIcon(self.driver)
        time.sleep(3)

        self.driver.close()

    @pytest.mark.skip
    def test_MoreRecords(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.moreRecordsIcon(self.driver)
        time.sleep(3)

        self.driver.close()

    @pytest.mark.skip
    def test_MoreProfile(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.moreProfileIcon(self.driver)
        time.sleep(3)

        self.driver.close()