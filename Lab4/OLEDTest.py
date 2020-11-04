import time
import datetime
import pillow as PIL
import spidev as SPI
import SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def daysDiff(day2):
    #time_array1 = time.strptime(day1, "%Y-%m-%d")
    #timestamp_day1 = int(time.mktime(time_array1))
    timestamp_day1 = time.time()
    time_array2 = time.strptime(day2, "%Y-%m-%d")
    timestamp_day2 = int(time.mktime(time_array2))
    result = (timestamp_day2 - timestamp_day1) // 60 // 60 // 24
    return result

FinalTest="2021-1-22"
RST = 19
DC = 16
bus = 0
device = 0
disp = SSD1306.SSD1306(rst=RST,dc=DC,spi=SPI.SpiDev(bus,device))
disp.begin()
disp.clear()
disp.display()
#显示北大logo
image = Image.open('logo.png').resize((disp.width,disp.height),Image.ANTIALIAS).convert('1')
disp.image(image)
disp.display()

font = ImageFont.load_default()
image1 = Image.new('RGB',(disp.width,disp.height),'black').convert('1')
draw = ImageDraw.Draw(image1)
draw.text((x,top),'Hello World',font=font,fill=255)
draw.text((x,top-10),time.strftime('%Y-%m-%d %H:%M:%S'),font=font,fill=255)
draw.text((x,top-20),"距期末考试还有：{} 天".format(daysDiff(FinalTest)),font=font,fill=255)
disp.image(image1)
disp.display()
