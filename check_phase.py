from scipy.io import wavfile
from scipy import signal, fft
import numpy as np
import os


def check_phase(audioFile):
    '''Returns phases of given wav file'''
    sampling_rate, samples = wavfile.read(audioFile)
    spectre = np.fft.fft(samples[0:200])
    phase = np.angle(spectre, deg=True)

    freq = np.fft.fftfreq(200, 1/sampling_rate)
    mask = freq>0
    
    return phase[mask]

