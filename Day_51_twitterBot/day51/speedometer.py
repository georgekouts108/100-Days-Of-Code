from selenium.webdriver.common.by import By
from time import sleep


class InternetSpeedometer:
    def __init__(self, driver):
        self.driver = driver
        self.download_speed = 0
        self.upload_speed = 0

    def get_report(self):
        return (self.download_speed, self.upload_speed)

    def set_speeds(self):
        self.driver.get('https://www.speedtest.net/')
        sleep(3)

        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()

        sleep(60)
        back_to_test_results_btn = self.driver.find_element(By.XPATH,
                                                            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
        back_to_test_results_btn.click()

        sleep(3)

        download_speed = self.driver.find_element(By.XPATH,
                                                  '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        upload_speed = self.driver.find_element(By.XPATH,
                                                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

        self.download_speed = float(download_speed.text)
        self.upload_speed = float(upload_speed.text)

        sleep(5)
