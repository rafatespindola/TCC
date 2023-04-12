import numpy as np
import pyaudio as pa 
import struct 
import matplotlib.pyplot as plt 

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
    '52': 'g', # esc
    '54': 'h'  # reset rx buffer 
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

buffer = ''
last_slot = ''

while 1:
    data = stream.read(CHUNK)
    data_int = struct.unpack(str(CHUNK) + 'h', data)
    data_fft = np.abs(np.fft.fft(data_int))*2/(11000*CHUNK)
    f_bins = data_fft[0:90] > 1

    # Obtem o slot mais baixo e salva no buffer
    if len(np.where(f_bins)[0]) > 0:
        slot = int(np.where(f_bins)[0][0])
        if str(slot) in freqs_meaning.keys() and last_slot != slot:
            last_slot = slot
            if freqs_meaning[str(slot)] not in 'gh':
                # Se for de 0 a f, adicione
                buffer += freqs_meaning[str(slot)]
            elif freqs_meaning[str(slot)] == 'g':
                # Se for 'g', então é ESC.
                # Repita o último caractere
                if len(buffer) > 0:
                    buffer += buffer[-1]
            elif freqs_meaning[str(slot)] == 'h':
                # Se for 'h', então é pra limpar o buffer
                # Serve para manter sincronismo
                buffer = ''

    if len(buffer) == 2:
        try:
            print(bytes.fromhex(buffer).decode('ascii'))
            buffer = ''
        except:
            pass
    
