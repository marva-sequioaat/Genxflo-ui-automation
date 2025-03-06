import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

URL="https://genxflo.com"


@pytest.fixture(scope="module")
def get_driver():
    # options=Options()
    # options.add_argument("--headless=new")
    driver=webdriver.Chrome()
    #driver=webdriver.Chrome(options=options)
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()