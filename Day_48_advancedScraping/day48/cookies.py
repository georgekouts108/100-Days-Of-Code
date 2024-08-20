from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime as dt

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie_btn = driver.find_element(By.XPATH, '//*[@id="cookie"]')


def buy_most_expensive_upgrade():
    bank = int(driver.find_element(By.ID, value='money').text.replace(',', ''))

    store = driver.find_element(By.ID, value='store')
    _store = list(store.text.split('\n'))

    item_name = ''
    item_cost = 0
    for i in range(len(_store)):
        if ' - ' in _store[i]:
            item = _store[i].split(' - ')
            _name = item[0]
            _cost = int(item[1].replace(',', ''))

            if bank < _cost:
                break

            if i == 0:
                item_name = _name
                item_cost = _cost
            else:
                if _cost > item_cost:
                    item_name = _name
                    item_cost = _cost
    try:
        item_button = driver.find_element(By.ID, value=f"buy{item_name}")
        item_button.click()
    except Exception:
        pass

start_time = dt.now()
while True:
    cookie_btn.click()
    secs_elapsed = (dt.now() - start_time).seconds
    if secs_elapsed > 30:
        cps = driver.find_element(By.ID, value='cps').text
        print(cps)
        break
    if secs_elapsed % 5 == 0:
        buy_most_expensive_upgrade()


driver.close()
