import numpy as np
import os
from scipy.io import wavfile
import check_phase
import check_peaks
import check_samples
import check_signal_to_noise_ratio


directories = []
audio_files = []

original_path = 'stegano/'

for dirpaths, dirnames, filenames in os.walk(original_path):
    directories.append(dirnames)
    audio_files.append(filenames)

dataset = np.array([])

file_freq_peaks = []
file_samples_peaks = []
file_phases = []
file_types = []
file_samples_signal_noise = []

counter = 0

for directory_name in directories[0]:
    for audio_file in audio_files[1]:
        
        file_freq_peaks.append(check_peaks.check_peaks(original_path + directory_name + '/' + audio_file))
        file_phases.append(check_phase.check_phase(original_path + directory_name + '/' + audio_file))
        file_samples_peaks.append(check_samples.check_peaks_sample(original_path + directory_name + '/' + audio_file))
        file_samples_signal_noise.append(check_signal_to_noise_ratio.check_signal_to_noise(original_path + directory_name + '/' + audio_file))
        if 'audio in' in directory_name:
            file_types.append([1, 0, 0, 0, 0])
        elif 'Echo Hiding' in directory_name:
            file_types.append([0, 1, 0, 0, 0])
        elif 'LSB' in directory_name:
            file_types.append([0, 0, 1, 0, 0])
        elif 'Phase Coding' in directory_name:
            file_types.append([0, 0, 0, 1, 0])
        elif 'Spread Spectrum' in directory_name:
            file_types.append([0, 0, 0, 0, 1])
        
        counter += 1
        percentage_done = (counter/(len(directories[0]) * len(audio_files[1])))*100

        # file_datas.append(datas_array)
        print(directory_name + '/' + audio_file + " done! (" + str(percentage_done) + " %)")


dataset = np.array([[file_freq_peaks], [file_phases], [file_types], [file_samples_peaks], [file_samples_signal_noise]])

np.save('dataset_training_5000_signal_noise_2', dataset)
