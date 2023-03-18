import numpy as np 
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

# fig,ax = plt.subplots()
# x = np.arange(0,2*CHUNK,2)
# line, = ax.plot(x, np.random.rand(CHUNK),'g') # 'g' green
# ax.set_ylim(-40000,40000)
# ax.ser_xlim = (0,CHUNK)
# fig.show()

while 1:
    data = stream.read(CHUNK)
    dataInt = struct.unpack(str(CHUNK) + 'h', data)
    # line.set_ydata(dataInt)
    # fig.canvas.draw()
    # fig.canvas.flush_events()
    print(dataInt)