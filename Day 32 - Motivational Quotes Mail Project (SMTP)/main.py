import smtplib
import datetime as dt
# import pandas as pd
import random
import os


# ---------------------------------------------------------------------------------------
# Using Date module

date = dt.datetime.now()
weekday = date.weekday()

# -----------------------------------------------------------------------------------------
#  Reading txt file and saving each line as a list item
# O is Monday & 6 is Sunday in Python weekdays
quotes_list = []
if weekday == 0:
    with open("quotes.txt") as quotes_data:
        for quote in quotes_data:
            quotes_list.append(quote)

    selected_message = random.choice(quotes_list)
    print(selected_message)

# ------------------------------------------------------------------------------------------
# Using smtp to send mail to the required people

    my_email = os.environ.get('MYMAILID1')
    password = os.environ.get('MAILKEY')
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=os.environ.get('MYMAILID2'),
            msg="Subject: This is testing mail - Weekly Motivation Quote Mail\n\n"f"{selected_message}"
        )


