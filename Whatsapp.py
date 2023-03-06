from twilio.rest import Client

account_sid = 'AC62652c4c5ab8445ece40c824884e5ea6'
auth_token = '8443b1efd1db8da7b10172edc8d73714'

def whatsapp(i):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body='Something is Suspicious going on!',
            media_url='https://img.freepik.com/free-vector/yellow-danger-warning-sign-vector-art-illustration_56104-872.jpg?w=900&t=st=1675823953~exp=1675824553~hmac=2c76f26b79e5e994c4a957444e88259a7a813016d86bb91dc1b0509160126b0e',
            from_='whatsapp:+14155238886',
            to='whatsapp:+919754159491'
        )
    print("Whatsapp: ", i ,"     "+message.sid)
    
    
