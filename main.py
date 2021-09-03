from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
downloadButtonElement = driver.find_element_by_id("downloadButton")
driver.implicitly_wait(10)
downloadButtonElement.click()

progressBarLabelElement = driver.find_element_by_class_name("progress-label")

print(progressBarLabelElement.text)

WebDriverWait(driver, 30).until(
    ec.text_to_be_present_in_element((By.CLASS_NAME, 'progress-label'), 'Completed!'))

print(progressBarLabelElement.text)

driver.close()
driver.quit()
