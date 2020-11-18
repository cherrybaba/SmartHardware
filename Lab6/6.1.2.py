import smbus
import time

address = 0x48
A0 = 0x40
bus = smbus.SMBus(1)
value = 215
flag = 1
while True:
    #亮度达到最低，标记flag，开始变亮
    if value == 155:
        flag = 1
    #亮度达到最高，标记flag，开始变暗
    elif value == 215:
        flag = 0
    if flag:
        value += 1
    else:
        value -= 1
    bus.write_byte_data(address,A0,value)
    time.sleep(0.1)
