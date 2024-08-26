from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class PropertyRecorder:
    def __init__(self, form_link):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.link = form_link
        self.driver.get(self.link)
        sleep(5)

    def record_listing(self, address, price, link):
        address_field = self.driver.find_element(By.XPATH,
                                                 '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_field = self.driver.find_element(By.XPATH,
                                               '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_field = self.driver.find_element(By.XPATH,
                                              '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit_btn = self.driver.find_element(By.XPATH,
                                              '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div')

        address_field.send_keys(address)
        price_field.send_keys(price)
        link_field.send_keys(link)
        submit_btn.click()
        sleep(3)

        another_response_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        another_response_button.click()
        sleep(2)
