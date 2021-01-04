import snowboydecoder
import sys
import signal
import MMC
import logging
import time
from picamera import PiCamera,Color
import time
import demjson
from pygame import mixer 
from aip import AipBodyAnalysis
from aip import AipSpeech
from threading import Thread

# Gestures:Thumb_up,Thumb_down,Fist,Five
# Code for listening to five hotwords at the same time
# Voice Models:magicMirror,goodbye,hello,clock,news

hand={'One':'数字1','Five':'Read More','Fist':'Read Less','Ok':'OK',
      'Prayer':'祈祷','Congratulation':'作揖','Honour':'作别',
      'Heart_single':'比心心','Thumb_up':'Previous News or clock disappear','Thumb_down':'Next News or clock appear',
      'ILY':'我爱你','Palm_up':'掌心向上','Heart_1':'双手比心1',
      'Heart_2':'双手比心2','Heart_3':'双手比心3','Two':'数字2',
      'Three':'数字3','Four':'数字4','Six':'数字6','Seven':'数字7',
      'Eight':'数字8','Nine':'数字9','Rock':'Rock','Insult':'竖中指','Face':'脸'}

""" 人体分析 APPID AK SK """
APP_ID = '23434762'
API_KEY = 'FV8ynuBjMImFgnbDs4EjllQf'
SECRET_KEY = 'xTrQA5tvZYNG0VQDx2xGepKMtEGw2oRH'

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def gestureDetect():
    global voiceState,clockFlag
    lastRes=0
    while True:
        #if voiceState!="CLOCK" and voiceState!="NEWS":
            #continue
        """1.拍照 """
        camera.start_preview()
        time.sleep(1)
        #mixer.music.stop()
        camera.capture('./image.jpg')
        camera.stop_preview()
        image = get_file_content('./image.jpg')

        """ 2.调用手势识别 """
        raw = str(client.gesture(image))
        text = demjson.decode(raw) # decode 返回的json
        try:
            res = text['result'][0]['classname']
        except:
            print('Nothing detected!' )
        else:
            if res==lastRes:
                print('Nothing detected!' )
            else:
                lastRes=res
                print('Detect' + hand[res])
                if voiceState=="CLOCK":
                    if clockFlag== "appear" and hand[res]=="Previous News or clock disappear":
                        #MMC.showAlert("Hide clock! Got it!",2000)
                        #time.sleep(2)
                        MMC.hideModule("clock")
                        clockFlag="disappear"
                    elif clockFlag=="disappear" and hand[res]== "Next News or clock appear":
                        #MMC.showAlert("Show clock! Got it!",2000)
                        #time.sleep(2)
                        MMC.showModule("clock")
                        clockFlag="appear"
                if voiceState == "NEWS":
                    if hand[res]=="Previous News or clock disappear":
                        #MMC.showAlert("Previous news! Got it!",2000)
                        #sleep(2)
                        MMC.previousArtical()
                    if hand[res]=="Next News or clock appear":
                        #MMC.showAlert("Next news! Got it!",2000)
                        #sleep(2)
                        MMC.nextArtical()
                    if hand[res]=="Read More":
                        #MMC.showAlert("Read the news! Got it!",1000)
                        MMC.readMore()
                    if hand[res]=="Read Less":
                        MMC.readLess()
# main loop
# make sure you have the same numbers of callbacks and models
def voiceDetect():
    global detector,logger
    logger.debug("start.")
    detector.start(detected_callback=callbacks,
                   interrupt_check=interruptCallback,
                   sleep_time=0.03)

    detector.terminate()
    logger.debug("finished.")

def singalHandler(signal, frame):
    global interrupted
    interrupted = True

def interruptCallback():
    global interrupted
    return interrupted

# callbacks
def wakeup():
    global voiceState
    voiceState="WAKEUP"
    MMC.setBrightness(100)
    print(voiceState)
    
        
def sleep():
    global voiceState
    if voiceState=="WAKEUP":
        voiceState="SLEEP"
        MMC.setBrightness(0)
    else:
        voiceState="WAKEUP" #退出设置
    print(voiceState)
    
        
def clock():
    global voiceState
    MMC.showAlert("Set clock! Got it!",2000)
    time.sleep(2)
    voiceState="CLOCK"
    print(voiceState)
    

def hello():
    global voiceState
    voiceState="HELLO"
    MMC.showAlert("Good afterNoon, BaoBeiEr~",2000)
    time.sleep(2)
    print(voiceState)
    
    
def news():
    global voiceState
    MMC.showAlert("Read the news! Got it!",1000)
    voiceState="NEWS"
    print(voiceState)



#camera设置    
camera = PiCamera()
client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)
'''cam config'''
camera.resolution = (1280, 720)
#声音设置
logging.basicConfig()
logger = logging.getLogger("snowboy") # 终端打印提示信息
voiceState="SLEEP"; # WAKEUP,CLOCK,HELLO,NEWS;control gesture
clockFlag="appear" # appear,disappear
interrupted = False

# confirm the num of models
if len(sys.argv) != 6:    
    print("Error: need to specify 5 model names")
    print("Usage: python demo.py 1st.model 2nd.model ... 5th.model")
    sys.exit(-1)
models = sys.argv[1:]

MMC.setBrightness(0)
# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, singalHandler)

sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
callbacks = [lambda: wakeup(),
             lambda: sleep(),
             lambda: clock(),
             lambda: hello(),
             lambda: news()]
print('Listening... Press Ctrl+C to exit')

try:
    voiceThread = Thread(target=voiceDetect(), args=())
    gestureThread =Thread(target=gestureDetect(), args=())

    voiceThread.start()
    gestureThread.start()
    voiceThread.join()
    gestureThread.join()
except KeyboardInterrupt:
    detector.terminate()

        