##################### Extra Hard Starting Project ######################
import random
import datetime as dt
import csv
import smtplib


def generate_bday_wish(name):
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        return file.read().replace('[NAME]', name)


def send_bday_wish(name, email):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user="georgekoutsaris0@gmail.com", password="nbnvasyxnikazyif")
    connection.sendmail(
        from_addr="georgekoutsaris0@gmail.com",
        to_addrs=email,
        msg=f"Subject:Happy Birthday " + name + "!" + "\n\n" + generate_bday_wish(name)
    )
    connection.close()


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
today_day = dt.datetime.now().day
today_month = dt.datetime.now().month
today_year = dt.datetime.now().year

with open('birthdays.csv', mode='r') as birthdays_file:
    contents = list(csv.reader(birthdays_file))[1:]
    for entry in contents:
        if int(entry[2]) == today_year and int(entry[3]) == today_month and int(entry[4]) == today_day:
            send_bday_wish(entry[0], entry[1])
