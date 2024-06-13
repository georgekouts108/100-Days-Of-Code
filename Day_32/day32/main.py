import smtplib
import random
import datetime as dt


def get_random_quote():
    with open('quotes.txt', 'r') as file:
        quotes = file.read().split('\n')
        quote = random.choice(quotes)
    return quote


def send_mail(sender_addr, sender_pwd, recip_addr, subject, message):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=sender_addr, password=sender_pwd)
    connection.sendmail(
        from_addr=sender_addr,
        to_addrs=recip_addr,
        msg=f"Subject:{subject}\n\n{message}"
    )
    connection.close()


gmail_email = "georgekoutsaris0@gmail.com"  # sender
gmail_app_pwd = "nbnvasyxnikazyif"
yahoo_email = "georgekoutsaris1@yahoo.com"  # recipient


weekday = dt.datetime.now().weekday()
if weekday == 2:
    quote = get_random_quote()
    send_mail(sender_addr=gmail_email,
              sender_pwd=gmail_app_pwd,
              recip_addr=gmail_email,
              subject='Quote of the Week!',
              message=quote)
