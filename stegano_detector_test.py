from tensorflow.keras.optimizers import Adam
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
import numpy as np
import sys
import check_peaks
import check_phase
import check_samples
import os

directories = []
audio_files = []

for dirpaths, dirnames, filenames in os.walk('wav_stego/'):
    directories.append(dirnames)
    audio_files.append(filenames)

opt = Adam(lr=0.1, beta_1=0.9, beta_2=0.999)

model = Sequential()
model.add(Dense(250, input_shape = [2, 99], activation='relu'))
model.add(Dense(120, activation='relu'))
model.add(Flatten())
#model.add(Dropout(rate=0.25))
model.add(Dense(5, activation='softmax'))
model.load_weights('nn_weights_two_parameters.h5')
model.compile(optimizer = opt, loss='categorical_crossentropy')

# audio_file = sys.argv[1]

# print(audio_file)

# file_freq_peaks = check_peaks.check_peaks(sys.argv[1])
# file_phases = check_phase.check_phase(sys.argv[1])
# #file_samples_peaks = check_samples.check_peaks_sample(sys.argv[1])

# input_data = [file_freq_peaks, file_phases]

# input_data = np.array([input_data], dtype=np.float32)

# print(model.predict(input_data))

counter = 0

for directory_name in directories[0]:
    for audio_file in audio_files[1]:
        file_freq_peaks = check_peaks.check_peaks('wav_stego/' + directory_name + '/' + audio_file)
        file_phases = check_phase.check_phase('wav_stego/' + directory_name + '/' + audio_file)
        input_data = [file_freq_peaks, file_phases]
        input_data = np.array([input_data], dtype=np.float32)
        print(input_data.shape)
        predicted_results = model.predict(input_data)
        real_result = []
        if 'audio in' in directory_name:
            real_result.append([1, 0, 0, 0, 0])
        elif 'Echo Hiding' in directory_name:
            real_result.append([0, 1, 0, 0, 0])
        elif 'LSB' in directory_name:
            real_result.append([0, 0, 1, 0, 0])
        elif 'Phase Coding' in directory_name:
            real_result.append([0, 0, 0, 1, 0])
        elif 'Spread Spectrum' in directory_name:
            real_result.append([0, 0, 0, 0, 1])

        real_result = np.array(real_result)

        if (real_result == predicted_results).all():
            print('Good type found ! ' + str(counter) + ' found so far...')
            counter += 1
        else:
            print('Did not find the good one... ' + str(counter) + ' found so far, making it ' + str((counter/5000)*100) + '% correct.')