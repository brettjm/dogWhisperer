import time
import RPi.GPIO as GPIO
import subprocess
from twilio.rest import Client
import twVars

PIN_FOOD  = 7
PIN_POTTY = 8

def setup():
   GPIO.setmode(GPIO.BCM)
   GPIO.setup(PIN_FOOD,  GPIO.IN, GPIO.PUD_DOWN)
   GPIO.setup(PIN_POTTY, GPIO.IN, GPIO.PUD_DOWN)

def sendAlert(message):
   twilioClient = Client(twVars.ACCOUNT_SID, twVars.AUTHTOKEN)
   twilioClient.messages.create(body  = message, 
                                from_ = twVars.TWILIO_NUMBER, 
                                to    = twVars.MY_NUMBER_1)
   twilioClient.messages.create(body  = message, 
                                from_ = twVars.TWILIO_NUMBER, 
                                to    = twVars.MY_NUMBER_2)

def main():
   setup()
   print("Starting up...")

   # PIN 7 AND 3.3V
   # normally 0, when connected 1
   try:
      while(True):
         if (GPIO.input(PIN_FOOD)):
            sendAlert('Feed me please!')
            time.sleep(2)

         elif (GPIO.input(PIN_POTTY)):
            print("Potty")
            subprocess.call(['mpg123', '-q', 'pee_clip.mp3'])
            time.sleep(2)

   except KeyboardInterrupt:
      GPIO.cleanup()
      print("\nExiting")

if __name__=="__main__":
   main()
