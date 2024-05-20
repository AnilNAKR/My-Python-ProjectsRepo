import requests
from bs4 import BeautifulSoup
import smtplib
import os

# Below is the url page of Iphone 15
amazon_item_url = "https://www.amazon.in/dp/B0CHX1W1XY?aref=uGX3flWSO3&aaxitk=c2d994c664586990a0a863d498ae1200&th=1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(amazon_item_url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-price-whole").get_text()
print(f"Product Price: {price}")
product_name = soup.find(class_="product-title-word-break").get_text().strip()
print(f"Product Name: {product_name}")
price_int = price.replace(",", "")
product_price = int(price_int[:-1])

if product_price <= 75000:
    my_email = os.environ.get('EMAIL_FROM')
    to_email = os.environ.get('EMAIL_TO')
    my_password = os.environ.get('EMAIL_TOKEN')
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_email,
            msg=f"Subject: Price of {product_name} has dropped\n\nThe price of {product_name} has dropped to Rs.{product_price}/-, Buy now!"
        )
