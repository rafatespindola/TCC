from Subcamada import Subcamada
import numpy as np
import pyaudio


class Physic(Subcamada):

    def __init__(self):
        Subcamada.__init__(self, None, 3)
        self.disable_timeout()
        self.last_symbol = ''

    def envia(self, quadro):
        bytes_hex = quadro.data.hex()
        bytes_hex_esc = self.do_not_repeat_symbol(bytes_hex)
        print('psc.envia: bytes_hex_esc: ' + bytes_hex_esc)
        self.from_hex_to_audio(bytes_hex_esc)

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
        #                 0      1      2      3      4      5      6      7
        frequency_list = [430.0, 452.0, 474.0, 496.0, 516.0, 538.0, 562.0, 580.0, 
        #                 8      9      a      b      c      d      e      f
                          604.0, 624.0, 646.0, 668.0, 689.0, 711.0, 733.0, 752.0,
        #                 g(esc)                  
                          774.0]
        duration = 0.2  # in seconds
        sampling_rate = 44100.0 
        symbol_list = self.generate_symbols(frequency_list, duration, sampling_rate)
        audio = self.genetate_audio(symbol_list, bytes_hex_esc)
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

    def genetate_audio(self, symbol_list, sequence):
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
            elif s == 'g':
                audio += symbol_list[16].tobytes() 

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








