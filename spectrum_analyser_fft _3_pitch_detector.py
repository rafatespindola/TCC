import numpy as np #importing Numpy with an alias np
import pyaudio as pa 
import struct 
import matplotlib.pyplot as plt 

CHUNK = 1024 * 2
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100 # in Hz

p = pa.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

while 1:
    data = stream.read(CHUNK) 
    data_int = struct.unpack(str(CHUNK) + 'h', data)
    data_fft = np.abs(np.fft.fft(data_int))*2/(11000*CHUNK)
    print('len: ' + str(len(data_fft)))

    maximo = max(data_fft)
    print('max: ' + str(maximo))
    
    index = 0
    for i in data_fft:
        if i == maximo:
            print('index freq: ' + str(index))
        index += 1
