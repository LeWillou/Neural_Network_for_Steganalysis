from tensorflow.keras.optimizers import Adam
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
import numpy as np
import sys
import check_peaks
import check_phase
import check_samples
import os
import check_signal_to_noise_ratio
import check_odd_numbers

directories = []
audio_files = []

original_path = '../wav_stego/audio in'

for dirpaths, dirnames, filenames in os.walk(original_path):
    audio_files.append(filenames)

opt = Adam(lr=0.1, beta_1=0.9, beta_2=0.999)

model = Sequential()
model.add(Dense(250, input_shape = [5, 199], activation='relu'))
model.add(Dense(120, activation='relu'))
model.add(Flatten())
#model.add(Dropout(rate=0.25))
model.add(Dense(5, activation='softmax'))
model.load_weights('nn_weights_5000_5_parameters.h5')
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

audio_in = [1, 0, 0, 0, 0]
echo_hiding = [0, 1, 0, 0, 0]
lsb = [0, 0, 1, 0, 0]
phase_coding = [0, 0, 0, 1, 0]
spread_spectrum = [0, 0, 0, 0, 1]


for audio_file in audio_files[0]:
    file_freq_peaks = check_peaks.check_peaks(original_path + '/' + audio_file)
    file_phases = check_phase.check_phase(original_path + '/' + audio_file)
    file_samples_peaks = check_samples.check_peaks_sample(original_path + '/' + audio_file)
    file_signal_to_noise = check_signal_to_noise_ratio.check_signal_to_noise(original_path + '/' + audio_file)
    file_odd_numbers = check_odd_numbers.check_odd_numbers(original_path + '/' + audio_file)
    input_data = [file_freq_peaks, file_phases, file_samples_peaks, file_signal_to_noise, file_odd_numbers]
    input_data = np.array([input_data], dtype=np.float32)
    # print(input_data.shape)
    predicted_results = model.predict(input_data)

    real_result = np.array(audio_in)

    if real_result.argmax() == predicted_results.argmax():
        counter += 1
        print('Found ! ' + str(counter) + ' found so far..., making it ' + str((counter/64)*100) + '% correct.')
    else:
        print('Did not find the good one... ' + str(counter) + ' found so far, making it ' + str((counter/64)*100) + '% correct.')
        if predicted_results.argmax() == 1:
            print('Echo Hiding found')
        elif predicted_results.argmax() == 2:
            print('LSB found')
        elif predicted_results.argmax() == 3:
            print('Phase Coding found')
        elif predicted_results.argmax() == 4:
            print('Spread Spectrum found')

