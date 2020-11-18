import smbus
import time
from threading import Thread

address = 0x48
A0 = 0x40
bus = smbus.SMBus(1)
value = 215
flag = 1

def setSleepTime(address,A0):
    bus.write_byte(address,A0)
    sleepTime = bus.read_byte(address)
    sleepTime = sleepTime/16*0.01
    return sleepTime
mythread = Thread(target=callable,args=())
mythread.start()
while True:
    mythread.join()
    mythread.setDaemon(True)
    #亮度达到最低，标记flag，开始变亮
    if value == 0:
        flag = 1
    #亮度达到最高，标记flag，开始变暗
    elif value == 255:
        flag = 0
    if flag:
        value += 1
    else:
        value -= 1
    bus.write_byte_data(address,A0,value)
    
    time.sleep(setSleepTime(address,A0))
