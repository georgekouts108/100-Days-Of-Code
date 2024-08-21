from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)  # this bridges the selenium tech with the Chrome browser

try:
    # login to tinder
    driver.get('https://tinder.com/')

    sleep(2)

    accept_cookies_btn = driver.find_element(By.XPATH, '//*[@id="u849573418"]/div/div[2]/div/div/div[1]/div[1]/button')
    accept_cookies_btn.click()

    sleep(2)

    login_button = driver.find_element(By.XPATH, '//*[@id="u849573418"]/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a')
    login_button.click()

    sleep(2)

    login_with_fb = driver.find_element(By.XPATH, '//*[@id="u-878807658"]/div/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
    login_with_fb.click()

    print(driver.window_handles)
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)

    sleep(3)

    fb_email_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    fb_email_field.send_keys(os.environ['PHONE_NUM'])
    fb_pwd_field = driver.find_element(By.XPATH, '//*[@id="pass"]')
    fb_pwd_field.send_keys(os.environ['FB_PWD'], Keys.ENTER)

    sleep(2)

    continue_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div/div[1]/div[3]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div/div/div/div[1]')
    continue_btn.click()

except Exception:
    print("something happened...")
    pass
