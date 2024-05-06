import pandas as pd
import random
import datetime as dt
import smtplib
import os

today = dt.datetime.now()
day = today.day
month = today.month
today_tuple = (month, day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_num = random.randint(1, 3)
    file_path = f"letter_templates/letter_{file_num}.txt"

    with open(file_path) as letter_content:
        content = letter_content.read()
        modified_content = content.replace("[NAME]", birthday_person['name'])
        print(modified_content)
    my_email = "n.anilkumar7896@gmail.com"
    my_password = os.environ.get('MAIL_KEY')
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f"Subject: This is testing mail for sending automated Birthday Wishes.\n\n{modified_content}"
        )
