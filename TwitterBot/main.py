import os
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
CHROME_DRIVER_PATH = "C:\\Development\\chromedriver.exe"
PROMISED_DOWN = 400
PROMISED_UP = 100


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

        time.sleep(70)

        self.download_speed = float(self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text)
        self.upload_speed = float(self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text)
        print(f"Download: {self.download_speed} | Upload: {self.upload_speed}")

        return self.download_speed, self.upload_speed

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/home')
        self.driver.maximize_window()
        time.sleep(2)

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
        time.sleep(5)

        tweet_message = f"Hello @MEOpt, you promised an up/download speed of {PROMISED_UP}/{PROMISED_DOWN} Mbps, " \
                        f"however I'm only getting {self.upload_speed}/{self.download_speed} Mbps.\n\n" \
                        f"This message is automated. #Python."

        tweet_box = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div["
                                                       "2]/main/div/div/div/div/div/div[3]/div/div[2]/div["
                                                       "1]/div/div/div/div[2]/div["
                                                       "1]/div/div/div/div/div/div/div/div/div/div/label/div["
                                                       "1]/div/div/div/div/div/div[2]/div/div/div/div")
        tweet_box.send_keys(tweet_message)

        send_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div["
                                                         "2]/main/div/div/div/div/div/div[3]/div/div[2]/div["
                                                         "1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]")
        send_button.click()


twitter_bot = InternetSpeedTwitterBot(chrome_driver_path=CHROME_DRIVER_PATH)
download_speed, upload_speed = twitter_bot.get_internet_speed()

if download_speed < PROMISED_DOWN or upload_speed < PROMISED_UP:
    twitter_bot.tweet_at_provider()
