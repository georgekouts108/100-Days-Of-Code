import os
from time import sleep
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

insta_username = os.environ['INSTA_UNAME']
insta_pwd = os.environ['INSTA_PWD']

driver.get('https://www.instagram.com/')
sleep(3)
uname_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
pwd_input = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

uname_input.send_keys(insta_username)
pwd_input.send_keys(insta_pwd, Keys.ENTER)
sleep(5)

driver.get(f'https://www.instagram.com/{os.environ["TARGET_UNAME"]}/')
sleep(5)
followers_list = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a')
followers_list.click()
sleep(5)

modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[4]"
modal = driver.find_element(by=By.XPATH, value=modal_xpath)
for i in range(10):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    sleep(2)

all_buttons = []
for i in range(83):
    try:
        button = driver.find_elements(By.CSS_SELECTOR, value=f"body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div > div > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1sxyh0.xurb0ha.x1uhb9sk.x6ikm8r.x1rife3k.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.x1l90r2v > div:nth-child({i+1}) > div > div > div > div > div > div > div:nth-child(3) > div > button")
        all_buttons.append(button)
    except Exception:
        print("an error happened...")

pprint(all_buttons)

for button in all_buttons:
    try:
        button[0].click()
        sleep(1.1)
    except ElementClickInterceptedException:
        cancel_button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
        cancel_button.click()
