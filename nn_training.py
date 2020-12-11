'''Modules import'''
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
import numpy as np
# import pandas as pd



'''--------------------------------------------------------------------------------------------'''
'''                                      Dataset uploading                                     '''
'''--------------------------------------------------------------------------------------------'''


data = np.load('dataset_training_5000_5_parameters.npy', allow_pickle=True)

# dataset_training_320 uses 3 parameters for the 5*64 audio files, dataset_training uses 2 
# parameters for 5*1000 audio files, dataset_training_wrong uses 3 parameters for 5*1000 
# audio files


'''--------------------------------------------------------------------------------------------'''
'''                                  Dataset formating part                                    '''
'''--------------------------------------------------------------------------------------------'''


parameter1 = []

for i in range(len(data[0][0])):
    parameter1.append(data[0][0][i])

parameter2 = []

for i in range(len(data[1][0])):
    parameter2.append(data[1][0][i])

parameter3 = []

for i in range(len(data[3][0])):
    parameter3.append(data[3][0][i])

parameter4 = []

for i in range(len(data[4][0])):
    parameter4.append(data[4][0][i])

parameter5 = []

for i in range(len(data[5][0])):
    parameter5.append(data[5][0][i])

output = []

for i in range(len(data[2][0])):
    output.append(data[2][0][i])

parameter1 = np.array(parameter1)
parameter2 = np.array(parameter2)
parameter3 = np.array(parameter3)
parameter4 = np.array(parameter4)
parameter5 = np.array(parameter5)

input_data = []

for i in range(len(parameter1)):
    transition_array = [parameter1[i], parameter2[i], parameter3[i], parameter4[i], parameter5[i]]
    input_data.append(transition_array)

input_data = np.array(input_data, dtype=np.float32)

# print(parameter3)

# input_check = pd.DataFrame(parameter3)

# for i in range(len(parameter3)):
#     if np.isnan(parameter3[i]).all():
#         print('Problem detected at ' + str(i))

# print(parameter3[1][0])

# input_data = [parameter1, parameter2]
# input_data = np.array(input_data)

output = np.array(output)


'''--------------------------------------------------------------------------------------------'''
'''                                     Neural network part                                    '''
'''--------------------------------------------------------------------------------------------'''


opt = Adam(lr=0.0001, beta_1=0.9, beta_2=0.999)

model = Sequential()

model.add(Flatten())
model.add(Dense(250, input_shape = [5, 199], activation='relu'))
model.add(Dense(120, activation='relu'))
model.add(Dropout(rate=0.2))
model.add(Dense(5, activation='softmax'))
model.compile(optimizer = opt, loss='categorical_crossentropy')
model.fit(input_data, output, epochs=1200, verbose=1)


model.save_weights('nn_weights_5000_5_parameters.h5')

# tanh activation
# features engineering