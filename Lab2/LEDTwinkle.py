import RPi.GPIO as GPIO
import time
LED=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

p=GPIO.PWM(LED,2.5)
p.start(50)
try:
  while True:
    time.sleep(0.05)
except KeyboardInterrupt:
  pass
  p.stop()
  GPIO.cleanup()
