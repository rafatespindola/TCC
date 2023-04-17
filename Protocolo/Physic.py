from Subcamada import Subcamada
import numpy as np
import pyaudio


class Physic(Subcamada):

    def __init__(self):
        Subcamada.__init__(self, None, 3)
        self.disable_timeout()
        self.last_symbol = ''
        self.channel = 1

    def envia(self, quadro):
        bytes_hex = quadro.data.hex()
        hex_esc = self.do_not_repeat_symbol(bytes_hex)
        esc_reset = self.insert_reset_symbol(hex_esc)
        self.from_hex_to_audio(esc_reset)

    def do_not_repeat_symbol(self, bytes_hex):
        bytes_hex_esc = ''
        for b in bytes_hex:
            if b == self.last_symbol:
                bytes_hex_esc += 'g' # ESC
                self.last_symbol = 'g'
            else:
                bytes_hex_esc += b
                self.last_symbol = b
        return bytes_hex_esc

    def from_hex_to_audio(self, bytes_hex_esc):
        
        if self.channel == 1:
            #                 Explicação: representação_em_hexa[slot_freq]
            #                 0[20]  1[22]  2[24]  3[26]  4[28]  5[30]  6[32]  7[34]
            frequency_list = [430.0, 474.0, 516.0, 562.0, 604.0, 646.0, 689.0, 733.0,
            #                 8[36]  9[38]  a[40]  b[42]  c[44]  d[46]  e[48]  f[50]    
                            774.0, 819.0, 861.0, 905.0, 948.0, 991.0, 1033.0,1076.0, 
            #                 g(esc)[52] repete o último simbolo                 
                            1120.0, 
            #                 h(reset)[54] reseta o buffer do rx
                            1161.0]
        elif self.channel == 2:
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
        symbol_list = self.generate_symbols(frequency_list, duration, sampling_rate)
        audio = self.generate_audio(symbol_list, bytes_hex_esc)
        self.play(audio)

    def play(self, audio):
        p = pyaudio.PyAudio()
        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=44100,
                        output=True)

        # play. May repeat with different volume values (if done interactively)
        stream.write(audio)
        stream.stop_stream()
        stream.close()
        p.terminate()    

    def generate_audio(self, symbol_list, sequence):
        audio = b''
        for s in sequence:
            if s == '0':
                audio += symbol_list[0].tobytes()
            elif s == '1':
                audio += symbol_list[1].tobytes()
            elif s == '2':
                audio += symbol_list[2].tobytes()
            elif s == '3':
                audio += symbol_list[3].tobytes()
            elif s == '4':
                audio += symbol_list[4].tobytes()
            elif s == '5':
                audio += symbol_list[5].tobytes()
            elif s == '6':
                audio += symbol_list[6].tobytes()
            elif s == '7':
                audio += symbol_list[7].tobytes()
            elif s == '8':
                audio += symbol_list[8].tobytes()
            elif s == '9':
                audio += symbol_list[9].tobytes()
            elif s == 'a':
                audio += symbol_list[10].tobytes()
            elif s == 'b':
                audio += symbol_list[11].tobytes()
            elif s == 'c':
                audio += symbol_list[12].tobytes()
            elif s == 'd':
                audio += symbol_list[13].tobytes()
            elif s == 'e':
                audio += symbol_list[14].tobytes()
            elif s == 'f':
                audio += symbol_list[15].tobytes()
            elif s == 'g': # esc
                audio += symbol_list[16].tobytes() 
            elif s == 'h': # reset
                audio += symbol_list[17].tobytes()
        return audio

    def generate_symbols(self, frequency_list, duration, sampling_rate):
        symbol_list= []
        t = int(duration * sampling_rate)  # 480
        template = np.arange(t) / sampling_rate  #
        x = np.linspace(0, np.pi, t)
        mask = np.sin(x)
        for freq in frequency_list:
            sinal = np.sin(template * freq * 2 * np.pi)
            symbol = np.multiply(sinal, mask).astype(np.float32)
            symbol_list.append(symbol)
        return symbol_list

    def insert_reset_symbol(self, hex_esc):
        # 'h' é o reset symbol
        # A cada 2X simbolos, 2x porque 1 byte possui 2 símbolos,
        # é inserido um reset de buffer do rx

        count = 0
        x = 5 # a cada quantos bytes um reset
        esc_reset = 'h' # uma comunicação sempre começa com um reset symbol

        for i in hex_esc:
            esc_reset += i
            count += 1
            if count == (2*x):
                esc_reset += 'h' # reset  
                count = 0

        print(esc_reset)

        return esc_reset








