from scipy.io import wavfile
from scipy import signal
import numpy as np
import os


def check_peaks_sample(audioFile):
    sampling_rate, samples = wavfile.read(audioFile)
    peaks_index_array, _ = signal.find_peaks(samples, prominence=10000)
    for_size = int(peaks_index_array.size/99)
    mean_peaks_array = []

    for i in range(99):
        mean_peaks_array.append(np.abs(samples[peaks_index_array[i*for_size:(i+1)*for_size]]).mean())

    return mean_peaks_array

# print(check_peaks_sample('stegano/Echo Hiding/blues.00001.wav'))