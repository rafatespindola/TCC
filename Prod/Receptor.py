import wave
import numpy as np
import struct
import matplotlib.pyplot as plt

# Caracteristicas do audio
audiofilename = "tx_data.wav"
audiofile = wave.open(audiofilename, 'r')
fileSize = audiofile.getparams()[3]  # n
sample_rate = audiofile.getparams()[2]  # fs
time_len = fileSize / sample_rate  # tx

audio = []
for i in range(fileSize):
    x = audiofile.readframes(1)
    audio.append(struct.unpack('h', x))

audio_list = []
for i in audio:
    audio_list.append(i[0])

# w = Window
w_frames = 2400
w_chunk = 0
w_graph = 1


# fft = sinal na frequencia
# threshold = limite mínimo que o sinal deve ter para ser considerado válido
def get_freq_from_fft(fft, threshold):
    freqs = [f for f in fft if f >= threshold]
    freqs_filtered = []

    freqs_rounded = []
    print(freqs_filtered)
    # frequency_list = [1000.0, 1300.0, 1600.0, 1900.0, 2200.0, 2500.0, 2800.0, 3100.0]
    for i in freqs_filtered:
        if 950 < i < 1050:
            freqs_rounded.append(1000)
        elif 1250 < i < 1350:
            freqs_rounded.append(1300)
        elif 1550 < i < 1650:
            freqs_rounded.append(1600)
        elif 1850 < i < 1950:
            freqs_rounded.append(1900)
        elif 1150 < i < 2050:
            freqs_rounded.append(2200)
        elif 2450 < i < 2550:
            freqs_rounded.append(2500)
        elif 2750 < i < 2850:
            freqs_rounded.append(2800)
        elif 3050 < i < 3150:
            freqs_rounded.append(3100)

    if len(freqs_rounded) == 0:
        return []
    elif len(freqs_rounded) == 1:
        return freqs_filtered

    print(freqs_rounded)

    i = 1
    ans = [] # answer
    ans.append(freqs_rounded[0])
    while i <= len(freqs_rounded):
        if freqs_rounded[i] != freqs_rounded[i-1]:
            ans.append(freqs_rounded[i])
        i += 1

    return ans



while w_chunk * w_frames < fileSize:
    w_audio_t = audio_list[w_chunk * w_frames:(w_chunk + 1) * w_frames]
    w_fileSize = len(w_audio_t)
    w_freq = np.fft.fftfreq(w_fileSize) * sample_rate
    mascara = w_freq > 0
    w_fft_calculo = 2.0 * np.abs(np.fft.fft(w_audio_t) / w_fileSize)

    plt.figure(w_graph)
    plt.title("Sinal da fft- Com Zoom")
    plt.plot(w_freq, w_fft_calculo)
    plt.show()

    w_graph += 1
    w_chunk += 1

    # # Obtem valores em número a partir do grafico/w_fft_calculo
    print(get_freq_from_fft(w_freq, 1500))
