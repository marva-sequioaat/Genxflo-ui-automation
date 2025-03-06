import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
from dotenv import load_dotenv
URL="https://genxflo.com"

load_dotenv()

def get_env(*variables):
    return tuple([os.getenv(i) for i in variables])

@pytest.fixture(scope="module")
def get_driver():
    options=Options()
    options.add_argument("--headless=new")
    # driver=webdriver.Chrome()
    driver=webdriver.Chrome(options=options)
    driver.get(URL)
    driver.maximize_window()
    yield driver
    driver.quit()
   
@pytest.fixture()
def get_credentials():
    email,password=get_env("EMAIL","PASSWORD")
    return {"email":email,"password":password}
