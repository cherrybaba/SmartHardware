import smbus
import time
import spidev as SPI
import SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

#设置OLED显示屏
RST = 19
DC = 16
bus = 0
device = 0
disp = SSD1306.SSD1306(rst=RST,dc=DC,spi=SPI.SpiDev(bus,device))
disp.begin()
disp.clear()
disp.display()

address = 0x48
A0 = 0x40
bus = smbus.SMBus(1)  # 初始化i2c Bus
while True:
    bus.write_byte(address,A0)
    value = bus.read_byte(address)
    font = ImageFont.load_default()
    image1 = Image.new('RGB', (disp.width, disp.height), 'black').convert('1')
    draw = ImageDraw.Draw(image1)
    #显示电压
    draw.text((50,50), 'Voltage='+str(value/256*3.3)+'V', font=font, fill=255)
    disp.image(image1)
    disp.display()
    time.sleep(1)
