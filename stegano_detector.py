from tensorflow.keras.optimizers import Adam
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
import numpy as np
import sys
import check_peaks
import check_phase
import check_samples

opt = Adam(lr=0.1, beta_1=0.9, beta_2=0.999)

model = Sequential()
model.add(Dense(250, input_shape = [3, 99], activation='relu'))
model.add(Dense(120, activation='relu'))
model.add(Flatten())
#model.add(Dropout(rate=0.25))
model.add(Dense(5, activation='softmax'))
model.load_weights('nn_weights_3_parameters_low_lr.h5')
model.compile(optimizer = opt, loss='categorical_crossentropy')

audio_file = sys.argv[1]

print(audio_file)

file_freq_peaks = check_peaks.check_peaks(sys.argv[1])
file_phases = check_phase.check_phase(sys.argv[1])
file_samples_peaks = check_samples.check_peaks_sample(sys.argv[1])

input_data = [file_freq_peaks, file_phases, file_samples_peaks]

input_data = np.array([input_data], dtype=np.float32)

print(model.predict(input_data))
