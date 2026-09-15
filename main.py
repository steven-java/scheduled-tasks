import pandas as pd
import smtplib
import random
import datetime as dt
import os

GMAIL = "steven.pptx@gmail.com"
GMAIL_PW = "ifyavkktuhurmzdk"

now = dt.datetime.now()
today = (now.month, now.day)
data=pd.read_csv('birthdays.csv')
birthdays_dict={(data_row.month,data_row.day):data_row for(index, data_row) in data.iterrows()}


 # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if today in birthdays_dict:
    num=random.randint(1,3)
    birthday_person=birthdays_dict[today]
    with open(f"letter_templates/letter_{num}.txt") as file:
        letter=file.read()
        new_letter=letter.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=GMAIL, password=GMAIL_PW)
        connection.sendmail(
            from_addr=GMAIL,
            to_addrs=birthday_person.email,
            msg=f"Subject:Happy Birthday!!\n\n{new_letter} "
        )
