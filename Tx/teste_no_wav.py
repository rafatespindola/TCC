import numpy as np
import pyaudio

p = pyaudio.PyAudio()

volume = 0.5  # range [0.0, 1.0]
fs = 44100  # sampling rate, Hz, must be integer
duration = 1  # in seconds, may be float
f = 440.0  # sine frequency, Hz, may be float

# generate samples
samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs))

t = int(duration * fs) 
x = np.linspace(0, np.pi, t)
mask = np.sin(x)
sinal_fade = np.multiply(samples, mask).astype(np.float32)

# per @yahweh comment explicitly convert to bytes sequence
output_bytes = (volume * sinal_fade).tobytes()

print('formatooo: ')
print(type(output_bytes))

output_bytes += output_bytes

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively)
stream.write(output_bytes)

stream.stop_stream()
stream.close()

p.terminate()
