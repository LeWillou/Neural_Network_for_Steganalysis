from scipy.io import wavfile
from scipy import signal
import numpy as np
import os

'''Try comparing with total length / segment length'''
def check_odd_numbers(audioFile):
    sampling_rate, samples = wavfile.read(audioFile)
    for_size = int(samples.size/199)

    odd_numbers_counter = []

    for i in range(199):
        odd_numbers_counter.append(len([num for num in samples[i * for_size:(i+1) * for_size] if num%2 == 1]))

    return odd_numbers_counter

# print(check_peaks_sample('stegano/Echo Hiding/blues.00001.wav'))