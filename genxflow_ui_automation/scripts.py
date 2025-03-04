from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def setup_driver_method2():
   
    
    # Make sure webdriver_manager is installed: pip install webdriver-manager
    service = Service(ChromeDriverManager().install())
    options = Options()
    
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# driver = webdriver.Chrome()
driver=setup_driver_method2()
wait=WebDriverWait(driver,10)
try:
    driver.get("https://genxflo.com")
    wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
    driver.maximize_window()
    
    locators = [
    (By.XPATH, '//*[@id="root"]/div/div/div[1]/div[3]/span'),
  
]
    try:
        login = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div/div[1]/div[3]/span'))
        )
      
        driver.execute_script("arguments[0].click();", login)
        print(f"Successfully clicked using locator")
        time.sleep(5)
        email_input=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/input')
        email_input.send_keys("marva@sequoiaat.com")
        print("EMAIL ENETERD")
        password_input=driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/input')
        password_input.send_keys('marva@sequoiaat')
        print("password entered")
        signin=wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div/div/div[2]/button/span')))
        signin.click()
       
        print("successfully clicked signin")
        time.sleep(3)
    except Exception as e:
        print(f"Failed with locator : {str(e)}")
    try:        
        create_pipeline=wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div')))
        create_pipeline.click()
        print("pipeline clicked successfully")
        time.sleep(3)
    except Exception as e:
        print(f"error occured while creating pipeline:{str(e)}")


except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    driver.quit()
        
 
