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
        self.sa.frcUpcomingClick()
        time.sleep(3)
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
        if self.sa.footflag == True:
            assert True
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_FRC_foot.png")
            self.driver.close()
            assert False
        self.sa.frcLiveClick()
        time.sleep(3)
        self.sa.frcCompletedClick()
        time.sleep(3)
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