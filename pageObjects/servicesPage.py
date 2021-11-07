from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class servicesPageUI:

    link_managePlan_xpath = "//a[text()='Manage plan']"
    link_activateSIM_xpath = "//a[text()='Activate now']"
    div_addService_xpath = "//div[@id='add_service_icon_mobile']"
    delay = 120

    def __init__(self, driver):
        self.driver = driver

    def selectAddServices(self, serviceAction):
        if serviceAction != "":
            if (serviceAction.strip()).upper() == "MANAGE PLAN":
                if WebDriverWait(self.driver, self.delay).until(ec.presence_of_element_located((By.XPATH, self.link_managePlan_xpath))):
                    self.driver.find_element_by_xpath(self.link_managePlan_xpath).click()
            if (serviceAction.strip()).upper() == "ADD SERVICE":
                if WebDriverWait(self.driver, self.delay).until(ec.presence_of_element_located((By.XPATH, self.div_addService_xpath))):
                    self.driver.find_element_by_xpath(self.div_addService_xpath).click()
            if (serviceAction.strip()).upper() == "ACTIVATE SIM":
                if WebDriverWait(self.driver, self.delay).until(ec.presence_of_element_located((By.XPATH, self.link_activateSIM_xpath))):
                    self.driver.find_element_by_xpath(self.link_activateSIM_xpath).click()
        else:
            return False

