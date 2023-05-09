import smtplib
import datetime as dt
import random
import pandas as pd

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

MY_EMAIL = "afonso.duarte.bernardes@gmail.com"
PASSWORD = ""
WEEK_DAY_MAP = {0: 'Monday', 1: 'Tuesday',
                2: 'Wednesday', 3: 'Thursday',
                4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

now = dt.datetime.now()
week_day = WEEK_DAY_MAP[now.weekday()]

today_day = now.day
today_month = now.month
today_year = now.year

list_of_birthdays = pd.read_csv("birthdays.csv").to_dict(orient="records")

for person in list_of_birthdays:
    # If it is the person's birthday.
    if person["day"] == today_day and person["month"] == today_month:
        with open(file=f"./letter_templates/letter_{random.randint(1, 3)}.txt", mode="r") as letter:
            message = letter.read()
            message = message.replace("[NAME]", person["name"])  # Replace with name of person from CSV.

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Transport Layer Security - Secures connection to email server.
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=person["email"],
                                msg=f"Subject: Happy Birthday!\n\n"
                                f"{message}"
                                )
