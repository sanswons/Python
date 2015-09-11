from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC0ba5aa9c1744abf390429b433695481b"
auth_token  = "112a77b800f00d718de095e8607e9cb2"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="My name is Ron Burgundy?",
    to="+919819195158",    # Replace with your phone number
    from_="+18329003431") # Replace with your Twilio number
print message.sid
