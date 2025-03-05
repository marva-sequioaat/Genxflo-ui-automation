import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

def test_main(get_driver):
    driver=get_driver
    
    page_title=driver.title
    assert page_title=="Genxflo - Nextflow Bioinformatics Pipeline Builder"

@pytest.mark.dependency()
def test_login(get_driver):
    driver=get_driver
    wait=WebDriverWait(driver,10) 
    
    try:
       
        login=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[1]/div[3]/span')
        login.click()
        print(f"Successfully clicked using locator")
        time.sleep(5)
        email_input=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/input')
        email_input.send_keys("marva@sequoiaat.com")
        print("EMAIL ENETERD")
        password_input=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/input')
        password_input.send_keys('marva@sequoiaat')
        print("password entered")
        signin=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/button/span')
        signin.click()
        time.sleep(10)
        pipeline_button=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div')
        assert pipeline_button
    except Exception as e:
        print(f"Failed with locator : {str(e)}")
        raise
@pytest.mark.dependency(depends=["test_login"])
def test_pipeline_form_creation(get_driver):
    driver=get_driver
    # pipeline_button=driver.find_element(By.XPATH,'/html/body/div/div/div/div[3]/div[1]/div')
    # if pipeline_button is None:
    pipeline_button=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div')
    pipeline_button.click()
    
    print("pipeline button clicked")
    time.sleep(5)
    print("sleep")
    pipeline_name=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/input')
    
    pipeline_name.send_keys("PIPELINE-ONE")
    pipeline_description=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[3]/textarea')
    pipeline_description.send_keys("This is a sample pipeline build to test genxflo ui")
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
    time.sleep(5)
    pipeline_start_button=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div[1]')
    
    assert pipeline_start_button


@pytest.mark.dependency(depends=["test_pipeline_form_creation"])
def test_pipeline_creation(get_driver):
    fastp_button=get_driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div/div[1]/div[4]/div[1]/button')
    fastp_button.click()
    time.sleep(3)
    #fastp_add_button=get_driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/button[2]')
    fastp_add_button=WebDriverWait(get_driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/button[2]')))
    fastp_add_button.click()
    view=get_driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/button[3]')
    view.click()

    drag=WebDriverWait(get_driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div[2]/div[1]')))
    #drag=WebDriverWait(get_driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,'react-flow__handle react-flow__handle-left nodrag nopan target connectable connectablestart connectableend connecting connectionindicator')))
    drop=WebDriverWait(get_driver,20).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/div[1]/div[2]')))
    #drop=WebDriverWait(get_driver,20).until(EC.element_to_be_clickable((By.CLASS_NAME,'react-flow__handle react-flow__handle-right nodrag nopan source connectable connectablestart connectableend connecting connectionindicator')))
  
    actions=ActionChains(get_driver)
    actions.drag_and_drop(drag,drop).perform()
    submit_button=get_driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div[3]/div/button[2]')
    submit_button.click()
    time.sleep(3)
    modal=get_driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div')
    assert modal,'Element is not displayed on the page'
