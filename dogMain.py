import time
import RPi.GPIO as GPIO
from twilio.rest import Client
import twilio_info

PIN_FOOD  = 7
PIN_POTTY = 8


def setup():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(PIN_FOOD,  GPIO.IN, GPIO.PUD_DOWN)
   GPIO.setup(PIN_POTTY, GPIO.IN, GPIO.PUD_DOWN)

def sendAlert(message):
   twilioClient = Client(ACCOUNT_SID, AUTHTOKEN)
   twilioClient.messages.create(body=message, from_=TWILIO_NUMBER, to=MY_NUMBER)

def main():
   setup()

   # PIN 7 AND 3.3V
   # normally 0, when connected 1
   try:
      while(True):
         if (GPIO.input(PIN_FOOD)):
            print("Food")
            time.sleep(2)

         if (GPIO.input(PIN_POTTY)):
            print("Potty")
            time.sleep(2)
   
   except KeyboardInterrupt:
      GPIO.cleanup()
      print("Exiting")

   # sendAlert('Feed me please!')

if __name__=="__main__":
   main()
