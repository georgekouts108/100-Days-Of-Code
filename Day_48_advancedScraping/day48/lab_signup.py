from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
last_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
email_address = driver.find_element(By.XPATH, '/html/body/form/input[3]')

first_name.send_keys("John")
last_name.send_keys("Smith")
email_address.send_keys("georgekoutsaris0@gmail.com")

signup_btn = driver.find_element(By.XPATH, value='/html/body/form/button')
signup_btn.click()
