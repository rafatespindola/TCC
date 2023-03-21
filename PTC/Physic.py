import sys
from Subcamada import Subcamada
from Quadro import Quadro
import logging  # https://realpython.com/python-logging/
import wave
import struct
from functions import FSK_generate_symbols, generate_audio
from playsound import playsound


class Transmissor(Subcamada):

    def __init__(self):
        Subcamada.__init__(self, None, 3)
        self.disable_timeout()
        logging.basicConfig(level=logging.WARNING)  # DEBUG, INFO, WARNING, ERROR, CRITICAL

    def envia(self, quadro):
        logging.info('Tx.recebe(): Recebeu quadro do Codificador')
        self.fromFreqToAudio(quadro)

    def fromFreqToAudio(self, quadro):
        # The sampling rate of the analog to digital convert
        sampling_rate = 48000.0
        # frequency of symbols to generate
        #                 00     01     10     11     00     01     10     11
        #                 0      1      2      3      4      5      6      7
        frequency_list = [689.0, 733.0, 430.0, 474.0, 516.0, 562.0, 604.0, 646.0]
        # symbol length in seconds
        duration = 0.09  # seconds
        # amplitude of the audio
        amplitude = 16000

        audiofile = "tx_data.wav"

        # generate symbols
        symbol = FSK_generate_symbols(frequency_list, duration, sampling_rate)

        # data to modulate
        # data = [0, 1]

        # import random
        # data = [random.getrandbits(1) for i in range(100)]
        # data = []
        # from Codificador import State
        # for i in quadro.freq_seq:
        #     if i == State.f1:
        #         data.append(0)
        #         data.append(0)
        #     elif i == State.f2:
        #         data.append(0)
        #         data.append(1)
        #     elif i == State.f3:
        #         data.append(1)
        #         data.append(0)
        #     elif i == State.f4:
        #         data.append(1)
        #         data.append(1)
        #     elif i == State.f5:
        #         data.append(0)
        #         data.append(0)
        #     elif i == State.f6:
        #         data.append(0)
        #         data.append(1)
        #     elif i == State.f7:
        #         data.append(1)
        #         data.append(0)
        #     elif i == State.f8:
        #         data.append(1)
        #         data.append(1)

        # generate an audio based on data fsk
        audio = generate_audio(quadro.freq_seq, symbol)

        # file properties
        nframes = len(audio)
        comptype = "NONE"
        compname = "not compressed"
        nchannels = 1
        sampwidth = 2

        # open wave file
        wav_file = wave.open(audiofile, 'w')
        # set properties
        wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

        # write the audio to file
        for s in audio:
            wav_file.writeframes(struct.pack('h', int(s * amplitude)))

        wav_file.close()

        playsound('tx_data.wav')


