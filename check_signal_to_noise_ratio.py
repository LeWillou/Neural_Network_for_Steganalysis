from scipy.io import wavfile
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
import os


def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)


sampling_rate, samples= wavfile.read('wav_stego/Spread Spectrum/Spread Spectrum/bagpipe.wav')

print(signaltonoise(samples))