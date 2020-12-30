import pyaudio
import wave
import RPi.GPIO as GPIO
import time

KEY=20
LED=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)
flag=3
try:
  while True:
    time.sleep(0.02)
    if GPIO.input(KEY)==GPIO.LOW:
        CHUNK = 512
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
        #filepath="4_"+str(flag)+".wav"
        filepath="test"+str(flag)+".wav"
        flag+=1
        wf = wave.open(filepath, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        print("* recording")
        while GPIO.input(KEY)==GPIO.LOW:
            for i in range(0,int(RATE/CHUNK*1)):
                data=stream.read(CHUNK)
                wf.writeframes(data)
        print ("* done recording")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf.close()
      
except KeyboardInterrupt:
  GPIO.cleanup() 