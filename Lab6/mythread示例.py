#!/usr/bin/env python3
import smbus
from time import sleep
from threading import Thread,Lock

#mylock = Lock()
delta = 5
address = 0x48
A0= 0x40
bus=smbus.SMBus(1)

def da_led():
    val=0
    global delta
    while True:
        print(delta)
        while val+delta<256:
            bus.write_byte_data(address,0x40,val)
            val+=delta
            sleep(0.1)
        while val-delta>=0:
            bus.write_byte_data(address,0x40,val)
            val-=delta
            sleep(0.1)


mythread = Thread(target=da_led)
mythread.setDaemon(True)
mythread.start()

bus.write_byte(address,A0)
while True:
    value = bus.read_byte(address)
    adj_value = (value/255.0)*3.3
    delta = int(value / 10)
#    print(adj_value,'V')
    sleep(0.1)
