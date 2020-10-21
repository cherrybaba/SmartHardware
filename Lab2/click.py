import RPi.GPIO as GPIO
import time

KEY=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY,GPIO.IN,GPIO.PUD_UP)
print("Key Test Program")

def my_callback(ch):
  print("KEY PRESS")
  return
GPIO.add_event_detect(KEY,GPIO.RISING,callback=my_callback,bouncetime=200)

try:
  while True:
    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()  
