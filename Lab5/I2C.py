import smbus
import time # 包含相关库文件
address = 0x68
register = 0x00
bus = smbus.SMBus(1) # 初始化i2c Bus
# FixTime 定义为 2019 年 6 月 12 日 18 时
FixTime = [0x00,0x00,0x18,0x03,0x12,0x06,0x19]
# 定义时钟操作函数
def ds3231SetTime():
  bus.write_i2c_block_data(address,register,FixTime)
def ds3231ReadTime():
  return bus.read_i2c_block_data(address,register,7);
ds3231SetTime() # 设置时间
ds3231ReadTime() # 读出时间