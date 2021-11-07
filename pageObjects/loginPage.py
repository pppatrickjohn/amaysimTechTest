from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class loginPageUI:

    txtbox_username_xpath = "//input[@id='username']"
    txtbox_password_xpath = "//input[@id='password']"
    btn_login_xpath = "//button[@name='button' and text()='login']"
    link_logout_xpath = "//a[text()='Logout']"
    delay = 15

    def __init__(self,driver):
        self.driver = driver

    def loginAccount(self, loginCreds):
        if ";" in loginCreds:
            userPass = loginCreds.split(";")
            if len(userPass) == 2:
                print("first condition")
                if WebDriverWait(self.driver,self.delay).until(ec.presence_of_element_located((By.XPATH,self.txtbox_username_xpath))):
                    self.driver.find_element_by_xpath(self.txtbox_username_xpath).clear()
                    self.driver.find_element_by_xpath(self.txtbox_username_xpath).send_keys(userPass[0])
                    self.driver.find_element_by_xpath(self.txtbox_password_xpath).clear()
                    self.driver.find_element_by_xpath(self.txtbox_password_xpath).send_keys(userPass[1])
                    self.driver.find_element_by_xpath(self.btn_login_xpath).click()
                    if not WebDriverWait(self.driver,self.delay).until(ec.presence_of_element_located((By.XPATH,self.link_logout_xpath))):
                        return False
            else:
                return False