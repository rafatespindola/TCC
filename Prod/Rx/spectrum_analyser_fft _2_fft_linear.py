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


fig, ax1 = plt.subplots()
x_fft = np.linspace(0, RATE, CHUNK) # linspace(start, end, num_pontos)
# x = np.arange(0,2*CHUNK,2) 
# line, = ax.plot(x, np.random.rand(CHUNK),'r')
line_fft, = ax1.plot(x_fft, np.random.rand(CHUNK), 'b')
# ax.set_ylim(-32000,32000)
# ax.ser_xlim = (0,CHUNK)
ax1.set_xlim(20,RATE/2)
ax1.set_ylim(0,10)
fig.show()


while 1:
    data = stream.read(CHUNK) # Pega um pedaco
    dataInt = struct.unpack(str(CHUNK) + 'h', data) # Transforma em vetor de int
    # line.set_ydata(dataInt)
    line_fft.set_ydata(np.abs(np.fft.fft(dataInt))*2/(11000*CHUNK))
    f_bins = line_fft.get_ydata()[0:100]>1
    print(f_bins)
    if f_bins[18] == True:
        print('387')
    elif f_bins[19] == True:
        print('410') 
    else:
        print('Nada')
    fig.canvas.draw()
    fig.canvas.flush_events()

