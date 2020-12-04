from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import os

audioFiles = []
path = 'wav_stego/Phase Coding/Phase Coding/'
figureCounter = 0

for paths, dirs, files in os.walk(path):
    audioFiles = files


for wavFile in audioFiles:
    if figureCounter == 20:
        plt.show()
        figureCounter = 0
    sampling_rate, samples = wavfile.read(path+wavFile)
    sampling_rate_input, samples_input = wavfile.read('wav_stego/audio in/audio in/' + wavFile)
    figs, axs = plt.subplots(1, 1, constrained_layout=True)
    figs.suptitle(wavFile)
    print(wavFile)
    print('Stego : ')
    print(samples.mean())
    print('Original : ')
    print(samples_input.mean())
    print('\n')
    # print(str((samples.mean()/samples_input.mean()) * 100) + '%')
    # if samples.mean()/20000 < 0.01 and samples.mean()/-20000 < 0.01:
    #     pass
    # else:
    #     print("Probable spread-spectrum detected in " + wavFile)
    axs.plot(samples, label=wavFile+' Stego')
    axs.plot(samples_input, label='Original ' + wavFile)
    axs.set_xlabel('Samples')
    axs.set_ylabel('Amplitude')
    axs.legend()
    figureCounter += 1

plt.show()
