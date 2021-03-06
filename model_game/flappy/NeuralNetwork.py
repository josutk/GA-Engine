from tensorflow.keras import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

class NeuralNetwork:

    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(units=26, input_shape=(13,) , name='input', activation='sigmoid'))
        self.model.add(Dense(units=1, input_shape=(26, ), activation='sigmoid', name='out'))
        sgd = SGD()
        self.model.compile(loss="mse", optimizer=sgd, metrics=["accuracy"])
    
    def get_model(self):
        return self.model