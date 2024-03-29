import numpy as np
import pyaudio as pa 
import struct 
import crc_ifsc

global channel
channel = int(input('Canal? [1/2]'))

CHUNK = 1024 * 2
FORMAT = pa.paInt16
CHANNELS = 1 # não alterar
RATE = 44100

p = pa.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input=True,
    output=False,
    frames_per_buffer=CHUNK
)

buffer = ''
last_slot = ''

if channel == 1:
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
elif channel == 2:
    freqs_meaning = {
        '56': '0',
        '58': '1',
        '60': '2',
        '62': '3',
        '64': '4',
        '66': '5',
        '68': '6',
        '70': '7',
        '72': '8',
        '74': '9',
        '76': 'a',
        '78': 'b',
        '80': 'c',
        '82': 'd',
        '84': 'e',
        '86': 'f',
        '88': 'g', # esc
        '90': 'h'  # reset rx buffer 
    }

while 1:
    data = stream.read(CHUNK)
    data_int = struct.unpack(str(CHUNK) + 'h', data)
    data_fft = np.abs(np.fft.fft(data_int))*2/(11000*CHUNK)
    f_bins = data_fft[20:91] > 1

    # Obtem o slot mais baixo e salva no buffer
    if len(np.where(f_bins)[0]) > 0:  

        # Se achou mais de uma freq ao mesmo tempo, e tais no canal 2
        #   Pegue a segunda freq
        # Senão
        #   Pegue a primeira mesmo
        if len(np.where(f_bins)[0]) > 1 and channel == 2:
            slot = int(np.where(f_bins)[0][1]) + 20
        else:
            slot = int(np.where(f_bins)[0][0]) + 20    

        if channel == 1 and slot not in [20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54]:
            slot = -1 # não deixa reconhecer uma frequencia que não está no seu canal
        elif channel == 2 and slot not in [56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90]:
            slot = -1 # não deixa reconhecer uma frequencia que não está no seu canal        

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

    if len(buffer) > 2:
        try:
            fcs = crc_ifsc.CRC16(bytes.fromhex(buffer))
            if fcs.check_crc():                    
                mensagem = bytes.fromhex(buffer[:-4]).decode('UTF-8') # retira 2 bytes (4 simbolos) do CRC 
                print(mensagem, end = "",  flush=True)
                buffer = ''
        except:
            pass
    
