import RPi.GPIO as GPIO
import time
LED=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

#GPIO.output(LED,GPIO.LOW)
pwm=GPIO.PWM(LED,5)
pwm.start(0)
try:
  while True:
    time.sleep(1)
    f=open('/sys/bus/w1/devices/28-0000096579d5/w1_slave','r')
    lines=f.readlines()
    #print(lines[0][-4:]+'test')
    if(lines[0][-4:-1]=="YES"):
      #print("readT")
      pos=lines[1].find('t=')
      t=int(lines[1][pos+2:])/1000
      print(t)
      if t>26:
        pwm.ChangeDutyCycle(50)
      else:
        pwm.ChangeDutyCycle(0)
    f.close()

except KeyboardInterrupt:
  pwm.stop()
  GPIO.cleanup()
