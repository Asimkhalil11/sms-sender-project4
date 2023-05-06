from twilio.rest import Client

SID = 'AC3189ddc0c552374cf85ee2cc79feff6f'
AUTH_TOKEN = 'c32f3b04cf358726ea72349a0e20a4c9'

client = Client(SID, AUTH_TOKEN)

sms_content = input('Please enter the SMS content: ')
recipient_phone_number = input('Please enter the recipient phone number: ')

client.messages.create(body=sms_content, from_='+13203627664', to=recipient_phone_number)
