from twilio.rest import Client
import os
import smtplib

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, customer_list):
        self._twilio_account_sid = os.environ['TWILIO_ACCT_SID']
        self._twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self._twilio_phone = os.environ['TWILIO_PHONE_NUM']
        self._client = Client(self._twilio_account_sid, self._twilio_auth_token)
        self.customer_emails = customer_list

    def send_emails(self, flight_data):
        body = ''
        if flight_data.stops > 0:
            body = (f"Low price alert! Only {flight_data.price} GBP to fly from {flight_data.origin} to "
                f"{flight_data.destination}, with {flight_data.stops} stop(s) departing on "
                f"{flight_data.departure_date} and returning on {flight_data.return_date}. ")
        else:
            body = (f"Low price alert! Only {flight_data.price} GBP to fly directly from {flight_data.origin} to "
                    f"{flight_data.destination}, departing on "f"{flight_data.departure_date} "
                    f"and returning on {flight_data.return_date}. ")

        sender_addr = os.environ['SMTPLIB_SENDER_EMAIL']
        sender_pwd = os.environ['SMTPLIB_SENDER_PWD']

        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=sender_addr, password=sender_pwd)
        for recip_addr in self.customer_emails:
            connection.sendmail(
                from_addr=sender_addr,
                to_addrs=recip_addr,
                msg=f"Subject:Low Flight Price Alert\n\n{body}"
            )
        connection.close()

    def send_text_message(self, mobile_num, message):
        self._client.messages.create(
            from_=self._twilio_phone,
            to=mobile_num,
            body=message
        )
