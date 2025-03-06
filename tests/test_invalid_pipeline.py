import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""Test case to verify the web page is loaded successfully"""
@pytest.mark.dependency()
def test_main(get_driver):
    driver=get_driver
    page_title=driver.title
    assert page_title=="Genxflo - Nextflow Bioinformatics Pipeline Builder"


"""Test case to verify the error message when a required field is kept empty"""
@pytest.mark.dependency(depends=["test_main"])
def test_empty_field_error(get_driver):
    driver = get_driver
    wait = WebDriverWait(driver, 10)
    
    login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[1]/div[3]/span')))
    login.click()
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[1]/input')))
    email_input.send_keys("marva@sequoiaat.com")
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[2]/div[2]/input')))
    password_input.send_keys('marva@sequoiaat')
    signin = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div/div[2]/button/span')))
    signin.click()
    pipeline_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div')))
    pipeline_button.click()
    pipeline_name=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/input')
    pipeline_name.send_keys(Keys.TAB)
    pipeline_description=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[3]/textarea')
    pipeline_description.send_keys(Keys.TAB)
    input_folder=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[4]/input')
    input_folder.send_keys("/home/marva/Projects/practice/bioinfo-pipeline1/output/SRR32313969_1.fastq")
    output_folder=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[5]/input')
    output_folder.send_keys("/output")
    reference_folder=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[6]/input')
    reference_folder.send_keys("/reference")
    time.sleep(5)
    reference_folder1=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[7]/div/input')
    reference_folder1.send_keys("/reference2")
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[8]/button[2]')
    next_button.click()
    error_message=driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div/div[2]/span')
    assert error_message.text=="Please ensure all required fields are completed before proceeding."


"""Test case to verify the error message when a reference path and base path are same"""
@pytest.mark.dependency(depends=["test_empty_field_error"])
def test_reference_path_error(get_driver):
    driver=get_driver
    reset_button=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[8]/button[1]')
    reset_button.click()
    pipeline_name=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/input')
    
    pipeline_name.send_keys("sample pipeline")
    pipeline_description=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[3]/textarea')
   
    pipeline_description.send_keys("pipeline description")
    input_folder=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[4]/input')
   
    input_folder.send_keys("/home/marva/Projects/practice/bioinfo-pipeline1/output/SRR32313969_1.fastq")
    output_folder=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[5]/input')
    output_folder.send_keys("/output")
    reference_folder=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[6]/input')
    reference_folder.send_keys("/reference")
    time.sleep(2)
    reference_folder1=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[7]/div/input')
    reference_folder1.clear()
    reference_folder1.send_keys("/reference")
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[8]/button[2]')
    next_button.click()
    error=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div/div[1]/div/div[2]/span')))
    assert error.text=="Reference file name is same as that of base path. Please enter actual reference filename"


"""Test case to verify the error message when invalid input file path is provided"""
@pytest.mark.dependency(depends=["test_empty_field_error"])
def test_input_path_error(get_driver):
    driver=get_driver
    reset_button=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[8]/button[1]')
    reset_button.click()
    pipeline_name=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/input')
    
    pipeline_name.send_keys("sample pipeline")
    pipeline_description=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[3]/textarea')
   
    pipeline_description.send_keys("pipeline description")
    input_folder=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[4]/input')
   #invalid input
    input_folder.send_keys("home")
    output_folder=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[5]/input')
    output_folder.send_keys("/output")
    reference_folder=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[6]/input')
    reference_folder.send_keys("/reference")
    time.sleep(2)
    reference_folder1=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[7]/div/input')
    reference_folder1.send_keys("/reference2")
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[8]/button[2]')
    next_button.click()
    input_path_error=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div/div[2]/div[4]/div[2]')))
    
    assert input_path_error.text=="The input file path should start with a '/' character."

"""Test case to verify the error message when invalid output file path is provided"""
@pytest.mark.dependency(depends=["test_empty_field_error"])
def test_output_path_error(get_driver):
    driver=get_driver
    reset_button=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[8]/button[1]')
    reset_button.click()
    pipeline_name=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/input')
    
    pipeline_name.send_keys("sample pipeline")
    pipeline_description=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[3]/textarea')
   
    pipeline_description.send_keys("pipeline description")
    input_folder=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[4]/input')
  
    input_folder.send_keys("/home")
    output_folder=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[5]/input')
    #invalid output
    output_folder.send_keys("output")
    reference_folder=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[6]/input')
    reference_folder.send_keys("/reference")
    time.sleep(2)
    reference_folder1=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[7]/div/input')
    reference_folder1.send_keys("/reference2")
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[8]/button[2]')
    next_button.click()
    output_path_error=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div/div[2]/div[5]/div[2]')))
    assert output_path_error.text=="The input file path should start with a '/' character."





