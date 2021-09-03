from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# import by using the keyword from selenium
# you think that you have to import webdriver, but you have to prefix from selenium
# from selenium.webdriver.common.by, inside the by is only the class By, and so forth the WebDriverWait
# expected_conditions have a lot of classes
driver = webdriver.Chrome()
driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
downloadButtonElement = driver.find_element_by_id("downloadButton")
driver.implicitly_wait(10)  # should always think of the implicitly_wait and call 1 time
downloadButtonElement.click()

progressBarLabelElement = driver.find_element_by_class_name("progress-label")

print(progressBarLabelElement.text)

WebDriverWait(driver, 30).until(
    ec.text_to_be_present_in_element((By.CLASS_NAME, 'progress-label'), 'Complete!'))
# WebDriver class accept the locator, not the element
# Have to provide the arguments to the WebDriverWait

print(progressBarLabelElement.text)

driver.quit()
