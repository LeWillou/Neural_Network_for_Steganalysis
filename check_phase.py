from scipy.io import wavfile
from scipy import signal, fft
import numpy as np
import os


def check_phase(audioFile):
    '''Returns phases of given wav file'''
    sampling_rate, samples = wavfile.read(audioFile)
    spectre = np.fft.fft(samples[0:400])
    phase = np.angle(spectre, deg=True)

    freq = np.fft.fftfreq(400, 1/sampling_rate)
    mask = freq>0

    # for_size = int(len(phase)/200)

    # mean_phases_array = []

    # for i in range(200):
    #     mean_phases_array.append(np.abs(phase[i*for_size:(i+1)*for_size].mean()))

    
    return phase[mask]

