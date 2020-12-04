from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import os

audioFiles = []
path = 'wav_stego/Spread Spectrum/Spread Spectrum/'
figureCounter = 0

for paths, dirs, files in os.walk(path):
    audioFiles = files


for wavFile in audioFiles:
    if figureCounter >= 20:
        plt.show()
        figureCounter = 0
    sampling_rate, samples = wavfile.read(path+wavFile)
    sampling_rate_input, samples_input = wavfile.read('wav_stego/audio in/audio in/' + wavFile)
    figs, axs = plt.subplots(1, 1, constrained_layout=True)
    figs.suptitle(wavFile)

    spectre = np.fft.fft(samples)
    freq = np.fft.fftfreq(samples.size, 1/sampling_rate)
    mask = freq>0

    spectre_input = np.fft.fft(samples_input)
    freq_input = np.fft.fftfreq(samples_input.size, 1/sampling_rate_input)
    mask_input = freq_input>0


    # if samples.mean()/20000 < 0.01 and samples.mean()/-20000 < 0.01:
    #     pass
    # else:
    #     print("Probable spread-spectrum detected in " + wavFile)

    axs.plot(freq[mask], np.abs(spectre[mask]), label='Stego')
    axs.plot(freq_input[mask_input], np.abs(spectre_input[mask_input]), label='Original')
    
    axs.set_xlabel('Frequency')
    axs.set_ylabel('Amplitude')
    axs.legend()
    figureCounter += 1



# sampling_rate, samples = wavfile.read(path+'bagpipe.wav')
# sampling_rate_input, samples_input = wavfile.read('wav_stego/audio in/audio in/' + 'bagpipe.wav')
# figs, axs = plt.subplots(1, 1, constrained_layout=True)
# figs.suptitle('bagpipe')
# # print('bagpipe.wav')
# # print('Stego : ')
# # print(samples.mean())
# # print('Original : ')
# # print(samples_input.mean())
# # print('\n')
# # print(str((samples.mean()/samples_input.mean()) * 100) + '%')
# # if samples.mean()/20000 < 0.01 and samples.mean()/-20000 < 0.01:
# #     pass
# # else:
# #     print("Probable spread-spectrum detected in " + wavFile)

# spectre = np.fft.fft(samples)
# freq = np.fft.fftfreq(samples.size, 1/sampling_rate)
# mask = freq>0

# spectre_input = np.fft.fft(samples_input)
# freq_input = np.fft.fftfreq(samples_input.size, 1/sampling_rate_input)
# mask_input = freq_input>0

# axs.plot(freq[mask], np.abs(spectre[mask]), label='Spread Spectrum')
# axs.plot(freq_input[mask_input], np.abs(spectre_input[mask_input]), label='Original')
# axs.set_xlabel('Frequence')
# axs.set_ylabel('Amplitude')
# axs.legend()

# # print(int(len(samples_input)/100))
# # for i in range(100):
# #     transition_array = []
# #     for l in range(int(len(samples_input)/100)):
# #         transition_array.append(samples[figureCounter+i])
# #     print(sum(transition_array)/len(transition_array))
# #     figureCounter += int(len(samples_input)/100)

# print(np.abs(spectre[mask]))
# print(np.abs(spectre_input[mask_input]))
# print(freq[mask])


# # for sample in samples_input:
# #     if figureCounter <= 20:
# #         print(sample)
# #         figureCounter += 1
# #     else:
# #         break

plt.show()
