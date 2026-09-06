# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime as dt
import pandas as pd
import random as rd
import smtplib

my_email = "m.bernat.madrid@gmail.com"
password = ""
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)


now = dt.datetime.now()
current_month = now.month
current_day = now.day

letters = []

for number in range(1, 4):
    with open(f"letter_templates/letter_{number}.txt", "r", encoding="utf-8") as file:
        content = file.read()
        letters.append(content)

df = pd.read_csv("birthdays.csv")

for (index, row) in df.iterrows():
    if row.month == current_month and row.day == current_day:
        random_letter = rd.choice(letters)
        birthday_letter = random_letter.replace("[NAME]", row["name"])
        connection.sendmail(
            from_addr=my_email, to_addrs=row["email"], msg=f"Subject: Peluchito birthday letter\n\n{birthday_letter}")


connection.close()
