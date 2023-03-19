import numpy as np
import pyaudio as pa 
import struct 
import matplotlib.pyplot as plt 

CHUNK = 1024 * 2
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100

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
    f_bins = data_fft[0:50] > 1

    # print(f_bins[1:])
    if f_bins[18] == True:
        print('388')
    elif f_bins[19] == True:
        print('409')
    elif f_bins[20] == True:
        print('430')        
    elif f_bins[21] == True:
        print('452')
    elif f_bins[22] == True:
        print('474')
    elif f_bins[23] == True:
        print('496')        
    elif f_bins[24] == True:
        print('516')
    elif f_bins[25] == True:
        print('538')
    elif f_bins[26] == True:
        print('562')        
    elif f_bins[27] == True:
        print('580')
