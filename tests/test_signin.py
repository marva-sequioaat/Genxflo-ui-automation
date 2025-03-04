import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By

def test_main(get_driver):
    driver=get_driver
    
    page_title=driver.title
    assert page_title=="Genxflo - Nextflow Bioinformatics Pipeline Builder"


def test_login(get_driver):
    driver=get_driver
    wait=WebDriverWait(driver,10) 
   
    try:
        # login = wait.until(
        #     EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[1]/div[3]/span'))
        # )
    
        # driver.execute_script("arguments[0].click();", login)
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
        # signin=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div/div[2]/button/span')))
        signin=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/button/span')
        signin.click()
        time.sleep(5)
        pipeline_button=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div')
        assert pipeline_button
        # print("successfully clicked signin")
        # time.sleep(3)
    except Exception as e:
        print(f"Failed with locator : {str(e)}")
        raise
    #     try:        
    #         create_pipeline=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div')))
    #         create_pipeline.click()
    #         print("pipeline clicked successfully")
    #         time.sleep(3)
    #     except Exception as e:
    #         print(f"error occured while creating pipeline:{str(e)}")


    # except Exception as e:
    #     print(f"An error occurred: {str(e)}")
    # finally:
    #     driver.quit()
            
