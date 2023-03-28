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
last_simbol = -1
last_buffer = ''

while 1:
    data = stream.read(CHUNK)
    data_int = struct.unpack(str(CHUNK) + 'h', data)
    data_fft = np.abs(np.fft.fft(data_int))*2/(11000*CHUNK)
    f_bins = data_fft[0:50] > 1


    if f_bins[32] and last_simbol != 32:
        buffer += '0'
        last_simbol = 32
    elif f_bins[34] and last_simbol != 34:
        buffer += '1'
        last_simbol = 34
    elif f_bins[20] and last_simbol != 20:
        buffer += '2'
        last_simbol = 20
    elif f_bins[22] and last_simbol != 22:
        buffer += '3'
        last_simbol = 22
    elif f_bins[24] and last_simbol != 24:
        buffer += '4'
        last_simbol = 24
    elif f_bins[26] and last_simbol != 26:
        buffer += '5'
        last_simbol = 26
    elif f_bins[28] and last_simbol != 28:
        buffer += '6'
        last_simbol = 28
    elif f_bins[30] and last_simbol != 30:
        buffer += '7'
        last_simbol = 30
        
    if len(buffer) > 0 and buffer != last_buffer: 
        print(buffer)
        last_buffer = buffer


    if buffer == '1201' or buffer == '5645':
        print('chegou: a')
        buffer = ''
    elif buffer == '1202' or buffer == '5646':
        print('chegou: b')
        buffer = ''
    elif buffer == '1203' or buffer == '5647':
        print('chegou: c')
        buffer = ''
    elif buffer == '1210' or buffer == '5654':
        print('chegou: d')
        buffer = ''    
    elif buffer == '1215' or buffer == '5651':
        print('chegou: e')
        buffer = ''    
    elif buffer == '1212' or buffer == '5656':
        print('chegou: f')
        buffer = ''    
    elif buffer == '1213' or buffer == '5657':
        print('chegou: g')
        buffer = ''    
    elif buffer == '1264' or buffer == '5620':
        print('chegou: h')
        buffer = ''
    elif buffer == '1265' or buffer == '5621':
        print('chegou: i')
        buffer = ''
    elif buffer == '1262' or buffer == '5626':
        print('chegou: j')
        buffer = ''
    elif buffer == '1267' or buffer == '5623':
        print('chegou: k')
        buffer = ''
    elif buffer == '1230' or buffer == '5674':
        print('chegou: l')
        buffer = ''
    elif buffer == '1231' or buffer == '5675':
        print('chegou: m')
        buffer = ''
    elif buffer == '1232' or buffer == '5676':
        print('chegou: n')
        buffer = ''
    elif buffer == '1237' or buffer == '5673':
        print('chegou: o')
        buffer = ''
    elif buffer == '1304' or buffer == '5740':
        print('chegou: p')
        buffer = ''
    elif buffer == '1301' or buffer == '5745':
        print('chegou: q')
        buffer = ''
    elif buffer == '1302' or buffer == '5746':
        print('chegou: r')
        buffer = ''
    elif buffer == '1303' or buffer == '5747':
        print('chegou: s')
        buffer = ''
    elif buffer == '1310' or buffer == '5754':
        print('chegou: t')
        buffer = ''
    elif buffer == '1315' or buffer == '5751':
        print('chegou: u')
        buffer = ''
    elif buffer == '1312' or buffer == '5756':
        print('chegou: v')
        buffer = ''
    elif buffer == '1313' or buffer == '5757':
        print('chegou: w')
        buffer = ''
    elif buffer == '1321' or buffer == '5765':
        print('chegou: y')
        buffer = ''
    elif buffer == '1320' or buffer == '5764':
        print('chegou: x')
        buffer = ''
    elif buffer == '1326' or buffer == '5762':
        print('chegou: z')
        buffer = ''
    elif buffer == '0204' or buffer == '4640':
        print('chegou: espaço')
        buffer = ''

