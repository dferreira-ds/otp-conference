# find here: twilio.com/console
TWILIO_ACCOUNT_SID = 'ACXXXXX'
TWILIO_AUTH_TOKEN = 'XXXXXXX'

# create here: twilio.com/console/verify/services
VERIFY_SERVICE_SID = 'VAXXXXX'

# replace with your number for testing
MODERATOR = '+1234567890'

# add your number and the numbers of other people joining your call
# could replace with your customer DB in production
KNOWN_PARTICIPANTS = {
  '+1234567891': 'Test',
  '+1234567892': 'Test2',
  MODERATOR: 'Diego'
}