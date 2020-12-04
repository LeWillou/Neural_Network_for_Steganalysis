from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
import numpy as np
import pandas as pd

data = np.load('dataset_training_320.npy', allow_pickle=True)

parameter1 = []

for i in range(len(data[0][0])):
    parameter1.append(data[0][0][i])

parameter2 = []

for i in range(len(data[1][0])):
    parameter2.append(data[1][0][i])

parameter3 = []

for i in range(len(data[3][0])):
    parameter3.append(data[3][0][i])

output = []

for i in range(len(data[2][0])):
    output.append(data[2][0][i])

parameter1 = np.array(parameter1)
parameter2 = np.array(parameter2)
parameter3 = np.array(parameter3)

input_data = []

for i in range(len(parameter1)):
    transition_array = [parameter1[i], parameter2[i], parameter3[i]]
    input_data.append(transition_array)

input_data = np.array(input_data, dtype=np.float32)

#print(input_data[0][0])

# input_data = [parameter1, parameter2]
# input_data = np.array(input_data)

output = np.array(output)

# print(output.shape)

#print(parameter1.shape)
#print(type(input_data[1][0][1]))
#print(data[1])

opt = Adam(lr=0.001, beta_1=0.9, beta_2=0.999)

model = Sequential()

model.add(Dense(250, input_shape = [3, 99], activation='relu'))
model.add(Dense(120))
model.add(Flatten())
# model.add(Dropout(rate=0.25))
model.add(Dense(5, activation='softmax'))
model.compile(optimizer = opt, loss='categorical_crossentropy')
model.fit(input_data, output, epochs=5000, verbose=1)


# model.add(Dropout(rate=0.25))

model.save_weights('nn_weights_two_parameters.h5')

#soft max à la fin
