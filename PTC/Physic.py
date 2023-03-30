from Subcamada import Subcamada
from Quadro import Quadro
import wave
import struct
from functions import FSK_generate_symbols, generate_audio
from playsound import playsound
import numpy as np


class Physic(Subcamada):

    def __init__(self):
        Subcamada.__init__(self, None, 3)
        self.disable_timeout()

    def envia(self, quadro):
        bytes_hex = quadro.data.hex()
        bytes_hex_esc = self.do_not_repeat_symbol(bytes_hex)
        self.from_hex_to_audio(bytes_hex_esc)

    def do_not_repeat_symbol(self, bytes_hex):
        last = ''
        bytes_hex_esc = ''
        for b in bytes_hex:
            if b == last:
                bytes_hex_esc += 'g' # ESC
            else:
                bytes_hex_esc += b
        return bytes_hex_esc

    def from_hex_to_audio(self):
        #                 0      1      2      3      4      5      6      7
        frequency_list = [430.0, 452.0, 474.0, 496.0, 516.0, 538.0, 562.0, 580.0, 
        #                 8      9      a      b      c      d      e      f
                          604.0, 624.0, 646.0, 668.0, 689.0, 711.0, 733.0, 752.0,
        #                 g (esc)                  
                          774.0]
        duration = 0.2  # in seconds
        sampling_rate = 44100.0 
        symbol = self.fsk_generate_symbols(frequency_list, duration, sampling_rate)
        # a partir dos simbolos, montar o audio com o teste_no_wav

    def fsk_generate_symbols(self, frequency_list, duration, sampling_rate):
        symbols = []
        t = int(duration * sampling_rate)  # 480
        template = np.arange(t) / sampling_rate  #
        x = np.linspace(0, np.pi, t)
        mask = np.sin(x)
        for freq in frequency_list:
            sinal = np.sin(template * freq * 2 * np.pi)
            symbol = np.multiply(sinal, mask)
            symbols.append(symbol)
        return symbols








