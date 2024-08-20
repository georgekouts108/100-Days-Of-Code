from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
all_portals = driver.find_element(By.XPATH, value='//*[@id="mp-other-content"]/ul/li[7]/b/a')

search_btn = driver.find_element(By.XPATH, value='//*[@id="searchform"]/button')
search = driver.find_element(By.NAME, value="search")
search.send_keys("The Wizard of Oz (1939 film)", Keys.ENTER)
