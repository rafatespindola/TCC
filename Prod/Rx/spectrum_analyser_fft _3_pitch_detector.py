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
    if f_bins[8] == True:
        print('58')
    elif f_bins[9] == True:
        print('65')
    elif f_bins[10] == True:
        print('72')        
    elif f_bins[11] == True:
        print('79')                
    elif f_bins[12] == True:
        print('12')
    elif f_bins[13] == True:
        print('13')
    elif f_bins[14] == True:
        print('300')        
    elif f_bins[15] == True:
        print('323')
    elif f_bins[16] == True:
        print('345')
    elif f_bins[17] == True:
        print('366')        
    elif f_bins[18] == True:
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
    elif f_bins[28] == True:
        print('28')
    elif f_bins[29] == True:
        print('29')                                              
    elif f_bins[30] == True:
        print('30')
    elif f_bins[31] == True:
        print('31')
    elif f_bins[32] == True:
        print('32')
    elif f_bins[33] == True:
        print('33')        
    elif f_bins[34] == True:
        print('34')
    elif f_bins[35] == True:
        print('35')
    elif f_bins[36] == True:
        print('36')        
    elif f_bins[37] == True:
        print('37')
    elif f_bins[38] == True:
        print('38')
    elif f_bins[39] == True:
        print('39')         
    elif f_bins[40] == True:
        print('40')
    elif f_bins[41] == True:
        print('41')
    elif f_bins[42] == True:
        print('42')
    elif f_bins[43] == True:
        print('43')        
    elif f_bins[44] == True:
        print('44')
    elif f_bins[45] == True:
        print('45')
    elif f_bins[46] == True:
        print('46')        
    elif f_bins[47] == True:
        print('47')
    elif f_bins[48] == True:
        print('38')
    elif f_bins[49] == True:
        print('49')                 
    
