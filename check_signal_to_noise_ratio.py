from scipy.io import wavfile
from scipy import stats
import numpy as np
import os


def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)


def check_signal_to_noise(audio_file):

    sampling_rate, samples= wavfile.read(audio_file)
    
    for_size = int(len(samples)/199)

    signal_to_noise_array = []

    for i in range(199):
        signal_to_noise_array.append(signaltonoise(samples[i * for_size: (i+1) * for_size]))

    return signal_to_noise_array