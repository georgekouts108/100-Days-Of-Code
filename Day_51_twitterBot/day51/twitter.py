from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


def get_complaint(isp_username, promised_download_speed, promised_upload_speed,
                  download_speed, upload_speed):

    return f"Hey {isp_username}, why is my internet speed {download_speed} down / {upload_speed} up when I pay for {promised_download_speed} down / {promised_upload_speed} up?"


class TwitterBot:
    def __init__(self, t_uname, t_pwd, driver):
        self.username = t_uname
        self.password = t_pwd
        self.driver = driver

    def login(self):
        self.driver.get('https://x.com/i/flow/login')
        sleep(3)
        uname_input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div[2]/div/div[4]/label/div/div[2]/div/input')
        uname_input.send_keys(self.username, Keys.ENTER)
        sleep(3)
        pwd_input = self.driver.find_element(By.NAME, 'password')
        pwd_input.send_keys(self.password, Keys.ENTER)
        sleep(3)

    def upload_tweet(self, tweet_message):
        new_tweet_text_input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        new_tweet_text_input.click()

        # TODO: upload the tweet







