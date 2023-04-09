# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client

# Set environment variables for your credentials
# Read more at http://twil.io/secure

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)
User = "Ronald Santos Garcia"
date ="March 25th"
call_purpose = "appointment"
reason = "late"
eta = "10 Minutes"
say = "" 
outBound = "+15712450024"
if call_purpose == "late": 
  say= "Hello this is {} and I am running late to my Appointment. My Estimated Time is {}".format(User,eta )

elif call_purpose == "sick": 
  say = "Hey, I am not going to be able to make it. I am currently sick. I am okay,butI won't be able to return your calls until later today."
elif call_purpose == "emergency": 
  say = "Hello, an Emergency came up and I won't be able to make it. I will call back late today and explained everything."
  
elif call_purpose =="make appointment": 
  say = "Hello, I was calling to make a appointment type for {} on {}. I would like the earlier/later appointment for that {}. Thank you, have a good day".format(User,date,date)
  
  
  
  
  

call = client.calls.create(
  
  twiml='<Response><Pause length="3"/><Say> {}</Say></Response>'.format(say),
  to=outBound,
  from_="+18665253387"
)

print(call.sid)
