import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "AAPL"
COMPANY_NAME = "Apple"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday's closing and the day before yesterday, get STOCK news.

alpha_endpoint = 'https://www.alphavantage.co/query'
alpha_api_key = os.environ.get("ALPHA_API_KEY")
alpha_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': alpha_api_key,
}

alpha_response = requests.get(alpha_endpoint, alpha_params)
alpha_data_daily = alpha_response.json()['Time Series (Daily)']

yesterday_date = str((datetime.now() - timedelta(1)).date())
yesterday_closing = float(alpha_data_daily[yesterday_date]["4. close"])

before_yesterday_date = str((datetime.now() - timedelta(2)).date())
before_yesterday_closing = float(alpha_data_daily[before_yesterday_date]["4. close"])

price_variation = ((yesterday_closing - before_yesterday_closing) / before_yesterday_closing) * 100


# STEP 2: Use https://newsapi.org - Get the first 3 news pieces for the COMPANY_NAME.
def get_news():
    today_date = str(datetime.now().date())

    news_api_key = os.environ.get("NEWS_API_KEY")
    news_endpoint = "https://newsapi.org/v2/everything"
    news_parameters = {
        "apiKey": news_api_key,
        "q": STOCK,
        "qInTitle": COMPANY_NAME,
        "from": yesterday_date,
        "to": today_date,
        "language": "en",
        "sort_by": "relevancy",
    }

    return requests.get(news_endpoint, news_parameters).json()['articles'][:3]


def send_message(news_list):
    # Twilio Setup
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    twilio_auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    twilio_phone_num_from = os.environ.get("TWILIO_PHONE_NUM_FROM")
    phone_num_to = os.environ.get("PHONE_NUM_TO")

    symbol = "🔺" if price_variation > 0 else "🔻"
    for news in news_list:
        news_title = news["title"]
        news_brief = news["description"]

        formatted_article = f"{STOCK}: {symbol}{price_variation:.3}% \nHeadline: {news_title} \nBrief: {news_brief}"

        client = Client(twilio_account_sid, twilio_auth_token)
        message = client.messages.create(
            body=formatted_article,
            from_=twilio_phone_num_from,
            to=phone_num_to,
        )

        print(message.status)


if abs(price_variation) >= 5:
    news_articles = get_news()
    send_message(news_articles)
