from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

class settingsPageUI:

    lbl_callForwarding_xpath = "//div[text()='Call forwarding']"
    link_callForwardingEdit_xpath = "//a[@id='edit_settings_call_forwarding']"
    lbl_callForwardingYes_xpath = "//div[@id='settings_call_forwarding']//following::div[text()='Yes']"
    link_confirm_xpath = "//a[text()='Confirm']"
    chkbox_callForwaringNo_xpath = "//input[@id='my_amaysim2_setting_call_divert_false']"
    chkbox_callForwaringYes_xpath = "//input[@id='my_amaysim2_setting_call_divert_true']"
    txtbox_forwardCallsTo_xpath = "//input[@id='my_amaysim2_setting_call_divert_number']"
    btn_callForwardingSave_xpath = "//input[@name='commit' and @value='Save']"
    img_loadingHide_xpath = "//div[@id='ajax_loading' and @style='display: none;']"
    lbl_invalidCharacter_xpath = "//span[text()='Please enter your phone number in the following format: 0412 345 678 or 02 1234 5678']"
    lbl_updateSuccess_xpath = "//*[contains(text(), 'Success')]"
    span_closeSuccess_xpath = "//div[@class='form_info_popup reveal-modal padding-none open']//following::a[@class='close-reveal-modal']"
    link_logout_xpath = "//a[@id='logout-link']"
    delay = 120

    def __init__(self, driver):
        self.driver = driver

    def dashboardMenu(self,selectedMenu):
        if selectedMenu != "":
            if WebDriverWait(self.driver, self.delay).until(ec.presence_of_element_located((By.XPATH, "//ul[@id='menu_list']//following::a[@href='/my-account/my-amaysim/" + selectedMenu.lower() + "']"))):
                self.driver.find_element_by_xpath("//ul[@id='menu_list']//following::a[@href='/my-account/my-amaysim/" + selectedMenu.lower() + "']").click()
        else:
            return False

    def callForwading(self,editCallFrwrdng):
        if ";" not in editCallFrwrdng:
            newEditCallForwarding = editCallFrwrdng + ";"
        else:
            newEditCallForwarding = editCallFrwrdng

        updateCallForwarding = newEditCallForwarding.split(";")

        if (updateCallForwarding[0].strip()).upper() == "NO":
            if WebDriverWait(self.driver, self.delay).until(ec.presence_of_element_located((By.XPATH,self.lbl_callForwarding_xpath))):
                currentVal = self.driver.find_element_by_xpath(self.lbl_callForwardingYes_xpath)
                if currentVal == True:
                    self.driver.find_element_by_xpath(self.link_callForwardingEdit_xpath).click()
                    if WebDriverWait(self.driver, self.delay).until(ec.presence_of_element_located((By.XPATH,self.link_confirm_xpath))):
                        self.driver.find_element_by_xpath(self.link_confirm_xpath).click()
                        self.driver.find_element_by_xpath(self.chkbox_callForwaringNo_xpath).click()
                else:
                    return True
        elif (updateCallForwarding[0].strip()).upper() == "YES":
            if WebDriverWait(self.driver, self.delay).until(ec.presence_of_element_located((By.XPATH,self.lbl_callForwarding_xpath))):
                self.driver.find_element_by_xpath(self.link_callForwardingEdit_xpath).click()
                if updateCallForwarding[1] != "":
                    if WebDriverWait(self.driver, self.delay).until(ec.presence_of_element_located((By.XPATH,self.link_confirm_xpath))):
                        self.driver.find_element_by_xpath(self.link_confirm_xpath).click()
                        currentVal = self.driver.find_element_by_xpath(self.chkbox_callForwaringYes_xpath)

                        if currentVal.get_attribute("value") != "true":
                            self.driver.find_element_by_xpath(self.chkbox_callForwaringYes_xpath).click()

                        self.driver.find_element_by_xpath(self.txtbox_forwardCallsTo_xpath).clear()
                        self.driver.find_element_by_xpath(self.txtbox_forwardCallsTo_xpath).send_keys(updateCallForwarding[1])
                        self.driver.find_element_by_xpath(self.btn_callForwardingSave_xpath).click()

                        if WebDriverWait(self.driver, self.delay).until(ec.presence_of_element_located((By.XPATH,self.img_loadingHide_xpath))):
                            time.sleep(2)
                            self.driver.find_element_by_xpath(self.span_closeSuccess_xpath).click()
        else:
            return False

    def logoutAccount(self):
        if WebDriverWait(self.driver, self.delay).until(ec.presence_of_element_located((By.XPATH,self.link_logout_xpath))):
            self.driver.find_element_by_xpath(self.link_logout_xpath).click()