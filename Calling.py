from twilio.rest import Client

account_sid = 'ACa1d4fe668cf8593d36ea196877fcb205'
auth_token = 'c751488b332a3f23243228edc905401f'
client = Client(account_sid, auth_token)

def calling(i) :
     call = client.calls.create(
         url='http://demo.twilio.com/docs/voice.xml',
          to='+917566634500',
          from_='+19542873100'
        )
     print("Calling: ", i, "     "+call.sid)