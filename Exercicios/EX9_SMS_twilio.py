import EX9_SMS_twilio_info as info
from twilio.rest import Client

account_sid = info.account_sid
auth_token = info.auth_token

client = Client(account_sid, auth_token)

message = client.messages.create(
    to=info.destination,
    from_=info.sender,
    body='oiiii',
)

print(message.sid)
