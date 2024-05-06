import requests
from twilio.rest import Client
import os

account_sid = os.environ.get('TWILIO_SID')
auth_token = os.environ.get('TWILIO_TOKEN')

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

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

daily_stock_data = [float(value['4. close']) for (key, value) in stock_data.items()]
stock_value_min = min(daily_stock_data)
stock_value_max = max(daily_stock_data)
difference = abs(stock_value_max - stock_value_min)
print(difference)

diff_percent = (difference / stock_value_max) * 100
percentage = f"{round(diff_percent, 2)}%"

if diff_percent > 20:
    print("Get News")

    news_parameters = {
        'apiKey': os.environ.get('NEWS_ENDPOINT_API_KEY'),
        'q': "Tesla Inc",
        'from': "2024-04-01",
        'to': "2024-04-14",
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_data = news_response.json()['articles'][10:11]

    news_data_format = [f"Headlines: {article['title']}\nBrief: {article['description']}" for article in news_data]

    for article in news_data_format:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"TSLA: 🔻{percentage}\n{article}",
            from_=os.environ.get('TWILIO_MOBILE'),
            to=os.environ.get('MY_MOBILE')
        )
        print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# There is still scope to expand this project and more functionalities to this service.
