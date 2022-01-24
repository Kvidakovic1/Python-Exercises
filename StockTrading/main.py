import requests
from twilio.rest import Client

STOCK_API_KEY = "O6DRGWTP5K6674O2"
NEWS_API_KEY = "2f6f8400617d4fedaa0a4b4752cb289b"


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIIO_SID = "ACa6678fbdc33f17f42f0a360854148d06"
TWILIIO_AUTH_TOKEN = "73f1ac4b865b42c9fcf5599ccbe92673"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
    }



response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterdays_closing_price = yesterday_data["4. close"]
print(yesterdays_closing_price)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing)


difference = abs(float(yesterdays_closing_price) - float(day_before_yesterday_closing))

diff_percent = (difference / float(yesterdays_closing_price)) * 100
print(diff_percent)

if diff_percent > 5:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qinTitle": COMPANY_NAME,

    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[:3]
    print(three_articles)

    formatted_articles =[f"Headline: {article['title']}. \nBrief: {article ['description']}" for article in three_articles]
    print(formatted_articles)

    client = Client(TWILIIO_SID, TWILIIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="+16204624744",
            to="+385915897286"
        )


