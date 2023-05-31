from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import os
import time


USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

chrome_driver_path = "C:\\Development\\chromedriver.exe"
chrome_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)
driver.maximize_window()

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
job_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")

for job in job_list:
    job.click()
    time.sleep(2)

    try:
        apply_button = driver.find_elements(By.CSS_SELECTOR, ".jobs-apply-button")[0]
        apply_button.click()
        time.sleep(2)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.text != "Submit application":
            # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
            close_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
            close_button.click()

            dismiss_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__confirm-dialog-btn")
            dismiss_button.click()

        else:
            follow_checkbox = driver.find_element(By.CSS_SELECTOR, "div form footer div label")
            follow_checkbox.click()
            submit_button.click()

            dismiss_button = driver.find_element(By.CSS_SELECTOR, "artdeco-modal__dismiss")
            dismiss_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
    except IndexError:
        print("Already applied to this job, skipped.")
        continue

time.sleep(5)
driver.quit()
