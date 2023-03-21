import numpy as np
from scipy.io.wavfile import write
from playsound import playsound


info = "12015646564756545651565656575620"
info_array = list(info)

print(info_array)

# Samples per second
sps = 44100

# Frequency / pitch of the sine wave
freq_hz = 440.0

# Duration
duration_s = 0.2
frames = duration_s * sps # counting how many frames for a note
each_sample_number = np.arange(duration_s * sps)



for i in range(len(info_array)):
    if(info_array[i] == "0"):
        freq_hz = 689.0 # 32
    elif(info_array[i] == "1"):
        freq_hz = 733.0 # 34
    elif(info_array[i] == "2"):
        freq_hz = 430.0 # 20
    elif(info_array[i] == "3"):
        freq_hz = 474.0 # 22
    elif(info_array[i] == "4"):
        freq_hz = 516.0 # 24
    elif(info_array[i] == "5"):
        freq_hz = 562.0 # 26 
    elif(info_array[i] == "6"):
        freq_hz = 604.0 # 28
    elif(info_array[i] == "7"):
        freq_hz = 646.0 # 30

    # added fall off feature
    waveform = (((frames - each_sample_number) / frames)**0.5) * np.sin(np.pi + 2 * np.pi * each_sample_number * freq_hz / sps)*0.3

    #The line above and below this one make an individual note.
    waveform_integers = np.int16(waveform * 32767)

    if(i == 0):
        waveformc = waveform_integers
        print(waveformc)
    else:
        waveformc = np.append(waveformc, waveform_integers, axis=None)

write('song.wav', sps, waveformc)
print("DONE")
playsound('song.wav')