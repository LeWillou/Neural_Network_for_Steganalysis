from scipy.io import wavfile
from scipy import signal
import numpy as np
import os


def check_peaks(audioFiLe):
    '''Returns mean of frequency peaks in given wav file'''
    sampling_rate, samples = wavfile.read(audioFiLe)
    
    spectre = np.fft.fft(samples)
    
    peaks_index_array, _ = signal.find_peaks(spectre, prominence=10000)
    for_size = int(peaks_index_array.size/199)
    mean_peaks_array = []

    for i in range(199):
        mean_peaks_array.append(np.abs(spectre[peaks_index_array[i*for_size:(i+1)*for_size]]).mean())

    return mean_peaks_array

