# Amazon Product Price Tracker Project

This Python script tracks the price of a product on Amazon and sends email notifications when the price drops below a specified threshold.

## Features

1) **Web Scraping:** Utilizes the **`requests`** library along with **`BeautifulSoup`** to scrape the Amazon product page and extract the product's name and price.

2) **Email Notification:** When the price of the product falls below a specified threshold (e.g., Rs. 75,000), the script sends an email notification to a specified recipient using the SMTP protocol.

## Usage

1) **Setup Environment Variables:** Set up environment variables for your email address (`EMAIL_FROM`), recipient's email address (`EMAIL_TO`), and email password or token (`EMAIL_TOKEN`) for authentication.

2) **Amazon Product URL:** Provide the URL of the Amazon product page (`amazon_item_url`) that you want to track.

3) **Run the Script:** Execute the Python script(main.py), and it will continuously monitor the price of the specified product on Amazon. When the price drops below the threshold, it will send an email notification to the specified recipient.
<hr>

![Day 47 Amazon price tracker](https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/5b3de3c0-ef6e-4be8-b6f3-81a601ba949b)

<hr>

https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/0971aa5f-9725-4eb4-99a8-6ad383a9ea8e

