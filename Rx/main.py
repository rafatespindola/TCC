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

#Initial condition
buffer = ''
last_symbol = -1
last_buffer = ''
times = 0
candidate = ''
required_times = 1

while 1:
    data = stream.read(CHUNK)
    data_int = struct.unpack(str(CHUNK) + 'h', data)
    data_fft = np.abs(np.fft.fft(data_int))*2/(11000*CHUNK)
    f_bins = data_fft[0:90] > 1

    print(f_bins[1:90])

    # if f_bins[20]:
    #     if candidate == '0':
    #         times += 1 
    #     else:
    #         times = 1    
    #         candidate = '0'
        
    #     if times > required_times and last_symbol != 20 and candidate == '0':
    #         buffer += '0'
    #         last_symbol = 20
    # elif f_bins[22]:
    #     if candidate == '1':
    #         times = times + 1 
    #     else:
    #         times = 1    
    #         candidate = '1'
        
    #     if times > required_times and last_symbol != 22  and candidate == '1':
    #         buffer += '1'
    #         last_symbol = 22
    # elif f_bins[24]:
    #     if candidate == '2':
    #         times += 1 
    #     else:
    #         times = 1    
    #         candidate = '2'
        
    #     if times > required_times and last_symbol != 24 and candidate == '2':
    #         buffer += '2'
    #         last_symbol = 24
    # elif f_bins[26]:
    #     if candidate == '3':
    #         times += 1 
    #     else:
    #         times = 1    
    #         candidate = '3'
        
    #     if times > required_times and last_symbol != 26 and candidate == '3':
    #         buffer += '3'
    #         last_symbol = 26
    # elif f_bins[28]:
    #     if candidate == '4':
    #         times += 1 
    #     else:
    #         times = 1    
    #         candidate = '4'
        
    #     if times > required_times and last_symbol != 28  and candidate == '4':
    #         buffer += '4'
    #         last_symbol = 28
    # elif f_bins[30]:
    #     if candidate == '5':
    #         times += 1 
    #     else:
    #         times = 1    
    #         candidate = '5'
        
    #     if times > required_times and last_symbol != 30 and candidate == '5':
    #         buffer += '5'
    #         last_symbol = 30
    # elif f_bins[32]:
    #     if candidate == '6':
    #         times += 1 
    #     else:
    #         times = 1    
    #         candidate = '6'
        
    #     if times > required_times and last_symbol != 32 and candidate == '6':
    #         buffer += '6'
    #         last_symbol = 32 
    # elif f_bins[34]:
    #     if candidate == '7':
    #         times += 1 
    #     else:
    #         times = 1    
    #         candidate = '7'
        
    #     if times > required_times and last_symbol != 34 and candidate == '7':
    #         buffer += '7'
    #         last_symbol = 34

    # if f_bins[20] and last_symbol != 20:
    #     buffer += '0'
    #     last_symbol = 20
    # elif f_bins[22] and last_symbol != 22:
    #     buffer += '1'
    #     last_symbol = 22
    # elif f_bins[24] and last_symbol != 24:
    #     buffer += '2'
    #     last_symbol = 24
    # elif f_bins[26] and last_symbol != 26:
    #     buffer += '3'
    #     last_symbol = 26
    # elif f_bins[28] and last_symbol != 28:
    #     buffer += '4'
    #     last_symbol = 28
    # elif f_bins[30] and last_symbol != 30:
    #     buffer += '5'
    #     last_symbol = 30
    # elif f_bins[32] and last_symbol != 32:
    #     buffer += '6'
    #     last_symbol = 32
    # elif f_bins[34] and last_symbol != 34:
    #     buffer += '7'
    #     last_symbol = 34
        
    if len(buffer) > 0 and buffer != last_buffer: 
        print(buffer)
        last_buffer = buffer


    if buffer in ('1201', '5645'):
        print('chegou: a')
        buffer = ''
    elif buffer in ('1202', '5646'):
        print('chegou: b')
        buffer = ''
    elif buffer in ('1203', '5647'):
        print('chegou: c')
        buffer = ''
    elif buffer in ('1210', '5654'):
        print('chegou: d')
        buffer = ''    
    elif buffer in ('1215', '5651'):
        print('chegou: e')
        buffer = ''    
    elif buffer in ('1212', '5656'):
        print('chegou: f')
        buffer = ''    
    elif buffer in ('1213', '5657'):
        print('chegou: g')
        buffer = ''    
    elif buffer in ('1264', '5620'):
        print('chegou: h')
        buffer = ''
    elif buffer in ('1265', '5621'):
        print('chegou: i')
        buffer = ''
    elif buffer in ('1262', '5626'):
        print('chegou: j')
        buffer = ''
    elif buffer in ('1267', '5623'):
        print('chegou: k')
        buffer = ''
    elif buffer in ('1230', '5674'):
        print('chegou: l')
        buffer = ''
    elif buffer in ('1231', '5675'):
        print('chegou: m')
        buffer = ''
    elif buffer in ('1232', '5676'):
        print('chegou: n')
        buffer = ''
    elif buffer in ('1237', '5673'):
        print('chegou: o')
        buffer = ''
    elif buffer in ('1304', '5740'):
        print('chegou: p')
        buffer = ''
    elif buffer in ('1301', '5745'):
        print('chegou: q')
        buffer = ''
    elif buffer in ('1302', '5746'):
        print('chegou: r')
        buffer = ''
    elif buffer in ('1303', '5747'):
        print('chegou: s')
        buffer = ''
    elif buffer in ('1310', '5754'):
        print('chegou: t')
        buffer = ''
    elif buffer in ('1315', '5751'):
        print('chegou: u')
        buffer = ''
    elif buffer in ('1312', '5756'):
        print('chegou: v')
        buffer = ''
    elif buffer in ('1313', '5757'):
        print('chegou: w')
        buffer = ''
    elif buffer in ('1321', '5765'):
        print('chegou: y')
        buffer = ''
    elif buffer in ('1320', '5764'):
        print('chegou: x')
        buffer = ''
    elif buffer in ('1326', '5762'):
        print('chegou: z')
        buffer = ''
    elif buffer in ('0204', '4640'):
        print('chegou: espaço')
        buffer = ''

