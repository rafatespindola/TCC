import numpy as np
import pyaudio as pa 
import struct 
import matplotlib.pyplot as plt 


        # #                 Explicação: representação_em_hexa[slot_freq]
        # #                 0[20]  1[22]  2[24]  3[26]  4[28]  5[30]  6[32]  7[34]
        # frequency_list = [430.0, 474.0, 516.0, 562.0, 604.0, 646.0, 689.0, 733.0,
        # #                 8[36]  9[38]  a[40]  b[42]  c[44]  d[46]  e[48]  f[50]    
        #                   774.0, 819.0, 861.0, 905.0, 948.0, 991.0, 1033.0,1076.0, 
        # #                 g(esc)[52]                  
        #                   1120.0]

freqs_meaning = {
    '20': '0',
    '22': '1',
    '24': '2',
    '26': '3',
    '28': '4',
    '30': '5',
    '32': '6',
    '34': '7',
    '36': '8',
    '38': '9',
    '40': 'a',
    '42': 'b',
    '44': 'c',
    '46': 'd',
    '48': 'e',
    '50': 'f',
    '52': 'g'
}

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
last_slot = ''
# last_symbol = -1
# last_buffer = ''
# times = 0
# candidate = ''
# required_times = 1

while 1:
    data = stream.read(CHUNK)
    data_int = struct.unpack(str(CHUNK) + 'h', data)
    data_fft = np.abs(np.fft.fft(data_int))*2/(11000*CHUNK)
    f_bins = data_fft[0:90] > 1

    # Obtem o slot mais baixo/grave sempre
    if len(np.where(f_bins)[0]) > 0:
        slot = int((np.where(f_bins)[0][0] - 20) / 2)
        if slot >= 0 and last_slot != slot:
            last_slot = slot
            buffer = freqs_meaning[str(slot)]
            print(buffer)

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
        
    # if len(buffer) > 0 and buffer != last_buffer: 
    #     print(buffer)
    #     last_buffer = buffer


    # if buffer in ('1201', '5645'):
    #     print('chegou: a')
    #     buffer = ''
    # elif buffer in ('1202', '5646'):
    #     print('chegou: b')
    #     buffer = ''
    # elif buffer in ('1203', '5647'):
    #     print('chegou: c')
    #     buffer = ''
    # elif buffer in ('1210', '5654'):
    #     print('chegou: d')
    #     buffer = ''    
    # elif buffer in ('1215', '5651'):
    #     print('chegou: e')
    #     buffer = ''    
    # elif buffer in ('1212', '5656'):
    #     print('chegou: f')
    #     buffer = ''    
    # elif buffer in ('1213', '5657'):
    #     print('chegou: g')
    #     buffer = ''    
    # elif buffer in ('1264', '5620'):
    #     print('chegou: h')
    #     buffer = ''
    # elif buffer in ('1265', '5621'):
    #     print('chegou: i')
    #     buffer = ''
    # elif buffer in ('1262', '5626'):
    #     print('chegou: j')
    #     buffer = ''
    # elif buffer in ('1267', '5623'):
    #     print('chegou: k')
    #     buffer = ''
    # elif buffer in ('1230', '5674'):
    #     print('chegou: l')
    #     buffer = ''
    # elif buffer in ('1231', '5675'):
    #     print('chegou: m')
    #     buffer = ''
    # elif buffer in ('1232', '5676'):
    #     print('chegou: n')
    #     buffer = ''
    # elif buffer in ('1237', '5673'):
    #     print('chegou: o')
    #     buffer = ''
    # elif buffer in ('1304', '5740'):
    #     print('chegou: p')
    #     buffer = ''
    # elif buffer in ('1301', '5745'):
    #     print('chegou: q')
    #     buffer = ''
    # elif buffer in ('1302', '5746'):
    #     print('chegou: r')
    #     buffer = ''
    # elif buffer in ('1303', '5747'):
    #     print('chegou: s')
    #     buffer = ''
    # elif buffer in ('1310', '5754'):
    #     print('chegou: t')
    #     buffer = ''
    # elif buffer in ('1315', '5751'):
    #     print('chegou: u')
    #     buffer = ''
    # elif buffer in ('1312', '5756'):
    #     print('chegou: v')
    #     buffer = ''
    # elif buffer in ('1313', '5757'):
    #     print('chegou: w')
    #     buffer = ''
    # elif buffer in ('1321', '5765'):
    #     print('chegou: y')
    #     buffer = ''
    # elif buffer in ('1320', '5764'):
    #     print('chegou: x')
    #     buffer = ''
    # elif buffer in ('1326', '5762'):
    #     print('chegou: z')
    #     buffer = ''
    # elif buffer in ('0204', '4640'):
    #     print('chegou: espaço')
    #     buffer = ''

