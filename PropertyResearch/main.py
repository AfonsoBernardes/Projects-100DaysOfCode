import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "c:/Development/chromedriver.exe"
OPEN_RENT_URL = "https://www.openrent.co.uk"
FORM_LINK = "INSERT FROM LINK"
USER_AGENT = os.environ.get("USER_AGENT")


# SCRAPE WEBSITE FOR PROPERTIES
def scrape_website(website_url):

    location = input("Which city do you wanna move to? ")
    city_area = input("How far, in kilometers, are you willing to be from city center? ")
    maximum_price = input("What is the maximum price you are willing to pay per month? ")

    headers = {"User-agent": USER_AGENT,
               "Accept-Language": "en-GB,en;q=0.9,fr;q=0.8,pt-PT;q=0.7,pt;q=0.6,es;q=0.5",
               }

    property_parameters = {
        "term": "London",
        "area": "5",
        "prices_max": "2000",
        "bedrooms_min": "0",
        "sortType": "1",  # Sort by ascending price.
    }

    page_response = requests.get("".join([website_url, "/properties-to-rent"]),
                                 params=property_parameters,
                                 headers=headers)
    page_response.raise_for_status()

    soup = BeautifulSoup(page_response.content, "html.parser")
    property_data = soup.find(id="property-data").find_all("a")

    url_list = []
    address_list = []
    price_list = []
    for flat in property_data:
        if 'savedsearch' not in flat['href']:
            address = flat.find_next('img')['alt'].split(",")
            address = " -".join(address[1:])
            url = "".join([OPEN_RENT_URL, flat['href']])
            price = flat.find_next("h2").text.split("<span>")[0].strip("\\r\\n").split("£")[-1].split("per")[0].replace(",", "")

            address_list.append(address)
            url_list.append(url)
            price_list.append(int(price))

    return address_list, url_list, price_list


def fill_form(form_url, flats_addresses, flats_urls, flats_prices):
    # ADD PROPERTIES' INFO TO GOOGLE FORM
    chrome_service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=chrome_service)
    driver.get(form_url)
    driver.maximize_window()

    for idx in range(len(flats_urls)):
        address_input, price_input, link_input = driver.find_elements(By.CSS_SELECTOR, "div input[type='text']")

        address_input.send_keys(flats_addresses[idx])
        price_input.send_keys(flats_prices[idx])
        link_input.send_keys(flats_urls[idx])

        driver.find_elements(By.CSS_SELECTOR, "div div div div[role='button']")[0].click()
        # time.sleep(2)
        driver.find_element(By.CSS_SELECTOR, "a").click()


flats_address_list, flats_url_list, flats_price_list = scrape_website(website_url=OPEN_RENT_URL)
print(flats_address_list)
print(flats_price_list)
fill_form(form_url=FORM_LINK, flats_addresses=flats_address_list,
          flats_urls=flats_url_list, flats_prices=flats_price_list)

