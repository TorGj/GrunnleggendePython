# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console..
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['Tors_sid']
auth_token = os.environ['Tors_token']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hei Vilde, lykke til med prøve, måtte teste Python sms-sending",
                     from_='+4740008356',
                     to='+4746506293'
                 )

print(message.sid)