import smbus
import time # 包含相关库文件
address = 0x68
register = 0x00
bus = smbus.SMBus(1) # 初始化i2c Bus
# FixTime 定义为 2019 年 6 月 12 日 18 时
FixTime = [0x00,0x32,0x18,0x03,0x12,0x06,0x19]
# 定义时钟操作函数
def ds3231SetTime():
  bus.write_i2c_block_data(address,register,FixTime)
def ds3231ReadTime():
  return bus.read_i2c_block_data(address,register,7);
def dec_bcd(bcdtime):
    for i in range(0,len(bcdtime)):
        bcdtime[i]=(bcdtime[i]//4<<4)+bcdtime[i]%10
    return bcdtime
def bcd_dec(dectime):
    for i in range(0,len(dectime)):
        dectime[i]=(dectime[i]//16*10)+dectime[i]%16
    return dectime
        
ds3231SetTime() # 设置时间
while True:
    time.sleep(1)
    #print(ds3231ReadTime())
    now=bcd_dec(ds3231ReadTime())# 读出时间
    print("year:{};month:{};date:{};time:{}:{}:{}".format(now[6],now[5],now[4],now[2],now[1],now[0]))
