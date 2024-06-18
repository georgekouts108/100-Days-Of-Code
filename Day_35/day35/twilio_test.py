from twilio.rest import Client
import os

account_sid = os.environ.get('TWILIO_ACCT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

your_mobile_number = '+1XXXXXXXXXX'

message = client.messages.create(
  from_='+16508259151',
  to=your_mobile_number,
  body='Hello from TWILIO'
)

print(message.status)
