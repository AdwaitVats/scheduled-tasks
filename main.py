# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import pandas
import smtplib
import os
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
import random
data=pandas.read_csv("birthdays.csv")
letter_list=["letter_1.txt","letter_2.txt","letter_3.txt"]
data_frame=pandas.DataFrame(data)
import datetime as dt
now=dt.datetime.now()
for (index,row) in data_frame.iterrows():
    if row["day"]==now.day and row["month"]==now.month:
        letter=random.choice(letter_list)
        with open(f"letter_templates/{letter}") as file:
            message=file.read()
            message=message.replace("[NAME]",row["name"])
        connection=smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(user=MY_EMAIL,password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="adwaitvats1@gmail.com",
                            msg=f"Subject: Birthday Wisher\n\n{message}")
        connection.close()
