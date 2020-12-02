import pyaudio
import wave
def record_audio(wave_out_path,record_second):
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
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    print("* recording")
    for i in range(0,int(RATE/CHUNK*record_second)):
        data=stream.read(CHUNK)
        wf.writeframes(data)
    print ("* done recording")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()
record_audio("output.wav",record_second=4)