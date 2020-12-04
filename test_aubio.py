from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import os

audioFiles = []
path = 'wav_stego/audio in/audio in/'
figureCounter = 0

for paths, dirs, files in os.walk(path):
    audioFiles = files


for wavFile in audioFiles:
    if figureCounter < 20:
        sampling_rate, samples = wavfile.read(path+wavFile)
        figs, axs = plt.subplots(2, 1, constrained_layout=True)
        figs.suptitle(wavFile)
        # print(len(samples))
        # if samples.mean()/20000 < 0.01 and samples.mean()/-20000 < 0.01:
        #     pass
        # else:
        #     print("Probable spread-spectrum detected in " + wavFile)
        axs[0].plot(samples)
        axs[0].set_xlabel('Samples')
        axs[0].set_ylabel('Amplitude')
        pxx, freq, t, cax = axs[1].specgram(samples, Fs=sampling_rate)
        axs[1].set_xlabel('Time (s)')
        axs[1].set_ylabel('Frequency (Hz)')
        figs.colorbar(cax)
        figureCounter += 1
    else:
        break
    
plt.show()
