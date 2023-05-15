import os
import smtplib
from bs4 import BeautifulSoup
import requests


USER_AGENT = os.environ.get("USER_AGENT")
ACCEPT_LANGUAGE = os.environ.get("ACCEPT_LANGUAGE")

EMAIL_FROM = os.environ.get("EMAIL_FROM")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_TO = os.environ.get("EMAIL_TO")
SERVER_ADDRESS = "smtp.gmail.com"

amazon_url = input("Paste the URL of the product you want: ")
target_price = float(input("What's your target price? "))

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,
}
response = requests.get(url=amazon_url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price = float(soup.find("span", class_="a-offscreen").text[:-1].replace(",", "."))

if price <= target_price:
    with smtplib.SMTP(SERVER_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=EMAIL_FROM, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL_FROM,
                            to_addrs=EMAIL_TO,
                            msg="Subject: AMAZON PRICE ALERT\n\n"
                            f"This item currently costs {price}€, which is below your target of {target_price}€. "
                            f"Click the link to buy: {amazon_url}".encode('UTF-8'))
