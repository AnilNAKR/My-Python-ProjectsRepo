import requests
from twilio.rest import Client
import os

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_TOKEN')

STOCK = "NKE"
COMPANY_NAME = "Nike Inc Footwear"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

alpha_vantage_api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')

parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': alpha_vantage_api_key,
}

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
stock_data = response.json()['Time Series (Daily)']
# print(stock_data)
# The above line takes all the last 100 days high, low, open, close data

daily_stock_data = [float(value['4. close']) for (key, value) in stock_data.items()]
# print(daily_stock_data)
stock_value_start = daily_stock_data[0]
stock_value_end = daily_stock_data[-1]
difference = abs(stock_value_start - stock_value_end)
if (stock_value_start - stock_value_end) < 0:
    symbol = "🔻"
else:
    symbol = "🔺"
print(f"Difference is stock price of {COMPANY_NAME} in last 100 trading days = {symbol} $ {round(difference, 2)}")

diff_percent = (difference / stock_value_start) * 100
percentage = f"{round(diff_percent, 2)}%"
print(f"Percentage Difference = {symbol}{percentage}")

if diff_percent > 15:
    print("Getting News from API as the difference percentage is > 15 %")

    news_parameters = {
        'apiKey': os.environ.get('NEWS_ENDPOINT_API_KEY'),
        'q': COMPANY_NAME,
        'from': "2024-05-01",
        'to': "2024-05-19",
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_data = news_response.json()['articles'][0:1]
    # print(news_data)

    news_data_format = [f"Headlines: {article['title']}\nBrief: {article['description']}" for article in news_data]
    # print(news_data_format)
    for article in news_data_format:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{STOCK}-{COMPANY_NAME}: {symbol}{percentage}\n{article}",
            from_=os.environ.get('TWILIO_MOBILE'),
            to=os.environ.get('MY_MOBILE')
        )
        print(message.status)
        print("Message has been sent to mobile.")
