from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
driver.implicitly_wait(5)
try:
    notAcceptButton = driver.find_element(By.CLASS_NAME, 'at-cm-no-button')
    notAcceptButton.click()
except:
    print('No element with this class name. Skipping...')

firstInputElement = driver.find_element(By.ID, 'sum1')
secondInputElement = driver.find_element(By.ID, 'sum2')

firstInputElement.send_keys(Keys.NUMPAD1, Keys.NUMPAD3)  # input 13 to the firstInputElement
secondInputElement.send_keys(20)
# getTotalButton = driver.find_element(By.CSS_SELECTOR, 'form#gettotal button')
getTotalButton = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]')
getTotalButton.click()

WebDriverWait(driver, 30).until(
    ec.text_to_be_present_in_element((By.ID, 'displayvalue'), '3'))

driver.quit()
