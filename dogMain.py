import time
import RPi.GPIO as GPIO
from twilio.rest import Client

PIN_FOOD  = 7
PIN_POTTY = 8

ACCOUNT_SID   = 'AC06d136e738e32531a3c1f14bf50adf20'
AUTHTOKEN     = 'cbe0e851ddff3d88f6426bafa044b7c8'
# MY_NUMBER     = '+18015084976'
MY_NUMBER     = '+19728387046'
TWILIO_NUMBER = '+13854744945'

def setup():
   GPIO.setmode(GPIO.BCM)
   # GPIO.setup(PIN_FOOD, GPIO.IN)
   GPIO.setup(PIN_FOOD, GPIO.IN, GPIO.PUD_DOWN)

def sendAlert(message):
   twilioClient = Client(ACCOUNT_SID, AUTHTOKEN)
   twilioClient.messages.create(body=message, from_=TWILIO_NUMBER, to=MY_NUMBER)

def main():
   setup()

   # PIN 7 AND 3.3V
   # normally 0, when connected 1
   try:
      while(True):
         print(GPIO.input(PIN_FOOD))
         time.sleep(.1)
   except KeyboardInterrupt:
      GPIO.cleanup()
      print("\nExiting")

   # sendAlert('Feed me please!')

if __name__=="__main__":
   main()
