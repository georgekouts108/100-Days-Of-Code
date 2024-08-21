from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)  # this bridges the selenium tech with the Chrome browser

try:
    driver.get('https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0')

    sleep(2)

    accept_cookies_button = driver.find_element(By.XPATH, '//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[1]')
    accept_cookies_button.click()

    sleep(2)

    # sign in to linkedin
    sign_in_button = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
    sign_in_button.click()

    sleep(2)

    email_input = driver.find_element(By.XPATH, '//*[@id="username"]')
    pwd_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')

    email_input.send_keys(os.environ['LINKEDIN_EMAIL'])
    pwd_input.send_keys(os.environ['LINKEDIN_PWD'])
    login_button.click()

    sleep(2)

    hide_msg_button = driver.find_element(By.XPATH, '//*[@id="ember113"]')
    hide_msg_button.click()

    sleep(2)

    # save the first jobs and follow the company
    save_job_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[5]/div/button')
    save_job_button.click()

    sleep(2)

    company_name_button = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[1]/div[1]/div/a')
    company_name_button.click()

    sleep(2)

    follow_btn = driver.find_element(By.XPATH, '//*[@id="ember389"]/div[2]/div[2]/div[3]/div/div[1]/div[1]/button')
    follow_btn.click()

    sleep(2)
except Exception:
    pass
