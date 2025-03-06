import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException

"""SIGNIN TESTS"""

#test1:no user found
#test2:invalid email
#test3: Not filled inputs
#test4:Wrong Email or password


#TEST1:please enusre all the required fields are fullfilled
#test2:The input file path should start with a '/' character
#test3:The reference base path should start with a '/' character.
#test4:reference name is same as that of base path.please enTER ACTUAL REFERENCE FILE NAME

def test_main(get_driver):
    driver=get_driver
    
    page_title=driver.title
    assert page_title=="Genxflo - Nextflow Bioinformatics Pipeline Builder"

   
def test_not_filled_inputfield(get_driver):
    driver = get_driver
    wait = WebDriverWait(driver, 10)
    login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[1]/div[3]/span')))
    login.click()
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[1]/input')))
    email_input.clear()
    email_input.send_keys("marva@sequoiaat.com")
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/input')))
    password_input.clear()
    time.sleep(3)
    password_input.send_keys(Keys.TAB)
    signin = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/button/span')))
    signin.click()
    wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[5]/p').text == "Please fill all the details")
    log_element=get_driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[5]/p')
    error_message=log_element.text
    expected_message="Please fill all the details"
    assert error_message==expected_message

def test_invalid_email(get_driver):
    driver = get_driver
    wait = WebDriverWait(driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[1]/input')))
    email_input.send_keys("marva@sequoi")
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/input')))
    password_input.send_keys('marva@sequoiaat')
    signin = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/button/span')))
    signin.click()
    wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[5]/p').text == "Email is invalid")
    log_element=get_driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[5]/p')
    error_message=log_element.text
    expected_message="Email is invalid"
    assert error_message==expected_message
    

def test_wrong_password(get_driver):
    driver = get_driver
    wait = WebDriverWait(driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[1]/input')))
    email_input.clear()
    email_input.send_keys("marva@sequoiaat.com")
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/input')))
    password_input.clear()
    password_input.send_keys('marva@')
    signin = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/button/span')))
    signin.click()
    wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[5]/p').text == "Wrong Email or Password")
    log_element=get_driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[5]/p')
    error_message=log_element.text
    expected_message="Wrong Email or Password"
    assert error_message==expected_message

def test_user_not_found(get_driver):
    driver = get_driver
    wait = WebDriverWait(driver, 10)
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[1]/input')))
    email_input.clear()
    email_input.send_keys("marvafathima62@gmail.com")
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/input')))
    password_input.clear()
    password_input.send_keys('marva@')
    signin = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/button/span')))
    signin.click()
    wait.until(lambda d: d.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[5]/p').text == "User not found")
    log_element=get_driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[5]/p')
    error_message=log_element.text
    expected_message="User not found"
    assert error_message==expected_message