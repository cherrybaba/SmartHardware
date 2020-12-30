import snowboydecoder
import sys
import signal
import MMC

# Demo code for listening to five hotwords at the same time
# Models:magicMirror,goodbye,hello,clock,news

voiceState="SLEEP"; # WAKEUP,CLOCK,HELLO,NEWS;control gesture
interrupted = False

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
    MMC.SetBrightness(100)
    print(voiceState)
        
def sleep():
    global voiceState
    voiceState="SLEEP"
    MMC.SetBrightness(0)
    print(voiceState)
        
def clock():
    global voiceState
    voiceState="CLOCK"
    MMC.showAlert("Set clock! Got it!",1000)
    MMC.showModule("clock") # 根据手势调整
    print(voiceState)

def hello():
    global voiceState
    voiceState="HELLO"
    MMC.showAlert("Good afterNoon, BaoBeiEr~")
    print(voiceState)
    
def news():
    global voiceState
    voiceState="NEWS"
    MMC.showAlert("Read the news! Got it!",1000)
    print(voiceState)
    
# confirm the num of models
if len(sys.argv) != 6:    
    print("Error: need to specify 5 model names")
    print("Usage: python demo.py 1st.model 2nd.model ... 5th.model")
    sys.exit(-1)
models = sys.argv[1:]

MMC.SetBrightness(0)
# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, singalHandler)

sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
callbacks = [wakeup(),sleep(),clock(),hello(),news()]
print('Listening... Press Ctrl+C to exit')

# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=callbacks,
               interrupt_check=interruptCallback,
               sleep_time=0.03)

detector.terminate()