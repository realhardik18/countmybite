from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('ACCOUNT_TOKEN')
whatsapp_number = os.getenv('WHATSAPP_NUMBER')

client = Client(account_sid, auth_token)

message = client.messages.create(
  from_=f'whatsapp:{whatsapp_number}',
  body='Your appointment is coming up on July 21 at 3PM',
  to='whatsapp:+919900951071'
)

print(message.sid)