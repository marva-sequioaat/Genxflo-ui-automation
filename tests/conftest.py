import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
URL="https://genxflo.com"
@pytest.fixture(scope="module")
def get_driver():
    options=Options()
    options.add_argument("--headless=new")
    driver=webdriver.Chrome(options=options)
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()