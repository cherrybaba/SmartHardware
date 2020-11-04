import time
import datetime
#import Pillow as PIL
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

while True:
  tardate=datetime.datetime(2028,5,4)
  nowdate=datetime.datetime.now()
  delta=tardate-nowdate
  days=delta.days
  seconds=delta.seconds
  hours=(seconds-(seconds%3600))/3600
  seconds=seconds%3600
  minutes=(seconds-(seconds%60))/60
  seconds=seconds%60
  time.sleep(1)

  pkuLogo= Image.open('/home/pi/pku.png').resize((40,40),Image.ANTIALIAS).convert('1')
  font = ImageFont.load_default()
  image = Image.new('RGB',(disp.width,disp.height),'black').convert('1')
  draw = ImageDraw.Draw(image)
  draw.text((32,0),'Hello World',font=font,fill=255)
  draw.text((5,15),time.strftime('%Y-%m-%d %H:%M:%S'),font=font,fill=255)
  draw.text((50,30),"days:{}".format(days),font=font,fill=255)
  draw.text((50,40),"minutes:{}".format(minutes),font=font,fill=255)
  draw.text((50,50),"seconds:{}".format(seconds),font=font,fill=255)
  image.paste(pkuLogo,(0,26))
  disp.image(image)
  disp.display()

