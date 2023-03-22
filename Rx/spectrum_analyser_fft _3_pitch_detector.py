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

buffer = ''
last_simbol = -1 # Start with a impossible simbol '-1'
last_buffer = ''
while 1:
    data = stream.read(CHUNK)
    data_int = struct.unpack(str(CHUNK) + 'h', data)
    data_fft = np.abs(np.fft.fft(data_int))*2/(11000*CHUNK)
    f_bins = data_fft[0:50] > 1

    # print(f_bins[1:])
    if f_bins[32] == True and last_simbol != 32:
        buffer += '0'
        last_simbol = 32
    elif f_bins[34] == True and last_simbol != 34:
        buffer += '1'
        last_simbol = 34
    elif f_bins[20] == True and last_simbol != 20:
        buffer += '2'
        last_simbol = 20
    elif f_bins[22] == True and last_simbol != 22:
        buffer += '3'
        last_simbol = 22
    elif f_bins[24] == True and last_simbol != 24:
        buffer += '4'
        last_simbol = 24
    elif f_bins[26] == True and last_simbol != 26:
        buffer += '5'
        last_simbol = 26
    elif f_bins[28] == True and last_simbol != 28:
        buffer += '6'
        last_simbol = 28
    elif f_bins[30] == True and last_simbol != 30:
        buffer += '7'
        last_simbol = 30

    if len(buffer) > 0 and buffer != last_buffer: 
        print(buffer)
        last_buffer = buffer


    if buffer == '1201':
        print('chegou: a')
        buffer = ''
    elif buffer == '1202':
        print('chegou: b')
        buffer = ''
    elif buffer == '1203':
        print('chegou: c')
        buffer = ''
    elif buffer == '1210':
        print('chegou: d')
        buffer = ''    
    elif buffer == '1215':
        print('chegou: e')
        buffer = ''    
    elif buffer == '1212':
        print('chegou: f')
        buffer = ''    
    elif buffer == '1213':
        print('chegou: g')
        buffer = ''    
    