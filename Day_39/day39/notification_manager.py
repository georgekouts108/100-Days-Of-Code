from twilio.rest import Client
import os

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self._twilio_account_sid = os.environ['TWILIO_ACCT_SID']
        self._twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
        self._twilio_phone = os.environ['TWILIO_PHONE_NUM']
        self._client = Client(self._twilio_account_sid, self._twilio_auth_token)

    def send_text_message(self, mobile_num, message):
        self._client.messages.create(
            from_=self._twilio_phone,
            to=mobile_num,
            body=message
        )
