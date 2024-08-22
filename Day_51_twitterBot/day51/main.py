import os
from selenium import webdriver
from speedometer import InternetSpeedometer
from twitter import TwitterBot, get_complaint

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

PROMISED_DOWN = 150
PROMISED_UP = 10

# get speeds
speedtest_driver = webdriver.Chrome(options=chrome_options)
speedometer = InternetSpeedometer(driver=speedtest_driver)
speedometer.set_speeds()
download_speed, upload_speed = speedometer.get_report()

# log in to twitter
twitter_driver = webdriver.Chrome(options=chrome_options)
twitter_bot = TwitterBot(t_uname=os.environ['TWITTER_UNAME'], t_pwd=os.environ['TWITTER_PWD'], driver=twitter_driver)
twitter_bot.login()

complaint_msg = get_complaint(
    isp_username='Internet Provider',
    promised_download_speed=PROMISED_DOWN,
    promised_upload_speed=PROMISED_UP,
    download_speed=download_speed,
    upload_speed=upload_speed
)

twitter_bot.upload_tweet(tweet_message=complaint_msg)
