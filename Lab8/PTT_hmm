import pyaudio
import wave
import RPi.GPIO as GPIO
import time
from hmmlearn import hmm
from python_speech_features import mfcc
from scipy.io import wavfile
import numpy as np
import joblib
from hmm_gmm import Model,compute_mfcc

KEY=20
LED=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY,GPIO.IN,GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)
pwm=GPIO.PWM(LED,10000)
pwm.start(0)

x=Model(['1','2','3','4'])
x.load()
light=0
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
        filepath="TEST.wav"
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
        result=x.test(filepath)
        if result=='1':
            #GPIO.output(LED,GPIO.HIGH)
            pwm.ChangeDutyCycle(50)
            light=50
        elif result=='2':
            #GPIO.output(LED,GPIO.LOW)
            pwm.ChangeDutyCycle(0)
            light=0
        elif result=='3':
            light+=20
            if light>100:
                light=100
            pwm.ChangeDutyCycle(light)
        elif result=='4':
            light-=20
            if light<0:
                light=0
            pwm.ChangeDutyCycle(light)
      
except KeyboardInterrupt:
  GPIO.cleanup() 