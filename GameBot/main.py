from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta

chrome_driver_path = "C:\\Development\\chromedriver.exe"
chrome_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, "cookie")

game_end_time = datetime.now() + timedelta(minutes=5)
chronometer_end_time = datetime.now() + timedelta(seconds=1)
while datetime.now() < game_end_time:
    cookie.click()

    if datetime.now() >= chronometer_end_time:
        chronometer_end_time = datetime.now() + timedelta(seconds=3)  # Update 5 second timer.

        # Get items fom store again with updated prices.
        store = driver.find_elements(By.CSS_SELECTOR, "#store b")[:-1]
        store_prices = [int(item.text.split("- ")[-1].replace(",", "")) for item in store][::-1]

        store_clickable_items = driver.find_elements(By.CSS_SELECTOR, "#store div")[:-1]
        store_clickable_items = store_clickable_items[::-1]

        for idx, item_price in enumerate(store_prices):
            money = int(driver.find_element(By.ID, "money").text.replace(",", ""))
            if item_price <= money:
                store_clickable_items[idx].click()
                break


cookies_per_second = driver.find_element(By.ID, "cps").text
print(cookies_per_second)
driver.quit()
