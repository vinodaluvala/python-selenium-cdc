import pytest
from selenium import webdriver
from pageObjects.classSanity import Sanity
from selenium.webdriver import ActionChains
import time

class Test_002_Sanity:

    baseURL = "https://www.cricket.com/"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Cricket Score, Match Schedule & Predictions, Latest News | Cricket.com":
            assert True
        else:
            assert False

    def test_FRC(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.frcClick()
        time.sleep(3)
        self.sa.frcUpcomingClick()
        time.sleep(3)
        self.sa.frcLiveClick()
        time.sleep(3)
        self.sa.frcCompletedClick()
        time.sleep(3)



        self.driver.close()

    def test_Criclytics(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.criclyticsClick()
        time.sleep(3)

        self.driver.close()

    def test_Schedule(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.scheduleClick()
        time.sleep(3)

        self.driver.close()

    def test_Series(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.seriesClick()
        time.sleep(3)

        self.driver.close()

    def test_News(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.newsClick()
        time.sleep(3)

        self.driver.close()

    def test_Players(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.newsClick()
        time.sleep(3)

        self.driver.close()

    def test_Teams(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.teamsClick()
        time.sleep(3)

        self.driver.close()

    def test_Videos(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.videosClick()
        time.sleep(3)

        self.driver.close()

    def test_MoreStadiums(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.moreStadiumsIcon(self.driver)
        time.sleep(3)

        self.driver.close()

    def test_MoreRankings(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.moreRankingsIcon(self.driver)
        time.sleep(3)

        self.driver.close()

    def test_MoreRecords(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.moreRecordsIcon(self.driver)
        time.sleep(3)

        self.driver.close()

    def test_MoreProfile(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.sa = Sanity(self.driver)
        self.sa.moreProfileIcon(self.driver)
        time.sleep(3)

        self.driver.close()