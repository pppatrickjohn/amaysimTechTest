import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(options=options,
                              executable_path=r".//Driver/chromedriver.exe")
    return driver