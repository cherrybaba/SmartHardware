import numpy as np
import RPi.GPIO as GPIO
import time
import math
KEY=20
LED=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY,GPIO.IN,GPIO.PUD_UP)

def my_callback(ch):
  global em1,em2,em3
  dy=0
  for i in range(0,len):
    ey=x1[i]*em1+x2[i]*em2+em3
    dy+=(ey-y[i])*(ey-y[i])
    em1=em1-lr*2*(ey-y[i])*x1[i]
    em2=em2-lr*2*(ey-y[i])*x2[i]
    em3=em3-lr*2*(ey-y[i])
  print(em1,em2,em3)
  dy=math.sqrt(dy/len)
  print(dy)
  if dy<1.1:
    GPIO.cleanup()
    exit()
GPIO.add_event_detect(KEY,GPIO.RISING,callback=my_callback,bouncetime=200)

try:

    len=2000
    m1=2
    m2=6
    m3=3

    x1=np.random.rand(len)*10
    x2=np.random.rand(len)*10
    y=x1*m1+x2*m2+m3+np.random.randn(len)

    lr=0.001
    em1,em2,em3=np.random.rand(3)*10
    print(m1,m2,m3)
    print(em1,em2,em3)
    while True:  
      time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()

#for j in range(0,1000):

