from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class homePageUI:

    link_simPlans_xpath = "//a[@aria-label='SIM plans']"
    link_activateSim_xpath = "//a[@aria-label='Activate SIM']"
    link_help_xpath = "//a[@aria-label='Help']"
    link_account_xpath = "//a[@aria-label='Account']"
    delay = 120

    def __init__(self,driver):
        self.driver = driver

    def selectMenuOption(self,menuToSelect):
        if menuToSelect != "":
            if (menuToSelect.strip()).upper() == "SIM PLANS":
                if WebDriverWait(self.driver,self.delay).until(ec.presence_of_element_located((By.XPATH,self.link_simPlans_xpath))):
                    self.driver.find_element_by_xpath(self.link_simPlans_xpath).click()
            if (menuToSelect.strip()).upper() == "ACTIVATE SIM":
                if WebDriverWait(self.driver,self.delay).until(ec.presence_of_element_located((By.XPATH,self.link_activateSim_xpath))):
                    self.driver.find_element_by_xpath(self.link_activateSim_xpath).click()
            if (menuToSelect.strip()).upper() == "HELP":
                if WebDriverWait(self.driver,self.delay).until(ec.presence_of_element_located((By.XPATH,self.link_help_xpath))):
                    self.driver.find_element_by_xpath(self.link_help_xpath).click()
            if (menuToSelect.strip()).upper() == "ACCOUNT":
                if WebDriverWait(self.driver,self.delay).until(ec.presence_of_element_located((By.XPATH,self.link_account_xpath))):
                    self.driver.find_element_by_xpath(self.link_account_xpath).click()
        else:
            return False