import RPi.GPIO as GPIO
import time

KEY=20
LED=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

print("KeyLED1 Test Program")


def my_callback(ch):
  global lighted
  if lighted==0:
    GPIO.output(LED,1)
    lighted=1
  else:
    GPIO.output(LED,0)
    lighted=0
  return
GPIO.add_event_detect(KEY,GPIO.RISING,callback=my_callback,bouncetime=200)

try:
  lighted=0
  while True:
    time.sleep(0.1)
except KeyboardInterrupt:
  GPIO.cleanup()  
