import os
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
PROMISED_UP = 500
PROMISED_DOWN = 100


class InternetSpeedTwitterBot:
    def __init__(self, chrome_driver_path):
        self.upload_speed = 0
        self.download_speed = 0
        self.chrome_service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.chrome_service)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()

        try:
            accept_button = self.driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
            accept_button.click()
            # time.sleep(1)
        except NoSuchElementException:
            pass

        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        time.sleep(150)

        self.download_speed = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.upload_speed = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text
        print(f"Download:{self.download_speed} | Upload: {self.upload_speed}")

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/home')
        self.driver.maximize_window()
        time.sleep(1)

        # Log in
        user_input = self.driver.find_element(By.CSS_SELECTOR, "input")
        user_input.send_keys(TWITTER_USERNAME)

        next_button = self.driver.find_elements(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div["
                                                          "2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")[0]
        next_button.click()

        time.sleep(1)
        password_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(TWITTER_PASSWORD)

        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                           '2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        log_in_button.click()
        time.sleep(3)


twitter_bot = InternetSpeedTwitterBot(chrome_driver_path=CHROME_DRIVER_PATH)
# twitter_bot.tweet_at_provider()
twitter_bot.get_internet_speed()

