from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os
import time

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

chrome_driver_path = "C:\\Development\\chromedriver.exe"
chrome_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)

driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3622448256&distance=25&f_AL=true&f_E=1%2C2&'
           'f_JT=F%2CI&f_TPR=r604800&geoId=102257491&keywords=software%20developer&refresh=true')

# Sign in
sign_in = driver.find_element(By.XPATH, "/html/body/div[3]/header/nav/div/a[2]")
sign_in.click()

email_box = driver.find_element(By.ID, "username")
email_box.send_keys(USERNAME)

password_box = driver.find_element(By.ID, "password")
password_box.send_keys(PASSWORD)

sign_in = driver.find_element(By.CSS_SELECTOR, "form div button")
sign_in.click()

time.sleep(15)

# Apply for jobs.
# try:
#     verify = driver.find_element(By.CSS_SELECTOR, "#home button")
#     verify.click()
#     print("Verified.")
#
# except NoSuchElementException:
#     print("Verification not needed.")

job_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in job_list:
    job.click()
    apply_button = driver.find_elements(By.CSS_SELECTOR, ".jobs-apply-button")
    apply_button.click()
    time.sleep(2)

time.sleep(100)