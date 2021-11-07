import pytest
from selenium import webdriver
from pageObjects.homePage import homePageUI
from pageObjects.loginPage import loginPageUI
from pageObjects.servicesPage import servicesPageUI
from pageObjects.settingsPage import settingsPageUI
from utils.readProperties import readConfig

class Test_amaysim():
    baseURL = readConfig.getApplicationURL()

    def test_amaysimModifyPlan(self,setup):
        list_Res = []
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.home = homePageUI(self.driver)
        self.login = loginPageUI(self.driver)
        self.service = servicesPageUI(self.driver)
        self.settings = settingsPageUI(self.driver)
        self.home.selectMenuOption("Account")
        self.login.loginAccount("0481862258;theHoff34")
        self.service.selectAddServices("Manage Plan")
        self.settings.dashboardMenu("Settings")
        self.settings.callForwading("Yes;0251018758")
        self.settings.logoutAccount()
        self.driver.close()