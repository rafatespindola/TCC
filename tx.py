import numpy as np
import pyaudio
import crc_ifsc

last_symbol = ''
channel = int(input('Canal? [1/2] '))

def envia(quadro):
        bytes_hex = quadro.data.hex()
        hex_esc = do_not_repeat_symbol(bytes_hex)
        esc_reset = insert_reset_symbol(hex_esc)
        from_hex_to_audio(esc_reset)

def do_not_repeat_symbol(bytes_hex):
    global last_symbol
    bytes_hex_esc = ''
    for b in bytes_hex:
        if b == last_symbol:
            bytes_hex_esc += 'g' # ESC
            last_symbol = 'g'
        else:
            bytes_hex_esc += b
            last_symbol = b
    print('esc: ' + bytes_hex_esc)

    return bytes_hex_esc

def from_hex_to_audio(bytes_hex_esc):
    global channel
    if channel == 1:
        #                 Explicação: representação_em_hexa[slot_freq]
        #                 0[20]  1[22]  2[24]  3[26]  4[28]  5[30]  6[32]  7[34]
        frequency_list = [430.0, 474.0, 516.0, 562.0, 604.0, 646.0, 689.0, 733.0,
        #                 8[36]  9[38]  a[40]  b[42]  c[44]  d[46]  e[48]  f[50]    
                        774.0, 819.0, 861.0, 905.0, 948.0, 991.0, 1033.0,1076.0, 
        #                 g(esc)[52] repete o último simbolo                 
                        1120.0, 
        #                 h(reset)[54] reseta o buffer do rx
                        1161.0]
    elif channel == 2:
        #                 Explicação: representação_em_hexa[slot_freq]
        #                 0[56]  1[58]  2[60]  3[62]  4[64]  5[66]  6[68]  7[70]
        frequency_list = [1205.0,1249.0,1292.0,1335.0,1378.0,1422.0,1465.0,1508.0,
        #                 8[72]  9[74]  a[76]  b[78]  c[80]  d[82]  e[84]  f[86]    
                            1550.0,1594.0,1637.0,1680.0,1723.0,1766.0,1808.0,1852.0,
        #                 g(esc)[88] repete o último simbolo                 
                            1896.0, 
        #                 h(reset)[90] reseta o buffer do rx
                            1938.0]
    
    duration = 0.2  # in seconds. Até 0.8 já funcionou bem.
    sampling_rate = 44100.0 
    symbol_list = generate_symbols(frequency_list, duration, sampling_rate)
    audio = generate_audio(symbol_list, bytes_hex_esc)
    play(audio)
    

def play(audio):
    p = pyaudio.PyAudio()
    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=44100,
                    output=True)

    stream.write(audio)
    stream.stop_stream()
    stream.close()
    p.terminate()    

def generate_audio(symbol_list, sequence):
    audio = b''
    for s in sequence:
        audio += symbol_list[int(s, 18)].tobytes()
    return audio

def generate_symbols(frequency_list, duration, sampling_rate):
    symbol_list= []
    t = int(duration * sampling_rate)  
    template = np.arange(t) / sampling_rate 
    x = np.linspace(0, np.pi, t)
    mask = np.sin(x)
    for freq in frequency_list:
        sinal = np.sin(template * freq * 2 * np.pi)
        symbol = np.multiply(sinal, mask).astype(np.float32)
        symbol_list.append(symbol)

    return symbol_list

# Define o frame
def insert_reset_symbol(hex_esc):
    return 'h' + hex_esc + 'h'
 
# Insere o CRC
def msg_with_crc(msg):
    c = crc_ifsc.CRC16(msg)
    return c.gen_crc()


while 1: 
    linha = input('>>> ')

    crc_chunk = 5

    while linha:
        l = linha[:crc_chunk]
        data_bytes = l.encode('UTF-8')
        msg_crc = msg_with_crc(data_bytes)
        bytes_hex = msg_crc.hex()
        hex_esc = do_not_repeat_symbol(bytes_hex)
        esc_reset = insert_reset_symbol(hex_esc)
        from_hex_to_audio(esc_reset)
        linha = linha[crc_chunk:]
