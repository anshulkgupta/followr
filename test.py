from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "ACec120bce9d6649ee44e22fc3d43e9c68"
auth_token = "902572dba95f5e11aa9cd0946a57d7e6"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+15712631584", from_="+13472692418",
                                     body="Hello there!")