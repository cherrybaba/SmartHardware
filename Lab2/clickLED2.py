import RPi.GPIO as GPIO
import time

KEY=20
LED=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY,GPIO.IN, GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)

print("KeyLED2 Test Program")

p=GPIO.PWM(LED,2.5)
p.start(0)

try:
  click=0
  double=0
  count=0
  while True:
    time.sleep(0.02)
    if count>0:
      count +=1
    if count>40:
      if double==1:
        double=0

      elif click==1:
        click=0
        p.ChangeFrequency(5)
      else:
        click=1
        p.ChangeDutyCycle(50)
     # print("click")
      count=0
    if GPIO.input(KEY)==GPIO.LOW:
      if count==0:
        count=1
      elif count>10 and count<40:
        click=0
        double=1
        p.ChangeDutyCycle(0)
        p.ChangeFrequency(2.5)
       # print("double")
    

except KeyboardInterrupt:
  GPIO.cleanup()  
