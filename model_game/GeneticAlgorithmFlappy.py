from genetic_model.GeneticAlgorithm import GeneticAlgorithmTemplate
from tensorflow.keras import Sequential
from tensorflow.python.keras.layers import Dense
import numpy as np
import random

class GeneticAlgorithmFlappy(GeneticAlgorithmTemplate):

    def __init__(self, population_size):
        self.population_size = population_size
        self.generation = []

    def population(self):
        for idx in range(population_size):
            model = Sequential()
            model.add(Dense(units=6, input_shape=(3,) , name='inpute'))
            model.add(Dense(units=1, input_shape=(6,), activation='sigmoid', name='out'))
            self.generation.append(model)
        
    def fitness(self, scores):
        np_scores = np.array(scores)
        indexs = np_scores.argsort()[-self.population_size/2:][::-1]
        return indexs

    def crossover(self):
        weights1 = self.population[idx1].get_weights()
        weights2 = self.population[idx2].get_weights()
        newWeight1 = weights2 
        newWeight2 = weights1
        weights1[0] = newWeight1[0]
        weights2[0] = newWeight2[0]
        return np.asarray([weights1, weights2])

    def mutation(self, weights):
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                if random.random() > 0.7:
                    if random.randint(0, 5000) % 2 == 0:
                        mutation = random.uniform(-0.8, 0.8)
                        weights[i][j] += mutation
                    else:
                        mutation = random.uniform(-0.8, 0.8)
                        weights[i][j] -= mutation
        return weights
