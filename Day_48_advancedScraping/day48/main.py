from selenium import webdriver
from selenium.webdriver.common.by import By

# this is how to keep the browser open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)  # this bridges the selenium tech with the Chrome browser
driver.get("https://www.python.org/")

upcoming_events = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events = upcoming_events.text.split('\n')

events_dict = {}
event_count = 0
for i in range(0, len(events)-1, 2):
    date, name = (events[i], events[i+1])
    new_event = {'time': date, 'name': name}

    events_dict[event_count] = new_event
    event_count += 1

driver.close()  # close the current tab the browser is on
# driver.quit()  # closes the entire browser
